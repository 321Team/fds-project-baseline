# FDS v3.1.18 Canonical Ticket Update Pack

> Status: CANDIDATE · 기준일: 2026-09-10 · 아직 미발행/미적용

## 적용 순서와 효력

1. Baseline·WBS/Gantt·이 Pack·Description·Manifest를 같은 후보로 독립 검토한다.
2. 이권욱의 명시적 승인 후 병합·정본 발행을 완료한다.
3. 발행된 SHA의 Description 후보와 그때의 실제 Issue 본문/댓글을 다시 대조하여 갱신한다. 수집 이후 운영 기록은 덮어쓰지 않고 보존한다.
4. 실제 Issue Type·Milestone·Label 등은 마지막에 현재 본문으로 새 계획을 생성해 동기화한다. 기존 stale plan은 재사용하지 않는다.

기존 64개 Record ID, Issue 번호, 상태와 담당자는 유지한다. 24건의 계획창은 Fast Tracking 권장안으로 보완하고 기간은 개인 휴가·주말을 제외해 재계산한다. Source·현행 Scope·Schedule Note 보완은 `audit/v3.1.18/property-delta.json`에 전후 값을 기록한다. Done/AC·승인 서명은 새로 생성하지 않는다.

전체 티켓은 64개다. WBS 일정관리 대상은 기존 52개와 종결 Decision 3개를 합한 55개이고, 이전에 Remaining Backlog에서 제외된 종결 티켓 9개는 이 Pack과 Baseline Closed Register로 유지한다. WBS 55개 집계를 전체 Issue 64개 집계로 오인하지 않는다.

## 64개 티켓별 최신 설명 후보

