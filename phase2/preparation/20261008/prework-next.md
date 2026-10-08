# Phase 2 사전 작업 목록과 착수 결과

2026-10-08 17:50 KST 후속 반영(아래 수행 기록은 각 관측 시점 기준). CODEX_ASSISTED. Phase 1 구현·실행·Close 제외. 현행 발행 정본은 docs-v3.1.21이며 이 문서는 working preparation이다. 담당·AC·일정·권한 범위를 새로 정하지 않는다.

16:23 KST 이후 후속: [설계 방향 승인6054292320](https://github.com/321Team/infra-rosa/issues/3#issuecomment-6054292320)을 반영했다. [D22 Lead 검토·12출력/A-B 선택안](d22-lead-review.md), [생성·삭제·보존·Review 준비](lifecycle-review-preparation.md) 작성 완료. D21 raw는 독립 승인·CI 후 PR161 병합 완료로 갱신했다(17:05:38 KST, merge277893c). 현재 1차 인수 준비 단계이며 [17:40 리뷰](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6056087764)의 후보 수용과 잔여를 아래에 반영한다. 이번 변경은 우리 준비 문서의 정정이며 생산자의 #3/#10/#11 보완 완료를 대신하지 않는다.

## 이번에 실제 완료한 것

- CICD [PR68](https://github.com/321Team/infra-cicd/pull/68): 이하영의 정확한 HEAD 독립 승인·CI 2건 SUCCESS와 미해결 차단 없음 확인 후 사용자 착수 지시에 따라 #46 Lead 이권욱 범위에서 수동 병합. HEAD `a466370ed9fcec724b4c5fe4f61f2e71f28d7298`, merge `8658c332fb5803ca1e53d3b8aefc4d4da179fdf6`, 14:47:36 KST. 예상 HEAD 지정 및 병합 후 재조회 완료. [Lead 기록](https://github.com/321Team/infra-cicd/pull/68#issuecomment-6053283635).
- MSA [PR24](https://github.com/321Team/fds-msa/pull/24): 생산자가 14:41:49 KST 병합한 결과를 수신했다. 승인 HEAD `85b20f45ba4e2a4b3afb55d1ab41c970938374ca`, merge `6a95e1a5d7e7e25ac83694ca932ea1be65699053`. R1~R4 해결·독립 승인 완료. 이 작업에서 새 승인하거나 병합한 것으로 표시하지 않는다.
- 승인 HEAD와 병합본의 CICD 5파일·MSA 3파일·Terraform network6/vpn10파일 **24개 바이트 동일** 확인. Terraform16파일은 기존 candidate manifest SHA256과 모두 일치한다. [검증 접수 기록](merged-source-receipt.json).
- `p2e2e.py`의 병합본 SHA256은 `a00ae029b69782040fa0e120d8a8b763e81325055cb70ca26c6d8d30ce88a07d`로 [생산자 수신값](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6053198464)과 일치한다. 실제 실행 시 다시 이 파일과 기준·CA·대상을 연결한다. hash 일치는 Runtime 성공이 아니다.

## 권장 순서·잔여·완료조건

| 순서 | 사전 작업 | 담당/소비 | 현재 상태와 다음 완료조건 |
|---|---|---|---|
| 1 | 승인 PR 병합·소스 연결 | 권욱 / 해당 Lead | 이번 단계 완료. Terraform6/7·CICD68·MSA24 병합 소스를 구분해 연결. 실제 실행 수용 SHA는 별도 |
| 2 | full IAM JSON/trust·정책 SHA·Action/Resource/Condition·AMI/PassRole/backend·회수/복구·simulation 기대표 | #35 하영 → 권욱 중앙 검토 | 입력 대기. 최신 [Lead 준비 수용](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6049616674)은 전체 정책 제출·부여 수용이 아님 |
| 3 | 중앙 검증/부여/readback → 각 본인 MFA·권한·state/lock·거부·복구 | #35 권욱/각 사용자 | 2 이후 실행. 예전 role 부재 관측을 현재 상태로 단정하지 않음. 중앙 검증과 업무 Plan 계정 구분 |
| 4 | ROSA 상세 topology·worker key/AZ·N-1 용량·disk·CIDR·platform egress·API/Ingress·STS/OIDC | #34/#38 하영 → 권욱 | private_a/2a·NAT1·3개 Namespace 방향 및 4.22.16/300GiB/IMDSv2/AutoRepair 후보 수용. 버전/교체 정책 문구·Pool 관리 소유권, NAT IaC·CIDR/용량·API/Ingress·연결 잔여. Quota PARTIAL, 역할 이름 필터 미발견·활성화 미확인. 생성 전 actual Node ID는 요구하지 않음 |
| 5 | Relay Libreswan/repo·조건부 HTTP 근거·EBS 보존/삭제·CPU credit·Session document 소유 | #35/#37 하영/재환 | 입력 대기. 소스 리뷰 차단은 해소. 실제 Stream9 설치·Agent Online은 생성 후 검증이며 새 병합 Gate로 올리지 않음 |
| 6 | 관리/반환/source·필수 DNS 및 App/DB source-set·NP·credential·복구 소유 | #40/#37/#38/#43/#47 권욱/하영/재환 | 계약 입력 대기. 경로·최소 권한·실패 시 중단과 원복 책임을 연결 |
| 7 | D22 생성 전 endpoint·CA/trust·pull principal·node-pull 경로 | #42 권욱 + 플랫폼 입력 | 공개 CA 후보·오프라인 이름 검증 수용. exact key/config/hash/provider·principal/경로 잔여. 생성 후 승인 경로 cold-pull → Basic Ready → D22 Final; P0 IP 후보를 D23 전체 DNS 일정에 묶지 않음 |
| 8 | App base/overlay·시험 DB 전환/정리·Secret·health 및 D-03 실패 경로 | #43 재환/하영 | 구현·실행본 대기. 엔진 timeout/오류 응답/DB 저장 실패 rollback은 각각 원본 필요; engine0/DB 경로 차단으로 대체하지 않음 |
| 9 | 설계 입력 취합·Freeze 판단과 network Plan 접수 | #34/#35 권욱/하영 | 아래 단계별 준비표 사용. 2~6 조건 중 해당 단계 입력 충족 전 Cloud Plan/Apply 미실행 |
| 10 | 실제 P2 Delivery adapter/transport·claim/lock/checkpoint·실패/UNKNOWN·복구 연결 | #46 권욱, #38/#42/#43 입력 | 진단 도구만 병합. [기존 계약](delivery-test-contract.md)의 실제 target/권한/approved digest/manifest/health 입력 대기. 입력 진단 RC0은 배포 허가 아님 |
| 11 | B2 장애·복구안 F1 시간표/F2 관리 접근·관측 보완 | #50 재환 → 권욱 QA | [검토 F1/F2](fault-packet-review.md) 유지. B1 도구 코드 차단은 해소. live P/T/F·관리 도달성은 해당 시험 직전 확정 |
| 12 | 시험 fixture/criteria·CA·도구 SHA·RUN·DB schema·H1·원본 연결 | #47/#50 재환/권욱 | 도구 버전/무결성 수신 완료, 실제 입력 대기. 기존 [16case](test-execution-matrix.tsv)는 모두 NOT_RUN |
| 13 | D21 canonical raw 편입 | #36 원본 보유자/권욱 | 원본8706bytes·기존 SHA256 수신/대조 완료. evidence PR161 HEAD162892f 독립 승인·CI 후 merge277893c, 17:05:38 KST 병합 완료. initiator/cleanup 별도 raw 미확인은 그대로 유지; Transport 결정 재개·OCI 재시험 없음 |
| 14 | 교육장 비용 리포트·운영/삭제/보존 창·Review 참석자/시각·일정 기록 정합 | #34/#52/#55 권욱/각 Lead | 이벤트별 절차·삭제/보존 책임·Review 의제 작성 완료. 보고금액·exact 창/참석자/시각 미정. 10/23 정리 목표가 Review 전 삭제 허가는 아님 |

17:50 KST 조회에서 full IAM/NAT 추가 PR과 하영의 리뷰 후속 정정은 미접수다. 먼저 우리 문서의 단계/상태 모순을 정정했으며 새 AWS 실행은 하지 않았다. #4의 10-13 Ready와 선행 G4 목표10-14 충돌은 담당자의 계획 정합화 대상으로 남긴다. exact 생성/삭제창은 미정이다.

2·4~8·11~14의 준비는 병렬 가능하다. 입력 대기 항목의 담당을 재배정하거나 미확정 값을 임의 작성해 통과시키지 않는다.

## Terraform Plan: 지금 완료한 준비와 실행 전 공백

검증한 최신 통합 소스는 `93d71500e3e881c55f1814cd144ca41f43e77f3d`이다. PR7 검토 HEAD와 network6/vpn10파일 및 기존 manifest가 일치한다. **이는 소스 무결성 수신이며 `accepted_execution_sha`/`accepted_execution_manifest`는 null**이다. 과거 PR6 checkout 또는 오래된 PR7 후보를 실행 소스로 자동 선택하지 않는다.

이번 수용된 NAT 설계를 구현하면 network 소스/권한·자원 수가 달라진다. 이전 `15 create`는 위 SHA의 과거 기대값일 뿐이다. NAT/EIP/default route/subnet tags와 의존성·삭제를 포함한 새 diff/manifest·Plan 기대표를 다시 수용해야 하며, 기존16파일 무결성이나 PR7 승인을 새 코드 승인으로 복제하지 않는다.

| 단계 | 사용할 기존 자료 / 선행 입력 | 완료·중단 기준 |
|---|---|---|
| 정책 접수 | [중앙 검증 인계](https://github.com/321Team/infra-terraform/blob/93d71500e3e881c55f1814cd144ca41f43e77f3d/docs/preflight-20261007/central-validation-handoff.md)의 full policy 최소 묶음 | 부분 backend/PassRole 정책만으로 INCOMPLETE 해제 금지. 새 AMI·provider read/cleanup coverage·소유 경계·simulation 입력 대조 |
| 중앙 검증 | 검토된 policy/trust SHA + 기존 승인 중앙 검증 세션, fresh before | ValidatePolicy/findings·변경 case simulation. 오류나 예상 밖 현재 설정이면 STOP. 검증 결과가 grant 완료는 아님 |
| 본인 권한 | 해당 grant/readback 후 [본인 U1](https://github.com/321Team/infra-terraform/blob/93d71500e3e881c55f1814cd144ca41f43e77f3d/docs/preflight-20261007/gwonuk-u1-plan.md) | 각 본인 MFA 역할·backend/lock·양성/음성·복구. 타인 세션 재사용 없음 |
| network saved Plan | 해당 Lead의 실제 source/manifest 수용·정책·입력·개인 FDS-IaC-Operator, [기존 Plan 절차](https://github.com/321Team/infra-terraform/blob/93d71500e3e881c55f1814cd144ca41f43e77f3d/docs/preflight-20261007/plan-runbook.md) | `terraform/network`, default workspace, `phase2/network/terraform.tfstate`. 93d7150 빈 state의 과거15create 기준을 NAT 추가본에 재사용하지 않음. 새 source/실제 state별 예상 create/update/delete 대조; 예상 밖 삭제/교체·중앙 자원 변경·오류면 STOP |
| Apply 이후 vpn Plan | 별도 Apply 판단 → 실제 network_handoff + 5의 명시 입력 | 합성 ID 사용 금지. route OFF 유지, actual worker/route 수용 시점 분리. network Plan에 ROSA 생성 후 ID를 선행조건으로 추가하지 않음 |

위 링크 안의 작성 당시 리뷰 대기/구 candidate SHA 문구는 이 수신 기록과 분리한다. 명령의 실제 실행 SHA는 해당 Lead 수용과 깨끗한 checkout 확인으로 고정하며 이 문서 자체를 실행 승인으로 소비하지 않는다. 명령·RC·원본은 개인 경로에 보존하고 state/plan/credential을 공개 기록에 넣지 않는다. 현재 AWS 읽기 재조회/ValidatePolicy/simulation/grant/Plan/Apply 전부 이번 회차 NOT_RUN이다.

## 유지하는 결정과 이후 단계

- 교육장 지원 확정, 자부담0, 목표USD400/중단450/상한500·예비50. 교육장 예상 총비용에 사용액을 다시 더하지 않는다. 지원 재확인·별도 Billing 접근·새 보고주기 요구 없음.
- 공용 OCP Team Code·Namespace·관리자 제약은 NONE_REPORTED. 실제 시험 target만 실행 전에 식별한다.
- G4 10/14 → G5 10/20 → G6 10/22 → Review/Freeze10/23 → Close10/26 유지. 10/9와 주말 비근무. Architecture Freeze와 10/23 결과 Freeze는 단계대로 구분한다.
- 사전 준비 후 Network 실행 → Relay/VPN·G4 → ROSA Basic Ready/D22/App Delivery·G5 → Hybrid/E2E·G6 → 증적 심사/발행·정리/종결이 남는다. G4 앞에 ROSA 실제 생성·cold-pull을 요구하지 않는다.

이번 목록 갱신은 GitHub 원본·관련 comment delta·Terraform/ROSA open PR·3개 저장소 고정 소스 대조 범위다. 개인 미게시 작업·전체 조직·AWS 실상태까지 확인했다고 주장하지 않는다. 본문/AC/Status/날짜/발행 정본은 수정하지 않는다. 준비 문서 변경 복구는 해당 커밋 revert이며 서버 원복 대상은 없다.
