# Claude 세션 작업 규칙 — fds-project-baseline

공통 규칙은 [AGENTS.md](AGENTS.md)에 있다. 모든 AI 도구에 적용되며, 아래에서 불러온다.

@AGENTS.md

핵심 규칙: **GitHub Issue 본문(body)을 쓰지 않는다.** GitHub MCP(`issue_write` 등)와 세션 프록시를 거치는 `gh`/API가 모두 해당한다. 본문 갱신은 교체 본문 파일과 plan으로 넘기고, 반영은 담당자가 로컬 `gh`로 한다. 근거는 [TICKET_SYNC_POLICY §5.1](governance/TICKET_SYNC_POLICY.md)이다.
