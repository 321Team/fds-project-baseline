# Phase 2 Test Plan — 2026-10-07 개정안

상태: **WORKING REVISION / 모든 신규 시험 결과 NOT_RUN**. 실행 템플릿을 실제 증적으로 사용하지 않는다.
기준·P0/P1·환경·단계·증적·복구 원칙은 [Test Strategy](FDS_Phase2_Test_Strategy_20261007.md)를 따른다.
아래 TP0 ID는 시험 추적 번호이며 새로운 AC 번호가 아니다. 티켓 원문 AC의 나열 순서로 매핑하고 최신 승인 변경을 함께 소비한다.

## 1. P0 AC 추적과 시험 범위

각 행의 단계별 준비 결과와 실제 RUNTIME/ACCEPTANCE를 따로 기록한다. 현재 표는 시험설계이며 **RUNTIME=NOT_RUN / ACCEPTANCE=PENDING**이다.

| ID / 영역 | 기존 Ticket·AC 근거 | 실제 대상·필수 판정/증적 | 기존 실행 책임 |
|---|---|---|---|
| TP0-01 AWS 계정/기본통제 | #35 AC3 필수 IAM/OIDC, AC4 State/Secret 통제; #38 AC2 승인 관리/배포 접근 | AWS 승인 계정·Region/주체·MFA/role 실효권한·backend 소유/접근·Secret reference. STS/simulator/부분 bootstrap을 전체 권한·ROSA 인수로 확대하지 않음 | #35 이하영, 중앙 지원 이권욱 |
| TP0-02 Terraform/IaC | #35 AC1 fmt/validate, AC2 Plan/Apply 일치, AC3 Route/Security/Output, AC5 재실행 비의도 변경 없음 | exact source/backend/input·검토 plan·actual Apply/Output·re-plan. CloudFormation 소유 bootstrap 4자원을 일반 Terraform으로 중복 생성/자동 편입하지 않음 | 이하영 |
| TP0-03 ROSA 구축 | #38 AC1 Cluster/Worker Ready, AC2 접근, AC4 승인 TCP 선행 | 실제 ROSA ID/API/Ingress/topology/Version·Ready·승인 계정 접근과 raw. G4 이후 Basic Ready와 Full을 분리 | 이하영 |
| TP0-04 Worker/MachinePool | #38 AC1, #34 승인 사양/의존성 Freeze | approved type/count/AZ/pool와 actual Ready/version/inventory 비교. 용량 근거·requests/limits·allocatable 추적. N-1/AZ 실패 시험을 새 AC로 만들지 않음 | #38 이하영, #34 이권욱 |
| TP0-05 VPN/Route 연결 | #37 AC1 Tunnel UP, AC2 승인 TCP, AC3 미승인 차단, AC4 Tunnel 중단·복구 | AWS↔On-Prem SA·route/return/source·승인 TCP·미승인 차단·down/recovery. Transport Adapter=aws_ec2_eip_relay 최종 handoff. mismatch-PSK 관측 ≠ 정상 Tunnel | #37 이재환 |
| TP0-06 DNS/관리 경로 | #38 AC2/4, 승인 TLS·관리 계약; #40/#48 전체 범위는 P1 | 승인 endpoint/FQDN/SAN·resolver/query/return path가 실제 관리·배포에 필요한 범위에서 동작. private 필수 subset 수용 전 미결; 전체 Hybrid DNS 구현을 P0로 승격하지 않음 | #40 이권욱 + #38 이하영 |
| TP0-07 Application | #43 AC1 두 서비스 Ready, AC2 API Route Health, AC3 engine 외부 비노출, AC4 4 Rule | 실제 ROSA의 approved digest/base+overlay·SCC/arbitrary UID·health·Route/Service/engine 비노출·R01/R02/R04/R07 raw. Lab 결과로 대체 금지 | 이재환 |
| TP0-08 DB/데이터 경로 | #47 AC1 ROSA→DB 승인 연결, AC2 저장/조회, AC3 미승인 source 차단; IF-03/04 | transaction-api→engine8001 평가, transaction-api→db01:5432 저장/조회; engine→DB DENY. actual approved DB source·pg_hba/firewall·schema·Transaction ID·DB row 연결 | 이재환 |
| TP0-09 CI/CD | #46 AC1 정상 배포, AC2 Test/Scan 실패차단, AC3 image/commit 역추적, AC4 Health/4Rule; 최신 rollback 계약 | RUN-A 성공·RUN-B 실제 Deploy 차단·이전 approved digest rollback/health. Run/Attempt→Source→Scan→Registry→manifest→ROSA imageID·health. #120 Go/CR 전 Runner-direct | 이권욱; 코드/증적 독립 검토는 비작성·비실행자 |
| TP0-10 Registry/Harbor 조건부 | #42 AC1 단일 Source/Fallback, AC2 Pull Route/TLS/Credential Test, AC3 APP/HYB/IF-19; #47 AC4 | 선택한 실제 Registry pull/trust/권한·digest 추적. Harbor면 VPN/source·CA/SAN·pull/push 분리와 기존 cold-pull 계약; Cloud Registry면 승인 대안 검증·Harbor 미사용 근거. Harbor 전체 AC 자동 추가 없음 | #42 이권욱 / #43·#47 이재환 |
| TP0-11 Secret/인증/권한/보안 | #35 AC4, #38 AC2/3 기본정책, D17/승인 security intent | 최소 RBAC/SA·token reference/expiry·Secret 접근/at-rest 등 승인 동등통제, NetworkPolicy Allow/Deny·SecurityContext/non-root/RO rootfs/seccomp/cap/SCC. 미채택 broad SCC/cluster-admin/TLS 우회 금지 | #38 이하영; 앱 #43 이재환 |
| TP0-12 기존 실패/복구 | #37 AC4; #119 승인 DB/engine 기대값; #50 정상/negative/recovery | DB 장애 readyz503·Endpoint 제외; engine 장애 API Ready·HTTP201·skipped=true·DB 저장. tunnel failure와 app failure 분리, 복구 후 동일 계약 회귀. 추가 복합장애·새 RPO/RTO 미편입 | #37/#50 이재환, 관련 통제 Lead |
| TP0-13 E2E/최종 회귀 | #50 AC1 정상거래, AC2 4Rule/DB, AC3 미승인 차단, AC4 tunnel 복구 regression, AC5 Critical 0 | 실제 ROSA+On-Prem: Route→API→engine 평가 + API→DB 저장. exact #47 handoff·fixture/schema·Transaction ID·digest·negative/recovery raw. HTTP200/일부 smoke만으로 PASS 금지 | 이재환 / PMO QA 이권욱 |
| TP0-14 Cleanup/재실행 | #35 AC5, #49 AC3 IaC/Runbook 재현, #55 잔존 Resource/Cost, #57 Close | 승인 scope의 app redeploy·IaC drift·final teardown, 삭제 전후 Cluster/NAT/EIP/ENI/LB/endpoint/EBS 등 실제 프로젝트 inventory·미삭제 Owner/기한·비용source. CloudFormation 소유/retention/삭제 승인 범위 유지 | 각 리소스 Lead / #49·#55 이권욱 |
| TP0-15 증적/인수 추적 | #49 AC1 P0별 evidence, AC2 as-built 차이 승인, AC4 Critical 문서0; #45/#53 Exit | Strategy §8 필드·명령/RC/raw·SHA256·Reviewer·단계상태·Known Issue. evidence 편입/검토와 Runtime AC 인수/정본 발행 분리 | #49 이권욱, 생산자 각 Lead |

