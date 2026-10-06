#!/usr/bin/env python3
"""Read-only AWS validation of PR145's partial inputs. Never grant or apply."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile

ACCOUNT = "774055931866"
REGION = "ap-northeast-2"
ROOT = f"arn:aws:iam::{ACCOUNT}:root"
IAC = f"arn:aws:iam::{ACCOUNT}:role/FDS-IaC-Operator"
RELAY = f"arn:aws:iam::{ACCOUNT}:role/FDS-Relay-SSM"
PROFILE = f"arn:aws:iam::{ACCOUNT}:instance-profile/FDS-Relay-SSM"
BUCKET = "fds-tfstate-774055931866-ap-northeast-2"
S3 = f"arn:aws:s3:::{BUCKET}"
COMPONENTS = ("network", "vpn", "rosa-prereq", "rosa-runtime")
USERS = ("321team-gwonuk", "321team-hayeoung", "321team-jaehwan")
SOURCE_MERGE = "f1e66492ca87f21d99d9848ab8606cd08185b9ff"
SOURCE_HASHES = {
    "candidates/iac-backend-passrole.candidate.json": "53eb7e501658c54d7e63802899731fccf49cc0d7de4ae18d87c996c7a9561562",
    "candidates/state-bucket-policy.candidate.json": "05f66bd2f8041dd14f032a166cfe9ab2abfb307024d2d0452e9fef47d6ae5813",
    "inputs/lead-values.json": "255321f7ea1a91cb27399e49467fa46bcff503d1d31dbad1eb8b14b0fbf50221",
}
READ_OPERATIONS = {
    "sts": {"get-caller-identity"},
    "iam": {"get-user", "get-role", "get-instance-profile", "list-role-policies",
            "get-role-policy", "list-attached-role-policies", "get-policy",
            "get-policy-version", "simulate-custom-policy"},
    "s3api": {"get-bucket-location", "get-bucket-versioning", "get-bucket-encryption",
              "get-public-access-block", "get-bucket-ownership-controls", "get-bucket-policy"},
    "accessanalyzer": {"validate-policy"},
}


class Stop(RuntimeError):
    pass


class AwsError(Stop):
    def __init__(self, operation, code):
        self.operation, self.code = operation, code
        super().__init__(f"{operation}: {code}; private response preserved")


def compact(value):
    return json.dumps(value, ensure_ascii=True, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(value).hexdigest()


def load_source(directory):
    documents = {}
    for name, expected in SOURCE_HASHES.items():
        data = (directory / name).read_bytes()
        if digest(data) != expected:
            raise Stop(f"Pinned PR145 bytes differ: {name}")
        documents[name] = json.loads(data)
    return documents


class Capture:
    def __init__(self, directory, runner=subprocess.run):
        self.directory, self.runner = Path(directory), runner
        self.number = 0

    def save(self, name, value):
        path = self.directory / name
        path.write_text(json.dumps(value, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
        path.chmod(0o600)
        return path

    def cli_version(self):
        try:
            result = self.runner(["aws", "--version"], capture_output=True, text=True,
                                 timeout=10, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise Stop("Cannot capture AWS CLI version") from exc
        value = (result.stdout or result.stderr).strip()
        if result.returncode or not value.startswith("aws-cli/2."):
            raise Stop("AWS CLI v2 is required")
        self.save("cli-version.json", {"AWSCLI": value})
        return value

    def call(self, label, service, operation, *args):
        if operation not in READ_OPERATIONS.get(service, set()):
            raise Stop(f"Operation outside read-only allowlist: {service} {operation}")
        if len(args) % 2 or any(not str(args[i]).startswith("--") for i in range(0, len(args), 2)):
            raise Stop("Malformed internal AWS arguments")
        # No caller-supplied CLI flags/endpoints. AWS credential env is inherited, never logged.
        for attempt in range(1, 3):
            self.number += 1
            name = f"{self.number:03d}-{label}-attempt{attempt}"
            env = os.environ.copy()
            env.update(AWS_MAX_ATTEMPTS="1", AWS_PAGER="", AWS_CLI_AUTO_PROMPT="off")
            command = ["aws", service, operation, *args, "--region", REGION,
                       "--output", "json", "--no-cli-pager", "--cli-connect-timeout", "5",
                       "--cli-read-timeout", "25"]
            try:
                result = self.runner(command, capture_output=True, text=True, timeout=40,
                                     check=False, env=env)
            except subprocess.TimeoutExpired as exc:
                self.save(name + ".json", {"Operation": operation, "Error": "TimeoutExpired"})
                for suffix, partial in (("stdout", exc.stdout), ("stderr", exc.stderr)):
                    if partial is not None:
                        path = self.directory / (name + "." + suffix)
                        path.write_bytes(partial if isinstance(partial, bytes) else partial.encode())
                        path.chmod(0o600)
                if attempt == 1:
                    continue
                raise AwsError(operation, "TIMEOUT")
            except OSError as exc:
                self.save(name + ".json", {"Operation": operation, "Error": type(exc).__name__})
                raise AwsError(operation, "CLI_UNAVAILABLE") from exc
            # Preserve complete API bytes only in the private capture, not stdout.
            raw = self.directory / (name + ".stdout")
            raw.write_text(result.stdout, encoding="utf-8")
            raw.chmod(0o600)
            if result.returncode:
                match = re.search(r"\(([A-Za-z0-9]+)\) when calling", result.stderr)
                code = match.group(1) if match else "UNCLASSIFIED"
                self.save(name + ".json", {"Operation": operation, "RC": result.returncode,
                                          "Code": code, "Stderr": result.stderr})
                if attempt == 1 and code in {"Throttling", "ThrottlingException", "ServiceUnavailable", "RequestTimeout"}:
                    continue
                raise AwsError(operation, code)
            try:
                data = json.loads(result.stdout)
            except ValueError as exc:
                raise AwsError(operation, "INVALID_JSON") from exc
            if not isinstance(data, dict):
                raise AwsError(operation, "INVALID_RESPONSE_OBJECT")
            # CLI auto-pagination remains on; any residual token is an incomplete capture.
            if any(data.get(key) for key in ("NextToken", "nextToken", "Marker", "NextMarker", "IsTruncated")):
                raise AwsError(operation, "INCOMPLETE_PAGINATION")
            return data

    def optional(self, label, service, operation, absent_codes, *args):
        try:
            return self.call(label, service, operation, *args)
        except AwsError as exc:
            if exc.code not in absent_codes:
                raise
            return {"CaptureState": "ABSENT", "Code": exc.code}


def context(principal=IAC, region=REGION, tls=True, **extra):
    values = {"aws:PrincipalArn": principal, "aws:RequestedRegion": region,
              "aws:SecureTransport": tls, "aws:PrincipalIsAWSService": False, **extra}
    return [{"ContextKeyName": key, "ContextKeyType": "boolean" if isinstance(value, bool) else "string",
             "ContextKeyValues": [str(value).lower() if isinstance(value, bool) else value]}
            for key, value in values.items()]


def simulation_cases(identity, bucket_policy):
    cases = []

    def add(label, actions, resource, expected, ctx=None, caller=None):
        if caller:
            # Explicit Deny override fixture, NOT the caller's current RO/guard/effective policies.
            policies = [{"Version": "2012-10-17", "Statement": [{"Effect": "Allow", "Action": actions, "Resource": resource}]}]
        else:
            policies = [identity]
        request = {"PolicyInputList": [compact(p) for p in policies], "ActionNames": actions,
                   "ResourceArns": [resource], "ContextEntries": ctx if ctx is not None else context()}
        if caller:
            request.update(ResourcePolicy=compact(bucket_policy), CallerArn=caller, ResourceOwner=ROOT)
        cases.append({"Label": label, "Expected": expected,
                      "Scope": "BUCKET_DENY_OVERRIDE_FIXTURE" if caller else "PARTIAL_IDENTITY_ONLY",
                      "Request": request})

    for component in COMPONENTS:
        state = f"{S3}/phase2/{component}/terraform.tfstate"
        add(component + "-state", ["s3:GetObject", "s3:PutObject"], state, "allowed")
        add(component + "-lock", ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"], state + ".tflock", "allowed")
    state = f"{S3}/phase2/network/terraform.tfstate"
    add("state-delete", ["s3:DeleteObject", "s3:DeleteObjectVersion"], state, "explicitDeny")
    add("lock-version-delete", ["s3:DeleteObjectVersion"], state + ".tflock", "explicitDeny")
    for label, target in [("other-key", S3 + "/phase2/other/terraform.tfstate"),
                          ("other-bucket", "arn:aws:s3:::fds-unapproved-fixture/phase2/network/terraform.tfstate"),
                          ("nondefault-workspace", S3 + "/env:/other/phase2/network/terraform.tfstate")]:
        add(label, ["s3:GetObject", "s3:PutObject"], target, "implicitDeny")
    add("outside-region", ["s3:GetObject", "s3:PutObject"], state, "implicitDeny", context(region="ap-northeast-1"))
    add("insecure", ["s3:GetObject", "s3:PutObject"], state, "implicitDeny", context(tls=False))
    add("wrong-principal", ["s3:GetObject"], state, "implicitDeny", context(principal=f"arn:aws:iam::{ACCOUNT}:user/{USERS[0]}"))
    for prefix in ("phase2/", "env:/"):
        add("list-" + ("phase2" if prefix == "phase2/" else "workspace"), ["s3:ListBucket"], S3, "allowed", context(**{"s3:prefix": prefix}))
    add("list-other-prefix", ["s3:ListBucket"], S3, "implicitDeny", context(**{"s3:prefix": "other/"}))
    add("read-relay-role", ["iam:GetRole"], RELAY, "allowed", context(region="us-east-1"))
    add("read-relay-profile", ["iam:GetInstanceProfile"], PROFILE, "allowed", context(region="us-east-1"))
    add("pass-relay-ec2", ["iam:PassRole"], RELAY, "allowed", context(**{"iam:PassedToService": "ec2.amazonaws.com"}))
    add("pass-other-role", ["iam:PassRole"], IAC, "implicitDeny", context(**{"iam:PassedToService": "ec2.amazonaws.com"}))
    add("pass-other-service", ["iam:PassRole"], RELAY, "implicitDeny", context(**{"iam:PassedToService": "lambda.amazonaws.com"}))
    add("pass-profile", ["iam:PassRole"], PROFILE, "implicitDeny", context(**{"iam:PassedToService": "ec2.amazonaws.com"}))
    add("edit-protected-role", ["iam:PutRolePolicy", "iam:UpdateAssumeRolePolicy"], RELAY, "explicitDeny")
    add("edit-protected-profile", ["iam:AddRoleToInstanceProfile"], PROFILE, "explicitDeny")
    add("edit-protected-bucket", ["s3:PutBucketPolicy", "s3:DeleteBucket"], S3, "explicitDeny")
    # S3 resource policy is supplied in ResourcePolicy, never in PolicyInputList.
    for user in USERS:
        caller = f"arn:aws:iam::{ACCOUNT}:user/{user}"
        for component in COMPONENTS:
            target = f"{S3}/phase2/{component}/terraform.tfstate"
            add(user + "-" + component + "-payload", ["s3:GetObject", "s3:GetObjectVersion", "s3:PutObject"],
                target, "explicitDeny", context(principal=caller, **{"s3:x-amz-server-side-encryption": "AES256"}), caller)
        add(user + "-lock-payload", ["s3:GetObject", "s3:DeleteObject"], state + ".tflock",
            "explicitDeny", context(principal=caller), caller)
        add(user + "-bucket-metadata", ["s3:GetBucketLocation"], S3, "allowed", context(principal=caller), caller)
    return cases


def check_simulation(case, response):
    request, expected = case["Request"], case["Expected"]
    rows = response.get("EvaluationResults")
    actions = {a.lower() for a in request["ActionNames"]}
    if not isinstance(rows, list) or len(rows) != len(actions):
        raise Stop("Simulation response action cardinality differs")
    if not all(isinstance(r, dict) for r in rows):
        raise Stop("Simulation response row is not an object")
    if {r.get("EvalActionName", "").lower() for r in rows} != actions:
        raise Stop("Simulation response actions differ")
    for row in rows:
        if row.get("EvalDecision") != expected:
            raise Stop("Simulation decision differs: " + case["Label"])
        # One exact resource per request handles both legacy and aggregate response shapes.
        per_resource = row.get("ResourceSpecificResults", [])
        if not isinstance(per_resource, list):
            raise Stop("Per-resource response is not an array")
        if per_resource:
            if len(per_resource) != 1 or not isinstance(per_resource[0], dict) or per_resource[0].get("EvalResourceName") != request["ResourceArns"][0]:
                raise Stop("Simulation returned a different resource")
            if per_resource[0].get("EvalResourceDecision") != expected:
                raise Stop("Per-resource decision differs")
        if expected == "allowed" and (row.get("MissingContextValues") or any(r.get("MissingContextValues") for r in per_resource)):
            raise Stop("Allowed result has missing context")


def snapshot_iam(capture):
    observations = {}
    for user in USERS:
        response = capture.call(user, "iam", "get-user", "--user-name", user)
        if response["User"]["Arn"] != f"arn:aws:iam::{ACCOUNT}:user/{user}":
            raise Stop("Unexpected approved user ARN/path")
    managed = {}
    for name in ("FDS-IaC-Operator", "FDS-Network-Operator", "FDS-ReadOnly-Audit", "FDS-Relay-SSM"):
        response = capture.optional(name, "iam", "get-role", {"NoSuchEntity"}, "--role-name", name)
        if response.get("CaptureState") == "ABSENT":
            observations[name] = "ABSENT"
            continue
        role = response["Role"]
        if role["Arn"] != f"arn:aws:iam::{ACCOUNT}:role/{name}":
            raise Stop("Unexpected role ARN/path")
        observations[name] = "PRESENT_SNAPSHOT_ONLY"
        inline = capture.call(name + "-inline", "iam", "list-role-policies", "--role-name", name)
        for policy_name in inline["PolicyNames"]:
            # Label uses hash, so external policy names cannot create paths.
            label = digest(policy_name.encode())[:16]
            capture.call(name + "-" + label, "iam", "get-role-policy", "--role-name", name, "--policy-name", policy_name)
        attached = capture.call(name + "-attached", "iam", "list-attached-role-policies", "--role-name", name)
        arns = [p["PolicyArn"] for p in attached["AttachedPolicies"]]
        if "PermissionsBoundary" in role:
            arns.append(role["PermissionsBoundary"]["PermissionsBoundaryArn"])
        for policy_arn in arns:
            if policy_arn in managed:
                continue
            label = digest(policy_arn.encode())[:16]
            before = capture.call(label + "-metadata", "iam", "get-policy", "--policy-arn", policy_arn)
            version = before["Policy"]["DefaultVersionId"]
            data = capture.call(label + "-document", "iam", "get-policy-version", "--policy-arn", policy_arn, "--version-id", version)
            after = capture.call(label + "-metadata-after", "iam", "get-policy", "--policy-arn", policy_arn)
            if after["Policy"]["DefaultVersionId"] != version:
                raise Stop("Managed policy default changed during capture")
            managed[policy_arn] = {"Version": version, "CompactDocumentSHA256": digest(compact(data["PolicyVersion"]["Document"]).encode())}
    profile = capture.optional("relay-profile", "iam", "get-instance-profile", {"NoSuchEntity"}, "--instance-profile-name", "FDS-Relay-SSM")
    if profile.get("CaptureState") != "ABSENT" and profile["InstanceProfile"]["Arn"] != PROFILE:
        raise Stop("Unexpected instance profile ARN/path")
    return {"Roles": observations, "Profile": "ABSENT" if profile.get("CaptureState") == "ABSENT" else "PRESENT_SNAPSHOT_ONLY", "ManagedPolicies": managed}


def snapshot_bucket(capture, expected_policy):
    args = ("--bucket", BUCKET, "--expected-bucket-owner", ACCOUNT)
    location = capture.optional("bucket-location", "s3api", "get-bucket-location", {"NoSuchBucket"}, *args)
    if location.get("CaptureState") == "ABSENT":
        return {"State": "ABSENT_AT_CAPTURE", "Bootstrap": "NOT_RUN", "NameAvailability": "NOT_GUARANTEED"}
    if location.get("LocationConstraint") != REGION:
        raise Stop("Existing bucket region differs; do not overwrite")
    responses = {}
    for operation, absent_codes in [
        ("get-bucket-versioning", set()),
        ("get-bucket-encryption", {"ServerSideEncryptionConfigurationNotFoundError"}),
        ("get-public-access-block", {"NoSuchPublicAccessBlockConfiguration"}),
        ("get-bucket-ownership-controls", {"OwnershipControlsNotFoundError"}),
        ("get-bucket-policy", {"NoSuchBucketPolicy"}),
    ]:
        responses[operation] = capture.optional(operation, "s3api", operation, absent_codes, *args)
    encryption = responses["get-bucket-encryption"].get("ServerSideEncryptionConfiguration", {}).get("Rules", [])
    ownership = responses["get-bucket-ownership-controls"].get("OwnershipControls", {}).get("Rules", [])
    public = responses["get-public-access-block"].get("PublicAccessBlockConfiguration", {})
    raw_policy = responses["get-bucket-policy"].get("Policy")
    actual_policy = json.loads(raw_policy) if isinstance(raw_policy, str) else raw_policy
    checks = {
        "VersioningEnabled": responses["get-bucket-versioning"].get("Status") == "Enabled",
        "DefaultAES256": len(encryption) == 1 and encryption[0].get("ApplyServerSideEncryptionByDefault", {}) == {"SSEAlgorithm": "AES256"},
        "PublicAccessBlockAllFour": all(public.get(k) is True for k in ("BlockPublicAcls", "IgnorePublicAcls", "BlockPublicPolicy", "RestrictPublicBuckets")),
        "BucketOwnerEnforced": ownership == [{"ObjectOwnership": "BucketOwnerEnforced"}],
        "CandidatePolicyStructuralMatch": actual_policy == expected_policy,
    }
    # Array order is preserved: structural equality is NOT a general policy-equivalence engine.
    return {"State": "OWNED_IN_SEOUL_AT_CAPTURE", "OwnerGuard": "EXPECTED_BUCKET_OWNER_CHECK_SUCCEEDED",
            "Checks": checks, "Readback": "ALL_STRUCTURAL_CHECKS_MATCH" if all(checks.values()) else "DIFFERENCES_REQUIRE_REVIEW",
            "ActualPolicyCompactSortedSHA256": digest(json.dumps(actual_policy, sort_keys=True, separators=(",", ":")).encode()) if actual_policy else None,
            "RootRecoveryRuntime": "NOT_TESTED"}


def run_capture(capture, documents):
    identity = capture.call("identity", "sts", "get-caller-identity")
    if identity.get("Account") != ACCOUNT or identity.get("Arn") != ROOT:
        raise Stop("Requires exact account root; no further AWS calls made")
    id_doc = documents["candidates/iac-backend-passrole.candidate.json"]
    bucket_doc = documents["candidates/state-bucket-policy.candidate.json"]
    summary = {"UTC": dt.datetime.now(dt.timezone.utc).isoformat(), "Account": ACCOUNT, "Region": REGION,
               "ExecutionArn": ROOT, "RootOperationScope": "READONLY_CAPTURE_ONLY",
               "CandidateSourceMerge": SOURCE_MERGE, "CandidateRawSHA256": SOURCE_HASHES,
               "CollectorRawSHA256": digest(Path(__file__).read_bytes()),
               "Scope": "PR145_PARTIAL_INPUTS_ONLY", "AWS_MUTATION": "NOT_RUN", "ROLE_GRANT": "NOT_RUN",
               "USER_RUNTIME": "NOT_TESTED", "APPLY_READINESS": "NOT_ASSESSED",
               "ROLE_RESOURCE_POLICY_SIMULATION": "NOT_SUPPORTED_NOT_TESTED",
               "ROOT_RECOVERY_RUNTIME": "NOT_TESTED", "EFFECTIVE_PERMISSIONS": "NOT_TESTED"}
    summary["Runtime"] = {"Python": platform.python_version(), "Platform": platform.platform(),
                          "AWSCLI": capture.cli_version()}
    summary["IAMSnapshot"] = snapshot_iam(capture)
    summary["BucketSnapshot"] = snapshot_bucket(capture, bucket_doc)
    findings = {}
    for label, policy_type, doc in [("identity", "IDENTITY_POLICY", id_doc), ("bucket", "RESOURCE_POLICY", bucket_doc)]:
        path = capture.save(label + "-validation-input.json", doc)
        args = ["--policy-document", "file://" + str(path), "--policy-type", policy_type]
        if label == "bucket":
            args += ["--validate-policy-resource-type", "AWS::S3::Bucket"]
        response = capture.call(label + "-validate", "accessanalyzer", "validate-policy", *args)
        if not isinstance(response.get("findings"), list):
            raise Stop("Validation response lacks findings array")
        findings[label] = [{"Type": f.get("findingType"), "Code": f.get("issueCode")} for f in response["findings"]]
    summary["ValidatePolicy"] = {"Result": "NO_FINDINGS" if not any(findings.values()) else "FINDINGS_REQUIRE_REVIEW", "Findings": findings}
    cases = simulation_cases(id_doc, bucket_doc)
    results = []
    for i, case in enumerate(cases, 1):
        path = capture.save(f"case-{i:02d}-input.json", case["Request"])
        response = capture.call(f"case-{i:02d}", "iam", "simulate-custom-policy", "--cli-input-json", "file://" + str(path))
        check_simulation(case, response)
        results.append({"Case": i, "Label": case["Label"], "Scope": case["Scope"], "Expected": case["Expected"], "Result": "PASS"})
        capture.save("matrix-progress.json", results)
        print(f"CASE={i:02d} LABEL={case['Label']} SCOPE={case['Scope']} RESULT=PASS", flush=True)
    summary["CandidateDeltaMatrix"] = {"Result": "PASS", "Cases": len(results), "Scopes": "PARTIAL_IDENTITY_AND_IAM_USER_BUCKET_DENY_FIXTURES_ONLY"}
    summary["Collection"] = "COMPLETE"
    capture.save("summary.json", summary)
    return summary


def write_manifest(directory):
    files = sorted(p for p in directory.iterdir() if p.is_file() and p.name != "SHA256SUMS")
    (directory / "SHA256SUMS").write_text("".join(f"{digest(p.read_bytes())}  ./{p.name}\n" for p in files), encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parent.parent / "20261006-iac-fixed-inputs")
    parser.add_argument("--output-parent", type=Path, default=Path.home())
    args = parser.parse_args(argv)
    os.umask(0o077)
    directory = Path(tempfile.mkdtemp(prefix="fds-iac-delta-precheck-", dir=args.output_parent)).resolve()
    capture = Capture(directory)
    print("CAPTURE_DIR=" + str(directory), flush=True)
    rc = 1
    try:
        documents = load_source(args.source_dir.resolve())
        summary = run_capture(capture, documents)
        print(json.dumps(summary, ensure_ascii=True, indent=2))
        rc = 0 if summary["ValidatePolicy"]["Result"] == "NO_FINDINGS" else 2
    except (Stop, OSError, ValueError, KeyError, TypeError) as exc:
        capture.save("stop.json", {"Collection": "INCOMPLETE", "Error": str(exc), "AWS_MUTATION": "NOT_RUN", "ROLE_GRANT": "NOT_RUN", "APPLY_READINESS": "NOT_ASSESSED"})
        print("STOP: " + str(exc), file=sys.stderr)
    finally:
        write_manifest(directory)
        print("AWS_MUTATION=NOT_RUN\nROLE_GRANT=NOT_RUN\nPRESERVED_DIR=" + str(directory), flush=True)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
