# v3.1.21 정본 수집 최신화 — 2026-10-03

최종 수집 시각: 2026-10-03T11:53:07.711+09:00. 최초 스냅샷 기록: 2026-10-03T11:38:03.223+09:00. 최초 원격조회 시작 시각은 별도 계측하지 않았다. 비원자적 스냅샷이며 각 Issue updated_at과 source HEAD 재조회 시작/종료시각을 별도 보존한다.

- 기준 정본: docs-v3.1.20 / RELEASED (Release API 확인)
- 입력 candidate HEAD: `39549c3b4aed92e6ea1e6e54735bfbe833b9c869`
- baseline main: `67ba6cf8a7f187e2dfcf188e4b2c55a853993778`; candidate behind=0 / ahead=91
- 14개 저장소 / Issue 78건 / 발행 이후 merged 257건 / 기존 대비 추가 144건
- main 계보 입력 255건, 후보 브랜치 동기화 #131/#133 2건을 구분한다.
- 수집 목록 누락 0은 이 조회 범위/시점 기준이며 Runtime 또는 AC PASS가 아니다.

## 실제 반영

intake.json, 두 candidate README, schedule.json을 갱신했다. repository-source-heads.json에 main/PR head/merge SHA/대상 브랜치/계보 검증을 고정했다. #34 Start/End를 10-08로, #34/#35/#36 Schedule Note를 순서와 HOLD 조건으로 정정하고 반영 후 본문 정확 일치 및 다른 메타데이터 불변을 확인했다.

## 검증·한계

STATIC: 병합 목록의 전체 페이지, merge SHA 계보, Record ID 유일성, 근무일 계산, 이슈 쓰기 전후 차이 검증. snapshot ZIP SHA256은 무결성만 확인한다. CI/Runtime은 이 작업에서 실행하지 않았다. 원본 Runtime의 성공을 재인수하지 않는다.

원본 메타데이터 이상 5건은 issue-index.json과 regeneration-plan.json에 남겼다. 부족한 값이나 closed/not_planned의 해석을 임의 Done/Cancelled로 고치지 않았다. 기존 workbook은 read-only 검사로 9개 시트·WBS 58개 레코드 및 stale 정본 표기를 확인했다. Workbook 수정·계산·시각 QA는 미실행이다.

## 재현

`snapshot.zip`를 UTF-8 JSON으로 풀면 원문 이슈/선택 댓글/PR/HEAD/계보/쓰기 전후 기록이 복원된다. `snapshot-integrity.json`의 압축/해제 해시를 검증한다. 이 감사 디렉터리에서 `python regenerate.py --from-snapshot <새 출력 디렉터리>`를 실행하면 네트워크 없이 동일 수집 산출물을 재생성한다(Python 3.12.14 검증). 출력 루트 기준 `SHA256SUMS`를 대조한다. 이 checksum은 audit 무결성용이며 Release SHA256SUMS가 아니다. 생성 규칙은 `regeneration-plan.json`, 전체 78건 입력 인덱스는 `proposed/Ticket-Pack-input.md`, Baseline 변경 입력은 `proposed/Baseline-change-input.md`다.

## 남은 HOLD

P1_CLOSE=HOLD / D21=OPEN / P2_ARCH_FREEZE=HOLD / P2_IAC_STAGE_A=NOT_READY. 10-08 연속 인계 시간은 미검증이다. 10-06 실제 Close와 미결 metadata/사양을 반영한 뒤 WBS/Baseline/Ticket Pack/Description 전체 재생성, Workbook QA, Manifest/SHA256SUMS/WEB/ZIP 검증이 필요하다. FULL_RELEASE_SET=NOT_GENERATED / MERGE=NOT_DONE / PUBLICATION=NOT_READY.
