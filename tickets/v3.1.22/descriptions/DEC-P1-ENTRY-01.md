문서 버전 **v3.1.22 / RELEASED after reviewed finalization merge**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# DEC-P1-ENTRY-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/62) · updated_at `2026-10-09T13:06:21Z` · body SHA256 `e8cd2a9b4633e536467b2cdec381fd9fd243d30f41b7e4bcd8b0c317c5ab5f9f`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | DEC-P1-ENTRY-01 |
| Phase | Phase 1 |
| Category | Architecture / Network |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-08-31 |
| Calendar Days | 5 |
| Working Days | 3 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | edge01→transaction-api 노출 방식을 Ingress/Reverse Proxy/NodePort 후보 중 확정하고 Port·Health Check·Firewall·NetworkPolicy 변경을 승인 |
| Related Decision IDs | D05; D18; D27 |
| Related Risk IDs | RISK-02; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #62 snapshot 2026-09-09T12:16:14Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | D18 PASS(2026-08-31). P1-APP-01 External Exposure와 P1-SEC-01 Allowlist/NetworkPolicy에 승인 결정을 전달한다. P1-LB-01 API LB와 P1-K8S-01 Cluster Bootstrap에는 Non-blocking이다. |

실제 GitHub 종결 `2026-09-09T18:54:41+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] 단일 구현안과 대체안이 기록된다.
- [x] Reverse Proxy + 제한 NodePort 방식에 대한 팀 합의가 완료된다.
- [x] `externalTrafficPolicy: Local` 적용이 결정값으로 확정된다.
- [x] Port와 Health Check 기준이 기록된다.
- [x] Firewall·NetworkPolicy 변경 범위와 Rollback 방식이 정의된다.
- [x] P1-APP/P1-SEC의 선행조건과 P1-LB/P1-K8S의 Non-blocking 관계가 반영된다.
- [x] P2 ROSA 전환 시 Exposure Adapter 교체 원칙이 정의된다.
- [x] 관련 Risk ID와 통제 기준이 연결된다.
- [x] 선택안, 책임 경계 및 Approver 승인 결과가 기록된다.

Runtime Manifest 적용 및 통합 테스트 완료 여부는 `P1-APP-01`, `P1-SEC-01`, `P1-HBR-01`에서 별도로 판정한다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
