# 팀원 기본 세션의 서비스 전반 조회 확대 — 적용 후보

2026-10-06 KST · CODEX_ASSISTED · 책임 #35 · 독립 REVIEW=CONDITIONAL_APPROVED(JSON 범위) · AWS MUTATION=NOT_RUN

## 확정 요구와 현재 증적

사용자 이권욱의 10:17 요청은 역할 전환 없이 공통 그룹에 ReadOnlyAccess를 추가하는 것이다. 교육장 통제 root로 실행하며 root MFA는 변경하지 않는다. 팀원 MFA·서울 리전 통제는 유지한다. 사용자 제출 출력 기준 기존 FDS-Human-Direct-ReadOnly-v1의 put RC0/readback PASS, 기존 두 정책·3인 membership·관리형 정책 없음의 보존 PASS, gwonuk 기본 user 세션의 EC2 VPC/ELBv2 조회 PASS다. 하영·재환 기본 세션은 미확인이다. 실제 AWS 세션에 직접 접속해 확인한 결과가 아니다.

## 추가 구성

- 그룹: FDS-Human-Bootstrap. 지정 user는 321team-gwonuk / 321team-hayeoung / 321team-jaehwan.
- AWS 관리형 정책 arn:aws:iam::aws:policy/ReadOnlyAccess를 그룹에 추가한다.
- 고객 관리형 정책 FDS-Human-ReadOnly-Guard-v1을 별도 생성하고 먼저 그룹에 연결한다. 입력은 ../inputs/human-readonly-guard.candidate.json.
- 기존 inline 3개·기존 role/trust·membership은 변경하지 않는다. AWS 관리형 정책만 단독 연결하면 MFA와 리전 조건을 우회하는 Allow가 생기므로 단독 적용 금지다.
- guard에는 Allow가 없다. 신규 가입자가 자동으로 확대 조회를 받지 않도록 미지정 principal을 Deny한다. 이는 해당 그룹의 다른 권한에도 적용되는 명시적 Deny이며 후속 멤버 추가 시 정책 리뷰가 필요하다.
- MFA=false 또는 key 누락 시 기본 조회를 Deny한다. 암호/MFA 초기 설정·본인 메타데이터 조회 예외는 기존 자기관리 흐름을 위해 유지한다. MFA 없는 다른 user 조회는 별도 NotResource Deny로 차단한다. 장기 access key의 일반 사용은 MFA 없는 조회 경로가 아니다.
- regional API는 서울만 허용한다. IAM/STS/Marketplace 및 명시된 global endpoint 서비스는 지역 Deny 예외다. 이 예외는 권한을 부여하지 않는다. S3 bucket 목록/위치 조회는 global 예외이고 object 읽기는 서울 endpoint 제한을 유지한다. RequestedRegion은 요청 endpoint 통제이며 데이터 위치 자체를 보장하지 않는다.
- 모든 글로벌 서비스의 예외가 완전히 나열됐다고 주장하지 않는다. 추가 화면 거부는 정확한 action/endpoint를 확인해 최소 예외를 리뷰하며 서울 제한을 해제하지 않는다.
- ReadOnlyAccess에는 S3/DynamoDB 등의 데이터 읽기가 포함되므로 기존 좁은 조회보다 공개 범위가 넓다. ELB SLR 생성·Marketplace 구독·ROSA 구축은 이번에 추가하지 않는다.
- AWS 관리형 정책은 AWS가 자동 갱신한다. 적용 시 default version과 원본 document/hash를 저장하고, 향후 정책 변경은 권한 변경으로 점검한다. 고객 guard는 별도 고정한다.

## 적용 선행조건

governance/REVIEW_AUTHORITY_POLICY.md §2: 실행 시 소비되는 정책·설정은 코드 변경이다. §2는 Markdown의 새 실행 로직도 코드로 분류하며 미검토 코드의 우회 적용을 금지한다. 본 후보는 기존 e24c881의 독립 승인 범위에 포함되지 않는다. 새 policy/명령 exact SHA의 독립 리뷰와 #35 Lead 실행 판단을 확인한다. 보안 통제 코드는 Pre-check 예외가 아니다. 새 관리자 계정이나 root MFA 등록을 선행조건으로 추가하지 않는다.

## 교육장 root CloudShell: 조회·백업

환경: aws CLI/jq/Python3, 프로젝트 root, HOME 작업 경로. 다음은 AWS 읽기만 수행한다.

