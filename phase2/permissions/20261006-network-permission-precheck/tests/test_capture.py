import contextlib
import copy
import importlib.util
import io
import hashlib
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


class ResumeTests(unittest.TestCase):
    """CLI/evidence orchestration fixtures; these do not evaluate an IAM policy."""
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.parent = Path(self.temp.name)
        self.inputs = p.load_inputs(SOURCE.parent / "inputs")
        self.start = p.cases("Bool")[0]
        self.observe = p.cases("Bool")[24]
        self.matrix = [self.start, self.observe]
        self.start_response = {"EvaluationResults": [{"EvalActionName": "ssm:StartSession",
            "EvalDecision": "allowed", "ResourceSpecificResults": [
                {"EvalResourceName": self.start["Resources"][0], "EvalResourceDecision": "allowed"},
                {"EvalResourceName": self.start["Resources"][1], "EvalResourceDecision": "allowed"}]}]}
        self.observe_response = {"EvaluationResults": [{"EvalActionName": "ssmmessages:OpenDataChannel",
            "EvalDecision": "allowed", "EvalResourceName": "*"}]}
        self.commands = []

    def tearDown(self):
        self.temp.cleanup()

    def cap(self, name, runner):
        directory = self.parent / name
        directory.mkdir()
        cap = p.Capture(directory, runner)
        cap.write("collector-source.py", SOURCE.read_bytes())
        for filename in p.INPUT_HASHES:
            cap.write(filename, (SOURCE.parent / "inputs" / filename).read_bytes())
        return cap

    def runner(self, failed_input=None):
        def invoke(command, **kwargs):
            self.commands.append(command)
            operation = command[2]
            rc, stderr = 0, ""
            if operation == "get-caller-identity":
                response = {"Account": p.ACCOUNT, "Arn": p.ROOT}
            elif operation == "describe-document":
                rc, stderr, response = 254, "(InvalidDocument) when calling DescribeDocument", {}
            elif operation == "validate-policy":
                response = {"findings": []}
            elif operation == "get-context-keys-for-custom-policy":
                response = {"ContextKeyNames": []}
            elif operation == "simulate-custom-policy":
                input_path = Path(command[command.index("--cli-input-json") + 1][7:])
                if input_path.name == failed_input:
                    raise subprocess.TimeoutExpired("aws", 60, output=b"partial raw")
                # Two literal response fixtures, selected by request kind only.
                # No allow/deny is derived from policy or ExpectedByResource.
                response = self.start_response if input_path.name.endswith("01-input.json") else self.observe_response
            else:
                raise AssertionError(operation)
            return subprocess.CompletedProcess(command, rc, json.dumps(response), stderr)
        return invoke

    def interrupted(self):
        cap = self.cap("original", self.runner("arn-Bool-02-input.json"))
        with patch.object(p, "cases", return_value=self.matrix), patch.object(p.time, "sleep"), \
             contextlib.redirect_stdout(io.StringIO()), self.assertRaises(p.AwsError):
            p.run(cap, self.inputs)
        return cap.directory

    def resign(self, directory):
        (directory / "SHA256SUMS").unlink()
        p.Capture(directory).manifest()

    def test_bounded_retry_preserves_attempts_and_child_settings(self):
        calls = []
        def runner(command, **kwargs):
            calls.append((command, kwargs))
            if len(calls) == 1:
                raise subprocess.TimeoutExpired("aws", 60, output=b"partial\xff")
            return subprocess.CompletedProcess(command, 0, "{}", "")
        cap = self.cap("retry", runner)
        with patch.object(p.time, "sleep") as sleep, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(cap.call("case", "iam", "simulate-custom-policy"), {})
        self.assertEqual(len(calls), 2)
        self.assertEqual((cap.directory / "001-case-partial-stdout.txt").read_bytes(), b"partial\xff")
        self.assertEqual(cap.last_evidence["Stdout"], "002-case-stdout.txt")
        self.assertEqual(calls[0][1]["timeout"], 60)
        self.assertEqual(calls[0][1]["env"]["AWS_MAX_ATTEMPTS"], "1")
        self.assertIn("--cli-read-timeout", calls[0][0])
        sleep.assert_called_once_with(3)

    def test_access_denied_is_not_retried(self):
        with patch.object(p.subprocess, "run", return_value=subprocess.CompletedProcess(
            [], 254, "", "(AccessDenied) when calling SimulateCustomPolicy")) as runner:
            cap = self.cap("denied", runner)
            with self.assertRaises(p.AwsError):
                cap.call("case", "iam", "simulate-custom-policy")
            self.assertEqual(runner.call_count, 1)

    def test_cli_read_timeout_is_bounded_and_classified(self):
        runner = lambda cmd, **kw: subprocess.CompletedProcess(cmd, 255, "", "Read timeout on endpoint URL: https://example")
        cap = self.cap("read-timeout", runner)
        with patch.object(p.time, "sleep"), contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(p.AwsError) as error:
                cap.call("case", "iam", "simulate-custom-policy")
        self.assertEqual(error.exception.code, "ReadTimeoutError")
        self.assertEqual(cap.number, 2)

    def test_resume_reparses_raw_and_never_repeats_completed_request(self):
        original = self.interrupted()
        original_bytes = {f.name: f.read_bytes() for f in original.iterdir()}
        self.commands.clear()
        with patch.object(p, "cases", return_value=self.matrix):
            resume = p.ResumeEvidence(original, self.inputs)
            cap = self.cap("continued", self.runner())
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(p.run(cap, self.inputs, resume=resume), 0)
        simulated = [Path(c[c.index("--cli-input-json") + 1][7:]).name
                     for c in self.commands if c[2] == "simulate-custom-policy"]
        self.assertEqual(len(simulated), 7)
        self.assertNotIn("arn-Bool-01-input.json", simulated)
        self.assertIn("arn-Bool-02-input.json", simulated)
        self.assertEqual(original_bytes, {f.name: f.read_bytes() for f in original.iterdir()})
        summary = json.loads((cap.directory / "summary.json").read_bytes())
        self.assertEqual(summary["Resume"]["ReusedCases"], 1)
        self.assertEqual(summary["Resume"]["FreshCases"], 7)
        self.assertEqual(summary["CHANNEL_SELECTION"], "NOT_MADE")

    def test_manifest_tampering_stops_before_aws(self):
        original = self.interrupted()
        (original / "arn-Bool-01-input.json").write_text("{}")
        with patch.object(p.subprocess, "run") as runner, self.assertRaises(p.Stop):
            p.ResumeEvidence(original, self.inputs)
        runner.assert_not_called()

    def test_resigned_changed_request_and_forged_summary_are_rejected(self):
        original = self.interrupted()
        input_path = original / "arn-Bool-01-input.json"
        raw = input_path.read_bytes()
        input_path.write_text("{}")
        self.resign(original)
        with patch.object(p, "cases", return_value=self.matrix), self.assertRaises(p.Stop):
            p.ResumeEvidence(original, self.inputs)
        input_path.write_bytes(raw)
        failure_path = original / "failure-summary.json"
        failure = json.loads(failure_path.read_bytes())
        failure["Partial"]["Candidates"]["arn-Bool"]["Cases"][0]["Observed"][0]["Decision"] = "implicitDeny"
        failure_path.write_text(json.dumps(failure))
        self.resign(original)
        with patch.object(p, "cases", return_value=self.matrix), self.assertRaises(p.Stop):
            p.ResumeEvidence(original, self.inputs)

    def test_document_drift_stops_before_simulator_reuse_or_new_calls(self):
        original = self.interrupted()
        self.commands.clear()
        with patch.object(p, "cases", return_value=self.matrix):
            resume = p.ResumeEvidence(original, self.inputs)
            cap = self.cap("drift", self.runner())
            with patch.object(p, "document_capture", return_value={"State": "DIFFERENT"}), \
                 contextlib.redirect_stdout(io.StringIO()), self.assertRaises(p.Stop):
                p.run(cap, self.inputs, resume=resume)
        self.assertFalse(any(c[2] == "simulate-custom-policy" for c in self.commands))
        self.assertFalse((cap.directory / "summary.json").exists())

    def test_resigned_prior_identity_cannot_be_overridden_by_summary(self):
        original = self.interrupted()
        identity = original / "001-identity-stdout.txt"
        identity.write_text(json.dumps({"Account": p.ACCOUNT,
                                       "Arn": f"arn:aws:iam::{p.ACCOUNT}:user/321team-gwonuk"}))
        self.resign(original)
        with patch.object(p, "cases", return_value=self.matrix), self.assertRaises(p.Stop):
            p.ResumeEvidence(original, self.inputs)

    def test_a_second_interruption_can_resume_copied_provenance(self):
        original = self.interrupted()
        with patch.object(p, "cases", return_value=self.matrix), patch.object(p.time, "sleep"), \
             contextlib.redirect_stdout(io.StringIO()):
            resume = p.ResumeEvidence(original, self.inputs)
            second = self.cap("second", self.runner("arn-BoolIfExists-01-input.json"))
            with self.assertRaises(p.AwsError):
                p.run(second, self.inputs, resume=resume)
            chained = p.ResumeEvidence(second.directory, self.inputs)
            self.assertEqual(len(chained.completed), 2)
            third = self.cap("third", self.runner())
            self.assertEqual(p.run(third, self.inputs, resume=chained), 0)
        self.assertTrue((third.directory / "prior-prior-SHA256SUMS").exists())

    def test_legacy_summary_without_evidence_references_is_reparsed(self):
        original = self.interrupted()
        path = original / "failure-summary.json"
        failure = json.loads(path.read_bytes())
        del failure["Partial"]["Candidates"]["arn-Bool"]["Cases"][0]["Evidence"]
        path.write_text(json.dumps(failure))
        self.resign(original)
        # Exercise the legacy response naming branch with the pinned fixture
        # source; this mock does not assert a real legacy AWS execution.
        digest = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
        with patch.object(p, "LEGACY_COLLECTOR_SHA256", digest), patch.object(p, "cases", return_value=self.matrix):
            resume = p.ResumeEvidence(original, self.inputs)
        self.assertEqual(len(resume.completed), 1)

    def test_role_session_name_observations_append_without_changing_old_numbering(self):
        rows = p.cases("Bool")
        self.assertEqual(rows[4]["Label"], "start-other-instance")
        self.assertEqual(rows[27]["Label"], "channel-observe-outside-region")
        self.assertEqual(len(rows), 30)
        for row, actor in zip(rows[28:], p.ACTORS):
            self.assertTrue(row["ObservationOnly"])
            self.assertEqual(row["ExpectedByResource"], {})
            self.assertIn("session/" + actor + "-", row["Resources"][0])
            self.assertIn("AROA", row["Context"]["aws:userid"])


if __name__ == "__main__":
    unittest.main()
