# Phase 2 Test Strategy — 2026-10-07 개정안

상태: **WORKING REVISION / REVIEW PENDING**. 시험계획 변경안이며 Runtime 실행·AC 인수·새 정본 발행이 아니다.
작성: 이권욱 / CODEX_ASSISTED. 기존 PR150에서 중복 작업을 통합한다.

## 1. 적용 기준과 변경 범위

- 조회 기준: 2026-10-07 KST. baseline main `40ac664b83485745ab86b5018b8e19c386484cc8`.
- 최신 발행 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST, Tag commit `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- 승인된 기준: [v3.1.21 전략](FDS_Test_Strategy_v3.1.21.md), [Baseline](../baseline/FDS_Project_Implementation_Baseline_v3.1.21.md), 발행 Description 및 최신 승인 Decision/CR. [9/30 전략](../audit/phase2-test-strategy-20260930/README.md)은 작성 당시 이력을 보존한다.
- 실행 계획: [Phase 2 Test Plan](FDS_Phase2_Test_Plan_20261007.md). 조회 범위·Issue 본문 hash·댓글·열린 PR은 [sources.json](../audit/phase2-test-plan-20261007/sources.json)에서 추적한다.
- **기존 AC·Priority·담당·일정·Gate 권한은 변경하지 않는다.** 아래 시험 ID는 추적용이며 신규 AC가 아니다. 승인되지 않은 후보 설계는 Runtime 입력으로 사용하지 않는다.
- 발행된 v3.1.21 파일·Tag·Manifest·SHA256SUMS·WBS/배포물은 보존한다. 이 개정안의 PR 병합과 차기 정본 통합·발행은 별도다.

핵심 성공체인은 **우리 On-Prem → AWS/ROSA**의 IaC·VPN·Platform·Application·CI/CD·DB·E2E 및 기존 인수/정리 조건이다. 재현성 / 무결성 / 추적성 / 이식성을 같은 source와 실제 target의 증적으로 검증한다.

## 2. P0 / P1 판정

| 구분 | 적용 원칙 | Gate 영향 |
|---|---|---|
| P0 | 기존 정본/승인 변경의 필수 구현·Runtime·인수 시험. 준비·모의 결과와 실제 인수를 분리 | 해당 Gate의 필수 AC/Exit 미충족은 HOLD/FAIL 원인 |
| P1 | Compliance, 추가 보안/관찰성, 선택 기능, RHOAI/RAG, 추가 복구·비용/운영 최적화·PoC | 미구현/Deferred만으로 P0·G5·G6·Project Close를 실패 처리하지 않음 |
| 조건부/미결 | D22 Registry 선택, 필수 관리 DNS subset, Worker 규모 등 미결 계약 | 권위 결정 전 자동 P0 편입·P1 강등 금지. 필요한 P0 실행 입력만 HOLD |

P1에서 기존 P0 AC를 위반하는 실제 결함이 발견되면 **위반한 P0 AC**를 근거로 판단한다. P1 시험 미완료 자체와 구분한다.
티켓 이름의 `P1-`은 **Phase 1** 표시이며 Priority P1이 아니다. #125의 “backup/rollback P1 유지”를 선택적 Priority P1으로 오독해 기존 필수 보안통제를 강등하지 않는다.

## 3. Lab / 실제 Target 경계

```text
Kolon Benit OCP
= LAB-PRECHECK / COMPATIBILITY / REHEARSAL

