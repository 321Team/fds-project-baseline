# D37 — GitHub Canonical Baseline Repository and v3.1.17 Release Record

> Version: v1.0  
> Decision date: 2026-09-04  
> Decision owner: 이권욱  
> Repository: `321Team/fds-project-baseline` (Private)  
> Decision status: USER APPROVED  
> Release status: READY FOR REVIEW

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
- GitHub `main` 보호 Ruleset 활성화 및 검증
- Draft PR 승인 후 v3.1.17 `RELEASED` 승격

**D37_DECISION_VERDICT=USER_APPROVED_RELEASE_PENDING**
