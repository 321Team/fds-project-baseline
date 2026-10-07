# 사전 준비 입력표

상태: PREPARATION / 확인 사실과 미확정 실행값 분리. 실제 source 출처·조회 시각은 sources.json.
본 표는 Deployment·Terraform·정책 실행 입력이 아니다.

## 기존 작업 재사용

| 항목 | 확인한 원본 | 판정 / 다음 단계 |
|---|---|---|
| 중앙 bootstrap 소스 | [PR148](https://github.com/321Team/fds-project-baseline/pull/148), HEAD e1cac2d39174821c839f2df6068fab16211bf872 | MERGED, merge40ac664b83485745ab86b5018b8e19c386484cc8. [#35 최종 수신](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6031865288): CREATE_COMPLETE·설정 PASS_USER_READBACK. assistant 직접 raw/AWS 재검증과 구분 |
| 실제 prepare 수신 | [#35 6030662302](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6030662302) | manifest RC0·root ARN·source UTC/helper hash의 사용자 출력 수신 완료. assistant의 AWS 직접 실행 아님 |
| 4자원 생성 조건 | [#35 Lead GO](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6031301706) | StateBucket/Policy 및 FDS-Relay-SSM Role/Profile만 조건부 GO. CloudFormation 소유권 채택·복구 책임 명시 |
| GO 실행 조건 | 같은 기록 C1~C5 | source/helper 동일성, 같은 실행의 fresh before, create 1회, timeout 검사, partial STOP, verify/readback 및 CloudShell 14건 확인 |
| GO 외 잔여 | 같은 기록 | 사람 role/grant·Stage-A·compute·ROSA·비용 설정·각 개인 Runtime은 별도 잔여 |
| D21 raw 인계 | [#36 마지막 인계](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-5966659098) | final responder/raw 수신·재해시·독립 증적 심사 잔여. mismatched PSK round-trip을 production Child SA로 승격하지 않음 |

중앙 실행은 [기존 README](https://github.com/321Team/fds-project-baseline/blob/e1cac2d39174821c839f2df6068fab16211bf872/phase2/permissions/20261007-central-bootstrap/README.md)를 그대로 소비한다. 이번 시험계획 갱신 세션에는 root CloudShell을 사용하지 않았다. 생성/설정 완료는 사용자 실행 출력의 최신 수신 기록으로만 소비한다. CloudFormation 소유권은 유지한다.

## 결정 입력과 무영향 준비 범위

| 티켓 / 책임 | 지금 정리할 입력 | 적용 전 미확정 / 소비조건 |
|---|---|---|
| #34 / 이권욱 | On-Prem→ROSA 이전 경계, Shared/Test OCP Lab 경계, P1 인계·source/evidence 참조 | #32 Known Issue 인계, topology/worker count/AZ·지원성·용량·비용 최종값. Architecture Freeze는 HOLD |
| #35 / 이하영 | 기존 schema/backend/SSM bootstrap 진행 수신 | full IaC implementation PR/SHA·API 목록·완결 permissions·Stage-A source/plan. 중앙4자원 readback은 수신됨. 중앙4자원 GO를 full apply로 확대하지 않음 |
| #38 / 이하영 | #43이 소비할 Namespace/RBAC/SCC/trust/Route handoff 항목 | 실제 Cluster/API/Version·Basic Ready. Lab admission만으로 Ready 처리하지 않음 |
| #40 / 이권욱 | DB/Harbor IP Endpoint 기본과 Private 관리 FQDN·DNS subset 후보의 차이 | 실제 Runner route/source, endpoint 이름/zone/port, 전달 범위·복구·비용. #48 신규 구현 GO는 별도 |
| #42 / 이권욱 | Harbor 재사용과 승인 Cloud Registry 비교 항목 | single Primary/Fallback, endpoint/repository, push/pull principal, trust, digest, source path, credential reference, 비용, #38 handoff |
| #46 / 이권욱 | delivery-preparation.md의 target adapter 경계 | #38 승인 Runtime 상태·#43 target/health·#42 D22·정확 source/digest/rollback |
| #49 / 이권욱 | 원본→source→Runtime→review→freeze 추적 목록 | 실제 evidence 편입/독립심사·immutable final set. 템플릿을 증적에 넣지 않음 |
| #50 / 이재환 | 현 AC case 초안·#119 기대결과·#47 actual identity 항목 | #47 handoff, fixture/DBschema/runtime pin·작업창·일정 정합화 |

## DNS·Registry 비교 준비

| 판단 축 | 기존 Harbor 경로에서 받아야 할 입력 | 승인 Cloud Registry 대안에서 받아야 할 입력 |
|---|---|---|
| source / lineage | 승인 app SHA·scan·Harbor digest, 기존 audience와 실제 pull source | 동일 app SHA·scan·push 후 registry digest·ROSA imageID |
| TLS / trust | 실제 CA fingerprint/SAN/FQDN·Runner/worker trust, ROSA trust 지원 방식 | 서비스 endpoint/FQDN·공식 trust·인증 방식, 실제 ROSA pull |
| 권한 | Runner push와 worker pull 분리, credential owner/expiry/reference | 최소 push/pull 권한·role/trust/credential reference |
| 경로 | VPN/Relay와 no-inner-NAT·source allowlist·actual return path | 승인 egress·endpoint/SG/NetworkPolicy와 node pull 경로 |
| 장애·복구 | tunnel/Harbor 장애 시 승인 fallback·이전 digest 재Pull | registry/credential/egress 실패 시 이전 digest 재Pull·fallback |
| 비용 | endpoint/NAT/전송·ROSA 유지·운영 경계 | 저장/요청/전송/endpoint/NAT 비용과 같은 runtime window |
| 인계 | #42 출력12항목→#43/#46/#47 | 같은 출력12항목. 임의 endpoint나 credential 배포 없음 |

숫자·제품별 지원 version·실제 endpoint 값은 미확정이다. 비교표의 빈 입력을 0원·PASS·허용으로 간주하지 않는다.

## 다음 입력 생산과 소비 책임

- #35 이하영이 provisioning source/plan 및 실제 자원 ID를 생산하고 #37 이재환이 경로 인수에 소비한다.
- #38 이하영이 platform/security handoff를 생산하고 #43 이재환·#46 이권욱이 소비한다.
- #43 이재환이 portable base/overlay와 actual app identity를 생산하고 #46/#47/#50이 소비한다.
- #42 이권욱이 D22 Decision을 생산한다. 결정 준비 문서 자체는 D22 GO가 아니다.
- 이번 문서는 별도 상시 Support 이중 승인이나 새 담당/기한을 부여하지 않는다.

