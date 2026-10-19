# P1-LNX-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/66) · updated_at `2026-10-09T13:06:32Z` · body SHA256 `1625eba7ec3eb263b1f856478ccfcfded39d1e2b413a8a73cc25a682192a63ab`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P1-LNX-01 |
| Phase | Phase 1 |
| Category | Linux / Network Baseline |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-24 |
| End | 2026-08-26 |
| Calendar Days | 3 |
| Working Days | 3 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Kubernetes 예정 Node의 CentOS Stream 10 Linux 필수조건 PASS, Static Network/Route/MTU/DNS 기준 검증, Network Verify FAIL=0, Evidence 및 Rollback 정보 확보, Kubernetes Service Role Check는 P1-K8S-01로 이관 |
| Related Decision IDs | D01 — 3인 / 8 Server / CentOS 10`, `D05 — Bridged Node / Service Endpoint`, `D13 — VMnet1/VMnet8 분리`, `D14 — Physical Return Route / Source NAT 금지`, `D15 — Gateway 비관리 제약`, `D16 — Reserved / DO_NOT_USE IP |
| Related Risk IDs | RISK-02 — Bridged Multi-MAC 제한`, `RISK-03 — CentOS Stream 10 Kubernetes 조합 검증 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #66 snapshot 2026-09-10T02:10:15Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 설계·사전구축 구간에서 2026-08-26 조기 완료. P1-LNX-01 완료판정은 Linux 필수조건과 Network Verify 기준이며 containerd/kubelet/kubeadm/API/Calico 동작은 포함하지 않는다. 해당 Role Check는 P1-K8S-01로 이관한다. |

실제 GitHub 종결 `2026-09-09T18:56:50+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] Kubernetes 예정 Node의 Linux 필수조건이 PASS다.
- [x] Kubernetes 예정 Node의 Network Verify 결과가 모두 `FAIL=0`이다.
- [x] IP / Prefix / MTU / Required Route가 Baseline과 일치한다.
- [x] Default Route가 필요한 Profile은 정확히 1개를 보유한다.
- [x] Default Route 금지 Profile은 Internet Route가 존재하지 않는다.
- [x] DO_NOT_USE IP가 Node에 할당되지 않았다.
- [x] Apply/Test 결과와 이전 상태 Backup 정보가 남아 있다.
- [x] Kubernetes Service Role Check 제외근거와 후속 이관 대상이 기록되었다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