| Record ID | Issue | Status | Start | End | Lead | 설명 후보 |
| --- | --- | --- | --- | --- | --- | --- |
| DEC-P1-FDS-01 | #4 | Done | 2026-09-08 | 2026-09-09 | 이재환 | [DEC-P1-FDS-01](v3.1.18/descriptions/DEC-P1-FDS-01.md) |
| DEC-P1-TXN-01 | #5 | Done | 2026-09-08 | 2026-09-09 | 이재환 | [DEC-P1-TXN-01](v3.1.18/descriptions/DEC-P1-TXN-01.md) |
| DEC-P1-ADMIN-01 | #6 | Done | 2026-09-08 | 2026-09-09 | 이하영 | [DEC-P1-ADMIN-01](v3.1.18/descriptions/DEC-P1-ADMIN-01.md) |
| D-SEC-01 | #7 | Done | 2026-08-26 | 2026-09-01 | 이하영 | [D-SEC-01](v3.1.18/descriptions/D-SEC-01.md) |
| MS-G0-01 | #8 | Done | 2026-08-26 | 2026-09-01 | 이권욱 | [MS-G0-01](v3.1.18/descriptions/MS-G0-01.md) |
| P1-LB-01 | #9 | In Progress | 2026-08-27 | 2026-09-17 | 이권욱 | [P1-LB-01](v3.1.18/descriptions/P1-LB-01.md) |
| P1-K8S-01 | #10 | In Progress | 2026-08-27 | 2026-09-17 | 이하영 | [P1-K8S-01](v3.1.18/descriptions/P1-K8S-01.md) |
| P1-DB-01 | #11 | In Progress | 2026-08-28 | 2026-09-17 | 이재환 | [P1-DB-01](v3.1.18/descriptions/P1-DB-01.md) |
| P1-DNS-01 | #12 | Done | 2026-08-28 | 2026-09-03 | 이권욱 | [P1-DNS-01](v3.1.18/descriptions/P1-DNS-01.md) |
| P1-HBR-01 | #13 | In Progress | 2026-08-31 | 2026-09-17 | 이하영 | [P1-HBR-01](v3.1.18/descriptions/P1-HBR-01.md) |
| ICR-D-NET-01-01 | #14 | In Progress | 2026-09-01 | 2026-09-21 | 이권욱 | [ICR-D-NET-01-01](v3.1.18/descriptions/ICR-D-NET-01-01.md) |
| P1-APP-01 | #15 | In Progress | 2026-09-01 | 2026-09-18 | 이재환 | [P1-APP-01](v3.1.18/descriptions/P1-APP-01.md) |
| P1-CICD-01 | #16 | In Progress | 2026-09-01 | 2026-09-18 | 이권욱 | [P1-CICD-01](v3.1.18/descriptions/P1-CICD-01.md) |
| P1-MON-01 | #17 | In Progress | 2026-09-07 | 2026-09-18 | 이재환 | [P1-MON-01](v3.1.18/descriptions/P1-MON-01.md) |
| MS-G1-01 | #18 | To Do | 2026-09-17 | 2026-09-17 | 이권욱 | [MS-G1-01](v3.1.18/descriptions/MS-G1-01.md) |
| P1-SEC-01 | #19 | In Progress | 2026-09-04 | 2026-09-21 | 이하영 | [P1-SEC-01](v3.1.18/descriptions/P1-SEC-01.md) |
| P1-E2E-01 | #20 | To Do | 2026-09-11 | 2026-09-22 | 이재환 | [P1-E2E-01](v3.1.18/descriptions/P1-E2E-01.md) |
| P1-DR-01 | #21 | To Do | 2026-09-11 | 2026-09-21 | 이재환 | [P1-DR-01](v3.1.18/descriptions/P1-DR-01.md) |
| P1-HA-01 | #22 | To Do | 2026-09-11 | 2026-09-21 | 이재환 | [P1-HA-01](v3.1.18/descriptions/P1-HA-01.md) |
| MS-G2-01 | #23 | To Do | 2026-09-21 | 2026-09-21 | 이하영 | [MS-G2-01](v3.1.18/descriptions/MS-G2-01.md) |
| P1-DOC-01 | #24 | To Do | 2026-09-11 | 2026-09-22 | 이권욱 | [P1-DOC-01](v3.1.18/descriptions/P1-DOC-01.md) |
| P1-MON-02 | #25 | To Do | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 | 이재환 | [P1-MON-02](v3.1.18/descriptions/P1-MON-02.md) |
| P1-DR-02 | #26 | To Do | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 | 이하영 | [P1-DR-02](v3.1.18/descriptions/P1-DR-02.md) |
| P1-HA-02 | #27 | To Do | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 | 이하영 | [P1-HA-02](v3.1.18/descriptions/P1-HA-02.md) |
| DEC-CAL-P1-01 | #28 | To Do | 2026-09-11 | 2026-09-11 | 이권욱 | [DEC-CAL-P1-01](v3.1.18/descriptions/DEC-CAL-P1-01.md) |
| MS-G3-01 | #29 | To Do | 2026-09-22 | 2026-09-22 | 이권욱 | [MS-G3-01](v3.1.18/descriptions/MS-G3-01.md) |
| P1-REV-01 | #30 | To Do | 2026-09-22 | 2026-09-23 | 이권욱 | [P1-REV-01](v3.1.18/descriptions/P1-REV-01.md) |
| MS-P1-REVIEW-01 | #31 | To Do | 2026-09-22 | 2026-09-22 | 이권욱 | [MS-P1-REVIEW-01](v3.1.18/descriptions/MS-P1-REVIEW-01.md) |
| MS-P1-CLOSE-01 | #32 | To Do | 2026-09-23 | 2026-09-23 | 이권욱 | [MS-P1-CLOSE-01](v3.1.18/descriptions/MS-P1-CLOSE-01.md) |
| MS-P2-START-01 | #33 | To Do | 2026-09-28 | 2026-09-28 | 이권욱 | [MS-P2-START-01](v3.1.18/descriptions/MS-P2-START-01.md) |
| P2-ARC-01 | #34 | To Do | 2026-09-28 | 2026-09-28 | 이권욱 | [P2-ARC-01](v3.1.18/descriptions/P2-ARC-01.md) |
| P2-IAC-01 | #35 | To Do | 2026-09-28 | 2026-10-08 | 이권욱 | [P2-IAC-01](v3.1.18/descriptions/P2-IAC-01.md) |
| P2-OCI-01 | #36 | To Do | 2026-09-28 | 2026-10-02 | 이권욱 | [P2-OCI-01](v3.1.18/descriptions/P2-OCI-01.md) |
| P2-VPN-01 | #37 | To Do | 2026-10-01 | 2026-10-08 | 이권욱 | [P2-VPN-01](v3.1.18/descriptions/P2-VPN-01.md) |
| P2-ROSA-01 | #38 | To Do | 2026-10-06 | 2026-10-16 | 이하영 | [P2-ROSA-01](v3.1.18/descriptions/P2-ROSA-01.md) |
| MS-G4-01 | #39 | To Do | 2026-10-08 | 2026-10-08 | 이권욱 | [MS-G4-01](v3.1.18/descriptions/MS-G4-01.md) |
| DEC-P2-DNS-01 | #40 | To Do | 2026-10-12 | 2026-10-16 | 이권욱 | [DEC-P2-DNS-01](v3.1.18/descriptions/DEC-P2-DNS-01.md) |
| DEC-P2-OP-01 | #41 | To Do | 2026-10-12 | 2026-10-16 | 이하영 | [DEC-P2-OP-01](v3.1.18/descriptions/DEC-P2-OP-01.md) |
| DEC-P2-REG-01 | #42 | To Do | 2026-10-12 | 2026-10-16 | 이하영 | [DEC-P2-REG-01](v3.1.18/descriptions/DEC-P2-REG-01.md) |
| P2-APP-01 | #43 | To Do | 2026-10-12 | 2026-10-16 | 이재환 | [P2-APP-01](v3.1.18/descriptions/P2-APP-01.md) |
| P2-OADP-01 | #44 | To Do | 2026-10-15 | 2026-10-22 | 이하영 | [P2-OADP-01](v3.1.18/descriptions/P2-OADP-01.md) |
| MS-G5-01 | #45 | To Do | 2026-10-16 | 2026-10-16 | 이하영 | [MS-G5-01](v3.1.18/descriptions/MS-G5-01.md) |
| P2-CICD-01 | #46 | To Do | 2026-10-16 | 2026-10-19 | 이권욱 | [P2-CICD-01](v3.1.18/descriptions/P2-CICD-01.md) |
| P2-HYB-01 | #47 | To Do | 2026-10-16 | 2026-10-22 | 이재환 | [P2-HYB-01](v3.1.18/descriptions/P2-HYB-01.md) |
| P2-DNS-01 | #48 | To Do | 2026-10-19 | 2026-10-20 | 이권욱 | [P2-DNS-01](v3.1.18/descriptions/P2-DNS-01.md) |
| P2-DOC-01 | #49 | To Do | 2026-10-19 | 2026-10-23 | 이권욱 | [P2-DOC-01](v3.1.18/descriptions/P2-DOC-01.md) |
| P2-E2E-01 | #50 | To Do | 2026-10-19 | 2026-10-22 | 이재환 | [P2-E2E-01](v3.1.18/descriptions/P2-E2E-01.md) |
| P2-OP-01 | #51 | To Do | 2026-10-19 | 2026-10-20 | 이하영 | [P2-OP-01](v3.1.18/descriptions/P2-OP-01.md) |
| DEC-CAL-P2-01 | #52 | To Do | 2026-10-22 | 2026-10-22 | 이권욱 | [DEC-CAL-P2-01](v3.1.18/descriptions/DEC-CAL-P2-01.md) |
| MS-G6-01 | #53 | To Do | 2026-10-22 | 2026-10-22 | 이권욱 | [MS-G6-01](v3.1.18/descriptions/MS-G6-01.md) |
| MS-DELIVERABLE-FREEZE-01 | #54 | To Do | 2026-10-23 | 2026-10-23 | 이권욱 | [MS-DELIVERABLE-FREEZE-01](v3.1.18/descriptions/MS-DELIVERABLE-FREEZE-01.md) |
| P2-REV-01 | #55 | To Do | 2026-10-23 | 2026-10-26 | 이권욱 | [P2-REV-01](v3.1.18/descriptions/P2-REV-01.md) |
| MS-P2-REVIEW-01 | #56 | To Do | 2026-10-23 | 2026-10-23 | 이권욱 | [MS-P2-REVIEW-01](v3.1.18/descriptions/MS-P2-REVIEW-01.md) |
| MS-PROJECT-CLOSE-01 | #57 | To Do | 2026-10-26 | 2026-10-26 | 이권욱 | [MS-PROJECT-CLOSE-01](v3.1.18/descriptions/MS-PROJECT-CLOSE-01.md) |
| CR-P1-ANS-01-01 | #58 | Done | 2026-09-04 | 2026-09-07 | 이권욱 | [CR-P1-ANS-01-01](v3.1.18/descriptions/CR-P1-ANS-01-01.md) |
| D-ARC-01 | #59 | Done | 원본 속성 미확인 | 원본 속성 미확인 | 이권욱 | [D-ARC-01](v3.1.18/descriptions/D-ARC-01.md) |
| D-NET-01 | #60 | Done | 2026-08-24 | 2026-08-26 | 이권욱 | [D-NET-01](v3.1.18/descriptions/D-NET-01.md) |
| D-WBS-01 | #61 | Done | 원본 속성 미확인 | 원본 속성 미확인 | 이권욱 | [D-WBS-01](v3.1.18/descriptions/D-WBS-01.md) |
| DEC-P1-ENTRY-01 | #62 | Done | 2026-08-27 | 2026-08-31 | 이권욱 | [DEC-P1-ENTRY-01](v3.1.18/descriptions/DEC-P1-ENTRY-01.md) |
| DEC-P1-MON-01 | #63 | Done | 2026-08-31 | 2026-08-31 | 이권욱 | [DEC-P1-MON-01](v3.1.18/descriptions/DEC-P1-MON-01.md) |
| DEC-P1-TLS-01 | #64 | Done | 2026-08-27 | 2026-08-31 | 이권욱 | [DEC-P1-TLS-01](v3.1.18/descriptions/DEC-P1-TLS-01.md) |
| P1-ANS-01 | #65 | Done | 2026-08-27 | 2026-09-01 | 이권욱 | [P1-ANS-01](v3.1.18/descriptions/P1-ANS-01.md) |
| P1-LNX-01 | #66 | Done | 2026-08-24 | 2026-08-26 | 이권욱 | [P1-LNX-01](v3.1.18/descriptions/P1-LNX-01.md) |
| P1-NET-01 | #67 | Done | 2026-08-27 | 2026-08-27 | 이권욱 | [P1-NET-01](v3.1.18/descriptions/P1-NET-01.md) |

