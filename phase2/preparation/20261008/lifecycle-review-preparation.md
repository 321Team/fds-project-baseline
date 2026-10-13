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

### 10/13 19:18 비용 결정 수신 — 실행 일정과 구분

[ROSA Cost GO 명시 결정](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6143326582)을 수신했다. 같은 범위의 비용 승인은 다시 대기시키지 않는다. 기본 HCP1·worker m5.xlarge3/gp3 300GiB×3·NLB/endpoint 및 정상 설치에 필요한 자동 private zone/registry S3, C1 최대worker4대·추가1대1시간/회2회 직렬, C4 비중첩 재생성1회 비용을 포함한다. 수량·소유·잔존은 실제 inventory에 연결한다.

승인 비용 기간은 10/15 생성 시작~10/23 Review 후 삭제 계획과, 삭제 선행조건 미충족 시10/26 삭제 착수까지 비상 유지 비용이다. **실제 생성/삭제창·주말 근무·C1/C4 실행을 확정한 것이 아니다.** 생성 지연으로 종료 범위를 자동 연장하지 않는다. 10/26 이후 유지·수량/범위 확대는 변경분만 판단한다. C2 Route53 Resolver·C3 ECR·추가 probe·별도 유료 계약은 제외다.

최신 비용 기록의 사용자 제공액은10/13 $0.19(EC2 $0.18+VPC $0.01)이며, 이번 작성자가 교육장 원본 리포트를 직접 받은 것은 아니다. cutoff·전체 예상 총비용은 미확인으로 유지하고 가용 잔액으로 계산하지 않는다. 전체400/450/500·지원 확정·자부담0, 비용 중앙 판단을 유지한다. Credit0을 지원 취소로 해석하지 않으며 구축 담당자에게 별도 상세 견적이나 중복 비용 Plan을 요구하지 않는다.

## 10/23 Review 의제와 미결 접수

의제는 G4/G5/G6 실제 결과·Hybrid Demo/원본 → source/digest/증적 무결성 및 publication → Critical/Known Issue/Deferred → 잔존 자원·비용·보존 → #55 Action/10/26 Close 조건 순서로 준비한다. 미실행 Runtime·Lab-only P0·미병합 evidence를 MET로 올리지 않는다.

미결: Review exact 시간/참석자, 생성/삭제 exact 창, Demo에 live 자원 필요 여부, 보존 자료 수신자·각 잔여 due. 이 값은 실행/회의 조율 후 기록하며 이번에 사람·일정을 임의 확정하지 않는다. 템플릿 작성은 Review 실행·Sign-off 완료가 아니다.

## 10/13 보완 — #52 결정용 운영안과 #55 Action 인계

