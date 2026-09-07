# D35 — Interface Register Correction / IF-11A Approval Record v1.0

## 1. Record

| Field | Value |
|---|---|
| Decision ID | `D35` |
| Date | 2026-09-02 |
| Status | **Done / APPROVED** |
| Decision Type | Interface Contract Integrity / Source Allowlist Approval |
| Review Basis | `FDS_Interface_Full_Audit_v3.1.14_R1.md` |
| IF-11A Reviewer / Approver | 이하영 |
| Canonical Issuer / Project Lead | 이권욱 |
| Canonical Baseline | `FDS_Project_Implementation_Baseline_v3.1.15.md` |

## 2. Approval Evidence

| Evidence | SHA-256 | 판정 |
|---|---|---|
| `D35_IF-11A_Approval_Evidence_20260902.png` | `309105ad959635b289a344a2a3d55c6b30fead8a56b5805720d3ec028f77129b` | 이하영: “IF-11A(CP/Worker 6대 → API LB) 승인합니다.” |
| `FDS_Interface_Full_Audit_v3.1.14_R1.md` | `4edf12298d816f4344d0f782dee6c31e92fa219ea65b200469b86eb38c7ec744` | 25개 Canonical Interface 전수 점검 기준 |
| `FDS_IF-11A_Ticket_Impact_and_Verification_Record_v1.1.md` | `257644ec0a3baa882640ea5c5a6667208421eb992ed93e7fddb9302fd588f855` | 승인 반영 티켓별 영향성·검증 주체 정본 |

사용자의 “승인 완료 정본 발행” 지시를 Project Lead 이권욱의 정본 발행 승인으로 기록한다. 첨부 이미지는 IF-11A 설계 승인 Evidence이며 Runtime Test 결과가 아니다.

## 3. Decision

### 3.1 IF-11A 승인

| ID | Source | Destination | Protocol / Port | Purpose | Owner | Design State | Runtime State |
|---|---|---|---|---|---|---|---|
| IF-11A | K8s Node `.102/.103/.104/.105/.107/.108/32` | API LB `10.1.93.109` | TCP 6443 | kubeadm init/join 및 안정된 Control Plane Endpoint | 이권욱 / 이하영 | **FROZEN / APPROVED** | **NOT TESTED — Stage A 대기** |

IF-11A는 P1-K8S-01의 kubeadm Bootstrap에 필요한 설계 계약이다. 승인에 따라 API LB의 Source Allowlist에 6개 Node `/32`를 추가할 수 있다.

### 3.2 기존 IF-06A 보존

| ID | Source | Destination | Protocol / Port | Purpose | Design State | Runtime State |
|---|---|---|---|---|---|---|
| IF-06A | `monitor01 10.250.10.30/32` | API LB `10.1.93.109` | TCP 6443 | External Blackbox Probe | **FROZEN / PRESERVE** | P1-MON-01에서 검증 |

IF-11A 추가는 IF-06A를 대체하거나 제거하지 않는다. P1-LB-01은 `.30/32` Rich Rule을 보존하고, Stage A에서 Rule 존재·광역 Port 미개방을 확인한다. monitor01의 실제 Probe/장애복구 시험은 P1-MON-01 소유이므로 Stage A 완료 차단조건에는 포함하지 않는다.

### 3.3 Canonical Register 정정

- ICR v1.3 `IF-21`은 `IF-02`, `IF-22`는 `IF-06`에 병합한다.
- ICR v1.3 `IF-23`의 Prometheus 부분은 `IF-06`, Control Plane 부분은 `IF-12B`로 분리·정본화한다.
- `IF-24 Alertmanager → monitor01 Webhook`은 `RETIRED / P1 N/A`로 유지하고, D33의 `IF-06B Prometheus → monitor01:443 Remote Write`만 사용한다.
- `IF-05C` Prometheus→Alertmanager 9093, `IF-12A` etcd 2379~2380, `IF-12B` CP→kubelet 10250, `IF-12C` Node 간 VXLAN 4789, `IF-13A` Workload→CoreDNS 53을 Canonical Register에 추가한다.
- Phase 2 `IF-17~20`은 승인되지 않은 구현값으로 오인하지 않도록 `PROVISIONAL`로 표시한다.
- P1-HBR-01을 Project Status Register에 복원한다.

