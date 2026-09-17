# v3.1.19 릴리즈 최종화 기록

FINALIZATION REVIEW PENDING · 내용 승인/병합 완료 · Tag/Release/Asset 게시 미완료.

| 항목 | 기록 |
|---|---|
| 내용 PR | [#73](https://github.com/321Team/fds-project-baseline/pull/73) |
| 독립 Reviewer | 이하영 (`hayeounglee`) |
| 승인 대상 HEAD | `ce3f0c9704dc8316c078c0c427928a97b08e4408` |
| 승인 시각 | 2026-09-17T22:51:49Z / 2026-09-18 07:51:49 KST |
| 승인 기록 | [Review 5242201621](https://github.com/321Team/fds-project-baseline/pull/73#pullrequestreview-5242201621) |
| 내용 병합 | `f759d2d72cd4f943b19cbb3b46952f75ed0b8b09` |
| 내용 병합 시각 | 2026-09-17T23:21:13Z / 2026-09-18 08:21:13 KST |
| 인라인 리뷰 | 0건 |
| 내용 CI | startup_failure 2건; CI PASS 아님 |
| 승인 후보 ZIP SHA256 | `579d7e18d976fdee119213ad6d5327d36276c53d7e6cae1e8644939f0a3aeb18` |
| 최종화 승인·병합 | 대기 — 새 HEAD 독립 승인 필요 |
| Tag | docs-v3.1.19, 최종화 병합 commit에 고정 |
| GitHub Publish/Asset 검증 | NOT EXECUTED |

## 변경 범위

CURRENT, 배포 문서 머리말, WBS의 배포 표기, 승인·병합 이력, Manifest·체크섬을 최종화한다. RELEASED 표기는 이 최종화 PR의 독립 승인·병합 후 적용할 메타데이터이며 GitHub 게시 성공을 뜻하지 않는다.

67개 티켓의 속성·일정·담당·AC, 58개 WBS 레코드의 데이터·수식·가용일과 차트는 변경하지 않는다. 각 Description·원문·intake·과거 검증 및 통합 기록의 CANDIDATE/PENDING/이전 정본 문구는 승인된 스냅샷 당시 기록으로 보존한다. WBS Source Note의 당시 문구도 같은 원칙이다.

검증: `audit/v3.1.19/finalization-validation.json`. 최종 ZIP은 갱신된 SHA256SUMS로 재생성하며 위 내용 후보 ZIP을 최종화 ZIP으로 재사용하지 않는다.

## 게시 절차

1. 최종화 HEAD 독립 승인과 미해결 차단 여부 확인 후 수동 병합한다.
2. 최종화 merge SHA에 docs-v3.1.19 Tag를 고정한다. 기존 태그 강제 이동 금지.
3. 그 Tag에서 `python3 scripts/build-canonical-package.py v3.1.19 /tmp/fds-v19-release` 실행.
4. `RELEASE_VERSION=v3.1.19 FDS_RELEASE_ZIP=/tmp/fds-v19-release/FDS_v3.1.19_Canonical_Baseline_Release_Package.zip bash scripts/verify-canonical-release.sh` 통과 확인.
5. Draft Release에 ZIP·sidecar·SHA256SUMS·WBS의 4개 Asset 업로드. `scripts/publish-canonical-release-assets.sh`와 `scripts/verify-wbs-gantt-distribution.sh v3.1.19 --published`로 실제 다운로드 바이트 확인.
6. Publish 후 published_at·Tag commit·4개 Asset digest 및 다운로드 검증 결과를 PR에 기록한다. 이전 v18 Tag/Release/Asset은 보존한다.

연결된 GitHub 도구는 현재 Release/Tag 생성·바이너리 Asset 업로드 API를 제공하지 않는다. 승인된 운영 환경의 GitHub CLI 또는 지원되는 인증된 UI가 필요하다. 이번 기록은 실제 게시 완료를 주장하지 않는다.

## 유지되는 잔여

NTP upstream/time authority, K8S 6/6·etcd·Storage·host 보호, Harbor/SEC 인수, 실제 앱 Test/Build/Scan/Push/Deploy 및 G1/G2는 원래의 Runtime/승인 상태로 유지한다. 문서 발행으로 작업 완료·AC를 변경하지 않는다.
