# P2-ARC-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/34) · updated_at `2026-10-19T09:38:19Z` · body SHA256 `2dbc6ac6e298940f7405bbe86f262f73e623b59969b3ea31267d240abf153d48`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P2-ARC-01 |
| Phase | Phase 2 |
| Category | Architecture / Hybrid Cloud |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-10-08 |
| End | 2026-10-08 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | OCI Relay·AWS VPC/VPN·ROSA·On-Prem 연계 Architecture, Interface IF-17~IF-20, Security, Decision, Exit Criteria Freeze 승인 |
| Related Decision IDs | D10; D21; D22; D23; D25; D26 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12; RISK-14; RISK-15 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #34 snapshot 2026-09-10T02:09:45Z; 일정: docs-v3.1.20 WBS + 2026-09-22 재계획 + 2026-09-24 일정 정합화; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 10-07은 사전설계/미결 입력 정리, 최종 Freeze 목표는 10-08 D21 결정 이후다. 순서: #36 D21 → #34 최종 Architecture/Transport 계약 Freeze → #35 Stage-A handoff. D21 또는 잔여 사양 미확정 시 Freeze HOLD; 같은 날 handoff 작업창은 별도 확인하며 G4/후속 일정을 자동 승인하지 않는다. |

실제 GitHub 종결 `2026-10-19T18:38:16+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [ ] Architecture와 Interface가 이권욱·이하영·이재환 검토 대상으로 배포된다.
- [ ] P2-OCI/IAC/VPN/ROSA/APP/CICD의 의존성이 연결된다.
- [ ] D21~D23·D26의 결정 시점과 조건부 범위가 명시된다.
- [ ] 변경 통제 기준이 승인된다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
