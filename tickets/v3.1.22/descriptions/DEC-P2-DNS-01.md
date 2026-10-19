문서 버전 **v3.1.22 / CANDIDATE**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# DEC-P2-DNS-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/40) · updated_at `2026-10-13T16:41:49Z` · body SHA256 `40ce4afdd023f56867be248ea65a5b0ef52548d89670d5b8a646a42502758ab4`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | DEC-P2-DNS-01 |
| Phase | Phase 2 |
| Category | Architecture / DNS |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | 2026-10-16 |
| End | 2026-10-16 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | P0 IP Endpoint 유지 또는 Hybrid DNS P1 적용을 확정하고 Resolver/Forwarding/Zone/Route/테스트·Cancelled 결정 근거를 승인 |
| Related Decision IDs | D11; D23 |
| Related Risk IDs | RISK-10; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #40 snapshot 2026-09-09T12:08:24Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 보류(Deferred) — 2026-10-14 이권욱 결정. D23 추가 Hybrid DNS 도입 보류 확정; 기존 DB/Harbor IP 및 ROSA public API/Route DNS·엄격 TLS 기준 유지. Owner 이권욱. 기존10/16은 보류 재검토 기준일이며 자동 재개 승인이 아니다. 재개는 이권욱의 별도 판단 후 결정. 기존 계획 기준: P0 Hybrid 경로 차단을 피하기 위해 10-16 단일 Decision window에서 IP Endpoint 유지 또는 DNS P1 적용을 확정한다. 구현(#48)은 Go이면서 P0 잔여 capacity가 있을 때만 별도 착수한다. |

## 현재 원 AC — 체크 상태 보존

- [ ] P0/P1 범위가 단일안으로 승인된다.
- [ ] 적용 시 Query Path와 Test가 정의된다.
- [ ] 미적용 시 N/A/Deferred 근거가 기록된다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
