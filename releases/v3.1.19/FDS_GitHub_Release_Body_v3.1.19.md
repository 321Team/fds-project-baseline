# FDS v3.1.19 — 정본 승인 변경·WBS·증적 통합

게시 본문 초안. 최종화 PR 승인·병합과 실제 Tag/Asset 검증 후 사용한다.

- 전체 67건·Milestone 67/67, 일정관리 58건·WBS/Gantt 9탭·차트 2개.
- 승인된 날짜·Milestone, Review 일정, 프록시 배치 및 OID-01/Storage/NTP downstream/Harbor/Trivy 입력 통합.
- Baseline·Ticket Pack·Description/원문·Interface/Decision/CR·WEB·아키텍처·Manifest·SHA256SUMS 포함.
- 내용 승인: [이하영, Review 5242201621](https://github.com/321Team/fds-project-baseline/pull/73#pullrequestreview-5242201621), HEAD `ce3f0c9704dc8316c078c0c427928a97b08e4408`. 내용 merge `f759d2d72cd4f943b19cbb3b46952f75ed0b8b09`.
- 최종화 승인·merge·Tag/Asset 게시는 별도 검증 대상. CI startup_failure는 로컬 검증과 구분.

배포 Asset 4개: `FDS_v3.1.19_Canonical_Baseline_Release_Package.zip`, 동일 ZIP의 `.sha256`, `SHA256SUMS`, `FDS_v3.1.19_WBS_and_Gantt_v1.0.xlsx`.

일정은 유연한 목표다. NTP upstream 및 Runtime/Gate 미결은 원문 그대로이며 문서 발행은 실서버 완료 승인이 아니다. 기존 v18 배포 이력을 보존한다. 게시자는 실제 최종화 승인·Tag commit·Asset 검증·published_at을 PR 기록에 연결한다.
