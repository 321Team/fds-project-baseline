# GitHub Label and Type Schema

Version: 1.0 · 2026-09-10. 기존 실제 라벨 철자와 대소문자를 유지한다.

## Phase

| 본문 값 | Label |
|---|---|
| Design | `phase:design` |
| Phase 1 | `phase:phase-1` |
| Phase 2 | `phase:phase-2` |

## Priority

| 본문 값 | Label |
|---|---|
| P0 | `priority:P0` |
| P1 | `priority:P1` |
| P2 | `priority:P2` |

## Status

| 본문 값 | Label |
|---|---|
| Blocked | `status:blocked` |
| Cancelled | `status:cancelled` |
| Done | `status:done` |
| In Progress | `status:in-progress` |
| In Review | `status:in-review` |
| To Do | `status:to-do` |

## Type

| 본문 값 | Label |
|---|---|
| Change Request | `type:change-request` |
| Decision | `type:decision` |
| Milestone | `type:milestone` |
| Task | `type:task` |

## Category

대표 영역만 Label로 투영한다. 전체 Category는 본문에 보존한다. 임의 키워드 추론으로 새 area를 만들지 않는다.

| Category | Label |
|---|---|
| Application / Data / Interface | `area:application` |
| Application / Governance | `area:application` |
| Application / MSA | `area:application` |
| Application / OpenShift | `area:application` |
| Application Security / Demonstration / Governance | `area:security` |
| Architecture / DNS | `area:architecture` |
| Architecture / Hybrid Cloud | `area:architecture` |
| Architecture / Network | `area:architecture` |
| Architecture / Operator Supply Chain | `area:architecture` |
| Architecture / Registry | `area:architecture` |
| Automation / Configuration Management | `area:automation` |
| Automation / DNS Client | `area:automation` |
| Backup / OpenShift | `area:backup` |
| CI/CD / OpenShift Delivery | `area:cicd` |
| CI/CD / Supply Chain | `area:cicd` |
| Cloud / Terraform | `area:cloud` |
| Data / Database | `area:data` |
| DNS / Hybrid Integration | `area:dns` |
| DNS / Supporting Service | `area:dns` |
| DR / Data Recovery | `area:dr` |
| DR / Platform Recovery | `area:dr` |
| HA / Platform Resilience | `area:ha` |
| HA / Resilience | `area:ha` |
| Hybrid Integration | `area:hybrid-integration` |
| Hybrid Network / VPN | `area:hybrid-network` |
| Infrastructure / Load Balancer | `area:infrastructure` |
| Kubernetes / Platform | `area:kubernetes` |
| Linux / Network Baseline | `area:linux` |
| Milestone / Close | `area:milestone` |
| Milestone / Cloud & VPN | `area:milestone` |
| Milestone / Deliverable | `area:milestone` |
| Milestone / Design Freeze | `area:milestone` |
| Milestone / Hybrid Integration | `area:milestone` |
| Milestone / Hybrid Network | `area:milestone` |
| Milestone / Infrastructure | `area:milestone` |
| Milestone / Review | `area:milestone` |
| Milestone / Review Readiness | `area:milestone` |
| Milestone / ROSA Application | `area:milestone` |
| Milestone / Security & Feature | `area:milestone` |
| Milestone / Start | `area:milestone` |
| Monitoring / Architecture / Security | `area:monitoring` |
| Monitoring / Observability | `area:monitoring` |
| Network / Connectivity Validation | `area:network` |
| Network / Infrastructure Design | `area:network` |
| Network / Interface Change Control | `area:network` |
| OpenShift / ROSA | `area:openshift` |
| Operator Supply Chain | `area:operator-supply-chain` |
| PMO / Documentation | `area:pmo` |
| PMO / Review | `area:pmo` |
| QA / Hybrid E2E | `area:qa` |
| QA / Integration Test | `area:qa` |
| Registry / Supply Chain | `area:registry` |
| Schedule / Governance | `area:schedule` |
| Security / Governance | `area:security` |
| Security / Kubernetes | `area:security` |
| Security / PKI | `area:security` |

## 실제 Type과 fallback

Task, Decision, Milestone, Change Request는 본문의 업무 분류다. GitHub 조직에 같은 이름의 활성 Type이 실제 존재하고 쓰기 기능·권한이 확인될 때만 native Type에 적용한다. 라벨 설정은 native Type 설정의 증거가 아니다. 특히 Decision/Milestone/Change Request를 Task로 일괄 대체하지 않는다.

현재 64건 native Type=null. 그중 62건은 본문 Type이 확정되어 type 라벨로 표현 가능하고, #59/#61은 원본 미확인이다. 현재 연결 도구에는 native Type 쓰기가 없으므로 미반영 상태로 기록한다. Free 플랜에서 Type 자체가 불가능하다고 단정하지 않는다.

`metadata:needs-source`는 원본 속성 미확인 예외다. 미확인 값을 정식 Phase/Type/Priority로 등록하지 않는다. 기존에 없는 사전값 라벨은 사용 예정 정의일 뿐 자동 생성 대상이 아니다.

