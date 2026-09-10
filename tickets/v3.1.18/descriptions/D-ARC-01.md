<!-- fds-canonical-description:v3.1.18 record-id:D-ARC-01 -->
# D-ARC-01 — Phase 1 Logical / Physical Architecture Design Freeze

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | D-ARC-01 |
| Phase | 원본 속성 미확인 |
| Category | 원본 속성 미확인 |
| Type | 원본 속성 미확인 |
| Status | Done |
| Priority | 원본 속성 미확인 |
| Start | 원본 속성 미확인 |
| End | 원본 속성 미확인 |
| Calendar Days | 원본 속성 미확인 |
| Working Days | 원본 속성 미확인 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Logical / Physical Architecture v3.1.2 Freeze, MSA / CI-CD / Monitoring / Security 경계 확정, IP·배치 정합성 확인, Release / Freeze / 승인 메타데이터 반영 |
| Related Decision IDs | D01`~`D09`, `D12`~`D16 |
| Related Risk IDs | RISK-02`, `RISK-04`, `RISK-06`, `RISK-07`, `RISK-08`, `RISK-09 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #59 snapshot 2026-09-09T12:15:20Z |
| Schedule Note | 원본 속성 미확인 |

## 현재 실행·검토 상태

D-ARC-01 Done/2026-08-26 유지. FUP-06 후보 원본 편입과 수용은 완료됐으나 개인별 과거 승인 회신·시각 참조 한계는 유지한다. 현재 Issue의 Phase/Type/일정 등 원본 미확인 속성은 추정하지 않는다.

