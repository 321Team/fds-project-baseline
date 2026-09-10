# FDS v3.1.18 릴리즈 최종화 기록

> FINALIZATION REVIEW PENDING · 내용 승인/병합 완료 · Tag/Release/Asset 게시 미완료

## 승인된 내용

| 항목 | 기록 |
|---|---|
| 내용 PR | [#69](https://github.com/321Team/fds-project-baseline/pull/69) |
| 승인 Reviewer | 이하영 (`hayeounglee`) |
| 승인 대상 HEAD | `04c1ca46dcf82f814d350b4d49539e3ba4d6a9b4` |
| 승인 시각 | 2026-09-10T14:20:47Z |
| 승인 기록 | [Review 5168287548](https://github.com/321Team/fds-project-baseline/pull/69#pullrequestreview-5168287548) |
| 내용 병합 | `02be2150f7662319a3d796cdcb99f6d26aec5472` |
| 내용 병합 시각 | 2026-09-10T14:38:32Z |
| 리뷰 스레드 | 0 |
| GitHub Actions / Commit Status | 실행 0건 / NOT RUN |
| 승인 후보 ZIP SHA-256 | `479db7f5e34306931c7dd13093ba316bf11cab0442316dc54fee86fcaecf9fab` |
| 이 최종화 변경 | 독립 리뷰·병합 대기 |
| 정식 Tag | `docs-v3.1.18` 생성 대기 — 최종화 병합 커밋에 고정 |
| GitHub Release / Assets | 미게시 |
| 게시 후 검증 | NOT RUN |

## 최종화 변경의 효력

이 PR의 `RELEASED / FINALIZATION` 및 CURRENT 값은 독립 승인·수동 병합 후 적용할 문서 메타데이터다. 이 PR이 열린 동안 main/CURRENT는 v3.1.17을 유지한다. GitHub 게시 완료는 Tag와 4개 배포 Asset의 일치 검증 이후 별도로 판정한다. 발행 시각은 GitHub Release의 실제 published_at을 사용한다.

승인된 사양·티켓 64건의 속성·일정·담당·AC, WBS 55건의 값·수식·차트 및 계획 배정은 바꾸지 않는다. WBS의 현 버전 머리말 10셀과 문서 배포 상태·승인 이력·체크섬만 최종화한다. `audit/v3.1.18/finalization-validation.json`에 비교 결과를 기록한다.

`canonical-records.json`, 64개 Description, 원본 Issue/후속 증적·후보 감사·통합 기록·계획 권장안은 승인된 후보 시점의 원문 또는 Issue 적용 입력이다. 이 파일들의 CANDIDATE/미발행/이전 운영 정본 문구는 해당 작성 시점의 기록으로 보존한다. 전체 배포 상태는 CURRENT, Baseline 머리말, 이 기록과 GitHub Release를 따른다. 실제 Issue 적용 전에 최신 운영 delta를 대조해야 한다.

## 인계 및 미결 사항

- PR #3의 커밋·배포 통제·09-08 휴가·DNS CR 완료를 #69가 인수했고, [종결 이력](https://github.com/321Team/fds-project-baseline/pull/3#issuecomment-5619977212)을 보존한다.
- 3CP+3Worker 총 6대·kubeadm·Calico·static local PV 구조를 유지한다. 리뷰어 댓글의 “Worker 6대”를 노드 증설 결정으로 해석하지 않는다.
- NTP 목적지·운영 주체·수치 기준, 최소 egress·MTU 실측, CP2 잔존 상태, 6/6 Ready·etcd 3 Member·DNS/cross-node·host 보호·Storage·재부팅/복구 및 Runtime/Permanent 전환은 기존 잔여로 유지한다.
- CA/CI-CD 및 외부 Monitoring·Notification 설계는 #69 본문의 별도 편입 입력이다. 이번 릴리즈 내용으로 통합 완료한 사실이 아니며, 후속 내용 변경 PR에서 추적한다. 이 제외를 프로젝트 전체 Scope Out 또는 취소로 해석하지 않는다.
- 내용 승인 및 문서 릴리즈는 Runtime 실행·인수·AC·Done을 추가로 승인하지 않는다.

## 게시 절차

1. 이 최종화 PR의 정확한 HEAD를 독립 Reviewer가 승인하고 승인 운영자가 수동 병합한다. 정책 §5~6과 이전 v3.1.17 최종화 PR #2의 절차를 유지한다.
2. 승인된 최종화 병합 커밋에 `docs-v3.1.18` Tag를 생성하고 GitHub Release 초안을 만든다. [게시 본문 초안](FDS_GitHub_Release_Body_v3.1.18.md)을 사용한다.
3. 해당 Tag의 파일로 아래 명령을 실행하여 ZIP/Sidecar를 재생성하고 검증한다. 내용 후보 ZIP을 최종화 ZIP으로 재사용하지 않는다.
4. ZIP, ZIP.sha256, SHA256SUMS, 독립 XLSX를 Release Asset으로 한 묶음 업로드한다. 기존 v3.1.17 Asset은 건드리지 않는다.
5. `--published` 검증 PASS를 확인하고 Release를 게시한다. 게시 후 같은 검증을 다시 확인하며 Actions 미실행은 NOT RUN으로 유지한다.

```bash
python3 scripts/build-canonical-package.py v3.1.18 /tmp/fds-v18-release
FDS_RELEASE_ZIP=/tmp/fds-v18-release/FDS_v3.1.18_Canonical_Baseline_Release_Package.zip RELEASE_VERSION=v3.1.18 bash scripts/verify-canonical-release.sh
bash scripts/publish-canonical-release-assets.sh v3.1.18 /tmp/fds-v18-release/FDS_v3.1.18_Canonical_Baseline_Release_Package.zip
bash scripts/verify-wbs-gantt-distribution.sh v3.1.18 --published
```

현재 연결은 PR/커밋 조작을 지원하지만 Release 생성·Tag 생성·Asset 업로드는 제공하지 않는다. 따라서 이 작성 작업은 실제 GitHub Release 게시 성공을 주장하지 않는다. 승인된 운영 환경에서 위 단계와 실제 최종화 SHA를 사용해야 한다.