```bash
(
set -euo pipefail
umask 077
[ "$(aws sts get-caller-identity --query Arn --output text --no-cli-pager)" = 'arn:aws:iam::774055931866:root' ] || exit 1
d=$(mktemp -d "$HOME/fds-all-readonly.XXXXXX")
printf 'BACKUP_DIR=%s\n' "$d"
aws sts get-caller-identity --output json --no-cli-pager > "$d/identity.json"
aws iam get-group --group-name FDS-Human-Bootstrap --output json --no-cli-pager > "$d/group.json"
jq -e '([.Users[].UserName]|sort)==["321team-gwonuk","321team-hayeoung","321team-jaehwan"]' "$d/group.json" >/dev/null
aws iam list-group-policies --group-name FDS-Human-Bootstrap --output json --no-cli-pager > "$d/inline-list.json"
jq -e '(.PolicyNames|sort)==["FDS-Assume-ReadOnly-Audit-v1","FDS-Human-Direct-ReadOnly-v1","FDS-SelfService-Password-MFA"]' "$d/inline-list.json" >/dev/null
for p in FDS-Assume-ReadOnly-Audit-v1 FDS-Human-Direct-ReadOnly-v1 FDS-SelfService-Password-MFA; do
  aws iam get-group-policy --group-name FDS-Human-Bootstrap --policy-name "$p" --output json --no-cli-pager > "$d/$p.json"
done
aws iam list-attached-group-policies --group-name FDS-Human-Bootstrap --output json --no-cli-pager > "$d/attached.json"
aws iam list-policies --scope Local --output json --no-cli-pager > "$d/local-policies.json"
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess --output json --no-cli-pager > "$d/readonly-metadata.json"
v=$(jq -r '.Policy.DefaultVersionId' "$d/readonly-metadata.json")
aws iam get-policy-version --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess --version-id "$v" --query PolicyVersion.Document --output json --no-cli-pager > "$d/readonly-document.json"
(cd "$d" && sha256sum ./*.json > SHA256SUMS)
printf 'READONLY_POLICY_VERSION=%s\n' "$v"
jq '{AttachedPolicies}' "$d/attached.json"
jq '[.Policies[]|select(.PolicyName=="FDS-Human-ReadOnly-Guard-v1")|{Arn,DefaultVersionId}]' "$d/local-policies.json"
printf 'PRECHECK_CAPTURE=COMPLETE\nAWS_MUTATION=NOT_RUN\n'
)
```

정상 판정: PRECHECK_CAPTURE=COMPLETE, 기존 관리형 정책 없음, 새 guard 없음. 예상 외 policy 또는 기존 guard가 있으면 덮어쓰기/재생성하지 않고 내용을 대조한다. 실패하면 부분 백업으로 표시하고 중단한다. 백업은 별도 다운로드해 보관한다.

## 적용 전 IAM simulator 검증

읽어온 AWS 관리형 policy와 guard를 함께 simulate-custom-policy로 평가한다. guard 단독 평가는 Allow가 없으므로 implicitDeny가 정상이다. action을 실제 호출하는 생성/삭제 거부시험은 금지한다.

필수 matrix: 지정3인 각각 MFA=true/서울에서 ec2:DescribeVpcs, elasticloadbalancing:DescribeLoadBalancers, iam:ListRoles allowed; MFA=false 및 key 누락에서 EC2 조회 explicitDeny; 서울 외 EC2 조회 explicitDeny; 지정 외 principal explicitDeny; MFA 없는 본인 iam:GetUser는 기존 자기관리 허용 유지, 다른 user iam:GetUser는 explicitDeny; iam:CreateServiceLinkedRole은 Allow 없음. S3 global 목록/서울 object 읽기, Cost Explorer/Marketplace 및 본인 암호/MFA 초기 설정도 회귀 평가한다. simulator 결과는 실제 Console 성공이나 SCP/resource policy까지 검증한 결과가 아니다.

## 적용 순서 — 독립 리뷰·simulator·Lead 실행 판단 후

정책 파일과 백업 경로 및 reviewed SHA/hash를 확인하고 동시 IAM 변경이 없는 작업창에서 진행한다. 기존 파일과 JSON 의미가 다른 항목은 덮어쓰지 않는다.

1. 새 guard 없음이 성공한 list-policies 결과로 확인되면 create-policy로 FDS-Human-ReadOnly-Guard-v1 하나 생성한다. 응답 ARN은 arn:aws:iam::774055931866:policy/FDS-Human-ReadOnly-Guard-v1이어야 한다.
2. guard default version document를 get-policy-version으로 재조회해 후보와 JSON 대조한다. 일치 전 연결하지 않는다.
3. guard를 FDS-Human-Bootstrap에 attach-group-policy하고 성공한 list-attached-group-policies에서 연결을 확인한다.
4. ReadOnlyAccess를 같은 그룹에 attach-group-policy한다. 이미 동일 ARN이 연결돼 있으면 SKIP한다.
5. 그룹 관리형 정책은 정확히 guard+ReadOnlyAccess 두 개, 기존 inline3개와 각각의 document, membership은 백업과 같아야 한다. 다른 변경 발견 시 STOP.
6. 3인은 본인 MFA로 새 로그인하고 역할 전환 없이 STS user ARN 확인 → 서울 EC2/ELBv2/IAM 및 업무상 필요한 서비스 조회를 수행한다. 전체 서비스 완전 검증이라고 표시하지 않는다.

