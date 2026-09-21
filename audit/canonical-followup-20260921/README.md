# PR #82 정본 무결성 실패 원인 및 §2.3 동기화 후보 — 2026-09-21

상태: **IN PROGRESS / REVIEW CANDIDATE**. 운영 정본은 RELEASED v3.1.19이며 이 디렉터리는 v3.1.19의 어떤 파일·태그·SHA256SUMS도 수정하지 않는다.

## 착수 근거

[PR #82](https://github.com/321Team/fds-project-baseline/pull/82)(`fix/canonical-ci-checkout-pin-20260918`)가 `actions/checkout@v4` SHA 고정으로 canonical-integrity의 시작 실패(startup_failure)는 해결했지만, `scripts/verify-canonical-release.sh`의 `sha256sum -c releases/v3.1.19/SHA256SUMS` 단계에서 4개 경로 불일치로 여전히 FAIL한다. 사용자가 원인 재점검과 §2.3에 따른 최소 동기화 PR 착수를 요청했다.

## 직접 수행한 검증

`checksum-drift.json`에 4개 파일 각각의 등록 해시(v3.1.19)·main 실제 해시·PR #82 브랜치 실제 해시를 기록했다. 방법과 범위는 `validation.json`을 따른다.

- **governance 문서 3건**(`GITHUB_IDENTITY_MAP.md`, `RELEASE_POLICY.md`, `TICKET_SYNC_POLICY.md`): main HEAD(`ba8a22f9adc25e52cf3e4d841f7e7357b5a79da1`) 자체가 이미 v3.1.19 SHA256SUMS와 불일치한다. PR #82는 이 3개 파일을 변경하지 않으므로 **이 PR의 책임이 아니다.**
- **`.github/workflows/canonical-integrity.yml`**: main에서는 SHA256SUMS와 일치하지만, PR #82의 1줄 변경이 이 파일 자체의 해시를 바꾸므로 **PR #82가 직접 유발한 항목이다.**
- canonical-integrity 워크플로는 main 브랜치에서 실행 이력이 0건이다. v3.1.19 발행 이후 이 검증이 main에서 실제로 통과한 적이 없으며, #80/#81 병합 커밋 메시지도 "CI startup_failure is recorded, not a CI PASS"라고 스스로 기록하고 있다.

## 이 후보가 제공하는 것

`checksum-drift.json`은 정본 Lead가 차기 정본 후보(예: v3.1.20)를 공식 발행할 때 `releases/vX.Y.Z/SHA256SUMS`·Distribution Manifest에 반영할 4개 파일의 현재 실제 SHA-256/Git blob 값이다. RELEASE_POLICY §2.3(완료 변경 요청의 정본 동기화)이 요구하는 동기화 대상 중 SHA256SUMS 항목에 한정된다.

## 이 후보가 수행하지 않는 것

- `releases/v3.1.19/SHA256SUMS`, CURRENT.md, Tag, GitHub Release Asset을 수정하지 않는다.
- WBS/Gantt, Ticket Pack, Distribution Manifest, Release Notes 등 §2 필수 산출물 10종의 정식 갱신·차기 버전 태깅을 수행하지 않는다 — 사용자가 선택한 범위는 "최소 동기화"이며 정식 릴리스 절차는 별도 결정 사항이다.
- PR #82의 병합 여부를 결정하지 않는다. PR #82는 이 기록과 무관하게 정본 Lead·독립 리뷰어(hayeounglee, 이미 APPROVED)의 별도 판단을 따른다.
- canonical-integrity 워크플로를 재실행하거나 CI 상태를 변경하지 않는다.

## 남은 조치 (Lead 결정 필요)

1. 차기 정본 후보를 언제 공식적으로 컷할지 결정 — 그 시점에 `checksum-drift.json`의 4개 값(및 PR #82 병합 시 `.github/workflows/canonical-integrity.yml`의 PR #82 head 해시)을 새 SHA256SUMS/Manifest에 반영한다.
2. PR #82는 governance 문서 3건 drift가 자신과 무관함을 이미 리뷰 코멘트에 기록했지만, 워크플로 파일 자체의 자기 유발 drift는 별도로 언급되지 않았다 — 병합 전 이 사실을 PR에 코멘트로 남기는 것을 권장한다.
3. canonical-integrity가 main에서 한 번도 성공하지 못한 근본 원인(발행 후 정본 동기화 누락)에 대한 재발 방지책은 이 기록의 범위 밖이며 별도 논의가 필요하다.

## 관련

- [PR #82](https://github.com/321Team/fds-project-baseline/pull/82)
- 실패 Run: [35293408375](https://github.com/321Team/fds-project-baseline/actions/runs/35293408375) / Job 105440900284
- `governance/RELEASE_POLICY.md` §2.3, §4, §6
