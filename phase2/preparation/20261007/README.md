# Phase 2 독립 사전 준비 — 2026-10-07

판정: **사전 준비 착수 / Phase 2 공식 Start·Architecture Freeze·Runtime 인수 미판정**.
작성: 이권욱 작업 지원 / CODEX_ASSISTED. 사용자 요청: Phase 1 미인수 상태에서 기존 사양에 영향 없는 Phase 2 사전 작업을 권장 순서로 수행.

## 적용 기준

2026-10-08 후속: [Phase 2 전용 실행 준비](../20261008/README.md)를 소비한다. 사용자 지시에 따라 이번 후속에서 Phase 1 작업은 제외하며, 기존 자료의 역사 기록과 현재 실행 입력을 구분한다.

- 현행 발행 정본: docs-v3.1.21, 2026-10-04 14:49:12 KST. 발행 기준 커밋 `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- 사전 준비 최초 main 기준은 `c34ca9c12d7cb38d610829cc59460ec6a8d87b1a`이며, 이번 시험전략 개정/동기화 기준은 `40ac664b83485745ab86b5018b8e19c386484cc8`이다. 과거 sources.json은 이력으로 보존하고 최신 조회는 audit/phase2-test-plan-20261007/sources.json에 기록한다.
- [#32 Phase 1 Close](https://github.com/321Team/fds-project-baseline/issues/32)는 OPEN. [#33 공식 Start](https://github.com/321Team/fds-project-baseline/issues/33)는 #32의 잔여·Known Issue/Deferred 인계가 Entry다. 일정 도래만으로 이를 충족했다고 표시하지 않는다.
- 사전 준비는 적용용 사양이 아닌 검토 입력이다. Phase 1 구현·AC·사용 중인 DNS/Harbor/DB/Runner 및 기존 Runtime 설정을 바꾸지 않는다.

## 권장 순서와 이번 수행

| 순서 | 사전 작업 / 연결 티켓 | 이번에 작성·확인한 결과 | 다음 완료조건 / 기존 책임 |
|---|---|---|---|
| 1 | 중앙 IaC/backend/Relay 준비 #35·#37 | 기존 PR147·148, prepare 수신 완료 및 Lead 조건부 GO를 재사용하도록 입력표에 연결 | #35 이하영 판단·소유권, 이권욱 중앙 root 실행. 승인된 4자원만 fresh before→1회 create→exact readback. 새 원본 #35 6031865288: 중앙 4자원 CREATE_COMPLETE/PASS_USER_READBACK 수신; full IaC/Stage-A는 별도 |
| 2 | 아키텍처·이식성 입력 #34·#38·#43 | 최신 소스의 고정값·참고 snapshot·재사용 경계를 정적 대조. portability-inventory.md 작성 | #38 이하영 platform/SCC 입력, #43 이재환 portable base/overlay. 승인 digest의 admission과 실제 arbitrary UID Running/Ready를 구분 |
| 3 | 관리 DNS·Registry 결정 자료 #40·#42 | input-register.md에 기존 계약과 미확정 값, 영향 없는 준비 범위를 분리 | 이권욱 Decision Lead. route/source·TLS·실제 환경 handoff·비용을 받아 단일안을 결정 |
| 4 | ROSA Delivery 입력 #46 | 현 P1 adapter·workflow의 고정 대상과 P2 변경 지점을 delivery-preparation.md에 정리 | 이권욱. #38/#43/#42의 실제 입력 후 별도 P2 adapter 구현·리뷰. P1 배포 경로를 바꾸지 않고 준비 |
| 5 | 시험·증적 누적 준비 #49·#50 | 승인된 #119와 네트워크 계약을 연결한 16개 case 초안·추적 항목 작성 | #50 이재환 실행/인수, #49 이권욱 최종 집계. 모든 결과 NOT_RUN, 실제 환경·fixture·이미지·승인 작업창에서 검증 |

새 티켓은 만들지 않았다. 위 산출물은 기존 책임 티켓의 준비 입력으로 연결한다. #43/#50 지원 문서를 작성한 것이 담당 변경이나 실행 인수는 아니다.

## 최신 Shared Lab / 실제 Target 경계

2026-10-07 최신 사용자 지시와 [#95 실측 댓글](https://github.com/321Team/fds-project-baseline/issues/95#issuecomment-6032524902)을 적용한다. **Kolon Benit OCP는 Shared/Test Lab이며 실제 Target은 우리 On-Prem→AWS/ROSA다.** 이전 PR 초안의 독점 전제는 현재 실행 입력으로 사용하지 않는다.

```text
Kolon Benit OCP = LAB-PRECHECK / COMPATIBILITY / REHEARSAL
AWS/ROSA = P0 IMPLEMENTATION / RUNTIME / ACCEPTANCE
```

기술적 cluster-admin 권한은 독점·Operator 설치·공용 cluster 장애주입 승인과 다르다. 기존 namespace-local·Quota/Owner·cleanup 경계를 유지한다. [Shared Lab 리허설 준비](shared-lab-rehearsal-preparation.md)를 사용하며 RHOAI는 read-only·RESOURCE_GATE=FAIL·Deferred 권고다. Lab PASS를 ROSA Runtime/인수·Migration Complete·G5/G6 Exit로 승격하지 않는다.

최신 [Test Strategy](../../../tests/FDS_Phase2_Test_Strategy_20261007.md)와 [Test Plan](../../../tests/FDS_Phase2_Test_Plan_20261007.md)은 P0/P1·TS01~16·Gate/증적을 기존 AC에 매핑한다. 16 case TSV는 APP/E2E/Delivery의 일부이며 전체 시험범위를 대신하지 않는다.
발행 v3.1.21은 보존하고 PR150 검토 입력으로 갱신한다. 기존 sources.json/verification.json은 14:14 시점의 이력이다. 이번 조회·검증은 [새 기록](../../../audit/phase2-test-plan-20261007/README.md)을 따른다.

## 확인된 정합성 쟁점

1. **#50 일정:** 10-22 하루의 Issue 실행 조건과 승인 전략의 10-21 주 시험 / 10-22 최종 회귀가 다르다. [E2E Lead 요청](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6013423361)을 기존 #47 handoff와 연결해 결정할 항목이다. 이번 case 초안은 날짜를 확정하지 않는다.
2. **DNS 선행순서:** #40은 IP Endpoint 기본·P1 DNS Decision, #48은 Go+G5 이후 capacity다. PR137의 Private 관리 DNS 후보는 Basic Ready 전 필요한 subset을 제안한다. 기존 조건을 유지한 채 차이를 검토 입력으로 남긴다.
3. **ROSA 규모:** 사용자 선택은 1 AZ·m5.xlarge 3대와 worker 1대 장애·복구 시험이다. actual worker subnet/AZ·platform egress·N-1 용량과 최종 Freeze/생성 GO는 별도 입력이다. AZ 전체 장애 대응은 새 P0가 아니다.
4. **비용:** 교육장 지원은 확정, 자부담0·목표400/중단450/상한USD500 유지. 사용액·예상 총비용 모두 교육장 리포트 기준이며 총비용에 사용액을 다시 더하지 않는다. 지원 재확인·Billing 접근·자체 견적을 선행조건으로 요구하지 않는다. 보고 금액 미수신은 NOT_ASSESSED이며 독립 사전 준비는 계속한다.
5. **Phase 1 DB 잔여:** #47의 db01 방화벽·pg_hba·edge01 k3s 정리 3건은 현재 P1 경로를 끊을 수 있다. #19 이관 조건 전 이번 무영향 사전 작업에 포함하지 않는다.

## 진행과 종료 기준

현재 할 일은 위 준비 산출물을 검토 입력으로 소비하고, 환경 또는 source가 변경된 항목만 갱신하는 것이다. 이미 통과한 중앙 prepare·14건 시험·46/9 simulation을 이 문서 작성을 이유로 반복하지 않는다.

실제 실행 전: 대상·권한·source SHA/digest·선행조건·정상/중단 기준·이전 상태 복구를 해당 기존 Runbook/티켓에서 고정한다. 자격증명·kubeconfig·Secret 값은 준비 문서에 넣지 않는다.

- STATIC: 문서/소스/티켓 대조 및 파일 정합성 확인
- MOCK·신규 CI: NOT_RUN (문서 준비만 수행)
- AWS/OCP/ROSA/P1 서버 RUNTIME: NOT_RUN
- REVIEW: 담당 검토 입력, 독립 승인으로 표시하지 않음
- MERGE·정본 PUBLICATION·AC 인수/티켓 종결: NOT_RUN

브랜치·Draft PR 게시 결과는 실제 GitHub 응답으로 별도 보고한다. 이 준비 문서는 적용 코드·새 정책·정본 발행물로 사용하지 않는다.

