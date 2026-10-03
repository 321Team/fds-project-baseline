# v3.1.21 Candidate — 최신 수집 2026-10-03

**CANDIDATE / COLLECTING / NOT RELEASED**

- Source main: `67ba6cf8a7f187e2dfcf188e4b2c55a853993778`
- Candidate 입력 HEAD: `39549c3b4aed92e6ea1e6e54735bfbe833b9c869` / behind=0
- 수집 시각(KST): 2026-10-03T11:53:07.711+09:00
- 14개 저장소 merged 257건, 기존 대비 144건 추가. infra-dns 신규 수집 포함.
- 상세·HEAD·원문·diff·생성 규칙: `audit/canonical-refresh-20261003/README.md`
- #110=Done Decision; #125/#130=CR completed; #126/#127/#128=no-change 이력. Runtime 완료와 분리.
- #34 최종 Freeze 목표=10-08 D21 이후; #35 Stage-A=동일일 조건부 handoff. source schedule.json 최신 이슈에서 재생성.
- P1 Close HOLD / D21 OPEN / Architecture HOLD / Stage-A NOT_READY.
- 기존 WBS STALE; 78개 Record 입력 인덱스/Baseline 변경 입력/10-06 Close 수신 구조 생성. 전체 Release Set은 NOT_GENERATED.

아래는 이전 수집 당시 원문이다. 오래된 source HEAD/날짜/#110 To Do/CR 미결 표기는 현행 판정으로 사용하지 않는다. 현재 상태는 위 스냅샷과 intake.json이 기준이다.

<details>
<summary>이전 수집 기록 — 역사적 원문</summary>

# v3.1.21 후보 사전 수집 기록 — 2026-09-27

## 1. 기준

- 정본 기준: `v3.1.20 / RELEASED`
- 발행 시각: 2026-09-23 02:37:13 KST
- 수집 기준 main: `e603d0d0177081d6f60b823f66e3559911c56272`
- 최신 상태 재수집: `2026-09-30 KST`
- 최신 main 동기화 merge: `904aa920750a109cbc4940ad1cdb429735b2d645` (main `c1d710c4f56f53d5ca274c5addbb8540cc6cff53` 포함)
- 후보 브랜치: `release/v3.1.21`
- 목적: 차기 정본 제작 전에 변경 입력과 미결 항목을 먼저 고정해 누락·중복 수집을 줄인다.
- 경계: 이 기록은 **CANDIDATE intake**이며 Runtime 완료, Gate 승인, 열린 PR 병합, 정본 발행을 새로 부여하지 않는다.

## 2. v3.1.20 이후 수집한 Merged 입력

### fds-project-baseline

`#83 #91 #92 #93 #94 #96 #97 #98 #99 #100 #101 #102 #103 #104 #105 #106 #107 #108 #111`

