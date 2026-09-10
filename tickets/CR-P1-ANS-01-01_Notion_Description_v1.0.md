# CR-P1-ANS-01-01 · Kubernetes Node DNS Resolver Automation

## Notion / WBS 속성

| 속성 | 값 |
|---|---|
| Record ID | `CR-P1-ANS-01-01` |
| Phase | Phase 1 |
| Category | Automation / DNS Client |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-04 |
| End | 2026-09-07 |
| Calendar Days | 4 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | 6개 노드 Resolver 자동화·기능·회귀·멱등성·Rollback·증적·Support Review 완료 |
| Related Decision IDs | D08; D09; D34; D35 |
| Related Risk IDs | RISK-02; RISK-04; RISK-07 |
| Source | Baseline v3.1.17; `321Team/infra-ansible` PR #1; 승인 HEAD `507d8882a04f53640b07251bcc234b7d6ee81c09`; Merge `4f9bdb7c08704eebb3d1b294751e51b0721b6af4` |
| Schedule Note | 2026-09-07 구현·검토·수동 병합 완료. GitHub Actions `NOT RUN`. v3.1.18 정본 후보에 동기화하며 후속 Gate는 자동 승인하지 않음. |

## 🎯 User Story

운영 담당자로서 Kubernetes 6개 노드의 DNS Resolver를 승인된 `dns01(10.1.93.52)` 우선, `dns02(10.1.93.53)` 보조 순서로 일관되게 구성하고 싶다. 이를 통해 `fds.internal`, 외부 DNS 및 Kubernetes 관련 서비스의 이름 해석을 반복 가능하고 복구 가능한 방식으로 유지한다.

## 📌 Scope

### In Scope

- 3개 Control Plane과 3개 Worker, 총 6개 노드의 Resolver 자동화
- `dns01(.52) → dns02(.53)` 순서 및 `fds.internal` 검색 도메인 적용
- FQDN·short name·외부 DNS·DNS 서버 직접 질의 검증
- kubelet·containerd 서비스 회귀 확인
- Check Mode, 멱등성, Rollback 및 재적용 검증
- 실행 증적, SHA-256, Support Review, 승인 HEAD와 Merge Commit 기록

### Out of Scope

- Kubernetes API 인증 완료
- P1-LB-01 Stage B 완료
- kubeadm init/join 및 클러스터 구성 완료
- ICR-D-NET-01-01 Runtime 완료
- GitHub Actions가 실행되지 않은 상태에서의 CI PASS 선언

## 📋 핵심 요구사항

1. 승인된 6개 노드만 대상으로 실행한다.
2. Resolver 순서는 `.52`를 Primary, `.53`을 Secondary로 고정한다.
3. `fds.internal` FQDN 및 short name을 모두 확인한다.
4. 외부 DNS와 두 DNS 서버에 대한 직접 질의를 확인한다.
5. kubelet과 containerd의 가용성 저하가 없어야 한다.
6. 동일 구성의 재실행은 변경 0건이어야 한다.
7. Rollback 및 재적용 절차와 결과를 증적으로 보존한다.
8. 증적의 원본성과 SHA-256을 확인하고 Reviewer 승인을 기록한다.

## ✅ Acceptance Criteria

- [x] Control Plane 적용: 2/2 노드 성공, `changed=4`, `failed=0`
- [x] Control Plane 멱등성: 2/2 노드 `changed=0`, `failed=0`
- [x] Worker 적용: 3/3 노드 성공, `changed=4`, `failed=0`
- [x] Worker 멱등성: 3/3 노드 `changed=0`, `failed=0`
- [x] 수정된 Check Mode API 검증: 5/5 노드 PASS
- [x] 최종 6노드 재검증: 6/6 노드 `changed=0`, `failed=0`
- [x] Resolver 순서: 6/6 노드 `.52 → .53` 확인
- [x] `fds.internal` FQDN 및 short name 확인
- [x] 외부 DNS: 6/6 노드 PASS
- [x] DNS 서버 직접 질의: 12/12 PASS
- [x] kubelet·containerd 회귀 없음: 6/6 노드 PASS

## 🧪 검증 및 증적

| 항목 | 결과 / 기준 |
|---|---|
| 원본 위치 | ansible01 실행 원본 및 `fds-project-evidence` 편입 후보 참조 |
| `EVIDENCE_INDEX.md` SHA-256 | `6f5568d805a5d7f43130d2fdca2ba631358f4f8be23e1f7d0799ae8243c7db1e` |
| `SHA256SUMS` SHA-256 | `05de9ba6b22d36ef8fc67bdf3dd8c6629c3e334fbb61620a265a46acdbfd4115` |
| 최종 6노드 검증 SHA-256 | `18cbda0fc7d91ebf58c89c230dccabaf9ad8239305856da03067210582194e83` |
| 무결성 검사 SHA-256 | `35a320650312e343764a5d7eecfe70c42bafcf43c8043a422d920030a20dee14` |
| 재확정 기록 SHA-256 | `db7da7eae13c1b07e6b073003a23229e76f3a86f6903a66ac9a2cf522f84395d` |
| 구현 PR | `321Team/infra-ansible` PR #1 |
| 승인 HEAD | `507d8882a04f53640b07251bcc234b7d6ee81c09` |
| Merge Commit | `4f9bdb7c08704eebb3d1b294751e51b0721b6af4` |
| CI | `NOT RUN` — CI PASS로 표기하지 않음 |

## 🔗 Dependency

- 선행: D08, D09, D34, D35, P1-DNS-01, P1-LB-01 Stage A
- 연계: P1-K8S-01, P1-LB-01, ICR-D-NET-01-01
- 정본 동기화 대상: Baseline, WBS/Gantt, Canonical Ticket Pack, Completion Record, 증적 참조, Release Notes 및 Manifest

## ⚖️ Decision / Risk Control

- `RISK-02`, `RISK-04`, `RISK-07`을 추적한다.
- 구현 완료를 Kubernetes API 인증, LB Stage B, kubeadm init/join 또는 ICR Runtime 완료로 확대 해석하지 않는다.
- GitHub Actions가 실행되지 않았으므로 검증 결과는 로컬·런타임 증적과 사람의 검토 기록으로만 판정한다.
- Release 전 Baseline·WBS/Gantt·Ticket Pack·완료 기록·Manifest 간 상태와 SHA를 재대조한다.

## 🤝 Review / Handoff

- Support Reviewer: 이하영 (`hayeounglee`)
- Support Review: APPROVED, 2026-09-07 11:13:58 KST
- Lead: 이권욱 (`GWONUK`)
- Lead 승인: 수동 병합 승인
- 승인 대상 HEAD: `507d8882a04f53640b07251bcc234b7d6ee81c09`
- 후속 인계: v3.1.18 전체 정본 묶음에 포함 후 독립 Reviewer가 동일 후보 HEAD를 재검토

## 🏁 Completion Record

- 기술 Acceptance Criteria: **11/11 PASS**
- 구현 PR: **MERGED**
- 완료일: **2026-09-07**
- 정본 상태: **v3.1.18 CANDIDATE에 동기화, 아직 RELEASED 아님**
- GitHub Actions: **NOT RUN**
- 완료 범위: 본 CR에 한정하며 후속 Gate 및 별도 ICR을 자동 완료 처리하지 않는다.
