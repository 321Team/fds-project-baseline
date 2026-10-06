#!/usr/bin/env python3
"""Compare synthetic Network permission candidates. No AWS mutations or sessions."""
import argparse
import copy
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

ACCOUNT = "774055931866"
REGION = "ap-northeast-2"
ROOT = f"arn:aws:iam::{ACCOUNT}:root"
SOURCE_MERGE = "711ad113246cf9ae6c18918ce702e3c8d3bc569c"
INPUT_HASHES = {
    "network-permissions.template.json": "bf5ff8a8538dbca287e6b3a2372fc15a491d5dbfed3a123aa51ddd30c02dd54f",
    "channel-options.review.json": "f9d87e83994a97eb5298191b3f4bab93d87707d3ec2c46124baef7cca2c997d8",
}
RELAY = "i-00000000000000000"  # Synthetic, never looked up or applied.
OTHER_RELAY = "i-00000000000000001"
DOCUMENT = "SSM-SessionManagerRunShell"
DOC_CHECK = "ssm:SessionDocumentAccessCheck"
OWNER = "ssm:resourceTag/aws:ssmmessages:session-id"
TARGET = "ssm:resourceTag/aws:ssmmessages:target-id"
ACTORS = ("321team-gwonuk", "321team-jaehwan")
READ_OPERATIONS = {
    "sts": {"get-caller-identity"},
    "ssm": {"describe-document", "get-document"},
    "accessanalyzer": {"validate-policy"},
    "iam": {"get-context-keys-for-custom-policy", "simulate-custom-policy"},
}


class Stop(RuntimeError):
    pass


class AwsError(Stop):
    def __init__(self, operation, code):
        self.operation, self.code = operation, code
        super().__init__(f"{operation}: {code}; private raw response preserved")


def compact(value):
    return json.dumps(value, ensure_ascii=True, separators=(",", ":"))


def load_inputs(directory):
    documents = {}
    for name, digest in INPUT_HASHES.items():
        raw = (Path(directory) / name).read_bytes()
        if hashlib.sha256(raw).hexdigest() != digest:
            raise Stop(f"Pinned PR141 input changed: {name}")
        documents[name] = json.loads(raw)
    return documents


def candidates(inputs):
    base = inputs["network-permissions.template.json"]
    options = inputs["channel-options.review.json"]
    result = {}
    for channel, key in (("arn", "OfficialSessionExampleCandidate"),
                         ("star", "ServiceAuthorizationResourceCandidate")):
        for operator in ("Bool", "BoolIfExists"):
            # Only bind a synthetic ID, replace the document-check operator,
            # and append one previously reviewed comparison option.
            doc = json.loads(compact(base).replace("__RELAY_INSTANCE_ID__", RELAY))
            condition = doc["Statement"][0]["Condition"]
            condition[operator] = condition.pop("Bool")
            statement = copy.deepcopy(options[key])
            statement["Sid"] = "CompareHumanOpenDataChannelOnly"
            doc["Statement"].append(statement)
            result[f"{channel}-{operator}"] = doc
    return result