필수 판정 범위는 각 원문 AC/승인 계약이다. 여러 row가 같은 AC를 검증해도 신규 하위 AC를 만들지 않는다.
MFA·지원 사양·TLS·source 등의 준비 입력을 임의 숫자/새 조직정책으로 확정하지 않는다.

## 2. P1 계획과 Deferred 기록

P1은 P0 완료 후 capacity·일정·비용·권한/지원성이 확보되면 수행한다. 수행하지 못하면 `Deferred/N/A/Cancelled`의 근거·Owner·재검토 조건을 기록하며 P0/G5/G6 실패로 처리하지 않는다.

| 추적 ID | 범위 / 기존 연결 | 완료 또는 Deferred 조건 |
|---|---|---|
| TP1-01 | Compliance #121 | Go/No-Go/Deferred, 지원 profile/suite·결과 처리·supply·cleanup. 규제 준수 인증으로 오표현 금지 |
| TP1-02 | 추가 Security/관찰성·운영 고도화 | 기존 P0 통제 위반과 추가 권고 분리. 승인 범위 또는 별도 후속 계약 |
| TP1-03 | GitOps #120, Operator supply #41/#51 | Go·CR·권한/공급/삭제 경로 후 구현. 현재 #46 Runner-direct P0 유지 |
| TP1-04 | OADP/S3 #44, 추가 복구·full ROSA recreate | 기존 P1 AC의 backup뿐 아니라 restore/health·raw 또는 Deferred. 새 P0 복구 기준 추가 없음 |
| TP1-05 | 전체 Hybrid DNS #40/#48 | 기존 IP Endpoint 또는 승인 DNS 선택/미적용 근거. private 접근 필수 subset 미결과 분리 |
| TP1-06 | RHOAI/RAG #95 | 현 Lab read-only, RESOURCE_GATE=FAIL, Deferred 권고. CR·ROSA Task·Version/Quota/Pool·비용·Entitlement·설치/삭제 확정 전 설치 안 함 |
| TP1-07 | 비용/운영 최적화·발표/PoC | P0 종료/비용통제는 유지. 선택 추가 시험·별도 live demo는 목적/종료시각/삭제범위 결정 후 |

