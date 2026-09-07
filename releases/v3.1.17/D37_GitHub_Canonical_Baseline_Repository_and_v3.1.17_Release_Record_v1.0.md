# D37 — GitHub Canonical Baseline Repository and v3.1.17 Release Record

> Version: v1.0  
> Decision date: 2026-09-04  
> Decision owner: 이권욱  
> Repository: `321Team/fds-project-baseline` (Private)  
> Decision status: USER APPROVED  
> Release status: RELEASED — 2026-09-07

## Decision

개발 코드 저장소와 분리된 Private 저장소에서 Baseline, WBS/Gantt, Ticket Update Pack, Release Notes, Manifest, Audit, WEB Snapshot 및 이전 릴리즈 이력을 관리한다.

- `main`: 승인된 정본만 유지한다.
- `release/v3.1.17`: v3.1.17 검토 후보를 유지한다.
- 모든 정본 변경은 Pull Request와 CODEOWNERS 검토를 거친다.
- 배포 묶음에는 SHA-256 목록과 ZIP sidecar hash를 포함한다.
- 과거 RELEASED 파일은 동일 경로에서 덮어쓰지 않고 버전별 디렉터리에 보존한다.
- 설계 승인, 문서 발행, 코드 Merge, Runtime PASS는 서로 다른 상태로 기록한다.

## Integrity corrections

| Control | v3.1.17 disposition |
|---|---|
| v3.1.15 / D35 history | `releases/v3.1.15/`에 원본 바이트 보존 |
| v3.1.16 / D36 history | `releases/v3.1.16/`에 원본 바이트 보존 |
| 담당자 영문 표기 | `KW LEE`→`GU LEE`, `KW/HY LEE`→`GU/HY LEE` |
| P1-K8S Source | `FDS_P1-K8S-01_Preflight_Review_v1.1`로 정정 |
| ICR Source | ICR v1.4와 Baseline v3.1.17로 정정 |
| P1-LB Stage B | D36 G1 목표와 정렬하여 Plan End 2026-09-07; Runtime Pending 유지 |
| WEB 산출물 | 정적 검토 Snapshot을 v3.1.17 배포 묶음에 포함 |
| CR-P1-ANS-01-01 | `In Review`; PR #1 Review/CI/Merge 미완료를 명시 |

## Open controls

- OID-02 Control Plane/System Image Registry 결정
- OID-03 Bootstrap Package/Registry Egress 결정
- `CR-P1-ANS-01-01` Reviewer 승인, CI, Merge 및 필요한 Runtime Evidence
- v3.1.17 finalization PR 승인·Merge 후 `docs-v3.1.17` Tag 및 GitHub Release 발행

## GitHub Free compensating control — 2026-09-05 approved

Private 저장소를 유지하며 유료 플랜이 필요한 Ruleset은 적용 대상에서 제외한다. Public 전환은 금지한다.

- 모든 변경은 `release/vX.Y.Z` Branch와 Pull Request를 사용한다.
- `main` 직접 Push 금지는 절차 통제로 유지한다.
- 최소 1인의 독립 Reviewer 승인을 받은 뒤 승인 운영자가 수동 Merge한다.
- PR에 대상 Head Commit SHA, 검증 결과, Reviewer, 승인 결과를 기록한다.
- GitHub Actions가 실행되지 않으면 로컬 SHA-256·Workbook QA·민감정보 검사 PASS를 PR Evidence로 보존하되, CI PASS로 표현하지 않는다.
- 자동 Merge와 자동 정본 배포는 사용하지 않는다.

## Release evidence — 2026-09-07

- Pull Request: `#1`
- Approved reviewer: `hayeounglee`
- Approved candidate HEAD: `53ea99cc904a411f64b95d0e61fcef8533c5f6a7`
- Merge commit: `8515ecd97e69035f329032ba17206972c7b0739d`
- Review threads: `0`
- GitHub Actions: `NOT RUN`; CI PASS 미선언
- Compensating evidence: Local artifact integrity, Workbook QA, Secret-pattern scan, ZIP/Sidecar verification `PASS`

**D37_DECISION_VERDICT=APPROVED_AND_RELEASED_FINALIZATION_IN_PROGRESS**
