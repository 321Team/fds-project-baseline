# D36 — Team Availability / Phase 1 Schedule & Status Update Record

> **Document Version:** v1.0  
> **Decision State:** Fixed / User Approved  
> **Approval Date:** 2026-09-03  
> **Effective Date:** 2026-09-03  
> **Canonical Baseline:** `FDS_Project_Implementation_Baseline_v3.1.16.md`

---

## 1. 승인 내용

2026-09-04 이재환의 개인 사정 휴가를 승인된 개인 부재로 등록한다. 이 날짜는 팀 전체 Non-working Date가 아니며, 이재환이 Lead 또는 필수 Support인 작업에만 가용성 영향을 적용한다.

기존 2026-09-14~09-17 예비군 부재는 유지한다.

## 2. 일정 영향 판정

| Record | Before | After | 판정 근거 | Downstream |
|---|---|---|---|---|
| `P1-DB-01` | End 2026-09-04 | End 2026-09-07 | 휴가일 단독 Lead 종료 금지, Lead 가용 작업일 6일 보존 | G1 연동 |
| `MS-G1-01` | 2026-09-04 | 2026-09-07 | `P1-DB-01` 완료와 Gate Evidence Review 정렬 | G1 +1 영업일 |
| `P1-APP-01` | End 2026-09-09 | End 2026-09-10 | 09-04 Owner 비가용일 보전 | G2 09-11 유지 |
| `P1-MON-01` | Start 2026-09-04 | Start 2026-09-07 | 복귀 후 Runtime 실행 착수 | G2 09-11 유지 |
| `P1-SEC-01` | 09-04~09-11 | 변경 없음 | Lead 이하영 유지, 09-04 Support는 이권욱이 커버 | G2 유지 |

다음 일정은 변경하지 않는다.

- G2 Security / Feature Ready: 2026-09-11
- G3 Review Ready: 2026-09-18
- Phase 1 Close: 2026-09-23
- Phase 2 Start 및 이후 일정

## 3. 티켓 상태 동기화

| Ticket | Canonical Status | 기준일 | 판정 |
|---|---|---|---|
| `P1-DNS-01` | **Done** | 2026-09-03 | 기술 검증, `.109` ACL/Resolver/Failover Delta, Support Review 완료 |
| `P1-K8S-01` | **In Progress** | 2026-09-03 | P1-LB Stage A PASS 인수 후 Gate 0~2 착수 |
| `P1-LB-01` | **In Progress** | 2026-09-03 | Stage A Technical/Evidence PASS; Stage B Backend UP·Authenticated API·Failover Pending |

`P1-LB-01`은 Stage A PASS만으로 Done 처리하지 않는다.

## 4. Interface Register 영향

| Interface | Runtime State Update | Ticket 영향 |
|---|---|---|
| IF-11 | Stage A Runner TCP Positive PASS; Authenticated Deploy Pending | `P1-LB-01`, `P1-CICD-01` |
| IF-11A | Stage A Node Positive 6/6 PASS; `.10` Negative PASS | `P1-LB-01`, `P1-K8S-01` |
| IF-12 | Pre-bootstrap Reachability PASS; Stage B Pending | `P1-LB-01`, `P1-K8S-01` |
| IF-13/14/15 | PASS / Support Review Closed | `P1-DNS-01=Done` |
| IF-13M | P1 N/A / Not Implemented, `.10` 제외 유지 | 도입 시 별도 Change Request |

Endpoint, Protocol, Port, Source Allowlist 설계값은 변경하지 않는다.

## 5. WBS / Gantt 통제

- `FDS_v3.1.16_WBS_and_Gantt_v1.0.xlsx`의 `Team Calendar` 시트에 개인 부재를 기록한다.
- Global Non-working Date는 기존 09-24~09-25, 10-05, 10-09만 유지한다.
- WBS `Lead Workdays`는 Global Non-working Date와 해당 Lead 개인 부재를 제외한다.
- Phase 1 Gantt의 이재환 Lead 작업 09-04 셀은 `L`로 표시한다.
- 상태값은 `To Do`, `In Progress`, `In Review`, `Done`, `Cancelled`만 사용한다.

## 6. 승인 및 배포 판정

| Item | Result |
|---|---|
| 사용자 휴가 입력 승인 | PASS |
| 개인/전사 휴무 구분 | PASS |
| 단독 Lead 종료일 충돌 제거 | PASS |
| G2/G3/Phase 1 Close 유지 | PASS |
| 상태 레지스터 정합성 | PASS |
| Interface Runtime 상태 분리 | PASS |

**D36_VERDICT=APPROVED_AND_RELEASED**

