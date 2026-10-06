import importlib.util
import contextlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "capture-work-role-precheck.py"
spec = importlib.util.spec_from_file_location("precheck", SOURCE)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class FakeAWS:
    def __init__(self, identity=None, failure=None, force_allowed=False):
        self.identity = identity or {"Account": p.ACCOUNT, "Arn": p.ROOT}
        self.failure = failure
        self.force_allowed = force_allowed
        self.commands = []

    def __call__(self, command, **kwargs):
        self.commands.append(command)
        service, operation = command[1:3]
        def value(flag):
            return command[command.index(flag) + 1]
        if operation == self.failure:
            return subprocess.CompletedProcess(command, 254, "", "An error occurred (AccessDenied) when calling the GetRole operation: denied")
        if operation == "get-caller-identity":
            data = self.identity
        elif operation == "get-group":
            data = {"Users": [{"Arn": p.arn("user", u)} for u in p.USERS]}
        elif operation == "get-user":
            data = {"User": {"Arn": p.arn("user", value("--user-name"))}}
        elif operation.startswith("list-") and operation.endswith("-policies"):
            data = {"AttachedPolicies": []} if "attached" in operation else {"PolicyNames": []}
        elif operation == "list-groups-for-user":
            data = {"Groups": [{"GroupName": p.GROUP}]}
        elif operation == "list-mfa-devices":
            data = {"MFADevices": [{"SerialNumber": "metadata-only"}]}
        elif operation == "list-access-keys":
            data = {"AccessKeyMetadata": []}
        elif operation == "get-role":
            return subprocess.CompletedProcess(command, 254, "", "An error occurred (NoSuchEntity) when calling the GetRole operation: absent")
        elif operation == "validate-policy":
            data = {"findings": []}
        elif operation == "get-context-keys-for-principal-policy":
            data = {"ContextKeyNames": ["aws:MultiFactorAuthPresent", "sts:RoleSessionName"]}
        elif operation == "simulate-principal-policy":
            request = json.loads(Path(value("--cli-input-json").removeprefix("file://")).read_text())
            user = request["PolicySourceArn"].rsplit("/", 1)[1]
            resource = request["ResourceArns"][0]
            role = resource.rsplit("/", 1)[1]
            context = {c["ContextKeyName"]: c["ContextKeyValues"][0] for c in request["ContextEntries"]}
            allowed = (context.get("aws:MultiFactorAuthPresent") == "true"
                       and context["sts:RoleSessionName"] == user and user in p.ASSIGNMENTS[role])
            decision = "allowed" if allowed or self.force_allowed else "implicitDeny"
            data = {"EvaluationResults": [{"EvalActionName": "sts:AssumeRole",
                                          "EvalResourceName": resource, "EvalDecision": decision}]}
        else:
            data = {"Items": []}
        return subprocess.CompletedProcess(command, 0, json.dumps(data), "")


class CollectorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_wrong_account_stops_before_iam(self):
        fake = FakeAWS(identity={"Account": "000000000000", "Arn": p.ROOT})
        with self.assertRaises(p.Stop):
            p.Capture(self.directory, fake).capture_iam()
        self.assertEqual(len(fake.commands), 1)

    def test_ordinary_user_stops_before_iam(self):
        fake = FakeAWS(identity={"Account": p.ACCOUNT, "Arn": p.arn("user", p.USERS[0])})
        with self.assertRaises(p.Stop):
            p.Capture(self.directory, fake).capture_iam()
        self.assertEqual(len(fake.commands), 1)

    def test_only_no_such_entity_is_role_absence(self):
        cap = p.Capture(self.directory, FakeAWS())
        cap.capture_iam()
        self.assertEqual(cap.roles, {name: "ABSENT" for name in p.OBSERVED_ROLES})
        with self.assertRaises(p.AwsError):
            p.Capture(self.directory, FakeAWS(failure="get-role")).capture_iam()

    def test_mutation_is_rejected_without_invocation(self):
        fake = FakeAWS()
        with self.assertRaises(p.Stop):
            p.Capture(self.directory, fake).call("mutation", "iam", "create-role")
        self.assertEqual(fake.commands, [])

    def test_full_mock_keeps_cli_pagination_and_has_no_aws_writes(self):
        fake = FakeAWS()
        cap = p.Capture(self.directory, fake)
        with contextlib.redirect_stdout(io.StringIO()):
            p.run(cap, simulate=True)
        summary = json.loads((self.directory / "summary.json").read_text())
        self.assertEqual(summary["SIMULATION_CASES"], 22)
        self.assertEqual(summary["ROLE_GRANT"], "NOT_RUN")
        self.assertEqual(summary["TRUST_RUNTIME"], "NOT_TESTED")
        self.assertEqual(summary["APPLY_READINESS"], "NOT_ASSESSED")
        for command in fake.commands:
            self.assertIn(command[2], p.READ_OPERATIONS[command[1]])
            self.assertNotIn("--no-paginate", command)
            self.assertNotIn("--max-items", command)
        self.assertTrue((self.directory / "SHA256SUMS").exists())

    def test_unexpected_allow_halts_and_preserves_results(self):
        with self.assertRaises(p.Stop), contextlib.redirect_stdout(io.StringIO()):
            p.run(p.Capture(self.directory, FakeAWS(force_allowed=True)), simulate=True)
        self.assertTrue((self.directory / "SHA256SUMS").exists())
        self.assertFalse((self.directory / "summary.json").exists())

    def test_validation_warning_is_not_approval(self):
        cap = p.Capture(self.directory, FakeAWS())
        original = cap.call
        def warning(label, service, operation, *args):
            if operation == "validate-policy":
                return {"findings": [{"findingType": "SECURITY_WARNING", "issueCode": "MOCK"}]}
            return original(label, service, operation, *args)
        cap.call = warning
        with self.assertRaises(p.Stop):
            cap.validate_candidates(p.candidate_documents())
        self.assertTrue((self.directory / "candidate-findings.json").exists())

    def test_timeout_preserves_error(self):
        def timeout(*args, **kwargs):
            raise subprocess.TimeoutExpired("aws", 60)
        with self.assertRaises(p.AwsError):
            p.Capture(self.directory, timeout).call("identity", "sts", "get-caller-identity")
        self.assertTrue((self.directory / "001-identity.json").exists())

    def test_managed_default_version_drift_halts(self):
        cap = p.Capture(self.directory)
        replies = iter([{"Policy": {"DefaultVersionId": "v1"}},
                        {"PolicyVersion": {"Document": {"Version": "2012-10-17"}}},
                        {"Policy": {"DefaultVersionId": "v2"}}])
        cap.call = lambda *args: next(replies)
        with self.assertRaises(p.Stop):
            cap.managed_policy("arn:aws:iam::aws:policy/ReadOnlyAccess")

    def test_invalid_cli_json_is_preserved(self):
        def malformed(command, **kwargs):
            return subprocess.CompletedProcess(command, 0, "not json", "")
        with self.assertRaises(p.AwsError):
            p.Capture(self.directory, malformed).call("identity", "sts", "get-caller-identity")
        self.assertTrue((self.directory / "001-identity.json").exists())


class CandidateTests(unittest.TestCase):
    def test_trust_has_only_assigned_users_and_requires_mfa_session_name(self):
        docs = p.candidate_documents()
        for role, users in p.ASSIGNMENTS.items():
            statements = docs[f"trust-{role}.candidate.json"]["Statement"]
            self.assertEqual({s["Principal"]["AWS"] for s in statements}, {p.arn("user", u) for u in users})
            for s in statements:
                user = s["Principal"]["AWS"].rsplit("/", 1)[1]
                self.assertEqual(s["Action"], "sts:AssumeRole")
                self.assertEqual(s["Condition"]["Bool"], {"aws:MultiFactorAuthPresent": "true"})
                self.assertEqual(s["Condition"]["StringEquals"], {"sts:RoleSessionName": user})

    def test_identity_has_exact_assigned_roles_and_no_write_or_cost_actions(self):
        for user in p.USERS:
            statement = p.candidate_documents()[f"assume-{user}.candidate.json"]["Statement"][0]
            self.assertEqual(statement["Action"], "sts:AssumeRole")
            self.assertEqual(set(statement["Resource"]), {p.arn("role", r) for r, users in p.ASSIGNMENTS.items() if user in users})
            self.assertNotIn("*", json.dumps(statement))

    def test_repository_candidate_files_match_collector(self):
        for name, doc in p.candidate_documents().items():
            self.assertEqual(json.loads((SOURCE.parent / "candidates" / name).read_text()), doc)


if __name__ == "__main__":
    unittest.main()
