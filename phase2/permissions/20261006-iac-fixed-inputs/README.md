# #35 확정 입력의 backend·PassRole·state 보호 후보

CODEX_ASSISTED. 2026-10-06 #35 후속 착수. 작성 범위는 권욱의 권한 설계·검증 지원이며 #35 구축/인수 Lead 이하영, #37 구성/인수 Lead 이재환을 유지한다.

하영의 [20:58:21 KST 결정](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6015740112)과 [#35 심층 리뷰](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6015979237)의 고정 입력을 검토 가능한 소스로 옮겼다. 이름/암호화/4 key 채택을 다시 요청하지 않는다. 21:29 KST 조회의 infra-terraform main `1f166d5c27ff24316887ae8ee2f2211fbb9a1a7d`는 resource 0개 scaffold이며 열린 구현 PR은 0개였다. 이 묶음으로 resource 구현이나 전체 업무 permissions가 완성되지 않는다.

## 범위와 파일

| 파일 | 용도·제한 |
|---|---|
| `inputs/lead-values.json` | 채택 값, 근거 commit/회신, 현재 미실행 경계. 실제 AWS 상태 수집물이 아님 |
| `candidates/iac-backend-passrole.candidate.json` | **부분 identity policy**. exact 4 state/lock, 필요한 bucket 조회, Relay role/profile 조회, EC2 exact PassRole. EC2 구축·SSM document·ROSA 쓰기 및 완결된 work-role 권한은 미포함 |
| `candidates/state-bucket-policy.candidate.json` | exact 8 object의 payload/변경 접근 제한과 TLS/SSE-S3 보호 **resource-policy 후보**. bucket 생성/보호 설정을 실행하는 도구가 아님 |
| `backends/*.candidate.hcl` | component별 확정 backend 입력 4개. Terraform root/resource 분리 구현을 대신하지 않음 |
| `integration.md` | 하영 구현 source/API 인계, account guard 반영안, 중앙/본인 시험·복구 계획 |
| `tests/test_fixed_inputs.py` | 표준 Python만 사용하는 오프라인 fixture·회귀 검사. AWS simulator/Access Analyzer/실제 API가 아님 |
| `SHA256SUMS` | 이 묶음의 배포 bytes 확인. AWS 적용/동작/전체 인수의 증명 아님 |

이 JSON은 실행 시 소비될 수 있는 IAM/보안 설정이다. 순수 Pre-check 병합 예외로 분류하지 않고 **코드/혼합 PR의 정확한 HEAD 독립 리뷰**를 받는다. 기존 trust/개인 AssumeRole 후보·공통 ReadOnly/guard·Network 후보·과거 collector/archive를 수정하지 않는다. 자동 부착/적용 명령은 제공하지 않는다.

## 부분 identity 정책의 경계

- Allow의 `aws:PrincipalArn`은 `arn:aws:iam::774055931866:role/FDS-IaC-Operator`로 제한한다. role 세션 문맥의 IAM role ARN이며 STS 세션 ARN이나 개인 IAM user ARN이 아니다. 잘못된 일반 계정 부착으로 동일 Allow를 부여하는 경로를 만들지 않는다.
- S3 state/lock 읽기·쓰기와 prefix 목록은 서울 endpoint와 TLS 조건이다. exact bucket 위치 조회와 IAM role/profile 조회는 별도다. IAM global API에 서울 RequestedRegion을 일괄 요구하지 않는다. 실제 bucket owner/region과 backend/provider account guard는 적용 전에 별도로 확인한다.
- state GetObject/PutObject, lock GetObject/PutObject/DeleteObject만 Allow한다. state DeleteObject 및 state/lock DeleteObjectVersion은 명시적 Deny다. state 버전 복구는 중앙의 승인된 회차로 한다.
- bucket ARN의 `NotAction=[s3:Get*,s3:List*]` Deny는 해당 protected bucket의 비조회 작업을 IaC가 수행하지 못하도록 한다. **bucket ARN만** 대상이며 object Put/lock Delete Allow와 혼동하지 않는다.
- Relay role/profile ARN의 `NotAction=[iam:Get*,iam:List*,iam:PassRole]` Deny로 일반 IaC의 protected identity 변경을 막는다. PassRole Allow는 role ARN 한 개와 `iam:PassedToService=ec2.amazonaws.com`이다. profile ARN에는 PassRole Allow가 없다.
- MFA는 기존 trust/개인 AssumeRole 후보에서 확인한다. assume 후 모든 AWS API 문맥에서 MFA=true를 요구하는 방식으로 구현하지 않는다. role permission은 기본 user RO/guard와 합산되지 않으므로 실제 구현에 필요한 조회·서비스 쓰기를 추후 소스로 정한다.
- 비용 설정·KMS·EC2/SSM/ROSA 쓰기 Allow는 없다. **이 fragment만으로 role을 발급하거나 Terraform 구축 가능이라고 판정하지 않는다.**

### native backend의 workspace 목록

Terraform 1.16.4의 [S3 Workspaces 소스](https://github.com/hashicorp/terraform/blob/v1.16.4/internal/backend/remote-state/s3/backend_state.go)는 기본 prefix `env:` 뒤 `/`를 붙여 ListObjectsV2를 호출한다. 후보는 `phase2/*`와 **정확한 `env:/` 목록 prefix**를 허용하되 `env:/...` state/lock 객체의 Get/Put/Delete는 허용하지 않는다. default workspace만 사용한다. 실제 init/lock 및 필요한 API는 아직 시험하지 않았으며 추가 호출이 있으면 해당 차이만 소스/정책으로 검토한다.

## bucket 원문 예외와 암호화

후보 whitelist는 IaC IAM role ARN과 기존 중앙 root 경로의 `arn:aws:iam::774055931866:root`이다. root 값은 현재 승인된 중앙 bootstrap/복구 경로를 검토할 수 있도록 구체화한 **코드 후보**이며 새 복구 role/계정 권한을 생성한 결정이 아니다. 다른 지정 복구 주체가 필요하면 exact ARN/source와 적용 범위를 해당 변경에서 검토한다. `aws:PrincipalArn` 조건의 root 값은 root 사용자만 가리키며 Principal의 account 전체 위임과 다르다.

8개 state/lock 객체에서 whitelist 밖 주체에는 `NotAction`으로 원문·버전 읽기와 변경을 Deny한다. ACL/tag/legal-hold/retention/parts의 지정 metadata 읽기만 Deny의 대상에서 제외한다. 이 방식은 UpdateObjectEncryption 등 새로운 변경 API를 나열 누락하여 노출하는 경로도 차단한다. **Deny 예외는 Allow가 아니다.** role/root의 실제 Allow·SCP·boundary·trust·다른 자원 정책은 별도로 판단한다.

일반 서비스·bucket metadata 조회는 유지한다. 다만 AWS의 `HeadObject`, `GetObjectAttributes`, `SelectObjectContent` 일부 조회는 IAM `s3:GetObject`/`s3:GetObjectVersion`를 사용한다. 따라서 **보호된 state/lock 객체의 HEAD·해당 속성 조회도 일반 사용자/Audit에 거부**된다. API 이름별 허용으로 raw GetObject와 분리할 수 있다고 표시하지 않는다. 필요한 비밀 없는 backend identity/실제 ID는 정제된 handoff artifact로 인계한다.

TLS Deny는 일반 호출에서 강제하며 AWS service network 문맥 문제를 피하기 위해 direct service principal을 해당 transport statement에서 제외한다. 이것이 service payload Allow는 아니다. whitelist 밖의 서비스도 위 object 보호 Deny에 걸린다.

PutObject는 명시적으로 AES256 외의 SSE header나 SSE-C header를 사용하면 Deny한다. encryption header 생략은 **실제 bucket default가 SSE-S3/AES256임을 확인한 조건**에서 정상 lock writer를 지원한다. 기본 암호화·Versioning/PAB/ACL disabled/TLS 보호가 완성됐다는 증거는 이 JSON만으로 만들 수 없다. 버킷 설정 readback은 중앙 bootstrap에 포함한다. 일반 IaC에는 bucket 보호 변경을 열지 않는다.

정확한 4 state/4 lock 이외의 backup·snapshot·임시 state 객체는 이번 예외 범위에 없다. 새 객체 경로를 저장하기 전에 접근 경계를 별도로 정의한다. 복구는 동일 key의 VersionId 보존 경로를 기본으로 하며 원본 state·binary plan·credentials를 GitHub/stdout에 공개하지 않는다. PSK/장기 credential은 source/plan/state/AMI에 넣지 않는다.

## 로컬 검증과 다음 실행

위 디렉터리에서 Python 3 표준 라이브러리와 `sha256sum`만 사용한다. AWS credential/CLI는 필요 없다.

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
sha256sum -c SHA256SUMS
```

정상 기준은 unittest 모든 항목 PASS와 배포 파일 해시 일치다. 불일치/실패 시 적용하지 않고 해당 source 차이부터 확인한다. 테스트 fixture matcher는 이 묶음의 단일 값 조건만 다루며 AWS resource applicability·API dependency·SCP·boundary·trust·서비스 동작을 모델링하지 않는다. Terraform fmt/init/validate와 AWS ValidatePolicy/simulation도 이 검사에 포함되지 않는다. 실패했다고 기존 AWS 설정을 삭제하거나 초기화하지 않는다.

다음 단계는 [integration.md](integration.md)의 actual resource/API 인계와 변경 범위 검증이다. 중앙 policy validation과 identity-side delta simulation은 해당 후보/완성 소스로 진행하되 bucket-policy role 평가의 simulator 지원 범위를 확인한다. 일반 사용자/Audit 음성 및 IaC role의 실제 원문/lock 동작은 비밀 없는 fixture와 본인 역할에서 별도로 받는다. 기존 unchanged identity22/Network120을 전체 재실행할 이유는 없다.

`SOURCE=PARTIAL_CANDIDATE / INDEPENDENT_REVIEW=NOT_RECEIVED / AWS_VALIDATE_POLICY=NOT_RUN / AWS_SIMULATION=NOT_RUN / AWS_MUTATION=NOT_RUN / ROLE_GRANT=NOT_RUN / USER_RUNTIME=NOT_TESTED / APPLY_READINESS=NOT_ASSESSED`

## 근거

- 정본 [#35 v3.1.21](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/P2-IAC-01.md), [#37 v3.1.21](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/P2-VPN-01.md)
- [하영 입력](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6011033747), [값 채택](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6015740112), [#35 리뷰](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6015979237), [#37 리뷰](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6015560773)
- [work-role trust/identity 후보](../20261006-work-role-precheck/README.md), [team build/test 범위](../20261006-team-build-test/README.md)
- 공식 문서(2026-10-06 확인): [S3 backend/lock/최소 권한](https://developer.hashicorp.com/terraform/language/backend/s3), [PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html), [PrincipalArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principalarn), [S3 API→IAM action](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html), [S3 조건](https://docs.aws.amazon.com/AmazonS3/latest/userguide/amazon-s3-policy-keys.html)
