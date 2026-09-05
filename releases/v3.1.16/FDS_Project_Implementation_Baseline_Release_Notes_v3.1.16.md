# FDS Project Implementation Baseline v3.1.16 Release Notes

> **Release Date:** 2026-09-03  
> **Release Type:** Schedule / Availability / Status Synchronization  
> **Decision:** D36 — Fixed / User Approved  
> **Supersedes:** v3.1.15 as active baseline

---

## 1. 릴리즈 목적

이재환의 2026-09-04 개인 사정 휴가를 WBS와 Gantt에 반영하고, 실제 진행 결과에 따라 P1-DNS-01, P1-K8S-01, P1-LB-01 상태 및 관련 Interface Runtime State를 정본화한다.

## 2. 주요 변경

### Team Availability

- 이재환: 2026-09-04 개인 휴가 추가
- 이재환: 기존 2026-09-14~09-17 예비군 유지
- 개인 부재와 팀 공통 Non-working Date를 분리
- WBS `Lead Workdays`를 Lead별 부재 기준으로 계산

### Schedule

| Record | Previous | v3.1.16 |
|---|---|---|
| `P1-DB-01` End | 09-04 | **09-07** |
| `MS-G1-01` | 09-04 | **09-07** |
| `P1-APP-01` End | 09-09 | **09-10** |
| `P1-MON-01` Start | 09-04 | **09-07** |

G2 09-11, G3 09-18, Phase 1 Close 09-23은 변경하지 않는다.

### Ticket Status

- `P1-DNS-01`: In Review → **Done**
- `P1-K8S-01`: To Do → **In Progress**
- `P1-LB-01`: **In Progress 유지** — Stage A PASS, Stage B Pending

### Interface Runtime State

- IF-11: Stage A Runner TCP Positive PASS
- IF-11A: Stage A Node Positive 6/6 PASS 및 `.10` Negative PASS
- IF-12: Pre-bootstrap Reachability PASS / Stage B Pending 유지
- IF-13/14/15: PASS / Support Review Closed
- IF-13M: P1 N/A / 미구현 유지

## 3. 신규/갱신 산출물

| File | Action |
|---|---|
| `FDS_Project_Implementation_Baseline_v3.1.16.md` | New active baseline |
| `D36_Team_Availability_and_Status_Update_Record_v1.0.md` | New decision record |
| `FDS_v3.1.16_WBS_and_Gantt_v1.0.xlsx` | New canonical WBS/Gantt |
| `FDS_v3.1.16_Canonical_Ticket_Update_Pack_v1.0.md` | New ticket upsert source |
| `FDS_Project_Implementation_Baseline_Release_Notes_v3.1.16.md` | New release notes |
| `FDS_Document_Distribution_Manifest_v3.1.16.md` | New integrity manifest |

## 4. 운영상 주의

- `P1-LB-01`은 Stage B 완료 전 Done으로 변경하지 않는다.
- 09-04는 팀 공통 휴무가 아니므로 다른 Lead의 일정 계산에서 제외하지 않는다.
- G1의 09-07 이동은 G2/G3/Phase 1 Close를 자동 이동시키지 않는다.
- 이후 실제 지연이 발생하면 별도 Change Request로 재기준선화한다.

## 5. 검증 결과

- WBS planning record count: 51
- Status: Done 3 / In Progress 6 / In Review 0 / To Do 42
- Phase 1 Gantt leave markers: 3 (`P1-DB-01`, `P1-APP-01`, `P1-MON-01`)
- Personal absence rows: 6
- Global Non-working Date 변경: 0
- Formula error: 0

**RELEASE_VERDICT=APPROVED_FOR_DISTRIBUTION**

