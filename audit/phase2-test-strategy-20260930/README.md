# Phase 2 Cost-aware Test Strategy — 2026-09-30 KST

## 1. 승인 상태와 목적

- Record ID: **P2-TEST-STRATEGY-01**
- 사용자 승인: **APPROVED STRATEGY INPUT — 2026-09-30 KST**
- 현행 정본: `docs-v3.1.20 / RELEASED`
- 차기 정본 후보: Draft PR #112 / `release/v3.1.21`
- 적용 범위: Phase 2 P0 Runtime/Integration/E2E와 P1 선택 시험의 실행 순서·비용 통제
- 비용 Decision: `DEC-P2-COST-01`
- 일정 기준: Phase 2 Start 10-07 / G4 10-14 / G5 10-20 / G6 10-22 / Freeze 10-23 / Project Close 10-26
- Phase 2 가용 작업일: **13일**
- Native Test Strategy Issue: **NOT CREATED**
- Issue 본문 직접 추가는 `governance/TICKET_SYNC_POLICY.md §5.1`에 따라 담당자 수동 반영 대상으로 둔다.

이 전략은 기존 티켓 Acceptance Criteria를 확대하거나 축소하지 않는다. **같은 AC를 더 저렴하고 재현 가능하게 검증하기 위한 실행 통제**다.

## 2. 프로젝트 제약을 반영한 핵심 원칙

1. **Phase 1 계약을 먼저 고정한다.** Phase 2 ROSA에서 요구사항·실패정책을 다시 정의하지 않는다.
2. **Shift-left.** Local/CI/제공 OCP Lab에서 제거 가능한 결함은 유료 ROSA에 반입하지 않는다.
3. **ROSA 생성은 늦추고, 한 번 생성한 Cluster는 G5→G6까지 같은 Runtime으로 연속 사용한다.**
4. **P0 우선.** GitOps/Compliance 등 P1은 P0 일정·비용을 침해하면 Deferred한다.
5. **유료 재시험은 변경 근거가 있어야 한다.** 동일 실패를 Source/설정 변경·사전검증 없이 반복하지 않는다.
6. **Full ROSA destroy→recreate는 P0 필수 시험이 아니다.** 이번 P0에서는 Terraform 재-plan/drift, App redeploy, 최종 teardown으로 재현성을 증명한다.
7. **10-22는 최초 디버깅일이 아니라 최종 Regression/Acceptance 일로 사용한다.**
8. **10-23은 신규 기능/선택 시험을 시작하지 않는다.** Final Evidence/Cost/Resource Inventory와 teardown을 우선한다.
9. **10-26 Project Close는 기본적으로 Evidence 기반으로 수행한다.** 별도 승인된 실시간 Demo 요건이 없으면 10-23 이후 ROSA를 유지하지 않는다.

## 3. Phase 1 → Phase 2 계약 Gate

Phase 2의 Failure/Recovery Expected Result는 #119의 정식 변경결정 결과를 소비한다.

현행 변경안 기준:

- 외부 DB 장애: transaction-api `/readyz=503` 및 Endpoint 제외
- fds-engine 장애: transaction-api Ready 유지, 거래 `HTTP 201`, `fds_evaluation_skipped=true`로 fail-open 저장

**#119가 승인/반영되기 전에는 위 문구를 Phase 2 최종 Acceptance로 확정했다고 기록하지 않는다.**

ROSA 유료 Runtime 전 최소 조건:

- P1 App/E2E의 최종 Expected Result와 Known Issue가 고정됨
- #119의 승인/잔여판정이 명시됨
- Phase 1 Close에서 Phase 2로 넘길 미완료 항목의 Owner/Due가 기록됨

## 4. Runtime Window 설계

| Window | 기간/조건 | 환경 | 목적 | 비용 성격 |
|---|---|---|---|---|
| **W0 PRECHECK** | 지금~10-08 | Local/CI + 제공 OCP(허용 시) | App/Manifest/OpenShift 호환성, 계약 선검증 | 프로젝트 Cloud 비용 최소 |
| **W1 G4** | 10-07~10-14 | AWS/OCI/Network 중심 | D21, IaC, IAM/OIDC, VPN, Registry 결정 | 제한적 유료 |
| **W2 G5** | 10-14~10-20 | 실제 ROSA | Platform→App→Runner Delivery | 주요 유료 Runtime |
| **W3 G6** | 10-20~10-22 | **W2와 동일 ROSA** | Hybrid→E2E→Failure/Recovery→Regression | 주요 유료 Runtime |
| **CLOSE** | 10-23 | 동일 환경→teardown | Final Evidence/Cost/Inventory/삭제 | 신규 시험 금지 |

