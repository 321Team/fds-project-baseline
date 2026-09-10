<!-- fds-canonical-description:v3.1.18 record-id:D-SEC-01 -->
# D-SEC-01 — Security Design Scope / Approval Review

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | D-SEC-01 |
| Phase | Design |
| Category | Security / Governance |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-26 |
| End | 2026-09-01 |
| Calendar Days | 7 |
| Working Days | 4 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | 승인권자 지정, D-SEC-01 검토 범위·산출물·Exit Criteria 승인, P1-SEC-01과의 경계 승인, 요구사항과 검증 증적 연결 후 Done 판정 |
| Related Decision IDs | D17; D28 |
| Related Risk IDs | RISK-05; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #7 snapshot 2026-09-09T12:13:54Z |
| Schedule Note | v3.1.14 최종 승인·정본 반영 완료. 구현은 P1-SEC-01로 이관. |

## 현재 실행·검토 상태

기준 시점의 Done 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #7](https://github.com/321Team/fds-project-baseline/issues/7), Issue 갱신 시각 `2026-09-09T12:13:54Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

# User Story

Security Design Lead 이하영으로서 D-SEC-01의 검토 범위, 승인권자, 산출물, Exit Criteria를 확정한다. 이를 통해 보안 설계 검토와 P1-SEC-01 구현 책임의 경계를 명확히 하고, 승인 증적 없이 티켓이 완료 처리되지 않도록 통제한다.

---

# Scope

## In Scope

- Lead 이하영 지정사항의 WBS·Notion·기준선 반영
- D-SEC-01 Approver 지정
- 보안 설계와 구현 티켓의 경계 정의
- 필수 산출물·Exit Criteria·Evidence 승인

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [x] Lead를 이하영으로 지정하고 이권욱 담당 전제를 제거한다.
- [x] 지원 역할과 승인권자를 D17/D34 승인 기록으로 확정했다. (Approver 이권욱, Technical Review Owner 이하영, Support 이재환; 2026-09-01)
- [x] Network Allowlist, Kubernetes Security, Secret, Registry Scan 중 설계 범위를 명시한다. — 2026-09-01 D17/D34 승인 기록으로 확인.
- [x] P1-SEC-01과 중복 또는 누락되는 항목을 제거한다. — 2026-09-01 D17/D34 승인 기록으로 확인.

---

# Acceptance Criteria

- [x] Lead 이하영이 WBS·Notion·기준선에 동일하게 기록된다.
- [x] Approver가 실명으로 지정된다. — 2026-09-01 D17/D34 승인 기록으로 확인.
- [x] In Scope/Out of Scope와 Exit Criteria가 승인된다. — 2026-09-01 D17/D34 승인 기록으로 확인.
- [x] D17/D34 승인 결과가 정본 WBS와 기준선의 `Done / PASS`에 반영되었다. Notion 실시간 상태는 별도 미대조다.
- [x] 승인된 Exit Criteria와 Evidence가 없으면 Done으로 변경되지 않는다. — 2026-09-01 D17/D34 승인 기록으로 확인.

---

# 검증 및 증적

- Lead 이하영 지정 기록
- 승인된 Scope/Exit Criteria
- Decision D17 결과
- 갱신된 WBS/Notion 화면
- Evidence Path: `docs/evidence/D-SEC-01/`

---

# Dependency

- **Blocked By:** 없음
- **Blocks / Next:** P1-SEC-01 Scope / Exit Criteria 경계 확정
- **Related Ticket:** P1-SEC-01, D-WBS-01
- **Milestone:** G0 Conditional Pass 해소

---

# Decision / Risk Control

- **Related Decision IDs:** D17; D28
- **Decision Control:** D17에서 Lead 이하영 지정은 반영되었으며, 검토 범위·승인권자·Exit Criteria 승인 결과가 본 티켓의 종결 근거다.
- **Related Risk IDs:** RISK-05; RISK-07
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Review / Handoff

- **Review Owner:** 등록된 Support 이권욱, 이재환
- **Review Sequence:** 단위 테스트 결과 확인 → 영향성 검토 → Review Result 기록
- **Lead Supplement:** 필요 시 이하영이 보완하며 강제 절차가 아니다.

---

# Completion Record

- **Result:** PASS — D17/D34 승인 및 P1-SEC-01 구현 Handoff 완료
- **Status:** Done
- **Exit Criteria:** 승인권자 지정, D-SEC-01 검토 범위·산출물·Exit Criteria 승인, P1-SEC-01과의 경계 승인, 요구사항과 검증 증적 연결 후 Done 판정
- **Completed Date:** 2026-09-01
- **Reviewer / Approver:** Technical Review Owner 이하영 / Approver 이권욱 — D34 승인 기록 기준

## 체크사항 보완 근거 (2026-09-09)

| 보완 항목 | 확인 근거 |
|---|---|
| 역할·승인권자 및 승인 실명 | 본문 D34 승인 기록의 Approval Authority / Technical Review Owner / Support |
| 설계 Scope·Exit Criteria | D34 승인 기록 §1~2; D17/D34 승인 |
| P1-SEC-01 경계·Handoff | D34 §2~4; Runtime 구현·시험은 P1-SEC-01에서 별도 판정 |
| Done의 승인·증적 조건 | D34 §3 상태 전이: D-SEC-01 Done/PASS, MS-G0-01 Done/FULL PASS |

근거 문서: `D34_D-SEC-01_Approval_and_Disposition_Record_v1.0.md` 및 본문에 연결된 RELEASED v3.1.17 정본. 이번 수정은 승인 기록을 Description에 동기화하며 새로운 서명이나 Runtime PASS를 부여하지 않는다.
