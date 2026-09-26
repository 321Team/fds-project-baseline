# #9 P1-LB-01 증적 경로 반영 — 2차 (2026-09-25)

지침 `issue-body-repair-20260925/kit/REPAIR_GUIDE_issue-9-74-75.md` §5를 따른다. #9는 [누락 후속](../evidence-path-followup-20260925/README.md)에서 본문 손상 때문에 보류됐다. [본문 복구](../issue-body-repair-20260925/README.md)를 반영하고 검증한 뒤, 같은 형식으로 증적 경로를 반영한다. 복구와 경로 반영은 따로 검증하기 위해 두 번에 나눠 적용한다.

## 교체 본문 (`bodies/issue-9.md`, LF)

변경 전 본문은 복구 반영된 현재 본문이다(`updated_at` 2026-09-24T19:01:49Z). 이 본문은 `issue-body-repair-20260925/bodies/issue-9.md`와 같고, 해시는 `66e540bb…`이다. 2026-09-25 반영 직후 재조회에서 바이트 일치를 확인했다.

변경은 두 가지뿐이다.

1. 상단에 `fds-evidence-path:20260923:v1` 마커 절을 추가한다. PR #105 7건과 같은 문구이고, 두 번째 항목만 #9 경위(누락 → 손상 복구 뒤 반영)로 바꿨다.
2. 현행 영역 454행 `` `docs/evidence/P1-LB-01/` `` 1곳을 `` `321Team/fds-project-evidence:evidence/P1-LB-01/` ``로 바꾼다. 보관 원문 안 572행의 같은 경로는 바꾸지 않는다.

생성 시 자동 확인한 것:

- 마커 절을 빼고 바꾼 값을 되돌리면 변경 전 본문과 바이트가 같다.
- 보관 원문 SHA-256 `43f83489…94201` 일치
- 현행 영역 구 경로 0(마커 절의 "변경 전" 표기는 제외)
- `&lt;`·`&gt;`·단독 ``` `` ```·footer·CRLF 0

## 실행 (Lead 로컬 `gh`, 9/23 절차와 동일)

`apply-evidence-path.ps1`은 9/23 스크립트와 같고, 주석 첫 줄만 다르다.

1. 점검(쓰기 없음): `powershell -ExecutionPolicy Bypass -File .\apply-evidence-path.ps1`
   - 정상: `READY #9 P1-LB-01` 뒤에 `DRY RUN ready=1`
2. 반영: `powershell -ExecutionPolicy Bypass -File .\apply-evidence-path.ps1 -Apply`
   - 정상: `OK #9 <시각>` 뒤에 `DONE applied=1`
3. `STOP`이 나오면 멈춘다. `edited after plan`이면 계획을 새로 만든다.
4. 반영 후 `issue-body-repair-20260925/fetch-edit-history.ps1`로 다시 조회해 세션에 전달한다. 세션이 다음을 확인하고 `result.json`에 남긴다.
   - 본문 SHA-256 일치
   - 보관 원문 해시
   - 손상 표기 0
   - 제목·상태·라벨 불변

## 반영 결과 (2026-09-25)

이권욱 로컬 `gh`로 실행했다. ZIP SHA-256 `8d6b8385…8aa9b` 일치를 확인했고, `DRY RUN ready=1` → `DONE applied=1`(2026-09-24T23:42:10Z).

재조회(읽기 전용): ZIP `22ab8d06…75cdcdc`, 내부 `SHA256SUMS.txt` 6/6 일치. 결과는 `result.json`에 있다.

- 재조회 본문(LF)이 `bodies/issue-9.md`와 바이트 일치(`2e098bbb…`). 편집 이력에 반영 편집 1건이 추가됐다(23:42:10Z, GWONUK).
- 현행 영역 구 경로 0, 새 경로 1. 보관 원문의 구 경로 1곳은 유지했다.
- 보관 원문 SHA-256 `43f83489…` 일치
- `&lt;`·`&gt;`·단독 ``` `` ```·footer·CRLF 0
- 제목·상태·라벨 불변. #74·#75는 19:01Z 이후 변경 없음. 반영 직후 수정 시각 역순 조회에서 다른 Issue 변경은 0건

STATIC=교체 본문 자동 검증 / Issue 쓰기=1/1 반영(Lead 로컬 `gh`)·재조회 검증 완료, 이 세션 쓰기 0
