# Canonical Document Release Policy

2026-09-18 승인 절차 개정: [코드 병합 독립 리뷰와 Lead 위임 정책](REVIEW_AUTHORITY_POLICY.md)을 적용한다. 독립 리뷰는 코드/혼합 PR 병합에 한정하며, 문서만 변경한 PR·최종화·발행은 정본 Lead가 검토·결정한다.

## 1. Branch model

- `main`: approved canonical documents only.
- `release/vX.Y.Z`: one controlled release candidate.
- Direct updates to `main` are prohibited.
- Each release candidate must be merged through a reviewed pull request.

## 2. Required release set

Every canonical version must contain all applicable items:

1. Project Implementation Baseline
2. WBS and Gantt workbook
3. Canonical Ticket Update Pack
4. Release Notes
5. Distribution Manifest
6. `SHA256SUMS`
7. Architecture source/export set when changed
8. Integrity audit result
9. Distribution ZIP and ZIP sidecar checksum when produced
10. WEB canonical status snapshot (required for every canonical release)

### 2.1 WBS/Gantt mandatory distribution control

- WBS/Gantt 내용의 변경 유무와 관계없이 모든 정본 버전에 해당 버전의 편집 가능한 `.xlsx` 원본을 반드시 배포한다.
- 같은 WBS/Gantt 파일을 다음 다섯 위치에서 동일한 경로·파일명·SHA-256으로 식별할 수 있어야 한다.
  1. 저장소 `wbs/` 경로
  2. Distribution Manifest
  3. `releases/vX.Y.Z/SHA256SUMS`
  4. 정본 배포 ZIP 내부
  5. GitHub Release의 독립 다운로드 Asset
- ZIP 안에만 포함되거나 GitHub Release Asset에만 존재하는 상태는 완전한 배포로 인정하지 않는다.
- 독립 Release Asset의 파일명과 SHA-256이 저장소 원본·ZIP 내부 파일과 다르면 발행을 중단한다.
- GitHub Release Asset은 Tag가 확정된 뒤 업로드하고, `scripts/verify-wbs-gantt-distribution.sh vX.Y.Z --published` 결과가 PASS일 때만 발행 완료로 판정한다.
- Asset 업로드는 `scripts/publish-canonical-release-assets.sh vX.Y.Z <ZIP 경로>`를 사용해 ZIP·Sidecar·`SHA256SUMS`·WBS/Gantt를 한 묶음으로 처리한다. 최종 `Publish release` 판단과 실행은 승인 운영자가 수행한다.
- GitHub Release가 발행되면 `canonical-integrity` Workflow가 `--published` 검증을 자동 실행한다. Actions가 실행되지 않거나 사용량 제한으로 중단되면 결과를 `NOT RUN`으로 기록하고 동일 스크립트의 로컬 PASS를 보상 증적으로 남긴다.
- v3.1.17은 WBS/Gantt가 저장소와 ZIP 내부에는 포함됐으나 독립 Release Asset으로는 제공되지 않았던 이력으로 보존한다. 과거 Tag나 Release Asset을 소급 변경하지 않고 v3.1.18부터 본 통제를 적용한다.

### 2.2 WEB 배포 통제

- 모든 정본 버전에 같은 기준선의 WEB 상태 스냅샷을 포함한다.
- WEB 파일은 저장소, Distribution Manifest, SHA256SUMS 및 정본 ZIP에서 식별하고 같은 바이트인지 검증한다.
- WEB은 기준일·RELEASED 버전·계획 목표·실제 상태를 구분하며 단독 갱신을 새 정본 발행으로 해석하지 않는다.
- 현재 v3.1.18 WEB은 기존 Tag/ZIP으로 보존하고 이 정책은 차기 정본 배포 검증에 반영한다.

### 2.3 완료 변경 요청의 정본 동기화

- 직전 RELEASED 버전 이후 `Done` 또는 `Merged`로 승인된 모든 Change Request는 다음 정본 후보에 반드시 동기화한다.
- 동기화 대상은 Baseline, WBS/Gantt, Canonical Ticket Pack, `tickets/<Record-ID>_Notion_Description_*.md`, Milestone/Completion Record, Evidence 참조, Release Notes 및 적용되는 Manifest·`SHA256SUMS`이다.
- Record ID, 상태, 담당자, 일정, Acceptance Criteria, 승인된 Head Commit, Merge Commit, CI/Runtime Evidence 상태가 산출물 사이에서 일치해야 한다.
- GitHub Actions가 실행되지 않은 경우 `NOT RUN`으로 명시하며 CI PASS로 대체하거나 확대 해석하지 않는다.
- 변경 요청 완료는 별도 티켓·ICR·Milestone·Runtime Gate를 자동 완료하거나 승인하지 않는다.
- 완료 변경 요청이 누락되거나 상호 상태가 불일치하면 정본 병합과 Release 발행을 중단한다.

