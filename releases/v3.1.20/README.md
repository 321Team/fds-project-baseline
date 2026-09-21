# v3.1.20 — CANDIDATE / COLLECTING (정식 발행 보류)

상태: **CANDIDATE / COLLECTING**. 운영 정본은 여전히 **RELEASED v3.1.19**(`releases/v3.1.19/`, Tag `docs-v3.1.19`)이다. 이 디렉터리는 아직 완성된 릴리스가 아니며, `SHA256SUMS`·Distribution Manifest·Release Notes 등 RELEASE_POLICY §2의 필수 산출물을 포함하지 않는다. Tag 생성·GitHub Release 발행은 수행하지 않았고 수행하지 않는다.

## 목적

이 브랜치는 v3.1.19 이후 발생하는 governance/tooling/티켓 변경분을 **정식 v3.1.20 발행 시점까지 모아두는 후보 수집 지점**이다. RELEASE_POLICY §2.3(완료 변경 요청의 정본 동기화) 대상이 쌓이면 이 브랜치 위에 반영하고, 정본 Lead가 실제 발행을 결정할 때 §2의 10개 필수 산출물(Baseline, WBS/Gantt, Ticket Pack, Release Notes, Manifest, SHA256SUMS, Architecture, Integrity Audit, ZIP, WEB 스냅샷)을 갖춰 완성한다.

## 2026-09-21 전수 감사 기준선 (착수 시점 스냅샷)

PR #86(`audit/canonical-followup-20260921/`)에서 수행한 전수 감사 결과:

- v3.1.19 태그(`966fc5365874b1d259a9810fc876b57c3bfa0e08`, 2026-09-17 23:53:12Z) 이후 **종결된 GitHub Issue 0건**, **`status:done` 라벨을 가진 Open Issue 0건** — WBS/Ticket Pack/Baseline/Architecture 동기화 대상 없음.
- 실제 변경분은 governance/tooling 파일 한정:
  - `governance/GITHUB_IDENTITY_MAP.md`, `RELEASE_POLICY.md`, `TICKET_SYNC_POLICY.md` — 수정 (PR #80, #81)
  - `governance/REVIEW_AUTHORITY_POLICY.md` — 신규 (PR #80, #81에서 수정)
  - `.github/workflows/pr-review.yml` — 신규
  - `README.md` — 수정 (PR #80, #81, #84); v3.1.19 SHA256SUMS에 미등재라 체크섬 영향 없음
  - `.github/workflows/canonical-integrity.yml` — [PR #82](https://github.com/321Team/fds-project-baseline/pull/82) 병합 시 추가 drift 예정 (미병합)
- 각 파일의 등록 해시 대 현재 해시 비교는 `audit/canonical-followup-20260921/checksum-drift.json`(PR #86)을 기준으로 한다.

## 이 커밋이 수행하지 않는 것

- v3.1.19의 어떤 파일·Tag·SHA256SUMS·GitHub Release도 수정하지 않는다.
- WBS/Gantt·Ticket Pack·Baseline·Architecture 문서를 새로 만들거나 복사하지 않는다 (변경 사유가 없음).
- git tag 생성, GitHub Release 발행, Asset 업로드를 수행하지 않는다 — RELEASE_POLICY §6에 따라 "권한 있는 운영자"의 별도 결정·실행 사항이다.

## 다음 조치 (Lead 결정 필요)

1. 이 브랜치를 유지하며 후속 governance/티켓 변경이 쌓이는지 관찰한다.
2. 실제 발행이 필요하다고 판단되는 시점에 §2 필수 산출물을 준비하고 이 PR을 갱신한다.
3. 그 전까지는 **Draft 상태를 유지**하며 병합·Tag·발행을 하지 않는다.
