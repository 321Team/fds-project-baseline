# P2-OCI-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/36) · updated_at `2026-10-19T09:38:30Z` · body SHA256 `f70908ecded811819f4e556078f9d4b81fef8c6536027b01c4c02084348221c6`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P2-OCI-01 |
| Phase | Phase 2 |
| Category | Milestone / Hybrid Network |
| Type | Decision |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-10-07 |
| End | 2026-10-08 |
| Calendar Days | 2 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-10; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #36 snapshot 2026-09-09T12:07:26Z; 일정: docs-v3.1.20 WBS + 2026-09-22 재계획 + 2026-09-24 일정 정합화; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | D21 결정창 10-07~10-08 유지. 교육장 UDP/500·4500 경로 관측 → return/NAT-T/IKE 검증 → 보안 노출·return-route·SPOF 판단 → Transport Adapter 선택을 거쳐 #34 최종 Freeze 및 #35 Stage-A에 인계한다. 경로 관측/Decision 미완료 시 D21 OPEN과 후속 HOLD를 유지한다. |

## 현재 원 AC — 체크 상태 보존

- [ ] OCI Primary의 실행 가능 여부가 증적으로 판정된다.
- [ ] Go 또는 단일 Fallback이 승인된다.
- [ ] P2-VPN-01과 P2-IAC-01 입력값이 확정된다.
- [ ] 미결 전제와 Owner/Due가 0건이다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
