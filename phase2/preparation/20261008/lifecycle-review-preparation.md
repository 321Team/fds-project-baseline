# 생성·운영·삭제·Review 선행 준비

2026-10-08 KST, CODEX_ASSISTED. #34/#52/#55 권욱 담당 준비안. 현재는 **1차 인수 준비 단계**이며 Phase 2 사전 문서 준비와 실제 착수를 구분한다. 정확한 생성/삭제 시각·Review 참석자/시각은 미정이다. 기존 날짜를 새로 승인하거나 자원 삭제를 실행하는 문서가 아니다. [#55 계약](https://github.com/321Team/fds-project-baseline/issues/55)과 [기존 인계표](evidence-handoff.md)를 따른다.

## 이벤트 기준 작업창

| 구간 | 진입 조건·지금 고정할 계약 | 종료/인계 |
|---|---|---|
| 생성 전 | 검토된 IaC/정책·source SHA, 해당 Freeze/단계 판단, 본인 권한, 교육장 리포트 기준 비용통제, 실행·중단·회수 범위 | source/Plan receipt와 실제 시작 KST 기록. 미충족이면 생성하지 않음 |
| Network/Relay/VPN | network saved Plan 검토→별도 Apply→actual handoff→vpn Plan/Apply→#37 검증 | G4 목표10/14. Agent/SA/경로·positive/negative/recovery 원본. G4 전에 ROSA Ready를 요구하지 않음 |
| ROSA/App | G4와 생성 선행 계약 충족·별도 Create GO → #38 생성/접근 → 승인된 최소 pull 경로·cold-pull → Basic Ready → D22 Final·App/Delivery | G5 목표10/20. 실제 version/identity/권한/이미지/업무 원본 |
| Hybrid/E2E | #47 H1 수신 후 #50 실행, F1/F2·fixture/DB·원복 조건 충족 | 10/21 본시험 구성, 10/22 회귀/G6. exact 시각은 승인된 실행본에서 고정 |
| 종료 준비 | 마지막 필요한 시험·재현/시연 방법·원본 보존·삭제 범위 확인. 삭제가 남은 Demo/Review를 막는지 확인 | 10/23 정리 목표와 Review를 조정. Review 전 자동 삭제 없음 |
| Review | 10/23 #49 집계→#54 산출물 Freeze→#56 Review→#55 Action 접수 | 미완료/차단/잔여 Owner/Due를 사실대로 기록 |
| Close | 10/26 잔여 Action·Cloud 잔존/비용·Sign-off 대조 | #57 인계. 10/24~25 주말 작업을 자동 배정하지 않음 |

## 삭제·보존 순서와 책임

일정 충돌은 [17:40 종합 검토](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6056087764)를 따른다. infra-rosa#4의 10-13 Cluster Ready 계획은 선행 #39 G4 목표10-14와 동시에 확정 실행 일정으로 사용할 수 없다. 담당자의 정합화 대상이며 새 날짜를 임의로 배정하지 않는다. #33은 Phase 1 Close 결과·Known Issue/Approved Deferred 등 기존 진입조건으로 판단한다. 10-23 Deliverable Freeze/Review는 Architecture Freeze나 자동 삭제 예약이 아니다.

| 대상 | 실행 책임 / 사전 수용 | 안전한 정리·보존 기준 |
|---|---|---|
| APP 시험 데이터·PV/이미지 | #43/#47 생산자, #46 공급자 | fixture/업무 원본·필요 백업/복구 범위·승인 digest 보존 확인. 임의 데이터 폐기 없음 |
| ROSA runtime | #38 하영 | 관리/Registry/egress 경로를 유지한 채 정상 Cluster 삭제 및 의존 LB/ENI/volume 상태 확인. 실패 시 다음 기반 자원 삭제 STOP |
| ROSA prereq roles/OIDC | #35 하영 | 클러스터 삭제 완료와 다른 소비자 없음 확인 후 승인된 전용 자원만. 공용/중앙 IAM·SLR 일괄 삭제 금지 |
| VPN/Relay | #35/#37 하영·재환 | ROSA 삭제와 필요한 On-Prem 접근 종료 후 route→Relay 및 전용 연결 자원 순서를 실제 Plan으로 검토. EBS delete-on-termination/보존 결정 재확인 |
| Network/NAT/EIP | #35 하영 | 의존 runtime·endpoint/LB/ENI 해소 후 NAT·전용 EIP·route/subnet/VPC를 검토된 Plan에 따라 정리. 예상 밖 delete/replace 시 STOP |
| 선택 ECR repository | 생성 시 #35/#46 | current/previous digest와 재현 자료의 보존 수신 후 별도 정리 판단. 이미지 강제삭제를 기본값으로 쓰지 않음 |
| backend/state/중앙 bootstrap/Session document | 중앙 권욱 | 기본 보존. state에는 민감정보 가능하므로 비공개 승인 저장소/권한 유지. prevent_destroy를 임의 해제하거나 state rm으로 우회하지 않음 |
| 증적·결정·Known Issue | 생산자→권욱 | 원본/해시/관측시각·source·명령/RC·복구·리뷰/병합/발행 연결. archive 확인 없이 유일 원본 삭제 금지 |

실제 인벤토리 접수 필드: ticket, owner, account/region, resource type/ID, state key/source SHA, 의존 소비자, 삭제/보존 결정, 복구 자료 위치·수신자, 실행 시작/끝 KST, 결과/잔존 이유·Owner/Due. 지금 actual ID나 완료시각을 합성하지 않는다.

삭제 중 실패하면 기존 접근/관측 경로를 유지하고 inventory와 IaC state 차이를 읽기 확인한 뒤 담당 Lead가 복구한다. 부분 실패에서 일괄 destroy 재실행·수동 강제삭제·관리 경로 선삭제를 하지 않는다. 클러스터 삭제 후 복구는 필요한 경우 재생성·보존 데이터 복원이며 즉시 undo로 표현하지 않는다.

## 비용 접수와 조치 연결

교육장 원본 링크/파일·as-of KST·기간·통화·사용액·예상 총비용을 수신할 때 각각 기존 목표400/중단450/상한USD500에 대조한다. 예상 총비용에 사용액을 다시 더하지 않는다. 미수신은 NOT_ASSESSED이며 0/PASS로 채우지 않는다. 지원 확정·자부담0·예비50 유지, 자체 Billing 조회/견적/새 제출주기는 추가하지 않는다.

목표 초과나 초과 예상은 기존 비용 정책에 따라 운영시간·남은 시험/자원 조정 판단으로 연결한다. HardStop 도달/초과 예상은 기존 중단·정리 절차로 넘기며 한도 확대·자부담을 자동 승인하지 않는다. 정리 뒤에도 후행 비용/잔존 사유를 교육장 리포트와 연결한다. 보고가 지연됐다고 자동 PASS를 선언하지 않는다.

## 10/23 Review 의제와 미결 접수

의제는 G4/G5/G6 실제 결과·Hybrid Demo/원본 → source/digest/증적 무결성 및 publication → Critical/Known Issue/Deferred → 잔존 자원·비용·보존 → #55 Action/10/26 Close 조건 순서로 준비한다. 미실행 Runtime·Lab-only P0·미병합 evidence를 MET로 올리지 않는다.

미결: Review exact 시간/참석자, 생성/삭제 exact 창, Demo에 live 자원 필요 여부, 보존 자료 수신자·각 잔여 due. 이 값은 실행/회의 조율 후 기록하며 이번에 사람·일정을 임의 확정하지 않는다. 템플릿 작성은 Review 실행·Sign-off 완료가 아니다.
