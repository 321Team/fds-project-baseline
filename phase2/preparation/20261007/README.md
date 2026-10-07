# Phase 2 독립 사전 준비 — 2026-10-07

판정: **사전 준비 착수 / Phase 2 공식 Start·Architecture Freeze·Runtime 인수 미판정**.
작성: 이권욱 작업 지원 / CODEX_ASSISTED. 사용자 요청: Phase 1 미인수 상태에서 기존 사양에 영향 없는 Phase 2 사전 작업을 권장 순서로 수행.

## 적용 기준

- 현행 발행 정본: docs-v3.1.21, 2026-10-04 14:49:12 KST. 발행 기준 커밋 `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- 이번 작업의 main 기준: `c34ca9c12d7cb38d610829cc59460ec6a8d87b1a`. 최신 Issue·승인·기존 코드에서 준비 입력을 정리했다. 조회 대상과 해시는 sources.json에 기록한다.
- [#32 Phase 1 Close](https://github.com/321Team/fds-project-baseline/issues/32)는 OPEN. [#33 공식 Start](https://github.com/321Team/fds-project-baseline/issues/33)는 #32의 잔여·Known Issue/Deferred 인계가 Entry다. 일정 도래만으로 이를 충족했다고 표시하지 않는다.
- 사전 준비는 적용용 사양이 아닌 검토 입력이다. Phase 1 구현·AC·사용 중인 DNS/Harbor/DB/Runner 및 기존 Runtime 설정을 바꾸지 않는다.

## 권장 순서와 이번 수행

| 순서 | 사전 작업 / 연결 티켓 | 이번에 작성·확인한 결과 | 다음 완료조건 / 기존 책임 |
|---|---|---|---|
| 1 | 중앙 IaC/backend/Relay 준비 #35·#37 | 기존 PR147·148, prepare 수신 완료 및 Lead 조건부 GO를 재사용하도록 입력표에 연결 | #35 이하영 판단·소유권, 이권욱 중앙 root 실행. 승인된 4자원만 fresh before→1회 create→exact readback. 실제 생성은 이번 세션 미실행 |
| 2 | 아키텍처·이식성 입력 #34·#38·#43 | 최신 소스의 고정값·참고 snapshot·재사용 경계를 정적 대조. portability-inventory.md 작성 | #38 이하영 platform/SCC 입력, #43 이재환 portable base/overlay. 승인 digest의 admission과 실제 arbitrary UID Running/Ready를 구분 |
| 3 | 관리 DNS·Registry 결정 자료 #40·#42 | input-register.md에 기존 계약과 미확정 값, 영향 없는 준비 범위를 분리 | 이권욱 Decision Lead. route/source·TLS·실제 환경 handoff·비용을 받아 단일안을 결정 |
| 4 | ROSA Delivery 입력 #46 | 현 P1 adapter·workflow의 고정 대상과 P2 변경 지점을 delivery-preparation.md에 정리 | 이권욱. #38/#43/#42의 실제 입력 후 별도 P2 adapter 구현·리뷰. P1 배포 경로를 바꾸지 않고 준비 |
| 5 | 시험·증적 누적 준비 #49·#50 | 승인된 #119와 네트워크 계약을 연결한 16개 case 초안·추적 항목 작성 | #50 이재환 실행/인수, #49 이권욱 최종 집계. 모든 결과 NOT_RUN, 실제 환경·fixture·이미지·승인 작업창에서 검증 |

새 티켓은 만들지 않았다. 위 산출물은 기존 책임 티켓의 준비 입력으로 연결한다. #43/#50 지원 문서를 작성한 것이 담당 변경이나 실행 인수는 아니다.

## 이번 사용자가 제공한 환경 전제

2026-10-07 프로젝트 대화 전제: **코오롱베니트 OCP/RHOAI는 팀 독점 가능한 테스트·검증 자원이며 팀 운영/편입 자원이 아니다. 본 경로는 우리 On-Prem→AWS ROSA 이전이다.**

기존 #33/#34/#38/#43 등과 W0 도구에는 SHARED_OCP_LAB·namespace-local 전제가 남아 있다. 이 차이를 preparation 입력으로 표시하며, 과거 문서를 다시 써서 승인됐던 것처럼 만들지 않는다. 실제 cluster identity·version·관리 권한·허용 장애 범위·복구 책임·초기 상태 보존은 아직 이번 세션에서 확인하지 못했다.

독점 Lab에서 cluster 단위 복구·재현성 시험을 설계할 수 있다. 실제 장애주입·Operator 설치·클러스터 변경은 명확한 시험/복구 범위를 받은 뒤 해당 작업에서 수행한다. Lab 결과는 ROSA HCP/AWS IAM/Hybrid 경로 인수를 대신하지 않는다. 기존 Admission-only 도구의 ENV enum에 새 값을 임의 주입하지 않는다.

## 확인된 정합성 쟁점

1. **#50 일정:** 10-22 하루의 Issue 실행 조건과 승인 전략의 10-21 주 시험 / 10-22 최종 회귀가 다르다. [E2E Lead 요청](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6013423361)을 기존 #47 handoff와 연결해 결정할 항목이다. 이번 case 초안은 날짜를 확정하지 않는다.
2. **DNS 선행순서:** #40은 IP Endpoint 기본·P1 DNS Decision, #48은 Go+G5 이후 capacity다. PR137의 Private 관리 DNS 후보는 Basic Ready 전 필요한 subset을 제안한다. 기존 조건을 유지한 채 차이를 검토 입력으로 남긴다.
3. **ROSA 규모:** #34 최신 Lead 의견은 HCP/m5.xlarge 동의와 1 AZ×3대 제안이다. 기존 후보 3 AZ×1대, N-1/2대 대안과 비용·생명주기 입력은 최종 Freeze 값이 아니다.
4. **비용:** 저장된 $500/$400/$450 정책과 후속 교육장 한도 기반 운영 입력은 모두 출처를 구분한다. 실제 한도·잔여·생성/삭제시각·총 완료비용을 받기 전 Cost GO를 부여하지 않는다.
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

