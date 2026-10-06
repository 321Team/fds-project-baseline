# #35 중앙 read-only delta validation — PR145 후속

CODEX_ASSISTED. #35 Lead 이하영, #37 소비 Lead 이재환, 권욱은 권한 검증 지원. 담당·일정·AC를 유지한다.

PR145는 HEAD `8c2640e4e6ef9120661d996d0a3d9fed375a99fc`의 하영·재환 독립 승인 후 2026-10-06 21:57:29 KST에 merge `f1e66492ca87f21d99d9848ab8606cd08185b9ff`로 편입됐다. 이번 수집기는 해당 merge의 두 정책과 고정 입력 JSON **raw SHA256 3개를 내부에 고정**한다. PR145의 Allow/Deny·backend HCL·고정 값 JSON bytes를 바꾸지 않는다. 문서에서 user_data 비밀 제외·문서 쓰기 범위·재생성 연결·root 사용/복구 기록을 보완한다.

이는 중앙 bootstrap·권한 적용에 앞선 **부분 정책 검증 결과 수집**이다. 전체 IaC 구축 권한, 실제 resource/API 구현, role trust/runtime 또는 bucket 정책 적용을 제공하지 않는다. 순수 읽기 전용 API만 allowlist에 있고 AWS 변경 API/SSM Parameter 원문/S3 object payload/사용자 credentials 조회는 없다. IAM 정책·trust·bucket 설정 원본은 실행자 전용 directory에 보존하며 공개 요약만 stdout에 출력한다.

## 수집 범위와 판정

| 수집 | 범위·판정 한계 |
|---|---|
| 실행 주체 | exact account root, 서울 API endpoint. root 사용 범위는 이번 readonly capture만이며 일상 Terraform apply 허용이 아님 |
| IAM snapshot | 승인 user3의 ARN, IaC/Network/Audit/Relay role·inline/attached/boundary 정책, Relay profile. managed default version을 전후 대조. PRESENT는 기대 trust/권한 일치나 grant 완료가 아님 |
| bucket snapshot | exact bucket에 ExpectedBucketOwner 사용, 서울 위치·Versioning·default AES256·PAB4·BucketOwnerEnforced·정책 구조 대조. raw object/state/versions는 읽지 않음 |
| ValidatePolicy | identity `IDENTITY_POLICY`, bucket `RESOURCE_POLICY` + `AWS::S3::Bucket`. findings 전부 private 보존·type/code만 stdout. 경고 포함 findings가 있으면 검토 필요, 자동 무시·수정 없음 |
| identity delta | **28 cases**. 4 state+4 lock, 삭제/버전 삭제, 다른 key/bucket/workspace/리전/주체/TLS, prefix, exact Relay 조회·PassRole(service/role/profile), 보호 bucket/Relay 편집. 이 fragment만 평가하며 user RO/guard/full role/SCP/boundary를 합성하지 않음 |
| IAM user bucket fixture | **18 cases**. 실제 user3의 CallerArn + 후보 ResourcePolicy + exact action/resource의 **synthetic Allow fixture**. 모든4 state 원문·버전/Put 및 대표 lock 거부, bucket metadata에서 이 후보 Deny와 충돌하지 않음. 실제 user의 현 RO/guard/권한을 수집·평가한 결과가 아님 |
| simulator 제한 | resource policy를 PolicyInputList에 넣지 않음. role/assumed-role/Audit/Network/root의 resource-policy 평가·whitelist 실제 복구는 NOT_SUPPORTED/NOT_TESTED. API 의존성·실제 bucket/state 존재·runtime도 NOT_TESTED |

**46개는 AWS에 요청할 delta cases 수다. 현재 AWS 실행 PASS 수가 아니다.** IAM custom simulation은 실제 S3/IAM 쓰기를 수행하지 않으며 실제 환경과 결과가 다를 수 있다. root/IaC 예외가 Allow라는 결론을 내리지 않는다. allowed 행은 누락 context 0을 요구하고 모든 request는 resource1개라 aggregate 응답으로 부분 거부가 묻히지 않게 한다. AWS의 legacy/새 ResourceSpecificResults 응답을 모두 확인한다.

bucket 위치는 root/ExpectedBucketOwner와 함께 `GetBucketLocation`을 사용한다. AWS는 위치 탐색에 HeadBucket을 권장하지만 여기서는 location/typed absence와 owner guard를 함께 수집하려고 지원되는 기존 API를 쓴다. AccessDenied·403/404 숫자·timeout·CLI 문제를 이름 부재나 생성 가능으로 바꾸지 않는다. typed NoSuchBucket은 **그 시점 부재**이며 이후 전역 이름 확보가 보장되지 않는다. 정책 JSON 구조 대조는 object key 순서만 무시하고 array 순서를 보존하며 일반적인 정책 의미 동등성 엔진이 아니다. snapshot 중 변경은 가능한 한 managed policy 전후 조회로 탐지하지만 전체 AWS snapshot의 원자성/장기 audit trail을 보장하지 않는다.

## 실행 소스와 CloudShell 준비

Python 3 표준 라이브러리·AWS CLI v2만 필요하다. 설치/상주/cron 등록 없이 1회 실행하고 실행자 `$HOME`에 mode700/파일600의 새 수집 경로를 만든다. AWS CLI pagination을 유지하고 남은 token을 발견하면 중단한다. 각 CLI 요청은 process40초·socket25초·connect5초, timeout/지정 transient error에는 최대1회 추가 시도한다. 실패/부분 raw 결과와 progress/manifest를 보존한다. 다음 실행은 새 directory이고 재시도를 과거 PASS에 이어붙이지 않는다.

