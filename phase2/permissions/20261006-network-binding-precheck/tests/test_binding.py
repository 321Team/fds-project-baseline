import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1] / "capture-network-binding-precheck.py"
spec = importlib.util.spec_from_file_location("binding", SOURCE)
binding = importlib.util.module_from_spec(spec)
spec.loader.exec_module(binding)
IID = "i-1234567890abcdef0"
PROFILE = f"arn:aws:iam::{binding.ACCOUNT}:instance-profile/relay/FDS-Relay"
ROLE = f"arn:aws:iam::{binding.ACCOUNT}:role/FDS-Relay"
KEY = f"arn:aws:kms:{binding.REGION}:{binding.ACCOUNT}:key/12345678-1234-1234-1234-123456789abc"


class Runner:
    def __init__(self):
        self.calls, self.overrides = [], {}
        self.instance = {"InstanceId": IID, "State": {"Name": "running"},
            "InstanceType": "t3.medium", "ImageId": "ami-079a2667364cee804",
            "SourceDestCheck": False, "Tags": [{"Key": k, "Value": v} for k, v in binding.TAGS.items()]}

    def __call__(self, command, **kwargs):
        self.calls.append(command)
        service, op = command[1:3]
        if op not in binding.READ_OPERATIONS.get(service, set()):
            raise AssertionError("Non-read operation executed")
        if kwargs.get("timeout") != 60 or kwargs["env"]["AWS_MAX_ATTEMPTS"] != "1":
            raise AssertionError("Missing timeout/retry bound")
        if command[command.index("--region") + 1] != binding.REGION:
            raise AssertionError("Unexpected region")
        answer = self.overrides.get(op)
        if callable(answer):
            answer = answer(command)
        if answer is None:
            answer = self.default(command)
        if isinstance(answer, Exception):
            raise answer
        if isinstance(answer, str):
            return subprocess.CompletedProcess(command, 254, "", f"An error occurred ({answer}) when calling the operation")
        return subprocess.CompletedProcess(command, 0, json.dumps(answer), "")

    def default(self, command):
        op = command[2]
        if op == "get-caller-identity":
            return {"Account": binding.ACCOUNT, "Arn": binding.ROOT}
        if op == "describe-document":
            return "InvalidDocument"
        if op == "list-documents":
            return {"DocumentIdentifiers": []}
        if op == "get-role":
            if command[command.index("--role-name") + 1] == "FDS-Network-Operator":
                return "NoSuchEntity"
            return {"Role": {"RoleName": "FDS-Relay", "Arn": ROLE}}
        if op == "list-role-policies":
            return {"PolicyNames": []}
        if op == "list-attached-role-policies":
            return {"AttachedPolicies": []}
        if op == "describe-instances":
            return {"Reservations": [{"OwnerId": binding.ACCOUNT, "Instances": [self.instance]}]}
        if op == "describe-instance-information":
            return {"InstanceInformationList": [{"InstanceId": IID, "PingStatus": "Online", "AgentVersion": "test"}]}
        if op == "get-instance-profile":
            return {"InstanceProfile": {"Arn": PROFILE, "Roles": [{"RoleName": "FDS-Relay", "Arn": ROLE}]}}
        if op == "describe-volumes":
            return {"Volumes": [{"VolumeId": "vol-1234567890abcdef0", "Encrypted": True,
                                 "KmsKeyId": KEY, "Attachments": [{"InstanceId": IID}]}]}
        if op == "describe-key":
            return {"KeyMetadata": {"Arn": KEY, "AWSAccountId": binding.ACCOUNT, "Enabled": True}}
        if op == "get-key-policy":
            return {"Policy": "{}"}
        raise AssertionError(op)


class BindingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.helper, _ = binding.dependencies()
        self.runner = Runner()
        self.cap = self.helper.Capture(Path(self.temp.name), self.runner)

    def collect(self, relay=None):
        return binding.collect(self.cap, self.helper, relay)

    def test_inventory_never_selects_or_reads_profile(self):
        result = self.collect()
        self.assertEqual(result["SelectedRelay"], "NOT_SELECTED_EVEN_IF_ONE_MATCH")
        self.assertEqual(result["RelayInventory"][0]["InstanceId"], IID)
        command = next(c for c in self.runner.calls if c[2] == "describe-instances")
        self.assertEqual(len(json.loads(command[command.index("--filters") + 1])), 3)
        self.assertNotIn("get-instance-profile", [c[2] for c in self.runner.calls])
        self.assertEqual(result["Document"]["Inventory"], "NOT_IN_COMPLETE_SELF_SESSION_LIST")

    def test_wrong_root_stops_before_resource_read(self):
        self.runner.overrides["get-caller-identity"] = {"Account": binding.ACCOUNT, "Arn": ROLE}
        with self.assertRaises(binding.Stop):
            self.collect()
        self.assertEqual(len(self.runner.calls), 1)

    def test_invalid_document_list_contradiction_is_review_required(self):
        self.runner.overrides["list-documents"] = {"DocumentIdentifiers": [{"Name": self.helper.DOCUMENT, "Owner": binding.ACCOUNT, "DocumentType": "Session"}]}
        self.assertEqual(self.collect()["Document"]["Inventory"], "LISTED_BUT_UNAVAILABLE_REVIEW_REQUIRED")

    def test_access_denied_is_not_absent(self):
        self.runner.overrides["describe-document"] = "AccessDeniedException"
        with self.assertRaises(self.helper.AwsError):
            self.collect()

    def test_network_role_unexpected_error_is_not_absent(self):
        self.runner.overrides["get-role"] = "AccessDenied"
        with self.assertRaises(self.helper.AwsError):
            self.collect()

    def test_pagination_bounded_and_no_false_absence(self):
        self.runner.overrides["list-documents"] = lambda c: {"DocumentIdentifiers": [], "NextToken": str(len(self.runner.calls))}
        with self.assertRaises(binding.Stop):
            self.collect()
        self.assertEqual(sum(c[2] == "list-documents" for c in self.runner.calls), 5)

    def test_pagination_repeated_token_stops(self):
        self.runner.overrides["list-documents"] = {"DocumentIdentifiers": [], "NextToken": "same"}
        with self.assertRaises(binding.Stop):
            self.collect()

    def test_document_owner_mismatch_stops(self):
        self.runner.overrides["list-documents"] = {"DocumentIdentifiers": [{"Name": "other", "Owner": "000000000001", "DocumentType": "Session"}]}
        with self.assertRaises(binding.Stop):
            self.collect()

    def test_inventory_unexpected_owner_stops(self):
        self.runner.overrides["describe-instances"] = {"Reservations": [{"OwnerId": "000000000001", "Instances": [self.runner.instance]}]}
        with self.assertRaises(binding.Stop):
            self.collect()

    def test_inventory_tag_mismatch_stops(self):
        self.runner.instance["Tags"] = []
        with self.assertRaises(binding.Stop):
            self.collect()

    def test_selected_exact_id_no_max_results(self):
        result = self.collect(IID)
        self.assertEqual(result["SelectedDependencies"]["Agent"]["PingStatus"], "Online")
        command = next(c for c in self.runner.calls if c[2] == "describe-instances")
        self.assertNotIn("--max-results", command)
        self.assertEqual(command[command.index("--instance-ids") + 1], IID)
        self.assertEqual(result["SelectedDependencies"]["Profile"]["State"], "ABSENT")

    def test_selected_wrong_id_stops(self):
        with self.assertRaises(binding.Stop):
            self.collect("i-1234567890abcdef1")

    def test_selected_agent_wrong_id_stops(self):
        self.runner.overrides["describe-instance-information"] = {"InstanceInformationList": [{"InstanceId": "i-1234567890abcdef1"}]}
        with self.assertRaises(binding.Stop):
            self.collect(IID)

    def test_profile_and_ebs_exact_dependencies_only(self):
        self.runner.instance["IamInstanceProfile"] = {"Arn": PROFILE}
        self.runner.instance["BlockDeviceMappings"] = [{"Ebs": {"VolumeId": "vol-1234567890abcdef0"}}]
        result = self.collect(IID)["SelectedDependencies"]
        self.assertEqual(result["Profile"]["Arn"], PROFILE)
        self.assertEqual(result["EBSKeys"][0]["Arn"], KEY)
        self.assertEqual(sum(c[2] == "get-key-policy" for c in self.runner.calls), 1)

    def test_profile_wrong_account_stops(self):
        self.runner.instance["IamInstanceProfile"] = {"Arn": PROFILE.replace(binding.ACCOUNT, "000000000001")}
        with self.assertRaises(binding.Stop):
            self.collect(IID)

    def test_volume_wrong_attachment_stops(self):
        self.runner.instance["BlockDeviceMappings"] = [{"Ebs": {"VolumeId": "vol-1234567890abcdef0"}}]
        self.runner.overrides["describe-volumes"] = {"Volumes": [{"VolumeId": "vol-1234567890abcdef0", "Attachments": []}]}
        with self.assertRaises(binding.Stop):
            self.collect(IID)

    def test_truncated_role_list_stops(self):
        self.runner.overrides["get-role"] = {"Role": {"RoleName": "FDS-Network-Operator", "Arn": ROLE.replace("FDS-Relay", "FDS-Network-Operator")}}
        self.runner.overrides["list-role-policies"] = {"PolicyNames": [], "IsTruncated": True, "Marker": "next"}
        with self.assertRaises(binding.Stop):
            self.collect()

    def test_timeout_partial_raw_is_preserved(self):
        self.runner.overrides["list-documents"] = subprocess.TimeoutExpired("aws", 60, output=b"partial")
        with self.assertRaises(self.helper.AwsError):
            self.collect()
        self.assertEqual(next(Path(self.temp.name).glob("*-partial-stdout.txt")).read_bytes(), b"partial")

    def test_write_and_simulate_operations_blocked(self):
        for service, op in (("iam", "put-role-policy"), ("iam", "simulate-custom-policy"), ("ssm", "start-session"), ("ec2", "reboot-instances")):
            with self.assertRaises(self.helper.Stop):
                self.cap.call("excluded", service, op)
        self.assertEqual(self.runner.calls, [])

    def test_dependency_hash_mismatch_before_execution(self):
        with patch.object(binding, "POLICY_HASH", "0" * 64):
            with self.assertRaises(binding.Stop):
                binding.dependencies()

    def test_offline_zero_aws_calls_manifest_and_private_files(self):
        with patch("subprocess.run", side_effect=AssertionError("AWS called")) as aws:
            with contextlib.redirect_stdout(io.StringIO()):
                rc = binding.main(["--offline", "--output-parent", self.temp.name])
            aws.assert_not_called()
        self.assertEqual(rc, 0)
        directory = next(Path(self.temp.name).glob("fds-network-binding-precheck-*"))
        self.assertTrue((directory / "SHA256SUMS").exists())
        self.assertEqual(json.loads((directory / "summary.json").read_text())["APPLY_READINESS"], "NOT_ASSESSED")
        if os.name == "posix":
            self.assertTrue(all(p.stat().st_mode & 0o777 == 0o600 for p in directory.iterdir()))

    def test_manifest_failure_never_prints_complete(self):
        real_dependencies = binding.dependencies
        def loaded():
            helper, paths = real_dependencies()
            helper.Capture.manifest = lambda self: (_ for _ in ()).throw(OSError("manifest unavailable"))
            return helper, paths
        stdout, stderr = io.StringIO(), io.StringIO()
        with patch.object(binding, "dependencies", loaded), contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            self.assertEqual(binding.main(["--offline", "--output-parent", self.temp.name]), 1)
        self.assertNotIn("OFFLINE_PLAN=COMPLETE", stdout.getvalue())
        self.assertIn("manifest persistence failed", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
