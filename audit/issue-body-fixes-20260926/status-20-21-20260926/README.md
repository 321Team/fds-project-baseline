# #20·#21 Status To Do → In Progress (2026-09-26)

지시: 2026-09-26 이권욱. 라벨은 2026-09-25 이재환(두 티켓 Lead)이 이미 `status:in-progress`로 바꿨다. 본문 Status만 To Do로 남아 있어 라벨과 맞지 않았다(TICKET_SYNC_POLICY §3).

## 변경 (Issue당 2줄, 나머지 바이트 불변)
| Issue | 줄 | 변경 전 → 변경 후 |
|---|---|---|
| #20 P1-E2E-01 | 50 | `\| Status \| To Do \|` → `\| Status \| In Progress \|` |
| #20 | 171 | `- **Status:** To Do` → `- **Status:** In Progress` (Completion Record) |
| #21 P1-DR-01 | 58 | `\| Status \| To Do \|` → `\| Status \| In Progress \|` |
| #21 | 179 | `- **Status:** To Do` → `- **Status:** In Progress` (Completion Record) |

- #20 본문은 CRLF 줄바꿈이다. 교체 본문도 CRLF를 그대로 유지했다.
- AC, 일정, 담당, 라벨, 상태는 바꾸지 않는다. 라벨은 이미 `status:in-progress`다.

## 실행 (Lead 로컬 `gh`)
1. 점검: `powershell -ExecutionPolicy Bypass -File .\apply-evidence-path.ps1`
   - 정상: `READY #20`, `READY #21`, `DRY RUN ready=2`
2. 반영: `powershell -ExecutionPolicy Bypass -File .\apply-evidence-path.ps1 -Apply`
   - 정상: `DONE applied=2`
3. `STOP edited after plan`이 나오면 멈춘다. 계획 시점 `updated_at`은 #20 `02:23:34Z`, #21 `02:23:35Z`다.
4. 반영 후 세션이 REST로 재조회해 대조한다. 확인 항목은 다음과 같다.
   - 본문이 교체 본문과 바이트 일치
   - 바뀐 줄 외 차이 0
   - 손상 신호 0