주요 의미:
- v3.1.20 finalization/후속 정정, 중간 산출물 일정 정합화
- Pre-check/Review Authority 및 Issue 동기화 정책 변경
- Phase 2 저장소·증적 경로 후속과 OCI/D21 일정 정합화
- Issue 본문/증적 경로 정정 이력
- `DEC-P1-IMG-01`(#110) Native Decision sync map 반영

### fds-project-evidence

`#7 #13 #16 #17 #19 #20 #21 #22 #23 #24 #25 #26 #27 #30 #31 #32 #33 #35 #36 #38 #39 #42 #49 #50 #51 #52 #53`

증적 원본의 존재를 수집 대상으로 삼되, 각 증적이 해당 Runtime/Gate 전체 완료를 의미한다고 확대하지 않는다.

### infra-ansible

`#42 #45 #46 #47 #48 #49 #50 #52 #54 #56`

주요 기능 입력: 일반 CI 준비/승인 기록, NTP 후속 검증기, injected facts 수정, LB Stage B 보조 inventory.

### infra-kubernetes

`#7 #11 #14 #15 #20 #22 #24 #25 #27 #28 #29 #30 #31 #32 #33 #34 #36 #37 #38 #39 #42 #43 #48`

주요 기능 입력: ICR/HEP-GNP·9100/10250 경로, kubelet serving TLS 후보/인수 입력, NodePort 30080 GNP, audit-window 정정, CP kubelet 10250 Worker source 허용.

### infra-lb

`#8 #9 #10 #11 #12 #13`

주요 기능 입력: Stage B 장애/복구 관측, failure budget 12/24s, SSH key 고정, readiness SSH PTY 비활성화.

### infra-cicd

`#29 #30 #31 #32 #33 #34 #35 #36`

Trivy/오프라인 수집·Runtime BLOCK 기록 및 검증 절차 정합화. BLOCK 기록은 PASS로 승격하지 않는다.

### infra-monitoring

`#6 #7 #8 #9 #10 #11 #20 #21 #22`

fds-app namespace 정정, monitor01 입력, Grafana namespace 정정, Alertmanager Discord receiver/KSM probe 반영.

### infra-db / infra-pki / infra-harbor-trivy / fds-msa

- infra-db: `#4 #5`
- infra-pki: `#5 #6`
- infra-harbor-trivy: `#4 #5`
- fds-msa: `#4 #5 #6 #8 #9`

## 3. 현재 계획 입력

### DEC-P1-IMG-01 (#110)

- Issue/Project 메타데이터 Status: **To Do / Todo 유지**
- Decision 판단: **APPROVED** — Review Owner `hayeounglee`가 DEC-01~04 및 7개 HOLD 조건을 제안대로 승인
- Start/End: 2026-09-27 ~ 2026-10-06
- Lead: 이재환
- Support: 이하영, 이권욱
- Review Owner: 이하영
- Related PR: `321Team/fds-msa#9` — **MERGED**, merge SHA `1c7f3651504097096c3a3fe4a86ac1973e169688`
- 승인된 방향: Wolfi + apko Python 3.13, P1 증적 계약, signed attestation Option A, 승인 후 구현 Gate
- Source/code 병합과 Delivery Runtime을 구분한다. `fds-msa#9` 병합으로 공급망 Source가 정본화됐지만 on-prem Test→Build→Scan, Harbor Push, Kubernetes Deploy, Runtime AC는 별도이며 현재 완료로 기록하지 않는다.
- 승인 후 Lead가 제안한 담당 분배·10/5 현장 전환 등의 추가 조건은 Review Owner 확인 전 기존 승인 범위에 자동 포함하지 않는다.
- Native GitHub Issue Type `Decision`은 아직 미적용이며 별도 ticket-sync 후속이 필요하다.
- 따라서 **Decision 승인 완료 / 메타데이터 drift 존재 / Delivery Runtime NOT_VERIFIED**로 기록한다.

## 4. WBS Team Calendar 반영

| Date | Person | 입력 | 직접 영향 |
|---|---|---|---|
| 2026-09-28 | 이재환 | 개인 사정으로 인한 휴가 | DEC-P1-IMG-01 Lead 가용성, CR-P1-MON-01-01/02 Support 가용성 |
| 2026-09-29 | 이하영 | 채용설명회 및 직무테스트로 인한 휴가 | CR-P1-MON-01-01/02 Lead 가용성, DEC-P1-IMG-01 Support/Review 가용성 |

적용 원칙:
- 개인 부재로만 기록하고 Global Non-working Date로 확대하지 않는다.
- 기존 Plan Start/End, Status, Lead/Support는 자동 이동·재배정하지 않는다.
- WBS/Gantt의 개인 부재 계산 범위만 새 Team Calendar 행까지 확장한다.
- `P1-MON-02 / P1-DR-02 / P1-HA-02`는 기존 End TBD를 유지한다.

## 5. Open / excluded — Merged 입력으로 승격 금지

- `fds-project-evidence#54` — P1-SEC-01 B1/B2 증적 편입 (evidence-layout 수정 필요)
- `infra-ansible#53` — NTP Runtime sample kubeconfig
- `infra-ansible#55` — kubelet serving TLS 6-node 영구 형상화
- `infra-kubernetes#49` — NodePort 32085 read-only drift precheck
- `infra-cicd#38` — Wolfi/apko 2-stage offline delivery contract
- `fds-msa#10` — Wolfi/apko exact offline base supply export

이미 병합된 `fds-project-evidence#50/#51`, `fds-msa#9`, `infra-kubernetes#7`, `infra-monitoring#20/#21/#22`, `infra-ansible#56`, `fds-project-evidence#52/#53`은 Open 제외 목록에서 제거하고 Merged 입력으로 승격했다.

위 Open PR은 상태 변화가 생기면 차기 intake refresh에서 다시 판정한다.

## 5.1 2026-09-30 ROSA/Priority 추가 입력

- 상세 감사: `audit/phase2-rosa-scope-priority-review-20260930/README.md`
- Priority matrix: `audit/phase2-rosa-scope-priority-review-20260930/priority-matrix.json`
- 실제 Issue 반영:
  - #25/#26/#27 → `phase:phase-2`, P1 유지, Milestone G6
  - #44 → Priority P1
  - #45 → #46 P2-CICD 선행조건 보완
  - #49/#50/#53 → OADP P1 non-blocking 정합화
  - #54 → D25/D26 Decision 참조 보완
- v3.1.20 status/citation 해석 문제는 **v3.1.21 후보 감사 기록에서만 설명**한다.
- `CURRENT.md`, `baseline/FDS_Project_Implementation_Baseline_v3.1.20.md`, `releases/v3.1.20/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.20.md`, `releases/v3.1.20/README.md`는 발행된 v3.1.20 정본 무결성을 위해 **main과 동일 바이트로 원복**했다.
- `docs-v3.1.20` Tag/Release Assets/SHA256SUMS 및 위 과거 정본 파일은 소급 변경하지 않는다.

## 5.2 2026-09-30 선택 제품/회의 결과 추가 입력

- 추가 절차 간소화: **이번에는 적용하지 않고 현행 유지, 후속 재검토**.
- 신규 P1 Decision:
  - #120 `DEC-P2-GITOPS-01` — OpenShift GitOps(Argo CD)
  - #121 `DEC-P2-COMP-01` — Compliance Operator
- 두 Decision 모두 G5/G6/Project Close non-blocking.
- 관련 Issue 연결: #34/#38/#41/#45/#46/#49/#53/#54.
- 회의록 후보와 Red Hat 제품 인벤토리 후보를 갱신했다.
- 상세 감사: `audit/phase2-product-intake-20260930/README.md`.

## 5.3 2026-09-30 일정 재계획

- Project Close: **2026-10-26 확정**
- Non-working: **10-05 / 10-09 / 토·일**
- Phase 1 final cutoff 10-02, Review/Close 10-06, Phase 2 Start 10-07.
- G4 10-14 / G5 10-20 / G6 10-22 / Freeze+Review 10-23 / Close 10-26.
- P1 구현 고정일은 제거하고 P0 잔여 capacity에서만 실행.
- 상세: `audit/project-schedule-replan-20260930/README.md`
- 기존 proposed WBS XLSX는 **STALE_REGENERATE_FROM_LATEST_ISSUES**로 판정.

## 5.4 2026-09-30 Cloud Cost 정책

- 사용자 승인 정책: **Target ≤ $400 / Operational Hard Stop $450 / Protected Reserve $50 / Total Ceiling $500**.
- 신규 Decision record: `DEC-P2-COST-01` — **APPROVED POLICY INPUT / P0 cost-lifecycle control**.
- $400 도달 또는 초과 예상 시 신규 P1/선택 실험 Deferred 우선.
- $450은 신규 유료 소비 Hard Stop이며 $450~$500은 billing lag·teardown delay·cleanup residual 전용 Reserve.
- 판정은 Actual/Gross + 확인 가능한 미반영/Projected cost를 포함한다.
- 관련: #34/#35/#38/#42/#49/#55/#57.
- Native Decision Issue는 TICKET_SYNC_POLICY §5.1에 따라 AI가 본문을 신규 작성하지 않고, `audit/phase2-cost-policy-20260930/`의 후보를 담당자가 수동 적용한다.
- 이 결정은 비용 통제를 승인한 것이며 AWS/ROSA provisioning·Runtime/Gate/Close 승인이 아니다.

## 5.5 2026-09-30 Cost-aware Test Strategy

- 사용자 승인 전략: **W0 PRECHECK → W1 G4 → W2 G5 → W3 G6 → 10-23 CLOSE/TEARDOWN**.
- ROSA는 G4에 가까운 시점까지 생성 시점을 늦추고, 생성 후 G5→G6를 동일 Cluster에서 연속 수행한다.
- Phase 1 Failure Contract(#119) 승인/잔여판정을 Phase 2 Expected Result의 선행 입력으로 사용한다.
- 제공 OCP는 LAB-RUNTIME/PRECHECK로만 사용하고 ROSA Runtime PASS로 승격하지 않는다.
- $400 Target 초과 예상 시 P1 Deferred-first, $450은 신규 유료 Runtime/Create/Recreate Hard Stop.
- Full ROSA destroy→recreate는 P0 필수가 아니며 조건부 P1.
- 10-21에 E2E 대부분을 수행하고 10-22는 Final Regression/Evidence 확정일로 사용한다.
- 별도 승인된 실시간 Demo 요구가 없으면 10-23 Final Evidence/Cost/Inventory 후 ROSA teardown을 기본값으로 한다.
- 상세: `audit/phase2-test-strategy-20260930/README.md`
- Machine-readable: `audit/phase2-test-strategy-20260930/runtime-window-plan.json`
- 기존 후보 WBS XLSX는 계속 **STALE / REGENERATION REQUIRED**이며 이 전략을 재생성 입력으로 포함한다.

## 5.6 2026-09-30 PR #112 무결성 정정

- 타 세션 PMO/QA 리뷰에서 발행된 v3.1.20 정본 파일 직접 수정이 `RELEASE_POLICY §2.4`와 충돌함을 확인했다.
- 다음 4개 파일을 최신 `main`과 동일 바이트로 원복했다.
  - `CURRENT.md`
  - `baseline/FDS_Project_Implementation_Baseline_v3.1.20.md`
  - `releases/v3.1.20/FDS_Project_Implementation_Baseline_Release_Notes_v3.1.20.md`
  - `releases/v3.1.20/README.md`
- latest `main`은 보조 PR #131로 후보 브랜치에 동기화했고, 동기화 후 `behind=0`을 확인했다.
- #125/#126/#127/#128/#130은 **미결 Change Request**이므로 결정 전까지 v3.1.21 승인 입력·정본 재생성 Source에서 제외한다.
- 본 정정은 Audit/Cost/Test Strategy 등 v3.1.21 신규 후보 기록을 폐기하지 않는다.
- 정본 재생성은 승인 완료된 Issue/CR만 Source로 사용하고, WBS/Baseline/Ticket Pack/Manifest/SHA256SUMS/ZIP/WEB을 일괄 재생성한다.

## 5.7 2026-09-30 Phase 2 담당 리밸런싱

- 팀 회고의 **3인 수행 전환 / 대형 티켓 집중 / 담당 인지 지연** 문제와 최근 #125~#130 CR·리뷰 피로를 반영해, 신규 리밸런싱 Ticket/CR을 추가하지 않고 기존 P0 3건의 실행 책임만 최소 조정했다.
- #35 P2-IAC-01: Lead **이권욱 → 이하영**, Support 이권욱
- #37 P2-VPN-01: Lead **이권욱 → 이재환**, Support 이권욱
- #42 DEC-P2-REG-01: Lead **이하영 → 이권욱**, Support 이하영·이재환
- 목적은 균등 분배 자체가 아니라 `Cloud Platform(#35→#38)`, `Hybrid data path(#37→#43→#47→#50)`, `Registry/CI-CD/Cost Governance(#42→#46)`의 연속 책임을 만들고 G4~G6 handoff를 줄이는 것이다.
- #35 이동과 동시에 #42를 반대 방향으로 이동해 이하영에게 대형 P0가 다시 집중되는 것을 방지한다.
- 일정·Scope·AC·Priority·Milestone·Review Authority는 변경하지 않았다.
- P1은 기존 Deferred-first/non-blocking을 유지한다.
- 상세: `audit/project-schedule-replan-20260930/README.md §5.1`.
- 기존 후보 WBS는 STALE이므로 다음 전체 재생성 시 최신 Issue Lead/Support를 Source로 반영한다.

## 6. v3.1.21 필수 이월 사항

`audit/canonical-followup-20260923/README.md`의 미반영 항목을 유지한다.

- `CURRENT.md` 및 발행된 v3.1.20 정본 파일은 **immutable history 유지**. 현재 후보에서는 직접 수정하지 않음
- v3.1.20 중간 산출물 DOCX 정정본의 차기 정본 무결성 반영
- v3.1.20 내부의 과거 CANDIDATE 표현에 대한 해석 정정은 **v3.1.21 Release Notes/audit에서만 기록**하고 과거 정본 바이트는 변경하지 않음
- governance drift를 차기 Manifest/SHA256SUMS에 동기화
- `retrospectives/`의 정본 체크섬 대상 편입 여부 결정

## 7. Candidate WBS 배치 원칙

초기 생성 시 `wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx` 경로는 정본 검증기가 완성된 v3.1.21 release set으로 판정해 SHA256SUMS/Manifest/ZIP을 요구했다. 파일 결함이 아니라 Release Gate 동작이었다.

따라서 사전 수집 단계에서는 동일 후보 원본을 `audit/canonical-candidate-20260927/proposed/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx`로 유지한다. 전체 정본 산출물을 재생성하는 시점에만 `wbs/` 정식 경로로 승격한다.

## 8. 완료/미완료 판정

- SOURCE COLLECTION: **REFRESHED (2026-09-27 17:43:36 KST 기준)**
- CANDIDATE BRANCH: **CREATED**
- WBS AVAILABILITY UPDATE: **APPLIED**
- ROSA / PRIORITY REVIEW: **APPLIED TO ISSUES + CANDIDATE AUDIT**
- PRODUCT INTAKE (#120/#121): **DECISION TICKETS CREATED / IMPLEMENTATION NOT RUN**
- PROCEDURE SIMPLIFICATION: **NO NEW CHANGE / CURRENT PROCESS RETAINED**
- v3.1.20 STATUS/CITATION CORRECTION: **APPLIED TO CANDIDATE BRANCH**
- SCHEDULE REPLAN: **APPLIED TO ISSUES + CANDIDATE AUDIT**
- CANDIDATE WBS XLSX: **STALE / REGENERATION REQUIRED**
- FULL CANONICAL REGENERATION: **NOT RUN**
- RUNTIME/GATE REVALIDATION: **NOT RUN**
- REVIEW/MERGE/RELEASE: **NOT DONE**


</details>
