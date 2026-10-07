# #39 G4 인수 입력표

계획일 **2026-10-14**, 인수 Lead **이권욱**. [#39 기존 계약](https://github.com/321Team/fds-project-baseline/issues/39)과 [Transport 정합화 5966008497](https://github.com/321Team/fds-project-baseline/issues/39#issuecomment-5966008497)을 사용한다. 새 AC를 추가하는 체크리스트가 아니다.

## 입력·증적·완료조건

| 입력 | 현재 확인 범위 | 생산 / 소비 책임 및 인수 시 필요한 증적 |
|---|---|---|
| #34 Architecture Freeze | 1 AZ·m5.xlarge 3대, worker 1대 장애·복구 방향. **최종 Freeze 미확인** | #34 이권욱: 고정 CIDR·접속 경계·IAM/OIDC·비용·ROSA 생성 선행 입력의 최종 결정과 #35/#37/#38 수신 링크 |
| #35 Full IaC | 중앙 4자원 CREATE_COMPLETE / PASS_USER_READBACK는 기존 수신 사실. PR4/5 병합과 PR6/7 준비를 전체 인프라 생성으로 해석하지 않음 | 생산 이하영, G4 소비 이권욱: 실제 VPC/Subnet/Route/SG/Relay/IAM/OIDC·state 식별자, 사용 코드 SHA, Plan 검토 및 Apply 결과·원본 RC/로그. 민감한 state 원문은 공개하지 않음 |
| #36 D21 | **OCI Primary NO-GO / AWS EC2+EIP Libreswan Relay 선택 결정 있음**. 최종 증적 publication 및 종결은 별도 잔여 | #36 생산 기록과 최종 선택 근거·증적 편입 링크 수신. 과거 IKE_AUTH 도달/불일치 PSK 인증 실패 관측을 정상 SA 또는 VPN PASS로 사용하지 않음 |
| #37 실제 Relay/VPN·Route/Security | SG 입력과 Stream9 AMI 방향 회신 있음. PR7 구현 후보와 MOCK/서명검증은 실제 Linux/AWS/VPN 시험이 아님 | 생산 이재환, 소비 이권욱: 선택 Relay Instance/ENI/EIP, IKE/selector/SA, 실제 route/security와 inner forwarding, 승인 TCP canary·비인가 차단·복구 로그. VGW/TGW attachment를 새 필수 자원으로 요구하지 않음 |
| #38 ROSA 생성 선행조건 | [infra-rosa #3 read-only](https://github.com/321Team/infra-rosa/issues/3#issuecomment-6035898024): 서울 HCP 지원·지원 version/type·최소 quota 등 조회. topology/capacity/권한 전체 GO 아님 | 생산 이하영, 소비 이권욱: 최종 region/version/topology/type/count 및 생성 권한/네트워크/quota 입력. G4 전 실제 ROSA Cluster Ready를 요구하지 않으며 생성 후 Runtime 인수는 #38 |
| 비용 | 교육장 리포트 기반 사용액·예상 총비용 추적. 이 점검에서 실제 보고 금액은 **미수신 / NOT_ASSESSED** | 이권욱: 리포트 참조/기준 시각/통화/적용 기간/사용액/예상 총비용을 기존 한도와 비교. 값이 없으면 비용 PASS를 만들지 않음. 지원 재확인·Billing 접근·자체 재견적은 추가 Gate 아님 |
| 최종 결과·잔여 | **G4 실제 인수 미완료**. 본 준비표로 Critical=0을 선언하지 않음 | 이권욱: 필수 입력별 실제 결과와 미완료 P0/승인 예외를 구분. `NOT READY / Known Issue / Approved Fallback`을 기존 기준대로 기록하고 Owner/Due·#38 handoff를 연결 |

## 코드와 실제 실행 구분

- PR6 HEAD `c0f9ae7cdd14b7220eb1a945e48169595812daea`: 수집·Plan 준비. PR6 자체 Terraform 디렉터리는 PR7 Stream9 구현이 아니다. source binding의 candidate와 accepted execution SHA를 구분한다.
- [PR7](https://github.com/321Team/infra-terraform/pull/7) HEAD `e4ee0bff2d6aba92a0b147b86e1f4759f315eded`: Ready/Open, 미병합, 조회 시 제출된 리뷰 0건, 요청 Reviewer `hayeounglee`·`supreme33-kr`. Reviewer 지정은 독립 승인 완료가 아니다.
- candidate AMI `ami-08d855918a18d0cf9`와 소유자·아키텍처·이미지 상태는 실행 계정/리전에서 최신 수집 자료로 다시 결속한다. AMI 방향 수용은 actual image readback이나 Cloud Plan을 대체하지 않는다.
- 실제 실행은 수용된 정확한 SHA와 깨끗한 checkout, #35 계정·권한·Gate에서 진행한다. Plan 결과만으로 Apply하지 않는다. 새 Runtime 코드는 적용 SHA의 독립 리뷰와 해당 Lead 실행 조건을 따른다.

## 수신과 재검증 방법

자료는 기존 `evidence/P2-IAC-01/`, `P2-OCI-01/`, `P2-VPN-01/`, `P2-ROSA-01/` 생산 경로를 참조하고 G4 결과는 `evidence/MS-G4-01/`에 연결한다. 담당별 원본을 복제해 새로운 시험 결과로 만들지 않는다. 증적 저장소 편입은 해당 저장소 독립 리뷰 정책을 따른다.

수신 시 대상 계정/리전/호스트·실행시각(KST)·code SHA·명령과 RC·원본 로그·해시를 연결한다. SHA256 일치는 파일 무결성만 뜻한다. 생성/적용/연결/승인 TCP/negative/복구 각 결과를 구분하고 실행하지 않은 행은 `NOT_RUN`으로 유지한다. 원본에 credential/PSK/개인키/state secret을 포함하지 않는다.

변경이 생긴 source와 미완료 조건만 재검증한다. G4 날짜 도래, 문서 PR 병합, Shared Lab PASS, 정적/모의시험 통과만으로 #38 생성 GO나 G4 PASS를 부여하지 않는다. 실제 실행 명령·중단/복구는 #35/#37의 해당 SHA Runbook을 사용하며 이 인수표에 별도 실행 절차를 중복 작성하지 않는다.