## 반영된 핵심 교정

- CR-P1-ANS-01-01 Done, Ansible PR #3·#4 병합과 운영 Issue #10 종결의 범위를 구분한다.
- Decision #4~6은 현행 유지/신규 확대 유예의 종결로 통합한다. 새 거래 보류·상태/API·운영 UI·보안 정책값을 도입하지 않는다.
- P1-HBR/P1-SEC의 실제 In Progress와 Runtime HOLD를 반영한다.
- P1-MON-01은 Runtime Acceptance 14개 + 필수 보조통제 2개다. P1-MON-02는 기존 P1 고도화 범위로 복원한다.
- Stage A 조건부 인수, 현재 Permanent 수신·편입과 잔여 인수 조건을 분리한다. CP1 Ready/사전 점검을 3CP+3Worker PASS로 확대하지 않는다.
- 임시 k3s/fds 실증, 정본 fds-app/monitoring-api 목표, 문서/코드 검증, 실제 Runtime을 구분한다.

## 보존한 예외와 판단 대기

- #59 D-ARC-01·#61 D-WBS-01의 원본 미확인 속성은 추정하지 않는다. 역사적 Done을 취소하지 않는다.
- 기존 Milestone HOLD 20건과 #46의 End/G5 충돌은 별도 판단 대상이다. 후보 발행으로 매핑 완료를 선언하지 않는다.
- P1-DR-01의 사전 착수 보고만으로 상태를 변경하지 않는다. 기존 To Do와 Runtime 미완료를 유지한다.
- DB 시간대/Timestamp 계약·배포와 소스 연결, OID-01/02/03, NTP 목적지, FUP 잔여 원본/승인 참조는 미확정 상태를 보존한다.

