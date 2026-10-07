# Phase 2 전용 사전 준비 — 2026-10-08

CODEX_ASSISTED. 사용자 'Phase 1 작업은 제외하고 나머지 건에 대해서 권장 순서대로 착수' 지시를 적용한다.

현재 상태: **사전 준비 문서 반영 / 결정안 수용·독립 코드 리뷰·실제 실행은 별도**. 이번 패킷은 런타임 설정이나 실행 가능한 tfvars가 아니다. Phase 1 Close/Harbor/기존 CICD 수정·시험·승인·티켓 처리는 범위 밖이다. 해당 생산물을 P2가 소비할 조건만 기록한다.

## 이번에 구체화한 결과

| 순서 | 결과 | 소비 위치 / 남은 조건 |
|---|---|---|
| 1 | PR6 운영안 G4=10-14 정합화, 이전 승인 이후 변경분 분리 | Terraform PR6. PR7 e4ee0bf의 독립 리뷰·Lead 판단은 별도 |
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
