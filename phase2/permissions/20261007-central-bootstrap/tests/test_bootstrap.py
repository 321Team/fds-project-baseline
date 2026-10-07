import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("bootstrap", HERE / "bootstrap-central.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
DOCS = m.load_source(HERE)
STACK_ID = m.STACK_PREFIX + "00000000-0000-0000-0000-000000000000"


class FakeAWS:
    def __init__(self, **changes):
        self.changes, self.calls = changes, []

    def __call__(self, command, **kwargs):
        service, operation = command[1:3]
        request = json.loads(Path(command[command.index("--cli-input-json") + 1][7:]).read_text()) if "--cli-input-json" in command else {}
        region = command[command.index("--region") + 1]
        self.calls.append((service, operation, request, region, kwargs))
        self.last_request = request
        if self.changes.get("timeout") == operation:
            raise subprocess.TimeoutExpired(command, 40, output=b"partial", stderr=b"bounded timeout")
        error = self.changes.get("error")
        if error and operation == error[0]:
            return SimpleNamespace(returncode=254, stdout="", stderr=f"An error occurred ({error[1]}) when calling the Test operation: test")
        if self.changes.get("bad_json") == operation:
            return SimpleNamespace(returncode=0, stdout="{", stderr="")
        existing = self.changes.get("verify", False)
        if service == "sts":
            value = {"Arn": self.changes.get("actor", m.ROOT), "Account": m.ACCOUNT}
        elif operation == "get-bucket-location":
            if not existing and not self.changes.get("bucket_exists"):
                return SimpleNamespace(returncode=254, stdout="", stderr="An error occurred (NoSuchBucket) when calling the Test operation: absent")
            value = {"LocationConstraint": self.changes.get("bucket_region", m.REGION)}
        elif operation in ("get-role", "get-instance-profile") and not existing:
            if not self.changes.get(operation):
                return SimpleNamespace(returncode=254, stdout="", stderr="An error occurred (NoSuchEntity) when calling the Test operation: absent")
            value = {}
        elif operation == "describe-stacks":
            if not existing:
                msg = f"Stack with id {m.STACK} does not exist" if not self.changes.get("ambiguous_stack_error") else "malformed request"
                return SimpleNamespace(returncode=254, stdout="", stderr=f"An error occurred (ValidationError) when calling the DescribeStacks operation: {msg}")
            value = {"Stacks": [{"StackId": STACK_ID, "StackName": m.STACK, "StackStatus": self.changes.get("stack_status", "CREATE_COMPLETE"), "EnableTerminationProtection": True}]}
        elif operation == "validate-template":
            value = {"Capabilities": ["CAPABILITY_NAMED_IAM"], "Parameters": []}
        elif operation == "get-policy":
            self.policy_reads = getattr(self, "policy_reads", 0) + 1
            version = "v3" if self.changes.get("version_drift") and self.policy_reads > 1 else "v2"
            value = {"Policy": {"Arn": m.AGENT_ARN, "DefaultVersionId": version}}
        elif operation == "get-policy-version":
            doc = copy.deepcopy(DOCS["agent-policy.expected.json"])
            if self.changes.get("agent_wildcard"):
                doc["Statement"][0]["Action"].append("ssm:*")
            value = {"PolicyVersion": {"VersionId": "v2", "IsDefaultVersion": True, "Document": doc}}
        elif operation == "describe-regions":
            value = {"Regions": [{"RegionName": m.REGION, "OptInStatus": "opt-in-not-required"}, {"RegionName": "ap-northeast-1", "OptInStatus": "opted-in"}, {"RegionName": "af-south-1", "OptInStatus": "not-opted-in"}]}
        elif operation == "describe-parameters":
            p = [{"Name": "/private/example", "Type": "SecureString", "Description": "SENSITIVE-METADATA-TEST"}] if self.changes.get("parameters") == (region, request["Shared"]) else []
            value = {"Parameters": p}
            if self.changes.get("truncated"):
                value["NextToken"] = "more"
        elif operation == "create-stack":
            value = {"StackId": STACK_ID}
        elif operation == "get-template":
            doc = copy.deepcopy(DOCS["bootstrap-stack.candidate.json"])
            if self.changes.get("template_drift"):
                doc["Resources"]["Extra"] = {"Type": "AWS::EC2::Instance"}
            value = {"TemplateBody": json.dumps(doc)}
        elif operation == "describe-stack-resources":
            value = {"StackResources": [{"LogicalResourceId": key, "ResourceType": kind, "PhysicalResourceId": physical, "ResourceStatus": "CREATE_COMPLETE"} for key, kind, physical in [("StateBucket", "AWS::S3::Bucket", m.BUCKET), ("StateBucketPolicy", "AWS::S3::BucketPolicy", m.BUCKET), ("RelayRole", "AWS::IAM::Role", m.ROLE), ("RelayProfile", "AWS::IAM::InstanceProfile", m.ROLE)]]}
        elif operation == "get-bucket-versioning":
            value = {"Status": self.changes.get("versioning", "Enabled")}
        elif operation == "get-bucket-encryption":
            value = {"ServerSideEncryptionConfiguration": {"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}}
        elif operation == "get-public-access-block":
            value = {"PublicAccessBlockConfiguration": dict.fromkeys(("BlockPublicAcls", "IgnorePublicAcls", "BlockPublicPolicy", "RestrictPublicBuckets"), True)}
        elif operation == "get-bucket-ownership-controls":
            value = {"OwnershipControls": {"Rules": [{"ObjectOwnership": "BucketOwnerEnforced"}]}}
        elif operation == "get-bucket-policy":
            policy = copy.deepcopy(DOCS["bootstrap-stack.candidate.json"]["Resources"]["StateBucketPolicy"]["Properties"]["PolicyDocument"])
            if self.changes.get("policy_reordered"):
                policy["Statement"].reverse()
                for row in policy["Statement"]:
                    if isinstance(row.get("Resource"), list):
                        row["Resource"].reverse()
            if self.changes.get("policy_drift"):
                policy["Statement"][0]["Condition"]["ArnNotEquals"]["aws:PrincipalArn"].append("arn:aws:iam::774055931866:user/other")
            value = {"Policy": json.dumps(policy)}
        elif operation == "get-role":
            role = {"Arn": m.ROLE_ARN, "RoleName": m.ROLE, "Path": "/", "MaxSessionDuration": 3600, "AssumeRolePolicyDocument": DOCS["bootstrap-stack.candidate.json"]["Resources"]["RelayRole"]["Properties"]["AssumeRolePolicyDocument"]}
            value = {"Role": role}
        elif operation == "list-role-policies":
            value = {"PolicyNames": ["unexpected"] if self.changes.get("inline") else []}
        elif operation == "list-attached-role-policies":
            value = {"AttachedPolicies": [{"PolicyArn": m.AGENT_ARN}]}
        elif operation == "get-instance-profile":
            value = {"InstanceProfile": {"Arn": m.PROFILE_ARN, "InstanceProfileName": m.ROLE, "Path": "/", "Roles": [{"Arn": "arn:aws:iam::774055931866:role/other" if self.changes.get("profile_drift") else m.ROLE_ARN}]}}
        else:
            raise AssertionError("Unexpected operation " + operation)
        return SimpleNamespace(returncode=0, stdout=json.dumps(value), stderr="")


class BootstrapTests(unittest.TestCase):
    def run_mode(self, mode="prepare", **changes):
        fake = FakeAWS(**changes)
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()) as output:
            args = ["--mode", mode, "--output-parent", tmp]
            if mode == "verify":
                args += ["--stack-id", STACK_ID]
            rc = m.main(args, fake)
            capture = next(Path(tmp).iterdir())
            saved = {p.name: p.read_bytes() for p in capture.iterdir() if p.is_file()}
            for row in saved["SHA256SUMS"].decode().splitlines():
                sha, path = row.split("  ")
                self.assertEqual(sha, hashlib.sha256(saved[path[2:]]).hexdigest())
            self.assertTrue(all((p.stat().st_mode & 0o777) == 0o600 for p in capture.iterdir() if p.is_file()))
            return rc, fake, saved, output.getvalue()

    def test_prepare_is_metadata_only_and_covers_owned_shared_enabled_regions(self):
        rc, fake, saved, out = self.run_mode()
        self.assertEqual(rc, 0)
        self.assertFalse(any(op == "create-stack" for _, op, *_ in fake.calls))
        rows = [(region, req["Shared"]) for _, op, req, region, _ in fake.calls if op == "describe-parameters"]
        self.assertEqual(set(rows), {(m.REGION, False), (m.REGION, True), ("ap-northeast-1", False), ("ap-northeast-1", True)})
        self.assertIn('"Status": "PREPARED_NO_MUTATION"', out)

    def test_create_submits_exactly_once_with_retention_and_no_human_grants(self):
        rc, fake, saved, out = self.run_mode("create")
        self.assertEqual(rc, 0)
        calls = [req for _, op, req, *_ in fake.calls if op == "create-stack"]
        self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0]["OnFailure"], "DO_NOTHING")
        self.assertTrue(calls[0]["EnableTerminationProtection"])
        self.assertNotIn("RoleARN", calls[0])
        self.assertEqual(json.loads(calls[0]["TemplateBody"]), DOCS["bootstrap-stack.candidate.json"])
        self.assertIn("SUBMITTED_NOT_READBACK", out)
        self.assertEqual(set(json.loads(calls[0]["TemplateBody"])["Resources"]), {"StateBucket", "StateBucketPolicy", "RelayRole", "RelayProfile"})
        for resource in json.loads(calls[0]["TemplateBody"])["Resources"].values():
            self.assertEqual(resource["DeletionPolicy"], "Retain")
            self.assertEqual(resource["UpdateReplacePolicy"], "Retain")

    def test_wrong_identity_stops_after_sts(self):
        rc, fake, saved, _ = self.run_mode("create", actor="arn:aws:iam::774055931866:user/321team-gwonuk")
        self.assertEqual(rc, 1)
        self.assertEqual(len(fake.calls), 1)

    def test_existing_or_foreign_region_bucket_never_modified(self):
        rc, fake, saved, _ = self.run_mode("create", bucket_exists=True, bucket_region="ap-northeast-1")
        self.assertEqual(rc, 1)
        self.assertEqual(len(fake.calls), 2)

    def test_access_denied_and_generic_validation_are_not_absence(self):
        for changes in ({"error": ("get-bucket-location", "AccessDenied")}, {"ambiguous_stack_error": True}):
            with self.subTest(changes=changes):
                rc, fake, saved, _ = self.run_mode("create", **changes)
                self.assertEqual(rc, 1)
                self.assertFalse(any(op == "create-stack" for _, op, *_ in fake.calls))

    def test_agent_document_drift_and_version_race_stop_before_mutation(self):
        for changes in ({"agent_wildcard": True}, {"version_drift": True}):
            rc, fake, saved, _ = self.run_mode("create", **changes)
            self.assertEqual(rc, 1)
            self.assertFalse(any(op == "create-stack" for _, op, *_ in fake.calls))

    def test_parameters_in_other_region_or_shared_require_scope_review_no_value_read(self):
        for location in (("ap-northeast-1", False), (m.REGION, True)):
            rc, fake, saved, out = self.run_mode("create", parameters=location)
            self.assertEqual(rc, 1)
            self.assertNotIn("SENSITIVE-METADATA-TEST", out)
            self.assertFalse(any(op in ("create-stack", "get-parameter", "get-parameters") for _, op, *_ in fake.calls))

    def test_truncated_or_invalid_responses_never_become_readiness(self):
        for changes in ({"truncated": True}, {"bad_json": "get-policy"}):
            rc, fake, saved, _ = self.run_mode("create", **changes)
            self.assertEqual(rc, 1)
            self.assertIn("stop.json", saved)

    def test_create_timeout_preserves_partial_has_no_retry_or_false_not_run(self):
        rc, fake, saved, out = self.run_mode("create", timeout="create-stack")
        self.assertEqual(rc, 1)
        self.assertEqual(sum(op == "create-stack" for _, op, *_ in fake.calls), 1)
        self.assertTrue(any(data == b"partial" for name, data in saved.items() if name.endswith("stdout")))
        self.assertEqual(json.loads(saved["stop.json"])["AWS_MUTATION"], "CREATE_ATTEMPT_OUTCOME_REQUIRES_INSPECTION")
        self.assertIn("CREATE_STACK_ATTEMPTED", out)

    def test_readback_checks_actual_settings_without_mutation(self):
        rc, fake, saved, out = self.run_mode("verify", verify=True, policy_reordered=True)
        self.assertEqual(rc, 0)
        self.assertIn("BOOTSTRAP_SETTINGS_PASS", out)
        self.assertFalse(any(op == "create-stack" for _, op, *_ in fake.calls))

    def test_readback_drift_or_incomplete_stack_stops_never_repairs(self):
        for changes in ({"stack_status": "CREATE_FAILED"}, {"template_drift": True}, {"versioning": "Suspended"}, {"policy_drift": True}, {"profile_drift": True}, {"inline": True}):
            rc, fake, saved, _ = self.run_mode("verify", verify=True, **changes)
            self.assertEqual(rc, 1)
            self.assertFalse(any(op not in m.READS.get(service, set()) for service, op, *_ in fake.calls))

    def test_pinned_source_tamper_and_invalid_stack_id_precede_aws(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            for n in m.SOURCE_HASHES:
                (p / n).write_bytes((HERE / n).read_bytes() + b" ")
            with self.assertRaises(m.Stop):
                m.load_source(p)
        for arn in (None, STACK_ID.replace(m.ACCOUNT, "000000000000"), STACK_ID.replace(m.REGION, "ap-northeast-1")):
            with self.assertRaises(m.Stop):
                m.check_stack_id(arn)

    def test_operation_boundary_rejects_mutation_content_reads_and_foreign_create(self):
        with tempfile.TemporaryDirectory() as tmp:
            fake = FakeAWS()
            c = m.Capture(tmp, fake)
            for service, operation in (("ssm", "get-parameter"), ("s3api", "get-object"), ("cloudformation", "delete-stack"), ("iam", "attach-role-policy")):
                with self.assertRaises(m.Stop):
                    c.call("forbidden", service, operation)
            with self.assertRaises(m.Stop):
                c.call("create", "cloudformation", "create-stack", {}, mutation=True)
            c.mode = "create"
            with self.assertRaises(m.Stop):
                c.call("foreign", "cloudformation", "create-stack", {"StackName": "other"}, mutation=True)
            self.assertEqual(fake.calls, [])

    def test_cli_is_bounded_paginated_and_does_not_print_credentials(self):
        rc, fake, saved, out = self.run_mode()
        for _, _, _, _, kwargs in fake.calls:
            self.assertEqual(kwargs["timeout"], 40)
            self.assertEqual(kwargs["env"]["AWS_MAX_ATTEMPTS"], "1")
        self.assertNotIn("AWS_SECRET_ACCESS_KEY", out)


if __name__ == "__main__":
    unittest.main()