def cases(operator):
    instance = f"arn:aws:ec2:{REGION}:{ACCOUNT}:instance/{RELAY}"
    other = f"arn:aws:ec2:{REGION}:{ACCOUNT}:instance/{OTHER_RELAY}"
    document = f"arn:aws:ssm:{REGION}:{ACCOUNT}:document/{DOCUMENT}"
    user_id = "AROASYNTHETICNETWORK01:" + ACTORS[0]
    session = f"arn:aws:ssm:{REGION}:{ACCOUNT}:session/{user_id}-example"
    context = {"aws:RequestedRegion": REGION, "aws:userid": user_id,
               DOC_CHECK: True, OWNER: user_id, TARGET: RELAY}
    rows = []

    def add(label, actions, resources, expected, changes=None, missing=(), observe=False):
        ctx = dict(context)
        ctx.update(changes or {})
        for key in missing:
            ctx.pop(key, None)
        if isinstance(expected, str):
            expected = {r: expected for r in resources}
        rows.append({"Label": label, "Actions": actions, "Resources": resources,
                     "Context": ctx, "ExpectedByResource": expected,
                     "IntentionalMissing": list(missing), "ObservationOnly": observe})

    for actor in ACTORS:
        uid = "AROASYNTHETICNETWORK01:" + actor
        add("start-" + actor, ["ssm:StartSession"], [instance, document], "allowed",
            {"aws:userid": uid, OWNER: uid})
        actor_session = session.replace(ACTORS[0], actor)
        add("own-session-" + actor, ["ssm:ResumeSession", "ssm:TerminateSession"],
            [actor_session], "allowed", {"aws:userid": uid, OWNER: uid})
    add("start-other-instance", ["ssm:StartSession"], [other, document],
        {other: "implicitDeny", document: "allowed"})
    for doc in ("AWS-StartPortForwardingSession", "AWS-StartSSHSession"):
        unapproved = f"arn:aws:ssm:{REGION}::document/{doc}"
        add("start-other-document-" + doc, ["ssm:StartSession"], [instance, unapproved],
            {instance: "allowed", unapproved: "implicitDeny"})
    add("document-check-false", ["ssm:StartSession"], [instance, document],
        {instance: "implicitDeny", document: "allowed"}, {DOC_CHECK: False})
    add("document-check-missing", ["ssm:StartSession"], [instance, document],
        {instance: "allowed" if operator == "BoolIfExists" else "implicitDeny",
         document: "allowed"}, missing=(DOC_CHECK,))
    add("start-outside-region", ["ssm:StartSession"], [instance, document],
        "implicitDeny", {"aws:RequestedRegion": "ap-northeast-1"})
    for label, changes, missing in (
        ("other-owner", {OWNER: "AROASYNTHETICNETWORK01:" + ACTORS[1]}, ()),
        ("other-target", {TARGET: OTHER_RELAY}, ()),
        ("owner-missing", {}, (OWNER,)),
        ("target-missing", {}, (TARGET,)),
        ("both-tags-missing", {}, (OWNER, TARGET)),
    ):
        add(label, ["ssm:ResumeSession", "ssm:TerminateSession"], [session],
            "implicitDeny", changes, missing)
    foreign_session = session.replace(ACCOUNT, "000000000001")
    add("session-foreign-account", ["ssm:ResumeSession", "ssm:TerminateSession"],
        [foreign_session], "implicitDeny")
    recovery = ["ec2:RebootInstances", "ec2:StopInstances", "ec2:StartInstances",
                "ec2:GetConsoleOutput", "ssm:GetConnectionStatus"]
    add("relay-recovery-and-read", recovery, [instance], "allowed")
    add("other-instance-recovery-and-read", recovery, [other], "implicitDeny")
    add("recovery-outside-region", recovery, [instance], "implicitDeny",
        {"aws:RequestedRegion": "ap-northeast-1"})
    diagnostics = ["ec2:DescribeInstances", "ec2:DescribeInstanceStatus",
                   "ec2:DescribeAddresses", "ec2:DescribeNetworkInterfaces",
                   "ec2:DescribeRouteTables", "ec2:DescribeSecurityGroups",
                   "ssm:DescribeInstanceInformation", "ssm:DescribeSessions",
                   "cloudwatch:GetMetricData"]
    add("regional-account-diagnostics", diagnostics, ["*"], "allowed")
    add("diagnostics-outside-region", diagnostics, ["*"], "implicitDeny",
        {"aws:RequestedRegion": "ap-northeast-1"})
    add("excluded-instance-actions", ["ec2:TerminateInstances", "ec2:ModifyInstanceAttribute",
        "ec2:CreateTags", "ec2:DeleteTags", "ssm:SendCommand"], [instance], "implicitDeny")
    add("excluded-structure-and-privilege", ["ec2:CreateRoute", "ec2:DeleteRoute",
        "ec2:AuthorizeSecurityGroupIngress", "ec2:AllocateAddress", "iam:CreateRole",
        "iam:PassRole", "secretsmanager:GetSecretValue", "ssm:GetParameter", "kms:Decrypt"],
        ["*"], "implicitDeny")
    add("excluded-agent-channels", ["ssmmessages:CreateControlChannel",
        "ssmmessages:CreateDataChannel", "ssmmessages:OpenControlChannel"], ["*"], "implicitDeny")
    for label, resource in (("own", session),
                            ("other", session.replace(ACTORS[0], ACTORS[1])), ("star", "*")):
        add("channel-observe-" + label, ["ssmmessages:OpenDataChannel"],
            [resource], {}, observe=True)
    add("channel-observe-outside-region", ["ssmmessages:OpenDataChannel"], ["*"], {},
        {"aws:RequestedRegion": "ap-northeast-1"}, observe=True)
    return rows


def request(policy, case):
    entries = [{"ContextKeyName": key,
                "ContextKeyValues": [str(value).lower() if isinstance(value, bool) else value],
                "ContextKeyType": "boolean" if isinstance(value, bool) else "string"}
               for key, value in case["Context"].items()]
    return {"PolicyInputList": [compact(policy)], "ActionNames": case["Actions"],
            "ResourceArns": case["Resources"], "ContextEntries": entries}


