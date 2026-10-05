#!/usr/bin/env python3
"""Offline fixed-contract checker; no AWS API, credentials or writes.
This checks the reviewed project contract, not IAM effective permissions.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

ACCOUNT = "774055931866"
USERS = sorted("arn:aws:iam::" + ACCOUNT + ":user/" + name for name in
               ("321team-gwonuk", "321team-hayeoung", "321team-jaehwan"))
ROLE = "arn:aws:iam::" + ACCOUNT + ":role/"
REGIONAL_ACTIONS = [
    "ec2:" + action for action in (
        "DescribeInstances", "DescribeInstanceTypes", "DescribeInstanceTypeOfferings",
        "DescribeImages", "DescribeAvailabilityZones", "DescribeVpcs", "DescribeSubnets",
        "DescribeRouteTables", "DescribeNetworkInterfaces", "DescribeSecurityGroups",
        "DescribeSecurityGroupRules", "DescribeAddresses", "DescribeNatGateways",
        "DescribeInternetGateways", "DescribeVolumes", "DescribeVpcEndpoints")
] + [
    "elasticloadbalancing:DescribeLoadBalancers", "elasticloadbalancing:DescribeTargetGroups",
    "cloudshell:CreateEnvironment", "cloudshell:CreateSession", "cloudshell:GetEnvironmentStatus",
    "cloudshell:StartEnvironment", "cloudshell:PutCredentials",
    "servicequotas:GetServiceQuota", "servicequotas:ListServiceQuotas",
    "servicequotas:ListRequestedServiceQuotaChangeHistory"
]
# Action/Resource source: user root readback 2026-10-05 09:47 KST,
# Inventory-ReadOnly-v1 and ROSA-Prereq-ReadOnly-v1. Not fetched live here.
CONTRACT = {
    "SeoulInventoryAndCloudShellWithMFA": (REGIONAL_ACTIONS, "*", True),
    "InspectExistingAuditRoleWithMFA": (
        ["iam:GetRole", "iam:ListRolePolicies", "iam:GetRolePolicy"],
        ROLE + "FDS-ReadOnly-Audit", False),
    "ViewSubscriptionsWithMFA": (["aws-marketplace:ViewSubscriptions"], "*", False),
    "ListRoleMetadataWithMFA": (["iam:ListRoles"], "*", False),
    "InspectELBRoleWithMFA": (["iam:GetRole"], ROLE +
        "aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing",
        False),
}

def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError("duplicate JSON key: " + key)
        obj[key] = value
    return obj

def read(path):
    raw = path.read_bytes()
    return json.loads(raw, object_pairs_hook=unique_object), hashlib.sha256(raw).hexdigest()

def strings(value):
    items = [value] if isinstance(value, str) else value
    if not isinstance(items, list) or not items or any(not isinstance(x, str) for x in items):
        raise ValueError("expected nonempty string/list")
    if len(set(items)) != len(items):
        raise ValueError("duplicate set entry")
    return sorted(items)

def validate(policy):
    if not isinstance(policy, dict) or set(policy) != {"Version", "Statement"}:
        raise ValueError("unexpected top-level policy fields")
    if policy["Version"] != "2012-10-17" or not isinstance(policy["Statement"], list):
        raise ValueError("unsupported policy structure")
    seen = set()
    for statement in policy["Statement"]:
        if not isinstance(statement, dict) or set(statement) != {
                "Sid", "Effect", "Action", "Resource", "Condition"}:
            raise ValueError("unexpected statement fields")
        sid = statement["Sid"]
        if not isinstance(sid, str) or sid not in CONTRACT or sid in seen:
            raise ValueError("unexpected or duplicate Sid")
        seen.add(sid)
        actions, resource, regional = CONTRACT[sid]
        if statement["Effect"] != "Allow" or strings(statement["Action"]) != sorted(actions):
            raise ValueError(sid + ": Action/Effect differs from source contract")
        if strings(statement["Resource"]) != [resource]:
            raise ValueError(sid + ": Resource changed")
        expected = {"Bool": {"aws:MultiFactorAuthPresent": "true"},
                    "ArnEquals": {"aws:PrincipalArn": USERS}}
        if regional:
            expected["StringEquals"] = {"aws:RequestedRegion": "ap-northeast-2"}
        condition = statement["Condition"]
        if not isinstance(condition, dict):
            raise ValueError(sid + ": invalid Condition")
        # Normalize only the exact PrincipalArn set. No BoolIfExists/ArnLike substitutions.
        condition = json.loads(json.dumps(condition))
        if isinstance(condition.get("ArnEquals"), dict) and "aws:PrincipalArn" in condition["ArnEquals"]:
            condition["ArnEquals"]["aws:PrincipalArn"] = strings(condition["ArnEquals"]["aws:PrincipalArn"])
        if condition != expected:
            raise ValueError(sid + ": MFA/principal/region contract changed")
    if seen != set(CONTRACT):
        raise ValueError("missing statements")
    return True

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--policy", type=Path, default=Path(__file__).resolve().parents[1] /
                        "inputs/human-direct-readonly.candidate.json")
    parser.add_argument("--readback", type=Path, help="optional PolicyDocument JSON from get-group-policy --query")
    args = parser.parse_args()
    try:
        policy, digest = read(args.policy)
        validate(policy)
        result = {"OFFLINE_CONTRACT": "PASS", "POLICY_SHA256": digest,
                  "AWS_EFFECTIVE_PERMISSIONS": "NOT_TESTED", "AWS_MUTATION": "NOT_RUN"}
        if args.readback:
            actual, actual_hash = read(args.readback)
            validate(actual)
            result.update(READBACK_CONTRACT="PASS", READBACK_SHA256=actual_hash)
        print(json.dumps(result, sort_keys=True))
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print("STOP: " + str(exc), file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
