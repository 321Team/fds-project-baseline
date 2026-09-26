# Claude 세션 작업 규칙 — fds-project-baseline

공통 규칙은 [AGENTS.md](AGENTS.md)에 있다. 모든 AI 도구에 적용되며, 아래에서 불러온다.

@AGENTS.md

핵심 규칙:
- **Issue 본문은 직접 수정하지 않는다.** 본문 전체 재작성과 절·문단·링크·마커 편집이 해당한다. 이런 변경은 교체 본문 파일과 plan으로 넘기고, 담당자가 로컬 `gh`로 반영한다.
- **필수 속성값과 AC·잔여 항목 체크 상태는 갱신할 수 있다.** 대상 줄만 문자열로 치환하고, `updated_at`을 재확인한다. 쓰기 뒤에 재조회해 다른 줄 변경 0, 손상 신호 증가 0을 확인하고, 근거를 코멘트로 남긴다.
- **Milestone 설명도 쓰지 않는다.** 세션 경로가 footer를 붙인다. 기한처럼 텍스트 없는 값만 바꿀 수 있고, 반영 후 재조회로 다른 필드 불변을 확인한다.
- 근거: [TICKET_SYNC_POLICY §5.1](governance/TICKET_SYNC_POLICY.md)
