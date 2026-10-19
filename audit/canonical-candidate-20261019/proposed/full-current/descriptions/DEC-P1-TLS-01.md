# DEC-P1-TLS-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/64) · updated_at `2026-10-09T13:06:26Z` · body SHA256 `6d924b398a843480866232a7af61236e5ee2b171068bcf9c9be0c2459958c375`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | DEC-P1-TLS-01 |
| Phase | Phase 1 |
| Category | Security / PKI |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-08-31 |
| Calendar Days | 5 |
| Working Days | 3 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Harbor와 edge01의 인증서 발급·SAN·CA Trust 배포·갱신·Rollback 방식을 확정하고 Consumer별 검증방법 승인 |
| Related Decision IDs | D19 |
| Related Risk IDs | RISK-06; RISK-08 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #64 snapshot 2026-09-09T12:17:08Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | D19 PASS(2026-08-31). Private CA + 서비스별 Leaf + Consumer CA Trust를 고정한다. Robot Account 설계·발급은 병행 가능하나 실제 로그인·Push/Pull Runtime Test는 CA Trust 적용 후 수행한다. |

실제 GitHub 종결 `2026-09-09T18:55:52+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] Private CA와 Harbor/edge01 별도 Leaf 구조가 승인된다.
- [x] 인증서 알고리즘·Owner·유효기간·배포경로가 확정된다.
- [x] 확정 FQDN과 실제 사용 IP가 Certificate Matrix의 SAN과 일치한다.
- [x] Runner·Worker·관리 Client의 CA Trust 배포방법이 정의된다.
- [x] TLS 1.2 이상과 인증서 검증 우회 금지 기준이 승인된다.
- [x] Root/Leaf Private Key 보관·백업·폐기·Evidence 마스킹 기준이 승인된다.
- [x] 실패·만료·SAN 불일치·Trust 제거·Rollback Test가 정의된다.
- [x] D-SEC-01 Robot Account 원칙과 TLS 책임 경계가 기록된다.
- [x] Worker Pull 계정과 CI/CD Push+Pull 계정 분리 기준이 기록된다.
- [x] Robot Account 설계 병행과 Runtime Test 실행 Gate가 구분된다.
- [x] P1-HBR-01/P1-CICD-01의 Endpoint 및 Trust 경로와 일치한다.
- [x] P2 Certificate/Trust Adapter 전환 원칙이 기록된다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
