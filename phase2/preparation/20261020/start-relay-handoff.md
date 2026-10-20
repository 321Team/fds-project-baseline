# #33 Start·#36 D21·#39 G4 인계 보완

기존 [Start 입력표](https://github.com/321Team/fds-project-baseline/issues/33#issuecomment-6270090544),
[D21 대장](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-6270089032)을 재사용한다.
원본/서명/OCI 시험을 새로 요구하지 않으며 이번에는 아래 delta만 연결한다.

| 항목 | 현재 근거·소비 | 남은 책임·완료조건 |
|---|---|---|
| #33 원 Entry | #32 Phase1 Close·기존 KI/Approved Deferred, #34 Architecture Freeze, docs-v3.1.22 실제 발행 수신은 기존 기록대로 충족 | 공식 Start의 원 Entry/Exit·Decision/Risk 최종 판정은 권욱. 준비표 자체를 소급 착수 GO·완료일로 만들지 않음 |
| 일정·비용 입력 delta | Review 10/23 18:00~19:30 세 명 가능, 10/26 Close 유지. 승인 규모 유지의 별도 시간/작업별 비용 제한 없음, 교육장 리포트 중앙 추적 | [Review 운영계획](review-plan.md)·지정 비용 세션 적용. 예전 14시 제안/참석 미정·중복 비용 대기를 현재 차단으로 복제하지 않음 |
| 환경 경계 | 실제 소비는 ROSA `fds-app`, `rosa-app`은 overlay. Phase1 자원 일괄 금지 해제, 개별 GO/AC·공용 Lab 관리자 제약 유지 | 공용 OCP를 실제 사용할 때의 TeamCode/namespace·제약 계약은 그 환경에 적용. ROSA 결과와 Lab-precheck를 혼합하지 않음 |
| #36 선택 | OCI Primary project-suitability NO-GO, **AWS EC2+EIP self-managed Libreswan Relay FINAL** 유지 | #35/#37은 기존 단일 transport 계약 소비. 새 OCI 구축/대안 재선택/전체 재시험 불필요 |
| #36 증적·한계 | final responder 원본 수신/편입 ev161 기존 완료. 정확한 전체 명령·RC·도구 버전 및 일부 initiator/cleanup raw의 미수집 한계 보존 | 권욱은 원 AC별 한계를 인계. 추가 실제 원본이 있을 때만 변경분 수신/검토. hash 일치를 tunnel/AC 성공으로 확대하지 않음 |
| #39 actual delta | [창 A 후속](https://github.com/321Team/fds-project-baseline/issues/39#issuecomment-6288503072): T1/T3 PASS, T3-R 성공 보고, T6 INCONCLUSIVE, W4/P9/P8/V9 정리 보고, #7 B/A·N3 미실행 | 재환 창 A 편입 PR·하영/재환 잔여 시험 또는 원 AC 처분 근거→권욱 G4 판정. G4 아직 In Progress |

#33/#36의 기존 In Progress를 유지한다. 일정/소스/증적 정리와 Milestone/전체 AC 인수·티켓 종결은 구분한다.
#40/#48/#120의 승인된 Deferred와 기존 Known Issue·이월 Risk의 Owner/기한/재검토 trigger를 보존한다.
