<!-- fds-canonical-description:v3.1.18 record-id:P2-CICD-01 -->
# P2-CICD-01 — Runner to ROSA Delivery

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-CICD-01 |
| Phase | Phase 2 |
| Category | CI/CD / OpenShift Delivery |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-16 |
| End | 2026-10-19 |
| Calendar Days | 4 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | GitHub→Self-hosted Runner→승인 Registry→ROSA Deploy→Health/Rule Smoke Test 흐름과 실패 시 배포차단 Evidence 확보 |
| Related Decision IDs | D22; D25 |
| Related Risk IDs | RISK-06; RISK-08; RISK-11; RISK-14 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #46 snapshot 2026-09-10T02:09:57Z |
| Schedule Note | P2-ROSA-01과 P2-APP-01의 Manifest/Image 계약을 사용하고 Registry는 D22 결과를 따른다. G5 ROSA Application Ready에 연결한다. |

## 현재 실행·검토 상태

Plan End 2026-10-19와 G5 목표 2026-10-16의 기존 충돌은 미해소다. 날짜를 임의 이동하지 않고 단일 Milestone 매핑 HOLD를 유지한다. 실행·일정 조정은 별도 Lead 판단 사항이다.

근거: [Issue #46](https://github.com/321Team/fds-project-baseline/issues/46), Issue 갱신 시각 `2026-09-10T02:09:57Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Cloud Delivery 담당자 이권욱으로서 검증된 Phase 1 Image를 승인 Registry에서 ROSA로 자동 배포한다. 이를 통해 On-Prem과 ROSA의 Delivery 추적성과 실패 차단 기준을 유지한다.

---

# Scope

## In Scope

- GitHub Private Repo
- Self-hosted Runner
- 승인 Registry
- oc/kubectl/Helm Deploy
- Health·Rule Smoke Test
- 실패 차단

## Out of Scope

- 승인되지 않은 Registry
- 수동 Secret 하드코딩
- Production 무중단 배포 보증

---

# 핵심 요구사항

- [ ] Commit SHA와 Image Digest를 연결한다.
- [ ] ROSA Credential을 Secret으로 통제한다.
- [ ] Test/Scan 실패 시 Deploy를 차단한다.
- [ ] D22 Registry 결정을 준수한다.

---

# Acceptance Criteria

- [ ] 정상 Commit이 ROSA까지 배포된다.
- [ ] Test 또는 Scan 실패 시 배포가 차단된다.
- [ ] 배포 Image와 Commit을 역추적할 수 있다.
- [ ] Health와 R01/R02/R04/R07 Smoke Test가 통과한다.

---

# 검증 및 증적

- Workflow Source
- Runner/Registry/ROSA Run
- Failed Gate Run
- Image Digest
- Evidence Path: docs/evidence/P2-CICD-01/

---

# Dependency

- **Blocked By:** P2-ROSA-01; P2-APP-01; DEC-P2-REG-01
- **Blocks / Next:** MS-G5-01; P2-HYB-01
- **Related Ticket:** P1-CICD-01
- **Milestone:** G5 ROSA Application Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D22; D25
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-06; RISK-08; RISK-11; RISK-14
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** GitHub→Self-hosted Runner→승인 Registry→ROSA Deploy→Health/Rule Smoke Test 흐름과 실패 시 배포차단 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