**PROPOSED / 일정·참석 수락 미확인 / 초대·Calendar 변경 없음.** 기존 [#52 Calendar Contract](https://github.com/321Team/fds-project-baseline/issues/52#issuecomment-5907902770)의 **10/23 Freeze·Review, 10/26 Close, 10/24~25 비근무**를 유지한다. [시간/참석자 미정 기록](https://github.com/321Team/fds-project-baseline/issues/52#issuecomment-6042799442)을 다음 안으로 구체화한다. 새 날짜 승인을 요구하는 안이 아니다.

### 권장 시간안

10/23 **14:00~15:30 KST, 90분**을 조율용 1안으로 제안한다. 같은 날 오전에 #49 집계와 #54 Freeze 검토를 마치고, 회의 뒤 업무시간에 Action을 정리할 여유를 두기 위한 선택이다. 실제 가용시간을 확인한 값이 아니다. 필수 참석자의 충돌이 있으면 **같은 날 확보 가능한 연속 90분**으로 조정해 #52에 단일 시작/종료값을 남긴다. 10/23 자체 변경은 기존 Schedule Change 절차를 적용하며 자동으로 주말에 이월하지 않는다.

권장 조율 완료 시점은 10/16 D23 결정 준비와 함께다(새 강제 일정 아님). #52의 기존 일정확정 AC는 아직 미충족이며 회의일까지 미정 상태를 방치하지 않는다. 확인할 항목은 `실제 시작/끝 KST · 참석 가능자/대체자 · 기존 책임별 승인권자 · Demo 방식` 네 묶음이다.

| 제안 역할 | 기존 책임자 / 확정 여부 | 준비해서 가져올 자료 |
|---|---|---|
| 진행·PMO/QA·Decision/종결 판단 | 이권욱 / 책임은 기존 기준, 해당 시간 참석 미확정 | 동일 candidate 목록, G4/G5/G6 판정, Decision/Known Issue, 교육장 리포트·Action 목록 |
| Cloud/ROSA/IaC 설명 | 이하영 / 참석 미확정 | #35/#38 actual·권한·보안·잔존 자원·정리 상태와 해당 Lead 판단 |
| VPN/App/Hybrid 결과 설명 | 이재환 / 참석 미확정 | #37/#43/#47/#50 결과·실패/복구·DB 원복·image/digest 추적 |
| 추가 승인권자/이해관계자 | 기존 티켓·승인 체계에 있는 경우만 확인 | 새 인물·상시 Support 서명 Gate를 만들지 않음 |

문서·업무 결과의 Lead 판단과 코드/증적 저장소의 독립 리뷰를 구분한다. 참석했다는 이유로 source/evidence의 독립 승인자가 되지 않으며, 이권욱 작성분을 타인의 승인으로 기재하지 않는다.

### 90분 진행표

| 상대 시간 (1안 기준) | 의제·책임 | 남길 출력 |
|---|---|---|
| T+00~10 (14:00) | 이권욱: #49→#54 동일 candidate·변경/미결 확인 | 회의 입력 SHA/manifest·Freeze 실제 판정. 미완료를 회의 개최만으로 수용하지 않음 |
| T+10~30 (14:10) | 이하영·이재환: G4/G5/G6·Hybrid 결과 | actual 환경/RUN·정상/거부/복구·미실행, 원본 링크. 새 Runtime 시험은 별도 승인창 |
| T+30~45 (14:30) | 이재환·이권욱: Demo 및 source/digest 추적 | 승인된 실제 Demo 또는 기존 기록 검토의 종류·결과. 기록 재생을 live 실행으로 표시하지 않음 |
| T+45~60 (14:45) | 이권욱: Decision·Critical/Known Issue/Deferred | 범위별 수용/보류·Owner·완료조건. 미충족 AC를 예외 문구만으로 PASS 처리하지 않음 |
| T+60~75 (15:00) | 이하영·이권욱: 자원·비용·보존/정리 | 삭제/보존 후보와 실제 상태, 비용 기준시각·예상 총비용·잔여 조치 |
| T+75~90 (15:15) | 이권욱: #55 Action readback·10/26 Close 조건 | 담당자·기한·증적·수용권자 및 미합의값. 실제 결정 기록 확인 |

이 진행표는 발표 시간 배분이며 실제 실행/정리 작업창이 아니다. 오전 Freeze가 준비되지 않으면 Review에서 상태·차단과 후속을 다룰 수 있지만 #54/#56 인수 완료로 올리지 않는다. 결석/자료 누락 영역은 담당자·재검토 조건을 남기고 독립적인 의제를 계속 진행한다.

### Demo와 정리의 선후관계

권장안은 우선 **기존 실제 증적을 이용한 Review**를 준비하고, live Demo가 필요하다고 결정된 경우에만 필요한 자원과 최소권한을 실제 Demo 종료·결함 재시험·증적 검토 완료까지 유지하는 것이다. 이는 기존 검증권한 유지 결정의 적용이며 새 권한 포괄 부여/분리 정책 재부착 승인이 아니다. live 필요 여부가 미정이면 삭제 승인을 추정하지 않는다. 실제 자원 보존시간·비용은 이권욱이 교육장 리포트와 남은 검증을 함께 판단한다.

### Action 접수와 Close로 넘기는 기준

| 접수 종류 | 담당 / 권장 순서 | 완료 증거와 수용 경계 |
|---|---|---|
| 소스·설정 결함 | 해당 생산 Lead; 기존 PR/티켓에 연결 | 수정 HEAD와 영향 시험·필수 코드 리뷰. 회의 메모를 승인으로 대체하지 않음 |
| Runtime·복구 미충족 | 해당 실행 Lead; 필요한 작업창 별도 | actual RUN/대상·정상/실패/복구 원본. 다른 담당 작업은 계속 진행 |
| 증적·문서 누락 | 생산자 누락 보완 → 이권욱 집계 | 기존 링크/원본 수신 단계·변경분 확인, 증적 PR은 독립 리뷰 |
| 정리·비용 잔여 | 자원별 owner → 이권욱 중앙 판단 | 실제 잔존 ID·사유·다음 조치·비용 보고; 강제삭제/기한만으로 완료 금지 |
| Deferred·Known Issue | 해당 Lead → 이권욱 | 이유·영향·Owner·기한 또는 재검토 trigger·승인 근거. 미확정 기한 합성 금지 |

Action마다 `출처/결정 KST · 대상/단계 · Owner · Due(미정이면 미정) · 완료조건 · 증거 링크 · 수용 책임 · 실제 상태`를 기존 #55 기록에 연결한다. 지금은 실제 Action이 발생한 것으로 채우지 않는다. 10/26에는 #55에서 Action·잔존/비용·필수 AC·sign-off를 대조한 뒤 #57로 인계한다. 미충족이면 종결 보류와 담당/완료조건을 남기며 10/26 도래만으로 Close하지 않는다.
