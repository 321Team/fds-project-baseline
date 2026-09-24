<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/DEC-P2-RHOAI-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/DEC-P2-RHOAI-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

# DEC-P2-RHOAI-01 — RHOAI(Red Hat OpenShift AI) 도입 범위 결정

> 신규 발행: 2026-09-23 KST · 2026-09-23 팀 회고 합의 "Phase 2 착수 시 RHOAI 도입안 포함 필수"에 따른 신규 Decision 티켓.
> 현행 발행 정본 [docs-v3.1.20](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.20)의 Baseline/WBS/Ticket Pack에는 이 Record가 없다. 차기 정본 후보에 반영하기 전까지 이 Issue 본문이 운영 기록이며, 정본 발행 상태를 뜻하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P2-RHOAI-01 |
| Phase | Phase 2 |
| Category | OpenShift / AI Platform |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | 2026-10-06 |
| End | 2026-10-16 |
| Calendar Days | 11 |
| Working Days | 8 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | RHOAI 도입/미도입/유예를 단일안으로 결정하고, 도입 시 적용 범위·ROSA 전제(Version/Quota/Operator 공급)·비용·삭제 절차와 Change Request 발행 근거를, 미도입·유예 시 N/A/Deferred 근거를 기록·승인 |
| Related Decision IDs | D26 — 기존 의미 유지(ROSA Operator 공급망). 신규 D 순번은 정본 Decision Register 대조 후 부여 |
| Related Risk IDs | 미부여 — 정본 Risk Register 대조 후 부여 |
| Source | 2026-09-23 팀 회고 합의([PR #94](https://github.com/321Team/fds-project-baseline/pull/94)); 사용자 2026-09-23 속성 결정(Type Decision·Lead 이하영·Priority P1·일정 10-06~10-16); 발행 docs-v3.1.20 Baseline §1.3/§3.2 |
| Schedule Note | Phase 2 착수(`MS-P2-START-01` #33, 10-06)와 동시에 시작하고 D22/D23/D26 결정 시한 10-16에 맞춘다. 10-09는 비근무일, 주말 작업 0. 일정은 조정 가능한 계획 목표다. Baseline §3.2에 따라 P1 미완료는 P0 Gate를 차단하지 않는다. |

---

# User Story

ROSA 플랫폼 담당자로서 Phase 2에서 RHOAI(Red Hat OpenShift AI)를 도입할지와 그 범위를 결정한다. 이를 통해 팀 회고에서 합의한 RHOAI 도입안을 Phase 2 계획에 포함하면서, 결정 전에 기존 P0 Hybrid 범위와 일정에 미확정 기능이 추가되지 않도록 한다.

---

# Scope

## In Scope

- RHOAI 도입/미도입/유예 대안 비교
- ROSA 대상 전제: 지원 Version, Worker/Quota, Operator 공급 방식(D26 연계)
- FDS 서비스(`transaction-api`, `fds-engine`)와의 연계 목적·범위
- 비용·삭제·복구 절차
- 도입 시 Change Request·후속 구현 티켓 정의

## Out of Scope

- 결정 전 RHOAI 설치·구성 등 구현 작업
- 기존 P0 Hybrid 범위·Gate 기준 변경
- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 도입 목적과 FDS 서비스 연계 범위를 명시한다.
- [ ] ROSA 지원 Version·Quota·Operator 공급 전제를 확인한다.
- [ ] 비용과 삭제·복구 절차를 기록한다.
- [ ] Baseline §1.3 Scope Out의 "AI Inference"와의 관계를 명시한다.

---

# Acceptance Criteria

- [ ] 도입/미도입/유예가 단일안으로 승인된다.
- [ ] 도입 시 Baseline §3.2에 따른 Change Request와 후속 구현 티켓(Owner/Due)이 발행된다.
- [ ] 미도입·유예 시 N/A/Deferred 근거가 기록된다.
- [ ] 결정 결과가 P2-ARC-01·P2-ROSA-01과 차기 정본 후보에 연결된다.

---

# 검증 및 증적

- Decision 비교표
- ROSA 전제(Version/Quota/Operator) 확인 기록
- 비용·삭제 절차
- 신규 Decision Register 항목
- Evidence Path: `321Team/fds-project-evidence:evidence/DEC-P2-RHOAI-01/`

---

# Dependency

- **Blocked By:** MS-P2-START-01
- **Blocks / Next:** 도입 결정 시 Change Request 및 구현 티켓
- **Related Ticket:** P2-ARC-01 (#34), P2-ROSA-01 (#38), DEC-P2-OP-01 (#41)
- **Milestone:** G5 ROSA Application Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D26 (신규 D 순번은 정본 레지스터 대조 후 부여)
- **Decision Control:** 결정 전에 조건부 구현 작업을 시작하지 않는다. Scope Out 기능 추가는 Baseline §3.2의 Change Request 절차를 따른다.
- **Related Risk IDs:** 미부여 — 정본 레지스터 대조 후 부여
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** RHOAI 도입/미도입/유예를 단일안으로 결정하고, 도입 시 적용 범위·ROSA 전제(Version/Quota/Operator 공급)·비용·삭제 절차와 Change Request 발행 근거를, 미도입·유예 시 N/A/Deferred 근거를 기록·승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용