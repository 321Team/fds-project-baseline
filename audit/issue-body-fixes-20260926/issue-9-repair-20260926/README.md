# #9 P1-LB-01 본문 재복구 (2026-09-26)

## 손상
2026-09-26T04:05Z 편집(LB 세션 `session_01GZPGUJ…`)이 상단에 "PR10 독립 승인·병합 완료" 절을 추가했다. 이 편집에서 두 가지 손상이 함께 생겼다.
- 기존 본문 링크 9줄에 ``` `` ```가 삽입됐다(유형 B).
- 기존 문장 1곳이 바뀌었다("…AC 체크는 유지." → "…유지한다.").

보관 원문 해시는 일치했다.

## 교체 본문 (`bodies/issue-9.md`)
- 04:05Z에 추가된 PR10 절(13줄)은 유지한다. 손상 신호 0건을 확인했다.
- 그 아래 본문은 마지막 검증본인 2차 반영본(SHA-256 `2e098bbb…`)과 바이트가 같다. 손상된 9줄과 바뀐 1줄은 이 검증본의 원래 문구로 되돌아간다.
- 확인한 것:
  - 보관 원문 SHA-256 `43f83489…` 일치
  - `&lt;`·`&gt;`·링크 ``` `` ```·footer 0건
  - 변경 전 본문과 비교해 차이는 위 10줄뿐
- 변경 전 SHA-256 `0dcf4e83…`(길이 42,842), 교체 후 `1ddbd311…`(길이 42,776)

## 실행 (Lead 로컬 `gh`, 9/23·9/25 절차와 동일)
1. 점검: `powershell -ExecutionPolicy Bypass -File .\apply-evidence-path.ps1`
   정상 결과: `READY #9 P1-LB-01`, `DRY RUN ready=1`
2. 반영: `powershell -ExecutionPolicy Bypass -File .\apply-evidence-path.ps1 -Apply`
   정상 결과: `OK #9 <시각>`, `DONE applied=1`
3. `STOP edited after plan`이 나오면 멈추고 계획을 새로 만든다. 계획 시점 `updated_at`은 2026-09-26T04:10:59Z다.
4. 반영 뒤 검증은 세션이 REST로 재조회해서 한다. 본문 바이트 일치를 확인한다.
