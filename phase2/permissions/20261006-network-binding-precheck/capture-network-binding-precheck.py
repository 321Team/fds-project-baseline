#!/usr/bin/env python3
"""Collect current binding dependencies; never bind, grant or start a session."""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys
import tempfile

ACCOUNT = "774055931866"
REGION = "ap-northeast-2"
ROOT = f"arn:aws:iam::{ACCOUNT}:root"
SOURCE_MERGE = "1059713f1a56a1a9d0d88aa37470c5e582e1d580"
HELPER_HASH = "f955a5c56c42183b93953282bb48851347ca53c0d0ba251849fe339db80d4d42"
POLICY_HASH = "d4c94fc90e3a7ffd46964883f69743befdd0241d2a58068d62ba45bd6ebba2f6"
TAGS = {"Project": "fds-hybrid", "ManagedBy": "terraform", "Phase": "phase2"}
READ_OPERATIONS = {
    "sts": {"get-caller-identity"},
    "ssm": {"describe-document", "get-document", "list-documents", "describe-instance-information"},
    "ec2": {"describe-instances", "describe-volumes"},
    "iam": {"get-role", "list-role-policies", "get-role-policy",
            "list-attached-role-policies", "get-instance-profile"},
    "kms": {"describe-key", "get-key-policy"},
}


class Stop(RuntimeError):
    pass


def dependencies():
    parent = Path(__file__).resolve().parent.parent
    paths = {
        "helper": parent / "20261006-network-permission-precheck/capture-network-permission-precheck.py",
        "policy": parent / "20261006-network-final-candidate/network-permissions.proposed.template.json",
    }
    for key, digest in (("helper", HELPER_HASH), ("policy", POLICY_HASH)):
        if paths[key].is_symlink() or hashlib.sha256(paths[key].read_bytes()).hexdigest() != digest:
            raise Stop(f"Pinned dependency changed: {key}")
    spec = importlib.util.spec_from_file_location("binding_capture_helper", paths["helper"])
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    # Replace, rather than extend, the original simulator's operation allowlist.
    helper.READ_OPERATIONS = {service: set(ops) for service, ops in READ_OPERATIONS.items()}
    return helper, paths


def complete(data):
    if data.get("NextToken") or data.get("Marker") or data.get("IsTruncated"):
        raise Stop("Incomplete response; truncated evidence cannot establish absence")
    return data


def pages(cap, label, service, operation, field, *args):
    result, token, seen = [], None, set()
    for page in range(1, 6):
        extra = ("--next-token", token) if token else ()
        data = cap.call(f"{label}-{page}", service, operation, *args, *extra)
        rows = data.get(field)
        if not isinstance(rows, list):
            raise Stop(f"Missing result list: {operation}")
        result.extend(rows)
        token = data.get("NextToken")
        if not token:
            complete(data)
            return result
        if not isinstance(token, str) or token in seen:
            raise Stop("Invalid/repeated pagination token")
        seen.add(token)
    raise Stop("Pagination exceeds bounded five-page capture; absence not assessed")


def role_capture(cap, helper, name, label):
    if not re.fullmatch(r"[\w+=,.@-]{1,64}", name, flags=re.ASCII):
        raise Stop("Invalid role name")
    try:
        role = cap.call(label, "iam", "get-role", "--role-name", name)["Role"]
    except helper.AwsError as exc:
        if exc.code == "NoSuchEntity":
            return {"Name": name, "State": "ABSENT"}
        raise
    if (role.get("RoleName") != name or not re.fullmatch(
            rf"arn:aws:iam::{ACCOUNT}:role/.+", role.get("Arn", ""))):
        raise Stop("Role identity/account mismatch")
    inline = complete(cap.call(label + "-inline", "iam", "list-role-policies",
                              "--role-name", name, "--no-paginate"))
    attached = complete(cap.call(label + "-attached", "iam", "list-attached-role-policies",
                                "--role-name", name, "--no-paginate"))
    names = inline.get("PolicyNames")
    policies = attached.get("AttachedPolicies")
    if not isinstance(names, list) or not isinstance(policies, list) or len(names) > 10:
        raise Stop("Missing/excessive role policy inventory")
    for i, policy in enumerate(names, 1):
        cap.call(f"{label}-policy-{i}", "iam", "get-role-policy",
                 "--role-name", name, "--policy-name", policy)
    return {"Name": name, "Arn": role["Arn"], "State": "PRESENT_REVIEW_REQUIRED",
            "PermissionsBoundary": role.get("PermissionsBoundary"),
            "InlinePolicyNames": names, "AttachedPolicies": policies,
            "AttachedPolicyDocuments": "NOT_COLLECTED", "TrustRuntime": "NOT_TESTED"}


