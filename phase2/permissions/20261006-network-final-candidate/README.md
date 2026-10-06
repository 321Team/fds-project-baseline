# Network 권한 최종 후보 검토 — star-Bool 권고

CODEX_ASSISTED. 책임 #35/#37. 2026-10-06 17:54 KST 사용자 실행 결과 수신 후 준비한 **새 IAM 정책 후보 리뷰**다. 후보 선택 권고와 실제 grant를 구분한다. 이번 범위에는 AWS 쓰기·적용 스크립트·Relay 생성·기본 문서 생성이 없다.

## 수신 결과와 출처

- 검토 수집기: PR142 HEAD `5bfec301b84b308f3d1d8ae974e70dc81642d189`, merge `8dbc4bcad19eba4e8b1f3d3be859e7484cef640a`. 재환의 최신 HEAD 독립 승인5425857957 및 GitHub 실제 병합(17:44:17 KST)을 확인했다.
- 사용자 전달 stdout: 24,125 bytes, SHA256 `33c5f39504c79da2a416bc18ecff084f5a81e87b09615c60a2f1068ea9277c4e`. 실제 원본 폴더 `/home/cloudshell-user/fds-network-permission-precheck-bruyz836`는 사용자 CloudShell에 보존한다.
- `NETWORK_CANDIDATE_CAPTURE=COMPLETE`, `NETWORK_PRECHECK_RC=0`. 후보4개 각각30그룹, 총120(기대 비교96 + 채널 관찰24), 재사용32/새88. 각 후보 validation=NO_FINDINGS/findings0/matrixCOLLECTED. case/action 전체 실제 API 실행 성공을 의미하지 않는다.
- 기본 문서 `ABSENT_OR_UNAVAILABLE`. 부재 또는 해당 조회에서 이용 불가를 의미하며, 문서 owner/default-version/내용/session KMS/logging을 확보했다고 표시하지 않는다. 기존과 새 capture의 문서 상태 비교를 수집기가 통과한 결과로 보고했지만 실제 문서 내용 drift를 검증한 것은 아니다.
- **받은 자료는 stdout만**이다. 이 세션은 private raw/API response/전체 summary/manifest를 독립 재검증하지 않았다. 수집기 source는 COMPLETE 전에 manifest를 저장하고 root/문서/재사용 raw를 검증하도록 구현돼 있다. 수신 파일 해시는 전달문 바이트의 출처 지표이며 AWS 독립 서명이나 최종 권한 증명이 아니다.
- 상세 결과를 `received-result-summary.json`으로 추출했다. stdout에서 실제 실행 시각/원본 ExecutionArn은 표시되지 않았으므로 수신 시각만 기록한다.

## 채널 관찰과 권고

Bool과 BoolIfExists 사이의 채널 관찰은 같았다.

| 채널 후보 | 서울 session ARN 입력4종 | 서울 `*` 입력 | 서울 외 `*` 입력 |
|---|---|---|---|
| ARN | implicitDeny | implicitDeny | implicitDeny |
| `*` | implicitDeny | allowed | implicitDeny |

session ARN 입력4종은 role-id를 포함한 본인/다른 사용자 형식과 RoleSessionName 형식의 권욱/재환 가설이다. 첫 Stage-A 실제 SessionId는 아직 없다. 모든 채널 관찰의 MissingContextValues는 빈 목록이었다. 이 결과만으로 deny 원인을 실제 SessionId 불일치라고 확정하지 않는다.

권고: **사람 OpenDataChannel만 `Resource="*"` + 서울 리전 조건으로 선택하는 star-Bool 후보를 정식 리뷰에 올린다.** 현재 ssmmessages 권한 표는 resource ARN 지정을 지원하지 않는다고 명시하고, 중앙 비교는 `*` 입력에서만 allow를 관찰했다. 반면 AWS Session Manager 예제에는 session ARN 방식도 있으므로 공식 자료 간 차이와 실제 client 검증의 필요성을 남긴다. `*` 정책으로 평가한 합성 ARN이 deny였다고 다른 사용자의 채널이 실제 차단된다고 주장하지 않는다. **채널 단계의 계정/target/소유자 ARN 격리는 이 statement 자체가 증명하지 않는다.**

