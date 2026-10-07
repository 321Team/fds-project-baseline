#!/usr/bin/env python3
"""Create-only central bootstrap candidate. No human grants, compute, or object reads."""
import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import uuid

ACCOUNT = "774055931866"
REGION = "ap-northeast-2"
ROOT = f"arn:aws:iam::{ACCOUNT}:root"
BUCKET = "fds-tfstate-774055931866-ap-northeast-2"
ROLE = "FDS-Relay-SSM"
ROLE_ARN = f"arn:aws:iam::{ACCOUNT}:role/{ROLE}"
PROFILE_ARN = f"arn:aws:iam::{ACCOUNT}:instance-profile/{ROLE}"
STACK = "FDS-Central-Bootstrap-v1"
STACK_PREFIX = f"arn:aws:cloudformation:{REGION}:{ACCOUNT}:stack/{STACK}/"
AGENT_ARN = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
SOURCE_HASHES = {
    "bootstrap-stack.candidate.json": "80bc24b09e3c8c2f37aa0e7e9eacac1ef3120184b55bd8628a828e4c7c143064",
    "agent-policy.expected.json": "cdda7894744469d6226b958532014ac3cd3d0d995e56d748ab5b88a989dadbf6",
}
READS = {
    "sts": {"get-caller-identity"},
    "cloudformation": {"validate-template", "describe-stacks", "describe-stack-resources", "get-template"},
    "iam": {"get-role", "get-instance-profile", "list-role-policies", "list-attached-role-policies", "get-policy", "get-policy-version"},
    "s3api": {"get-bucket-location", "get-bucket-versioning", "get-bucket-encryption", "get-public-access-block", "get-bucket-ownership-controls", "get-bucket-policy"},
    "ec2": {"describe-regions"},
    "ssm": {"describe-parameters"},
}


class Stop(RuntimeError):
    pass


class AwsError(Stop):
    def __init__(self, operation, code, stderr=""):
        self.code, self.stderr = code, stderr
        super().__init__(f"{operation}: {code}; private response preserved")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def compact(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":"))


def policy_form(value, key=""):
    """IAM unordered sets and scalar/list forms; not a generic CFN normalizer."""
    if key in {"Statement", "Action", "NotAction", "Resource", "NotResource", "AWS", "Service", "Federated"} and not isinstance(value, list):
        value = [value]
    if isinstance(value, dict):
        return {k: policy_form(v, k) for k, v in value.items()}
    if isinstance(value, list):
        return sorted((policy_form(v) for v in value), key=compact)
    return value


def policy_hash(value):
    return digest(compact(policy_form(value)).encode())


def load_source(directory):
    docs = {}
    for name, expected in SOURCE_HASHES.items():
        data = (Path(directory) / name).read_bytes()
        if digest(data) != expected:
            raise Stop("Pinned source bytes differ: " + name)
        docs[name] = json.loads(data)
    return docs


def check_stack_id(value):
    if not isinstance(value, str) or not value.startswith(STACK_PREFIX) or not re.fullmatch(r"[0-9a-fA-F-]{36}", value[len(STACK_PREFIX):]):
        raise Stop("Unexpected stack ARN/account/region/name")
    return value


