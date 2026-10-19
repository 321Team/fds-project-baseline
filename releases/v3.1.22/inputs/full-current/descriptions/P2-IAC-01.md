# P2-IAC-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/35) · updated_at `2026-10-19T09:38:24Z` · body SHA256 `677720e9b9fc7235f187a60f2dceecae874203e5a774a560821b584b7e8c8f49`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P2-IAC-01 |
| Phase | Phase 2 |
| Category | Cloud / Terraform |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-10-08 |
| End | 2026-10-14 |
| Calendar Days | 7 |
| Working Days | 4 |
| Lead | 이하영 |
| Support | 이권욱 |
| Exit Criteria | AWS VPC 10.20.0.0/16, ROSA 선행 인프라와 IAM/OIDC 최소권한의 Terraform fmt/validate/plan/apply, State·Secret 통제 및 G4 Evidence 확보 |
| Related Decision IDs | D10; D21; D25 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #35 snapshot 2026-09-10T02:09:47Z; 일정: docs-v3.1.20 WBS + 2026-09-22 재계획 + 2026-09-24 일정 정합화; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 10-08 Stage-A 목표는 #36 D21 결정 → #34 최종 Freeze 이후에만 유효하다. Transport Adapter·Subnet/AZ·Route·backend/state 계약 및 reviewed plan/evidence를 고정한 뒤 #37(10-12)이 소비한다. 10-14 Full completion/G4 목표 유지. 당일 작업창 부족 또는 선행 HOLD 시 handoff를 완료로 기록하지 않고 후속 일정 재평가; Stage-A는 전체 AC PASS가 아니다. |

## 현재 원 AC — 체크 상태 보존

- [ ] fmt/validate가 통과한다.
- [ ] 승인 Plan과 Apply 결과가 일치한다.
- [ ] 필수 Route/Security/Output과 IAM/OIDC가 생성된다.
- [ ] State와 Secret 접근이 통제된다.
- [ ] 재실행 시 비의도 변경이 없다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
