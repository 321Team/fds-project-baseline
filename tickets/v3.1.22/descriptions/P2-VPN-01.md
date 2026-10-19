문서 버전 **v3.1.22 / CANDIDATE**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# P2-VPN-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/37) · updated_at `2026-10-19T09:47:38Z` · body SHA256 `2b32f927a8fec876b349ab7a0b7fe51277a06c44fe85a8a05e814f2ef69fdada`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P2-VPN-01 |
| Phase | Phase 2 |
| Category | Hybrid Network / VPN |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-10-12 |
| End | 2026-10-14 |
| Calendar Days | 3 |
| Working Days | 3 |
| Lead | 이재환 |
| Support | 이권욱 |
| Exit Criteria | 승인 Transit 경로의 Tunnel UP, On-Prem↔VPC Route, UDP 500/4500/IPsec, Source·승인 TCP Path 및 장애 Evidence 확보 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-04; RISK-10; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #37 snapshot 2026-09-10T02:09:49Z; 일정: docs-v3.1.20 WBS + 2026-09-22 재계획 + 2026-09-24 일정 정합화; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | #35 전체 완료를 기다리지 않고 10-08 Stage-A handoff(VPC/Subnet/Route/VPN 입력) 수신 후 10-12 착수한다. #35 Full과 #37 완료는 모두 10-14 G4 판정 전에 충족해야 한다. |

## 현재 원 AC — 체크 상태 보존

- [ ] 승인 Tunnel이 UP이다.
- [ ] On-Prem↔VPC 승인 TCP 경로가 성공한다.
- [ ] 미승인 경로가 차단된다.
- [ ] Tunnel 중단·복구가 Runbook대로 재현된다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
