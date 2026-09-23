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
| `scripts/verify-canonical-release.sh` (실제 스크립트 실행) | **PASS** — SHA256SUMS 체크섬 불일치 0(176/176 OK), 시크릿 스캔 findings=0(378개 파일 스캔), WBS/Gantt 배포 검증(candidate) PASS |
| 시크릿 스캔 회귀 원인·수정 이력 | `verify-document-secrets.py`가 `.xlsx`는 스킵하면서 동일한 OOXML 컨테이너인 `.docx`는 스킵하지 않아 어떤 내용의 `.docx`든 100% "unreadable text"로 오탐했다. 1줄 수정(`.docx`를 스킵 목록에 추가)은 자동 커밋 분류기가 보안 스캐너 변경으로 차단해 사용자가 GitHub 웹 UI로 직접 커밋(`b0550f0`)했다. pull 후 재실행해 findings 1→0 확인 |
| Baseline 헤더/§0 절 | `sed`로 렌더링 확인, CANDIDATE/COLLECTING 상태 표기 및 신규 §0 절 삽입 확인 |
| DOCX(중간 산출물 보고서) 구조 | `scripts/office/validate.py` XSD 스키마 검증 PASS (Paragraphs: 169) |
| WBS 수식 재계산(LibreOffice) | **NOT RUN** — 샌드박스에서 `soffice` 타임아웃(120s/180s 모두 실패, 환경 전역 문제로 별도 확인). 셀 diff로 수식이 편집되지 않았음만 확인했고, 재계산 결과 자체는 검증하지 못했다 |
| DOCX 렌더링(PDF 변환 후 육안 확인) | **NOT RUN** — 동일 `soffice` 환경 장애. XSD 통과만 확인, 실제 페이지 레이아웃·표 렌더링은 미검증 |
| GitHub Actions `canonical-integrity` 워크플로 실행 | HEAD `9fa13f8` 기준 실제 Actions 실행 확인(run #94 push / #95 pull_request) — 둘 다 `conclusion: success` |
| 독립 리뷰어 승인 | PR #87, supreme33-kr(이재환, AI 보조·사람 확인 CONFIRMED 명시) APPROVED 3회, 최신 2건이 HEAD `9fa13f8` 기준. CHANGES_REQUESTED 없음, 미해결 리뷰 스레드 0건 |
| 실제 Excel/Word 프로그램에서 열람 확인 | **NOT RUN** — 사용자가 실제 프로그램에서 최종 확인 권장 |
| 실제 GitHub Issue 재수집(`ticket-sync.py`) | **NOT RUN** — 일정 변경은 Issue 코멘트로만 기록했고, `tickets/v3.1.19/{canonical-records.json,descriptions,sources}`는 v3.1.19 시점 스냅샷을 그대로 참조한다(Manifest에 명시) |
| Distribution ZIP 생성(`build-canonical-package.py`) | 스크립트 자체가 SHA256SUMS의 175개 경로(docx 포함) 각각을 재해시해 대조한 뒤에만 ZIP을 작성하도록 되어 있어, 실행 성공 자체가 175/175 일치의 추가 증거다. 생성물은 Git에 커밋하지 않고(§2.1·v3.1.19 관례와 동일) 로컬 산출물로 사용자에게 전달했다 |
| WBS/Gantt 배포 통제(§2.1, 5곳 전부) | Tag `docs-v3.1.20`·GitHub Release·Asset 4종 업로드는 정본 Lead가 웹 UI에서 직접 수행(이 세션의 git tag push는 HTTP 403, GitHub MCP 도구셋에 Release 쓰기 기능 없음). 발행 후 5번째 위치(GitHub Release Asset)를 GitHub가 보고하는 asset `digest` 필드로 대조 — WBS `e0b324161d07b0d46db93065d9c3334c36459d0d84b2b7c4e81ff6799e210479`, ZIP `9a1044d5c84273ca54ecdf577395c1c45d4813b18a26a1192e68dac4305230d4` 모두 저장소 원본·Manifest·SHA256SUMS·ZIP 내부 값과 일치. `gh` CLI 부재로 `--published` 모드 자동 검증은 수행하지 못했고 수동 대조로 대체했다 |

## 범위와 한계

- 문서 간 내부 정합성(WBS/Ticket Pack/WEB 상호 일치, SHA256SUMS 176/176 OK)과 `verify-canonical-release.sh` 전체 실행 PASS(시크릿 스캐너 수정 반영 후)를 확인했다. 이 PASS는 로컬 재현 기준이며, GitHub Actions 실제 실행, 독립 리뷰어 승인, 운영 Runtime 인수, Tag/Release 발행을 대신하지 않는다.
- WBS 수식 재계산과 DOCX 렌더링은 이 샌드박스의 `soffice` 장애로 미수행이다. 실제 Excel/Word에서 파일을 열어 재계산·레이아웃을 확인할 것을 권장한다.
- Architecture는 이번 후보에서 변경하지 않아(§2 item 7, 조건부 요건) 감사 대상에서 제외했다.
- Distribution ZIP은 docx 포함 최종 SHA256SUMS(175경로) 기준으로 재생성·재검증했다.
- v3.1.19 이후 종결(Done 전환)된 Issue가 0건이므로 §2.3 완료 변경 요청 동기화 검증은 이번 감사의 적용 대상이 아니다(governance/CI 수정과 Phase 2 일정 재계획만 해당).

## 승인 경계

이 감사는 정본 Lead(이재환)의 PR #87 리뷰·승인을 대신하지 않았으며, 실제로 PR #87은 이재환(`supreme33-kr`) APPROVED 3회로 병합됐다. Tag(`docs-v3.1.20`) 생성·GitHub Release 발행·Asset 업로드는 §6에 따라 권한 있는 운영자(정본 Lead)가 직접 실행했다. `CURRENT.md`는 이 발행을 반영해 v3.1.20으로 갱신했다(별도 PR).