근거: [Issue #59](https://github.com/321Team/fds-project-baseline/issues/59), Issue 갱신 시각 `2026-09-09T12:15:20Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

# User Story

Architecture 담당자로서 Phase 1의 Logical Architecture와 8대 Windows/VMware 기반 Physical Architecture를 단일 기준으로 설계·동결한다.

이를 통해 Kubernetes, Network, CI/CD, Application, Data, Monitoring 및 Security 영역의 경계와 연결관계를 명확히 하고, 후속 구축 티켓이 동일한 배치·IP·Interface 계약을 기준으로 구현과 검증을 수행하도록 한다.

---

# Scope

## In Scope

- Phase 1 External, Management, Physical FDS Network 및 Kubernetes Cluster의 논리 경계 정의
- 3 Control Plane + 3 Worker Kubernetes 배치와 API Load Balancer 경로 정의
- `transaction-api`와 `fds-engine`의 2-Service MSA 및 PostgreSQL 연계 정의
- GitHub Actions / Self-hosted Runner / Harbor / Kubernetes Deploy의 CI/CD 경계 정의
- Prometheus의 Node, Kubelet, Application 및 FDS Metrics 수집 경로 정의
- Business Namespace의 Default Deny, Required Allowlist, RBAC, non-root 및 seccomp 보안 경계 정의
- 8대 Physical Host와 Management, Kubernetes, Edge, Registry, Database, DNS, VPN VM/Service 배치 정의
- Physical `10.1.93.0/24`, Management `10.250.10.0/24`, VMnet8 `192.168.10.0/24`의 역할과 연결관계 정의
- 주요 Endpoint, Port, Source Preservation, Return Route 및 외부 조건부 NAT 경계 정의
- Logical / Physical Architecture Release, Freeze Ticket, Freeze Date 및 승인 상태 메타데이터 확정

## Out of Scope

- VM, Kubernetes, Application, Database, Monitoring 또는 Security Policy의 실제 구축·운영 완료
- 개별 Network 경로의 현장 검증 — `D-NET-01`에서 수행
- 개별 WBS, Backlog 및 Interface 상태관리 — `D-WBS-01`에서 수행
- `D-SEC-01`의 승인권자·검토 범위·Exit Criteria 결정 — Lead 이하영은 확정
- Phase 2 OCI / AWS / ROSA 상세 Logical / Physical Architecture

---

# 핵심 요구사항

- [x] Physical Host 8대의 공통 Baseline을 Intel Core i5-13400, RAM 64GB, SSD 932GB, Windows + VMware Workstation Pro로 정의한다.
- [x] Kubernetes Cluster를 Control Plane 3대와 Worker 3대로 구성한다.
- [x] `k8s-api-lb01(10.1.93.109:6443)`에서 Control Plane `.102/.103/.104:6443`으로 연결되는 API 경로를 정의한다.
- [x] Worker `.105/.107/.108`에서 `harbor01(10.1.93.54:443)`로 연결되는 Image Pull 경로를 정의한다.
- [x] Client → `edge01` → `transaction-api` → `fds-engine`의 서비스 요청 경로를 정의한다.
- [x] `transaction-api` → `db01(10.1.93.55:5432)`의 Transaction / FDS Result 저장 경로를 정의한다.
- [x] `cicd-runner01(10.250.10.20)`의 GitHub, Harbor 및 Kubernetes API 배포 경로를 정의한다.
- [x] `monitor01(10.250.10.30)`의 Node `9100`, Kubelet `10250`, Application `8000`, FDS `8001` Metrics 경로를 정의한다.
- [x] Management VM의 Source `.10/.20/.30`이 Physical FDS Network에서 보존되는 구조를 정의한다.
- [x] 모든 Physical FDS VM의 `10.250.10.0/24 via 10.1.93.58` Return Route와 내부 Source NAT 금지를 명시한다.
- [x] `VMnet8`에는 FDS Workload VM NIC를 연결하지 않는 Isolation Rule을 정의한다.
- [x] `.56/.57/.59` Reserved 및 `.100/.101/.106` DO_NOT_USE 조건을 Logical / Physical Architecture에 반영한다.

---

# Acceptance Criteria

- [x] Logical Architecture v3.1.2에 External, Management, Physical FDS Network 및 Kubernetes 경계가 구분되어 있다.
- [x] Physical Architecture v3.1.2에 server01~08의 Windows Host IP와 주요 VM / Service 배치가 반영되어 있다.
- [x] Kubernetes 3CP + 3Worker, API LB, Harbor, PostgreSQL, Edge 및 DNS P1 배치가 두 Architecture 간에 일치한다.
- [x] `transaction-api` / `fds-engine` 2-Service MSA와 PostgreSQL 저장 흐름이 표현되어 있다.
- [x] GitHub Actions → Runner → Harbor → Kubernetes Deploy의 CI/CD 경계가 표현되어 있다.
- [x] Prometheus의 Infrastructure 및 Application / FDS Metrics 경로가 표현되어 있다.
- [x] Default Deny, Required Allowlist, RBAC, non-root 및 seccomp의 Security Boundary가 표현되어 있다.
- [x] Physical, Management, VMnet8 Subnet과 Return Route, Source Preservation, NAT 금지 및 IP 예외가 Network Baseline v2.3과 일치한다.
- [x] 두 Mermaid 원본에 `Release: v3.1.2`, `Freeze Ticket: D-ARC-01`, `Freeze Date: 2026-08-26`, `Status: APPROVED / DONE` 메타데이터가 기록되어 있다.
- [x] Implementation Baseline v3.1.3의 Configuration-controlled Deliverables와 Project Status Register에 D-ARC-01 종결 근거가 반영되어 있다.

---

# 검증 및 증적

- `FDS_Phase1_Logical_Architecture_v3.1.2.mmd`
  - External / Management / Physical / Kubernetes 논리 경계
  - Application / Data / CI-CD / Monitoring / Security 흐름
  - Source Preservation, Return Route, NAT 및 IP 예외 Note
- `FDS_Phase1_Physical_Architecture_v3.1.2.mmd`
  - server01~08 Physical Host 및 VM / Service 배치
  - VMnet0 / VMnet1 / VMnet8 연결관계
  - Return Route, 내부 Source NAT 금지 및 IPAM 예외
- `FDS_Project_Implementation_Baseline_v3.1.4.md`
  - Configuration-controlled Deliverables
  - Physical Resource / Placement
  - Application / CI-CD / Monitoring / Security 기준
  - Gate Exit Criteria 및 Project Status Register
- Consistency Source: `FDS_Network_Baseline_v2.3`

---

# Dependency

- **Blocked By:** 프로젝트 핵심 설계결정 `D01`~`D09`, `D12`~`D16`
- **Blocks / Next:** `D-NET-01`, `D-WBS-01` 및 Phase 1 Remaining Backlog의 구현·검증
- **Related Ticket:** `D-NET-01`, `D-WBS-01`, `D-SEC-01`, `P1-K8S-01`, `P1-APP-01`, `P1-SEC-01`, `P1-CICD-01`, `P1-MON-01`
- **Milestone Contribution:** G0의 Architecture / Network / WBS 항목 중 Architecture `PASS`

---

# Decision / Risk Control

- **Related Decision IDs:** `D01`~`D09`, `D12`~`D16`
- **Decision Control:** 3인·8 Server·CentOS 10, Kubernetes 3CP + 3Worker, 2-Service MSA, External PostgreSQL / Harbor, Bridged Endpoint, DNS P1 경계 및 Network 분리·Route·IP 예외 결정을 Architecture에 반영한다.
- **Related Risk IDs:** `RISK-02`, `RISK-04`, `RISK-06`, `RISK-07`, `RISK-08`, `RISK-09`
- **Risk Control:** Architecture는 Shared L2 / 비관리 Gateway, TLS Trust, Security Allowlist, 외부 GitHub 의존성 및 단일 PostgreSQL 경계를 표시한다. 실제 완화조치와 Positive / Negative / Recovery 검증은 해당 구현 티켓의 Exit Criteria와 Evidence로 관리한다.
- **Change Control:** Freeze 이후 Component, Placement, IP, Endpoint, Port, Protocol, Security Boundary 또는 Producer / Consumer 관계 변경은 Architecture / Interface Change Request와 영향도 검토 후 새 Version으로 반영한다.

---

# Completion Record

- **Result:** `PASS`
- **Status:** `DONE`
- **Ticket Gate:** `CLOSED`
- **Exit Criteria:** Logical / Physical Architecture v3.1.2 Freeze, MSA / CI-CD / Monitoring / Security 경계 확정, IP·배치 정합성 확인, Release / Freeze / 승인 메타데이터 반영
- **Completed Date:** `2026-08-26`
- **Reviewer / Approver:** Architecture v3.1.2 및 Implementation Baseline 승인 기록 참조
- **Closure Basis:** `FDS_Phase1_Logical_Architecture_v3.1.2.mmd`, `FDS_Phase1_Physical_Architecture_v3.1.2.mmd`, `FDS_Project_Implementation_Baseline_v3.1.4.md`
- **Closure Boundary:** 본 티켓의 종결은 Phase 1 Architecture 설계 동결을 의미하며 개별 구성요소의 구현 완료를 의미하지 않는다. `D-SEC-01`은 `IN PROGRESS / Lead 이하영`, 관련 `D17`은 Scope·Approver·Exit Criteria 검토 중이며, G0 Design Freeze는 `CONDITIONAL PASS`다.
- **Next:** `D-NET-01` / `D-WBS-01` 완료 이력 유지 및 Phase 1 Remaining Backlog 실행

## 담당자 속성 복원 근거 (2026-09-09)

`FDS_Project_Implementation_Baseline_v3.1.2.md` §3.1 Frozen WBS의 해당 Record ID 행에서 Lead 이권욱 / Support 이하영, 이재환을 확인했다. 본문 17개 속성 항목을 유지하고 Lead·Support만 복원했다. Type의 원본 값은 해당 표에 없어 `원본 속성 미확인`을 유지한다. 이후 정본의 완료 이력과 충돌하는 과거 D-SEC/G0 상태는 이번 복원의 근거로 사용하지 않았다.
