# 3인 IAM 기본 세션 조회 권한 — 적용 후보
2026-10-05 KST · CODEX_ASSISTED · e24c881 IAM 범위 독립 APPROVED / AWS NOT RUN

## 10/5 저녁 독립 리뷰 후속 — IAM 쓰기 실행 주체
e24c8813c9b16868e6efbc56889eae2d5e882509의 IAM/플랫폼 범위 [독립 승인5412755619](https://github.com/321Team/fds-project-baseline/pull/137#pullrequestreview-5412755619)을 확인했다. 실행 허가·Freeze·병합과 구분한다.
리뷰 권고를 반영한 실행 조건: #35 Lead가 **MFA 인증이 확인된 승인 관리자 IAM principal**과 필요한 최소권한을 지정한다. root를 최초 설정에 사용해야 한다면 계정 Owner가 MFA를 설정하고 MFA 인증 세션을 확인한 뒤 수행한다. root MFA=0인 현재 기록만으로 IAM 쓰기를 진행하지 않는다. root MFA는 외부 Owner 통제이므로 프로젝트가 임의 등록/복구/재설정하지 않는다.
계정 MFA 등록 수치와 실제 실행 세션의 MFA 인증은 구분한다. STS ARN만으로 MFA 여부를 증명하지 않는다. 승인 관리자 principal의 현재 존재/권한/세션은 아직 미확인이다. 관리자 경로가 없으면 Owner에 연결하며 공용 조회 역할에 쓰기를 붙여 우회하지 않는다.
아래 과거 root 실행 후보는 이 조건이 우선한다. 후보 IAM JSON과 실행 명령 자체는 이번에 변경하지 않았다. 해당 범위의 기존 승인은 e24c881 기준이며 새 문서 보완 및 수집기 코드 수정은 변경 범위를 구분해 검토한다.

## 목적과 변경
사용자 09:53 기본 로그인 세션 조회 요구 및 09:54 착수 지시에 따른 후보다. 현재는 FDS-ReadOnly-Audit로 전환해야 조회할 수 있다. FDS-Human-Bootstrap에 새 inline policy `FDS-Human-Direct-ReadOnly-v1` 하나를 추가한다.
입력: [정책 JSON](../inputs/human-direct-readonly.candidate.json). 10/5 사용자가 제출한 기존 조회 역할의 두 정책과 동일한 Action/Resource 범위에 모든 statement마다 MFA=true 및 정확한 3인 PrincipalArn 조건을 추가한다. 서울 제한은 기존 regional statement에 유지하고 IAM/Marketplace global 조회에는 새 지역 제한을 붙이지 않는다.

대상 3인: 321team-gwonuk / 321team-hayeoung / 321team-jaehwan. 그룹 신규 가입자가 자동으로 이 조회 허용을 받지 않도록 principal을 제한한다. 사람이 아닌 role session에 대한 grant가 아니다.
CloudShell 환경/세션 생성 API는 도구 사용에 필요한 예외이며 프로젝트 리소스 생성 권한이 아니다. 정책 이름의 ReadOnly는 프로젝트 자원 조회 범위를 뜻한다.
기존 password/MFA self-service, AssumeRole 허용, 조회 역할과 trust는 유지한다. 사용자 직접 정책, 장기 키, ELB role 생성, operator 권한, Marketplace Subscribe, Secret/S3 object/SSM parameter 조회는 추가하지 않는다.
새 Allow는 MFA 조건이 없거나 false일 때 적용되지 않는다. 다른 정책의 권한을 전역 차단하는 Deny는 추가하지 않으므로 모든 권한에 대한 MFA 강제 정책이라고 해석하지 않는다.

## 실행 전 준비 — 지금은 리뷰 후보
#35 Lead 이하영의 실행 판단과 적용 코드/정책 exact SHA 독립 리뷰가 선행한다. 근거: REVIEW_AUTHORITY_POLICY §2–4. 권욱 작성 후보를 자기 승인하지 않는다. P1 인수/Freeze/유료 Apply 승인과 별개다.
위 실행 조건을 충족하는 MFA 인증된 승인 관리자 CloudShell(프로젝트 계정)에서 작업한다. 비공개 저장소의 검토된 SHA에서 정책 JSON을 내려받아 CloudShell에 `human-direct-readonly.candidate.json`으로 업로드한다. 원격 코드를 pipe 실행하지 않는다.

1. `aws sts get-caller-identity`로 프로젝트 account 및 Lead가 지정한 exact principal 확인. 다르면 STOP. 별도로 해당 세션 MFA 인증 및 필요한 IAM 권한을 확인하며 ARN만으로 MFA 사용을 판정하지 않는다.
2. 기존 조회 결과를 재요청하지 않는다. 실제 적용 직전에는 drift 확인 목적으로 `aws iam get-group --group-name FDS-Human-Bootstrap`의 정확한 3인 membership 및 각자의 MFA 등록을 확인한다.
3. `aws iam list-group-policies --group-name FDS-Human-Bootstrap`, `aws iam list-attached-group-policies --group-name FDS-Human-Bootstrap` 확인. 알려진 기존 inline은 FDS-SelfService-Password-MFA와 FDS-Assume-ReadOnly-Audit-v1이다. 예상 밖 정책/사용자 또는 불명확한 오류가 있으면 STOP.
4. 새 policy가 이미 있으면 `get-group-policy`로 조회하여 후보와 비교한다. 동일하면 쓰기 없이 SKIP, 다르면 STOP. 덮어쓰기하지 않는다. 이름 미존재 판정은 성공한 전체 list 결과로 한다.
5. 아래 백업은 신규 작업 디렉터리에 실행한다. 모든 명령 성공 후 디렉터리의 JSON을 승인된 별도 보관 위치에 복사하고 size/hash를 대조한다. 외부 보관 완료 전 쓰기를 시작하지 않는다.

```bash
umask 077
capture_dir=$(mktemp -d "$HOME/fds-direct-readonly.XXXXXX") || exit 1
aws iam get-group --group-name FDS-Human-Bootstrap --output json --no-cli-pager > "$capture_dir/group.json" &&
aws iam list-group-policies --group-name FDS-Human-Bootstrap --output json --no-cli-pager > "$capture_dir/inline-list.json" &&
aws iam list-attached-group-policies --group-name FDS-Human-Bootstrap --output json --no-cli-pager > "$capture_dir/attached-list.json" &&
aws iam get-group-policy --group-name FDS-Human-Bootstrap --policy-name FDS-SelfService-Password-MFA --output json --no-cli-pager > "$capture_dir/self-service.json" &&
aws iam get-group-policy --group-name FDS-Human-Bootstrap --policy-name FDS-Assume-ReadOnly-Audit-v1 --output json --no-cli-pager > "$capture_dir/assume.json" &&
cp -- human-direct-readonly.candidate.json "$capture_dir/candidate.json" &&
sha256sum "$capture_dir"/*.json
```

출력 RC 실패 시 부분 백업이므로 STOP. 디렉터리를 보존하고 실패 원인만 처리한다. `capture_dir`는 같은 CloudShell 세션에서 유지한다. 세션이 바뀌면 실제 디렉터리를 다시 지정한다. 두 기존 정책과 추가 후보의 공백 제외 합계가 group inline quota 5120 characters 이내인지 확인하며, 초과하면 임의 policy 삭제 대신 별도 설계로 전환한다.

## 적용 — 선행 조건 및 백업 확인 후 한 줄
아래 명령은 IAM 쓰기이며 검토된 파일과 백업의 candidate가 일치할 때만 사용한다. 실행자가 사전 확인을 수행하는 절차이며 자동 preflight/rollback 스크립트가 아니다. 동시 IAM 작업이 없도록 Lead 작업창에서 수행한다.

```bash
python3 check-human-direct-readonly.py --policy human-direct-readonly.candidate.json && cmp -- human-direct-readonly.candidate.json "$capture_dir/candidate.json" && aws iam put-group-policy --group-name FDS-Human-Bootstrap --policy-name FDS-Human-Direct-ReadOnly-v1 --policy-document "file://$capture_dir/candidate.json" --no-cli-pager
```

RC를 즉시 기록한다. 타임아웃/오류도 미적용으로 단정하지 않고 아래 readback을 수행한다. 재실행으로 덮어쓰지 않는다.

## 적용 후 확인
```bash
aws iam get-group-policy --group-name FDS-Human-Bootstrap --policy-name FDS-Human-Direct-ReadOnly-v1 --query PolicyDocument --output json --no-cli-pager > "$capture_dir/applied.json"
```

RC=0인 경우 JSON을 파싱해 candidate와 Statement/Action/Resource/Condition을 비교한다. 배열 순서/단일 문자열 표현 차이만으로 권한 차이라고 단정하지 않는다. 기존 두 정책 및 membership도 백업과 비교한다. 신규 정책 이외 변경 발견 시 STOP, 원인 확인 없이 기존 정책을 복원하지 않는다.
설정 readback 일치는 본인 사용 성공이 아니다. 각 사용자는 MFA로 새 로그인하고 **역할 전환 없이** 서울 CloudShell에서 아래 한 줄을 실행한다.
```bash
aws sts get-caller-identity --query Arn --output text --no-cli-pager; printf 'IDENTITY_RC=%s\n' "$?"; aws ec2 describe-vpcs --region ap-northeast-2 --query 'Vpcs[].{VpcId:VpcId,Cidr:CidrBlock}' --output json --no-cli-pager; printf 'VPC_READ_RC=%s\n' "$?"
```
caller는 본인의 IAM user ARN이어야 하며 assumed-role이면 기본 세션 검증이 아니다. MFA 없는 session/다른 region/대상 외 principal은 이 새 정책에서 Allow되지 않는지 정적으로 검토한다. 생성/삭제 API 호출을 거부 시험으로 사용하지 않는다.
CloudShell 및 후속 API의 실제 MFA context 전달/유효 권한은 본인 실행으로 확인한다. 실패하면 exact action/session/region/error를 기록하고 MFA 조건 제거 또는 ReadOnlyAccess/Administrator 부여로 우회하지 않는다. 기존 조회 역할 경로를 유지한다.

## 복구
신규 정책의 사전 부재와 이번 작업의 생성이 확인되고, 현재 정책이 이번 후보와 일치하며 후속 변경이 없을 때만 다음 삭제를 수행한다. 기존 설정/역할/사용자/MFA를 삭제하지 않는다.
```bash
aws iam delete-group-policy --group-name FDS-Human-Bootstrap --policy-name FDS-Human-Direct-ReadOnly-v1 --no-cli-pager
```
그 후 성공한 list-group-policies에서 신규 이름 부재, 기존 두 정책 및 membership의 백업 일치를 확인한다. 삭제 실패면 RECOVERY_PENDING으로 보고하고 확대 삭제하지 않는다. 이전부터 존재했거나 drift가 있으면 이 복구를 실행하지 않는다.

## 검증 및 근거
10/5 제출된 기존 그룹 정책 두 개와 후보의 공백 제외 JSON 크기 합계: 4256 characters / 5120. 실제 적용 직전 drift 확인은 별도다.
정적 범위 비교: 기존 조회 role의 5개 statement와 Action/Resource 동일, 모든 statement에 MFA+정확한 3인 조건, regional statement에 서울 제한 유지. AWS validation/simulation 및 실제 적용·본인 runtime은 NOT_RUN. 독립 REVIEW/MERGE는 PENDING.
AWS 근거: [MFA request context](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-multifactorauthpresent), [CloudShell IAM](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html).

크기 기준: [AWS IAM inline quota](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html).

## 10/5 오프라인 계약 검사 보완
[검사기](check-human-direct-readonly.py)는 AWS/credential/network 접근 없이 로컬 JSON만 읽는다. 검토된 동일 SHA의 검사기를 policy와 함께 CloudShell 작업 디렉터리에 준비한다.
저장소 checkout에서는:
```bash
python3 phase2/runbooks/check-human-direct-readonly.py && python3 -m unittest discover -s phase2/runbooks/tests -p test_human_direct_readonly.py -v
```
CloudShell 적용 전 한 줄의 첫 단계가 검사기이며, RC2면 중단한다. 기존 수동 membership/정책 drift/백업/독립 리뷰/Lead 실행 조건은 별도 유지한다. 검사기만으로 자동 적용 승인되지 않는다.

적용 후 get-group-policy --query PolicyDocument의 RC=0 JSON을 대상으로:
```bash
python3 check-human-direct-readonly.py --policy "$capture_dir/candidate.json" --readback "$capture_dir/applied.json"
```
정상: OFFLINE_CONTRACT=PASS, READBACK_CONTRACT=PASS, 두 파일 hash 출력. 이는 좁게 고정한 Action/Resource/Condition 계약 일치이며 AWS IAM simulator나 SCP/session을 포함한 유효권한 검증이 아니다. Statement/Action/Resource/principal 배열 순서와 Action/Resource 단일 문자열 표현을 정규화한다. 그 밖의 표현은 보수적으로 거부하므로 모든 IAM 의미 동등성을 판정한다고 주장하지 않는다.
후보 JSON SHA256: `c3be8228aa21289ae8773a600f272f9975f94dc8ba5a0123f2f67a7d4c8e3652`.

직접 로컬 실행: unittest4개 통과, 그중 보안 변경 subcase12개 모두 거부. 정상 후보 및 순서/단일값 표현 차이는 허용, 중복 JSON key는 거부. 12개는 MFA 제거/false/BoolIfExists, 대상 외 사용자, 서울 제한 제거/교체, 생성 권한/Action wildcard, ELB ARN wildcard, NotAction, statement 누락/중복이다.
이 검증기는 특정 계정/3인/서울 및 10/5 사용자 제출된 기존 role 범위에 결속된 보안 검사 코드다. 다른 환경에서 사용하려면 환경별 계약과 입력을 함께 변경·리뷰하며 제한을 삭제하지 않는다. 신규 보안 통제 코드를 순수 수집기 예외로 병합하지 않는다. 정책 JSON 자체 및 AWS는 이번 후속에서 변경하지 않았다.
