# FDS v3.1.18 Release Notes

> CANDIDATE · 2026-09-10 · 현재 RELEASED v3.1.17

## 변경 이유

v3.1.17 발행 이후 DNS CR·Ansible 후속 변경·Decision 종결·모니터링 사전 실증·보안/Harbor 착수가 누적됐다. 기존 티켓 설명과 WBS가 이 사실을 동일하게 표현하지 않아, 메타데이터 동기화보다 먼저 전체 정본 후보를 정리한다.

## 변경 내용

- Baseline에 실제 승인·merge와 미완료 Runtime·인수 조건을 구분해 통합했다. Stage A 조건부 인수와 CP1 사전 진단은 전체 Bootstrap 완료가 아니다.
- 원본 Issue 64개의 본문·댓글 스냅샷과 64개 Description 후보를 Record ID로 연결했다. 원래 실행 이력·AC·상태·Lead/Support·계획일을 보존하며 실제 Issue는 갱신하지 않았다.
- WBS 기존 8개 탭을 보존하고 Fast Track Plan을 추가한 총 9개 탭으로 구성했으며 기존 52개 계획 레코드에 종결 Decision 3개를 포함했다. 이력 관리 대상 9개는 Baseline/Ticket Pack에 보존한다.
- 계획 55건: Done 7 / In Progress 9 / In Review 0 / To Do 39. 전체 64건: Done 16 / In Progress 9 / To Do 39.
- P1-HBR-01·P1-CICD-01·P1-SEC-01을 현재 In Progress로 반영했다. 수식 범위·집계·Milestone/Decision 표시를 확장했다.
- Team Calendar의 이하영 09-08·09-10 부재를 작업일 계산에 포함했다. P1-SEC-01은 최초 속성 6일→09-08 반영 5일→09-10 추가 반영 4일, DEC-P1-ADMIN-01은 2→1일이다. 이후 사용자 재편성 요청으로 아래 Fast Tracking 권장 계획을 추가했다.
- P1-MON-01의 14개 Runtime AC + 필수 보조통제 2개를 구분했다. P1-MON-02는 D33의 HA·Dashboard/Alert·장기 보존 고도화 범위를 복원하고 검토용 AC를 구체화했다.
- 기존 PR #3·#68의 배포 통제·속성 정책·검증 도구를 통합 후보에 포함했다. 기존 PR은 별도 이력으로 남긴다.

## 검토가 필요한 후보 교정

1. K8S/ICR의 과거 일괄 firewalld OFF 순서와 현재 canary·보호 전환 조건의 충돌을 해소하는 문구를 제안한다. D34 목표는 유지하고 실제 Source·실행 승인 없이 노드를 변경하지 않는다.
2. P1-MON-02 고도화 AC의 상세화는 독립 리뷰 대상이다. 09-12~18 중 Lead 가용일은 1일이므로 실행 가능성·일정 판단을 별도로 남긴다.
3. 기존 G1 09-07 미달성을 보존하고 사용자 요청에 따라 09-17 오후 목표를 권장한다. Gate 상태와 Acceptance는 유지한다.

## 잔여·예외

- #59/#61의 원본 미확인 속성, Milestone HOLD 20건과 #46 End/G5 충돌을 유지한다.
- DB Timestamp/시간대·실제 배포와 Source 연결, OID/NTP 목적지, FUP 원본/인수 참조는 후속 확인 대상이다.
- k3s 사전 실증은 담당자 보고다. 이번 작업은 실서버 시험·독립 Runtime 재검증이 아니다.
- 과거 Task Type 34건 적용·카탈로그 생성 이후 native 적용은 stale plan에서 중단됐다. 최종 속성 동기화는 아직 완료되지 않았다.

## 검증과 발행

후보의 구체적 검증 결과는 `audit/v3.1.18/validation.json` 및 `audit/FDS_Canonical_Integrity_Audit_v3.1.18.md`를 따른다. 체크섬은 `releases/v3.1.18/SHA256SUMS`에서 파일 단위로 검증한다.

독립 리뷰와 이권욱의 명시적 merge 승인 후 content merge / finalization / tag / Release Asset 검증을 수행한다. 현재 `CURRENT.md`와 v3.1.17 파일·태그·Release는 유지한다. ZIP은 Git에 중복 보관하지 않으며 외부 생성한 후보 ZIP과 sidecar를 검토 자료로 제공한다. 발행된 독립 WBS Asset 검증과 CI는 이번 로컬 검증에 포함되지 않는다.

발행 후 순서는 **티켓 Description의 최신 운영 delta 대조·갱신 → 매핑 재작성 → 새 plan 검토·적용 → 재조회**다. 이전 fingerprint를 덮어써서 stale 검사를 우회하지 않는다.

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
