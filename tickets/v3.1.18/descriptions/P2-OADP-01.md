<!-- fds-canonical-description:v3.1.18 record-id:P2-OADP-01 -->
# P2-OADP-01 — OADP / S3 Backup

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-OADP-01 |
| Phase | Phase 2 |
| Category | Backup / OpenShift |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-15 |
| End | 2026-10-22 |
| Calendar Days | 8 |
| Working Days | 6 |
| Lead | 이하영 |
| Support | 이권욱 |
| Exit Criteria | OADP→S3 443, Backup 대상·Credential·Schedule, Restore 또는 승인 복구검증과 Evidence 확보 |
| Related Decision IDs | D12 |
| Related Risk IDs | RISK-11; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #44 snapshot 2026-09-10T02:09:55Z |
| Schedule Note | Backup 생성만으로 DONE 처리하지 않고 Restore 또는 승인된 복구 검증이 필요하다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #44](https://github.com/321Team/fds-project-baseline/issues/44), Issue 갱신 시각 `2026-09-10T02:09:55Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

OpenShift 백업 담당자로서 ROSA Workload의 구성과 필요한 데이터를 S3에 보호한다. 이를 통해 Cloud 측 배포를 재현하거나 복구할 수 있는 최소 DR Evidence를 확보한다.

---

# Scope

## In Scope

- OADP
- S3
- Credential
- Backup Scope
- Restore/Recovery Test
- Runbook

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] OADP→S3는 TCP 443만 사용한다.
- [ ] Credential을 Secret으로 관리한다.
- [ ] Backup 대상과 제외 대상을 명시한다.
- [ ] Backup Retention과 비용 영향을 기록한다.
- [ ] 복구 대상 Namespace를 격리한다.

---

# Acceptance Criteria

- [ ] Backup이 성공하고 Object가 확인된다.
- [ ] Restore 또는 승인된 복구검증이 성공한다.
- [ ] Workload Health와 Config 정합성이 확인된다.
- [ ] Runbook과 Evidence가 저장된다.

---

# 검증 및 증적

- OADP/S3 Config
- Backup Log/Object
- Restore/Recovery Result
- Workload Health
- Backup/Restore Runbook
- Evidence Path: `docs/evidence/P2-OADP-01/`

---

# Dependency

- **Blocked By:** P2-ROSA-01
- **Blocks / Next:** P2-E2E-01, P2-DOC-01
- **Related Ticket:** P2-APP-01
- **Milestone:** G6 Hybrid Integration Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D12
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** OADP→S3 443, Backup 대상·Credential·Schedule, Restore 또는 승인 복구검증과 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
