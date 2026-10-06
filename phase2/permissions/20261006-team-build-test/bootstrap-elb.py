#!/usr/bin/env python3
"""Check or create only the project's ELB service-linked role.

Default is read-only. --apply requires the exact education account root.
No IAM user/group grant, ELB resource, retry, or automatic deletion is performed.
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys

ACCOUNT = "774055931866"
SERVICE = "elasticloadbalancing.amazonaws.com"
NAME = "AWSServiceRoleForElasticLoadBalancing"
PATH = "/aws-service-role/" + SERVICE + "/"
ARN = "arn:aws:iam::" + ACCOUNT + ":role" + PATH + NAME
ROOT = "arn:aws:iam::" + ACCOUNT + ":root"


class Stop(RuntimeError):
    pass


class AwsError(Stop):
    def __init__(self, operation, code, detail):
        self.operation = operation
        self.code = code
        super().__init__(f"{operation}: {code}: {detail}")


def aws(service, operation, *args):
    command = ["aws", service, operation, *args,
               "--output", "json", "--no-cli-pager"]
    try:
        result = subprocess.run(command, capture_output=True, text=True,
                                timeout=60, check=False)
    except (subprocess.TimeoutExpired, OSError) as exc:
        raise AwsError(operation, "RESULT_UNKNOWN", str(exc)) from exc
    if result.returncode:
        match = re.search(r"\(([A-Za-z0-9]+)\) when calling the [A-Za-z0-9]+ operation", result.stderr)
        code = match.group(1) if match else "UNCLASSIFIED"
        raise AwsError(operation, code,
                       f"RC={result.returncode} {result.stderr.strip()}")
    try:
        payload = json.loads(result.stdout)
    except (ValueError, TypeError) as exc:
        raise AwsError(operation, "INVALID_JSON",
                       "Successful CLI response was not valid JSON") from exc
    if not isinstance(payload, dict):
        raise AwsError(operation, "INVALID_RESPONSE", "Expected a JSON object")
    return payload


def validate_role(role):
    if not isinstance(role, dict):
        raise Stop("Role response is missing")
    if (role.get("Arn"), role.get("Path"), role.get("RoleName")) != (ARN, PATH, NAME):
        raise Stop("Unexpected ELB role account/ARN/path/name")
    trust = role.get("AssumeRolePolicyDocument")
    if not isinstance(trust, dict):
        raise Stop("Missing ELB service trust")
    statements = trust.get("Statement", [])
    if isinstance(statements, dict):
        statements = [statements]
    if not isinstance(statements, list):
        raise Stop("Unexpected trust statement format")
    allows = [s for s in statements if isinstance(s, dict) and s.get("Effect") == "Allow"]
    if not allows:
        raise Stop("No ELB service trust Allow")
    for statement in allows:
        action = statement.get("Action")
        actions = [action] if isinstance(action, str) else action
        principal = statement.get("Principal")
        if not isinstance(principal, dict) or set(principal) != {"Service"}:
            raise Stop("Unexpected trust principal")
        service = principal["Service"]
        services = [service] if isinstance(service, str) else service
        if services != [SERVICE] or actions != ["sts:AssumeRole"]:
            raise Stop("Unexpected ELB service trust Allow")


def run(apply=False, call=aws):
    print("UTC=" + dt.datetime.now(dt.timezone.utc).isoformat())
    identity = call("sts", "get-caller-identity")
    if identity.get("Account") != ACCOUNT:
        raise Stop("Execution account mismatch")
    if apply and identity.get("Arn") != ROOT:
        raise Stop("--apply requires the exact education account root")
    print("EXECUTION_ARN=" + str(identity.get("Arn")))
    try:
        response = call("iam", "get-role", "--role-name", NAME)
    except AwsError as exc:
        if exc.operation != "get-role" or exc.code != "NoSuchEntity":
            raise
        response = None
    if response is not None:
        validate_role(response.get("Role"))
        print("ELB_ROLE_CHECK=PASS")
        print("ELB_CREATE=SKIP_EXISTING")
        print("AWS_MUTATION=NOT_RUN")
        return
    if not apply:
        print("ELB_ROLE_CHECK=ABSENT")
        print("ELB_CREATE=NOT_RUN")
        print("AWS_MUTATION=NOT_RUN")
        return
    # After this line any timeout/error may leave the role created.
    # Preserve the error and check with default mode; never automatically retry.
    print("ELB_CREATE=ATTEMPTING", flush=True)
    created = call("iam", "create-service-linked-role", "--aws-service-name", SERVICE)
    validate_role(created.get("Role"))
    applied = call("iam", "get-role", "--role-name", NAME)
    validate_role(applied.get("Role"))
    print("ELB_ROLE_CHECK=PASS")
    print("ELB_CREATE=CREATED")
    print("AWS_MUTATION=CREATE_ELB_SERVICE_LINKED_ROLE_ONLY")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="Create the exact missing ELB role using education root")
    args = parser.parse_args()
    try:
        run(apply=args.apply)
    except Stop as exc:
        print("STOP: " + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

