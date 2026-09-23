# 증적 경로 일괄 반영 — 나머지 45건 (로컬 `gh` 실행용)

세션 쓰기 경로의 링크 변형(상위 README §3) 때문에, 남은 45건은 담당자 PC의 `gh`로 반영한다. 각 본문은 2026-09-23 재수집한 **현재 본문**을 기준으로 다시 만들었다. 오전 스냅샷 이후 #17 본문이 수정됐고 #24는 수정 시각만 바뀌었으며, 둘 다 현재 본문을 기준으로 했다.

| 파일 | 내용 |
|---|---|
| `plan.json` | 대상 45건: Issue 번호, Record ID, 계획 시점 `updated_at`, 변경 전 본문 SHA-256(LF), 교체 본문 파일과 SHA-256 |
| `bodies/issue-<번호>.md` | 교체할 본문(LF). 변경은 상단 `fds-evidence-path:20260923:v1` 마커 절 추가와 현행 영역 Evidence Path 값 변경뿐이다 |
| `apply-evidence-path.ps1` | Windows PowerShell 5.1용 실행 스크립트(ASCII) |

계획 생성 시 확인한 것: 45건 모두 마커가 없다. 보관 원문이 있는 본문은 원문 SHA-256이 일치한다. 교체 본문은 최대 58,359자다.

## 실행 순서

1. 브랜치 ZIP을 내려받는다: <https://github.com/321Team/fds-project-baseline/archive/refs/heads/claude/busy-goodall-nop332.zip>
   - 브라우저로 받아야 파일 바이트가 그대로 유지된다. PowerShell 리디렉션(`>`)은 인코딩을 바꾸므로 쓰지 않는다.
2. 압축을 풀고 이 폴더(`audit/phase2-repo-bootstrap-20260923/evidence-path-batch`)로 이동한다.
3. 점검 실행(쓰기 없음): `powershell -ExecutionPolicy Bypass -File .\apply-evidence-path.ps1`
   - 정상: `READY #번호` 45줄 뒤에 `DRY RUN ready=45`
4. 반영: `powershell -ExecutionPolicy Bypass -File .\apply-evidence-path.ps1 -Apply`
   - 정상: `OK #번호 <시각>` 45줄 뒤에 `DONE applied=45`

## 중단과 재실행

- 아래 경우 `STOP`으로 즉시 멈춘다. 이미 반영한 건은 그대로 두고 되돌리지 않는다.
  - 본문 파일 해시 불일치
  - 계획 이후 Issue 수정(`updated_at` 변경)
  - `gh` 읽기·쓰기 실패
- 반영한 번호는 `applied.txt`에 남는다. 원인을 해결하고 다시 실행하면 기록된 번호는 건너뛴다.
- `edited after plan`으로 멈추면 그 Issue는 계획을 새로 만들어야 한다. 임의로 건너뛰거나 본문 파일을 고치지 않는다.

## 검증 상태

STATIC: 45개 본문 파일 SHA-256 = `plan.json` 확인, 스크립트 ASCII 확인. 2026-09-23 이권욱 PC에서 실행: 점검 모드 `DRY RUN ready=45`, 반영 `DONE applied=45`(12:28:56Z~12:30:56Z). 세션에서 재조회로 검증: 45건 모두 계획 본문과 일치, 깨진 링크 0, footer 없음, 현행 영역 구 경로 0, 보관 원문 해시 일치 44건(보관 원문 없음 1건). 결과는 상위 `evidence-path-result.json`에 기록했다.
