# DEC-P2-COMP-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/121) · updated_at `2026-10-15T02:15:33Z` · body SHA256 `c709fd2b10dd77cea6cb0a13b85eb23098808d5258a315e65757a08cce2ef3ae`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | DEC-P2-COMP-01 |
| Phase | Phase 2 |
| Category | OpenShift / Security Compliance |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | TBD — G5 이후 P0 잔여 capacity 시 |
| End | TBD — 10-26 이전 강제하지 않음 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | Compliance Operator 도입/미도입/유예를 단일안으로 결정하고, 도입 시 ROSA topology(HCP 여부)·지원 Version·Scan profile/suite·결과 처리·Known Issue 경계·Operator 공급경로를 승인 |
| Related Decision IDs | D17(Security); D26(Operator 공급망); 신규 Decision Register 순번은 차기 정본에서 부여 |
| Related Risk IDs | RISK-07; RISK-10; RISK-11 |
| Source | 2026-09-29 팀 회의 Red Hat 제품 검토; 2026-09-30 사용자 범위 결정; Red Hat Compliance Operator 공식 문서; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | P1/non-blocking. #38 ROSA Platform/Security P0와 겹치지 않도록 G5 이후 capacity가 있을 때만 결정한다. Go 전에는 #38 현행 Security AC를 유지한다. |

## 현재 원 AC — 체크 상태 보존

- [ ] 도입 / 미도입 / 유예가 단일안으로 기록된다.
- [ ] ROSA topology와 Compliance Operator 지원 조건을 확인한다.
- [ ] HCP 사용 시 control-plane 접근 제약과 Operator scheduling 조건을 반영한다.
- [ ] 최소 Scan profile/suite와 대상 node/workload 범위를 고정한다.
- [ ] PASS/FAIL가 아니라 Compliant/NonCompliant/Error/NotApplicable 결과를 구분한다.
- [ ] NonCompliant 결과는 Severity/적용가능성/P0 영향 검토 후 Known Issue 또는 별도 Task로 이관한다.
- [ ] Operator Version/Subscription/Scan Source/Result/Evidence SHA를 추적한다.
- [ ] 재실행 및 cluster recreate 후 동일 Source로 재현 가능함을 검증할 계획을 정한다.
- [ ] G5/G6 일정 침해 시 Deferred로 전환한다.

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