AWS/ROSA
= P0 IMPLEMENTATION / RUNTIME / ACCEPTANCE
```

| 환경 | 허용 소비 | 인수 경계 |
|---|---|---|
| `ENV=SHARED_OCP_LAB` | 지원·Catalog·schema/admission, 허용 namespace의 UID/SCC·health·manifest 리허설 | 공용 테스트/사전검증 Lab. 실제 Target이 아님 |
| `ENV=AWS_ROSA` | 실제 승인 계정·Cluster·MachinePool·접근·배포·보안 Runtime | ROSA P0 인수조건은 실제 ROSA에서 재검증 |
| `ENV=ROSA_HYBRID` | 실제 ROSA + On-Prem 경로의 DB/Registry/VPN/E2E | 양쪽 source·route·identity를 결속한 실제 통합 인수 |
| `ENV=AWS_ONPREM_NETWORK` | ROSA 생성 전 G4용 AWS/On-Prem IaC·VPN 검증 | AWS 경로 검증이며 아직 ROSA Runtime PASS가 아님 |

ENV 표기는 문서의 증적 분류다. 기존 도구의 허용 ENV enum을 변경하거나 미지원 값을 실행 인자로 넣지 않는다.

Kolon OCP PASS를 **ROSA Runtime PASS / Migration Complete / P0 Acceptance / G5·G6 Exit**로 승격하지 않는다. Lab 미실행은 그 자체로 P0 차단을 추가하지 않으며, 실제 ROSA 필수 시험은 생략하지 않는다.

공용 Lab은 Team namespace·Quota·Owner/만료·cleanup을 따른다. 기술적 cluster-admin 권한은 독점 사용·Operator 설치·drain/reboot·공용 자원 변경의 승인 근거가 아니다. 신규 cluster-wide 설치, 장애주입·HA/부하 시험은 기존 허용범위/관리자 승인을 확인하기 전 실행하지 않는다. RHOAI는 §6의 read-only 범위로 제한한다.

## 4. 검증 단계

각 항목을 별도 상태로 기록한다. 일렬 진행으로 모든 단계를 자동 PASS 처리하지 않는다.

| 단계 | 의미 / 최소 기록 |
|---|---|
| STATIC | 문서·source·manifest·AC mapping·정적 검사 |
| MOCK | 합성 입력·격리 모의 경로. 실제 AWS/Cluster 증거 아님 |
| CI | exact commit의 실제 Run/Job/검사 수·결과. 검사 0건은 NOT_RUN |
| LAB-PRECHECK | 공용 Lab에서 실행한 호환성/리허설 범위와 제한 |
| RUNTIME | 실제 지정 target에서 수행한 명령·RC·raw·관측 결과 |
| REVIEW | 검토자·대상 SHA·검토 범위·판정. 자체 검토와 사람 독립 승인 구분 |
| MERGE | 실제 PR merge commit. 실행/인수와 별개 |
| PUBLICATION | 승인 정본·Tag·Manifest/Asset의 실제 발행 상태 |
| ACCEPTANCE | 해당 AC/Gate 책임자의 실제 증적 기반 인수 판정 |

- STATIC/MOCK PASS ≠ Runtime PASS
- CI PASS ≠ ROSA Runtime PASS
- Kolon OCP PASS ≠ ROSA Acceptance
- SHA256 일치 ≠ 시험 성공
- PR Merge ≠ Runtime Acceptance
- Runtime 실행 ≠ 정본 발행

## 5. 기존 TS01~16의 재정렬

원본 [TS01~16](FDS_Test_Strategy_v3.1.21.md)의 ID·의미·기록은 보존한다. 아래는 실행 우선순위/AC 적용 경계를 밝힌 것이며 새 인수조건이 아니다.

| 기존 ID | 이번 연결 | AC 경계 |
|---|---|---|
| TS01 | P0 준비 — #34/#35/#38 | 지원 Version/IAM/Quota·reviewed plan 등 생성 전 입력. actual Ready를 생성 전 요구하지 않음 |
| TS02 | LAB-PRECHECK → P0 ROSA — #38/#43 | admission은 실제 arbitrary UID/Ready와 다름. ROSA security·업무 재검증 필수 |
| TS03 | P0 승인 규모/용량 입력 + 미결 N-1/AZ 시험 | Worker count/type/AZ/limits는 Freeze 입력. N-1·AZ 장애를 새 필수 AC로 확정하지 않음; §9에서 결정 추적 |
| TS04 | P0 관리 접근/승인 DNS·TLS 기반 + P1 전체 Hybrid DNS | #40/#48 전체 Priority P1 유지. private 관리에 필요한 subset의 책임/시점 수용은 미결 |
| TS05 | P0 D21 원본/결정 추적 | AWS EC2+EIP Relay 최종 handoff를 사용. mismatched-PSK pathcheck ≠ 정상 Child SA |
| TS06 | P0 VPN — #37 | Tunnel UP·승인 TCP/미승인 차단·중단/복구. 추가 rekey/DPD/장시간 시험은 승인 계약 범위에서만 필수 판정 |
| TS07 | P0 Hybrid DB — #47 | actual approved source·API 양성·engine/미승인 음성. replacement 결합시험은 승인된 범위 확인 |
| TS08 | P0 선택 Registry — #42/#43/#47 | Harbor 선택 시 해당 trust/pull/권한·digest 검증. Harbor 미선택 시 승인 대안/Cancelled 근거, Harbor 전체 재인수 추가 없음 |
| TS09 | P0 #46 Delivery | RUN-A·RUN-B 및 source/digest/imageID 추적. Phase 1 #16→#13 공유 증적은 소비자 인수와 별도 |
| TS10 | P0 #46 기존 rollback 계약 | 이전 승인 digest로 복원·health. 신규 전체 플랫폼 재생성을 요구하지 않음 |
| TS11 | P0 #43/#47/#50 | 정상·4 Rule·DB 저장/조회와 Transaction ID trace |
| TS12 | P0 기존 #119 장애계약 소비 | DB /readyz503·Endpoint 제외, engine fail-open HTTP201·skipped=true·저장, 복구 회귀 |
| TS13 | Phase 1 #19/#125 인계/기존 rollback 책임 | Phase 2로 새 AC를 만들거나 예방 rotation을 자동 인수하지 않음. 수신·책임·승인 위험수용 경계 유지 |
| TS14 | P0 #38 Secret/권한·동등 통제 + P1 #44 OADP | root disk 암호화만으로 Secret 인수 금지. OADP 미실행은 P0 차단 아님 |
| TS15 | 추가 복합장애/회복탄력성 검토 | 기존 #37 tunnel recovery/#50 regression은 P0 유지. worker+Relay 동시 장애·AZ PVC/RPO-RTO는 승인 AC 없는 신규 필수시험으로 추가하지 않음 |
| TS16 | P0 종료/정리 — #49/#55/#57 | 실제 삭제·잔여 자원/비용·원본 보존. 삭제 명령 RC만으로 종료하지 않음 |

## 6. P1 시험과 RHOAI

| P1 영역 | 기존 연결 / 실행 기준 |
|---|---|
| Compliance·추가 Security validation | #121 / #38 P0 보안 완료 후, 적용 profile·지원/권한·결과 처리·cleanup 고정 |
| GitOps·Operator 공급 확장 | #120/#41/#51 / Go·별도 CR 전 Runner-direct P0 계약 유지 |
| OADP·추가 복구/회복탄력성 | #44, full ROSA recreate·복합장애 추가 시험 / 승인 범위·여유 비용/시간 확보 후 |
| 전체 Hybrid DNS 확장 | #40/#48 / Go+capacity 조건. 필수 private 접근 subset 미결과 분리 |
| 관찰성/운영·비용 최적화, 발표/PoC | 승인된 기존 범위 또는 별도 후속 결정. 새 모니터링 제품·목표 수치를 P0로 추가하지 않음 |
| RHOAI / RAG | #95 DEC-P2-RHOAI-01 / P1, Deferred-first, P0·Project Close·G5·G6 non-blocking |

### #95 최신 Lab 판정

근거: [2026-10-07 사전분석 댓글 6032524902](https://github.com/321Team/fds-project-baseline/issues/95#issuecomment-6032524902). 아래는 등록된 read-only 관측의 소비이며 이번 문서 작업에서 OCP를 직접 재조회한 결과가 아니다.

- OCP 4.20.0 / Kubernetes v1.33.5, Master 3 / Worker 2.
- Worker 각각 8 vCPU / 약 8 GiB RAM, allocatable 약 6.65 GiB. RHOAI Operator 미설치.
- `rhods-operator.3.5.1` Catalog 제공, 기술적 설치 권한·기본 StorageClass 경로 확인. **PVC Runtime·설치/삭제·RHOAI/RAG Runtime은 NOT_RUN**.
- **RESOURCE_GATE=FAIL / DEFERRED 권고**. 증설 가능성이 낮아 현재 Lab에서 설치를 시도하는 계획을 두지 않는다.
- [Red Hat 3.5 설치 요구사항 §3.1](https://docs.redhat.com/en/documentation/red_hat_openshift_ai_self-managed/3.5/html/installing_and_uninstalling_openshift_ai_self-managed/installing-and-deploying-openshift-ai_install): 최소 Worker 2대, 각 8 CPU/32 GiB RAM, workload 추가 자원 필요. 현재 Lab RAM은 미충족.
- Catalog의 RAG 구성요소 존재는 CPU-only RAG Runtime 지원/성공의 증거가 아니다. 같은 공식 문서의 OGX/RAG 구성요소 요구사항에는 GPU-enabled nodes 등이 명시된다. 실제 선택할 기능·CPU-only 지원성은 향후 Go 전 별도 확인한다. 이 미확인은 P1 내부 문제다.

현 계약은 **read-only catalog/support/compatibility**를 기본으로 유지한다. Resource Gate FAIL을 G5/G6 실패로 처리하지 않는다. Deferred 권고를 Issue #95의 실제 종결·승인 완료로 표시하지 않는다.

향후 Go 전환 조건: **별도 CR + ROSA 대상 구현 티켓**, Version/Quota/MachinePool, 총 비용/결제주체, Subscription/Entitlement, Operator 공급 및 설치/삭제·복구 경로를 확정한다. Go 결정만으로 RHOAI를 P0에 편입하지 않는다.

## 7. 실행 순서·재시험·이식성

`W0 STATIC/MOCK/CI/LAB-PRECHECK → W1 G4 → W2 실제 ROSA G5 → W3 동일 ROSA Hybrid/E2E G6 → 원본 보존/teardown/Close`를 유지한다.
정확한 작업창은 Test Plan §4의 최신 티켓 계획·미결사항을 따른다. #50의 10/21 주 시험안과 10/22 본문 조건을 자동 확정하지 않는다.

- Portable Core는 app/Rule/failure contract·source/digest·test/scan·기대값이다.
- Adapter는 ROSA API/context·namespace·SCC/arbitrary UID·Registry trust·VPN/source·DNS·MachinePool이다. On-Prem node IP·고정 UID·참고 manifest를 승인 ROSA 입력으로 복사하지 않는다.
- 같은 환경·source SHA/digest·설정·회차·기대값인 원본만 재사용한다. Lab→ROSA 증적 재사용으로 실제 인수를 대체하지 않는다.
- 실패 → 원인/가설 → 변경 SHA 또는 일시 오류 재시도 사유 → 필요한 STATIC/MOCK/CI/LAB-PRECHECK → 영향 Runtime 재검증. 필수 negative/recovery는 비용을 이유로 생략하지 않는다.
- P0 재현성은 기존 fmt/validate/plan·비의도 drift 없는 re-plan·app redeploy·source/digest trace·final teardown으로 확인한다. Full ROSA destroy→recreate는 9/30 승인 전략상 조건부 P1이며 §9의 #38 문구 차이를 그대로 기록한다.

## 8. 증적·중단·복구

P0 Runtime Record에는 가능한 범위에서 다음을 결속한다. 환경에 적용되지 않는 값은 N/A 사유, 미수신은 PENDING과 생산자를 적는다.

| 추적 묶음 | 필드 |
|---|---|
| 환경/주체 | ENV, 대상 Host/Cluster/Namespace, Region, 실행자·계정/권한 reference, 시작/종료 KST, Cluster/Platform Version |
| 구현 입력 | Git SHA / Bundle SHA, Manifest/Source SHA, Terraform plan/실제 ID, approved image digest / runtime imageID, adapter ID |
| 시험 | Ticket/원문 AC, Case/Window/Run ID·Attempt, fixture/schema revision, 실행 명령, Exit Code, stdout/stderr 원본 로그, 주요 결과·실패/미실행 범위 |
| 인수 체인 | 증적 파일 SHA256, 수신/원본 경로, Reviewer·검토 SHA/판정, RUNTIME / REVIEW / MERGE / PUBLICATION / ACCEPTANCE 각각 상태 |
| 종료 | before/after inventory, cleanup·복구 결과, 잔여 Owner/완료조건, 비용 source·예상 잔여 비용 |

합성 결과·템플릿·summary만으로 실제 Runtime 증적을 만들지 않는다. 비밀값·토큰·키·kubeconfig는 저장하지 않고 참조·sanitized 원본·마스킹 범위를 기록한다.
증적은 `fds-project-evidence:evidence/<Record ID>/<회차>/`에 기존 독립 편입 심사를 적용한다. 증적 PR 병합은 업무 AC 인수와 별개다.

Runtime 명령은 해당 구현 Runbook에서 대상·계정·권한·경로·선행조건·순서·성공·중단·원복을 고정한 뒤 실행한다.
대상/source 불일치, 예상 밖 권한·범위·비용 소비, TLS/방화벽/SCC 우회, 실패 후 배포 지속, 공유 자원 영향 또는 복구 불명확 시 신규 변경을 중단한다. 승인된 이전 상태/이전 digest로 복구하고 health·정책·잔여 자원을 재확인한다.
DB 시험은 전용 fixture/ID·mutation 창·정리/보존 기준으로 Phase 1/2 데이터를 분리한다.

## 9. 결정 필요 사항과 완료조건

| 미결/차이 | 기존 담당 | 완료조건 / P0 영향 |
|---|---|---|
| Worker type/count/AZ, N-1/AZ 장애 필요성, 지원 Version/Quota | #34 이권욱 + #38 이하영 | Lead 제안 HCP/m5.xlarge/1 AZ×3대를 지원/비용/용량 근거로 Freeze. 새 HA AC 확정 없음; 생성 입력 미확정은 관련 P0 실행 HOLD |
| Private 관리 DNS subset vs #40/#48 P1 순서 | #40 이권욱, #38 이하영 | API/OAuth/Ingress·Harbor/DB FQDN/SAN·route/source와 최소 query 계약/책임/시점을 수용. 전체 DNS P1 미완료는 비차단; 실제 P0 접근 불능은 해당 AC로 판단 |
| D22 final Registry / 실제 trust·source·digest | #42 이권욱, #38/#43 생산자 | Primary/Fallback 단일 승인, 논리 pre-create 계약과 Basic Ready 후 actual pull 인수 분리. 필수 #42 미결은 #43/#46/G5 입력 HOLD |
| #50 10/21 주 시험 vs 10/22 단일 조건 | #50 이재환 / PMO 이권욱 | #47 handoff 이후 승인 작업창·회귀 시간을 정렬. 날짜만으로 Gate FAIL/PASS 금지 |
| #38 “create/delete/recreate 후 재현 절차” vs full recreate P1 | #38 이하영 / #34 이권욱 | 기존 승인 전략과 절차 범위를 명시적으로 정합화. full ROSA recreate를 새 P0 필수로 추가하거나 기존 승인 요구를 삭제하지 않음 |
| 교육장 비용 한도·ROSA 서비스 비용·생성/삭제 시각 | #34/#35/#38 비용 입력 담당 | 최신 교육장 조건·결제주체·total-to-complete를 고정. 구 $400/$450/$500과 관계 미결; 미확인 0원/Cost GO 금지 |
| #35 full IaC source/API/permissions 및 #37 실제 Relay handoff | #35 이하영 → #37 이재환 | 중앙 4자원 PASS_USER_READBACK과 전체 IaC/업무역할·Stage-A를 구분, 구현 PR/SHA·권한·실제 Relay 입력 확보 |
| #47 DB 접근통제 이관 | #47 이재환 / 보안 이하영 | #19 이관 조건 후 기존 3건 적용·양성/음성·raw 확인. 이 문서가 Phase 1 Runtime 변경을 승인하지 않음 |
| RHOAI Go/Deferred, Entitlement·PVC·선택 RAG 지원성 | #95 이하영 | 현 Lab Deferred 권고·근거와 재검토 조건 기록. Go는 §6 조건. **P0 비차단** |

## 10. 이번 변경의 상태

STATIC=문서·AC·diff 검토 대상. MOCK/LAB-PRECHECK/RUNTIME/ACCEPTANCE 신규 실행=NOT_RUN.
REVIEW=CODEX_ASSISTED 자체 검토, 사람의 독립 승인 아님. CI·MERGE·PUBLICATION은 실제 PR/Run/Release에서 별도 확인한다.
현재 요청은 시험계획 갱신이다. AWS/ROSA·On-Prem 구현 코드·권한·Runtime을 변경하거나 Gate/티켓을 종결하지 않는다.