### W0 — 무료/저비용 사전제거

제공 OCP는 **LAB-RUNTIME/PRECHECK**로만 사용한다.

공급자 정책이 허용하면 다음을 사전검증한다.

- transaction-api / fds-engine Deployment
- arbitrary UID / SCC 호환
- SecurityContext
- Service / Route
- /livez / /readyz
- Config/Secret 구조
- ServiceAccount / namespace RBAC
- NetworkPolicy
- 4 Rule Smoke
- Pod restart/recovery

다음은 OCP Lab 결과로 대체하지 않는다.

- AWS STS/OIDC/IAM
- ROSA HCP 특성
- AWS/OCI/VPN Hybrid path
- 최종 ROSA Runtime
- 최종 Hybrid E2E
- GitOps/Compliance Runtime

공급자 답변이 늦으면 W0 OCP 실행은 **non-blocking**이며 Local/CI 선검증만 완료하고 실제 OpenShift compatibility를 W2에서 소비한다.

### W1 — G4 / ROSA 생성 전 결함 제거

순서:

`Terraform fmt/validate → Plan Review → D21 Go/No-Go → IAM/OIDC/Network prerequisite → VPN/Route → Cost GO → ROSA Create`

- #36 D21은 10-08까지 단일 Primary/Fallback으로 결정한다.
- #35/#37의 준비·검증이 완료되기 전 ROSA를 장시간 먼저 띄워두지 않는다.
- #38의 10-12~10-14 작업은 Region/Version/Quota, STS/OIDC, Namespace/RBAC/NetworkPolicy/SecurityContext, Terraform input 등 **creation readiness**로 수행 가능하다.
- 실제 ROSA Create는 G4에 가까운 시점, 명목상 **10-14 전후**를 목표로 한다.
- 티켓 Start/End 자체는 이번 전략으로 변경하지 않는다.

### W2 — G5 / Platform → App → CI/CD

#38 → #43 → #46 순서로 실행한다.

**#38 Platform capture**
- Cluster/Worker Ready
- Version
- 승인 Identity/RBAC
- Namespace
- NetworkPolicy
- SecurityContext
- Hybrid route prerequisite
- Cost/Lifecycle

동일 사실을 의미 없이 반복 캡처하지 않는다.

**#43 App**
- transaction-api Ready
- fds-engine Ready
- transaction-api Route health
- fds-engine 외부 직접 노출 금지
- R01 / R02 / R04 / R07 Smoke

**#46 CI/CD**
기본 유료 Runtime은 아래 두 종류로 충분하게 설계한다.

- RUN-A: 정상 Pipeline → Test → Scan → Registry → ROSA Deploy → Health/Rule Smoke
- RUN-B: 고의 Test 또는 Scan FAIL → Deploy 차단

Commit SHA → Image Digest → ROSA Runtime imageID 추적을 보존한다.

### W3 — G6 / Hybrid + E2E 묶음 실행

#47과 #50은 가능한 한 하나의 승인 Runtime Window에서 연속 수행한다.

1. Hybrid TCP/DB 정상 연결
2. 정상 Transaction
3. R01
4. R02
5. R04
6. R07
7. 미승인 DB/Source 차단
8. 외부 DB 장애 — 승인된 Expected Result 확인
9. fds-engine 장애 — 승인된 fail-open Expected Result 확인
10. Tunnel Down
11. Tunnel Recovery
12. Final Regression

모든 거래는 가능한 범위에서 Transaction ID로 API/FDS/DB Evidence를 연결한다.

내부 실행 목표:
- 10-20: Hybrid 기본 path 최초 성공
- 10-21 오전: 정상 + Rule + DB
- 10-21 오후: Negative + Failure/Recovery 준비/실행
- 10-22: Final Regression + Evidence 확정

10-22에 처음으로 전체 E2E를 시작하는 계획은 사용하지 않는다.

## 5. ROSA Create 전 Cost GO Checkpoint

정식 Milestone을 새로 만들지 않고 **Execution Checkpoint**로 운영한다.