## 3. 실제 Gate Exit Criteria

| Gate / 기존 책임 | 실제 필수 입력·Exit | P1 경계 / 현 상태 |
|---|---|---|
| G4 #39 / 이권욱 | #35 Terraform 인프라와 #37 승인 Transit/VPN, Route/Security·ROSA 선행조건·승인 TCP 준비도, 관련 Decision/Risk/Known Issue와 WBS/Notion 기록 | bootstrap 4자원 readback은 전체 G4 아님. **ACCEPTANCE=PENDING** |
| G5 #45 / 이하영 | #38 Platform/Security + #43 실제 ROSA App/Route/Health/Rule + #46 ROSA 정상 Delivery·실패차단/trace + #42 Registry 결정. Decision/Risk/Known Issue·결과 기록 | #40/#41 결정상태/Deferred/N/A 확인과 구현 완료 구분. #44/#48/#51/#95/#120/#121 미완료는 비차단. **ACCEPTANCE=PENDING** |
| G6 #53 / 이권욱 | #47 실제 ROSA→On-Prem DB/선택 Registry + #50 Hybrid E2E/negative/tunnel recovery regression, 기존 Critical Issue 0 기준과 Decision/Risk/Known Issue 기록 | P1 OADP 등의 실행결과 또는 Deferred/N/A 추적. Lab PASS·PR merge 대체 금지. **ACCEPTANCE=PENDING** |
| Freeze/Review/Close #49/#54/#55/#56/#57 / 해당 Lead | P0별 raw/evidence·as-built 차이 승인·재현 Runbook·Critical 문서결함0, Review Action/Sign-off·Source 인계·잔존 Cloud Resource/Cost 통제 | P1/Known Issue의 Owner·후속 완료조건 연결. 문서 통합/발행·Runtime/Gate 인수 각각 판단 |

