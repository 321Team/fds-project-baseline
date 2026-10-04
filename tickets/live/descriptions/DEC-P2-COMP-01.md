<!-- fds-canonical-live:v3.1.21 record-id:DEC-P2-COMP-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/DEC-P2-COMP-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 해당 업무의 기존 AC·Exit Criteria와 실행/인수 구분을 유지한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:DEC-P2-COMP-01:end -->

<!-- issue-decision-contract-20261001:v1:start -->
## 2026-10-01 Compliance Decision Contract v1

### Default
#38 P0 Security 완료 뒤 capacity-based / Deferred-first.

### Shared OCP
관리자 승인 또는 사전 설치 확인 전 설치/Scan HOLD. Lab Scan 결과를 ROSA Compliance Acceptance로 승격하지 않는다.

### Go condition
ROSA topology/HCP 조건, 지원 Version, profile/suite, result handling, Operator supply, 비용/일정, cleanup이 명확해야 한다.

### Exit
Go / No-Go / Deferred와 발견사항의 P0/Known Issue 경계를 기록한다. 규제 준수 인증으로 과대 표현하지 않는다.
<!-- issue-decision-contract-20261001:v1:end -->

<!-- shared-ocp-boundary-20261001:start -->
## 2026-10-01 공용 OCP Lab 실행경계

교육기관 제공 OCP는 **공용 Multi-tenant Lab**으로 사용한다. Cluster/Node 독점은 전제하지 않으며, 이 환경의 결과는 기본적으로 `LAB-PRECHECK`이다.

### 공통 자원·명명 규칙
- 사람 간 Team Code는 `J1`, `J2` 형식으로 관리하되 Kubernetes Namespace 실제 이름은 소문자 DNS 형식으로 매핑한다.
- Namespace: `j1-<purpose>`, `j2-<purpose>` 형식. 예: `j1-fds-app`, `j1-monitoring`, `j1-cicd-test`.
- Team Code 미배정 상태에서는 문서 템플릿에 `jX-<purpose>`를 사용하고 실제 생성 전에 코드와 Owner를 고정한다.
- 생성 자원에는 최소 `team`, `project=fds-hybrid`, `purpose` label을 부여하고, Owner/만료일은 annotation 또는 동등 추적정보로 남긴다.
- ResourceQuota/LimitRange의 **정확한 수치**는 공용 OCP 관리자 정책을 따른다. 임의로 quota를 확대하거나 다른 조의 자원을 침범하지 않는다.

### 허용/금지 경계
- 허용: Namespace-local Deployment/Service/Route, namespace RBAC, NetworkPolicy, SecurityContext, manifest/schema, health, image pull, 이미 제공된 Operator의 허용 범위 내 namespace-local CR 사전검증.
- 금지/사전승인 필요: 신규 cluster-wide Operator 설치, CRD/ClusterRole/SCC/MachineConfig/Node 설정 변경, cluster-admin 사용, Node 전용 affinity/taint로 사실상 독점, hostNetwork/hostPort/privileged의 임의 사용, Node reboot/drain·장애주입·대규모 load/performance/HA 시험.
- 공용 OCP의 다른 사용자 workload 영향을 받는 성능·용량·HA 수치는 **인수 증적이 아니다**.

### Evidence / Cleanup
- 증적에는 `ENV=SHARED_OCP_LAB`, Cluster/Version, Team Code, Namespace, 실행시각, manifest/source SHA, 명령/RC/원본 로그를 포함한다.
- 공용 OCP PASS를 ROSA Runtime PASS로 승격하지 않는다. ROSA P0 인수조건은 실제 ROSA에서 재검증한다.
- 시험 종료 시 자기 Team Namespace/자원만 정리하고, 삭제 전/후 resource inventory를 보존한다.
<!-- shared-ocp-boundary-20261001:end -->

### 이 티켓 적용
Compliance Operator 설치/Scan은 공용 Cluster에 영향을 줄 수 있으므로 관리자 명시 승인 또는 사전 설치 확인 전에는 HOLD한다. 허용되더라도 Lab 결과는 ROSA Compliance Acceptance가 아니라 Precheck다.



<!-- schedule-realign-20261001:issue-121:start -->
## 2026-10-01 일정·WIP 정합화

- **Deferred-first:** Compliance Operator Decision은 #38 P0 Security 완료 뒤 여유가 있을 때만 수행한다. 미수행 시 기존 Security AC를 유지하고 Deferred 근거를 남긴다.

- Scope/AC/Priority/Review Authority 변경 없음.
- P1 Decision은 P0 Gate를 자동 차단하지 않는다.
<!-- schedule-realign-20261001:issue-121:end -->
# DEC-P2-COMP-01 — Compliance Operator 도입 범위 결정