이 PR은 기존 후보를 바꾸지 않는 collector지만 **source 무결성 검사와 IAM 판정 로직을 포함하므로 코드/혼합 기준으로 정확한 HEAD 독립 리뷰를 요청**한다. Pre-check 예외로 이 검사를 우회하는 병합/운영 적용을 하지 않는다. 기존 사용자 승인된 중앙 분석 범위는 유지하며 새 상시 이중승인/값 재채택을 요구하지 않는다.

리뷰된 정확한 source SHA로 GitHub archive를 받아 새 임시 디렉터리에 풀고 다음을 실행한다. 실제 배포 source SHA·archive 해시·collector 해시·AWS CLI/Python 버전·UTC/KST를 실행 기록에 함께 남긴다. mutable main이나 `latest`에 의존하지 않는다. 아카이브 신뢰는 GitHub/리뷰된 source에 근거하며 SHA 파일만으로 생성자 인증을 대체하지 않는다.

```bash
# 압축 해제된 저장소 디렉터리에서 실행
python3 -m unittest discover -s phase2/permissions/20261007-iac-delta-precheck/tests -p 'test_*.py' -v
(cd phase2/permissions/20261006-iac-fixed-inputs && sha256sum -c SHA256SUMS)
(cd phase2/permissions/20261007-iac-delta-precheck && sha256sum -c SHA256SUMS)
python3 phase2/permissions/20261007-iac-delta-precheck/capture-iac-delta-precheck.py
```

각 선행 명령의 RC0·해시 일치를 확인한 뒤 마지막 명령을 실행한다. shell의 `set -e/-u/pipefail`에 의존하지 않는다. 마지막 Python이 성공/실패 RC를 반환하고 stop 조건은 예외로 명시한다. `--source-dir`는 다른 위치의 **동일 고정 bytes**를 지정할 때만, `--output-parent`는 승인된 private 경로를 지정할 때만 사용한다. 정책 입력을 임의 바꾸면 AWS 호출 전에 멈춘다.

## 결과 수신·후속

- RC0: capture COMPLETE + ValidatePolicy NO_FINDINGS + delta46 PASS. **apply readiness·실효권한·role grant·본인 runtime·Stage-A/AC PASS를 의미하지 않는다.** bucket 부재/설정 차이는 별도 요약을 읽는다.
- RC2: capture COMPLETE + findings 검토 필요. raw findings와 위치를 해당 source diff로 리뷰한다.
- RC1: source/account/API/schema/pagination/decision/timeout 등 중단, capture INCOMPLETE. `stop.json`·마지막 private raw·progress 보존 후 해당 범위만 수정/다시 수집한다. 기존 AWS 설정을 초기화하지 않는다.
- 권욱은 stdout summary + 전체46행 또는 실패 행/RC + PRESERVED_DIR + source/collector/archive SHA + UTC/KST를 전달한다. **private archive·IAM raw·state/plan·credential을 공개 Issue에 통째로 붙이지 않는다.** 필요 원본은 기존 승인된 비공개 증적 경로로 인계한다. SHA는 수신 bytes 확인이며 변조 불가능/장기 audit의 대체가 아니다.
- 하영은 실제 component/resource/API/dependent-action/bootstrap/document **구현 PR/SHA + full IaC permissions JSON**을 연결한다. resource0 scaffold와 local-only 초안은 완성 인계로 승격하지 않는다. root desired bootstrap 생성/적용은 그 source와 before/readback/복구 범위가 구체화된 회차에서 진행한다.
- 이후 필요한 중앙 bootstrap·delta grant/readback, 권욱·하영 각 본인 IaC MFA runtime, 일반 IAM user3/Audit/Network의 비밀 없는 fixture GetObject/GetObjectVersion 거부, root whitelist 실제 복구·lock/version 복구를 받는다. role resource-policy 시험은 본인 runtime으로 확인하며 synthetic caller로 대체하지 않는다.
- #37은 actual Relay/profile/document/Agent/EBS 인계 후 exact bind→권욱·재환 각 본인 U1. 비용 설정 보류·교육장 daily 기반 통제·기존 Freeze/reviewed plan/cleanup·10/8 Stage-A→10/12 #37→10/14 G4 조건을 유지한다.

`AWS_VALIDATION=NOT_RUN_AT_SOURCE_PUBLICATION / AWS_SIMULATION=NOT_RUN_AT_SOURCE_PUBLICATION / AWS_MUTATION=NOT_RUN / ROLE_GRANT=NOT_RUN / USER_RUNTIME=NOT_TESTED / APPLY_READINESS=NOT_ASSESSED`

## 근거

- [PR145](https://github.com/321Team/fds-project-baseline/pull/145), [Lead 채택](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6015740112), [부분 정책](../20261006-iac-fixed-inputs/README.md), [구현 인계](../20261006-iac-fixed-inputs/integration.md)
- [리뷰 정책 §3.2 대상 외/코드 기준](../../../governance/REVIEW_AUTHORITY_POLICY.md)
- AWS 공식: [ValidatePolicy/types](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/validate-policy.html), [SimulateCustomPolicy/ResourcePolicy/role 제한/응답](https://docs.aws.amazon.com/cli/latest/reference/iam/simulate-custom-policy.html), [simulator 실제 환경 차이](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html), [bucket location/owner](https://docs.aws.amazon.com/cli/latest/reference/s3api/get-bucket-location.html)