오류/timeout은 미적용으로 단정하지 않는다. attach/create 재실행 전에 현재 policy/document/attachment를 읽어 실제 변경 지점을 확인한다. guard 실패 시 ReadOnlyAccess를 연결하지 않는다. 일부 거부를 이유로 MFA 조건이나 리전 Deny를 삭제하지 않는다.

## 복구

이번 작업 전 두 신규 attachment가 없었고 현재 내용이 이번 후보와 일치하며 후속 변경 없음이 확인될 때만 수행한다. ReadOnlyAccess 연결을 먼저 해제하고 성공한 목록에서 부재 확인 후 guard 연결을 해제한다. 반대 순서는 광범위 조회의 MFA/리전 제한을 제거하므로 금지한다. 기존 inline3개는 유지한다. 새 고객 guard policy 객체는 연결 해제 후 남겨도 추가 권한을 주지 않으며, 삭제하려면 list-entities-for-policy로 다른 user/group/role 사용이 없음을 확인한다. 기존 정책 객체를 삭제하거나 기존 정책을 덮어써 복구하지 않는다. 이후 기존 사용자 조회와 정책/membership 보존을 확인한다. 일부 복구 실패는 RECOVERY_PENDING이다.

## 검증 범위

정적 JSON·Deny/조건·크기 검사와 사용자 제출 IAM simulator10개 케이스 PASS를 확인했다. 신규 JSON은 review5423110520의 조건부 독립 APPROVED이며 새 실행 명령은 별도 확인 대상이다. AWS 적용/신규 확대 조회 Runtime/MERGE는 미수행이다. 전체 서비스/자기관리API의 완전 검증이나 Assistant의 AWS 직접 검증으로 표시하지 않는다.

공식 근거:
- https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReadOnlyAccess.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-requested-region.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.html


## 2026-10-06 시뮬레이션 결과 — 사용자 실행 출력 수신

사용자 제출 결과 기준이다. Assistant가 AWS에 직접 접속하거나 원본 result JSON을 수신해 독립 검증한 것으로 표시하지 않는다. 수신 기준 시각: 2026-10-06 11:09 KST.

- 사전 백업: /home/cloudshell-user/fds-all-readonly.Yn8Upt.tar.gz, SHA256 5387959256f7ad791f6c6fe8c5edc0492a18d8e92e958a85735df768749cd127. 그룹 관리형 attachment [] 및 Local guard 미존재, PRECHECK_CAPTURE=COMPLETE, AWS_MUTATION=NOT_RUN.
- 실제 계정에서 조회한 ReadOnlyAccess default version=v190. 공식 웹페이지의 이전 v188 표기를 실계정 현황으로 사용하지 않는다.
- 최초 요청은 policyInputList ValidationError로 평가 전에 중단했다. 원문 ReadOnlyAccess 146475 characters가 131072 한도를 초과한 것이 진단 출력으로 확인됐다. 허용 외 문자는 0. json.loads 후 ensure_ascii=True/separators=(',',':')로 직렬화하면 94907 characters이며 JSON 내용 동등성을 확인했다. 정책 JSON과 Action/Resource/Condition은 변경하지 않았다. 이 처리는 시뮬레이션 입력 표현의 보정이다.
- 최초 요청 보존: simulation-awjazmim/01-input.json. 정규화 파일: simulation-awjazmim/01-input.compact.json.
- 최종 결과 경로: /home/cloudshell-user/fds-all-readonly.Yn8Upt/simulation-compact-l53akbrf. 각 요청/원본 결과 및 SHA256SUMS는 사용자 실행 코드가 해당 경로에 생성하며 실제 파일 재수신/재해시는 별도다.
- SIMULATOR_MATRIX=PASS CASES=10 READONLY_VERSION=v190; AWS_MUTATION=NOT_RUN.

| 케이스 | 확인된 시뮬레이션 판정 |
|---|---|
| 01–03 | 지정 3인 각각 MFA=true/서울: EC2 DescribeVpcs, ELB DescribeLoadBalancers, IAM ListRoles allowed |
| 04–05 | MFA=false 및 MFA key 누락: EC2 조회 explicitDeny |
| 06 | 서울 외 EC2 조회 explicitDeny |
| 07 | 지정 외 principal EC2 조회 explicitDeny |
| 08–09 | MFA 없는 본인 GetUser allowed / 다른 user GetUser explicitDeny |
| 10 | ELB CreateServiceLinkedRole implicitDeny |

