# Work · Codex 공통 작업 지침

이 파일은 Work와 Codex에 동일하게 적용한다. 먼저 `WORK_START.md`와
`handoff/OPERATING_RULES.md`를 읽는다. 대화 기억·이전 ZIP·로컬 CURRENT 사본만으로
현재 사양이나 진행 상태를 판단하지 않는다.

1. 사양은 `handoff/baseline.lock.json`의 발행 Tag/Commit/Checksum으로 고정한다.
   작업 상태는 관련 GitHub Issue 본문·댓글·PR HEAD·Review·증적 수신 Commit을
   새로 조회한다. 사양과 상태의 출처를 서로 대체하지 않는다.
2. 한 작업에 `handoff/task.template.json`을 채우고 공통 context receipt를 만든다.
   Work와 Codex는 같은 task SHA-256/context_id를 인계한다. 수행 전과 인계 전에
   `scripts/shared_context.py check`를 실행한다. 다른 값·조회 실패·오래된 receipt는
   중단 사유다. 내려받은 API 사본은 SNAPSHOT_ONLY이며 현재 상태 확인을 대신하지 않는다.
3. 수정 대상 저장소의 base Commit 및 작업 HEAD를 결과에 기록한다. 시작 이후
   새로운 Issue/PR이 작업에 관련되면 task watch 목록을 갱신하고 함께 재인계한다.
   다른 미병합 PR의 내용을 main에 존재하는 것으로 가정하지 않는다.
4. `governance/RELEASE_POLICY.md`, `governance/TICKET_SYNC_POLICY.md`,
   `governance/GITHUB_IDENTITY_MAP.md`의 승인·필드 소유권을 지킨다. Issue 상태,
   AC, 담당, 일정, 승인, Runtime 완료는 소스 코드 수정으로 자동 변경하지 않는다.
5. 이 공통 체계의 추가는 v3.1.18 배포본 변경이 아니다. 기존 배포 파일·Manifest·Tag·
   Asset을 덮어쓰지 않는다. 이번 변경도 release 브랜치/Draft PR로 제출하고 독립 검토와
   승인 운영자의 수동 병합을 거친다. 자기 승인이나 자동 병합을 하지 않는다.
6. Cloud Codex는 구현·정적/모의검증·재생성·PR 준비에 사용한다. 교육장 VM 실행,
   kubeadm/etcd/방화벽/SELinux/Harbor 적용은 해당 티켓의 현장 Gate에서 수행한다.
   공용 PC에 개인키·장기 토큰·개인 작업 저장소를 저장하지 않는다.
7. 결과는 STATIC, MOCK, CI, RUNTIME, REVIEW, MERGE, PUBLICATION을 구분한다.
   미실행은 NOT_RUN, 미확인은 UNVERIFIED, 승인은 PENDING으로 기록한다.
   checksum 일치나 테스트 통과는 Runtime/독립 승인 증거가 아니다.

AGENTS.md는 세션 시작 시 읽히므로 지침이 바뀌면 새 세션에서 다시 읽는다.
새 사양이나 새 승인을 추측하여 빈칸을 채우지 않는다.
