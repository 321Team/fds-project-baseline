# 누락 context 9케이스 보완 실험

CODEX_ASSISTED. #35 중앙 부분 IAM 후보의 음성 판정 근거 조사다. 원래46케이스·archive·정책·capture는 보존한다. 신규 명령 블록은 PR146 승인 코드 자체가 아니며, 기존 `Capture`·`check_simulation`을 재사용하는 일회성 후보 실험이다. IAM/S3 설정·권한을 변경하거나 배포/병합 gate로 사용하지 않는다.

## 대상과 의미

사용자가 전달한 기존 집계는46 responses/93 actions, allowed28·explicitDeny50·implicitDeny15다. explicitDeny의 근거 없는 행0, matched statements는 identity8/resource42다. implicitDeny15 중14 action에 누락 context가 있어 아래9케이스만 보완한다. API의 MissingContextValues는 입력 정책에 필요한 키의 보고이며 각 거부 원인의 확정 설명이 아니다.

| 원래 case | 기존 거부 조건·action 수 | 추가할 누락 키 |
|---|---|---|
| 11–13 | 다른 key/bucket/workspace, GetObject·PutObject 각2 | iam:PassedToService, s3:prefix |
| 14–15 | 다른 지역/TLS false, GetObject·PutObject 각2 | iam:PassedToService, s3:prefix |
| 16 | 다른 principal, GetObject1 | iam:PassedToService, s3:prefix |
| 19 | 다른 prefix, ListBucket1 | iam:PassedToService |
| 23–24 | 다른 role/service, PassRole 각1 | s3:prefix |

원문 정책에서 `s3:prefix`는 ListBucket Allow, `iam:PassedToService`는 PassRole Allow에만 있다. 다른 action 문장의 키도 보고된 것으로 **추정**하며 보완 결과 전까지 확정하지 않는다. case19의 `other/`, case24의 `lambda.amazonaws.com`, 지역·TLS·principal·resource·정책 문자열을 그대로 유지한다. case25의 implicitDeny는 누락 context가 없어 다시 실행하지 않는다.

## 중앙 root CloudShell에서 한 번 실행

원래 collector 해시와 capture manifest를 먼저 확인한다. 보존 입력9개는 승인 소스가 만든 원래 요청과 구조 전체를 대조하고, 기존 키가 없을 때만 값을 추가한다. 새로운 private 형제 디렉터리에 요청·raw·progress·manifest를 기록한다. STS1 + custom simulation9 성공 응답을 목표로 하며, 기존 collector의 bounded retry/timeout을 재사용한다. 설정 조회·ValidatePolicy·나머지37케이스는 반복하지 않는다.

