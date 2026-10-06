"""Offline review fixtures only: this is not an AWS IAM policy simulator.

The matcher supports only this bundle's single-valued conditions. It does not
model SCPs, permissions boundaries, API dependencies, principal trust, AWS
resource applicability, or live backend behaviour. Unsupported syntax fails.
"""
import fnmatch
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ACCOUNT = "774055931866"
REGION = "ap-northeast-2"
BUCKET = f"arn:aws:s3:::fds-tfstate-{ACCOUNT}-{REGION}"
IAC = f"arn:aws:iam::{ACCOUNT}:role/FDS-IaC-Operator"
RELAY = f"arn:aws:iam::{ACCOUNT}:role/FDS-Relay-SSM"
PROFILE = f"arn:aws:iam::{ACCOUNT}:instance-profile/FDS-Relay-SSM"
CENTRAL = f"arn:aws:iam::{ACCOUNT}:root"
COMPONENTS = ("network", "vpn", "rosa-prereq", "rosa-runtime")
STATES = [f"{BUCKET}/phase2/{c}/terraform.tfstate" for c in COMPONENTS]
LOCKS = [s + ".tflock" for s in STATES]


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def read_json(name):
    return json.loads((ROOT / name).read_text(), object_pairs_hook=unique_object)


def values(value):
    return value if isinstance(value, list) else [value]


def condition_matches(conditions, context):
    for operator, entries in conditions.items():
        for key, wanted in entries.items():
            actual = context.get(key)
            expected = values(wanted)
            if operator == "Null":
                ok = (actual is None) == (str(wanted).lower() == "true")
            elif operator == "Bool":
                ok = actual is not None and str(actual).lower() in [str(x).lower() for x in expected]
            elif operator in ("StringEquals", "ArnEquals"):
                ok = actual is not None and actual in expected
            elif operator in ("StringNotEquals", "ArnNotEquals"):
                ok = actual is None or actual not in expected
            elif operator == "StringLike":
                ok = actual is not None and any(fnmatch.fnmatchcase(actual, x) for x in expected)
            else:
                raise ValueError(f"unsupported fixture condition: {operator}")
            if not ok:
                return False
    return True


def match_statements(policy, action, resource, context):
    matches = []
    for statement in policy["Statement"]:
        if "Principal" in statement and statement["Principal"] != "*":
            raise ValueError("fixture matcher only supports Principal=*")
        if ("Action" in statement) == ("NotAction" in statement):
            raise ValueError("exactly one Action/NotAction required")
        field = "Action" if "Action" in statement else "NotAction"
        included = any(fnmatch.fnmatchcase(action.lower(), x.lower()) for x in values(statement[field]))
        if (field == "Action" and not included) or (field == "NotAction" and included):
            continue
        if not any(fnmatch.fnmatchcase(resource, x) for x in values(statement["Resource"])):
            continue
        if condition_matches(statement.get("Condition", {}), context):
            matches.append(statement)
    return matches


def identity_match(policy, action, resource, context):
    matches = match_statements(policy, action, resource, context)
    if any(x["Effect"] == "Deny" for x in matches):
        return "deny-matched"
    if any(x["Effect"] == "Allow" for x in matches):
        return "allow-matched"
    return "no-allow-matched"


def context(principal=IAC, region=REGION, tls=True, **extra):
    return {"aws:PrincipalArn": principal, "aws:RequestedRegion": region,
            "aws:SecureTransport": tls, "aws:PrincipalIsAWSService": False, **extra}