def document_capture(cap, helper):
    state = helper.document_capture(cap)
    filters = [{"Key": "Owner", "Values": ["Self"]},
               {"Key": "DocumentType", "Values": ["Session"]}]
    documents = pages(cap, "session-documents", "ssm", "list-documents", "DocumentIdentifiers",
                      "--filters", json.dumps(filters), "--max-results", "20", "--no-paginate")
    if any(d.get("Owner") != ACCOUNT or d.get("DocumentType") != "Session" for d in documents):
        raise Stop("Unexpected owner/type in self Session document inventory")
    matches = [d for d in documents if d.get("Name") == helper.DOCUMENT]
    if len(matches) > 1:
        raise Stop("Duplicate basic document inventory")
    if state["State"] == "ABSENT_OR_UNAVAILABLE":
        inventory = "LISTED_BUT_UNAVAILABLE_REVIEW_REQUIRED" if matches else "NOT_IN_COMPLETE_SELF_SESSION_LIST"
    else:
        if not matches:
            raise Stop("Basic document changed/unlisted during capture")
        inventory = "LISTED"
    return {**state, "SelfSessionDocumentCount": len(documents), "Inventory": inventory,
            "ConfigurationDecision": "HANDOFF_REQUIRED", "Runtime": "NOT_TESTED"}


def instance_summary(instance):
    ident = instance.get("InstanceId", "")
    if not re.fullmatch(r"i-(?:[0-9a-f]{8}|[0-9a-f]{17})", ident):
        raise Stop("Invalid returned instance ID")
    tags = instance.get("Tags", [])
    keys = [t.get("Key") for t in tags]
    if len(set(keys)) != len(keys):
        raise Stop("Duplicate instance tags")
    tag_map = {t["Key"]: t.get("Value") for t in tags}
    return {"InstanceId": ident, "State": instance.get("State", {}).get("Name"),
            "ApprovedTagsMatch": all(tag_map.get(k) == v for k, v in TAGS.items()),
            "InstanceType": instance.get("InstanceType"), "ImageId": instance.get("ImageId"),
            "HandoffShapeMatch": instance.get("InstanceType") == "t3.medium" and
                                 instance.get("ImageId") == "ami-079a2667364cee804",
            "SourceDestCheck": instance.get("SourceDestCheck"),
            "ProfileArn": instance.get("IamInstanceProfile", {}).get("Arn"),
            "BindingDecision": "NOT_MADE"}


def extract_instances(reservations):
    instances = []
    for reservation in reservations:
        if reservation.get("OwnerId") != ACCOUNT or not isinstance(reservation.get("Instances"), list):
            raise Stop("Instance reservation owner/shape mismatch")
        instances.extend(reservation["Instances"])
    ids = [i.get("InstanceId") for i in instances]
    if len(set(ids)) != len(ids):
        raise Stop("Duplicate instance inventory")
    return instances


