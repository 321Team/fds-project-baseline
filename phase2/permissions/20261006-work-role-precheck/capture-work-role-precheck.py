#!/usr/bin/env python3
"""Capture IAM inputs and optionally test proposed AssumeRole policies. No AWS writes."""
import argparse
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
ROOT = f"arn:aws:iam::{ACCOUNT}:root"
REGION = "ap-northeast-2"
GROUP = "FDS-Human-Bootstrap"
USERS = ("321team-gwonuk", "321team-hayeoung", "321team-jaehwan")
ASSIGNMENTS = {
    "FDS-IaC-Operator": ("321team-gwonuk", "321team-hayeoung"),
    "FDS-Network-Operator": ("321team-gwonuk", "321team-jaehwan"),
}
OBSERVED_ROLES = ("FDS-ReadOnly-Audit", *ASSIGNMENTS)
READ_OPERATIONS = {
    "sts": {"get-caller-identity"},
    "iam": {
        "get-group", "get-user", "get-role", "get-policy", "get-policy-version",
        "list-groups-for-user", "list-mfa-devices", "list-access-keys",
        "list-group-policies", "get-group-policy", "list-attached-group-policies",
        "list-user-policies", "get-user-policy", "list-attached-user-policies",
        "list-role-policies", "get-role-policy", "list-attached-role-policies",
        "get-context-keys-for-principal-policy", "simulate-principal-policy",
    },
    "ec2": {"describe-availability-zones", "describe-images", "describe-vpcs",
            "describe-instances"},
    "s3api": {"list-buckets"},
    "accessanalyzer": {"validate-policy"},
}


class Stop(RuntimeError):
    pass


class AwsError(Stop):
    def __init__(self, operation, code, detail):
        self.operation, self.code = operation, code
        super().__init__(f"{operation}: {code}: {detail}")


def arn(kind, name):
    return f"arn:aws:iam::{ACCOUNT}:{kind}/{name}"


def condition(user):
    return {"Bool": {"aws:MultiFactorAuthPresent": "true"},
            "StringEquals": {"sts:RoleSessionName": user}}


def candidate_documents():
    docs = {}
    for role, users in ASSIGNMENTS.items():
        docs[f"trust-{role}.candidate.json"] = {
            "Version": "2012-10-17",
            "Statement": [{"Sid": "Allow" + user.removeprefix("321team-").title(),
                           "Effect": "Allow", "Principal": {"AWS": arn("user", user)},
                           "Action": "sts:AssumeRole", "Condition": condition(user)}
                          for user in users],
        }
    for user in USERS:
        docs[f"assume-{user}.candidate.json"] = {
            "Version": "2012-10-17",
            "Statement": [{"Sid": "AssumeAssignedWorkRoles", "Effect": "Allow",
                           "Action": "sts:AssumeRole",
                           "Resource": [arn("role", role) for role, users in ASSIGNMENTS.items()
                                        if user in users],
                           "Condition": condition(user)}],
        }
    return docs


def compact(doc):
    return json.dumps(doc, ensure_ascii=True, separators=(",", ":"))


