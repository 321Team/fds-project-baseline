# v3.1.21 Canonical Candidate

> **Status:** CANDIDATE / COLLECTING / NOT RELEASED  
> **Started:** 2026-09-27 KST  
> **Base canonical:** `docs-v3.1.20`  
> **Source main snapshot:** `e603d0d0177081d6f60b823f66e3559911c56272`  
> **Latest intake refresh:** `2026-09-30 KST`  
> **Candidate/main sync commit:** `e0e1889fd5a7c465c167d79d7533e40f2dd2b596`

이 브랜치는 v3.1.20 발행 이후의 정본 동기화 입력을 미리 수집하는 **후보 수집 지점**이다. 이 상태는 정본 승인·병합·Tag·Release 발행을 의미하지 않는다.

## 이번 사전 수집에 포함한 것

- v3.1.20 발행 후 main 및 관련 저장소의 Merged 변경 이력 수집.
- v3.1.20 발행 후 정정 기록에서 지정한 v3.1.21 이월 항목 수집.
- `DEC-P1-IMG-01`(#110)은 **Review Owner Decision 승인 완료**를 기록하되 Issue/Project 메타데이터 `To Do/Todo` drift와 Delivery Runtime `NOT_VERIFIED`를 함께 보존한다.
- 관련 `fds-msa#9`은 병합 입력으로 승격했지만 on-prem Test→Build→Scan, Harbor Push, Kubernetes Deploy 완료로 확대하지 않는다.
- `audit/canonical-candidate-20260927/proposed/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx` 후보 생성.
  - 2026-09-28 이재환: 개인 사정으로 인한 휴가
  - 2026-09-29 이하영: 채용설명회 및 직무테스트로 인한 휴가
  - 개인 부재 계산 범위를 Team Calendar 12행 → 14행으로 확장.
  - 기존 일정·Status·Lead/Support를 자동 변경하지 않음.
  - 영향 창: `DEC-P1-IMG-01`, `CR-P1-MON-01-01`, `CR-P1-MON-01-02`.

상세 수집 근거는 `audit/canonical-candidate-20260927/`을 따른다.

## 2026-09-30 ROSA 범위·Priority 전수 검수

- 현행 인용 정본을 `docs-v3.1.20 / RELEASED`로 명시하고, v3.1.20 파일에 남은 발행 전 Candidate 표현이 현재 상태로 오용되지 않도록 status/citation correction을 후보 브랜치에 반영했다.
- 상세 검수: `audit/phase2-rosa-scope-priority-review-20260930/README.md`
- Machine-readable matrix: `audit/phase2-rosa-scope-priority-review-20260930/priority-matrix.json`
- P1 carry-over:
  - #25 P1-MON-02 → Phase 2 / P1 / G6 non-blocking
  - #26 P1-DR-02 → Phase 2 / P1 / G6 non-blocking
  - #27 P1-HA-02 → Phase 2 / P1 / G6 non-blocking
- P2-OADP-01(#44): P0 → **P1**, G6/E2E non-blocking
- Dependency correction:
  - #45에 P2-CICD-01(#46) 선행조건 추가
  - #49/#50/#53에서 P1 OADP를 P0 blocker에서 제거
  - #54 Related Decision에 D25/D26 보완
- #40/#41/#48/#51/#95는 P1/conditional 또는 Deferred 원칙을 유지한다.
- ROSA 공통 기준은 managed/customer 책임경계, Terraform Source, STS/OIDC, SCC/RBAC/NetworkPolicy, Source→Runtime→Evidence, failure/recovery를 사용한다.

**주의:** 위 Issue metadata/body 변경은 운영 입력으로 이미 반영했으나, 후보 WBS/Baseline/Ticket Pack 전체 재생성은 아직 수행하지 않았다. 정본 후보 산출물은 Issue 최신 상태를 수집하여 일괄 재생성한다.

## 2026-09-30 선택 제품 유입 범위

- 회의 결과: **추가 절차 간소화 미적용 / 현행 Governance·Review·Evidence 절차 유지 / 후속 재검토**.
- 활성 추가 제품 검토는 다음 두 P1 Decision으로 한정:
  - #120 `DEC-P2-GITOPS-01` — OpenShift GitOps(Argo CD), P1 / G5·G6 non-blocking
  - #121 `DEC-P2-COMP-01` — Compliance Operator, P1 / G5·G6 non-blocking
- #120 미결정이면 #46 Runner direct ROSA Delivery를 유지한다. Go 시에만 Delivery Contract 변경 CR을 발행한다.
- #121 미결정이면 #38 현행 ROSA Platform/Security P0 AC를 유지한다. Compliance 결과는 자동 P0 blocker나 규제 준수 인증으로 확대하지 않는다.
- RHOAI(#95)는 P1/Deferred 우선이며 이번 활성 유입 범위에서 제외한다.
- 상세: `audit/phase2-product-intake-20260930/README.md`

## 2026-09-30 일정 재계획

- **Project Close:** 2026-10-26(월) 확정
- **Non-working:** 10-05, 10-09, 토·일
- **Phase 1:** 10-02 G3/최종 증적·문서 cutoff → 10-06 Review/Close
- **Phase 2 Start:** 10-07
- **G4:** 10-14
- **G5:** 10-20
- **G6:** 10-22
- **Deliverable Freeze / Phase 2 Review:** 10-23
- **Project Close:** 10-26
- 상세: `audit/project-schedule-replan-20260930/README.md`
- Machine-readable: `audit/project-schedule-replan-20260930/schedule.json`
- 기존 후보 WBS XLSX는 이번 재계획 전 생성본이므로 **STALE / 전체 재생성 대상**이다. 최신 Issue 일정에서 재생성하며 바이너리 부분 패치로 정합성을 깨지 않는다.

## 후보 WBS 위치와 Gate 경계

사전 수집 단계에서는 WBS를 `audit/canonical-candidate-20260927/proposed/` 아래에 둔다. `wbs/FDS_v3.1.21_...` 경로는 Manifest/SHA256SUMS/ZIP/WEB 등 전체 릴리즈 세트가 준비될 때 승격한다. 이는 `canonical-integrity`가 불완전한 릴리즈 후보를 차단하는 현행 Gate와 일치한다.

## 아직 정본 후보 완성으로 판정하지 않는 항목

다음은 이 PR에서 **수집/기록만** 하고 최종 정본 동기화 완료로 판정하지 않는다.

- Baseline / Ticket Pack / Description 전체 재생성 및 상호 대조
- ROSA 범위·P0/P1 재분류를 WBS Priority/Phase/Milestone에 동기화
- v3.1.20 발행 후 정정 사항의 전체 반영
- Manifest / SHA256SUMS / Distribution ZIP / WEB snapshot 생성
- 필요 시 Architecture 재발행 사유 판정
- 전체 Workbook 수식 재계산 및 렌더링 기반 시각 QA
- GitHub Release Tag/Asset 발행 검증

열려 있는 구현·증적 PR은 병합 완료 입력으로 승격하지 않는다. 현재 제외 목록은 audit 기록의 **Open / excluded** 절을 따른다.

## Release gate

최종 v3.1.21 병합/발행 전에는 `governance/RELEASE_POLICY.md` §2~§6의 필수 산출물과 검증을 다시 수행해야 한다.