def selected_dependencies(cap, helper, instance):
    ident = instance["InstanceId"]
    info = complete(cap.call("agent", "ssm", "describe-instance-information",
        "--filters", json.dumps([{"Key": "InstanceIds", "Values": [ident]}]), "--no-paginate"))
    agents = info.get("InstanceInformationList")
    if not isinstance(agents, list) or len(agents) > 1 or any(a.get("InstanceId") != ident for a in agents):
        raise Stop("Agent target/shape mismatch")
    agent = {k: agents[0].get(k) for k in ("InstanceId", "PingStatus", "AgentVersion", "PlatformType")} if agents else {"State": "NOT_LISTED"}
    profile_arn = instance.get("IamInstanceProfile", {}).get("Arn")
    profile_state = {"State": "ABSENT"}
    if profile_arn:
        match = re.fullmatch(rf"arn:aws:iam::{ACCOUNT}:instance-profile/(?:[\w+=,.@-]+/)*([\w+=,.@-]+)", profile_arn)
        if not match:
            raise Stop("Instance profile account/path mismatch")
        profile = cap.call("profile", "iam", "get-instance-profile", "--instance-profile-name", match[1])["InstanceProfile"]
        if profile.get("Arn") != profile_arn or not isinstance(profile.get("Roles"), list) or len(profile["Roles"]) != 1:
            raise Stop("Instance profile ARN/role mismatch")
        role = profile["Roles"][0]
        captured = role_capture(cap, helper, role["RoleName"], "agent-role")
        if captured.get("Arn") != role.get("Arn"):
            raise Stop("Profile role changed/mismatched during capture")
        profile_state = {"State": "CAPTURED_REVIEW_REQUIRED", "Arn": profile_arn, "Role": captured}
    volume_ids = [b["Ebs"]["VolumeId"] for b in instance.get("BlockDeviceMappings", []) if "Ebs" in b]
    if len(volume_ids) != len(set(volume_ids)) or any(not re.fullmatch(r"vol-(?:[0-9a-f]{8}|[0-9a-f]{17})", v) for v in volume_ids):
        raise Stop("Invalid/duplicate volume binding")
    volumes, keys = [], []
    if volume_ids:
        data = complete(cap.call("volumes", "ec2", "describe-volumes", "--volume-ids", *volume_ids, "--no-paginate"))
        rows = data.get("Volumes")
        if not isinstance(rows, list) or len(rows) != len(volume_ids) or {v.get("VolumeId") for v in rows} != set(volume_ids):
            raise Stop("Volume response coverage mismatch")
        for row in rows:
            if not any(a.get("InstanceId") == ident for a in row.get("Attachments", [])):
                raise Stop("Volume attachment changed/mismatched")
            volumes.append({k: row.get(k) for k in ("VolumeId", "State", "Encrypted", "KmsKeyId")})
        for index, arn in enumerate(sorted({v["KmsKeyId"] for v in volumes if v.get("KmsKeyId")}), 1):
            if not re.fullmatch(rf"arn:aws:kms:{REGION}:{ACCOUNT}:key/[0-9a-f-]+", arn):
                raise Stop("EBS KMS ARN outside selected account/region")
            metadata = cap.call(f"ebs-key-{index}", "kms", "describe-key", "--key-id", arn)["KeyMetadata"]
            if metadata.get("Arn") != arn or metadata.get("AWSAccountId") != ACCOUNT:
                raise Stop("KMS metadata identity mismatch")
            cap.call(f"ebs-key-policy-{index}", "kms", "get-key-policy", "--key-id", arn, "--policy-name", "default")
            keys.append({k: metadata.get(k) for k in ("Arn", "KeyManager", "KeyState", "Enabled")})
    return {"Agent": agent, "Profile": profile_state, "EBSVolumes": volumes, "EBSKeys": keys,
            "SessionKMS": "SEPARATE_DOCUMENT_CONFIGURATION_DECISION", "Runtime": "NOT_TESTED"}