## 4. Stage A 판정 경계

현재 확인된 LB→CP `.102/.103/.104:6443`의 `Connection refused`는 **Route 도달 / kube-apiserver 미기동**으로 해석하며 Backend 사전 경로 PASS다. 다음 조건이 모두 충족되기 전에는 `Stage A PASS / Listener Ready`를 선언하지 않는다.

- API LB `10.1.93.109:6443` Listener·HAProxy·SELinux Enforcing 정상
- IF-11 Runner `.20/32`, IF-11A Node 6대, IF-06A monitor01 `.30/32` Rich Rule 존재 및 Zone-wide 6443 미개방
- Node 6대 → API LB Positive PASS
- Runner `.20` → API LB Positive PASS
- 미승인 ansible01 `.10` → API LB Negative PASS
- Evidence 01~19, `99_SHA256SUMS.txt`, Handoff Review와 Repository Commit ID 확보

Stage A PASS 전 상태는 다음과 같다.

| Item | State |
|---|---|
| P1-LB-01 | `In Progress` |
| Stage A | `Handoff Pending` |
| P1-K8S-01 Gate 0 Preflight | 실행 가능 |
| P1-K8S-01 kubeadm Bootstrap | **HOLD** |
| G1 Infrastructure Ready | `To Do` |

## 5. Ticket Impact / Verification Owner

| Ticket | 영향 | 현재 상태 | 구현 / 검증 주체 |
|---|---|---|---|
| P1-LB-01 | IF-11A·IF-06A Source Allowlist, Listener, Positive/Negative, Hash/Handoff | In Progress | 구현 이권욱 / 인수 이하영 |
| P1-K8S-01 | Stage A Evidence 인수 후 kubeadm, IF-11A Node Positive | To Do / Bootstrap HOLD | 이하영 / Network 지원 이권욱 |
| P1-MON-01 | IF-06A `.30/32` Probe 및 장애/복구 | In Progress | 이재환 / Network 이권욱 / Security 이하영 |
| P1-CICD-01 | IF-11 Runner `.20` Positive, API 인증 배포 | To Do | 이권욱 / 이하영 |
| P1-DNS-01 | API LB `.109` DNS ACL/Resolver delta | In Review / Technical PASS | 이권욱 / Support 이하영 |
| P1-SEC-01 | HEP/GNP와 Host Firewall 경계 회귀 | To Do | 이하영 / 이권욱 |
| ICR-D-NET-01-01 | Canonical IF 매핑·Calico/Route/IF-06B Runtime | In Progress | 이권욱 / 이하영 / 이재환 |
| P1-HBR-01 | IF-09 Push·IF-10 Pull·OID-02 Registry 결정 | To Do | Lead 이하영 / Support 이권욱 |

## 6. Non-impact / No Reopen

- D-SEC-01/D17/D34의 승인과 `MS-G0-01 / G0 FULL PASS`는 유지한다.
- D35는 설계 정합성 정정이며 D-SEC-01 또는 G0를 재개방하지 않는다.
- 설계 승인만으로 P1-LB-01 Stage A, P1-K8S-01, G1 또는 G2 Runtime 완료를 선언하지 않는다.

## 7. Release Result

| Item | Result |
|---|---|
| D35 | **PASS / Done** |
| IF-11A Design | **APPROVED / FROZEN** |
| IF-06A | **PRESERVED** |
| Canonical Baseline | **v3.1.15 RELEASED** |
| Runtime | **CONDITIONAL / Evidence Pending** |
