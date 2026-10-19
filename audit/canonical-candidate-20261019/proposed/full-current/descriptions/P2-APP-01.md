# P2-APP-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/43) · updated_at `2026-10-19T09:38:51Z` · body SHA256 `449a971a44a453c5e1d84f320d02979d00c7332e3e3ecca8132f3c9389c77359`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P2-APP-01 |
| Phase | Phase 2 |
| Category | Application / OpenShift |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-10-16 |
| End | 2026-10-19 |
| Calendar Days | 4 |
| Working Days | 2 |
| Lead | 이재환 |
| Support | 이하영 |
| Exit Criteria | Phase 1과 동일한 transaction-api/fds-engine Image/Contract를 ROSA에 배포하고 Route/Health/Rule 기본검증 PASS |
| Related Decision IDs | D03; D22 |
| Related Risk IDs | RISK-06; RISK-07; RISK-11 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #43 snapshot 2026-09-10T02:09:53Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 10-15 #38 Basic Ready + #42 Registry Decision 수신 후 10-16 착수. #38 전체 Security 검증과 병행하되, #43은 승인된 Namespace/RBAC/Registry 경계 밖으로 확장하지 않는다. |

## 현재 원 AC — 체크 상태 보존

- [ ] 두 서비스가 ROSA에서 Ready다.
- [ ] Route를 통한 transaction-api Health가 성공한다.
- [ ] fds-engine이 외부에 직접 노출되지 않는다.
- [ ] 4개 Rule Smoke Test가 통과한다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
