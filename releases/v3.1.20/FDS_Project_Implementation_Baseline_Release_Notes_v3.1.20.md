# FDS v3.1.20 Release Notes

상태: **RELEASED** · `docs-v3.1.20` · 게시 2026-09-23 02:37:13 KST

> **발행 후 상태 정정 — 2026-09-30 KST:** 본 문서 아래의 `후보`, `발행 잔여`, `정식 발행 보류` 표현은 2026-09-22 후보 작성 시점의 역사 기록이다. 현재 정본 상태는 `CURRENT.md`와 GitHub Release API의 `docs-v3.1.20 / RELEASED`가 우선한다. v3.1.20 Tag/Asset/SHA256SUMS는 소급 수정하지 않으며, 본 상태 설명 정정은 차기 정본 후보 PR #112에서 추적한다.

전체 67건 / 일정관리 58건 / 역사적 종결 9건 / Milestone 67/67건. 상태 집계: Done 18, In Progress 11, To Do 38. (v3.1.19 대비 Status 변경 없음 — governance/CI 수정과 Phase 2 24건 일정 갱신만 반영)

## 승인 입력과 적용 경계

| 항목 | 반영한 값·결정 | 유지되는 경계 |
|---|---|---|
| [PR #82](https://github.com/321Team/fds-project-baseline/pull/82) | `canonical-integrity.yml` checkout SHA 고정 (병합 완료) | CI 워크플로 자체 보안 강화 조치이며 정본 콘텐츠 변경 아님 |
| [PR #88](https://github.com/321Team/fds-project-baseline/pull/88) | `verify-canonical-release.sh` WARN/FAIL 분리 로직 신설(governance/·`.github/workflows/`·스크립트 자기 경로 한정 WARN, 그 외 전부 FAIL); hayeounglee 리뷰 2건(FAILED open/read 미탐지, `scripts/` 예외 과다범위) 수정 반영 후 병합 | `verify-document-secrets.py` 등 다른 scripts/ 파일은 예외 대상에서 명시적으로 제외 |
| [PR #89](https://github.com/321Team/fds-project-baseline/pull/89) | `.github/workflows/pr-review.yml`(Gemini AI 리뷰 연동, 중단됨) 제거 (병합 완료) | 리뷰 자동화 도입 자체를 재검토하지 않음, 단순 원복 |
| [PR #86](https://github.com/321Team/fds-project-baseline/pull/86) | `audit/canonical-followup-20260921/` 전수 감사 및 checksum-drift 기록 (병합 완료) | 감사 결과 기록이며 감사 자체가 정본 상태를 변경하지 않음 |
| governance/RELEASE_POLICY.md §2.4 (PR #88) | "운영 경로 드리프트" WARN 예외 범위를 문서화 | FAIL 대상(정본 콘텐츠 경로) 축소나 완화 아님 |
| Phase 2 일정 재계획 (Lead 이재환 결정, 2026-09-22) | `MS-P2-START-01`(#33) 착수 09-28→10-06 순연 반영. 뒷단(G6 10-22~Project Close 10-26) 고정 + 앞단(착수~G5) 24일→16일 압축(비율 0.667). `DEC-P2-DNS-01`(#40)·`DEC-P2-OP-01`(#41)·`DEC-P2-REG-01`(#42) 3건은 Decision Register 시한(2026-10-16) 고정으로 압축 예외. `CR-P1-MON-01-01`(#74) End, `CR-P1-MON-01-02`(#75) Start/End TBD값에 실제 값 입력 | Baseline/WBS/Ticket Pack의 Plan Start/End만 갱신했으며 Status·Lead·AC 등 종결 필드는 변경하지 않음(§4.1 일정 유연성 범위). 실제 착수·완료·Gate 승인 여부를 바꾸지 않음 |

근거: [releases/v3.1.20/README.md](https://github.com/321Team/fds-project-baseline/blob/release/v3.1.20/releases/v3.1.20/README.md) 2026-09-21/09-22 감사 기록 및 2026-09-22 Phase 2 일정 재계획 절. Phase 2 티켓별 갱신 코멘트는 각 Issue(#33~#57, #74~#75)에 개별 기록했다.

## 승인·관측·보류 분류

APPROVED_INPUT은 확인된 사용자/Lead 결정의 명시 범위만 뜻한다. GitHub의 Merged는 코드/문서 편입 사실이며 Runtime 인수나 정식 발행이 아니다. 이번 버전은 v3.1.19 태그 이후 종결(Done 전환) Issue가 0건이므로 §2.3(완료 변경 요청의 정본 동기화) 기준상 의무 발행 사유는 없으며, Lead 요청에 따라 governance/CI 수정과 Phase 2 일정 재계획을 후보로 수집한 것이다. 원문 AC·Status·Lead·종결 이력은 새로 체크하거나 변경하지 않았다.

## 배포 구성

이번 후보는 다음 3개 산출물을 v3.1.19 대비 실제 편집으로 갱신했다: Baseline(`FDS_Project_Implementation_Baseline_v3.1.20.md`), WBS/Gantt(`FDS_v3.1.20_WBS_and_Gantt_v1.0.xlsx`, 9개 탭), Ticket Pack(`FDS_v3.1.20_Canonical_Ticket_Update_Pack_v1.0.md`). Architecture는 변경 사유가 없어(§2 item 7, 조건부 요건) v3.1.19 산출물을 그대로 참조한다. Interface/Decision/CR Register, 67건 Description 원문, `governance/`·`.github/workflows/` 정책·CI 변경분은 v3.1.19 Register/파일을 기준으로 하되 본 Release Notes 상단 표의 PR로 추적한다.

WBS 편집은 셀 단위 diff로 검증했다(포뮬러 0건 변경, 의도한 48개 셀만 변경). 이 샌드박스에서 LibreOffice 재계산이 동작하지 않아 정식 재계산 검증은 미수행이므로, 실제 Excel에서 재계산·시각 확인을 권장한다.

## 후보 작성 당시 발행 잔여 — 현재는 발행 완료

아래 내용은 후보 작성 당시 잔여 항목이었다. 이후 PR #87 병합·최종화와 `docs-v3.1.20` Tag/GitHub Release/Asset 발행이 완료되어 현재 배포 상태 판단에는 사용하지 않는다. 당시 후보 단계에서는 이재환 리뷰, Distribution Manifest, SHA256SUMS, Integrity Audit Result, WEB 스냅샷, Distribution ZIP+checksum 및 Tag/Release 발행이 잔여였다.

배포 상태의 효력과 작성 시점은 `releases/v3.1.20/README.md`를 따른다.
