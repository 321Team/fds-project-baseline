# FDS v3.1.17 Canonical Ticket Update Pack

> **Version:** v1.0  
> **As of:** 2026-09-04  
> **Authority:** D37 / `FDS_Project_Implementation_Baseline_v3.1.17.md`  
> **Purpose:** Notion·WBS·상태 레지스터 Upsert Source
> **Status:** RELEASED — 2026-09-07 정본. 개별 티켓 Runtime 상태는 각 레코드의 상태를 유지한다.

---

## 1. 적용 규칙

- 아래 티켓은 기존 Description 전체를 삭제하지 않고 명시된 속성과 Schedule Note를 갱신한다.
- `Done`은 Acceptance와 Evidence가 종결된 경우에만 사용한다.
- 개인 휴가는 팀 공통 Non-working Date로 등록하지 않는다.
- P1-LB Stage A PASS와 전체 Ticket Done을 구분한다.
- 개발 저장소 CR과 문서 정본 발행 상태를 분리한다.

## 2. Canonical Upsert Matrix

| ID | Status | Plan Start | Plan End | Lead | Support | Update |
|---|---|---:|---:|---|---|---|
| `P1-LB-01` | In Progress | 2026-08-27 | **2026-09-07** | 이권욱 | 이하영 | Stage A Technical/Evidence PASS, Stage B target aligned to G1; Runtime Pending |
| `P1-K8S-01` | In Progress | 2026-08-27 | 2026-09-04 | 이하영 | 이권욱 | 2026-09-03 Gate 0~2 착수 |
| `P1-DB-01` | In Progress | 2026-08-28 | **2026-09-07** | 이재환 | 이권욱 | 09-04 개인 휴가, 복귀 후 완료 |
| `P1-DNS-01` | **Done** | 2026-08-28 | **2026-09-03** | 이권욱 | 이하영 | Technical/Evidence/Support Review Closed |
| `P1-APP-01` | In Progress | 2026-09-01 | **2026-09-10** | 이재환 | 이하영 | 09-04 개인 휴가 반영, G2 유지 |
| `P1-MON-01` | In Progress | **2026-09-07** | 2026-09-11 | 이재환 | 이권욱 | Runtime Start를 복귀일로 이동 |
| `MS-G1-01` | To Do | **2026-09-07** | **2026-09-07** | 이권욱 | 이하영, 이재환 | P1-DB 완료일과 정렬 |
| `P1-SEC-01` | To Do | 2026-09-04 | 2026-09-11 | 이하영 | 이권욱, 이재환 | 09-04 이재환 Support 공백은 이권욱 커버 |
| `CR-P1-ANS-01-01` | **In Review** | 2026-09-04 | TBD | 이권욱 | 이하영 | `321Team/infra-ansible` PR #1 Open; Reviewer requested; Review 0 / CI 0 / Merge Pending |

## 3. Schedule Note — 붙여넣기 원문

### P1-LB-01

Stage A Listener/Source Allowlist/Node 6대·Runner Positive/ansible01 `.10` Negative/secure-transfer Evidence PASS(2026-09-03). Stage B 목표는 승인된 D36 G1 기준일 2026-09-07로 재기준선화한다. Bootstrap 후 Backend UP, Authenticated API, Failover/Recovery 검증은 Pending이므로 Status는 In Progress를 유지한다.

### P1-K8S-01

2026-09-03 착수. P1-LB-01 Stage A PASS Evidence를 인수해 Gate 0~2를 진행한다. SELinux Enforcing을 유지하고, Kubernetes Node의 firewalld는 Calico 설치 전에 비활성화한 뒤 named HostEndpoint/GlobalNetworkPolicy로 전환한다. D34 확정값을 적용한다.

### P1-DB-01

이재환의 2026-09-04 개인 휴가로 당일 작업 및 단독 종료를 배치하지 않는다. Plan End를 2026-09-07로 이동해 Lead 가용 작업일 6일을 보존한다.

### P1-DNS-01

기술 검증, k8s-api-lb01 `.109` ACL/Resolver/Failover Delta, Support Review가 완료되어 2026-09-03 Done으로 종결한다. Management DNS는 P1 N/A, Reverse/PTR은 N/A로 유지한다.

### P1-APP-01

이재환의 2026-09-04 개인 휴가를 반영해 Plan End를 2026-09-10으로 조정한다. 이하영이 기술 지원하며 G2 2026-09-11 목표는 유지한다.

### P1-MON-01

이재환의 2026-09-04 개인 휴가로 Runtime Plan Start를 2026-09-07로 이동한다. 사전 Metrics/Target 설계는 유지하고 이권욱 지원 아래 G2 2026-09-11 목표를 유지한다.

### MS-G1-01

P1-DB-01 Plan End와 정렬해 G1 Target을 2026-09-07로 이동한다. P1-DNS-01 Done 및 P1-LB-01 Stage A PASS를 반영하되 P1-LB Stage B와 나머지 G1 Runtime Evidence는 계속 필요하다.

### CR-P1-ANS-01-01

2026-09-04 기준 `321Team/infra-ansible` PR #1은 Open이며 Reviewer `hayeounglee`가 요청되어 있다. Head Commit은 `507d8882a04f53640b07251bcc234b7d6ee81c09`, Base/Main은 `98cf3f826ac0805bcc771ad760a15d931c1bd414`다. Review와 CI Status가 각각 0이므로 `In Review`를 유지하고 Merge·Runtime 완료를 선언하지 않는다.

## 4. 불변 사항

- G2 2026-09-11
- G3 2026-09-18
- Phase 1 Close 2026-09-23
- IF-11/IF-11A Source Allowlist 설계
- SELinux Enforcing 유지
- firewalld→Calico HostEndpoint 전환 원칙

**CANONICAL_TICKET_UPDATE_PACK_VERDICT=RELEASED**