class Capture:
    def __init__(self, directory, runner=subprocess.run):
        self.directory, self.runner = Path(directory), runner
        self.number, self.files = 0, []
        self.managed, self.groups, self.roles = {}, set(), {}

    def save(self, name, data):
        path = self.directory / name
        path.write_text(json.dumps(data, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")
        self.files.append(path)
        return path

    def call(self, label, service, operation, *args):
        if operation not in READ_OPERATIONS.get(service, set()):
            raise Stop(f"AWS operation outside capture allowlist: {service} {operation}")
        self.number += 1
        name = f"{self.number:03d}-{re.sub(r'[^A-Za-z0-9_.-]', '-', label)}.json"
        command = ["aws", service, operation, *args, "--output", "json", "--no-cli-pager"]
        try:
            result = self.runner(command, capture_output=True, text=True,
                                 timeout=60, check=False)
        except (subprocess.TimeoutExpired, OSError) as exc:
            self.save(name, {"Operation": operation, "Error": type(exc).__name__})
            raise AwsError(operation, "UNAVAILABLE", type(exc).__name__) from exc
        if result.returncode:
            match = re.search(r"\(([A-Za-z0-9]+)\) when calling the [A-Za-z0-9]+ operation", result.stderr)
            code = match.group(1) if match else "UNCLASSIFIED"
            self.save(name, {"Operation": operation, "Code": code,
                             "RC": result.returncode, "Stderr": result.stderr})
            raise AwsError(operation, code, f"RC={result.returncode}; preserved {name}")
        try:
            data = json.loads(result.stdout)
        except ValueError as exc:
            self.save(name, {"Operation": operation, "Error": "INVALID_JSON"})
            raise AwsError(operation, "INVALID_JSON", name) from exc
        if not isinstance(data, dict):
            raise Stop(f"Unexpected response object: {operation}")
        self.save(name, data)
        return data

    def managed_policy(self, policy_arn):
        if policy_arn in self.managed:
            return
        label = hashlib.sha256(policy_arn.encode()).hexdigest()[:16]
        metadata = self.call(label + "-metadata", "iam", "get-policy", "--policy-arn", policy_arn)
        version = metadata["Policy"]["DefaultVersionId"]
        document = self.call(label + "-version", "iam", "get-policy-version",
                             "--policy-arn", policy_arn, "--version-id", version)
        after = self.call(label + "-metadata-after", "iam", "get-policy", "--policy-arn", policy_arn)
        if after["Policy"]["DefaultVersionId"] != version:
            raise Stop(f"Managed default version changed during capture: {policy_arn}")
        self.managed[policy_arn] = {
            "Version": version,
            "DocumentSHA256": hashlib.sha256(compact(document["PolicyVersion"]["Document"]).encode()).hexdigest(),
        }

    def policies(self, kind, name):
        option = "--" + kind + "-name"
        names = self.call(name + "-inline", "iam", f"list-{kind}-policies", option, name)
        for policy in names["PolicyNames"]:
            self.call(name + "-" + policy, "iam", f"get-{kind}-policy",
                      option, name, "--policy-name", policy)
        attached = self.call(name + "-attached", "iam", f"list-attached-{kind}-policies", option, name)
        for policy in attached["AttachedPolicies"]:
            self.managed_policy(policy["PolicyArn"])

    def group_policies(self, name):
        if name not in self.groups:
            self.groups.add(name)
            self.policies("group", name)

    def capture_iam(self):
        identity = self.call("identity", "sts", "get-caller-identity")
        if identity.get("Account") != ACCOUNT or identity.get("Arn") != ROOT:
            raise Stop("Requires the exact education account root for central capture")
        group = self.call("bootstrap-group", "iam", "get-group", "--group-name", GROUP)
        if sorted(u["Arn"] for u in group["Users"]) != sorted(arn("user", u) for u in USERS):
            raise Stop("Bootstrap membership differs from the approved three exact users")
        self.group_policies(GROUP)
        for user in USERS:
            doc = self.call(user, "iam", "get-user", "--user-name", user)["User"]
            if doc["Arn"] != arn("user", user):
                raise Stop("Unexpected user ARN/path")
            if "PermissionsBoundary" in doc:
                self.managed_policy(doc["PermissionsBoundary"]["PermissionsBoundaryArn"])
            self.call(user + "-mfa", "iam", "list-mfa-devices", "--user-name", user)
            self.call(user + "-access-keys", "iam", "list-access-keys", "--user-name", user)
            self.policies("user", user)
            groups = self.call(user + "-groups", "iam", "list-groups-for-user", "--user-name", user)
            for entry in groups["Groups"]:
                self.group_policies(entry["GroupName"])
        for role in OBSERVED_ROLES:
            try:
                doc = self.call(role, "iam", "get-role", "--role-name", role)["Role"]
            except AwsError as exc:
                if exc.operation != "get-role" or exc.code != "NoSuchEntity":
                    raise
                self.roles[role] = "ABSENT"
                continue
            self.roles[role] = "PRESENT_REVIEW_REQUIRED"
            if "PermissionsBoundary" in doc:
                self.managed_policy(doc["PermissionsBoundary"]["PermissionsBoundaryArn"])
            self.policies("role", role)

    def inventory(self):
        self.call("availability-zones", "ec2", "describe-availability-zones", "--region", REGION,
                  "--query", "{Zones:AvailabilityZones[].{Name:ZoneName,Id:ZoneId,State:State}}")
        self.call("relay-ami", "ec2", "describe-images", "--region", REGION,
                  "--image-ids", "ami-079a2667364cee804", "--owners", "125523088429",
                  "--query", "{Images:Images[].{Id:ImageId,Owner:OwnerId,State:State,Architecture:Architecture}}")
        self.call("project-vpcs", "ec2", "describe-vpcs", "--region", REGION,
                  "--filters", "Name=cidr-block,Values=10.20.0.0/16",
                  "--query", "{Vpcs:Vpcs[].{Id:VpcId,Cidr:CidrBlock,Tags:Tags}}")
        self.call("project-instances", "ec2", "describe-instances", "--region", REGION,
                  "--filters", "Name=tag:Project,Values=fds-hybrid",
                  "Name=tag:ManagedBy,Values=terraform", "Name=tag:Phase,Values=phase2",
                  "--query", "{Instances:Reservations[].Instances[].{Id:InstanceId,Vpc:VpcId,Subnet:SubnetId,State:State.Name,PrivateIP:PrivateIpAddress,Image:ImageId,Type:InstanceType,SourceDestCheck:SourceDestCheck,Profile:IamInstanceProfile.Arn}}")
        self.call("bucket-metadata", "s3api", "list-buckets",
                  "--query", "{Buckets:Buckets[].{Name:Name,Created:CreationDate}}")

    def validate_candidates(self, docs):
        findings = {}
        for name, doc in docs.items():
            args = ["--region", REGION, "--policy-document", "file://" + str(self.directory / name)]
            if name.startswith("trust-"):
                args += ["--policy-type", "RESOURCE_POLICY", "--validate-policy-resource-type",
                         "AWS::IAM::AssumeRolePolicyDocument"]
            else:
                args += ["--policy-type", "IDENTITY_POLICY"]
            response = self.call("validate-" + name, "accessanalyzer", "validate-policy", *args)
            findings[name] = response["findings"]
        self.save("candidate-findings.json", findings)
        # Warnings also require review; a successful API response is not approval.
        if any(findings.values()):
            raise Stop("Candidate findings require review; see candidate-findings.json")

    def simulate_assume(self, docs):
        cases = []
        for user in USERS:
            policy = compact(docs[f"assume-{user}.candidate.json"])
            self.call(user + "-context-keys", "iam", "get-context-keys-for-principal-policy",
                      "--policy-source-arn", arn("user", user), "--policy-input-list", policy)
            for role, assigned in ASSIGNMENTS.items():
                cases.extend((user, role, mfa, user, mfa is True and user in assigned)
                             for mfa in (True, False, None))
                if user in assigned:
                    cases.append((user, role, True, "wrong-session-name", False))
        for index, (user, role, mfa, session, expected_allow) in enumerate(cases, 1):
            context = [{"ContextKeyName": key, "ContextKeyValues": [value], "ContextKeyType": "string"}
                       for key, value in (("aws:PrincipalArn", arn("user", user)),
                                          ("aws:username", user), ("aws:RequestedRegion", REGION),
                                          ("sts:RoleSessionName", session))]
            if mfa is not None:
                context.append({"ContextKeyName": "aws:MultiFactorAuthPresent",
                                "ContextKeyValues": [str(mfa).lower()], "ContextKeyType": "boolean"})
            request = {"PolicySourceArn": arn("user", user),
                       "PolicyInputList": [compact(docs[f"assume-{user}.candidate.json"])],
                       "ActionNames": ["sts:AssumeRole"], "ResourceArns": [arn("role", role)],
                       "ContextEntries": context}
            source = self.save(f"simulation-{index:02d}-input.json", request)
            response = self.call(f"simulation-{index:02d}-result", "iam", "simulate-principal-policy",
                                 "--cli-input-json", "file://" + str(source))
            rows = response.get("EvaluationResults", [])
            acceptable = {"allowed"} if expected_allow else {"implicitDeny", "explicitDeny"}
            ok = (len(rows) == 1 and rows[0].get("EvalActionName", "").lower() == "sts:assumerole"
                  and rows[0].get("EvalResourceName") == arn("role", role)
                  and rows[0].get("EvalDecision") in acceptable
                  and (not expected_allow or not rows[0].get("MissingContextValues")))
            print(f"ASSUME_CASE={index:02d} USER={user} ROLE={role} MFA={mfa} RESULT={'PASS' if ok else 'FAIL'}")
            if not ok:
                raise Stop(f"Identity-side candidate simulation mismatch: case{index:02d}")
        return len(cases)

    def manifest(self):
        lines = [hashlib.sha256(path.read_bytes()).hexdigest() + "  ./" + path.name
                 for path in sorted(set(self.files))]
        (self.directory / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="ascii")


def run(capture, simulate=False):
    print("UTC=" + dt.datetime.now(dt.timezone.utc).isoformat())
    print("CAPTURE_DIR=" + str(capture.directory))
    try:
        capture.capture_iam()
        capture.inventory()
        docs = candidate_documents()
        for name, doc in docs.items():
            capture.save(name, doc)
        cases = 0
        if simulate:
            capture.validate_candidates(docs)
            cases = capture.simulate_assume(docs)
        summary = {"Account": ACCOUNT, "Region": REGION, "Roles": capture.roles,
                   "ManagedPolicies": capture.managed, "CandidateCount": len(docs),
                   "CANDIDATE_VALIDATION": "NO_FINDINGS" if simulate else "NOT_RUN",
                   "IDENTITY_SIDE_CANDIDATE_SIMULATION": "PASS" if simulate else "NOT_RUN",
                   "SIMULATION_CASES": cases, "TRUST_RUNTIME": "NOT_TESTED",
                   "WORK_ROLE_PERMISSION_SIMULATION": "NOT_RUN", "ROLE_GRANT": "NOT_RUN",
                   "AWS_MUTATION": "NOT_RUN", "APPLY_READINESS": "NOT_ASSESSED"}
        capture.save("summary.json", summary)
        print(json.dumps(summary, ensure_ascii=True))
        print("CENTRAL_PRECHECK_CAPTURE=COMPLETE")
    finally:
        capture.manifest()
        print("PRESERVED_DIR=" + str(capture.directory))
        print("AWS_MUTATION=NOT_RUN")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--simulate-assume", action="store_true",
                        help="Validate five candidate documents and simulate identity-side AssumeRole only")
    args = parser.parse_args()
    os.umask(0o077)
    directory = tempfile.mkdtemp(prefix="fds-work-role-precheck-", dir=Path.home())
    try:
        run(Capture(directory), simulate=args.simulate_assume)
    except (Stop, KeyError, TypeError, ValueError) as exc:
        print("STOP: " + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
