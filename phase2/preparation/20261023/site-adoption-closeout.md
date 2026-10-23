# #46 운영 SITE 연결 — 현재 입력과 실행 시 생성값

이권욱 / CODEX_ASSISTED · 2026-10-23. 이 문서는 실행 입력·새 승인 원본이 아닌 운영 채택 검토표다. `SITE=None`, 실제 SSH·ROSA·발급·배포는 미실행이다. 이미 수신한 원본10/10·발급 인가와 구현을 재사용하고 없는 실제값을 합성하지 않는다.

## 현재 코드 연결과 남은 채택

| 구간 | 구현·기수신 근거 | 남은 실제 채택 / 담당 |
|---|---|---|
| 고정 대상·산출물 | `delivery_fds_site_inputs`: 실제 API origin·cluster UUID·namespace UID·SA/UID·issuer/audience·공개 CA·MSA42 source·render/contract·2이미지·Route host가 수신 원본과 연결됨 | 권욱: 기존 profile을 재사용. 과거 LB 주소를 현재 endpoint로 고정하지 않음. 원본은 [수신 검토](https://github.com/321Team/fds-project-baseline/issues/46#issuecomment-6339413996) 참조 |
| 실제 Runner/job·SSH | `assemble_existing_job_site` → owned rendezvous → peer UID 검증 → 기존 부모/driver. SSH bridge·pipe/socketpair stdio 구현, PR120 호환 보완 | 권욱 채택·재환 기존 자료 대조: 실제 hostname·일반 UID·helper UID·같은 netns·SSH 방향/계정/current key·절대 helper 경로·인증된 공개 ready 전달. GitHub 등록명 `cicd-runner01`만으로 OS hostname/UID를 확정하지 않음 |
| 발급·메모리 전달 | PR122 `TokenRequestIssuer`/`RequestBoundSupplier`, PR123 READY 후 발급→bridge→ACK/EOF/rc. actor는 전달하지 않고 deployer/source 자격만 전달 | 권욱 연결·하영 기존 발급 경계 근거: 현재 actor와 실제 endpoint·원본 보존/인계 연결. `can-i`나 설계 항목만으로 발급 성공을 선언하지 않음 |
| 원본/control·계획 완성 | 기존 private source 인증, 5역할 `SourceRoleWiring`, `PreparedAuthorityPlan`, authority factory·현재 RBAC·baseline 대조 | 권욱: 실제 approval/platform/producer/baseline original과 control의 의미·인증 경로를 채택. finish는 아래 실행 단계에서 생성. 해시·타입·복사한 JSON을 권위로 승격하지 않음 |
| 이미 존재하는6객체 | existing-target 경로는 Deployment2·Service2·Route2의 full raw·UID/spec/허용 owner·명시 previous를 요구. replicas0을 허용하며 first-empty로 자동 전환하지 않음 | 권욱 인수·하영 플랫폼 원본·재환 previous 근거: 현재 full spec/managedFields 원본을 연결. UID/RV 표와 배포 manifest를 결합해 만들지 않음. SCC/UID Pod JSON도6객체 full baseline 대체물이 아님 |

## 사전에 결정할 값과 실행 때만 생기는 값

1. 사전 코드 채택: 기존 대상, trusted source/control 의미, Reader 저장소 범위, 실제 Runner/SSH/helper 경로, 명시 baseline/previous, 소비할 기승인 범위. 미확정이면 현재 차단을 유지한다.
2. 실제 job 시작 때: native workflow SHA/run/attempt·nonce·현재 peer·로컬 monotonic 마감. 미래 run 번호나 두 호스트 공통 monotonic 값을 사전 문서에서 만들지 않는다. 이 값은 담당자 사전 제출 누락으로 취급하지 않는다.
3. 실제 발급 때: TLS로 받은 TokenRequest 원문, fingerprint·iat/exp, receipt. **`Binding.platform_receipt_sha256`은 request.key 전에 고정된 플랫폼 원본이다. 이후 발급 응답의 hash를 역대입하지 않는다.** 두 원본의 의미와 인증 연결은 별도로 채택하며 명목상 projection으로 대신하지 않는다.
4. 실제 종료 때: 후속 관측과 독점 접근 종료 원본·control, terminal progress/finish receipt. 미래 완료 해시를 미리 고정하지 않는다. 미수신·미설치면 완료 대신 기존 fence를 유지한다.

## 실패·정리와 다음 검증

- 발급 전 READY/UID/기한 실패에는 발급하지 않는다. POST를 시도했는데 응답이 불명확하면 발급 여부 불명으로 보존하고 자동 재시도하지 않는다.
- 발급 후 전달 실패도 유효 자격이 남을 수 있다. 기존 supplier의 `take_receipt()`로 실제 receipt를 먼저 비공개 인계한 다음 `close()`한다. 로컬 참조/FD 정리는 서버 토큰 회수가 아니다. 상세 만료·인증 확인은 실행 GO와 실제 자격 수명 범위에서 정하며, 코드 병합만으로 추가 발급·SA 삭제를 허용하지 않는다.
- PR121 부모 정리와 PR124 계획 실패 정리는 source/session/FD의 소유권을 보존한다. borrowed full plan을 임의로 닫거나 실패를 성공으로 바꾸지 않는다.
- PR120~124 로컬 통합 `b9a975aa`에서 Windows944건(787 PASS/157 SKIP/0 FAIL)을 확인했다. 테스트 의존성 누락·격리 계정 읽기 오류는 해시 고정 PyYAML6.0.3과 사용자 실행 경로로 해결했고 실패 로그도 보존했다. 이후 PR121→122→123→124를 main에 병합해 `49f2ecbe` Linux932건(928 PASS/4 SKIP/0 FAIL), validate/p2-intake2 SUCCESS를 확인했다. 이후 PR120도 양측 담당 범위 승인 후 main `aa64731c`로 병합했다. 이 main과 기존 로컬 통합본의 전체 tree가 일치하고 validate/p2-intake 2건 SUCCESS·Linux944건(940 PASS/4 SKIP/0 FAIL)을 확인했다. 과거 932건은 PR120 제외 당시 범위다. 테스트 fixture는 운영 승인값이 아니다.
- 실제 채택 뒤 수행할 정상 배포·실패 차단·복구/finish 검증은 별도 Runtime 단계다. 기존 수동 창 C 결과와 코드 MOCK/CI를 #46 Runtime 인수로 전용하지 않는다.

## 외부 AI 검토의 반영 범위

Claude Code는 계획 소진/예외·참조 정리, Grok CLI는 #49 시각/수신·편입 판정, Antigravity CLI는 이 표의 입력 흐름을 검토했다. 모두 모델·high를 명시했으며 서버 effort 메타데이터 부재는 별도 기록했다. 실제 원본·자격은 제공하지 않았다. Antigravity의 “6객체=이미지6종” 추정은 기각했다(실제2이미지/6객체). Grok의 미수신을 미생성으로 바꾸는 제안도 채택하지 않았다. Claude의 실제 job 실행 제안은 이번 Runtime 금지 범위에 따라 실행하지 않았다. 이들은 독립 사람 승인 또는 실제 현장 검증을 대체하지 않는다.