```bash
python3 - <<'PY'
import copy, hashlib, importlib.util, json, os, pathlib, subprocess, tempfile

os.umask(0o077)
home = pathlib.Path.home()
package = home / "fds-iac-delta-run-20261007-01/fds-iac-delta-precheck-20261007"
helper = package / "phase2/permissions/20261007-iac-delta-precheck/capture-iac-delta-precheck.py"
original = home / "fds-iac-delta-precheck-j2uxfqvr"
if hashlib.sha256(helper.read_bytes()).hexdigest() != "277f0b08695e486186820ec26d2087502467e2de585d10a64cf6b5f59d3b04f5":
    raise SystemExit("STOP: collector 해시 불일치")
subprocess.run(["sha256sum", "-c", "--status", "SHA256SUMS"], cwd=original, check=True)
spec = importlib.util.spec_from_file_location("reviewed_collector", helper)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
docs = mod.load_source(package / "phase2/permissions/20261006-iac-fixed-inputs")
cases = mod.simulation_cases(docs["candidates/iac-backend-passrole.candidate.json"], docs["candidates/state-bucket-policy.candidate.json"])
selected = (11, 12, 13, 14, 15, 16, 19, 23, 24)
pending = []
for number in selected:
    raw = (original / f"case-{number:02d}-input.json").read_bytes()
    request = json.loads(raw)
    if request != cases[number - 1]["Request"]:
        raise SystemExit(f"STOP: 보존 입력과 승인 소스 불일치 CASE={number:02d}")
    amended = copy.deepcopy(request)
    names = {c["ContextKeyName"] for c in amended["ContextEntries"]}
    added = []
    for key, value in (("iam:PassedToService", "ec2.amazonaws.com"), ("s3:prefix", "phase2/")):
        if key not in names:
            amended["ContextEntries"].append({"ContextKeyName": key, "ContextKeyValues": [value], "ContextKeyType": "string"})
            added.append(key)
    pending.append((number, raw, amended, added))

output = pathlib.Path(tempfile.mkdtemp(prefix="fds-iac-context-completion-", dir=home))
capture = mod.Capture(output)
print("CONTEXT_DIR=" + str(output), flush=True)
rows = []
rc = 1
try:
    identity = capture.call("identity", "sts", "get-caller-identity")
    if identity.get("Arn") != mod.ROOT or identity.get("Account") != mod.ACCOUNT:
        raise mod.Stop("예상한 중앙 root 계정이 아님")
    capture.save("origin.json", {"OriginalDirectory": str(original), "CollectorSHA256": hashlib.sha256(helper.read_bytes()).hexdigest(), "AWS_MUTATION": "NOT_RUN"})
    for number, raw, request, added in pending:
        path = capture.save(f"case-{number:02d}-input.json", request)
        response = capture.call(f"case-{number:02d}", "iam", "simulate-custom-policy", "--cli-input-json", "file://" + str(path))
        mod.check_simulation({"Request": request, "Expected": "implicitDeny", "Label": f"context-{number:02d}"}, response)
        missing = sorted({key for row in response["EvaluationResults"] for item in [row, *row.get("ResourceSpecificResults", [])] for key in item.get("MissingContextValues", [])})
        rows.append({"Case": number, "OriginalInputSHA256": hashlib.sha256(raw).hexdigest(), "AddedContext": added, "Actions": len(response["EvaluationResults"]), "Decisions": [r["EvalDecision"] for r in response["EvaluationResults"]], "MissingContext": missing})
        capture.save("progress.json", rows)
        print(f"CASE={number:02d} ACTIONS={rows[-1]['Actions']} ACTUAL={rows[-1]['Decisions']} MISSING={missing}", flush=True)
    summary = {"Collection": "COMPLETE", "Cases": len(rows), "Actions": sum(r["Actions"] for r in rows), "AllImplicitDeny": True, "CasesWithMissingContext": sum(bool(r["MissingContext"]) for r in rows), "AWS_MUTATION": "NOT_RUN", "ROLE_GRANT": "NOT_RUN", "USER_RUNTIME": "NOT_TESTED"}
    capture.save("summary.json", summary)
    print(json.dumps(summary), flush=True)
    rc = 0
except Exception as exc:
    capture.save("stop.json", {"Collection": "INCOMPLETE", "ErrorType": type(exc).__name__, "Error": str(exc), "AWS_MUTATION": "NOT_RUN"})
    print("STOP: " + str(exc), flush=True)
finally:
    mod.write_manifest(output)
    print("AWS_MUTATION=NOT_RUN\nPRESERVED_DIR=" + str(output), flush=True)
raise SystemExit(rc)
PY
printf 'CONTEXT_EXPERIMENT_RC=%s\n' "$?"
```

기대 확인값은 `Cases=9 / Actions=14 / AllImplicitDeny=true / CasesWithMissingContext=0 / RC=0`이다. 이 보완 실험은 아직 AWS에서 실행하지 않았다. 기존46케이스를 실패로 바꾸거나 전체 실효권한 검증 완료로 올리지 않는다. 판정 변화·누락 지속·중단이 있으면 원본을 보존하고 해당 행만 조사한다. 정제 출력과 RC를 전달하며 정책·state·credential 원문은 공개하지 않는다.

로컬 모의 실행에서 정상9케이스·14 action/10 calls, 다른 주체 중단/1 call, 판정 변화 중단/2 calls를 확인했다. 모든 회차에서 원본 입력 bytes·정책·기존 context가 보존되고 새 manifest가 일치했다. Python 구문 검사도 통과했다. 이는 AWS 실제 응답 검증이 아니다.

## 리뷰 분류와 잔여 작업

새 실행 블록을 추가했으므로 PR147의 이번 diff를 문서만으로 분류하지 않는다. 새 블록과 영향 범위는 독립 리뷰 후 Lead가 병합을 판단한다. root CloudShell의 후보 simulation은 [REVIEW_AUTHORITY_POLICY §4](https://github.com/321Team/fds-project-baseline/blob/94d41fa49634b868bdbd2509fc9649542e882c78/governance/REVIEW_AUTHORITY_POLICY.md)의 격리 후보 시험 범위다. 신규 로직의 운영 배포·영구 반영·실제 권한 변경은 포함하지 않는다. 새9케이스 명령을 PR146의 과거 승인 범위로 표시하지 않는다.

backend/Relay bootstrap desired source와 실제 full IaC 권한 source 준비는 이어간다. 이번 보완을 Lead 값 재채택이나 source 준비의 대기 조건으로 삼지 않는다. 보완 결과가 갖춰져도 실제 role의 ResourcePolicy 평가·root 복구·본인 U1·apply readiness는 미검증 상태다.

공식 근거: [EvaluationResult](https://docs.aws.amazon.com/IAM/latest/APIReference/API_EvaluationResult.html), [IAM policy simulator](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html).
