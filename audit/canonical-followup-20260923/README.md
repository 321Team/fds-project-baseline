# v3.1.20 발행 후 정정 기록 (2026-09-23)

기준: main `2784eb9` (PR #99 병합 후), 태그 `docs-v3.1.20` → `336446500ef99…`(PR #87 내용 병합). 결정: 2026-09-23 정본 Lead(사용자) “권장사항으로 처리” — 발행된 Tag·Release Asset은 수정하지 않는다. main의 정정은 이 기록으로 추적하고, 체크섬 대상 파일의 정정은 차기 후보 v3.1.21에서 정식 반영한다(A안).

이 기록은 정본 발행이나 v3.1.21 후보 생성이 아니다. 아래 “v3.1.21 반영 필요” 항목은 아직 수행하지 않았다.

## 1. 확인 사실과 처리

| # | 항목 | 확인 사실 | 처리 |
|---|---|---|---|
| 1 | 루트 README 버전 표시 | README가 태그 `docs-v3.1.19`와 “현재 발행 정본 v3.1.17”(v3.1.18 후보 절)로 표시됐다. v3.1.20 최종화 PR #91은 `CURRENT.md`만 갱신했다. | 이 PR에서 README를 v3.1.20 기준으로 정정했다. 발행 이력 표로 정리했다. README는 SHA256SUMS 대상이 아니다. |
| 2 | Tag 대상 | `docs-v3.1.20`은 최종화 병합 `9f57e69`(PR #91)가 아닌 내용 병합 `3364465`(PR #87)를 가리킨다. 태그 시점 `CURRENT.md`는 “v3.1.19 / RELEASED”다. main `CURRENT.md`는 태그를 “finalization merge commit”으로 적고 있다. v3.1.19는 최종화 병합(`966fc53`, PR #79)을 태그했다. | 발행 Tag를 옮기지 않는다(불변). README에 주의 문구를 넣었다. **v3.1.21 반영 필요:** `CURRENT.md`의 Tag 설명을 사실대로 정정한다. 다만 `CURRENT.md`는 `releases/v3.1.20/SHA256SUMS` 대상이므로 이번에는 수정하지 않는다. |
| 3 | 발행 후 Release 디렉터리 수정 | PR #92(발행 후, 독립 리뷰 hayeounglee)가 `releases/v3.1.20/reports/FDS_Interim_Deliverable_Report_v3.1.20.docx`를 정정했다. 태그 시점 `337fa275a33f3196b51adcfac9befdee9c9b9fba4571a904a3f5e2705c5935c3` → main `04b8daf58efb4fdfb7947d6b4635c4be4e3bd237ec2b466daa70962bba777735`. 정정 내용은 CR-P1-MON-01-01/02 일정 확정이다. 같은 PR에서 Manifest·SHA256SUMS를 재계산했고, SHA256SUMS에서 Manifest 자신의 행을 제거했다. | A안을 적용한다. main의 정정본을 유지하고 이 기록으로 추적한다. **발행 ZIP·Release Asset은 태그 시점 docx를 기준으로 생성된 것으로 본다(비공개 저장소라 Asset 재다운로드 대조는 NOT RUN).** **v3.1.21 반영 필요:** 정정 docx 포함, Manifest 해시 행 복원 또는 대체 무결성 수단을 명시한다. |
| 4 | `releases/v3.1.20/README.md` 상태 문구 | 파일이 여전히 “CANDIDATE / COLLECTING (정식 발행 보류)”로 표시된다. SHA256SUMS 대상(`f0511340…`)이다. | 이번에는 수정하지 않는다(체크섬 대상). **v3.1.21 반영 필요:** v3.1.20 RELEASED/SUPERSEDED 상태로 정리한다. |
| 5 | governance 드리프트 | PR #93(Pre-check 정책)으로 `governance/REVIEW_AUTHORITY_POLICY.md`, `governance/RELEASE_POLICY.md`가 등록 해시와 다르다. `verify-canonical-release.sh`는 WARN(§2.4 예상 드리프트)이다. | **v3.1.21 반영 필요:** SHA256SUMS·Manifest에 동기화한다(RELEASE_POLICY §2.3). |
| 6 | `retrospectives/` | PR #94·#96·#97·#98·#99로 추가됐다. SHA256SUMS·Manifest·README 구조 표에 없다. | README 구조 표에 추가했다. **v3.1.21 결정 필요:** 정본 체크섬 대상 편입 여부를 정한다. |

## 2. 검증

- `bash scripts/verify-canonical-release.sh` (main `2784eb9` + 이 PR): 결과는 `canonical-integrity: PASS (WITH OPERATIONAL DRIFT WARNINGS)`다. WARN 대상은 governance 2건이다.
- 태그 대조: `git show docs-v3.1.20:<path> | sha256sum`으로 위 docx 해시와 태그 시점 `CURRENT.md` 내용을 확인했다.
- 이 검사는 main 파일과 main의 SHA256SUMS 간 일치만 본다. Tag·Release Asset과의 일치는 판정하지 않는다.

## 3. 상태

REVIEW=NOT_REQUIRED(문서 전용, 정본 Lead 판단) / 발행 Tag·Asset 변경 없음 / v3.1.21 후보 NOT STARTED