이 후보의 정합성 PASS는 Release 승인·운영 Gate 해제와 구분한다. 배포 자산과 독립 리뷰가 준비돼도 명시적 merge 승인 전에는 발행하지 않는다.

## 2026-09-10 추가 반영

- 이하영 09-10 면접 휴가를 추가하고 09-08 기록은 유지한다. P1-SEC-01 가용 작업일은 기존 후보 5→4일(원래 Issue 속성 6→4)이다. 이는 기존 계획창 09-04~11의 계산이다. Fast Tracking 권장창 09-04~21의 가용일은 10일이며 잔여 공수가 아니다. 담당·상태는 유지한다.
- ICR과 K8S에 Worker/NTP 검토를 추가한다. PR #2는 같은 HEAD의 Ready for review / 이하영 리뷰 요청 상태다. PR #3은 3309866766236bbdbe20b9e2ae1d8fd6f9233bcd의 Draft다.
- Worker 수집은 무결성 PASS / 완전성 PARTIAL / 운영 인수 HOLD. 시간 속성 공백, CP→Worker 0/9, kubelet listener 부재·auto-restart, Cockpit 허용·mask 및 NTP 승인 미완료를 기록한다. Worker→LB TCP 3/3은 부분 증적이다.
- 이번 반영은 고정된 검토 기록의 문서 동기화다. 실제 v1.1 supplement·canary·join·보호 인계 실행 또는 승인 완료를 의미하지 않는다.
- ICR은 이권욱 Lead·이하영 Support, In Progress와 실제 종료 미확정을 유지한다. 기존 End TBD는 이력에 보존하고 이번 권장 Plan End만 09-21로 제안한다. 09-10 휴가는 지원·독립 리뷰 일정 영향으로 관리한다.
- 상세 원문·출처: `audit/v3.1.18/followup-20260910.json`. 기존 원본 스냅샷과 당시 판정은 보존한다.

