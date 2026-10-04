# Current Canonical Release

이 문서는 실제 게시된 운영 정본의 포인터다. v3.1.21 후보 수집·검토 상태는 운영 정본의 발행 상태와 별도로 관리한다. GitHub 게시 사실은 아래 Release API로 확인한다.

| Field | Value |
|---|---|
| Repository status | ACTIVE / CANONICAL |
| Canonical document version | v3.1.20 / PUBLISHED (verified Release API) |
| History path | `releases/v3.1.20/` |
| Approved content HEAD | `9fa13f8e99da43d668a4ed38218e69ab55b6db75` |
| Content merge | `336446500ef9a71c4796e6cfc8bc4db18daceb09` |
| Reviewer | 이재환 (`supreme33-kr`), REVIEW_AUTHORITY_POLICY상 문서/최종화 전용 PR — Lead 검토·결정, APPROVED 3회 |
| Content approval (KST) | 2026-09-23 02:15:33 +09:00 |
| Content merge (KST) | 2026-09-23 02:18:11 +09:00 |
| Canonical release tag | `docs-v3.1.20` — finalization merge commit |
| GitHub publication | Verified via Release API — `published_at` 2026-09-22T17:37:13Z |
| Published timestamp | 2026-09-23 02:37:13 +09:00 (Release API `published_at`) |

## Publication evidence

- [v20 Release](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.20) / [Release API](https://api.github.com/repos/321Team/fds-project-baseline/releases/tags/docs-v3.1.20).
- [PR #87](https://github.com/321Team/fds-project-baseline/pull/87) / [Content merge](https://github.com/321Team/fds-project-baseline/commit/336446500ef9a71c4796e6cfc8bc4db18daceb09).
- WBS/Gantt 배포 통제(§2.1) 5곳 전부 확인: 저장소 원본·Manifest·`SHA256SUMS`·ZIP 내부·GitHub Release Asset 모두 SHA-256 `e0b324161d07b0d46db93065d9c3334c36459d0d84b2b7c4e81ff6799e210479` 동일. Release Asset은 GitHub이 업로드 시점에 계산해 API로 보고하는 `digest` 필드로 대조했다(리포지토리 비공개로 인해 비인증 재다운로드가 차단되어, 로컬 재다운로드 방식 대신 사용).
- Distribution ZIP(`FDS_v3.1.20_Canonical_Baseline_Release_Package.zip`) SHA-256 `9a1044d5c84273ca54ecdf577395c1c45d4813b18a26a1192e68dac4305230d4` — 로컬 생성 sidecar와 GitHub Release Asset digest 일치 확인.
- `git tag docs-v3.1.20`와 GitHub Release 생성·Asset 4종 업로드는 이 세션의 git/GitHub 도구 권한 밖(HTTP 403, Release 쓰기 API 미제공)이라 정본 Lead가 GitHub 웹 UI에서 직접 수행했다.

## Last verified publication at finalization preparation

v3.1.19 was published on **2026-09-18 09:20:13 KST**, tag `docs-v3.1.19`, target `966fc5365874b1d259a9810fc876b57c3bfa0e08`, four Assets. [Release](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.19).

v3.1.20 is now the operational publication; v3.1.19 becomes the previous preserved release. Its Tag/Release/Assets are unmodified and remain accessible at the link above.

## Scope

RELEASED in document headings means approved content plus reviewed finalization on main and matching checksums. It does not imply that GitHub Publish, operational Runtime, AC or Gate acceptance has occurred. v3.1.20 carries forward Baseline/WBS/Ticket Pack with real edits limited to governance/CI fixes (PR #82/#86/#88/#89) and the Phase 2 schedule replan (Lead decision, 2026-09-22); Architecture is unchanged from v3.1.19 (no revision reason this cycle, §2 item 7 conditional requirement). Snapshot-time candidate wording in retained source/Description/audit inputs remains historical. Planning dates remain adjustable targets.

## 2026-10-03 current status clarification (candidate correction)

- `docs-v3.1.20`: Release API draft=false, published_at=2026-09-22T17:37:13Z (2026-09-23 02:37:13 KST), 실제 PUBLISHED. Release text의 CANDIDATE/COLLECTING/정식 발행 보류는 당시 snapshot 문구다. 기존 tag/assets/release byte를 소급 수정하지 않는다.
- `v3.1.21`: baseline PR #112 CANDIDATE/COLLECTING/NOT_PUBLISHED. 이 포인터 후보 수정은 v3.1.21 release 발행이 아니다.
- Phase 2 current delta: [R/I/T/P follow-up](https://github.com/321Team/fds-project-baseline/blob/release/v3.1.21/audit/phase2-ritp-followup-20261003/README.md), [architecture candidate PR #8](https://github.com/321Team/fds-project-architecture/pull/8). D21 FINAL과 full Architecture Freeze HOLD를 구분한다.
- Apply/Runtime/Gate acceptance는 document publication 상태와 별개다. AI 사용: CODEX_ASSISTED.
