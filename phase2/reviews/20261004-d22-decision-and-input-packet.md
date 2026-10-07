# D22 논리 결정 검토 패킷 및 후속 입력 — 2026-10-04
AI usage: CODEX_ASSISTED.
현재 작업 위치: 비공개 baseline PR137. PROPOSED / DECISION_NOT_RECORDED / FREEZE_HOLD.
최신 재조회: baseline #34/#38/#42 comments. 기존 책임·AC·일정을 유지한다.

2026-10-08 현재 소비 기준: [Phase 2 결정 패킷](../preparation/20261008/decision-packet.md)의 D22 단계 계약을 따른다. 아래 10/4~5 관측·PENDING은 이력이며 새 실행 상태로 복제하지 않는다. 교육장 지원은 확정이고 사용액·예상 총비용은 교육장 리포트 기준이다. 본 문서의 자체 견적/비용 입력 대기 표현보다 이 기준이 우선한다. 새 APP Build/Scan 성공과 원격 Push·승인 digest·ROSA Runtime 미완료를 구분한다. P1 Harbor/CICD 수정·실행·인수는 이번 범위에서 제외한다.

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
| monitoring consumer | [consumer runbook](../runbooks/20261004-harbor-consumer-reference-readonly.md): source상 workload5개/SA/Secret 연결 | 1.6 현장 대조 확보: workload5/Pod7/Secret2; 실제 pull·Ready 별도 |
| fds-app consumer | 기존 기대 SA transaction-api-sa / fds-engine-sa | 1.6 현장 연결 확보: workload2/Pod6/Secret1; 내부 credential 별도 |
| Runner credential | 기존 robot$push actor 확인 | /run/user/1000/containers/auth.json owner/mode600 확인; 실제 CI binding 미확인 |
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
- cost: 선택 경로를 교육장 리포트의 보고 범위와 연결하고 사용액·예상 총비용을 기존 한도와 비교. 실제 미수신 금액은 null, 자체 별도 견적 제출을 필수로 만들지 않음.
- final: Basic Ready 후 strict TLS/인증/negative/cold-pull/업무/복구 증적 수용으로 판정.

권욱 #42 Lead는 이 후보의 수용/수정/보류를 원 결정 위치에 기록한다. 이 파일 생성은 그 판단을 대신하지 않는다.

## 4. 지금 실행 가능한 순서
2026-10-04 17:55 control01 및 Runner 사용자 출력 수신으로 아래 1~3의 참조 조회·연결표 반영을 완료했다(USER_READBACK). 동일 조회를 반복하지 않는다. 다음은 Runner active credential reference 확인과 platform/APP 입력 연결이다. 상세 범위는 D22 입력1.6 참조.
1. control01에서 기존 context를 확인하고 [조회 절차](../runbooks/20261004-harbor-consumer-reference-readonly.md) §2를 실행한다. Secret 값은 출력하지 않는다.
2. Runner에서 같은 절차 §3의 후보 파일 metadata만 확인한다. 실제 active authfile은 기존 IF09/CI 실행 방식과 결속하며 후보 파일 존재만으로 확정하지 않는다.
3. 결과로 D22 consumer 연결표를 채운다. 권한 부족은 기존 운영자 조회로 해소하고 RBAC를 신설하지 않는다.
4. platform producer의 selected HCP version/registry CA 입력/지원·capacity 입력을 연결한다. static 자료를 actual platform PASS로 바꾸지 않는다.
5. APP producer의 최종 동일 digest build→scan→registry→runtime 연결을 소비한다. 타 세션 P1 시험을 중복 수행하지 않는다.
6. 교육장 리포트 수신 후 원본/기간/as-of/통화/사용액/예상 총비용을 연결한다. 총비용 중복 가산·미확인 값0 처리 금지.

## 5. 완료 판정과 실패 처리
Consumer 조회 RC0는 메타데이터 조회 성공만 의미한다. 실제 credential rotation/pull/권한거부 PASS가 아니다.
조회에는 cluster write가 없으므로 실패 시 rollback은 없다. 오류 출력·실행위치·context를 확인한 뒤 해당 단계만 재조회한다.
rotation 전에는 각 consumer 교체순서, 이전 자격 즉시 무효화 여부, 안전 전달, 실패 복구, 승인 시험 digest를 확정한다.
기존 체계와 별개의 신규 승인 Gate/담당/기한을 만들지 않는다.

연결: [미확정 register](20261003-unresolved-design-register.md), [관리/DNS 계약](20261004-private-management-bidirectional-dns-contract.md), [D22 입력](20261004-harbor-d22-input-contract.md).

