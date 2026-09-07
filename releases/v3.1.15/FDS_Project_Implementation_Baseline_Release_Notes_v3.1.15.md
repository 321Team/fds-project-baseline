# FDS Project Implementation Baseline v3.1.15 — Release Notes

## Release

| Field | Value |
|---|---|
| Version | `v3.1.15` |
| Release Date | 2026-09-02 |
| Release Type | Interface Contract Integrity / IF-11A Approval |
| Decision | `D35` |
| Status | **RELEASED** |
| Previous Canonical | `FDS_Project_Implementation_Baseline_v3.1.14.md` — SUPERSEDED, 이력 보존 |
| Canonical Issuer | 이권욱 |

## Approval

- 이하영이 `IF-11A CP/Worker 6대 → API LB` 설계를 승인했다.
- 이권욱이 v3.1.15 정본 발행을 승인했다.
- 승인 Evidence와 SHA-256은 `D35_Interface_Register_Correction_and_IF-11A_Approval_Record_v1.0.md`에 고정했다.

## Canonical Changes

- IF-11A Node 6대 `.102/.103/.104/.105/.107/.108/32 → API LB .109:6443`를 `FROZEN / APPROVED`로 추가했다.
- IF-06A monitor01 `.30/32 → API LB .109:6443`를 Source Allowlist에 보존했다.
- Kubernetes/Monitoring 필수 계약 IF-05C, IF-12A, IF-12B, IF-12C, IF-13A를 Register에 추가했다.
- ICR의 중복 IF-21/22/23을 IF-02/06/12B로 병합하고 IF-24를 `RETIRED / P1 N/A`로 확정했다.
- Phase 2 IF-17~20을 `PROVISIONAL`로 정정했다.
- Interface의 Design State와 Runtime Evidence State를 분리했다.
- Management DNS `.10/.20/.30`은 IF-13M/OID-04로 분리하고 결정 전 미구현 상태를 유지했다.
- Project Status Register에 P1-HBR-01을 Lead 이하영 / Support 이권욱으로 복원했다.

## Runtime / Gate Boundary

| Item | Release State |
|---|---|
| D35 / IF-11A Design | Done / Approved |
| D-SEC-01 / G0 | Done / FULL PASS 유지, 재개방 없음 |
| P1-LB-01 | In Progress |
| P1-LB Stage A | Handoff Pending |
| P1-K8S Gate 0 Preflight | 실행 가능 |
| P1-K8S kubeadm Bootstrap | **HOLD — Stage A PASS Evidence 전** |
| G1 / G2 | To Do / Runtime Evidence 필요 |

LB→CP `.102/.103/.104:6443`의 `Connection refused`는 Pre-bootstrap 경로 도달 PASS이지만 Listener Ready 전체 PASS가 아니다. Node 6대·Runner Positive, ansible01 `.10` Negative, IF-11/11A/06A Rule, Listener, SHA256/Handoff Evidence가 모두 필요하다.

## Superseded Artifacts

- Baseline v3.1.14 → v3.1.15
- Stage A Build Guide v1.2 → v1.3
- Stage A Completion Pack v1.0 → v1.1
- ICR-D-NET-01-01 v1.3 → v1.4
- Canonical Ticket Update Pack v3.1.14 → v3.1.15
- IF-11A Ticket Impact Record v1.0 → v1.1

기존 발행본은 삭제하거나 덮어쓰지 않고 이력으로 보존한다.