### 기술 조건

- Phase 1 App/Failure contract: FROZEN 또는 승인된 Known Issue로 인계
- D21: DECIDED
- Terraform Plan: REVIEWED
- D22 Registry: DECIDED
- VPN prerequisite: READY 또는 승인된 적용계획 고정
- ROSA inputs: FROZEN
- Control Cost: KNOWN
- P0 Cost-to-Complete: ESTIMATED

### 비용 판정

- **GREEN:** Control Cost + 예상 P0 완료비용 ≤ $400 → 계획대로 P0 진행
- **AMBER:** $400 초과 예상, $450 미만 → 신규 P1/선택 시험 Deferred, P0-only로 재계획하고 teardown 시점 재확정
- **RED:** Control Cost 또는 예상치가 $450 이상 → 신규 유료 Runtime/Create/Recreate 금지, Hard Stop/cleanup 적용
- **$450~$500:** 테스트 예산이 아니며 billing lag/teardown delay/cleanup residual 전용

`Control Cost` 정의는 DEC-P2-COST-01을 따른다.

## 6. 재시험 정책

유료 Runtime 재시험 전 반드시 다음을 남긴다.

`Failure → Root Cause/Hypothesis → Source/Config 변경 SHA → STATIC/LAB Precheck → Expected Result → Paid Retest`

- Source/Config 변경 없이 동일 유료 시험을 반복하지 않는다.
- 환경성/일시성 오류라면 재실행 사유와 관측 차이를 기록한다.
- 추가 재시험이 필요하면 Defect/실패 원인과 영향을 Evidence에 연결한다.
- 비용 절감을 이유로 승인된 Negative/Recovery AC를 생략하지 않는다.

## 7. Full ROSA Recreate 판정

이번 P0에 **Full ROSA destroy→recreate→E2E 재수행을 추가하지 않는다.**

P0 재현성 확인:
- Terraform fmt/validate/plan
- 재-plan 시 비의도 drift 없음
- App redeploy
- 동일 Commit/Image Digest 추적
- 최종 teardown과 Resource inventory 확인

Full ROSA recreate는 아래 조건을 모두 만족할 때만 **조건부 P1**로 검토한다.

- 모든 P0 Runtime/G5/G6 완료
- Control Cost 및 P0 Cost-to-Complete가 $400 Target을 침해하지 않음
- 10-23 Freeze를 지연시키지 않음
- 별도 실행 목적과 Acceptance가 고정됨

## 8. P1 제품 시험

#120 GitOps / #121 Compliance는 **Deferred-first** 원칙을 적용한다.

다음 중 하나면 구현/Runtime을 Deferred한다.

- P0 결함/재시험이 남음
- Control Cost가 $400을 초과하거나 초과 예상
- G5/G6 일정 영향 예상
- Operator 공급/권한/공용 Lab 정책 미확정

Decision 자체는 수행할 수 있으나 **Decision 완료와 Runtime 구현을 구분한다.**

## 9. 10-23 Freeze / Teardown

별도 승인된 10-26 실시간 Demo 요구가 없으면:

`10-22 G6 → 10-23 Final Evidence/Cost/Inventory → ROSA teardown → Resource deletion 확인 → 10-23 Freeze → 10-26 Evidence 기반 Close`

- 삭제 명령 실행만으로 종료로 보지 않는다.
- 실제 프로젝트 귀속 리소스 inventory와 비용 증가 정지 여부를 확인한다.
- 10-23 이후 신규 P1/선택 시험을 시작하지 않는다.
- 10-23 이후 ROSA 유지가 필요하면 이유·예상 비용·종료시각을 별도 기록한다.

## 10. Runtime Window Evidence Contract

각 유료 Window는 최소 다음을 기록한다.

- Window ID
- 대상 Ticket/AC
- 시작/종료 시각(KST)
- Cluster/Region/Version
- Source Commit / Terraform SHA / Image Digest
- 시작 전 Control Cost / 예상 Cost-to-Complete
- 실행 Test Case
- Result / Defect
- 재시험이면 변경 SHA와 사유
- 종료 후 Cost/Resource inventory
- teardown 여부
- 원본 로그/명령/종료상태
- Evidence archive SHA256

Source → Runtime → Evidence → Cost chain을 유지한다.

## 11. 티켓 영향

