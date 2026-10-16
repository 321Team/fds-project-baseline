# Phase 2 전용 사전 준비 — 2026-10-08

**10/16 최신 진입점:** [순차 수행·D22·G4·Freeze/Review 인계](readiness-handoff-20261016.md). PR40 병합과 PR87 검토본, D1 고정·10/17 Create 조건·D22 A채택을 연결했다. 아래 과거 현황은 당시 이력이며 D22 Final/G4/공식 Start는 계속 미완료다.

**10/15 최신 준비:** [현재 G4 입력](gate-followup-20261014.md#1015-현재-입력과-후속-조건), [권욱 순차 수행](sequential-worklist-20261013.md#1015-권장-순서-착수-결과), [증적 인수](evidence-handoff.md#1015-인수표-변경분)를 우선 소비한다. 아래10/08~10/14 표는 각 시점의 이력이다. Stage2 v4 독립 검토·한정 GO는 기존 이력이며, [10/15 09:39 실행자 보고](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6181672488)에서 10/14 작업은 미실행으로 확인됐다. 이후 [09:46 새 한정 GO](https://github.com/321Team/infra-terraform/issues/12#issuecomment-6181760266)가 등록됐다. 해당 창·고정본·직전 사전조건 범위만 유효하고 실제 Apply 결과는 아직 미확인이다. VPN PR6와 TF PR32는 병합 완료다. 생성 Plan 키트 v5 직접 수신·검토를 마쳤고 실행 전 입력은 남았다. 이번 변경은 GitHub 인계용 준비 문서이며 새 GO·정본 발행이 아니다.

**10/14 15:47 후속:** [G4 현재 입력·실행 키트 검토·다음 담당](gate-followup-20261014.md). Stage2 Plan/정책4개 보완·PR226 편입 완료, version4.22.17/name 고정, 재환 B0/B1 15:40 착수 보고·완료 원본 미수신을 반영했다. Stage2 Apply는 키트 수정·의존성/병합본 검사 후 별도 GO 대상이다. Harbor 창 반납을 선행조건으로 추가하지 않는다. 아래 이전 시각 표시는 당시 이력이다.

**10/14 10:58 KST 현재 작업:** [권욱 P0 13건의 순서와 P1 보류 3건](sequential-worklist-20261013.md#현재-작업-목록--1014-1058-kst-조회)을 따른다. #40/#48/#120은 기존 결정으로 보류하며 이 착수 요청으로 재개하지 않는다. Delivery 후속 코드 → Architecture/G4 증적 → 중앙 비용 기록 → 산출물/Review 인계 순으로 진행했다. [PR75](https://github.com/321Team/infra-cicd/pull/75)·[PR167](https://github.com/321Team/fds-project-baseline/pull/167)·[PR214](https://github.com/321Team/fds-project-evidence/pull/214)는 병합 완료이고 후속 [PR80](https://github.com/321Team/infra-cicd/pull/80)은 별도 코드 검토 대상이다. 비용은 [10/14 제공액2.85USD](lifecycle-review-preparation.md#1014-1100-중앙-비용-입력-수신)를 수신했으며 기간/cutoff/예상 총비용은 미확인이다. 아래의 과거 목록은 당시 이력이다.

**10/14 13:04 KST 병합 반영:** [PR80](https://github.com/321Team/infra-cicd/pull/80) HEAD `eeadfd256b5360fb414569e15f0e32c2efd9ea39`는 [이하영 독립 승인](https://github.com/321Team/infra-cicd/pull/80#pullrequestreview-5512480439)·HEAD CI 2 SUCCESS 확인 후13:04:33에 병합됐다(`b183fddb9c65e7119bf008214c34bef3ca4066d2`). Linux MOCK 135건 중124 PASS/11 SKIP이며 실제 verifier·운영 연결·Runtime 인수는 잔여다. 아래10:58/11:08 기록은 당시 조회 이력이다.

**최신 준비 진입점:** [10/14 Phase 1 보호·순차 착수 결과](phase-boundary-20261014.md), [D23 결정 필드](decision-packet.md#1014-d23-ac-대조-결과와-결정용-필드), [D22 앱별 생산 원본 대조](d22-lead-review.md#1014-생산-원본-대조--앱별-currentprevious), [현재 입력16개·#49 집계](evidence-handoff.md#1014-입력표와-현재-증적의-대조). 본문의 10/08 현황은 당시 기록이며 각 문서의 최신 보완과 구분해 읽는다.

CODEX_ASSISTED. 사용자 'Phase 1 작업은 제외하고 나머지 건에 대해서 권장 순서대로 착수' 지시를 적용한다.

**현재 D23:** 이권욱의10/14 “보류” 결정으로 [추가 Hybrid DNS는 DEFERRED](decision-packet.md#현재-d23-결정--추가-hybrid-dns-보류). 기존 IP/public DNS·TLS 기준과 #48 OPEN을 유지한다. 과거 D23 PENDING은 검토 이력이며 D22는 계속 PENDING이다.

현재 상태: **1차 인수 준비 단계 / Phase 2 사전 문서 준비 병행**. 결정안 수용·독립 코드 리뷰·실제 실행은 별도다. 이번 패킷은 런타임 설정이나 실행 가능한 tfvars가 아니다. Phase 1 Close/Harbor/기존 CICD 수정·시험·승인·티켓 처리는 범위 밖이다. 해당 생산물을 P2가 소비할 조건만 기록한다.

10-08 오후 후속: [최신 변경·시험 준비](execution-readiness-update.md), [기존16case 실행 자료](test-execution-matrix.tsv), [장애 패킷 검토](fault-packet-review.md)를 소비한다. Terraform PR6/7은 최신 독립 승인 후 병합됐으며, 아래 최초 준비 시점의 후보/리뷰 대기 표현보다 새 수신 기록을 우선한다. full IAM·Cloud Plan·Runtime은 여전히 별도 잔여다.

14:50 KST 재점검: **[권장 순서·사전 작업 목록·착수 결과](prework-next.md)**를 최신 목록으로 사용한다. CICD PR68 병합 완료, MSA PR24 R1~R4 해소·생산자 병합 수신 완료. [24파일 소스 무결성](merged-source-receipt.json)을 대조했고 전체 IAM/실제 입력/Runtime은 미완료다.

16:23 KST 이후 권욱 선행 작업: [ROSA 설계 승인](https://github.com/321Team/infra-rosa/issues/3#issuecomment-6054292320)을 아래 입력표/결정안에 반영했다. private_a·NAT1·3개 Namespace 방향은 수용됐으며 상세 구현/전체 Freeze는 미완료다. [D22 Lead 검토·A/B 선택안](d22-lead-review.md)과 [생성·운영·삭제·Review 준비](lifecycle-review-preparation.md)를 추가했다. D21 raw는 evidence PR161 HEAD `162892f99a4d779a4f452be2bcf38b8e90bbbe6f`의 독립 승인·CI 후 17:05:38 KST 병합됐으며 merge는 `277893c7865bd2af9751ca73ee00985370c9eaf2`다. 원본 편입은 정본 publication/티켓 완료와 구분한다. D22 Final/실제 실행 승인은 별도 유지한다.

17:50 KST 후속: [ROSA 종합 검토](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6056087764)를 준비표에 반영했다. **생성 전 계약 → Gate 충족·별도 생성 판단 → 실제 cold-pull → Basic Ready → D22 Final** 순서로 문서의 모순을 정정했다. 버전/Pool·CA는 사전 후보 수용이며 Runner 입력·경로·IAM은 미완결이다. 하영의 후속 정정 댓글과 full IAM/NAT PR은 이번 조회에서 추가 접수되지 않았다.

## 이번에 구체화한 결과

| 순서 | 결과 | 소비 위치 / 남은 조건 |
|---|---|---|
| 1 | PR6/7 최신 독립 승인·병합 결과 수신 | PR6 77c6324 / PR7 1279215 승인, 통합 main93d7150. 실행 수용 SHA/manifest·IAM·Freeze/실행 판단은 별도 |
| 2 | [Freeze·D22·DNS·APP·일정 결정안](decision-packet.md) | #34/#40/#42/#43/#47/#50. 담당 입력·해당 Lead 결정 전 제안값 |
| 3 | [Delivery·시험 입력/실패/복구 계약](delivery-test-contract.md) | #46/#50. 가짜 endpoint/ID/credential을 넣어 실행하지 않음 |
| 4 | [담당별 입력 접수표](input-intake.tsv) | 실제값과 생성 후 관측을 구분. 초안 접수표이며 Runtime 결과 아님 |
| 5 | [D21 publication·G4/G5/G6·정리 인수 준비](evidence-handoff.md) | #36/#39/#45/#49/#53~#57. 원본 미수신·미실행을 합성 증적으로 채우지 않음 |

## 확정값 / 다시 요구하지 않을 것

- G4 10-14, G5 10-20, G6 10-22, Review/Freeze 10-23, Close 10-26. 10-09 및 주말 비근무. 근거 [#52 결정](https://github.com/321Team/fds-project-baseline/issues/52#issuecomment-5907902770). Review 시간/참석자만 미정.
- 1 AZ·m5.xlarge 3대·worker 1대 장애/복구 방향. AZ 전체 장애 P0 추가 없음.
- 교육장 지원 확정, 자부담0, 목표400/중단450/상한USD500·예비50. 사용액·예상 총비용은 교육장 리포트. 지원 재승인·Billing 접근·자체 견적·새 보고주기 요구 없음.
- 공용 OCP Team Code·Namespace·관리자 제약은 사용자 확인 '없음'. 실제 Lab 시험 target과 ROSA namespace는 각 실행 시 식별한다.
- 중앙 bootstrap 4자원·기존 SG/Session document 방향·기존 TLS/DNS 관측은 범위대로 재사용. full IAM 및 사람 역할 시험 완료로 확대하지 않는다.

## 진행 상태와 다음 순서

IAM full policy 제출·검토 → 중앙 부여/readback → 각 본인 MFA/권한/lock 시험 → network saved Plan → 해당 Apply 판단 → actual network handoff → vpn Plan 순서를 유지한다. 준비 문서를 만드는 동안 권한 부여·정책 simulation·Cloud Plan은 실행하지 않았다.

Freeze는 생성 전 네트워크/권한/보안 계약을 받아 판단한다. actual resource IDs/Agent Online/ROSA Runtime, Basic Ready 뒤 D22 Final은 생성 후 단계다. G4 PASS가 ROSA 생성 선행조건이며 G4를 위해 ROSA Cluster Ready를 먼저 요구하지 않는다.

조건부 P1 DNS 전체/Operator/OADP/GitOps/Compliance/RHOAI 구현은 착수하지 않는다. 기존 Deferred-first와 담당자의 결정/재검토 기록만 소비한다. 관리용 필수 DNS subset은 일반 Hybrid DNS 확장과 구분한다.

## 검증·출처·복구

기준 main: baseline `81365568fd0b946ad93e4d82ae8191add5fcacd0`, Terraform `0eabe8daa75a6b9bf960fe1ea5eeaf6a8818f216`, CICD `4e9324cd8acf0ba67b35f950b4c952db8064540e`, APP `adc90410f99cb7af5b40bc8ff92c45272e9f8bee`. 발행 정본 docs-v3.1.21 유지.

Issue 원문/최신 댓글·PR 상태·기존 준비 문서의 정적 대조를 수행한다. 수정 파일의 링크·TSV·UTF-8/LF·민감정보·diff를 검증하고 실제 결과는 PR에 남긴다. 이번 새 MOCK/LAB/AWS/ROSA Runtime=NOT_RUN. 문서 전용이며 복구는 해당 커밋 revert다. canonical 파일·Issue 본문/AC/Status·Phase 1 코드·서버 설정을 변경하지 않는다.

## 10/13 순차 작업 인계

[작업 목록과 다음 행동](sequential-worklist-20261013.md)을 재사용한다. 이 폴더의 10/08 기록과 `input-intake.tsv`는 당시 접수 이력이며, 최신 승인·소스·접수 상태는 각 문서의 **10/14 보완**을 우선 참조한다. 위 private 관리 경로 전제는 현재 public/public 승인에 맞춰 [DNS 보완](decision-packet.md)에서 구분했다. 이 보완도 정본 발행·D22/D23 확정·Gate 인수는 아니다. [준비 PR 리뷰 절차](evidence-handoff.md#준비-pr의-리뷰-절차-정정)에 따라 코드 PR75의 독립 리뷰와 문서 PR167의 Lead 판단을 구분한다.
