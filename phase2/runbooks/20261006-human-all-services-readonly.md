# 팀원 기본 세션의 서비스 전반 조회 확대 — 적용 후보

2026-10-06 KST · CODEX_ASSISTED · 책임 #35 · 독립 REVIEW=PENDING · AWS MUTATION=NOT_RUN

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

정적 JSON·Deny/조건·크기 검사만 수행한다. IAM simulator/AWS 적용/신규 확대 조회 Runtime/독립 REVIEW/MERGE는 아직 미수행이다. 기존 정책의 사용자 제출 Runtime 결과와 신규 확대 후보의 미실행을 구분한다.

공식 근거:
- https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReadOnlyAccess.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_aws_deny-requested-region.html
- https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies-choosing-managed-or-inline.html