## 3. Version and status rules

- `CANDIDATE`: exists only on a release branch and is not canonical.
- `RELEASED`: approved, merged to `main`, and checksum verified.
- `SUPERSEDED`: retained without modification after a newer release.
- File names, internal version labels, manifest entries, and `CURRENT.md` must agree.

## 4. Review gates

A release must not be merged when any of the following remains unresolved:

- Baseline, WBS/Gantt, ticket, milestone, owner, or date mismatch
- Missing required artifact or checksum
- Formula or workbook integrity error
- Unresolved review thread
- Secret, token, private key, password, or unmasked credential exposure
- Runtime evidence represented as complete when only design approval exists
- WBS/Gantt가 ZIP과 독립 GitHub Release Asset 중 어느 한쪽에서 누락되거나 SHA-256이 불일치함

### 4.1 일정 유연성과 사실관계

2026-09-11 사용자 지시에 따라 점검표 및 WBS/Gantt의 날짜는 필수 준수 기한이 아닌 조정 가능한 계획 목표로 관리한다.

- 일정 변경·목표 미달 자체는 문서 승인 차단 또는 Runtime FAIL의 근거가 아니다.
- 가용성·선행 작업·인계 상황에 따라 계획을 조정하고 Baseline·WBS/Gantt·티켓의 현행 값과 변경 근거를 일치시킨다.
- 계획일과 실제 착수·완료일을 구분한다. 실제 날짜·기간의 모순은 원본 근거로 확인한다.
- 대표 Milestone은 추적 목적에 따라 확정하거나 근거 있는 의도적 미배정으로 처리한다. 미확정 값을 승인 없이 N/A로 바꾸지 않는다.
- Gate의 실제 선행조건·검증·증적·인수 요건은 일정 유연성과 별도로 충족해야 한다.

## 5. Approval and traceability

- 정본 Lead는 기존 배정을 유지한다. 코드 변경 Reviewer 경로는 `@GWONUK`, `@hayeounglee`를 유지하되 작성자 자신의 독립 승인은 인정하지 않는다.
- 문서 전용 PR은 Lead가 직접 검토·병합할 수 있다. 독립 리뷰가 불필요해도 정확한 HEAD, 필수 산출물·무결성 확인과 결정 기록은 유지한다.
- The PR must record scope, changed artifacts, validation results, and known limitations.
- The approved candidate HEAD and its content-merge commit are recorded as review evidence.
- A version tag such as `docs-v3.1.17` fixes the finalization merge commit as the published canonical release point. This avoids recursive commits made only to record their own SHA.

## 6. GitHub Free Private Repository compensating control

GitHub Free에서 Private 저장소 Ruleset 또는 Branch Protection을 적용할 수 없으면 다음 보상 통제를 사용한다.

- 저장소를 Public으로 전환하지 않는다.
- 정본 후보는 release branch와 Pull Request로 제출한다. 운영 정책만 변경하는 경우 별도 docs branch의 PR을 사용할 수 있으며 main 직접 Push는 금지한다.
- 코드/실행 설정 변경을 포함한 PR에만 최소 1인의 작성자 외 독립 Reviewer 검토·승인을 기록한다. 문서 전용 PR은 Lead의 검토·결정 기록으로 처리한다.
- 정본 Lead가 검토 대상 Head Commit SHA와 SHA-256 검증 결과를 확인한 뒤 권한 있는 운영자가 수동 Merge한다. 같은 문서의 최종화·Tag·발행에 독립 승인을 반복 요구하지 않는다.
- 직접 `main` Push, 자동 Merge, CI 직후 자동 정본 배포를 금지한다.
- GitHub Actions 실행이 없으면 로컬 검증 결과만 기록하며 CI PASS로 오인 표시하지 않는다.
- Merge 후 `CURRENT.md`, Release 상태 및 Tag를 별도 finalization 변경으로 확정한다.

## 7. Large artifact and repository-size policy

- Markdown 정본과 검토·편집이 필요한 WBS/Gantt 원본은 Git에서 버전 관리한다.
- 배포용 ZIP은 정식 Release Tag 이후 GitHub Release Asset으로 제공하는 것을 기본으로 하며, 다음 버전부터 동일 ZIP을 Git 이력에 반복 추가하지 않는다.
- 현 저장소 이력은 재작성하지 않는다. 기존 v3.1.17 후보 ZIP은 해당 릴리즈의 감사 추적을 위해 유지한다.
- 단일 파일이 50 MiB에 접근하거나 저장소가 1 GiB에 접근하면 크기 점검을 수행하고 Release Asset 또는 Git LFS 전환을 결정한다.
- Git LFS는 실제 대용량 편집 원본이 발생하고 Free 사용량·대역폭 통제가 합의된 경우에만 도입한다.