`network-permissions.proposed.template.json`은 PR141의 원본7 statements + 이미 비교한 ServiceAuthorizationResourceCandidate 1개다. Relay placeholder를 수집기의 합성 ID로 바꾸면 PR142 `star-Bool` 후보와 JSON 구조가 정확히 같다. 기존7 statements/region/document/owner/target/복구 조회 범위는 그대로이며 8 statements/18 unique actions다. 비교한 statement의 Sid도 유지한다. 허용 범위가 비슷한 별도 정책을 재작성하지 않는다.

## 문서 조건과 첫 client 경로

첫 후보는 기존 **Bool true**를 유지한다. 중앙 case09에서 Bool은 검사 키 누락 시 instance implicitDeny, BoolIfExists는 instance allowed였고 각자의 기대값과 일치했다. IAM IfExists는 키가 없으면 해당 조건을 true로 평가한다. 문서 제한이 목적이므로 실제 client가 정상 검사 context를 공급하는지 확인하기 전 누락 키 허용으로 완화하지 않는 권고다. 이는 Bool이 실제 CLI/콘솔에서 이미 성공했다는 결론이 아니다.

첫 Stage-A는 **AWS CLI + Session Manager plugin, `--document-name SSM-SessionManagerRunShell` 명시**를 제안한다. 실제 document/context 조건 공급 여부와 owner/target 태그는 서비스 runtime에서 확인한다. 문서 이름 명시가 검사 키 공급을 보장한다고 주장하지 않는다. 이 경로가 정당한 요청을 거부하면 실제 오류·요청 조건을 확인해 BoolIfExists 등 변경 diff를 검토하고, 자동 완화하거나 다른 문서로 우회하지 않는다. 포트포워딩·SSH 문서와 사람 SendCommand/Agent 전용3종을 추가하지 않는다.

## 실제 적용 전 인계와 담당 범위

| 항목 | 필요한 값/증적 | 기존 담당 연결 |
|---|---|---|
| SSM 기본 문서 | 이용 불가 사유, account owner·Session/Standard_Stream·default-version·내용 SHA, session KMS/S3/CloudWatch 설정과 생성/구성 코드 | #35 IaC/bootstrap 인계(하영), 중앙 root 검증·적용 |
| Relay/Agent | Stage-A Relay actual ID, role/profile exact ARN, Agent 설치·Online, SourceDestCheck readback·EBS key/Start 복구 의존성 | 기존 IaC 구현/인계; 권한 초안 리뷰와 병행 |
| 최종 bind | 위 값으로 placeholder 제거, exact 정책/hash·trust/개인 AssumeRole/기존설정·원복 기준 확인, 변경 범위 중앙 validation/simulation | 중앙 root; 기존22-case를 이유 없이 다시 하지 않음 |
| 사용자 runtime | 권욱·재환 각 본인 U1의 STS role/session, 실제 SessionId 형식, 기본 셸 연결·본인 Resume/Terminate 및 정해진 복구/음성 경계 결과 | 권욱/재환 각각; 공통 ReadOnly 결과를 쓰기 role PASS로 대체하지 않음 |

현재 기본 문서를 임의의 무로그/무KMS 설정으로 만들지 않는다. 문서 설정 부재가 KMS 불필요의 증거가 아니며 세션 KMS와 Relay EBS key는 별도로 판단한다. 네트워크 담당자에게 문서 생성/수정·KMS/비용·IAM 권한을 자동으로 추가하지 않는다. actual ID가 없어도 이 후보 리뷰는 진행하고, 실제 bind/grant와 첫 Stage-A 접속에는 값을 확보한다. IaC JSON 전체를 후보 리뷰의 새 대기로 만들지 않는다.

적용 가능한 정책 또는 AWS 변경 명령은 이번 PR에서 제공하지 않는다. placeholder가 남은 이 파일을 연결하지 않는다. 역할 grant/실제 client 연결/기본 문서 생성은 아직 미실행이다. 이 수신 결과의 원복 API는 없으며 원본 보존·소스 revert로 관리한다.

## 리뷰·검증 상태

