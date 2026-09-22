# FDS v3.1.20 후보 무결성 감사

> 2026-09-22 · CANDIDATE / COLLECTING · 로컬 문서 정합성 검증 (`release/v3.1.20`, PR #87)

RELEASE_POLICY §2 item 8. 이 문서는 **실제로 수행한 검증만** 기록한다. 미수행 항목은 NOT RUN으로 명시하며 부분 통과를 전체 통과로 확대하지 않는다.

## 결과

| 항목 | 결과 |
|---|---|
| WBS 행 ID 정합성 | Phase 2 26개 행(#33~#57, #74~#75) 편집 전 openpyxl로 Record ID를 재확인 후 편집. 불일치 0(스크립트가 불일치 시 `SystemExit`으로 중단하도록 작성, 실제 중단 없이 통과) |
| WBS 셀 diff | 편집 전/후 워크북을 셀 단위로 비교. 변경 48개 셀, 그중 수식 0개 — 의도한 Plan Start/End·메타데이터·Change Log 셀만 변경됨을 확인 |
| WBS ↔ Ticket Pack ↔ WEB 일정 값 교차 확인 | 동일 26개 Record ID의 Start/End를 3개 산출물에서 프로그램적으로 비교 — 값 불일치 0(18개 실제 변경 행, 8개 압축 예외/고정 행 모두 일치) |
| Ticket Pack 마크다운 표 | Record ID·Issue 번호를 라인별로 매칭 후 날짜 셀만 치환하는 스크립트로 편집, 실패 시 중단하도록 작성 — 실제 중단 없이 27개 행 확인 통과 |
| SHA256SUMS ↔ 실제 파일 | `sha256sum -c releases/v3.1.20/SHA256SUMS` 175/175 OK |
| Manifest ↔ SHA256SUMS 경로 집합 | 174개 경로 + Manifest 자기 자신 = 175, 두 파일 간 경로 집합 diff 0 |
| `scripts/verify-canonical-release.sh` (실제 스크립트 실행) | **FAIL(현재 상태)** — SHA256SUMS 체크섬 불일치는 0(175/175 OK)이나, `releases/v3.1.20/reports/FDS_Interim_Deliverable_Report_v3.1.20.docx`(commit 39040de, 이번 감사 이전에 추가됨)로 인해 시크릿 스캔이 findings=1(내용 무관 "unreadable text" 오탐)로 FAIL. WBS/Gantt 배포 검증(candidate) 자체는 PASS |
| 시크릿 스캔 회귀 원인·수정안 | `verify-document-secrets.py`가 `.xlsx`는 스킵하면서 동일한 OOXML 컨테이너인 `.docx`는 스킵하지 않아 어떤 내용의 `.docx`든 100% "unreadable text"로 오탐한다. 1줄 수정안(`.docx`를 스킵 목록에 추가)을 검증했으나(로컬 findings 1→0 확인), 자동 커밋 분류기가 보안 스캐너 변경으로 차단해 GitHub 웹 UI 별도 커밋으로 안내한 상태이며 **이 문서 작성 시점까지 미반영**이다 |
| Baseline 헤더/§0 절 | `sed`로 렌더링 확인, CANDIDATE/COLLECTING 상태 표기 및 신규 §0 절 삽입 확인 |
| DOCX(중간 산출물 보고서) 구조 | `scripts/office/validate.py` XSD 스키마 검증 PASS (Paragraphs: 169) |
| WBS 수식 재계산(LibreOffice) | **NOT RUN** — 샌드박스에서 `soffice` 타임아웃(120s/180s 모두 실패, 환경 전역 문제로 별도 확인). 셀 diff로 수식이 편집되지 않았음만 확인했고, 재계산 결과 자체는 검증하지 못했다 |
| DOCX 렌더링(PDF 변환 후 육안 확인) | **NOT RUN** — 동일 `soffice` 환경 장애. XSD 통과만 확인, 실제 페이지 레이아웃·표 렌더링은 미검증 |
| GitHub Actions `canonical-integrity` 워크플로 실행 | **NOT RUN** — 로컬 재현만 수행, 실제 CI 실행·결과는 push 후 Actions 탭에서 별도 확인 필요 |
| 독립 리뷰어 승인 | **NOT RUN** — PR #87 이재환 리뷰 진행 중, 미승인 |
| 실제 Excel/Word 프로그램에서 열람 확인 | **NOT RUN** — 사용자가 실제 프로그램에서 최종 확인 권장 |
| 실제 GitHub Issue 재수집(`ticket-sync.py`) | **NOT RUN** — 일정 변경은 Issue 코멘트로만 기록했고, `tickets/v3.1.19/{canonical-records.json,descriptions,sources}`는 v3.1.19 시점 스냅샷을 그대로 참조한다(Manifest에 명시) |
| Distribution ZIP 생성(`build-canonical-package.py`) | 스크립트 자체가 SHA256SUMS의 174개 경로 각각을 재해시해 대조한 뒤에만 ZIP을 작성하도록 되어 있어, 실행 성공 자체가 174/174 일치의 추가 증거다. 생성물은 Git에 커밋하지 않고(§2.1·v3.1.19 관례와 동일) 로컬 산출물로 사용자에게 전달했다 |
| WBS/Gantt 배포 통제(§2.1, 5곳 중 4곳) | `scripts/verify-wbs-gantt-distribution.sh v3.1.20 --candidate` PASS — 저장소 원본·Manifest·SHA256SUMS·ZIP 내부 4곳에서 동일 SHA-256(`e0b32416...`) 확인. 5번째(GitHub Release 독립 Asset)는 Tag/발행 전이라 해당 없음(`--published` 모드는 발행 후 별도 실행 필요) |

## 범위와 한계

- 문서 간 내부 정합성(WBS/Ticket Pack/WEB 상호 일치, SHA256SUMS 175/175 OK)은 확인했으나, `verify-canonical-release.sh` 전체 실행은 위 표와 같이 **현재 FAIL**이다(원인: 시크릿 스캐너의 `.docx` 미스킵 오탐, 수정안은 웹 UI 커밋 반영 대기 중). 이 FAIL이 해소되기 전에는 어떤 항목도 "canonical-integrity PASS"로 보고하지 않는다. GitHub Actions 실행, 독립 리뷰어 승인, 운영 Runtime 인수, Tag/Release 발행을 대신하지 않는다.
- WBS 수식 재계산과 DOCX 렌더링은 이 샌드박스의 `soffice` 장애로 미수행이다. 실제 Excel/Word에서 파일을 열어 재계산·레이아웃을 확인할 것을 권장한다.
- Architecture는 이번 후보에서 변경하지 않아(§2 item 7, 조건부 요건) 감사 대상에서 제외했다.
- Distribution ZIP은 현재 SHA256SUMS(174경로, docx 미포함) 기준으로 생성·검증했다. docx가 스캐너 수정 후 Manifest/SHA256SUMS에 추가되면 ZIP을 재생성해야 하며, 지금 생성한 ZIP은 그 시점에 다시 검증 대상이 아니게 된다.
- v3.1.19 이후 종결(Done 전환)된 Issue가 0건이므로 §2.3 완료 변경 요청 동기화 검증은 이번 감사의 적용 대상이 아니다(governance/CI 수정과 Phase 2 일정 재계획만 해당).

## 승인 경계

이 감사는 정본 Lead(이재환)의 PR #87 리뷰·승인을 대신하지 않는다. `CURRENT.md`는 v3.1.19를 유지한다. Tag 생성·GitHub Release 발행·Asset 업로드는 §6에 따라 권한 있는 운영자의 별도 결정·실행 사항이며 이 감사 결과가 그 결정을 선취하지 않는다.
