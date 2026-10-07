# ROSA prerequisites: 과거 IAM 조회 권한 보완안 및 현재 실행 경계
기준: 2026-10-03 17:38:57 KST 사용자 ROSA console 출력.
Source: 사용자 계정조회이며 Assistant live AWS readback 아님. CODEX_ASSISTED.

## 현재 P2 준비에서의 사용 — 2026-10-05 정정
이 파일명에 readonly가 있어도 아래 과거 코드는 IAM write를 포함한다. `put-role-policy`는 권한 변경이고 `delete-role-policy`는 그 제거다. 이 문서를 여는 것 또는 일반적인 사전 작업 착수 지시는 이 코드의 실행 승인이 아니다.
현재 작업은 Phase 1 진행 중이며 IAM/공용 환경을 바꾸지 않는다. 아래 과거 root 실행안을 다시 수행하지 않는다. 이미 적용된 정책이 있다면 재적용하지 않으며, 적용 여부·권한은 기존 기록과 별도 관측 범위로 판단한다.
현재 조회 준비의 진입점은 [고정 AWS 조회 수집](20261003-readiness-evidence-capture.md)이다. 기존 MFA assumed read-only role을 사용하며 root가 필요하지 않다. 실제 수집의 독립 검토·역할/계정 확인 조건은 해당 절차를 유지한다.
원래 제안과 명령은 추적성을 위해 아래에 보존한다. 이를 새로운 Runtime GO나 과거 적용 실패/성공 판정으로 해석하지 않는다.

## 작성 당시 판정
- 화면은 quota 요구 충족을 표시하나 각 quota 전체 exact readback/최종 HCP sizing 승인으로 확대하지 않는다.
- ROSA activation 상태는 ViewSubscriptions 거부로 UNVERIFIED. "활성화하지 못함"을 미구독 또는 실제 activation action 실패로 확정하지 않는다.
- ELB section 실제 거부 action은 ListRoles. 기존 서비스 연결 역할 존재/부재 및 Create 결과는 UNVERIFIED.
- ROSAManageSubscription은 Subscribe/Unsubscribe 포함하므로 조회를 위해 전체 managed policy를 붙이지 않는다.
- 보완: ViewSubscriptions* / ListRoles* / exact ELB GetRole만 허용. Marketplace 구독 및 계정 role metadata는 global조회. ListRoles는 계정 역할 메타데이터 목록 노출이며 의도적으로 이 범위의 조회를 허용한다.
- CreateServiceLinkedRole/CreateRole/PassRole/Subscribe/Unsubscribe 권한을 추가하지 않는다. 기존 3인+MFA trust는 변경하지 않는다.
- 조회를 위한 최소 추가 policy도 독립 리뷰 PENDING; Apply/operator 승인으로 확대하지 않는다.

## 과거 권한 변경 실행안 — 현재 준비 작업에서는 실행하지 않음
다음은 당시 검토한 별도 IAM 변경안이다. 실행 대상이 승인된 경우 같은 프로젝트 계정 root CloudShell에서만 실행. 기존 role/trust/정책은 교체하지 않는다. 새로운 이름 policy가 다른 내용으로 존재하면 중단한다.
POLICY_MATCH=true는 읽은 policy 문서와 기대한 조회 policy 일치만 뜻한다. 권한평가·SCP·ROSA 실제조회 PASS가 아니다.
불일치/오류이면 중단하고 출력 전달. 이 변경을 철회할 경우 이번 추가 policy만 delete-role-policy로 제거; 기존 역할/기존 policy 유지.

```bash
python3 - <<'PY'
import json, subprocess
A = "774055931866"
R = "FDS-ReadOnly-Audit"
P = "FDS-ROSA-Prereq-ReadOnly-v1"
def aws(*args, missing=False):
    r = subprocess.run(["aws", *args, "--output", "json", "--no-cli-pager"],
                       capture_output=True, text=True)
    if r.returncode:
        if missing and "(NoSuchEntity)" in r.stderr: return None
        raise RuntimeError(r.stderr.strip())
    return json.loads(r.stdout or "{}")
def norm(p):
    p = json.loads(json.dumps(p))
    for s in p["Statement"]:
        for key in ("Action", "Resource"):
            if key in s:
                s[key] = sorted(s[key] if isinstance(s[key], list) else [s[key]])
    p["Statement"].sort(key=lambda s: json.dumps(s, sort_keys=True))
    return p
if aws("sts","get-caller-identity")["Arn"] != "arn:aws:iam::"+A+":root":
    raise SystemExit("STOP: project root session required.")
aws("iam","get-role","--role-name",R)
policy = {"Version":"2012-10-17","Statement":[
    {"Sid":"ViewMarketplaceSubscriptions","Effect":"Allow",
     "Action":"aws-marketplace:ViewSubscriptions","Resource":"*"},
    {"Sid":"ListRoleMetadataForROSAConsole","Effect":"Allow",
     "Action":"iam:ListRoles","Resource":"*"},
    {"Sid":"InspectELBServiceLinkedRole","Effect":"Allow",
     "Action":"iam:GetRole","Resource":"arn:aws:iam::"+A+
     ":role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing"}
]}
old = aws("iam","get-role-policy","--role-name",R,"--policy-name",P,missing=True)
if old and norm(old["PolicyDocument"]) != norm(policy):
    raise SystemExit("STOP: same-name policy differs; no overwrite.")
if not old:
    aws("iam","put-role-policy","--role-name",R,"--policy-name",P,
        "--policy-document",json.dumps(policy))
actual = aws("iam","get-role-policy","--role-name",R,"--policy-name",P)
print(json.dumps({"ROLE":R,"POLICY":P,
      "POLICY_MATCH":norm(actual["PolicyDocument"]) == norm(policy),
      "READBACK":actual["PolicyDocument"]},indent=2))

PY
```

이후 root창을 사용하지 않고 권욱 IAM으로 MFA 로그인 후 FDS-ReadOnly-Audit 역할을 새로 전환한다.
ROSA prerequisites 페이지를 새로 열고 현재 activation/quota/ELB 결과만 조회한다.
Enable/Subscribe/Create를 실행하지 않는다. absent ELB role의 자동생성 시도가 거부된다면 의도한 조회 경계이며 생성 권한을 자동추가하지 않는다.
CLI existing ELB role 직접 조회:
```bash
aws iam get-role --role-name AWSServiceRoleForElasticLoadBalancing --query 'Role.{Arn:Arn,Path:Path}' --output json --no-cli-pager
```
NoSuchEntity=조회시 role 미존재. AccessDenied=존재 미확인. 이를 구분한다.

Rollback(이번 추가 policy만 제거):
```bash
aws iam delete-role-policy --role-name FDS-ReadOnly-Audit --policy-name FDS-ROSA-Prereq-ReadOnly-v1 --no-cli-pager
```

검증: STATIC AST PASS / 실제 role policy 적용 및 ROSA 조회 사용자 실행 대기 / 독립 리뷰 PENDING /
Architecture Freeze HOLD / 유료 resource Create/Apply/Project Runtime NOT_RUN.
공식 근거: https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ROSAManageSubscription.html