def inspect_result(result, case):
    """Require full action/resource coverage; never reuse aggregate for multiple ARNs."""
    if result.get("IsTruncated") or result.get("Marker"):
        raise Stop("Incomplete simulation response")
    rows = result.get("EvaluationResults")
    if not isinstance(rows, list) or len(rows) != len(case["Actions"]):
        raise Stop("Missing/duplicate simulation actions")
    actions = [row.get("EvalActionName", "").lower() for row in rows]
    if len(set(actions)) != len(actions) or set(actions) != {a.lower() for a in case["Actions"]}:
        raise Stop("Unexpected simulation actions")
    observed = []
    for row in rows:
        if row.get("EvalDecision") not in {"allowed", "implicitDeny", "explicitDeny"}:
            raise Stop("Invalid aggregate simulation decision")
        resources = row.get("ResourceSpecificResults")
        level = "RESOURCE_SPECIFIC"
        if not resources:
            # '*': aggregate is sufficient. Legacy exact single-resource output
            # is accepted only when it identifies that exact requested ARN.
            if case["Resources"] == ["*"] or (
                len(case["Resources"]) == 1 and row.get("EvalResourceName") == case["Resources"][0]
            ):
                resources = [{"EvalResourceName": case["Resources"][0],
                              "EvalResourceDecision": row.get("EvalDecision"),
                              "MissingContextValues": row.get("MissingContextValues", [])}]
                level = "SINGLE_RESOURCE_AGGREGATE"
            elif case["ObservationOnly"]:
                observed.append({"Action": row["EvalActionName"], "Aggregate": row.get("EvalDecision"),
                                 "MissingContextValues": row.get("MissingContextValues", []),
                                 "EvidenceLevel": "AGGREGATE_ONLY_NO_ARN_INFERENCE"})
                continue
            else:
                raise Stop("No exact per-resource evidence; aggregate cannot identify the requested ARNs")
        names = [r.get("EvalResourceName") for r in resources]
        if len(set(names)) != len(names) or set(names) != set(case["Resources"]):
            raise Stop("Missing/duplicate/unexpected simulation resources")
        for resource in resources:
            name = resource["EvalResourceName"]
            decision = resource.get("EvalResourceDecision")
            missing = resource.get("MissingContextValues", [])
            if decision not in {"allowed", "implicitDeny", "explicitDeny"}:
                raise Stop("Invalid simulation decision")
            if not case["ObservationOnly"]:
                if decision != case["ExpectedByResource"][name]:
                    raise Stop(f"Unexpected decision: {case['Label']} {row['EvalActionName']} {name} {decision}")
                unexpected_missing = set(missing) - set(case["IntentionalMissing"])
                if unexpected_missing or (decision == "allowed" and
                    set(row.get("MissingContextValues", [])) - set(case["IntentionalMissing"])):
                    raise Stop("Unexpected missing simulation context")
            observed.append({"Action": row["EvalActionName"], "Resource": name,
                             "Decision": decision, "MissingContextValues": missing,
                             "EvidenceLevel": level})
    return observed