**새 IAM 정책 변경 후보**로 독립 리뷰를 요청한다. PR142의 승인은 수집기 승인이고 이 채널 선택·문서 조건 권고/최종 apply 승인이 아니다. 일반 코드/실행 입력 기준으로 다루며 Pre-check 무리뷰 병합 예외를 이 정책에 적용하지 않는다. Reviewer는 기존 하영/재환이며 필수 서명 수를 새로 늘리지 않는다.

- STATIC: 생성 JSON 파싱, 8 statements/18 actions, placeholder·조건·기존7 statements 보존 및 합성 bind 후 기존 star-Bool 구조 일치 PASS.
- 신규 unit/mock/CI/AWS API: 아직 미실행 또는 해당 없음. PR142의 로컬 Linux 29 unit/mock PASS와 Windows 28 PASS/POSIX mode 표현1 FAIL을 보존한다. canonical-integrity CI는 정본 검사이며 unit29 실행 CI가 아니다.
- 실제 AWS 수집: 사용자 stdout 기준 RC0/120그룹. 최종 actual-bound 정책 validation/simulation, 사용자 effective permission 및 client runtime는 NOT_TESTED.
- `RECOMMENDATION=star-Bool / STATUS=PROPOSED_FOR_REVIEW / CHANNEL_SELECTION=NOT_MADE / FINAL_APPLY_POLICY=NOT_CREATED / ROLE_GRANT=NOT_RUN / AWS_MUTATION=NOT_RUN / APPLY_READINESS=NOT_ASSESSED`.

비용 설정 보류, 기존 담당/AC/일정/Freeze·티켓 상태는 그대로다. 이번 권고의 수용/리뷰를 역할 grant나 최종 인수로 확대하지 않는다.

## 18:16 병합 후 리뷰 후속

후보 HEAD `87d1bb2533dc05927b64ed9ab7f4d9b9ff1f0ca7`에 재환 review5426140186 APPROVED와 Lead review5426256383을 근거로 PR143은 2026-10-06 18:16:11 KST merge `1059713f1a56a1a9d0d88aa37470c5e582e1d580`에 병합됐다. 하영 review5426272751은 동일 HEAD에 18:17:14 KST 추가 승인했다. 위 PROPOSED_FOR_REVIEW 상태는 제출 당시 기록이다. 현재 후보 소스 리뷰/병합은 완료됐고 실제 bind/grant/client runtime는 여전히 미실행이다.

리뷰 후속은 [실제 bind 의존성 Pre-check](../20261006-network-binding-precheck/README.md)에 연결했다. 문서 구성을 final bind/U1 선행조건으로 명시하고, Start/Resume 토큰 취득 경계와 채널 runtime 증명을 구분하며, 실제 SessionId·owner/target·각 본인 계정 결과를 요구한다. 다른 사람의 진행 중인 업무 세션을 음성 시험 대상으로 삼지 않는다. 진단 DescribeSessions의 타인 metadata 조회 범위를 기록했다. 승인된 후보 JSON/Bool/18 actions는 변경하지 않는다.

추가 수신한 [재환의 구성 결정6013422735](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6013422735)은 세션 로깅/KMS/Run As를 사용하지 않는 Standard_Stream 문서를 #35 Terraform에서 생성·readback하도록 정했다. 위 "임의의 무로그/무KMS 설정으로 만들지 않는다"는 제출 당시 경계를 보존하고, 이제 담당 Lead의 명시적 결정으로 인계한다. 실제 생성 source/readback·Relay 의존성·EBS/state KMS·최종 정책/사용자 시험은 아직 확보하지 않았다. 이 결정 자체를 P0·AC 충족으로 판정하지 않는다.

## 공식 근거 (2026-10-06 확인)

- [ssmmessages action/resource 권한 표](https://docs.aws.amazon.com/service-authorization/latest/reference/list_ssmmessages.html)
- [Session Manager 예제](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-restrict-access-quickstart.html)
- [SSM Start/Resume/Terminate·조건/시스템 태그](https://docs.aws.amazon.com/service-authorization/latest/reference/list_ssm.html)
- [IAM IfExists 조건 연산자](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html)
- [세션 시작/CLI plugin](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html)
