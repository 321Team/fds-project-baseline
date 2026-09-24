# Claude 세션 작업 규칙 — fds-project-baseline

이 저장소를 여는 AI 세션은 아래를 따른다. 정책 원문이 우선한다.

## GitHub Issue 본문 쓰기 금지

- **Issue 본문(body)을 쓰지 않는다.** GitHub MCP(`issue_write` 등), 세션 프록시를 거치는 `gh`/API 모두 해당한다. 근거는 [TICKET_SYNC_POLICY §5.1](governance/TICKET_SYNC_POLICY.md)이다.
  - 이 경로로 쓴 본문에서 손상이 반복 확인됐다.
  - 손상 유형: `&lt;`·`&gt;` 엔티티화, 링크 ``` `` ``` 삽입, 따옴표 변환, footer 추가
- **본문 갱신이 필요하면** 다음 두 가지만 한다.
  1. 교체 본문 파일(UTF-8, LF)과 plan(`number`, `updated_at`, 변경 전 SHA-256, 파일 SHA-256)을 저장소 audit 경로에 준비한다. 반영은 담당자가 로컬 `gh`로 한다.
  2. 또는 결과를 Issue 코멘트로 남긴다. 세션 경로 코멘트에는 footer가 붙을 수 있다.
- 조회·대조(읽기)와 코멘트는 허용된다. 제목·라벨·상태 변경은 [TICKET_SYNC_POLICY](governance/TICKET_SYNC_POLICY.md)와 [REVIEW_AUTHORITY_POLICY](governance/REVIEW_AUTHORITY_POLICY.md)를 따른다.

## 참고

- 현재 발행 정본: [CURRENT.md](CURRENT.md)
- 발행·동기화 규칙: [RELEASE_POLICY](governance/RELEASE_POLICY.md)