[Gate 댓글 #45 5907191285](https://github.com/321Team/fds-project-baseline/issues/45#issuecomment-5907191285),
[#53 5907197070](https://github.com/321Team/fds-project-baseline/issues/53#issuecomment-5907197070)의 P0/P1 분리를 유지한다.

Critical Known Issue를 적었다는 이유만으로 Critical 0 AC를 통과시키지 않는다. 최신 운영 댓글의 예외/Known Issue 문구와 원문 Critical 0 요구가 다른 경우 영향·권한 있는 명시적 예외/변경 근거를 Gate Lead가 확인한 뒤 판정한다. 이 계획이 위험수용/예외 승인을 새로 만들지 않는다.

## 4. 작업창·선행순서

일자는 **계획 목표**이고 Runtime 실행·Gate 승인이 아니다. 티켓 원문 일정은 변경하지 않는다.

| 창 | 현재 계획/조건 | 실행과 인계 |
|---|---|---|
| W0 | Local/CI/Lab 사전검증 병행 | source/admission/UID·fixture 사전제거. Shared Lab 미실행만으로 차단하지 않음 |
| W1 / G4 | #34 Freeze 목표10/8, #35 10/8~14, #37 10/12~14, G4 10/14 | D21 최종 handoff→Freeze→검토 IaC Stage-A→VPN→Full G4. 유료 생성은 지원/계정/권한/plan/비용·정리 조건 후 |
| W2 / G5 | #38 10/15~19, #43 10/16~19, #46/G5 10/20 | Basic Ready→D22 actual 결정→App→Full security→Delivery/G5. #38 생성 전 입력과 actual은 구분 |
| W3 / G6 | #47 10/21, #50 10/22, G6 10/22 | #47 exact handoff→#50 정상/Rule/negative/실패복구→최종회귀. 10/21 주 시험안은 Lead 요청의 미결이며 자동 확정 안 함 |
| 종료 | Freeze/teardown10/23, Close10/26 계획 | evidence·cost·inventory 보존 후 승인 범위 삭제/실제 잔여 확인. 별도 승인 live demo 없이 추가 유지/유료시험 안 함 |

이번 조회에서 #35는 중앙 4자원 CREATE_COMPLETE·설정 PASS_USER_READBACK 수신 기록을 가진다. assistant의 AWS 재실행/직접 raw 검증이 아니며 full IaC·업무role/Relay·Stage-A readiness·ROSA는 별도 잔여다. 기존 통과 시험·bootstrap을 문서 수정 때문에 반복하지 않는다.

## 5. 실행 Record 작성 순서

1. 실행 직전 최신 원문 AC·Decision, source HEAD와 환경/구성 변화를 확인한다.
2. 대상 Host/Cluster·계정/권한·작업경로·pin·expected result·안전한 fixture를 고정한다.
3. 정상/음성/실패·복구 명령, 성공/중단 기준·원복 담당을 기존 책임 Runbook에서 구체화한다.
4. 명령·RC·stdout/stderr·actual identity·주요 결과를 원본으로 수집하고 각 단계 상태를 기록한다.
5. 원본 파일/Bundle·Manifest SHA256, 수신 범위·마스킹·Reviewer·편입/merge·publication 상태를 연결한다.
6. 실패 원인/변경 영향을 해결한 뒤 필요한 시험만 재실행한다. cleanup 실패·부분성공을 전체 PASS로 기록하지 않는다.
7. AC 수용과 Gate·정본 발행은 해당 책임자가 실제 증적·승인 범위로 별도 판정한다.

기존 [16 case 초안](../phase2/preparation/20261007/test-case-draft.tsv)은 APP/E2E/Delivery 세부 준비의 일부다. 전체 Phase 2 범위는 이 계획 TP0-01~15와 원문 AC mapping을 따른다. 첫 2개 Lab case는 비인수 사전검증이고 대응 ROSA 통제는 TP0-07/11에서 재검증한다.

현재 STATIC=설계·정합성 검토 대상 / MOCK·LAB-PRECHECK·RUNTIME·ACCEPTANCE 신규 수행=NOT_RUN.
CI/REVIEW/MERGE/PUBLICATION은 최신 PR150 기록을 확인한다. 이 문서는 신규 구현 코드·AWS/ROSA Runtime 변경·승인·티켓 종결을 수행하지 않는다.
