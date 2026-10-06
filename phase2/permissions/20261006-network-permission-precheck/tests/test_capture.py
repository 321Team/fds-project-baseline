import contextlib
import copy
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1] / "capture-network-permission-precheck.py"
spec = importlib.util.spec_from_file_location("network_capture", SOURCE)
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class ResultTests(unittest.TestCase):
    def setUp(self):
        self.case = {"Label": "mixed-resource", "Actions": ["ssm:StartSession"],
                     "Resources": ["instance-arn", "document-arn"],
                     "ExpectedByResource": {"instance-arn": "allowed", "document-arn": "implicitDeny"},
                     "IntentionalMissing": [], "ObservationOnly": False}
        # Canned current AWS response: aggregate alone cannot describe each ARN.
        self.result = {"EvaluationResults": [{"EvalActionName": "ssm:StartSession",
            "EvalDecision": "implicitDeny", "EvalResourceName": "arn:${Partition}:ec2:...",
            "ResourceSpecificResults": [
                {"EvalResourceName": "instance-arn", "EvalResourceDecision": "allowed"},
                {"EvalResourceName": "document-arn", "EvalResourceDecision": "implicitDeny"},
            ]}]}

    def test_current_resource_decisions_are_used(self):
        rows = p.inspect_result(self.result, self.case)
        self.assertEqual([r["Decision"] for r in rows], ["allowed", "implicitDeny"])

    def test_aggregate_cannot_hide_unexpected_document_allow(self):
        self.result["EvaluationResults"][0]["ResourceSpecificResults"][1]["EvalResourceDecision"] = "allowed"
        with self.assertRaises(p.Stop):
            p.inspect_result(self.result, self.case)

    def test_missing_or_duplicate_resource_is_rejected(self):
        for resources in ([self.result["EvaluationResults"][0]["ResourceSpecificResults"][0]],
                          [self.result["EvaluationResults"][0]["ResourceSpecificResults"][0]] * 2):
            response = copy.deepcopy(self.result)
            response["EvaluationResults"][0]["ResourceSpecificResults"] = resources
            with self.assertRaises(p.Stop):
                p.inspect_result(response, self.case)

    def test_multi_resource_aggregate_only_is_rejected(self):
        del self.result["EvaluationResults"][0]["ResourceSpecificResults"]
        with self.assertRaises(p.Stop):
            p.inspect_result(self.result, self.case)

    def test_missing_context_and_truncation_cannot_pass(self):
        response = copy.deepcopy(self.result)
        response["EvaluationResults"][0]["ResourceSpecificResults"][0]["MissingContextValues"] = ["unexpected-key"]
        with self.assertRaises(p.Stop):
            p.inspect_result(response, self.case)
        self.result["IsTruncated"] = True
        with self.assertRaises(p.Stop):
            p.inspect_result(self.result, self.case)

    def test_duplicate_action_is_rejected(self):
        self.result["EvaluationResults"] *= 2
        self.case["Actions"].append("ssm:TerminateSession")
        with self.assertRaises(p.Stop):
            p.inspect_result(self.result, self.case)

    def test_channel_aggregate_is_observation_without_arn_inference(self):
        case = {**self.case, "Actions": ["ssmmessages:OpenDataChannel"],
                "Resources": ["session-arn"], "ExpectedByResource": {}, "ObservationOnly": True}
        result = {"EvaluationResults": [{"EvalActionName": "ssmmessages:OpenDataChannel",
                                         "EvalDecision": "allowed", "EvalResourceName": "*"}]}
        rows = p.inspect_result(result, case)
        self.assertEqual(rows[0]["EvidenceLevel"], "AGGREGATE_ONLY_NO_ARN_INFERENCE")
        self.assertNotIn("Resource", rows[0])

    def test_malformed_channel_observation_is_rejected(self):
        case = {**self.case, "ObservationOnly": True}
        self.result["EvaluationResults"][0]["EvalDecision"] = "unknown"
        with self.assertRaises(p.Stop):
            p.inspect_result(self.result, case)


class CaptureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)
        self.inputs = p.load_inputs(SOURCE.parent / "inputs")

    def tearDown(self):
        self.temp.cleanup()

    def test_aws_mutation_stops_before_runner(self):
        with patch.object(p.subprocess, "run") as runner:
            cap = p.Capture(self.directory, runner)
            with self.assertRaises(p.Stop):
                cap.call("bad", "ssm", "start-session")
            runner.assert_not_called()

    def test_wrong_root_stops_after_identity_and_keeps_manifest(self):
        commands = []
        def runner(command, **kwargs):
            commands.append(command)
            return subprocess.CompletedProcess(command, 0,
                json.dumps({"Account": p.ACCOUNT, "Arn": f"arn:aws:iam::{p.ACCOUNT}:user/321team-gwonuk"}), "")
        with self.assertRaises(p.Stop), contextlib.redirect_stdout(io.StringIO()):
            p.run(p.Capture(self.directory, runner), self.inputs)
        self.assertEqual(len(commands), 1)
        self.assertTrue((self.directory / "failure-summary.json").exists())
        self.assertTrue((self.directory / "SHA256SUMS").exists())

    def test_malformed_and_nonobject_json_keep_exact_private_raw(self):
        for n, stdout in enumerate(("not JSON\n", "[]\n")):
            subdir = self.directory / str(n)
            subdir.mkdir()
            runner = lambda cmd, **kw: subprocess.CompletedProcess(cmd, 0, stdout, "diagnostic\n")
            cap = p.Capture(subdir, runner)
            with self.assertRaises(p.AwsError):
                cap.call("identity", "sts", "get-caller-identity")
            self.assertEqual((subdir / "001-identity-stdout.txt").read_text(), stdout)
            for path in subdir.iterdir():
                self.assertEqual(path.stat().st_mode & 0o777, 0o600)

    def test_timeout_keeps_partial_streams(self):
        def runner(*args, **kwargs):
            raise subprocess.TimeoutExpired("aws", 60, output=b"partial\xff", stderr=b"error")
        with self.assertRaises(p.AwsError):
            p.Capture(self.directory, runner).call("identity", "sts", "get-caller-identity")
        self.assertEqual((self.directory / "001-identity-partial-stdout.txt").read_bytes(), b"partial\xff")

    def test_manifest_failure_never_prints_complete(self):
        cap = p.Capture(self.directory)
        output = io.StringIO()
        with patch.object(cap, "manifest", side_effect=OSError("disk error")):
            with self.assertRaises(OSError), contextlib.redirect_stdout(output):
                p.run(cap, self.inputs, offline=True)
        self.assertNotIn("COMPLETE", output.getvalue())

    def test_offline_invokes_no_aws_and_retains_not_granted_status(self):
        with patch.object(p.subprocess, "run") as runner, contextlib.redirect_stdout(io.StringIO()):
            rc = p.run(p.Capture(self.directory, runner), self.inputs, offline=True)
        runner.assert_not_called()
        self.assertEqual(rc, 0)
        summary = json.loads((self.directory / "summary.json").read_text())
        self.assertEqual(summary["Collection"], "OFFLINE_PREPARED")
        self.assertEqual(summary["CHANNEL_SELECTION"], "NOT_MADE")
        self.assertEqual(summary["ROLE_GRANT"], "NOT_RUN")
        self.assertEqual(summary["USER_EFFECTIVE_PERMISSION"], "NOT_TESTED")

    def test_document_default_version_drift_stops(self):
        initial = {"Document": {"Name": p.DOCUMENT, "Owner": p.ACCOUNT,
                   "DocumentType": "Session", "DefaultVersion": "1", "Status": "Active"}}
        after = copy.deepcopy(initial)
        after["Document"]["DefaultVersion"] = "2"
        cap = p.Capture(self.directory)
        with patch.object(cap, "call", side_effect=[initial, {"Content": "{}"}, after]):
            with self.assertRaises(p.Stop):
                p.document_capture(cap)

    def test_validation_error_skips_only_that_candidate_without_policy_selection(self):
        cap = p.Capture(self.directory)
        commands = []
        def call(label, service, operation, *args):
            commands.append(operation)
            if operation == "get-caller-identity":
                return {"Account": p.ACCOUNT, "Arn": p.ROOT}
            if operation == "describe-document":
                raise p.AwsError(operation, "InvalidDocument")
            if operation == "validate-policy":
                return {"findings": [{"findingType": "ERROR", "issueCode": "test-error"}]}
            raise AssertionError("No simulation is allowed for invalid candidates")
        with patch.object(cap, "call", side_effect=call), contextlib.redirect_stdout(io.StringIO()):
            rc = p.run(cap, self.inputs)
        self.assertEqual(rc, 2)
        self.assertNotIn("simulate-custom-policy", commands)
        summary = json.loads((self.directory / "summary.json").read_text())
        self.assertEqual(summary["CHANNEL_SELECTION"], "NOT_MADE")
        self.assertTrue(all(c["Matrix"] == "SKIPPED_VALIDATION_ERRORS" for c in summary["Candidates"].values()))

    def test_pinned_input_tampering_stops(self):
        for name in p.INPUT_HASHES:
            (self.directory / name).write_bytes((SOURCE.parent / "inputs" / name).read_bytes())
        path = self.directory / "network-permissions.template.json"
        path.write_bytes(path.read_bytes() + b" ")
        with self.assertRaises(p.Stop):
            p.load_inputs(self.directory)

    def test_channel_invalid_input_is_not_deny_or_auto_selection(self):
        cap = p.Capture(self.directory)
        experimental = {"Label": "channel-experiment", "Actions": ["ssmmessages:OpenDataChannel"],
            "Resources": ["*"], "Context": {}, "ExpectedByResource": {},
            "IntentionalMissing": [], "ObservationOnly": True}
        def call(label, service, operation, *args):
            if operation == "get-caller-identity":
                return {"Account": p.ACCOUNT, "Arn": p.ROOT}
            if operation == "validate-policy":
                return {"findings": []}
            if operation == "get-context-keys-for-custom-policy":
                return {"ContextKeyNames": []}
            if label.startswith("arn-"):
                raise p.AwsError(operation, "InvalidInput")
            return {"EvaluationResults": [{"EvalActionName": "ssmmessages:OpenDataChannel",
                    "EvalDecision": "allowed", "EvalResourceName": "*"}]}
        with patch.object(cap, "call", side_effect=call), patch.object(p, "cases", return_value=[experimental]), \
             patch.object(p, "document_capture", return_value={"State": "ABSENT_OR_UNAVAILABLE"}), \
             contextlib.redirect_stdout(io.StringIO()):
            rc = p.run(cap, self.inputs)
        summary = json.loads((self.directory / "summary.json").read_text())
        self.assertEqual(rc, 2)
        self.assertEqual(summary["Candidates"]["arn-Bool"]["Cases"][0]["Status"],
                         "OBSERVATION_INPUT_REJECTED_REVIEW_REQUIRED")
        self.assertEqual(summary["Candidates"]["star-Bool"]["Cases"][0]["Status"], "OBSERVED_NOT_RUNTIME_PROOF")
        self.assertEqual(summary["CHANNEL_SELECTION"], "NOT_MADE")


if __name__ == "__main__":
    unittest.main()
