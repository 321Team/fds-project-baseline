# Phase 2 Start / G4 인수 사전 준비

조회 기준: 2026-10-08 02:00 KST. 작성: 이권욱 작업 지원, CODEX_ASSISTED.

**현재 준비도: #33 공식 Start 승인 근거 미확인 / #39 G4 실제 인수 입력 미완료.** 이 문서는 기존 조건에 대한 추적표이며, Lead의 Gate 판정·예외 승인·Runtime GO·정본 발행을 대신하지 않는다.

- [Start 입력과 Close 인계](start-readiness.md)
- [G4 생산·수신·검증표](g4-readiness.md)
- [조회 출처와 범위](sources.json)

## 기준과 사용자 확정 입력

발행 기준은 `docs-v3.1.21 / 979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`, 작업 기준 baseline main은 `81365568fd0b946ad93e4d82ae8191add5fcacd0`이다. 조회한 Issue 본문과 후속 결정 댓글을 함께 대조했다. 과거 본문에 남은 오래된 일정을 최신 값으로 복제하지 않는다.

1. **공용 OCP:** 이권욱의 2026-10-08 답변은 “Team Code·Namespace 및 관리자 제약 모두 없음”이다. 해당 값은 사용자 확인값 `NONE_REPORTED`로 기록하며 추가 입력 대기로 두지 않는다. 실제 API 권한·quota를 조회한 결과는 아니다. 기존 Shared Lab과 실제 AWS/ROSA 인수 환경 구분은 유지한다. 이 답변만으로 새 자원 생성·공용 cluster 변경·장애주입을 수행하지 않는다. 실제 Lab 시험 시 대상 자원을 정하는 것은 실행 준비이며 공식 Start의 별도 명명 승인 Gate로 추가하지 않는다.
2. **일정:** [#52의 9월 30일 결정](https://github.com/321Team/fds-project-baseline/issues/52#issuecomment-5907902770)에 따라 G4 10-14, G5 10-20, G6 10-22, Review/Freeze 10-23, Close 10-26을 사용한다. 10-09와 주말은 비근무다. 10-23 Review 시간·참석자는 사용자 답변대로 미정이며 날짜 미확정과 구분한다. 이번 작업은 일정 재승인이 아니다.
3. **비용:** 교육장 지원은 이미 진행 중이다. 사용액과 예상 **총비용** 모두 교육장 리포트 금액으로 추적한다. 총비용에 사용액을 다시 더하지 않는다. 기존 USD400 목표 / 450 중단 / 500 상한 / 예비비 50, 자부담 0을 유지한다. 리포트가 없으면 `NOT_ASSESSED`이며 0원·초과·PASS로 간주하지 않는다. Billing 접근, 별도 견적 산출, 지원 재확인을 신규 선행 Gate로 만들지 않는다. 근거: [#34 비용 기준](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6041695587), [#35 적용](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6041696150).
4. **ROSA:** 1 AZ·m5.xlarge 3대와 worker 1대 장애·복구 시험은 사용자 선택 방향이다. AZ 전체 장애 대응을 P0에 추가하지 않는다. 방향 선택과 Architecture Freeze·생성 GO·실제 시험은 구분한다.

## 이번 수행과 경계

STATIC: 기존 AC/Execution Contract, 최신 댓글, PR7 HEAD·리뷰, 증적 저장소의 지정 경로 유무를 대조했다. #30에서 제공한 최신 Close 입력을 소비했으며 개별 Phase 1 서버·하위 티켓의 모든 원본을 재심사하지 않았다. 증적 저장소는 main `b1328ea3efd5cfb1ce966fd0285d99bd7a4d28eb` 전체 경로 목록(truncated=false)에서 `evidence/MS-P1-CLOSE-01/`, `MS-P2-START-01/`, `MS-G4-01/`, `DEC-CAL-P2-01/`을 찾지 못했다. 다른 경로에 자료가 전혀 없다는 뜻은 아니다.

이번 변경은 Markdown 및 조회 메타데이터뿐이다. MOCK·AWS/ROSA/OCP RUNTIME·Terraform Plan/Apply는 수행하지 않았다. CI는 PR의 실제 실행 결과를 별도로 확인한다. 기존 `phase1-close-input.json`의 빈 records를 합성 데이터로 채우지 않았다. Issue 본문·AC·Status는 그대로 두고 운영 댓글에 연결한다.

## 이미 준비된 자료 재사용

- [Phase 2 시험/증적 준비](../../phase2/preparation/20261007/test-evidence-preparation.md), [Shared Lab 준비](../../phase2/preparation/20261007/shared-lab-rehearsal-preparation.md), [시험전략](../../tests/FDS_Phase2_Test_Strategy_20261007.md)을 재사용한다. 이 문서의 최신 사용자 입력은 이전 준비 문서의 미확정 비용/Team Code 표현에 대한 운영 delta다.
- [D22 Registry 결정 입력](../../phase2/reviews/20261004-d22-decision-and-input-packet.md)은 #42의 기존 준비물이다. 새 비교표 작성이나 최종 Registry 선택을 이번 #33/#39 준비와 혼합하지 않는다.
- [infra-terraform PR6](https://github.com/321Team/infra-terraform/pull/6)의 collector/실행 준비와 [PR7](https://github.com/321Team/infra-terraform/pull/7)의 Relay 후보를 재사용한다. PR6의 기존 Terraform 디렉터리를 PR7의 Stream9 구현으로 오인하지 않는다.

## 다음 실행 순서

1. #30 → #31/#32의 실제 Close 결과·잔여 처분을 수신해 이권욱이 #33 Start를 판단한다. 미완료 P1은 Owner/Due/Deferred 근거로 분리하며 자동 차단하지 않는다.
2. #34 Freeze 입력과 #35의 기존 IAM/Stage-A 조건을 확정하고, PR7 독립 리뷰·수용된 실행 SHA를 기준으로 Plan 준비를 소비한다. IAM Grant·Plan·Apply를 문서 게시로 승인하지 않는다.
3. #35 실제 IaC와 #37 실제 VPN 결과를 아래 G4 표에 연결하고, 이권욱이 10-14 목표 G4를 판정한다. #38의 클러스터 생성 완료를 G4 진입 조건으로 역으로 요구하지 않는다.
4. 10-23 Review 시간·참석자는 기존 #52에서 후속 확정한다. 지금의 문서 준비를 차단하지 않는다.

변경 복구는 이 문서 전용 커밋의 revert다. 실제 클라우드 변경이 없어 인프라 원복은 해당 없음. 정본·티켓 종결·증적 저장소 편입은 이번 PR 게시와 별도다.