| Ticket | 적용 |
|---|---|
| #33 | Phase 2 Start에서 계약·P0 범위·Cost strategy 인계 확인 |
| #34 | Architecture에 W0~W3/Cost GO/teardown 경계 연결 |
| #35 | ROSA Create 전에 fmt/validate/plan 및 비용 리소스 고정 |
| #36 | 10-08 D21 단일안 확정; 장기 조사로 ROSA 비용창을 잠식하지 않음 |
| #37 | G4 전 VPN/Route 기본 path와 recovery 입력 확보 |
| #38 | 10-12부터 준비 가능, 실제 유료 Create는 G4 근처로 늦춤 |
| #43 | OCP Precheck 결과를 소비하되 ROSA App Smoke는 별도 수행 |
| #46 | 정상 1종 + 실패차단 1종 중심으로 Delivery Evidence 확보 |
| #47 | Hybrid 기본 path를 10-20부터 확보 |
| #50 | 10-21 대부분 실행, 10-22 Final Regression/Evidence 확정 |
| #49 | Window/Cost/Source→Runtime→Evidence chain을 Deliverable에 반영 |
| #55 | 비용·Runtime window·teardown 준수 검토 |
| #57 | 10-26 Close는 삭제/비용/잔여 Known Issue 확인 |
| #119 | Phase 2 DB/FDS 장애 Expected Result의 선행 계약 |
| #120/#121 | P1 Deferred-first / P0 non-blocking 유지 |

## 12. 현재 검증 상태

- STRATEGY INPUT: **APPROVED**
- CANDIDATE PR: **APPLIED**
- ISSUE BODY: **NOT MODIFIED**
- ISSUE OPERATING COMMENTS: **TO BE APPLIED**
- WBS XLSX: **STALE / REGENERATION REQUIRED**
- OCP APP PRECHECK: **NOT RUN**
- ROSA RUNTIME: **NOT RUN**
- COST MEASUREMENT: **NOT RUN**
- REVIEW / MERGE / PUBLICATION: **NOT DONE**

## 13. 적용 전 Issue snapshot

- #33: updated_at `2026-09-30T08:58:57Z` — [MS-P2-START-01] Phase 2 Start
- #34: updated_at `2026-09-30T13:12:04Z` — [P2-ARC-01] Hybrid / OCI / AWS / ROSA Architecture Freeze
- #35: updated_at `2026-09-30T13:12:14Z` — [P2-IAC-01] AWS / ROSA Terraform IaC
- #36: updated_at `2026-09-30T08:59:13Z` — [P2-OCI-01] OCI Relay Go / No-Go
- #37: updated_at `2026-09-30T08:59:39Z` — [P2-VPN-01] OCI Relay / AWS Site-to-Site VPN
- #38: updated_at `2026-09-30T13:12:24Z` — [P2-ROSA-01] ROSA Platform / Security
- #43: updated_at `2026-09-30T09:00:29Z` — [P2-APP-01] ROSA Application Deployment
- #46: updated_at `2026-09-30T09:00:40Z` — [P2-CICD-01] Runner to ROSA Delivery
- #47: updated_at `2026-09-30T09:00:46Z` — [P2-HYB-01] Hybrid DB / Registry Integration
- #49: updated_at `2026-09-30T13:12:52Z` — [P2-DOC-01] Cloud / Hybrid Deliverable Freeze
- #50: updated_at `2026-09-30T09:01:14Z` — [P2-E2E-01] Hybrid E2E / Regression
- #55: updated_at `2026-09-30T13:13:01Z` — [P2-REV-01] Phase 2 Review / Project Close Execution
- #57: updated_at `2026-09-30T13:13:11Z` — [MS-PROJECT-CLOSE-01] Project Close
- #119: updated_at `2026-09-30T08:58:51Z` — [CR-P1-APP-01-01] P1-APP-01 AC "DB/FDS 장애 시 /readyz 503" 문구 정정 — fds-engine fail-open 정합
- #120: updated_at `2026-09-30T09:06:38Z` — [DEC-P2-GITOPS-01] OpenShift GitOps (Argo CD) 도입 범위 결정
- #121: updated_at `2026-09-30T09:06:45Z` — [DEC-P2-COMP-01] Compliance Operator 도입 범위 결정

Issue 본문 수동 반영 또는 정본 재생성 시 최신 `updated_at`과 원문을 다시 대조한다.