## Fast Tracking 및 주말 제약 반영

주말 교육장 가용량은 0이다. G1 09-17 오후 → G2 09-21 오후 → G3 09-22 오전 → Review 09-22 오후 → Close 09-23 오후를 조건부 권장한다. 09-23 오전 1.5인일을 보완 버퍼로 남긴다. 실제 잔여공수와 인계 품질 확인 전에는 09-23 성공을 확약할 수 없다.

이번 Start/End 변경은 사용자 요청에 따른 일정 권장안이며 승인된 실행 실적이 아니다. 기존 일정 전후 값은 `audit/v3.1.18/fast-track-plan.json`, 실제 본문·댓글은 원본 스냅샷으로 보존한다. Record ID·상태·Lead·Support·AC·승인 기록은 유지한다.

- 기존 8개 WBS 탭 보존 + Fast Track Plan 추가(총 9개), 54개 AM/PM·담당 배정.
- 미착수 P1-MON-02/DR-02/HA-02 구현 유예, P0 AC 전부 유지.
- Phase 2 Review도 10-24 토요일에서 10-23 금요일 오후로 권장한다.
- 상세: `releases/v3.1.18/FDS_Phase1_Fast_Track_Schedule_Recommendation_v1.0.md`, 원본/전후/배정: `audit/v3.1.18/fast-track-plan.json`.
