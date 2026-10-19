문서 버전 **v3.1.22 / RELEASED after reviewed finalization merge**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# DEC-P1-MON-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/63) · updated_at `2026-10-09T13:06:24Z` · body SHA256 `61ab60f5943c173ff7b872b9377d5b50bbcccc3afe249ef6658bc94d9aa12ab7`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | DEC-P1-MON-01 |
| Phase | Phase 1 |
| Category | Monitoring / Architecture / Security |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-31 |
| End | 2026-08-31 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Grafana 포함 Kubernetes 내부 관측 Stack, node-exporter 통제 예외, monitor01 외부 Watchdog, IF-05/IF-06 계열, 보안·Rollback·후속 구현 책임을 D33으로 승인하고 Baseline·Architecture·Addendum·Release Notes를 발행 |
| Related Decision IDs | D05; D14; D17; D19; D33 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #63 snapshot 2026-09-09T12:16:31Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | D33 Done/2026-08-31. 본 후보의 Closed/Decision Register에 연결. Runtime 14개 Acceptance는 P1-MON-01, P1 고도화는 P1-MON-02 책임이다. |

실제 GitHub 종결 `2026-09-09T18:55:13+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] Hybrid Monitoring 배치와 장애영역이 Logical/Physical Architecture v3.1.3에 반영됐다.
- [x] Kubernetes 내부 Stack, node-exporter 예외 및 monitor01 외부 Watchdog 역할이 확정됐다.
- [x] IF-05/IF-06 계열의 Source, Destination, Protocol, Port, Owner, Acceptance가 동결됐다.
- [x] D-SEC-01 Monitoring System Exception Addendum v1.0이 발행됐다.
- [x] Grafana P0 범위와 P1-MON-02 HA·장기보존 경계가 분리됐다.
- [x] P1-MON-01의 14개 Runtime Acceptance와 Evidence 책임이 정의됐다.
- [x] 문서 Rollback과 Runtime Rollback 승인 원칙이 정의됐다.
- [x] Baseline v3.1.13 및 Release Notes에 D33 변경이 반영됐다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
