# #35 중앙 backend·Relay identity bootstrap 후보

작성일: 2026-10-07 KST. AI 보조: Codex. 분류: **새 Runtime 코드·IAM 정책·CloudFormation 설정을 포함하는 혼합 변경**. 독립 리뷰와 Lead 병합 판단 대상이다. 이 자료의 작성·모의 시험·PR 제출은 AWS 적용이나 Stage-A GO가 아니다.

## 근거와 구현 제안

- [Lead 확정값 #35](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6015740112): 계정 `774055931866`, 서울 `ap-northeast-2`, 고정 backend bucket, SSE-S3, Versioning, PAB 4개, BucketOwnerEnforced, default workspace의 고정 state/lock 경로, 중앙 bootstrap/recovery 소유권, Relay role/profile 이름·EC2 trust.
- [구현 인계 #35](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6015979237), [Agent 정책 범위 검토 #37](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6015560773).
- 기존 bucket 정책은 병합 `f1e66492ca87f21d99d9848ab8606cd08185b9ff`의 `phase2/permissions/20261006-iac-fixed-inputs/candidates/state-bucket-policy.candidate.json`을 내용 변경 없이 template에 포함했다. 원본 raw SHA-256: `05f66bd2f8041dd14f032a166cfe9ab2abfb307024d2d0452e9fef47d6ae5813`. 임베딩 후 JSON 들여쓰기는 원본 파일과 다르므로 정책 구조로 대조한다.
- PR #146의 중앙 수집 46 case/93 action, context 보완 9 case/14 action의 수신 결과는 [PR #147](https://github.com/321Team/fds-project-baseline/pull/147)에 있다. 이 패키지는 해당 정책 시뮬레이션을 다시 요구하지 않는다. 그 결과는 full IaC 권한·assumed-role bucket runtime·root recovery runtime을 증명하지 않는다.

**제안:** 초기 backend의 순환 의존성을 없애기 위해 아래 4개 자원을 별도 CloudFormation stack `FDS-Central-Bootstrap-v1`이 소유한다. 일반 Terraform은 생성된 profile을 data source로 참조한다. 별도 로컬 Terraform state나 다섯 번째 backend module을 만들지 않는다. CloudFormation 사용은 이번 후보의 새 구현 제안이며, 기존 Lead 결정이 이미 이 도구를 채택했다고 해석하지 않는다.

| 논리 자원 | 종류 | 고정값·보호 |
|---|---|---|
| StateBucket | AWS::S3::Bucket | `fds-tfstate-774055931866-ap-northeast-2`, 서울, AES256, Enabled Versioning, PAB 4개 true, BucketOwnerEnforced |
| StateBucketPolicy | AWS::S3::BucketPolicy | 기존 확정 후보의 state payload·TLS·principal 보호 정책 그대로 |
| RelayRole | AWS::IAM::Role | `FDS-Relay-SSM`, path `/`, EC2 service만 AssumeRole, AmazonSSMManagedInstanceCore만 연결 |
| RelayProfile | AWS::IAM::InstanceProfile | `FDS-Relay-SSM`, path `/`, 위 role 1개만 연결 |

모든 자원에 `DeletionPolicy: Retain`, `UpdateReplacePolicy: Retain`을 둔다. 생성은 termination protection과 `OnFailure: DO_NOTHING`으로 요청한다. 이 보호는 실패를 자동 복구하거나 root recovery 시험을 통과시킨다는 뜻이 아니다. 별도 주체가 stack을 삭제하면 retained 자원은 CloudFormation 관리에서 떨어질 수 있으므로 삭제·재생성·자동 편입을 복구 방법으로 사용하지 않는다.

사람용 IaC/Network role·trust·개인 AssumeRole 정책·권한 부여, EC2/EIP/EBS/VPC/ROSA, Session document, state/lock object 작업, Parameter 값, Secret, 비용 설정은 범위 밖이다. 이 패키지는 IAM 서비스 역할을 생성하며, 생성된 역할을 사람에게 부여하지 않는다.

## Agent 정책과 metadata 한계

`agent-policy.expected.json`은 [AWS 공식 AmazonSSMManagedInstanceCore v2](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.html)의 25개 action을 고정한 비교 입력이다. 실제 AWS default version·document를 두 번의 metadata 조회 사이에 확인한다. 버전 또는 내용이 다르면 중단한다. 정책의 `ssm:GetParameter`, `ssm:GetParameters`는 `Resource: "*"`이며 region 조건이 없다.

prepare/create는 계정에서 활성화된 모든 AWS region에 대해 `DescribeParameters`의 소유 metadata와 `Shared=true` metadata를 조회한다. 값은 읽지 않는다. 한 건이라도 발견되면 생성 요청 전에 중단하고 해당 소유자에게 분류·접근 범위 검토를 인계한다. 자동으로 customer policy를 만들거나 기존 guard를 고치지 않는다.

중요한 한계:

- `Shared=true`는 RAM에 promoted된 shared Parameter metadata만 반환한다. 정책으로 공유됐지만 promoted되지 않은 항목 등은 완전하게 증명하지 못한다. metadata 0건은 전체 effective access나 비밀정보 부재의 증명이 아니다.
- managed policy 연결은 향후 AWS default version 변경을 동결하지 않는다. 실제 Relay를 배치·사용하기 전에 정책 drift, 새 region/Parameter/공유 설정과 resource policy·KMS 조건을 다시 평가한다. 필요한 경우 소유자 검토를 거친 최소 권한 customer policy 변경으로 처리한다.
- 출력은 region별 건수만 공개한다. 이름·설명 등을 포함한 raw metadata는 0700 수집 디렉터리의 0600 파일에 보존한다. raw archive 전체를 공개 GitHub에 올리지 않는다.

공식 참고: [DescribeParameters](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-parameters.html), [CreateStack](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-stack.html), [DeletionPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-deletionpolicy.html).

## 검토·실행 순서

1. 이하영님은 bootstrap 소유권·backend 연계·전체 IaC 정책과의 관계, 이재환님은 Relay Agent 권한·Network 연계·실패 보존을 검토한다. 최소 1인의 작성자 외 적격 독립 리뷰와 최신 변경분 검토를 기록한다. Reviewer 지정은 리뷰 완료가 아니다.
2. Lead가 CloudFormation 구현 제안, 정확한 리뷰/병합 SHA, 아래 선행조건·중단/복구 기준을 확인하고 실행 여부를 결정한다. 추가적인 상시 Support 이중 승인을 만들지 않는다.
3. root CloudShell에서 아래 prepare를 실행한다. 수신 결과와 manifest를 확인한 뒤 같은 검토 소스의 create를 실행한다. create도 부재·Agent 정책·metadata를 새로 조회한다.
4. `SUBMITTED_NOT_READBACK` 수신 후 exact StackId로 CloudFormation 상태를 확인한다. `CREATE_COMPLETE`일 때만 verify를 실행한다. verify가 설정 대조를 통과해야 bootstrap 완료로 수신한다.

근거는 [REVIEW_AUTHORITY_POLICY §2·§3·§4](https://github.com/321Team/fds-project-baseline/blob/c34ca9c12d7cb38d610829cc59460ec6a8d87b1a/governance/REVIEW_AUTHORITY_POLICY.md)다. “작성자 외 적격 검토자 최소 1인의 독립 리뷰 후 Lead가 병합 결정”을 적용한다. 이 패키지는 쓰기·IAM 보안 통제 코드가 섞여 있어 §3.2 Pre-check 병합 예외로 분류하지 않는다. 독립 리뷰 전에는 로컬 모의 시험만 실행하며, root에서 이 혼합 helper의 실행은 검토 소스 확정 후 진행한다.

## CloudShell 실행

실행 환경: 기존 root CloudShell, Python 3.10 이상, AWS CLI v2. 기존 인증 세션을 사용한다. credential을 명령·출력·파일에 새로 적지 않는다. 비용 설정 권한은 추가하지 않는다.

검토·병합 SHA로 고정된 archive와 `.sha256`을 같은 디렉터리에 받는다. archive 파일명은 `fds-central-bootstrap-20261007.tar.gz`이다. 새 private 디렉터리에만 압축을 푼다. 명령은 조건별 RC를 확인하며 `set -e`, `set -u`, `pipefail`을 사용하지 않는다.

```bash
cd "$HOME"
umask 077
sha256sum -c fds-central-bootstrap-20261007.tar.gz.sha256
```

`OK` 후:

```bash
bootstrap_run_dir=$(mktemp -d "$HOME/fds-central-bootstrap-run.XXXXXX")
printf 'BOOTSTRAP_RUN_DIR=%s\n' "$bootstrap_run_dir"
tar --no-same-owner -xzf "$HOME/fds-central-bootstrap-20261007.tar.gz" -C "$bootstrap_run_dir"
```

압축 해제 RC=0 후 출력된 실행 경로로 이동한다. 아래 변수는 같은 CloudShell 세션에서 유지한다.

```bash
cd "$bootstrap_run_dir/fds-central-bootstrap-20261007"
sha256sum -c SHA256SUMS
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

manifest 모두 OK 및 시험 OK 후 읽기 전용 prepare:

```bash
python3 bootstrap-central.py --mode prepare
printf 'BOOTSTRAP_PREPARE_RC=%s\n' "$?"
```

성공: RC=0, `Status=PREPARED_NO_MUTATION`, `AWS_MUTATION=NOT_RUN`, 수집 경로 보존. prepare는 CloudFormation validate-template와 metadata 조회만 수행한다. 현재 생성 가능성을 최종 보증하지 않으며 bucket 이름 가용성도 보증하지 않는다. STOP이면 create로 넘어가지 않는다.

정확한 소스 리뷰·Lead 실행 판단과 prepare 결과 수신이 완료됐을 때만:

```bash
python3 bootstrap-central.py --mode create
printf 'BOOTSTRAP_CREATE_RC=%s\n' "$?"
```

create는 root/account 일치와 fresh preflight 후 `CreateStack`을 **1회** 요청한다. CLI 자동 재시도도 끈다. 성공 응답은 `Status=SUBMITTED_NOT_READBACK`, `StackId`, `ClientRequestToken`이다. 이는 자원 생성 완료나 runtime PASS가 아니다.

반환된 **exact StackId**를 다음 변수에 넣어 조회한다. placeholder를 그대로 실행하지 않는다.

```bash
bootstrap_stack_id='반환된 exact StackId'
aws cloudformation describe-stacks --stack-name "$bootstrap_stack_id" \
  --region ap-northeast-2 \
  --query 'Stacks[0].{StackId:StackId,Status:StackStatus,Protection:EnableTerminationProtection}' \
  --output json --no-cli-pager
```

`CREATE_IN_PROGRESS`이면 조회만 이어간다. `CREATE_COMPLETE` 후:

```bash
python3 bootstrap-central.py --mode verify --stack-id "$bootstrap_stack_id"
printf 'BOOTSTRAP_VERIFY_RC=%s\n' "$?"
```

verify는 exact stack·template·자원 4개, bucket 보호·기존 정책, role EC2 trust·단일 Agent policy, profile 단일 role, 실제 Agent version/document를 조회 대조한다. RC=0과 `Readback=BOOTSTRAP_SETTINGS_PASS`를 받는다. 일반 계정 권한·Agent/SSM runtime·root recovery·Stage-A 적용 가능성은 여전히 미검증이다.

각 단계에서 출력된 `PRESERVED_DIR`를 보존하고 manifest를 확인한다.

```bash
bootstrap_capture_dir='출력된 PRESERVED_DIR'
(cd "$bootstrap_capture_dir" && sha256sum -c --status SHA256SUMS)
printf 'BOOTSTRAP_CAPTURE_MANIFEST_RC=%s\n' "$?"
```

공유할 것은 UTC, exact execution ARN, 소스/helper hash, mode, RC, summary/stop의 판정·StackId·token·수집 경로·manifest RC다. Parameter raw 이름·설명·credential은 공유하지 않는다. 각 일반 계정의 테스트 결과는 이후 실제 역할 부여 단계에서 따로 받는다.

## 중단·복구

| 상황 | 처리 |
|---|---|
| root/account 불일치, source hash 불일치 | 생성 전에 중단. 실행 소스·세션을 확인한다. |
| bucket/role/profile/stack 존재 | 동일 설정이어도 자동 편입·overwrite하지 않는다. 소유권·정확한 차이를 확인하고 별도 검토 변경으로 해결한다. |
| AccessDenied·일반 ValidationError·잘린 응답·timeout | 부재나 PASS로 취급하지 않는다. raw 응답·부분 로그·manifest를 보존한다. |
| Agent version/document 변경, Parameter metadata 발견 | 생성 요청 전에 중단. 실제 범위와 소유자 검토를 거쳐 후보를 수정한다. |
| create timeout/오류 | 요청 전에 token을 journal에 기록한다. 결과 미확정으로 표시하며 **create를 다시 실행하지 않는다**. root에서 고정 stack 이름으로 DescribeStacks/DescribeStackEvents를 조회하고 원본 token·발견한 exact StackId를 대조한다. |
| CREATE_FAILED 등 부분 생성 | 자동 rollback/delete/import/repair하지 않는다. stack event와 실제 생성 자원을 보존한다. 실패 원인·자원 소유권·안전한 수정 또는 복구 범위를 Lead가 결정하고 필요한 변경 소스만 리뷰한다. |
| CREATE_COMPLETE이나 readback 불일치 | PASS를 만들기 위해 쓰지 않는다. IAM propagation과 실제 drift를 확인한다. 원인을 확인한 뒤 읽기 전용 verify만 다시 실행할 수 있다. |

`Retain`과 termination protection은 데이터 보호 수단이다. partial failure에 무조건 정상 상태로 돌아가는 rollback 약속은 하지 않는다. 복구 구현·삭제·update 권한은 이 create-only helper에 없다. root recovery 원본 runtime 증적도 이번 모의 시험으로 대체하지 않는다.

## 재현성과 남은 인계

소스 패키지는 helper·고정 template·Agent 비교 문서·provenance·README·시험·SHA256SUMS로 자급된다. 이전 collector 경로를 설치하거나 import하지 않는다. helper는 실행 JSON의 raw hash를 고정하고 결과에 자신의 실제 raw hash를 기록한다. archive는 소스 파일만 포함하며 실제 AWS 수집 결과를 포함하지 않는다. 각 실행은 새 private 디렉터리에 request/raw/summary/manifest를 남긴다.

로컬 모의 시험 14건 PASS: read-only 경계, root/계정, typed absence, 버전 race/확장, 활성 region·shared metadata, 잘린 응답, create 단일 요청·retention, timeout 부분 보존, exact readback·drift, source tamper, credential 비출력. 모의 시험은 AWS 실제 API 호환·CloudFormation 생성·effective permission 증명이 아니다. 실제 AWS: `NOT_RUN`, 사람 권한 부여: `NOT_RUN`.

bootstrap 수신 후 이하영님의 full IaC build/action·resource 정책과 Stage-A 소스를 연결한다. Network는 role/trust/개인 AssumeRole 선행조건을 확보한 다음 실제 Relay·Session document binding과 U1로 넘어간다. 이번 4개 자원 생성만으로 개인별 업무 역할이 완성되거나 #35/#37을 종결하지 않는다.
