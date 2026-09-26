# Issue 본문 정정 기록 — 2026-09-26

이날 반영한 Issue 본문 변경 3건의 기록이다. 모두 담당자가 로컬 `gh`로 `apply-evidence-path.ps1`를 실행해 반영했다([TICKET_SYNC_POLICY §5.1](../../governance/TICKET_SYNC_POLICY.md)). 세션은 교체 본문과 plan만 준비하고, 반영 뒤 REST로 재조회해 대조했다.

| 폴더 | 대상 | 변경 | 반영(UTC) |
|---|---|---|---|
| `issue-9-repair-20260926/` | #9 | 재손상 복구: 09-26 04:05Z LB 세션 편집이 다시 일으킨 엔티티화·링크 `` 삽입을 되돌리고, 그 편집의 정당한 변경은 유지함 | 04:20:00Z |
| `status-20-21-20260926/` | #20·#21 | 본문 필수 속성 Status를 `In Progress`로 정정 | 05:50:52Z·05:51:02Z |
| `status-74-20260926/` | #74 | 인수 완료 확인 후 본문 Status를 `Done`으로 정정. 라벨은 세션이 값 전용 쓰기로 변경(05:53:17Z) | 05:54:51Z |

각 폴더의 구성은 `bodies/`(교체 본문, UTF-8·LF), `plan.json`(`number`, `updated_at`, 변경 전 SHA-256, 파일 SHA-256), `apply-evidence-path.ps1`, `README.md`다.

## 재검증

`result.json`은 반영 뒤 REST GET으로 읽은 결과다(읽기 전용).

- 4건 모두 현재 본문의 SHA-256(LF 정규화)이 `bodies/` 파일과 일치한다.
- 손상 신호(`&lt;`·`&gt;`·링크 `` 삽입·footer)는 모두 0이다.

## 남은 사항

- #11 본문 Status 불일치는 담당 Lead의 결정을 기다린다. 결정 전에는 변경하지 않는다.
- #9를 편집한 LB 세션에 중단을 알리는 노티는 사용자가 전달한다. 세션끼리는 메시지를 보낼 수 없다.
