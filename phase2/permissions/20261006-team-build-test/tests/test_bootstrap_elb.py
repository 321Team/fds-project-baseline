"""Offline tests: no AWS credentials or network calls."""
import contextlib
import copy
import importlib.util
import io
import pathlib
import subprocess
import unittest
from unittest import mock

SOURCE = pathlib.Path(__file__).resolve().parents[1] / "bootstrap-elb.py"
SPEC = importlib.util.spec_from_file_location("elb_bootstrap", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def role():
    return {"Role": {"RoleName": M.NAME, "Arn": M.ARN, "Path": M.PATH,
                     "AssumeRolePolicyDocument": {
                         "Version": "2012-10-17", "Statement": [{
                             "Effect": "Allow", "Action": "sts:AssumeRole",
                             "Principal": {"Service": M.SERVICE}}]}}}


class Calls:
    def __init__(self, responses):
        self.responses = list(responses)
        self.commands = []

    def __call__(self, *args):
        self.commands.append(args)
        if not self.responses:
            raise AssertionError("Unexpected extra call")
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response


ROOT = {"Account": M.ACCOUNT, "Arn": M.ROOT}
USER = {"Account": M.ACCOUNT,
        "Arn": "arn:aws:iam::" + M.ACCOUNT + ":user/321team-gwonuk"}


def missing():
    return M.AwsError("get-role", "NoSuchEntity", "missing")


class BootstrapTests(unittest.TestCase):
    def execute(self, calls, apply=False):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            M.run(apply=apply, call=calls)
        return output.getvalue()

    def test_default_missing_is_read_only(self):
        calls = Calls([USER, missing()])
        output = self.execute(calls)
        self.assertIn("ELB_ROLE_CHECK=ABSENT", output)
        self.assertEqual(len(calls.commands), 2)

    def test_existing_role_skips_mutation(self):
        calls = Calls([ROOT, role()])
        output = self.execute(calls, apply=True)
        self.assertIn("ELB_CREATE=SKIP_EXISTING", output)
        self.assertEqual(len(calls.commands), 2)

    def test_apply_creates_only_exact_service_once_and_reads_back(self):
        calls = Calls([ROOT, missing(), role(), role()])
        output = self.execute(calls, apply=True)
        self.assertIn("ELB_CREATE=CREATED", output)
        self.assertEqual(calls.commands[2], ("iam", "create-service-linked-role",
                                             "--aws-service-name", M.SERVICE))
        self.assertEqual(len(calls.commands), 4)

    def test_wrong_account_stops_before_role_read(self):
        calls = Calls([{"Account": "000000000000", "Arn": M.ROOT}])
        with self.assertRaises(M.Stop):
            self.execute(calls, apply=True)
        self.assertEqual(len(calls.commands), 1)

    def test_apply_rejects_nonroot_before_role_read(self):
        calls = Calls([USER])
        with self.assertRaises(M.Stop):
            self.execute(calls, apply=True)
        self.assertEqual(len(calls.commands), 1)

    def test_access_denied_is_not_absence(self):
        calls = Calls([ROOT, M.AwsError("get-role", "AccessDenied", "denied")])
        with self.assertRaises(M.AwsError):
            self.execute(calls, apply=True)
        self.assertEqual(len(calls.commands), 2)

    def test_unexpected_existing_role_stops(self):
        bad = role()
        bad["Role"]["Arn"] = bad["Role"]["Arn"].replace(M.ACCOUNT, "000000000000")
        calls = Calls([ROOT, bad])
        with self.assertRaises(M.Stop):
            self.execute(calls, apply=True)
        self.assertEqual(len(calls.commands), 2)

    def test_extra_human_trust_is_rejected(self):
        bad = role()
        bad["Role"]["AssumeRolePolicyDocument"]["Statement"].append({
            "Effect": "Allow", "Action": "sts:AssumeRole",
            "Principal": {"AWS": USER["Arn"]}})
        calls = Calls([ROOT, bad])
        with self.assertRaises(M.Stop):
            self.execute(calls, apply=True)
        self.assertEqual(len(calls.commands), 2)

    def test_create_result_unknown_is_not_retried(self):
        calls = Calls([ROOT, missing(),
                       M.AwsError("create-service-linked-role", "RESULT_UNKNOWN", "timeout")])
        with self.assertRaises(M.AwsError):
            self.execute(calls, apply=True)
        self.assertEqual(len(calls.commands), 3)

    def test_readback_failure_never_deletes_or_recreates(self):
        calls = Calls([ROOT, missing(), role(),
                       M.AwsError("get-role", "NoSuchEntity", "readback missing")])
        with self.assertRaises(M.AwsError):
            self.execute(calls, apply=True)
        self.assertEqual(len(calls.commands), 4)

    def test_cli_error_parser_distinguishes_codes(self):
        for code in ("NoSuchEntity", "AccessDenied"):
            response = subprocess.CompletedProcess([], 254, "", (
                "An error occurred (" + code + ") when calling the GetRole operation: error"))
            with mock.patch.object(M.subprocess, "run", return_value=response):
                with self.assertRaises(M.AwsError) as raised:
                    M.aws("iam", "get-role", "--role-name", M.NAME)
            self.assertEqual(raised.exception.code, code)

    def test_timeout_is_unknown_and_no_retry(self):
        with mock.patch.object(M.subprocess, "run",
                               side_effect=subprocess.TimeoutExpired(["aws"], 60)) as mocked:
            with self.assertRaises(M.AwsError) as raised:
                M.aws("iam", "create-service-linked-role",
                      "--aws-service-name", M.SERVICE)
            self.assertEqual(raised.exception.code, "RESULT_UNKNOWN")
            self.assertEqual(mocked.call_count, 1)

    def test_invalid_success_json_stops(self):
        response = subprocess.CompletedProcess([], 0, "invalid", "")
        with mock.patch.object(M.subprocess, "run", return_value=response):
            with self.assertRaises(M.AwsError):
                M.aws("iam", "get-role", "--role-name", M.NAME)


if __name__ == "__main__":
    unittest.main()

