# D22 논리 결정 검토 패킷 및 후속 입력 — 2026-10-04
AI usage: CODEX_ASSISTED.
현재 작업 위치: 비공개 baseline PR137. PROPOSED / DECISION_NOT_RECORDED / FREEZE_HOLD.
최신 재조회: baseline #34/#38/#42 comments. 기존 책임·AC·일정을 유지한다.

## 1. 검토할 단일 권장안
기존 On-Prem Harbor를 P2 primary registry 후보로 유지하고, P2 pull principal은 P1과 분리하는 방안을 검토한다.
Runner push와 P2 node pull은 별도 actor로 관리한다. 생성 전 endpoint/CA/권한/source 규칙을 결정하고, 생성 후 실제 node-source 및 cold-pull 증적으로 최종 인수한다.
후보 수용만으로 계정 발급·Secret 갱신·HCP 설정·방화벽 변경·paid Create/Apply를 허용하지 않는다.

## 2. 확보값과 미확인 범위
| 입력 | 확보값/근거 | 남은 판단 |
|---|---|---|
| current leaf | [D22 1.3](20261004-harbor-d22-input-contract.md): pinned CA FQDN TLS 및 현장checksum USER_READBACK | raw 독립 수신/재해시, OS/각 runtime trust |
| P1 Robot | [D22 1.4](20261004-harbor-d22-input-contract.md): worker pull, push push+pull, fds범위, enabled, duration30 | P2 principal 발급/공유 정책 선택, 실제 인증/negative |
| 만료 | worker10-16 17:02:37, push10-18 17:16:55 KST | 10-12~13 기존 rotation 일정(안)의 실행창 확정·완료 |
| monitoring consumer | [consumer runbook](../runbooks/20261004-harbor-consumer-reference-readonly.md): source상 workload5개/SA/Secret 연결 | live workload/SA/Pod/Secret metadata 대조 |
| fds-app consumer | 기존 기대 SA transaction-api-sa / fds-engine-sa | 실제 Pod/SA와 harbor-pull-secret 연결 |
| Runner credential | 기존 robot$push actor 확인 | 실제 authfile/CI reference/실행사용자 결속 |
| 공개 CA | pinned Root PEM 및 hostname→PEM JSON 후보 | exact HCP version/CLI 지원·IP/FQDN endpoint 선택과 key 정합 |
| app image | P1 관측 digest와 승인 자원 baseline 존재 | 최종 build/scan/provenance/registry digest/P2 승인 연결 |

위 관측값은 2026-10-04 snapshot이며 이후 rotation/설정변경 시 다시 관측한다.

## 3. 실제 결정문 후보 — 아직 승인 아님
- primary: On-Prem Harbor 조건부 재사용.
- endpoint: harbor.fds.internal:443 권장 후보. 기존 IP 인증 consumer를 자동 전환하지 않는다. DNS/route와 secret registry key/CA JSON key를 함께 확정한다.
- project/repository: 기존 fds 및 승인 app repository만. repository별 final digest는 APP handoff 수신 후 고정.
- pull identity: P2 전용 pull-only principal 제안, namespace/SA 범위와 만료·보관 reference를 결정.
- push identity: 기존 Runner 책임 분리 유지. 새 권한 확대 없이 필요한 project 범위만.
- trust: 검토된 공개 CA를 selected HCP 방식에 맞게 사전 입력. insecure/TLS bypass 금지.
- source: node-pull source와 Pod egress를 별도 관측. 기존 IPsec envelope가 Runner 관리망 경로를 충족한다고 가정하지 않음.
- fallback: 자동 mirror/failover 없음. 신규 pull 실패 시 신규 rollout 중단, 정상 workload 및 이전 승인 digest 보존.
- cost: registry 경로 transfer·DNS·network·필요 mirror 총비용 포함. 실제 금액은 사용자10-06 이후 입력 전 null.
- final: Basic Ready 후 strict TLS/인증/negative/cold-pull/업무/복구 증적 수용으로 판정.

권욱 #42 Lead는 이 후보의 수용/수정/보류를 원 결정 위치에 기록한다. 이 파일 생성은 그 판단을 대신하지 않는다.

## 4. 지금 실행 가능한 순서
1. control01에서 기존 context를 확인하고 [조회 절차](../runbooks/20261004-harbor-consumer-reference-readonly.md) §2를 실행한다. Secret 값은 출력하지 않는다.
2. Runner에서 같은 절차 §3의 후보 파일 metadata만 확인한다. 실제 active authfile은 기존 IF09/CI 실행 방식과 결속하며 후보 파일 존재만으로 확정하지 않는다.
3. 결과로 D22 consumer 연결표를 채운다. 권한 부족은 기존 운영자 조회로 해소하고 RBAC를 신설하지 않는다.
4. platform producer의 selected HCP version/registry CA 입력/지원·capacity 입력을 연결한다. static 자료를 actual platform PASS로 바꾸지 않는다.
5. APP producer의 최종 동일 digest build→scan→registry→runtime 연결을 소비한다. 타 세션 P1 시험을 중복 수행하지 않는다.
6. 비용 텍스트 수신 후 한도/기간/as-of/누적/잔여운영·teardown 비용을 연결한다. 미확인 값0 처리 금지.

## 5. 완료 판정과 실패 처리
Consumer 조회 RC0는 메타데이터 조회 성공만 의미한다. 실제 credential rotation/pull/권한거부 PASS가 아니다.
조회에는 cluster write가 없으므로 실패 시 rollback은 없다. 오류 출력·실행위치·context를 확인한 뒤 해당 단계만 재조회한다.
rotation 전에는 각 consumer 교체순서, 이전 자격 즉시 무효화 여부, 안전 전달, 실패 복구, 승인 시험 digest를 확정한다.
기존 체계와 별개의 신규 승인 Gate/담당/기한을 만들지 않는다.

연결: [미확정 register](20261003-unresolved-design-register.md), [관리/DNS 계약](20261004-private-management-bidirectional-dns-contract.md), [D22 입력](20261004-harbor-d22-input-contract.md).