## 6. Runner source 대조 후 다음 작업 정정
2026-10-04 18:30 이후 [D22 입력1.7](20261004-harbor-d22-input-contract.md)에서 current infra-cicd main Push adapter 미구현과 IF09 authfile 격리 미확정을 확인했다.
현재 파일 존재 확인을 반복하거나 운영 credential 교체로 진행하지 않는다. 다음은 기존 P1 담당 구현 경로에서 명시적 authfile/cleanup 격리 보완 및 독립 리뷰를 연결하는 것이다. P2는 해당 source/runtime handoff를 소비하며 타 세션의 코드 변경·시험을 중복하지 않는다.
비용 입력 대기와 별개로 D22 논리 결정안·platform 지원/capacity·APP approved digest 입력 연결은 계속 가능하다. 이 문서는 신규 권한/실행창/승인을 부여하지 않는다.


## 7. P1 진행 중 APP 입력 소비와 검증 준비 — 2026-10-04 후속
[APP Lead 최신 보고](https://github.com/321Team/fds-project-baseline/issues/43#issuecomment-5980505812)는 P1 진행 중 환경의 snapshot이다. P1/Phase2 인수나 최종 P2 이미지 승인을 의미하지 않는다. [resource-fit §10](20261003-resource-fit-recommended-design.md)과 [capacity 파생값](../inputs/20261004-app-capacity-derived.json)에 반영했으며 동일 자료 재수집을 요청하지 않는다.

| 입력 | 현재 소비 가능 | 미확인 / P2 소비 조건 |
|---|---|---|
| current P1 image | transaction-api a7093136…, fds-engine5e2a081c…의 보고된 full digest | 최종 P2 build/scan/provenance/digest 승인과 별도. source↔live 미검증 |
| 자원/rollout | 각3replica·250m/256Mi request, 25% surge/unavailable; 산술표 확보 | 실제 HCP 예산/N-1/종료 중첩·배치/PDB |
| SA/보안 | transaction-api-sa/fds-engine-sa, token automount=false·제한 securityContext | fixed UID10001/GID999를 P2에서 그대로 허용한다고 가정하지 않음 |
| service/probe | TA8000/metrics9091, engine8001/metrics9090, /livez·/readyz | engine grpc라는 이름과 HTTP 의미 대조; P2 edge/Route 선택은 별도 |
| secret/storage | DATABASE_URL 참조 존재, 보고상 두 앱 PVC/volumes 없음 | 값/credential 수집 없음. P2 DB secret reference·trust·network 및 platform storage 별도 |
| 배포 소스 | 현장 요약 및 repo 참고본 | 권위 portable base 미확보를 숨기지 않음. 현장 report를 그대로 deployable YAML로 생성하지 않음 |

준비할 수 있는 기대값:
- strict DNS→FQDN TLS→승인 P2 pull-only 인증→exact approved digest cold-pull 연결. 사전 캐시 hit를 cold-pull PASS로 표시하지 않는다.
- 승인 SA/namespace와 제한 보안조건에서 arbitrary UID·읽기 전용 rootfs·필요 쓰기경로·probe·업무 동작을 검증. 미확인 쓰기경로를 임의 volume으로 해결하지 않는다.
- 잘못된 CA/비승인 source·credential/권한 밖 push는 거부돼야 한다. 실제 negative 시험은 해당 환경/창의 승인 조건 후 수행.
- 신규 rollout/pull 실패 시 이전 정상 workload/digest 보존, 자동 mirror·재빌드·tag fallback 없음.
이번에는 시나리오/입력 경계만 작성했다. P1 Robot/Secret/CA/CI authfile/운영 이미지 변경·실제 pull·Pod 생성 없음. 기존 P1 생산·검토 세션의 결과를 소비하며 별도 중복 구현하지 않는다.


## 8. 공급·Delivery source 연결 — 2026-10-05
[플랫폼·이미지 handoff §2~5](20261005-platform-image-handoff.md)에 현재 소스와 입력 소비 범위를 구체화했다.
CI PR45/46은 병합됐으나 Runtime adapter NOT_INTEGRATED / Push·Deploy NOT_EXECUTED 범위다. §6의 운영 Push adapter/authfile 잔여를 해결 완료로 바꾸지 않는다.
P1 live digest와 현재 apko Dockerfile을 같다고 가정하지 않으며 source→build→scan→remote digest→P2 runtime을 결속해야 한다. #110의 운영 전환 이관안은 #30 수신 확정과 별도다.
기존 generic admission 도구/CI 결과를 실제 P2 namespace·SA·endpoint·audience·UID 동작으로 자동 승계하지 않는다. 추가 계정·Secret·CA·manifest 적용 없음.
