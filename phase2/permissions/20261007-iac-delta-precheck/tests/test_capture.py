import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import Mock, patch

HERE = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("iac_delta", HERE / "capture-iac-delta-precheck.py")
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)
SOURCE = HERE.parent / "20261006-iac-fixed-inputs"


def result(value=None, error=None):
    return subprocess.CompletedProcess([], 254 if error else 0,
                                       json.dumps(value) if value is not None else "",
                                       f"An error occurred ({error}) when calling the GetRole operation" if error else "")


class CaptureTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_mutation_and_content_reads_rejected_before_cli(self):
        runner = Mock()
        cap = M.Capture(self.path, runner)
        for service, operation in [("iam", "put-role-policy"), ("s3api", "put-bucket-policy"),
                                   ("s3api", "get-object"), ("ssm", "get-parameter"),
                                   ("ec2", "run-instances")]:
            with self.subTest(operation=operation), self.assertRaises(M.Stop):
                cap.call("forbidden", service, operation)
        runner.assert_not_called()

    def test_wrong_identity_stops_after_one_call(self):
        runner = Mock(return_value=result({"Account": M.ACCOUNT, "Arn": M.IAC}))
        with self.assertRaises(M.Stop):
            M.run_capture(M.Capture(self.path, runner), {})
        self.assertEqual(runner.call_count, 1)

    def test_pinned_source_tamper_precedes_aws(self):
        copy = self.path / "source"
        shutil.copytree(SOURCE, copy)
        target = copy / next(iter(M.SOURCE_HASHES))
        target.write_bytes(target.read_bytes() + b" ")
        with self.assertRaises(M.Stop):
            M.load_source(copy)
        self.assertEqual(len(M.load_source(SOURCE)), 3)

    def test_access_denied_is_never_absence(self):
        cap = M.Capture(self.path, Mock(return_value=result(error="AccessDenied")))
        with self.assertRaises(M.AwsError):
            cap.optional("role", "iam", "get-role", {"NoSuchEntity"}, "--role-name", "FDS-IaC-Operator")

    def test_only_typed_absence_is_accepted(self):
        cap = M.Capture(self.path, Mock(return_value=result(error="NoSuchEntity")))
        self.assertEqual(cap.optional("role", "iam", "get-role", {"NoSuchEntity"}, "--role-name", "FDS-IaC-Operator")["CaptureState"], "ABSENT")

    def test_timeout_is_bounded_preserves_partial_and_is_not_absence(self):
        runner = Mock(side_effect=subprocess.TimeoutExpired("aws", 40, output=b"partial", stderr=b"partial-error"))
        with self.assertRaises(M.AwsError):
            M.Capture(self.path, runner).optional("role", "iam", "get-role", {"NoSuchEntity"}, "--role-name", "FDS-IaC-Operator")
        self.assertEqual(runner.call_count, 2)
        self.assertEqual((self.path / "001-role-attempt1.stdout").read_bytes(), b"partial")
        self.assertEqual((self.path / "002-role-attempt2.stderr").read_bytes(), b"partial-error")

    def test_cli_keeps_pagination_private_files_and_credential_env_unprinted(self):
        runner = Mock(return_value=result({"PolicyNames": []}))
        M.Capture(self.path, runner).call("inline", "iam", "list-role-policies", "--role-name", "FDS-IaC-Operator")
        args, kwargs = runner.call_args
        self.assertNotIn("--no-paginate", args[0])
        self.assertEqual(kwargs["timeout"], 40)
        self.assertEqual(kwargs["env"]["AWS_MAX_ATTEMPTS"], "1")
        self.assertEqual((self.path / "001-inline-attempt1.stdout").stat().st_mode & 0o777, 0o600)

    def test_truncated_and_invalid_responses_stop(self):
        for value in [{"NextToken": "remaining"}, {"IsTruncated": True}, []]:
            with self.subTest(value=value), self.assertRaises(M.AwsError):
                M.Capture(self.path, Mock(return_value=result(value))).call("response", "iam", "list-role-policies", "--role-name", "FDS-IaC-Operator")

    def test_matrix_never_pretends_to_evaluate_resource_policy_roles(self):
        docs = M.load_source(SOURCE)
        cases = M.simulation_cases(docs["candidates/iac-backend-passrole.candidate.json"], docs["candidates/state-bucket-policy.candidate.json"])
        self.assertEqual(len(cases), 46)
        resource_cases = [c for c in cases if "ResourcePolicy" in c["Request"]]
        self.assertEqual(len(resource_cases), 18)
        for case in cases:
            req = case["Request"]
            self.assertEqual(len(req["ResourceArns"]), 1)
            for doc in map(json.loads, req["PolicyInputList"]):
                self.assertTrue(all("Principal" not in s for s in doc["Statement"]))
            if case in resource_cases:
                self.assertIn(req["CallerArn"], [f"arn:aws:iam::{M.ACCOUNT}:user/{u}" for u in M.USERS])
                self.assertEqual(case["Scope"], "BUCKET_DENY_OVERRIDE_FIXTURE")
        positive_resources = {c["Request"]["ResourceArns"][0] for c in cases if c["Label"].endswith(("-state", "-lock"))}
        self.assertEqual(len(positive_resources), 8)

    def test_simulator_legacy_and_aggregate_shapes(self):
        case = {"Label": "read", "Expected": "allowed", "Request": {"ActionNames": ["s3:GetObject"], "ResourceArns": [M.S3 + "/phase2/network/terraform.tfstate"]}}
        row = {"EvalActionName": "s3:GetObject", "EvalDecision": "allowed", "MissingContextValues": []}
        M.check_simulation(case, {"EvaluationResults": [row]})
        row["ResourceSpecificResults"] = [{"EvalResourceName": case["Request"]["ResourceArns"][0], "EvalResourceDecision": "allowed"}]
        M.check_simulation(case, {"EvaluationResults": [row]})
        row["ResourceSpecificResults"][0]["EvalResourceName"] += "-other"
        with self.assertRaises(M.Stop):
            M.check_simulation(case, {"EvaluationResults": [row]})

    def test_simulator_missing_action_context_and_bad_decision_stop(self):
        case = {"Label": "read", "Expected": "allowed", "Request": {"ActionNames": ["s3:GetObject"], "ResourceArns": [M.S3 + "/state"]}}
        rows = [[], [{"EvalActionName": "s3:PutObject", "EvalDecision": "allowed"}],
                [{"EvalActionName": "s3:GetObject", "EvalDecision": "implicitDeny"}],
                [{"EvalActionName": "s3:GetObject", "EvalDecision": "allowed", "MissingContextValues": ["aws:PrincipalArn"]}]]
        for row in rows:
            with self.subTest(row=row), self.assertRaises(M.Stop):
                M.check_simulation(case, {"EvaluationResults": row})

    def test_existing_foreign_region_stops(self):
        cap = M.Capture(self.path, Mock(return_value=result({"LocationConstraint": "us-east-1"})))
        with self.assertRaises(M.Stop):
            M.snapshot_bucket(cap, {})

    def test_bucket_absent_does_not_imply_name_available(self):
        cap = M.Capture(self.path, Mock(return_value=result(error="NoSuchBucket")))
        self.assertEqual(M.snapshot_bucket(cap, {})["NameAvailability"], "NOT_GUARANTEED")

    def test_bucket_readback_mismatch_is_reported_not_fixed(self):
        runner = Mock(side_effect=[result({"LocationConstraint": M.REGION}), result({}),
                                  result(error="ServerSideEncryptionConfigurationNotFoundError"),
                                  result(error="NoSuchPublicAccessBlockConfiguration"),
                                  result(error="OwnershipControlsNotFoundError"), result(error="NoSuchBucketPolicy")])
        observed = M.snapshot_bucket(M.Capture(self.path, runner), {"Statement": []})
        self.assertEqual(observed["Readback"], "DIFFERENCES_REQUIRE_REVIEW")
        self.assertFalse(any(observed["Checks"].values()))
        for call in runner.call_args_list:
            cmd = call.args[0]
            self.assertEqual(cmd[cmd.index("--expected-bucket-owner") + 1], M.ACCOUNT)
            self.assertTrue(cmd[2].startswith("get-"))

    def test_managed_version_race_is_not_snapshot_complete(self):
        role = {"Role": {"Arn": M.IAC}}
        runner = Mock(side_effect=[*[result({"User": {"Arn": f"arn:aws:iam::{M.ACCOUNT}:user/{u}"}}) for u in M.USERS],
                                  result(role), result({"PolicyNames": []}),
                                  result({"AttachedPolicies": [{"PolicyArn": "arn:aws:iam::aws:policy/ReadOnlyAccess"}]}),
                                  result({"Policy": {"DefaultVersionId": "v1"}}),
                                  result({"PolicyVersion": {"Document": {"Statement": []}}}),
                                  result({"Policy": {"DefaultVersionId": "v2"}})])
        with self.assertRaises(M.Stop):
            M.snapshot_iam(M.Capture(self.path, runner))

    def test_stop_always_preserves_manifest_and_non_success(self):
        with patch.object(M, "run_capture", side_effect=M.Stop("fixture stop")), patch("builtins.print"):
            rc = M.main(["--source-dir", str(SOURCE), "--output-parent", str(self.path)])
        self.assertEqual(rc, 1)
        output = next(self.path.glob("fds-iac-delta-precheck-*"))
        stop = json.loads((output / "stop.json").read_text())
        self.assertEqual(stop["Collection"], "INCOMPLETE")
        self.assertEqual(stop["ROLE_GRANT"], "NOT_RUN")
        self.assertIn("stop.json", (output / "SHA256SUMS").read_text())


if __name__ == "__main__":
    unittest.main()