class Capture:
    def __init__(self, directory, runner=subprocess.run):
        self.directory, self.runner = Path(directory), runner
        self.number = 0

    def write(self, name, value):
        path = self.directory / name
        with path.open("xb") as stream:
            os.chmod(path, 0o600)
            if not isinstance(value, (str, bytes)):
                value = json.dumps(value, ensure_ascii=True, indent=2) + "\n"
            stream.write(value.encode("utf-8") if isinstance(value, str) else value)
        return path

    def call(self, label, service, operation, *args):
        if operation not in READ_OPERATIONS.get(service, set()):
            raise Stop("AWS operation outside read-only precheck allowlist")
        self.number += 1
        prefix = f"{self.number:03d}-{label}"
        command = ["aws", service, operation, *args, "--region", REGION,
                   "--output", "json", "--no-cli-pager"]
        try:
            response = self.runner(command, capture_output=True, text=True, timeout=60, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            self.write(prefix + "-partial-stdout.txt", getattr(exc, "stdout", None) or "")
            self.write(prefix + "-partial-stderr.txt", getattr(exc, "stderr", None) or "")
            self.write(prefix + "-error.json", {"Operation": operation, "Error": type(exc).__name__})
            raise AwsError(operation, type(exc).__name__) from exc
        self.write(prefix + "-stdout.txt", response.stdout)
        self.write(prefix + "-stderr.txt", response.stderr)
        self.write(prefix + "-status.json", {"Operation": operation, "RC": response.returncode})
        if response.returncode:
            match = re.search(r"\(([A-Za-z0-9]+)\) when calling", response.stderr)
            raise AwsError(operation, match.group(1) if match else "UNCLASSIFIED")
        try:
            data = json.loads(response.stdout)
        except ValueError as exc:
            raise AwsError(operation, "INVALID_JSON") from exc
        if not isinstance(data, dict):
            raise AwsError(operation, "NON_OBJECT_JSON")
        return data

    def manifest(self):
        paths = sorted(p for p in self.directory.iterdir() if p.is_file() and p.name != "SHA256SUMS")
        return self.write("SHA256SUMS", "".join(
            f"{hashlib.sha256(p.read_bytes()).hexdigest()}  ./{p.name}\n" for p in paths))


def document_capture(cap):
    try:
        before = cap.call("document-before", "ssm", "describe-document", "--name", DOCUMENT)["Document"]
    except AwsError as exc:
        if exc.operation == "describe-document" and exc.code == "InvalidDocument":
            return {"State": "ABSENT_OR_UNAVAILABLE", "ContentRead": False,
                    "HandoffRequired": "Create/configure approved document by its responsible owner; not this collector"}
        raise
    content = cap.call("document-content", "ssm", "get-document", "--name", DOCUMENT,
                       "--document-version", "$DEFAULT", "--document-format", "JSON")
    after = cap.call("document-after", "ssm", "describe-document", "--name", DOCUMENT)["Document"]
    keys = ("Name", "Owner", "DocumentType", "DefaultVersion", "Hash", "HashType", "Status")
    if {k: before.get(k) for k in keys} != {k: after.get(k) for k in keys}:
        raise Stop("SSM document metadata/default-version changed during capture")
    if (before.get("Name") != DOCUMENT or before.get("Owner") != ACCOUNT or
        before.get("DocumentType") != "Session" or before.get("Status") != "Active" or
        content.get("DocumentVersion") != before.get("DefaultVersion") or
        content.get("DocumentType") != "Session" or content.get("Name") != DOCUMENT):
        raise Stop("Document owner/type/name/status/default-version requires review")
    doc = json.loads(content["Content"])
    if not isinstance(doc, dict) or doc.get("sessionType") != "Standard_Stream":
        raise Stop("Default document is not the reviewed Standard_Stream shell")
    inputs = doc.get("inputs", {})
    if not isinstance(inputs, dict):
        raise Stop("Malformed session document inputs")
    return {"State": "CAPTURED_NOT_RUNTIME_TESTED", "Owner": before["Owner"],
            "DefaultVersion": before["DefaultVersion"], "SessionType": doc["sessionType"],
            "ContentUTF8SHA256": hashlib.sha256(content["Content"].encode()).hexdigest(),
            "KmsKeyId": inputs.get("kmsKeyId"), "S3BucketName": inputs.get("s3BucketName"),
            "CloudWatchLogGroupName": inputs.get("cloudWatchLogGroupName")}


def run(cap, inputs, offline=False):
    summary = {"SourceMerge": SOURCE_MERGE, "InputSHA256": INPUT_HASHES,
        "Target": "SYNTHETIC_ONLY", "SyntheticInstanceId": RELAY,
        "UTC": dt.datetime.now(dt.timezone.utc).isoformat(),
        "TRUST_RUNTIME": "NOT_TESTED", "USER_EFFECTIVE_PERMISSION": "NOT_TESTED",
        "SERVICE_CONTEXT": "SYNTHETIC_NOT_OBSERVED", "CHANNEL_SELECTION": "NOT_MADE",
        "FINAL_POLICY": "NOT_CREATED", "ROLE_GRANT": "NOT_RUN", "AWS_MUTATION": "NOT_RUN",
        "APPLY_READINESS": "NOT_ASSESSED", "Candidates": {}}
    rc = 0
    try:
        if not offline:
            identity = cap.call("identity", "sts", "get-caller-identity")
            if identity.get("Arn") != ROOT or identity.get("Account") != ACCOUNT:
                raise Stop("Requires exact education account root for central candidate collection")
            summary["ExecutionArn"] = identity["Arn"]
            summary["Document"] = document_capture(cap)
        for name, policy in candidates(inputs).items():
            operator = name.split("-", 1)[1]
            path = cap.write(name + "-SYNTHETIC-NOT-FOR-ATTACHMENT.json", policy)
            matrix = cases(operator)
            state = {"PolicySHA256": hashlib.sha256(path.read_bytes()).hexdigest(),
                     "CasesPlanned": len(matrix), "Cases": [], "Validation": "NOT_RUN"}
            summary["Candidates"][name] = state
            if not offline:
                validated = cap.call(name + "-validate", "accessanalyzer", "validate-policy",
                    "--policy-type", "IDENTITY_POLICY", "--policy-document", "file://" + str(path))
                if validated.get("nextToken"):
                    raise Stop("Uncollected validation findings page")
                findings = validated.get("findings")
                if not isinstance(findings, list):
                    raise Stop("Malformed validation findings")
                state["Validation"] = "NO_FINDINGS" if not findings else "FINDINGS_REVIEW_REQUIRED"
                state["Findings"] = findings
                if findings:
                    rc = 2
                if any(f.get("findingType") == "ERROR" for f in findings):
                    state["Matrix"] = "SKIPPED_VALIDATION_ERRORS"
                    print(f"CANDIDATE={name} VALIDATION=ERROR MATRIX=SKIPPED", flush=True)
                    continue
                cap.call(name + "-context-keys", "iam", "get-context-keys-for-custom-policy",
                         "--policy-input-list", compact(policy))
            for i, case in enumerate(matrix, 1):
                input_path = cap.write(f"{name}-{i:02d}-input.json", request(policy, case))
                cap.write(f"{name}-{i:02d}-expectations.json", case)
                if offline:
                    continue
                try:
                    response = cap.call(f"{name}-{i:02d}", "iam", "simulate-custom-policy",
                                        "--cli-input-json", "file://" + str(input_path))
                except AwsError as exc:
                    if not case["ObservationOnly"] or exc.code != "InvalidInput":
                        raise
                    # Rejected experimental channel input is not an IAM deny or
                    # proof of service scoping. Preserve it and compare fixed options.
                    state["Cases"].append({"Label": case["Label"],
                        "Status": "OBSERVATION_INPUT_REJECTED_REVIEW_REQUIRED", "Code": exc.code})
                    rc = 2
                    print(f"CANDIDATE={name} CASE={i:02d} RESULT=OBSERVATION_INPUT_REJECTED", flush=True)
                    continue
                observed = inspect_result(response, case)
                status = "OBSERVED_NOT_RUNTIME_PROOF" if case["ObservationOnly"] else "EXPECTED_POLICY_MATCH"
                state["Cases"].append({"Label": case["Label"], "Status": status, "Observed": observed})
                print(f"CANDIDATE={name} CASE={i:02d} LABEL={case['Label']} RESULT={status}", flush=True)
            state["Matrix"] = "OFFLINE_INPUTS_PREPARED" if offline else "COLLECTED"
        summary["Collection"] = "OFFLINE_PREPARED" if offline else (
            "COLLECTED_REVIEW_REQUIRED" if rc else "COLLECTED_NO_VALIDATION_FINDINGS")
        cap.write("summary.json", summary)
    except Exception as exc:
        summary["Collection"] = "STOPPED_PARTIAL"
        cap.write("failure-summary.json", {"ErrorType": type(exc).__name__, "Reason": str(exc),
                                            "Partial": summary})
        raise
    finally:
        # No COMPLETE marker if evidence/manifest persistence fails.
        cap.manifest()
    print("OFFLINE_PREPARE=COMPLETE" if offline else "NETWORK_CANDIDATE_CAPTURE=COMPLETE", flush=True)
    print("CHANNEL_SELECTION=NOT_MADE FINAL_POLICY=NOT_CREATED ROLE_GRANT=NOT_RUN AWS_MUTATION=NOT_RUN", flush=True)
    print("APPLY_READINESS=NOT_ASSESSED", flush=True)
    return rc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs-dir", type=Path, default=Path(__file__).resolve().parent / "inputs")
    parser.add_argument("--output-parent", type=Path, default=Path.home())
    parser.add_argument("--offline", action="store_true", help="Prepare synthetic inputs; invoke no AWS command")
    args = parser.parse_args()
    os.umask(0o077)
    directory = None
    try:
        inputs = load_inputs(args.inputs_dir)  # Fail before AWS if sources changed.
        directory = Path(tempfile.mkdtemp(prefix="fds-network-permission-precheck-", dir=args.output_parent))
        print("CAPTURE_DIR=" + str(directory), flush=True)
        cap = Capture(directory)
        cap.write("collector-source.py", Path(__file__).read_text(encoding="utf-8"))
        for name in INPUT_HASHES:
            cap.write(name, (args.inputs_dir / name).read_text(encoding="utf-8"))
        return run(cap, inputs, args.offline)
    except (Stop, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"STOP: {exc}", file=sys.stderr)
        if directory:
            print("PRESERVED_DIR=" + str(directory), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