> 신규 Decision · 2026-09-30 KST
> 현행 정본: `docs-v3.1.20 / RELEASED`
> 차기 정본 후보: Draft PR #112
> **Priority P1 / G5·G6·Project Close non-blocking**

## 티켓 속성

| Property | 입력값 |
|---|---|
| Record ID | DEC-P2-COMP-01 |
| Phase | Phase 2 |
| Category | OpenShift / Security Compliance |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | TBD — G5 이후 P0 잔여 capacity 시 |
| End | TBD — 10-26 이전 강제하지 않음 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | Compliance Operator 도입/미도입/유예를 단일안으로 결정하고, 도입 시 ROSA topology(HCP 여부)·지원 Version·Scan profile/suite·결과 처리·Known Issue 경계·Operator 공급경로를 승인 |
| Related Decision IDs | D17(Security); D26(Operator 공급망); 신규 Decision Register 순번은 차기 정본에서 부여 |
| Related Risk IDs | RISK-07; RISK-10; RISK-11 |
| Source | 2026-09-29 팀 회의 Red Hat 제품 검토; 2026-09-30 사용자 범위 결정; Red Hat Compliance Operator 공식 문서; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | P1/non-blocking. #38 ROSA Platform/Security P0와 겹치지 않도록 G5 이후 capacity가 있을 때만 결정한다. Go 전에는 #38 현행 Security AC를 유지한다. |

## User Story

ROSA 보안 담당자로서 Compliance Operator를 제한된 보안 점검 수단으로 도입할지 결정한다. 이를 통해 설정 점검 결과를 반복 가능하게 수집하되, 교육/PoC 프로젝트를 규제 준수 인증으로 오표현하거나 발견사항 전체를 즉시 P0 범위로 확대하지 않는다.

## In Scope

- ROSA/HCP 지원성 및 설치 조건 확인
- Compliance Operator 설치/유예 결정
- 최소 ScanSetting/ScanSettingBinding/ComplianceSuite 범위
- Profile 선택 기준
- Scan 결과와 Source/Cluster/Operator Version 연결
- NonCompliant 결과의 Known Issue/Owner/Due 처리 기준
- Rerun/cleanup/recreate 검증
- D26 Operator 공급경로
- Evidence 보존 기준

## Out of Scope

- 금융 규제 준수 인증 주장
- 모든 NonCompliant 항목의 즉시 remediation
- P0 Gate 자동 차단
- Managed control plane에 대한 고객 직접 remediation
- 결정 전 Operator 설치

## Acceptance Criteria

- [ ] 도입 / 미도입 / 유예가 단일안으로 기록된다.
- [ ] ROSA topology와 Compliance Operator 지원 조건을 확인한다.
- [ ] HCP 사용 시 control-plane 접근 제약과 Operator scheduling 조건을 반영한다.
- [ ] 최소 Scan profile/suite와 대상 node/workload 범위를 고정한다.
- [ ] PASS/FAIL가 아니라 Compliant/NonCompliant/Error/NotApplicable 결과를 구분한다.
- [ ] NonCompliant 결과는 Severity/적용가능성/P0 영향 검토 후 Known Issue 또는 별도 Task로 이관한다.
- [ ] Operator Version/Subscription/Scan Source/Result/Evidence SHA를 추적한다.
- [ ] 재실행 및 cluster recreate 후 동일 Source로 재현 가능함을 검증할 계획을 정한다.
- [ ] G5/G6 일정 침해 시 Deferred로 전환한다.

## Dependency / Relation

- Related: #34 P2-ARC-01, #38 P2-ROSA-01, #41 DEC-P2-OP-01, #49 P2-DOC-01
- **P0 Blocker: 없음**
- 도입 결정 시: 필요하면 별도 P2-COMP-01 구현 Task 발행
- Milestone: G5 ROSA Application Ready (추적용이며 Gate blocker 아님)

## Decision Control

Red Hat 공식 문서에는 ROSA HCP에서 Compliance Operator를 설치하는 별도 절차가 있으며, Compliance Operator 1.5.0부터 ROSA HCP에 대해 테스트되었다고 명시되어 있다. HCP는 관리형 control plane 접근이 제한되므로 기본 master node scheduling을 그대로 사용할 수 없고 Subscription scheduling 설정을 조정해야 한다.

제품 설치 가능성과 프로젝트 P0 필요성은 별개다. 이번 프로젝트에서는 보안 검증 고도화용 P1 Decision으로만 관리한다.

공식 참조:
- https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/compliance-operator

## Completion Record

- Result: PENDING DECISION
- Runtime: NOT RUN
- Review: NOT DONE