class Capture:
    def __init__(self, directory, runner=subprocess.run, mode="prepare"):
        self.directory, self.runner, self.mode = Path(directory), runner, mode
        self.number, self.mutation_attempted = 0, False

    def save(self, name, data):
        path = self.directory / name
        path.write_text(json.dumps(data, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
        path.chmod(0o600)
        return path

    def call(self, label, service, operation, request=None, region=REGION, mutation=False):
        if mutation:
            if self.mode != "create" or (service, operation) != ("cloudformation", "create-stack") or self.mutation_attempted:
                raise Stop("Mutation outside one create-stack request")
            keys = {"StackName", "TemplateBody", "Capabilities", "OnFailure", "EnableTerminationProtection", "ClientRequestToken"}
            if not isinstance(request, dict) or set(request) != keys or request["StackName"] != STACK or request["Capabilities"] != ["CAPABILITY_NAMED_IAM"] or request["OnFailure"] != "DO_NOTHING" or request["EnableTerminationProtection"] is not True:
                raise Stop("Unexpected create-stack arguments")
            if not re.fullmatch(r"fds-bootstrap-[0-9a-f]{32}", request["ClientRequestToken"]) or json.loads(request["TemplateBody"]) != load_source(Path(__file__).resolve().parent)["bootstrap-stack.candidate.json"]:
                raise Stop("Unpinned create-stack source/token")
        elif operation not in READS.get(service, set()):
            raise Stop("Operation outside metadata read allowlist")
        if not re.fullmatch(r"[a-z0-9-]+", label) or not re.fullmatch(r"[a-z]{2}(?:-[a-z]+)+-[0-9]+", region):
            raise Stop("Invalid internal label/region")
        self.number += 1
        name = f"{self.number:03d}-{label}"
        command = ["aws", service, operation]
        if request is not None:
            path = self.save(name + "-input.json", request)
            command += ["--cli-input-json", "file://" + str(path)]
        command += ["--region", region, "--output", "json", "--no-cli-pager", "--cli-connect-timeout", "5", "--cli-read-timeout", "25"]
        env = os.environ.copy()
        env.update(AWS_MAX_ATTEMPTS="1", AWS_PAGER="", AWS_CLI_AUTO_PROMPT="off")
        if mutation:
            self.mutation_attempted = True
            self.save("create-attempt.json", {"ClientRequestToken": request["ClientRequestToken"], "Mutation": "CREATE_STACK_ATTEMPTED_OUTCOME_PENDING", "AutomaticRetry": False})
        try:
            result = self.runner(command, capture_output=True, text=True, timeout=40, check=False, env=env)
        except subprocess.TimeoutExpired as exc:
            for suffix, raw in (("stdout", exc.stdout), ("stderr", exc.stderr)):
                if raw is not None:
                    path = self.directory / (name + "." + suffix)
                    path.write_bytes(raw if isinstance(raw, bytes) else raw.encode())
                    path.chmod(0o600)
            self.save(name + "-error.json", {"Operation": operation, "Code": "TIMEOUT", "MutationAttempted": self.mutation_attempted})
            raise AwsError(operation, "TIMEOUT") from exc
        except OSError as exc:
            raise AwsError(operation, "CLI_UNAVAILABLE") from exc
        for suffix, data in (("stdout", result.stdout), ("stderr", result.stderr)):
            path = self.directory / (name + "." + suffix)
            path.write_text(data, encoding="utf-8")
            path.chmod(0o600)
        if result.returncode:
            match = re.search(r"\(([A-Za-z0-9]+)\) when calling", result.stderr)
            raise AwsError(operation, match.group(1) if match else "UNCLASSIFIED", result.stderr)
        try:
            data = json.loads(result.stdout)
        except ValueError as exc:
            raise AwsError(operation, "INVALID_JSON") from exc
        if not isinstance(data, dict) or any(data.get(k) for k in ("NextToken", "Marker", "IsTruncated", "NextMarker")):
            raise AwsError(operation, "INVALID_OR_INCOMPLETE_RESPONSE")
        return data


def identity(capture):
    value = capture.call("identity", "sts", "get-caller-identity")
    if value.get("Arn") != ROOT or value.get("Account") != ACCOUNT:
        raise Stop("Exact root/account is required")
    return value


def require_absent(capture):
    checks = [
        ("bucket-before", "s3api", "get-bucket-location", {"Bucket": BUCKET, "ExpectedBucketOwner": ACCOUNT}, "NoSuchBucket"),
        ("role-before", "iam", "get-role", {"RoleName": ROLE}, "NoSuchEntity"),
        ("profile-before", "iam", "get-instance-profile", {"InstanceProfileName": ROLE}, "NoSuchEntity"),
    ]
    for label, service, operation, request, absent in checks:
        try:
            capture.call(label, service, operation, request)
        except AwsError as exc:
            if exc.code != absent:
                raise
        else:
            raise Stop("Existing resource; no adoption/overwrite: " + label)
    try:
        capture.call("stack-before", "cloudformation", "describe-stacks", {"StackName": STACK})
    except AwsError as exc:
        if exc.code != "ValidationError" or not re.search(r"Stack with id " + re.escape(STACK) + r" does not exist(?:\s|$)", exc.stderr):
            raise
    else:
        raise Stop("Existing bootstrap stack; no update/recreate")
    return {"Bucket": "ABSENT", "Role": "ABSENT", "Profile": "ABSENT", "Stack": "ABSENT", "BucketNameAvailability": "NOT_GUARANTEED"}


def agent_snapshot(capture, expected):
    request = {"PolicyArn": AGENT_ARN}
    first = capture.call("agent-metadata-before", "iam", "get-policy", request)["Policy"]
    if first.get("Arn") != AGENT_ARN or first.get("DefaultVersionId") != "v2":
        raise Stop("Agent managed policy ARN/default version drift")
    version = capture.call("agent-version", "iam", "get-policy-version", {**request, "VersionId": "v2"})["PolicyVersion"]
    if version.get("VersionId") != "v2" or version.get("IsDefaultVersion") is not True or policy_form(version["Document"]) != policy_form(expected):
        raise Stop("Agent managed policy document drift")
    last = capture.call("agent-metadata-after", "iam", "get-policy", request)["Policy"]
    if last.get("Arn") != AGENT_ARN or last.get("DefaultVersionId") != "v2":
        raise Stop("Agent managed policy changed during capture")
    return {"Arn": AGENT_ARN, "Version": "v2", "SemanticSHA256": policy_hash(version["Document"]), "ParameterReads": "GetParameter/GetParameters Resource *; no region condition"}


def parameter_metadata(capture):
    response = capture.call("enabled-regions", "ec2", "describe-regions", {"AllRegions": True})
    records = response["Regions"]
    if not isinstance(records, list) or not records:
        raise Stop("Enabled region inventory missing")
    regions = []
    for row in records:
        status = row["OptInStatus"]
        if status not in {"opt-in-not-required", "opted-in", "not-opted-in"}:
            raise Stop("Unexpected region opt-in state")
        if status != "not-opted-in":
            regions.append(row["RegionName"])
    if REGION not in regions or len(regions) != len(set(regions)) or len(regions) > 50:
        raise Stop("Invalid enabled region set")
    results = []
    for region in sorted(regions):
        counts = {}
        for shared in (False, True):
            value = capture.call("parameters-" + region + ("-shared" if shared else "-owned"), "ssm", "describe-parameters", {"Shared": shared}, region)
            parameters = value.get("Parameters")
            if not isinstance(parameters, list) or not all(isinstance(p, dict) for p in parameters):
                raise Stop("Parameter metadata response missing array")
            counts["PromotedShared" if shared else "Owned"] = len(parameters)
        results.append({"Region": region, **counts})
        capture.save("parameter-progress.json", results)
        print(f"PARAMETER_REGION={region} OWNED={counts['Owned']} PROMOTED_SHARED={counts['PromotedShared']}", flush=True)
        if counts["Owned"] or counts["PromotedShared"]:
            raise Stop("Parameter metadata present; review access scope before Agent attachment")
    return {"Regions": results, "ValuesRead": False, "Scope": "OWNED_AND_RAM_PROMOTED_SHARED_METADATA_ONLY_NOT_COMPLETE_EFFECTIVE_ACCESS_PROOF", "FutureRegionOrParameterChanges": "REASSESS_BEFORE_RELAY_USE"}


def preflight(capture, docs):
    before = require_absent(capture)
    template = docs["bootstrap-stack.candidate.json"]
    validation = capture.call("validate-template", "cloudformation", "validate-template", {"TemplateBody": compact(template)})
    if "CAPABILITY_NAMED_IAM" not in validation.get("Capabilities", []) or validation.get("Parameters"):
        raise Stop("Unexpected template capabilities/parameters")
    agent = agent_snapshot(capture, docs["agent-policy.expected.json"])
    parameters = parameter_metadata(capture)
    return {"Before": before, "AgentPolicy": agent, "ParameterMetadata": parameters, "TemplateValidation": "PASS", "CreateScope": "4_BOOTSTRAP_RESOURCES_ONLY", "UserRuntime": "NOT_TESTED"}


def submit(capture, docs):
    template = docs["bootstrap-stack.candidate.json"]
    request = {"StackName": STACK, "TemplateBody": compact(template), "Capabilities": ["CAPABILITY_NAMED_IAM"], "OnFailure": "DO_NOTHING", "EnableTerminationProtection": True, "ClientRequestToken": "fds-bootstrap-" + uuid.uuid4().hex}
    result = capture.call("create-stack", "cloudformation", "create-stack", request, mutation=True)
    stack_id = check_stack_id(result.get("StackId"))
    return {"StackId": stack_id, "ClientRequestToken": request["ClientRequestToken"], "Status": "SUBMITTED_NOT_READBACK", "AWS_MUTATION": "CREATE_BOOTSTRAP_STACK_REQUEST_SUBMITTED", "HUMAN_ROLE_GRANT": "NOT_RUN"}


def readback(capture, docs, stack_id):
    stack_id = check_stack_id(stack_id)
    response = capture.call("stack", "cloudformation", "describe-stacks", {"StackName": stack_id})
    stacks = response["Stacks"]
    if not isinstance(stacks, list) or len(stacks) != 1 or stacks[0].get("StackId") != stack_id or stacks[0].get("StackName") != STACK:
        raise Stop("Stack identity mismatch")
    stack = stacks[0]
    if stack.get("StackStatus") != "CREATE_COMPLETE":
        raise Stop("Stack not CREATE_COMPLETE; no repair or resubmit")
    if stack.get("EnableTerminationProtection") is not True or stack.get("RoleARN"):
        raise Stop("Unexpected stack protection/service role")
    actual = capture.call("stack-template", "cloudformation", "get-template", {"StackName": stack_id, "TemplateStage": "Original"})["TemplateBody"]
    if isinstance(actual, str):
        actual = json.loads(actual)
    if actual != docs["bootstrap-stack.candidate.json"]:
        raise Stop("Stack template differs from pinned source")
    resources = capture.call("stack-resources", "cloudformation", "describe-stack-resources", {"StackName": stack_id})["StackResources"]
    expected = {"StateBucket": ("AWS::S3::Bucket", BUCKET), "StateBucketPolicy": ("AWS::S3::BucketPolicy", BUCKET), "RelayRole": ("AWS::IAM::Role", ROLE), "RelayProfile": ("AWS::IAM::InstanceProfile", ROLE)}
    if not isinstance(resources, list) or len(resources) != 4 or {r["LogicalResourceId"] for r in resources} != set(expected):
        raise Stop("Unexpected stack resource set")
    for row in resources:
        if (row["ResourceType"], row["PhysicalResourceId"]) != expected[row["LogicalResourceId"]] or row.get("ResourceStatus") != "CREATE_COMPLETE":
            raise Stop("Stack resource/readiness mismatch")
    request = {"Bucket": BUCKET, "ExpectedBucketOwner": ACCOUNT}
    location = capture.call("bucket-region", "s3api", "get-bucket-location", request)
    versioning = capture.call("bucket-versioning", "s3api", "get-bucket-versioning", request)
    encryption = capture.call("bucket-encryption", "s3api", "get-bucket-encryption", request)
    public = capture.call("bucket-public", "s3api", "get-public-access-block", request)
    ownership = capture.call("bucket-ownership", "s3api", "get-bucket-ownership-controls", request)
    policy = json.loads(capture.call("bucket-policy", "s3api", "get-bucket-policy", request)["Policy"])
    if location.get("LocationConstraint") != REGION or versioning.get("Status") != "Enabled":
        raise Stop("Bucket location/versioning mismatch")
    rules = encryption["ServerSideEncryptionConfiguration"]["Rules"]
    if len(rules) != 1 or rules[0].get("ApplyServerSideEncryptionByDefault") != {"SSEAlgorithm": "AES256"}:
        raise Stop("Bucket AES256 encryption mismatch")
    expected_public = docs["bootstrap-stack.candidate.json"]["Resources"]["StateBucket"]["Properties"]["PublicAccessBlockConfiguration"]
    if public.get("PublicAccessBlockConfiguration") != expected_public or ownership["OwnershipControls"]["Rules"] != [{"ObjectOwnership": "BucketOwnerEnforced"}]:
        raise Stop("Bucket public access/ownership mismatch")
    expected_policy = docs["bootstrap-stack.candidate.json"]["Resources"]["StateBucketPolicy"]["Properties"]["PolicyDocument"]
    if policy_form(policy) != policy_form(expected_policy):
        raise Stop("Bucket policy mismatch; never overwrite to pass")
    role = capture.call("role", "iam", "get-role", {"RoleName": ROLE})["Role"]
    role_source = docs["bootstrap-stack.candidate.json"]["Resources"]["RelayRole"]["Properties"]
    if role.get("Arn") != ROLE_ARN or role.get("Path") != "/" or role.get("RoleName") != ROLE or role.get("PermissionsBoundary") or role.get("MaxSessionDuration") != 3600:
        raise Stop("Role identity/boundary/duration mismatch")
    if policy_form(role["AssumeRolePolicyDocument"]) != policy_form(role_source["AssumeRolePolicyDocument"]):
        raise Stop("EC2 trust mismatch")
    inline = capture.call("role-inline", "iam", "list-role-policies", {"RoleName": ROLE})["PolicyNames"]
    attached = capture.call("role-attached", "iam", "list-attached-role-policies", {"RoleName": ROLE})["AttachedPolicies"]
    if inline != [] or len(attached) != 1 or attached[0]["PolicyArn"] != AGENT_ARN:
        raise Stop("Unexpected Relay permissions")
    profile = capture.call("profile", "iam", "get-instance-profile", {"InstanceProfileName": ROLE})["InstanceProfile"]
    if profile.get("Arn") != PROFILE_ARN or profile.get("Path") != "/" or profile.get("InstanceProfileName") != ROLE or len(profile["Roles"]) != 1 or profile["Roles"][0].get("Arn") != ROLE_ARN:
        raise Stop("Profile identity/role binding mismatch")
    agent = agent_snapshot(capture, docs["agent-policy.expected.json"])
    return {"StackId": stack_id, "Readback": "BOOTSTRAP_SETTINGS_PASS", "StateBucket": BUCKET, "RelayRoleArn": ROLE_ARN, "RelayProfileArn": PROFILE_ARN, "BucketPolicySemanticSHA256": policy_hash(policy), "AgentPolicy": agent, "Runtime": "NOT_TESTED", "ApplyReadinessForStageA": "NOT_ASSESSED", "HumanRoleGrant": "NOT_RUN", "RootRecoveryRuntime": "NOT_TESTED"}


def write_manifest(directory):
    directory = Path(directory)
    rows = [p for p in sorted(directory.iterdir()) if p.is_file() and p.name != "SHA256SUMS"]
    (directory / "SHA256SUMS").write_text("".join(f"{digest(p.read_bytes())}  ./{p.name}\n" for p in rows), encoding="utf-8")
    (directory / "SHA256SUMS").chmod(0o600)


def main(argv=None, runner=subprocess.run):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("prepare", "create", "verify"), default="prepare")
    parser.add_argument("--stack-id")
    parser.add_argument("--output-parent", type=Path, default=Path.home())
    args = parser.parse_args(argv)
    os.umask(0o077)
    directory = Path(tempfile.mkdtemp(prefix="fds-central-bootstrap-" + args.mode + "-", dir=args.output_parent))
    capture = Capture(directory, runner, args.mode)
    print("CAPTURE_DIR=" + str(directory), flush=True)
    rc = 1
    try:
        docs = load_source(Path(__file__).resolve().parent)
        if args.mode == "verify":
            check_stack_id(args.stack_id)
        elif args.stack_id:
            raise Stop("Stack ARN is only accepted for read-only verify")
        actor = identity(capture)
        capture.save("source.json", {"UTC": dt.datetime.now(dt.timezone.utc).isoformat(), "ExecutionArn": actor["Arn"], "HelperRawSHA256": digest(Path(__file__).read_bytes()), "SourceRawSHA256": SOURCE_HASHES, "Mode": args.mode})
        if args.mode == "verify":
            summary = readback(capture, docs, args.stack_id)
        else:
            summary = preflight(capture, docs)
            capture.save("preflight.json", summary)
            if args.mode == "create":
                summary = {**summary, **submit(capture, docs)}
            else:
                summary.update(Status="PREPARED_NO_MUTATION", AWS_MUTATION="NOT_RUN", SourceReviewAndExecutionDecision="REQUIRED_FOR_CREATE")
        capture.save("summary.json", summary)
        print(json.dumps(summary, ensure_ascii=True), flush=True)
        rc = 0
    except Exception as exc:
        mutation = "CREATE_ATTEMPT_OUTCOME_REQUIRES_INSPECTION" if capture.mutation_attempted else "NOT_RUN"
        capture.save("stop.json", {"Collection": "INCOMPLETE", "ErrorType": type(exc).__name__, "Error": str(exc), "AWS_MUTATION": mutation, "AutomaticRetryOrRollback": False})
        print("STOP: " + (str(exc) if isinstance(exc, Stop) else type(exc).__name__), flush=True)
    finally:
        write_manifest(directory)
        print("AWS_MUTATION=" + ("CREATE_STACK_ATTEMPTED_CHECK_SUMMARY" if capture.mutation_attempted else "NOT_RUN"), flush=True)
        print("HUMAN_ROLE_GRANT=NOT_RUN\nPRESERVED_DIR=" + str(directory), flush=True)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
