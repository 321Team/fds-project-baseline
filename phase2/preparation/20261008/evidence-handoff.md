# D21·Gate·최종 정리 증적 인계 준비

CODEX_ASSISTED. 실제 원본을 대신하는 문서가 아니다. Phase 1 작업은 제외한다.

## D21 publication 접수

[#36 권위 기록](https://github.com/321Team/fds-project-baseline/issues/36)의 결정은 FINAL / OCI Primary NO-GO / AWS EC2+EIP Libreswan Relay 선택이다. 재선택이나 새 OCI 시험은 불필요하다.

| 접수 대상 | 알려진 기준 | 이번 실제 상태 |
|---|---|---|
| canonical responder raw | d21-ike-observer-20261003T042646Z.log / 8706 bytes / SHA256 e5f754a3d66c6fe452605ff914a6294e87aa85bf6a345ec0fadb981f18745cb0 | 이 작업의 조회한 로컬 준비 경로에 원본 없음. 새 수신·재해시 미수행 |
| 결정·인계 | #36 final 블록과 #34/#35/#37 연결, source/시각/실행자/명령/RC, cleanup 근거 | 기존 기록을 참조. source 없는 실행 필드는 추정하지 않음 |
| candidate 변경 | D21 당시 AMI와 PR7 Stream9 e4ee0bf가 다름 | 원본 역사 AMI를 바꾸지 않고 새 검토/수용 기록으로 연결 |
| publication | evidence/P2-OCI-01/에 원본+manifest+한계+결정/consumer refs | 원본 없이 evidence PR/합성 로그를 생성하지 않음. independent review와 merge 잔여 |

원본이 도착하면 size/SHA를 먼저 비교하고 원본 그대로 보존한다. 불일치/민감정보가 있으면 공개 게시를 멈추고 원본·공개용 사본을 구분한다. 실제 IKE_AUTH 도달/불일치 PSK 응답은 production SA·Tunnel 인수 증적이 아니다. 권욱 실행/생산 결과의 독립 증적 심사는 하영/재환 등 기존 정책에 따른다.

## Gate 소비표

| Gate | 필수 실제 입력 | 지금의 준비 / 최종 판단 책임 |
|---|---|---|
| G4 #39 / 10-14 | #35 Full IaC 실제 ID·Plan/Apply, D21, #37 Relay/SA/route/security/승인 TCP/negative/recovery, #38 생성 선행 입력·비용 | 기존 [PR152](https://github.com/321Team/fds-project-baseline/pull/152)의 G4 표 재사용. 이권욱. ROSA Cluster Ready를 G4 전에 요구하지 않음 |
| G5 #45 / 10-20 | #38 Full security/SCC·UID/RBAC/NP, #43 App, #46 정상 Delivery·실패차단, #42 D22 Final, P1 결정상태 | 기술 Lead 이하영, PMO/QA 이권욱. source→remote digest→runtime imageID, evidence review/merge 대조 |
| G6 #53 / 10-22 | #47 exact Hybrid handoff와 #50 Final E2E/Regression | 이권욱. 실제 ROSA→On-Prem 증적, Critical·Known Issue·미충족을 구분 |
| #49/#54/#56 / 10-23 | 동일 immutable candidate set, Decision/Known Issue·source/evidence/manifest·비용/정리 상태 | 이권욱. Lab/ROSA 분리, 미병합 evidence·미승인 CR을 완료로 올리지 않음 |

새로운 시험 없이 'PASS'를 채우는 체크리스트가 아니다. 생산 티켓의 최신 raw/commit을 소비하고 hash 무결성·STATIC/MOCK/CI/Runtime·REVIEW/MERGE/PUBLICATION을 구분한다.

## 운영·삭제·Review 준비의 최소 완료조건

기존 [Terraform 운영·정리안](https://github.com/321Team/infra-terraform/blob/work/p2-preflight-plan-20261007/docs/preflight-20261007/operating-teardown-plan.md)을 사용한다. 실제 작업창은 미정이며 문서에 적힌 시작/종료 시간은 제안이다.

1. 자원별 owner·실제 ID/state·삭제/보존·의존 순서·복구 가능 상태와 증적 수신 여부를 정한다.
2. ROSA 정상 삭제 및 의존 자원 확인 → 승인된 vpn/network 삭제 plan 순서. CFn bootstrap/backend/state/evidence·공용 IAM/SLR은 기본 삭제 대상이 아니다.
3. account Session document의 prevent_destroy/중앙 소유를 존중한다. 일괄 destroy·임의 state rm/target 우회 없음.
4. 실제 삭제 완료시각과 EIP/EBS/snapshot/ENI/LB/NAT/endpoint 등 잔존 사유·Owner를 연결한다. 교육장 리포트의 후행 사용액/예상 총비용으로 비용을 추적한다.
5. 10-23 Review 시간·참석자 미정. 10-26 Close에는 승인된 Review Action·정리·잔여 Owner/Due·sign-off를 소비한다. 이 패킷이 Freeze/Review/Close를 승인하지 않는다.

조건부 DNS/Operator/OADP/GitOps/Compliance/RHOAI는 해당 Lead의 Go/No-Go/Deferred·근거/Owner·재검토 조건을 연결한다. 실제 구현 완료가 P0 필수인 것처럼 Gate를 추가하지 않는다.
