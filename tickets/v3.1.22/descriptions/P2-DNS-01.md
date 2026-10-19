문서 버전 **v3.1.22 / RELEASED after reviewed finalization merge**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# P2-DNS-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/48) · updated_at `2026-10-13T16:41:54Z` · body SHA256 `15ae082d9a00115ba706df9fbe857eef2b391796b882aaf748cb8b820c92e345`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P2-DNS-01 |
| Phase | Phase 2 |
| Category | DNS / Hybrid Integration |
| Type | Task |
| Status | To Do |
| Priority | P1 |
| Start | TBD — D23 Go + P0 잔여 capacity 시 |
| End | TBD — 10-26 이전 강제하지 않음 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | D23이 Hybrid DNS를 선택한 경우 Resolver/Conditional Forwarding/Route/Query Test PASS; IP Endpoint 유지 시 Cancelled 결정 근거 승인 |
| Related Decision IDs | D11; D23 |
| Related Risk IDs | RISK-10; RISK-12; RISK-15 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #48 snapshot 2026-09-10T02:10:01Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 보류(Deferred) — 2026-10-14 이권욱 결정. 추가 Hybrid DNS 구현을 보류하며 OPEN 유지; Cancelled/완료 아님. Owner 이권욱. D23 Go와 P0 잔여 capacity 및 이권욱의 별도 재개 판단 전 구현하지 않는다. 기존 계획 기준: P1 Conditional. D23가 Hybrid DNS Go이고 P0 일정 여유가 있을 때만 실행한다. 그렇지 않으면 Cancelled/Deferred 근거를 남기고 IP Endpoint로 P0 E2E를 진행한다. |

## 현재 원 AC — 체크 상태 보존

- [ ] Hybrid DNS 선택 시 양방향 승인 Query가 성공한다.
- [ ] 미승인 Query가 차단된다.
- [ ] 장애 시 IP Endpoint 또는 승인 Fallback이 동작한다.
- [ ] IP Endpoint 선택 시 Cancelled 결정 근거가 승인된다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
