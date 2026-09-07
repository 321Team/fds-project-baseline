# Canonical Document Release Policy

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

## 5. Approval and traceability

- Review owners: `@GWONUK`, `@hayeounglee`
- The PR must record scope, changed artifacts, validation results, and known limitations.
- The approved candidate HEAD and its content-merge commit are recorded as review evidence.
- A version tag such as `docs-v3.1.17` fixes the finalization merge commit as the published canonical release point. This avoids recursive commits made only to record their own SHA.

## 6. GitHub Free Private Repository compensating control

GitHub Free에서 Private 저장소 Ruleset 또는 Branch Protection을 적용할 수 없으면 다음 보상 통제를 사용한다.

- 저장소를 Public으로 전환하지 않는다.
- 모든 변경은 release branch와 Pull Request로 제출한다.
- 최소 1인의 독립 Reviewer 승인을 기록한다.
- 승인 운영자가 검토 대상 Head Commit SHA와 SHA-256 검증 결과를 확인한 뒤 수동 Merge한다.
- 직접 `main` Push, 자동 Merge, CI 직후 자동 정본 배포를 금지한다.
- GitHub Actions 실행이 없으면 로컬 검증 결과만 기록하며 CI PASS로 오인 표시하지 않는다.
- Merge 후 `CURRENT.md`, Release 상태 및 Tag를 별도 finalization 변경으로 확정한다.

## 7. Large artifact and repository-size policy

- Markdown 정본과 검토·편집이 필요한 WBS/Gantt 원본은 Git에서 버전 관리한다.
- 배포용 ZIP은 정식 Release Tag 이후 GitHub Release Asset으로 제공하는 것을 기본으로 하며, 다음 버전부터 동일 ZIP을 Git 이력에 반복 추가하지 않는다.
- 현 저장소 이력은 재작성하지 않는다. 기존 v3.1.17 후보 ZIP은 해당 릴리즈의 감사 추적을 위해 유지한다.
- 단일 파일이 50 MiB에 접근하거나 저장소가 1 GiB에 접근하면 크기 점검을 수행하고 Release Asset 또는 Git LFS 전환을 결정한다.
- Git LFS는 실제 대용량 편집 원본이 발생하고 Free 사용량·대역폭 통제가 합의된 경우에만 도입한다.
