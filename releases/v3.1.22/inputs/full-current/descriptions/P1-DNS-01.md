# P1-DNS-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/12) · updated_at `2026-10-09T13:05:24Z` · body SHA256 `03eb461ade125e58c6b6724241d2e39ee2bdc73e85a815b10dcde70f52715b99`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P1-DNS-01 |
| Phase | Phase 1 |
| Category | DNS / Supporting Service |
| Type | Task |
| Status | Done |
| Priority | P1 |
| Start | 2026-08-28 |
| End | 2026-09-03 |
| Calendar Days | 7 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Primary/Secondary·TSIG·제한 Query/Recursion·Failover Evidence와 k8s-api-lb01 `.109` Resolver/ACL/IPSet 검증 및 Support Review 승인 |
| Related Decision IDs | D08; D09; D34; D35 |
| Related Risk IDs | RISK-02; RISK-04; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #12 snapshot 2026-09-10T02:09:19Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 기술 검증·Support Review·.109 ACL/Resolver/Failover Delta 확인 완료. 2026-09-03 Done 승인. |

실제 GitHub 종결 `2026-09-09T18:41:10+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] 원본 Evidence SHA-256 및 Support Review 승인 — DNS-AC-12/14/16 PASS (2026-09-03 승인본).
- [x] `.109` Positive Test PASS, 비승인 Source Negative Test 유지 — DNS-AC-06/10/11; DNS-NT-01/03; DNS-CR-05 PASS (2026-09-03 승인본).
- [x] Secret/TSIG 원문이 Evidence에 포함되지 않음 — DNS-AC-13 PASS (2026-09-03 승인본).

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
