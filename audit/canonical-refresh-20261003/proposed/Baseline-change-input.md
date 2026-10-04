# v3.1.21 Baseline 재생성 변경 입력

기준: docs-v3.1.20 RELEASED. 수집 2026-10-03T11:53:07.711+09:00. 이 문서는 변경 입력이며 전체 Baseline을 대체하지 않는다.

- 발행 이후 14개 저장소 병합 입력 257건( main 계보 255건, 후보 동기화 2건). 기존 intake 대비 144건 추가.
- #110: Done/closed(completed) Decision 완료를 반영. Delivery Runtime 완료와 분리.
- #125: accepted/completed; encryption·backup·rollback P1 유지, preventive rotation NOT MET/RISK ACCEPTED.
- #126: withdrawn/no change; 원 AC 유지.
- #127: rejected/no change; source-preservation 필수 유지.
- #128: withdrawn/no AC change. MTU/identity 수용은 기존 #10 evidence interpretation. Body Status Todo drift는 미해소.
- #130: CHG01/02 accepted/completed; #14 OID-02 추적 및 #13 AC05A/05B 생산·인수 분리, HBR end-to-end gate 유지.
- 일정: D21 10-08 → #34 최종 Freeze 10-08 → #35 Stage-A 10-08(조건부) → #37 10-12. 잔여 사양/당일 작업창은 미검증.
- D21 preferred AWS EC2/EIP Relay는 후보이며 확정 사양 아님. UDP 경로 관측, security/return-route/SPOF 결정 전 임의 승격 금지.
- Phase 1 Close 10-06 결과는 아직 없음. phase1-close-input.json에 실제 판정/원본 증적 수신 후 반영.
- 기존 v3.1.20 정본/Tag/Assets 및 CURRENT.md 불변. WBS 58행은 78개 Issue 입력과 전량 대조 필요.

상세 원문은 snapshot.zip, 해시는 issue-index.json, 다음 생성 규칙은 regeneration-plan.json 참조.