이 10개 케이스는 위 선택 API/조건 범위의 성공이며 모든 서비스, 모든 자기관리 API 또는 전체 simulator 권고 matrix를 완료했다는 뜻이 아니다. CloudShell/MFA 등록·해제·AssumeRole/S3 객체·비용/Marketplace 등 추가 회귀 영역은 아직 위 출력에서 확인되지 않았다. AWS 원문 v190 및 기존 그룹 정책과 guard를 합산한 후보 평가이며 실제 신규 policy 연결, 3인 확대 조회 Runtime, SCP/permission boundary/resource policy 실효평가, 독립 REVIEW/MERGE는 미수행이다.

후속: 새 정책 범위는 이하영(hayeounglee)의 기존 지정 독립 reviewer 경로로 검토하고 #35 Lead 실행 판단 후 교육장 root에서 guard 생성/대조/연결→ReadOnlyAccess 연결→기존 설정 보존→사용자 기본 세션 검증을 진행한다. 기존 e24c881 승인 범위를 본 확대 정책 승인으로 승계하지 않는다. root MFA나 별도 관리자 생성은 선행조건으로 추가하지 않는다.


## 2026-10-06 2차 독립 리뷰 반영 — 실행 전 조건 분리

신규 정책 JSON의 독립 승인: [review5423110520](https://github.com/321Team/fds-project-baseline/pull/137#pullrequestreview-5423110520), 대상 b573e4c82eddc89a8cc8aa12a74ba8409e31bd4b. 조건부 APPROVED이며 계정 데이터 읽기 노출 확인/수용, guard 직후 회귀, 실행 명령 고정이 선행한다. 본 섹션의 새 실행 명령은 후보이며 JSON 승인에 포함됐다고 표시하지 않는다. 새 명령 diff 확인과 #35 Lead 실행 판단 전 실행하지 않는다. 기존 independent review를 새 명령 승인으로 재사용하지 않는다.

교육장 root 경로는 사용자가 이미 명시적으로 지정했고 root MFA는 교육장 Owner 통제 사항이다. 별도 관리자 생성이나 root MFA 등록을 다시 요구하지 않는다. 이 기존 실행 경로 지시는 유지하되 계정 Owner의 MFA 상태/승인이나 미확인 데이터 자산의 위험 수용을 새로 만들어 기록하지 않는다.

### 조건 1 — 실제 v190 데이터 읽기 범위와 계정 자산

CloudShell 백업 readonly-document.json의 Allow action pattern을 실제 데이터 읽기 action과 대조한다. Action/Resource/Condition을 함께 기록하고 패턴 일치를 AWS 유효권한 PASS로 표시하지 않는다. S3 list-buckets 및 서울 SSM describe-parameters는 이름/유형 메타데이터만 수집한다. S3 객체·tfstate·로그·Parameter 값·Secret 값·Lambda 소스를 읽지 않는다.

bucket/parameter가 있으면 목록만으로 내용을 판단하거나 안전하다고 단정하지 않는다. 계정 Owner/프로젝트 책임자가 tfstate·증적·자격증명 저장 용도를 확인해야 한다. 이름이나 샘플 key의 비일치로 민감정보 부재를 판정하지 않는다. 데이터 읽기 노출 수용은 실제 조사 결과를 제시한 뒤 #35/PR에 기록한다. 사용자의 기존 ReadOnlyAccess 추가 지시를 아직 보지 못한 민감 자산 전부의 수용으로 확대하지 않는다. 보호 Deny를 추가하면 새로운 guard SHA의 독립 리뷰가 필요하며 ViewOnlyAccess 대체도 사용자 요구 변경으로 구분한다.

### 단계 A — guard만 생성·대조·연결하는 exact 후보

선행: 조건1 결과와 데이터 범위 판단, 본 명령의 diff 검토 및 #35 Lead 실행 판단, 백업 외부 보관, 코드 hash 일치, 동시 IAM 작업 없음. 아래 블록은 ReadOnlyAccess를 연결하지 않는다. 본 코드의 shell syntax/API/mock/runtime 검증은 아직 미실행이며 실제 적용 완료로 표시하지 않는다.

이미 생성돼 있는 guard는 동일 JSON이면 재생성하지 않고 현재 version을 대조한다. 다른 policy, path, attachment, membership 또는 기존 inline drift는 STOP한다.

~~~bash
(
set -euo pipefail
umask 077
cd "$HOME"
d="$HOME/fds-all-readonly.Yn8Upt"
g="FDS-Human-Bootstrap"
ga="arn:aws:iam::774055931866:policy/FDS-Human-ReadOnly-Guard-v1"
[ "$(aws sts get-caller-identity --query Arn --output text --no-cli-pager)" = "arn:aws:iam::774055931866:root" ] || exit 1
(cd "$d" && sha256sum -c SHA256SUMS)
printf '%s\n' 'c04a04948e48ecfa11f286e8b261ac2d4589dc934159d66ac2a9cf139bc1a084  human-readonly-guard.candidate.json' | sha256sum -c -
t=$(mktemp -d "$d/guard-apply.XXXXXX")
printf 'APPLY_DIR=%s\n' "$t"
aws iam get-group --group-name "$g" --output json --no-cli-pager > "$t/group-before.json"
jq -e '([.Users[].Arn]|sort)==["arn:aws:iam::774055931866:user/321team-gwonuk","arn:aws:iam::774055931866:user/321team-hayeoung","arn:aws:iam::774055931866:user/321team-jaehwan"]' "$t/group-before.json" >/dev/null
aws iam list-group-policies --group-name "$g" --output json --no-cli-pager > "$t/inline-before.json"
diff -u <(jq -S '.PolicyNames|sort' "$d/inline-list.json") <(jq -S '.PolicyNames|sort' "$t/inline-before.json")
for p in FDS-Assume-ReadOnly-Audit-v1 FDS-Human-Direct-ReadOnly-v1 FDS-SelfService-Password-MFA; do
  aws iam get-group-policy --group-name "$g" --policy-name "$p" --output json --no-cli-pager > "$t/$p.before.json"
  diff -u <(jq -S '.PolicyDocument' "$d/$p.json") <(jq -S '.PolicyDocument' "$t/$p.before.json")
done
aws iam list-attached-group-policies --group-name "$g" --output json --no-cli-pager > "$t/attached-before.json"
jq -e --arg ga "$ga" '(.AttachedPolicies|length)==0 or ((.AttachedPolicies|length)==1 and .AttachedPolicies[0].PolicyArn==$ga)' "$t/attached-before.json" >/dev/null
aws iam list-policies --scope Local --output json --no-cli-pager > "$t/local-before.json"
matches=$(jq '[.Policies[]|select((.PolicyName|ascii_downcase)=="fds-human-readonly-guard-v1")]|length' "$t/local-before.json")
if [ "$matches" = 0 ]; then
  aws iam create-policy --policy-name FDS-Human-ReadOnly-Guard-v1 --path / --policy-document "file://$HOME/human-readonly-guard.candidate.json" --output json --no-cli-pager > "$t/create-result.json"
  jq -e --arg ga "$ga" '.Policy.Arn==$ga' "$t/create-result.json" >/dev/null
else
  jq -e --arg ga "$ga" '[.Policies[]|select((.PolicyName|ascii_downcase)=="fds-human-readonly-guard-v1")]|length==1 and .[0].Arn==$ga' "$t/local-before.json" >/dev/null
fi
aws iam get-policy --policy-arn "$ga" --output json --no-cli-pager > "$t/guard-metadata.json"
v=$(jq -r '.Policy.DefaultVersionId' "$t/guard-metadata.json")
aws iam get-policy-version --policy-arn "$ga" --version-id "$v" --query PolicyVersion.Document --output json --no-cli-pager > "$t/guard-readback.json"
diff -u <(jq -S . "$HOME/human-readonly-guard.candidate.json") <(jq -S . "$t/guard-readback.json")
if ! jq -e --arg ga "$ga" 'any(.AttachedPolicies[]; .PolicyArn==$ga)' "$t/attached-before.json" >/dev/null; then
  aws iam attach-group-policy --group-name "$g" --policy-arn "$ga" --no-cli-pager
fi
aws iam list-attached-group-policies --group-name "$g" --output json --no-cli-pager > "$t/attached-after.json"
jq -e --arg ga "$ga" '(.AttachedPolicies|length)==1 and .AttachedPolicies[0].PolicyArn==$ga' "$t/attached-after.json" >/dev/null
printf 'GUARD_ONLY_ATTACHED=PASS\nREADONLY_ATTACHMENT=NOT_RUN\n'
)
~~~

create/attach timeout/오류는 변경 여부 미확인이다. 중단 후 현재 policy/version/attachment를 조회하고 재실행 또는 복구를 판단한다. 마지막 출력이 없다고 무조건 미생성으로 판단하지 않는다. guard가 불일치하면 update-policy-version/덮어쓰기로 고치지 않는다. 정책 대조 방식은 배열 순서 동일을 요구하는 보수적 jq 대조이며 의미 동등의 모든 표현을 수용하는 검증기는 아니다.

### 조건 2 — guard만 연결한 상태의 3인 회귀 barrier

ReadOnlyAccess 연결 전에 3인 각 본인 MFA 새 로그인으로 다음을 확인하고 user ARN·시각·RC/화면 결과를 남긴다. 본인 역할 전환은 AWS Console Switch Role 기능으로 기존 FDS-ReadOnly-Audit에 전환하고 assumed-role ARN·서울 VPC 조회를 확인한다. CLI에 장기 키를 만들거나 OTP를 로그에 입력하지 않는다. 이 역할 trust 경로는 외부 role 세션이며 group Deny가 role에 승계됐다고 가정하지 않는다.

- 기본 MFA user 세션: STS user ARN, 서울 CloudShell 사용, VPC 조회.
- 본인 정보 조회: iam get-user, get-account-password-policy, list-mfa-devices --user-name 본인 user, list-access-keys --user-name 본인 user.
- role 전환: 기존 MFA 로그인 세션으로 Switch Role 성공 및 role 세션 STS/VPC 조회.
- 실제 비밀번호 변경·MFA 재등록/해제는 회귀시험을 위해 수행하지 않는다. 해당 변경 권한은 기존 3정책+guard를 합산한 simulator로 본인 user/MFA resource에 대해 확인하며 실패 시 원래 정책의 기저 문제와 신규 guard 회귀를 분리한다.

3인 중 실패/미확인 시 READONLY_ATTACHMENT=HOLD. 본인 정보 조회 일부가 기존에도 실패했으면 신규 guard로 발생한 회귀인지 이전3정책과 guard 추가 결과를 비교하고 Lead가 판단한다. password policy 자체가 없다는 NoSuchEntity는 조회 권한 거부와 구분한다.

### 단계 B — 3인 회귀 PASS 후 ReadOnlyAccess만 연결하는 exact 후보

선행: 단계A 일치/완료, 조건1 데이터 범위 수용 또는 보호 결정, 조건2 세 사람 기록 PASS, 본 명령 diff 검토 및 #35 Lead 실행 판단. 아래 명령은 조건2를 자동 증명하지 않으므로 실행자는 PR/#35의 실제 증적을 대조한다.

~~~bash
(
set -euo pipefail
umask 077
d="$HOME/fds-all-readonly.Yn8Upt"
g="FDS-Human-Bootstrap"
ga="arn:aws:iam::774055931866:policy/FDS-Human-ReadOnly-Guard-v1"
ra="arn:aws:iam::aws:policy/ReadOnlyAccess"
[ "$(aws sts get-caller-identity --query Arn --output text --no-cli-pager)" = "arn:aws:iam::774055931866:root" ] || exit 1
t=$(mktemp -d "$d/readonly-attach.XXXXXX")
printf 'APPLY_DIR=%s\n' "$t"
aws iam get-policy --policy-arn "$ra" --output json --no-cli-pager > "$t/readonly-metadata.json"
jq -e '.Policy.DefaultVersionId=="v190"' "$t/readonly-metadata.json" >/dev/null
aws iam get-policy-version --policy-arn "$ra" --version-id v190 --query PolicyVersion.Document --output json --no-cli-pager > "$t/readonly-document.json"
diff -u <(jq -S . "$d/readonly-document.json") <(jq -S . "$t/readonly-document.json")
aws iam get-policy --policy-arn "$ga" --output json --no-cli-pager > "$t/guard-metadata.json"
v=$(jq -r '.Policy.DefaultVersionId' "$t/guard-metadata.json")
aws iam get-policy-version --policy-arn "$ga" --version-id "$v" --query PolicyVersion.Document --output json --no-cli-pager > "$t/guard-readback.json"
printf '%s\n' 'c04a04948e48ecfa11f286e8b261ac2d4589dc934159d66ac2a9cf139bc1a084  human-readonly-guard.candidate.json' | (cd "$HOME" && sha256sum -c -)
diff -u <(jq -S . "$HOME/human-readonly-guard.candidate.json") <(jq -S . "$t/guard-readback.json")
aws iam get-group --group-name "$g" --output json --no-cli-pager > "$t/group-before.json"
jq -e '([.Users[].Arn]|sort)==["arn:aws:iam::774055931866:user/321team-gwonuk","arn:aws:iam::774055931866:user/321team-hayeoung","arn:aws:iam::774055931866:user/321team-jaehwan"]' "$t/group-before.json" >/dev/null
aws iam list-group-policies --group-name "$g" --output json --no-cli-pager > "$t/inline-before.json"
diff -u <(jq -S '.PolicyNames|sort' "$d/inline-list.json") <(jq -S '.PolicyNames|sort' "$t/inline-before.json")
for p in FDS-Assume-ReadOnly-Audit-v1 FDS-Human-Direct-ReadOnly-v1 FDS-SelfService-Password-MFA; do
  aws iam get-group-policy --group-name "$g" --policy-name "$p" --output json --no-cli-pager > "$t/$p.before.json"
  diff -u <(jq -S '.PolicyDocument' "$d/$p.json") <(jq -S '.PolicyDocument' "$t/$p.before.json")
done
aws iam list-attached-group-policies --group-name "$g" --output json --no-cli-pager > "$t/attached-before.json"
jq -e --arg ga "$ga" --arg ra "$ra" '([.AttachedPolicies[].PolicyArn]|sort)==[$ga] or ([.AttachedPolicies[].PolicyArn]|sort)==([$ga,$ra]|sort)' "$t/attached-before.json" >/dev/null
if ! jq -e --arg ra "$ra" 'any(.AttachedPolicies[]; .PolicyArn==$ra)' "$t/attached-before.json" >/dev/null; then
  aws iam attach-group-policy --group-name "$g" --policy-arn "$ra" --no-cli-pager
fi
aws iam list-attached-group-policies --group-name "$g" --output json --no-cli-pager > "$t/attached-after.json"
jq -e --arg ga "$ga" --arg ra "$ra" '([.AttachedPolicies[].PolicyArn]|sort)==([$ga,$ra]|sort)' "$t/attached-after.json" >/dev/null
aws iam get-group --group-name "$g" --output json --no-cli-pager > "$t/group-after.json"
diff -u <(jq -S '[.Users[].Arn]|sort' "$t/group-before.json") <(jq -S '[.Users[].Arn]|sort' "$t/group-after.json")
aws iam list-group-policies --group-name "$g" --output json --no-cli-pager > "$t/inline-after.json"
diff -u <(jq -S '.PolicyNames|sort' "$d/inline-list.json") <(jq -S '.PolicyNames|sort' "$t/inline-after.json")
for p in FDS-Assume-ReadOnly-Audit-v1 FDS-Human-Direct-ReadOnly-v1 FDS-SelfService-Password-MFA; do
  aws iam get-group-policy --group-name "$g" --policy-name "$p" --output json --no-cli-pager > "$t/$p.after.json"
  diff -u <(jq -S '.PolicyDocument' "$d/$p.json") <(jq -S '.PolicyDocument' "$t/$p.after.json")
done
(cd "$t" && sha256sum ./*.json > SHA256SUMS)
printf 'READONLY_ATTACHMENT=PASS\nNEW_USER_RUNTIME=NOT_TESTED\n'
)
~~~

정책 version/본문 drift는 STOP이며 새로운 현재 default version을 임의 수용하지 않는다. 원문 v190 SHA256은 위 원문 readonly-document.json의 SHA256SUMS에 보관하며 주기적 default version/document 변경 점검 항목으로 유지한다. 콘솔/CloudShell 기본 리전은 서울로 지정한다. 글로벌 endpoint 예외가 없는 API의 거부는 exact action/endpoint를 확인해 최소 예외를 별도 변경·리뷰한다.

### 복구 exact 후보

이번 작업 전 attachment가 없었고 이번 작업에서 생성/연결한 것이 확인되고 최신 readback이 후보와 같고 다른 변경이 없을 때만 실행한다. 아래는 고객 policy 객체를 삭제하지 않는다. 정상 순서는 ReadOnlyAccess 해제 확인 후 guard 해제다. 과거부터 존재했거나 후속 작업이 있으면 이 일괄 복구를 사용하지 않는다.

~~~bash
(
set -euo pipefail
umask 077
[ "$(aws sts get-caller-identity --query Arn --output text --no-cli-pager)" = "arn:aws:iam::774055931866:root" ] || exit 1
g="FDS-Human-Bootstrap"
ga="arn:aws:iam::774055931866:policy/FDS-Human-ReadOnly-Guard-v1"
ra="arn:aws:iam::aws:policy/ReadOnlyAccess"
t=$(mktemp -d "$HOME/fds-readonly-recovery.XXXXXX")
aws iam list-attached-group-policies --group-name "$g" --output json --no-cli-pager > "$t/before.json"
if jq -e --arg ra "$ra" 'any(.AttachedPolicies[]; .PolicyArn==$ra)' "$t/before.json" >/dev/null; then
  aws iam detach-group-policy --group-name "$g" --policy-arn "$ra" --no-cli-pager
fi
aws iam list-attached-group-policies --group-name "$g" --output json --no-cli-pager > "$t/after-readonly.json"
jq -e --arg ra "$ra" 'all(.AttachedPolicies[]; .PolicyArn!=$ra)' "$t/after-readonly.json" >/dev/null
if jq -e --arg ga "$ga" 'any(.AttachedPolicies[]; .PolicyArn==$ga)' "$t/after-readonly.json" >/dev/null; then
  aws iam detach-group-policy --group-name "$g" --policy-arn "$ga" --no-cli-pager
fi
aws iam list-attached-group-policies --group-name "$g" --output json --no-cli-pager > "$t/after-guard.json"
jq -e --arg ga "$ga" --arg ra "$ra" 'all(.AttachedPolicies[]; .PolicyArn!=$ga and .PolicyArn!=$ra)' "$t/after-guard.json" >/dev/null
printf 'NEW_ATTACHMENTS_REMOVED=PASS\nRECOVERY_DIR=%s\n' "$t"
)
~~~

기존 inline3개·user membership·role/trust는 기존 백업과 조회 대조하여 보존 여부를 별도로 확인한다. 새 attachment 제거만으로 전체 복구 완료를 선언하지 않는다. AWS 오류가 발생하면 RECOVERY_PENDING으로 표시하고 확대 삭제나 guard 우선 해제를 하지 않는다.


### 조건1 수집 exact 명령 — AWS 조회 전용

다음은 v190 Action 패턴/조건 원문 및 전체 소유 S3 bucket 목록·서울 SSM parameter 이름/유형을 수집한다. 성공한 목록의 0건은 해당 수집범위의 부재이며 다른 서비스/리전/계정의 민감 자산 부재까지 증명하지 않는다. meta 자산이 있으면 목적·내용 분류가 필요하다. 파일 이름·Parameter 이름은 비공개 자료로 보관한다.

~~~bash
(
set -euo pipefail
umask 077
[ "$(aws sts get-caller-identity --query Arn --output text --no-cli-pager)" = "arn:aws:iam::774055931866:root" ] || exit 1
d="$HOME/fds-all-readonly.Yn8Upt"
t=$(mktemp -d "$d/data-scope.XXXXXX")
printf 'CAPTURE_DIR=%s\n' "$t"
aws iam get-group --group-name FDS-Human-Bootstrap --output json --no-cli-pager > "$t/group.json"
jq '[.Users[]|{UserName,Arn}]' "$t/group.json"
jq -e '([.Users[].Arn]|sort)==["arn:aws:iam::774055931866:user/321team-gwonuk","arn:aws:iam::774055931866:user/321team-hayeoung","arn:aws:iam::774055931866:user/321team-jaehwan"]' "$t/group.json" >/dev/null
aws iam get-policy --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess --output json --no-cli-pager > "$t/readonly-metadata.json"
jq -e '.Policy.DefaultVersionId=="v190"' "$t/readonly-metadata.json" >/dev/null
aws iam get-policy-version --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess --version-id v190 --query PolicyVersion.Document --output json --no-cli-pager > "$t/readonly-document.json"
diff -u <(jq -S . "$d/readonly-document.json") <(jq -S . "$t/readonly-document.json")
python3 - "$t/readonly-document.json" <<'PY'
import fnmatch, hashlib, json, pathlib, sys
p=pathlib.Path(sys.argv[1])
doc=json.loads(p.read_text())
targets=["s3:GetObject","s3:GetObjectVersion","ssm:GetParameter","ssm:GetParameters","ssm:GetParametersByPath","lambda:GetFunction","dynamodb:GetItem","dynamodb:BatchGetItem","dynamodb:Query","dynamodb:Scan","secretsmanager:GetSecretValue","kms:Decrypt","logs:GetLogEvents","logs:FilterLogEvents"]
rows=[]
for action in targets:
    for s in doc["Statement"]:
        if s.get("Effect")!="Allow":
            continue
        patterns=s.get("Action",[])
        patterns=[patterns] if isinstance(patterns,str) else patterns
        matches=[x for x in patterns if fnmatch.fnmatchcase(action.lower(),x.lower())]
        if matches:
            rows.append({"Action":action,"MatchedAllowPatterns":matches,"Resource":s.get("Resource"),"Condition":s.get("Condition")})
print(json.dumps({"READONLY_V190_DOCUMENT_SHA256":hashlib.sha256(p.read_bytes()).hexdigest(),"DATA_READ_PATTERN_MATCHES":rows,"EFFECTIVE_PERMISSION_TEST":"NOT_RUN"},indent=2))
PY
aws s3api list-buckets --region ap-northeast-2 --output json --no-cli-pager > "$t/s3-buckets.json"
aws ssm describe-parameters --region ap-northeast-2 --query 'Parameters[].{Name:Name,Type:Type,Tier:Tier}' --output json --no-cli-pager > "$t/ssm-parameters.json"
jq '{BucketCount:(.Buckets|length),BucketNames:[.Buckets[].Name]}' "$t/s3-buckets.json"
jq '{SeoulParameterCount:length,Parameters:.}' "$t/ssm-parameters.json"
(cd "$t" && sha256sum ./*.json > SHA256SUMS)
printf 'DATA_SCOPE_CAPTURE=COMPLETE\nPARAMETER_VALUES=NOT_READ\nS3_OBJECT_CONTENT=NOT_READ\nAWS_MUTATION=NOT_RUN\n'
)
~~~
