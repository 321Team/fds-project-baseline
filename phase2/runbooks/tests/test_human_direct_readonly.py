"""Offline security-regression tests; fixture is the actual candidate JSON."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("checker", ROOT / "check-human-direct-readonly.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
POLICY = json.loads((ROOT.parent / "inputs/human-direct-readonly.candidate.json").read_text())

class ContractTests(unittest.TestCase):
    def test_current_candidate(self):
        self.assertTrue(checker.validate(POLICY))

    def test_equivalent_order_and_scalar_representation(self):
        p = copy.deepcopy(POLICY)
        p["Statement"].reverse()
        for s in p["Statement"]:
            if isinstance(s["Action"], list):
                s["Action"].reverse()
            else:
                s["Action"] = [s["Action"]]
            s["Resource"] = [s["Resource"]]
            s["Condition"]["ArnEquals"]["aws:PrincipalArn"].reverse()
        self.assertTrue(checker.validate(p))

    def test_unsafe_changes_rejected(self):
        def condition_change(p, key, value):
            p["Statement"][0]["Condition"][key] = value
        mutations = [
            ("MFA removed", lambda p: p["Statement"][0]["Condition"].pop("Bool")),
            ("MFA false", lambda p: condition_change(p, "Bool", {"aws:MultiFactorAuthPresent": "false"})),
            ("MFA missing accepted", lambda p: condition_change(p, "BoolIfExists", p["Statement"][0]["Condition"].pop("Bool"))),
            ("fourth user", lambda p: p["Statement"][0]["Condition"]["ArnEquals"]["aws:PrincipalArn"].append("arn:aws:iam::774055931866:user/other")),
            ("region removed", lambda p: p["Statement"][0]["Condition"].pop("StringEquals")),
            ("other region", lambda p: condition_change(p, "StringEquals", {"aws:RequestedRegion": "us-east-1"})),
            ("create permission", lambda p: p["Statement"][0]["Action"].append("ec2:RunInstances")),
            ("wildcard actions", lambda p: p["Statement"][0].update(Action="*")),
            ("ELB wildcard ARN", lambda p: p["Statement"][-1].update(Resource="*")),
            ("NotAction alternative", lambda p: p["Statement"][0].update(NotAction="iam:*")),
            ("missing grant", lambda p: p["Statement"].pop()),
            ("duplicate grant", lambda p: p["Statement"].append(copy.deepcopy(p["Statement"][0]))),
        ]
        for name, mutate in mutations:
            with self.subTest(name=name):
                p = copy.deepcopy(POLICY)
                mutate(p)
                with self.assertRaises(ValueError):
                    checker.validate(p)

    def test_duplicate_json_key_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"Effect":"Deny","Effect":"Allow"}', object_pairs_hook=checker.unique_object)

if __name__ == "__main__":
    unittest.main()
