# v3.1.21 후보 사전 수집 기록 — 2026-09-27

## 1. 기준

- 정본 기준: `v3.1.20 / RELEASED`
- 발행 시각: 2026-09-23 02:37:13 KST
- 수집 기준 main: `e603d0d0177081d6f60b823f66e3559911c56272`
- 최신 상태 재수집: `2026-09-30 KST`
- 최신 main 동기화 merge: `e0e1889fd5a7c465c167d79d7533e40f2dd2b596`
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
- v3.1.20 status/citation correction을 `CURRENT.md`, `releases/v3.1.20/README.md`, v3.1.20 Release Notes, v3.1.20 Baseline의 **main-side 설명**에 후보 반영했다.
- `docs-v3.1.20` Tag/Release Assets/SHA256SUMS는 변경하지 않는다.

## 6. v3.1.21 필수 이월 사항

`audit/canonical-followup-20260923/README.md`의 미반영 항목을 유지한다.

- `CURRENT.md`의 v3.1.20 현행 정본/인용 규칙 정정 — **후보 브랜치 반영 완료, 병합 대기**
- v3.1.20 중간 산출물 DOCX 정정본의 차기 정본 무결성 반영
- `releases/v3.1.20/README.md`·Release Notes·Baseline의 과거 CANDIDATE 문구를 역사 기록으로 명시 — **후보 브랜치 반영 완료, 병합 대기**
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
- v3.1.20 STATUS/CITATION CORRECTION: **APPLIED TO CANDIDATE BRANCH**
- FULL CANONICAL REGENERATION: **NOT RUN**
- RUNTIME/GATE REVALIDATION: **NOT RUN**
- REVIEW/MERGE/RELEASE: **NOT DONE**