class FixedInputs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.identity = read_json("candidates/iac-backend-passrole.candidate.json")
        cls.bucket = read_json("candidates/state-bucket-policy.candidate.json")

    def test_backend_normal_operations(self):
        for resource in STATES + LOCKS:
            for action in ("s3:GetObject", "s3:PutObject"):
                with self.subTest(resource=resource, action=action):
                    self.assertEqual(identity_match(self.identity, action, resource, context()), "allow-matched")
        for lock in LOCKS:
            self.assertEqual(identity_match(self.identity, "s3:DeleteObject", lock, context()), "allow-matched")

    def test_state_and_version_deletion_explicitly_blocked(self):
        for state in STATES:
            self.assertEqual(identity_match(self.identity, "s3:DeleteObject", state, context()), "deny-matched")
        for resource in STATES + LOCKS:
            self.assertEqual(identity_match(self.identity, "s3:DeleteObjectVersion", resource, context()), "deny-matched")

    def test_other_keys_buckets_and_workspaces_have_no_allow(self):
        for resource in (BUCKET + "/phase2/network/backup.tfstate", BUCKET + "/env:/dev/phase2/network/terraform.tfstate",
                         "arn:aws:s3:::other-bucket/phase2/network/terraform.tfstate"):
            for action in ("s3:GetObject", "s3:PutObject", "s3:DeleteObject"):
                self.assertEqual(identity_match(self.identity, action, resource, context()), "no-allow-matched")

    def test_wrong_principal_region_and_tls_have_no_backend_allow(self):
        for ctx in (context(principal=CENTRAL), context(principal=f"arn:aws:iam::{ACCOUNT}:user/321team-gwonuk"),
                    context(principal=f"arn:aws:sts::{ACCOUNT}:assumed-role/FDS-IaC-Operator/321team-gwonuk"),
                    context(principal=None), context(region="ap-northeast-1"), context(tls=False), context(tls=None)):
            for action in ("s3:GetObject", "s3:PutObject"):
                self.assertEqual(identity_match(self.identity, action, STATES[0], ctx), "no-allow-matched")

    def test_prefix_metadata_without_nondefault_object_access(self):
        for prefix in ("phase2/", "phase2/vpn/", "phase2/network/terraform.tfstate", "env:/"):
            self.assertEqual(identity_match(self.identity, "s3:ListBucket", BUCKET, context(**{"s3:prefix": prefix})), "allow-matched")
        for prefix in ("", "env:/dev/", "unrelated/", None):
            self.assertEqual(identity_match(self.identity, "s3:ListBucket", BUCKET, context(**{"s3:prefix": prefix})), "no-allow-matched")

    def test_exact_passrole_service_and_global_iam_lookup(self):
        good = context(region="us-east-1", **{"iam:PassedToService": "ec2.amazonaws.com"})
        self.assertEqual(identity_match(self.identity, "iam:PassRole", RELAY, good), "allow-matched")
        self.assertEqual(identity_match(self.identity, "iam:GetRole", RELAY, good), "allow-matched")
        self.assertEqual(identity_match(self.identity, "iam:GetInstanceProfile", PROFILE, good), "allow-matched")
        for resource, ctx in ((PROFILE, good), (RELAY + "-other", good), (RELAY, context()),
                              (RELAY, context(**{"iam:PassedToService": "lambda.amazonaws.com"}))):
            self.assertEqual(identity_match(self.identity, "iam:PassRole", resource, ctx), "no-allow-matched")

    def test_protected_bucket_and_relay_identity_mutation(self):
        for action in ("s3:DeleteBucket", "s3:PutBucketPolicy", "s3:PutEncryptionConfiguration", "s3:PutLifecycleConfiguration"):
            self.assertEqual(identity_match(self.identity, action, BUCKET, context()), "deny-matched")
        for action, resource in (("iam:PutRolePolicy", RELAY), ("iam:AttachRolePolicy", RELAY),
                                 ("iam:UpdateAssumeRolePolicy", RELAY), ("iam:AddRoleToInstanceProfile", PROFILE)):
            self.assertEqual(identity_match(self.identity, action, resource, context()), "deny-matched")

    def test_bucket_payload_and_mutation_deny_nonusers(self):
        principals = [f"arn:aws:iam::{ACCOUNT}:user/{u}" for u in
                      ("321team-gwonuk", "321team-hayeoung", "321team-jaehwan")]
        principals += [f"arn:aws:iam::{ACCOUNT}:role/FDS-ReadOnly-Audit",
                       f"arn:aws:iam::{ACCOUNT}:role/FDS-Network-Operator", None]
        for principal in principals:
            for resource in STATES + LOCKS:
                for action in ("s3:GetObject", "s3:GetObjectVersion", "s3:PutObject", "s3:DeleteObject",
                               "s3:PutObjectAcl", "s3:UpdateObjectEncryption"):
                    matches = match_statements(self.bucket, action, resource, context(principal=principal))
                    self.assertTrue(any(s["Sid"] == "DenyStatePayloadAndMutationOutsideApprovedPrincipals" for s in matches))

    def test_bucket_whitelist_is_not_an_allow(self):
        for principal in (IAC, CENTRAL):
            self.assertEqual(match_statements(self.bucket, "s3:GetObject", STATES[0], context(principal=principal)), [])
        self.assertTrue(all(s["Effect"] == "Deny" for s in self.bucket["Statement"]))

    def test_bucket_metadata_and_transport(self):
        ordinary = context(principal=f"arn:aws:iam::{ACCOUNT}:user/321team-gwonuk")
        for action, resource in (("s3:ListBucket", BUCKET), ("s3:GetBucketLocation", BUCKET),
                                 ("s3:GetObjectTagging", STATES[0]), ("s3:GetObjectAcl", STATES[0])):
            self.assertEqual(match_statements(self.bucket, action, resource, ordinary), [])
        for principal in (IAC, CENTRAL):
            matches = match_statements(self.bucket, "s3:GetObject", STATES[0], context(principal=principal, tls=False))
            self.assertTrue(any(s["Sid"] == "DenyInsecureTransport" for s in matches))
        service = context(principal=None, tls=False, **{"aws:PrincipalIsAWSService": True})
        self.assertTrue(match_statements(self.bucket, "s3:GetObject", STATES[0], service))

    def test_encryption_absent_aes256_and_incompatible_headers(self):
        self.assertEqual(match_statements(self.bucket, "s3:PutObject", STATES[0], context()), [])
        self.assertEqual(match_statements(self.bucket, "s3:PutObject", LOCKS[0], context(**{"s3:x-amz-server-side-encryption": "AES256"})), [])
        for extra in ({"s3:x-amz-server-side-encryption": "aws:kms"},
                      {"s3:x-amz-server-side-encryption": "aws:kms:dsse"},
                      {"s3:x-amz-server-side-encryption-customer-algorithm": "AES256"}):
            self.assertTrue(match_statements(self.bucket, "s3:PutObject", STATES[0], context(**extra)))

    def test_adopted_input_backend_mapping_and_account_guard(self):
        inputs = read_json("inputs/lead-values.json")
        self.assertEqual(inputs["Account"], ACCOUNT)
        self.assertEqual(inputs["Region"], REGION)
        self.assertEqual(inputs["Workspace"], "default")
        self.assertEqual(inputs["StateKeys"], {c: f"phase2/{c}/terraform.tfstate" for c in COMPONENTS})
        self.assertEqual(inputs["ServiceWritePermissions"], "NOT_INCLUDED")
        self.assertEqual(inputs["RoleGrant"], "NOT_RUN")
        self.assertEqual(inputs["ApplyReadiness"], "NOT_ASSESSED")
        for component in COMPONENTS:
            text = (ROOT / "backends" / f"{component}.candidate.hcl").read_text()
            self.assertIn(f'key                 = "phase2/{component}/terraform.tfstate"', text)
            self.assertIn(f'allowed_account_ids = ["{ACCOUNT}"]', text)
            self.assertIn("encrypt             = true", text)
            self.assertIn("use_lockfile        = true", text)
            self.assertNotRegex(text, r"(?i)(access_key|secret_key|token|skip_|dynamodb)")
            self.assertNotIn("REPLACE_", text)

    def test_allow_scope_excludes_service_cost_kms_and_mutable_iam(self):
        allowed = [a for s in self.identity["Statement"] if s["Effect"] == "Allow" for a in values(s["Action"])]
        self.assertEqual(set(allowed), {"s3:GetBucketLocation", "s3:ListBucket", "s3:GetObject", "s3:PutObject", "s3:DeleteObject",
                                        "iam:GetRole", "iam:GetInstanceProfile", "iam:PassRole"})
        self.assertNotIn("*", allowed)
        for s in self.identity["Statement"]:
            if s["Effect"] == "Allow":
                self.assertNotIn("*", values(s["Resource"]))
                self.assertEqual(s["Condition"]["ArnEquals"]["aws:PrincipalArn"], IAC)
        with self.assertRaises(ValueError):
            json.loads('{"Version": "a", "Version": "b"}', object_pairs_hook=unique_object)


if __name__ == "__main__":
    unittest.main(verbosity=2)