def collect(cap, helper, relay_id=None):
    identity = cap.call("identity", "sts", "get-caller-identity")
    if identity.get("Arn") != ROOT or identity.get("Account") != ACCOUNT:
        raise Stop("Expected account root session required")
    summary = {"ExecutionArn": identity["Arn"], "Document": document_capture(cap, helper),
               "NetworkRole": role_capture(cap, helper, "FDS-Network-Operator", "network-role")}
    if relay_id:
        if not re.fullmatch(r"i-(?:[0-9a-f]{8}|[0-9a-f]{17})", relay_id) or relay_id == "i-00000000000000000":
            raise Stop("Actual explicit Relay ID required")
        data = complete(cap.call("selected-instance", "ec2", "describe-instances", "--instance-ids", relay_id, "--no-paginate"))
        instances = extract_instances(data.get("Reservations", []))
        if len(instances) != 1 or instances[0].get("InstanceId") != relay_id:
            raise Stop("Selected instance not returned exactly once")
        summary["SelectedRelay"] = instance_summary(instances[0])
        summary["SelectedDependencies"] = selected_dependencies(cap, helper, instances[0])
    else:
        filters = [{"Name": "tag:" + k, "Values": [v]} for k, v in TAGS.items()]
        reservations = pages(cap, "relay-inventory", "ec2", "describe-instances", "Reservations",
            "--filters", json.dumps(filters), "--max-results", "20", "--no-paginate")
        summary["RelayInventory"] = [instance_summary(i) for i in extract_instances(reservations)]
        if any(not i["ApprovedTagsMatch"] for i in summary["RelayInventory"]):
            raise Stop("Filtered inventory contains unapproved tags")
        summary["SelectedRelay"] = "NOT_SELECTED_EVEN_IF_ONE_MATCH"
    return summary


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-parent", type=Path, default=Path.home())
    parser.add_argument("--relay-id", help="Owner-confirmed actual ID; no automatic selection or policy bind")
    parser.add_argument("--offline", action="store_true", help="Verify sources and save plan only; zero AWS calls")
    args = parser.parse_args(argv)
    os.umask(0o077)
    cap, helper = None, None
    try:
        if args.relay_id and (not re.fullmatch(r"i-(?:[0-9a-f]{8}|[0-9a-f]{17})", args.relay_id) or args.relay_id == "i-00000000000000000"):
            raise Stop("Actual explicit Relay ID required")
        helper, paths = dependencies()
        directory = Path(tempfile.mkdtemp(prefix="fds-network-binding-precheck-", dir=args.output_parent))
        cap = helper.Capture(directory)
        print(f"CAPTURE_DIR={directory}", flush=True)
        for name, path in (("binding-collector-source.py", Path(__file__)), ("pinned-helper.py", paths["helper"]), ("proposed-NOT-FOR-ATTACHMENT.json", paths["policy"])):
            cap.write(name, path.read_bytes())
        summary = {"UTC": dt.datetime.now(dt.timezone.utc).isoformat(), "Account": ACCOUNT, "Region": REGION,
            "SourceMerge": SOURCE_MERGE, "HelperSHA256": HELPER_HASH, "TemplateSHA256": POLICY_HASH,
            "Mode": "OFFLINE_PLAN" if args.offline else "SELECTED_DEPENDENCIES" if args.relay_id else "SCOPED_INVENTORY",
            "AWS_MUTATION": "NOT_RUN", "ROLE_GRANT": "NOT_RUN", "FINAL_POLICY": "NOT_CREATED",
            "APPLY_READINESS": "NOT_ASSESSED", "USER_RUNTIME": "NOT_TESTED"}
        cap.write("read-operation-plan.json", {k: sorted(v) for k, v in READ_OPERATIONS.items()})
        if not args.offline:
            summary.update(collect(cap, helper, args.relay_id))
        summary["Collection"] = "COMPLETE"
        cap.write("summary.json", summary)
        cap.manifest()  # Persist before printing success.
        print(json.dumps(summary, ensure_ascii=True, indent=2))
        print("NETWORK_BINDING_CAPTURE=COMPLETE" if not args.offline else "OFFLINE_PLAN=COMPLETE")
        print("AWS_MUTATION=NOT_RUN")
        return 0
    except Exception as exc:
        print(f"STOP: {type(exc).__name__}: {exc}", file=sys.stderr)
        if cap:
            try:
                cap.write("failure-summary.json", {"Collection": "STOPPED_PARTIAL", "ErrorType": type(exc).__name__, "Reason": str(exc), "AWS_MUTATION": "NOT_RUN", "APPLY_READINESS": "NOT_ASSESSED"})
                if not (cap.directory / "SHA256SUMS").exists():
                    cap.manifest()
                print(f"PRESERVED_DIR={cap.directory}", file=sys.stderr)
            except Exception:
                print("STOP: partial manifest persistence failed", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
