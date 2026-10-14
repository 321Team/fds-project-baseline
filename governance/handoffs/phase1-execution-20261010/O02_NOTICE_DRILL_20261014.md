# O02 알림 게시·수신 시험안 — 2026-10-14

CODEX_ASSISTED · 작성 이권욱. **PLAN / RUNTIME NOT_RUN**. 사용자 요청은 시험안 준비와 Harbor 11:20 시작을 고려한 작업창 배정이다. 아래 새 시험 Run 생성·수동 notify·소유 Run 취소는 아직 실행하지 않았고, 이 회차의 실행 허용 및 운영자 가용성 확인 후 수행한다. 새 코드·Workflow·설정·AC 변경은 없다.

## 1. 목적과 기존 실적

[O02](SESSION_AND_HANDOVER.md#o02--runner-두-번째-운영자와-queue알림-운영)의 잔여인 실제 대기 관측→봇 댓글·멘션→운영자 수신·판단→해소 관측을 확인한다. 제2운영자의 공급·인증·회수 실습은 [PR81 회차](https://github.com/321Team/infra-ansible/issues/61#issuecomment-6136928532)로 이미 충족했다. 이번 시험에서 Runner를 다시 공급하거나 완료 CI를 rerun하지 않는다.

- 구현: [infra-ansible PR81](https://github.com/321Team/infra-ansible/pull/81), main `ec15dcbd022942add199a8f4718c0f88105e880e`.
- 원본: [알림 코드](https://github.com/321Team/infra-ansible/blob/ec15dcbd022942add199a8f4718c0f88105e880e/tools/ansible-ci-queue-alert.py), [알림 Workflow](https://github.com/321Team/infra-ansible/blob/ec15dcbd022942add199a8f4718c0f88105e880e/.github/workflows/ansible-queue-alert.yml), [regression Workflow](https://github.com/321Team/infra-ansible/blob/ec15dcbd022942add199a8f4718c0f88105e880e/.github/workflows/ansible-regression.yml), [운영자 카드](https://github.com/321Team/infra-ansible/blob/ec15dcbd022942add199a8f4718c0f88105e880e/docs/runbooks/Ansible-CI-Operator-Card.md).
- 첫 schedule [38383293926](https://github.com/321Team/infra-ansible/actions/runs/38383293926)은 실제 관측 `NO_ALERT / NO_ALERT_NO_COMMENT`. 정상 무발송은 확인됐지만 경고 게시·사람 수신은 입증하지 않는다.
- 기존 [후속 방침](https://github.com/321Team/infra-ansible/issues/61#issuecomment-6137546423)은 다음 업무상 대기를 기다리는 방식이었다. 이번 안은 사용자의 별도 시험안 요청에 따른 **한 회차의 통제된 대기 시험 제안**이다. 실제 장애·업무 지연 또는 정상 regression PASS로 기록하지 않는다. 채택하지 않으면 기존 방침을 유지한다.

## 2. 선택한 방식과 변경 범위

기존 main의 `ansible-regression.yml`을 **새 workflow_dispatch 1회**만 생성한다. 현재 matching Runner가 없는 상태를 확인하고 회차 동안 공급하지 않아 실제 GitHub Job을 queued로 유지한다. Job의 실제 `created_at`에서 10분 경과 후 기존 알림 Workflow의 `notify=true`를 한 번 호출한다. schedule이 먼저 같은 대상 경고를 게시했다면 그 결과를 사용하고 중복 dispatch를 생략한다.

이재환이 자신의 GitHub 알림 화면에서 멘션을 확인하고 #61에 수신·판단을 회신하면, 이권욱이 그 시험 Run만 정상 cancel한다. completed/cancelled 확인 후 기존 알림 Workflow로 해소를 한 번 관측한다. 해소도 schedule 결과가 먼저 있으면 재사용한다.

| 자원/행위 | 상한·경계 |
|---|---|
| 시험 regression Run | 새 1개 / Attempt1. 기존 완료 Run rerun 없음 |
| 수동 알림 Run | 경고·해소 각 최대1개, 총2개 / 각 Attempt1. schedule과 중복 불필요 |
| 직접 게시 | #61에 시험 시작 식별과 종료 결과 각1개. 봇 상태 댓글은 기존 코드가 게시하고 사람이 위조하지 않음 |
| 담당자 회신 | 이재환의 실제 수신·판단1개. 비밀값·토큰 없음 |
| 취소 | 이 회차에 만든 Run ID만. 다른 Run 취소·force-cancel·Runner 제거 없음 |
| 서버/credential | 접속·설치·Runner 공급·token 발급·Secret/RBAC/Harbor/DB 변경 없음 |
| 코드/운영변수 | 기존 승인 SHA·labels·threshold10·recipients·enabled·cron 유지 |

기존 `GITHUB_TOKEN`으로 봇이 게시하고, 관리 PC는 기존 `gh` 권한으로 dispatch/read/cancel한다. 새 PAT는 만들지 않는다. Actions write 또는 Issues write가 없으면 STOP이며 권한을 즉흥 확대하지 않는다. hosted 알림은 정상 실행 시 과거 약10초였지만 시작 지연은 보장할 수 없다. manual notify 두 번의 Job timeout5분 기준 계산상 최대10분의 실행 예산을 고려하며, 기존 다른 CI500분 유보 기준을 실행 전 최신 사용량으로 재확인한다. 이는 자동 비용 상한이 아니다.

## 3. 작업창 — 오늘 10:00~10:45 KST

현재 Harbor 세션 기록은 **DB ~11:15, Harbor H3 11:20부터**, 종료 시각 미확정이다. H3의 45분은 아직 제안 예산이고 H4는 별도다. Harbor가12:05에 끝난다고 가정해 후속 창을 잡지 않는다. 이 시험은 서버 실행이 없어 DB 작업과 기술 자원이 겹치지 않으며, Harbor 시작 전35분을 남긴다. 이재환의 DB 참여 등 **사람의 동시 작업 가능 여부는 별도 확인**한다.

| KST | 작업 | 시간 상한·완료조건 |
|---|---|---|
| 10:00~10:05 | fresh 읽기·참여 확인·시험 예고 | 정확 main, 활성 regression0, matching Runner0, 수신자 가용성·공급 배제 확인 |
| 10:05 목표, 늦어도10:10 | 시험 dispatch1회, Run/Attempt/Job 고정 | 한 개만 식별. API 불명확 시 재요청하지 않고 목록 확인 |
| Job created_at+10분, 대략10:15~10:20 | 임계 대기→경고 notify | 호스트 공급 없이 실제 queued임을 재확인. 10:20 이후 새 경고 dispatch 금지 |
| ~10:30 | 봇 게시·운영자 수신/queue-watch 판단 | 알림 지연·미수신이면 실패/미확인 보존. **10:30에 수신 여부와 무관하게 시험 Run 취소 요청** |
| 10:30~10:40 | 취소 완료·해소 관측·artifact 보존 | terminal 및 시험 queued 부재. 10:35 이후 새 해소 dispatch 금지 |
| 10:40~10:45 | 잔여 시험 Run 확인·마감 | own 수동 notify가 지연 중이면 cancel. 미확정은 인계, 자동 연장 없음 |
| 10:45~11:20 | 여유35분 | 새 O02 시험 없음. 원본 대조 등 로컬 작업만 가능 |

예상 소요는 **30~40분**, 확보 창은45분이다(사전5 + 실제 대기10 + hosted 시작/게시·수신10 + 취소/해소·보존10 + 여유10). API 또는 사람 대기가 길어지면 PASS 없이 종료하며 Harbor 창을 뒤로 밀지 않는다. 종료 시각 도달은 실제 취소 완료의 증거가 아니다.

실행자·회수 담당은 이권욱, 기존 운영 담당·주 수신자는 이재환(`supreme33-kr`), 기존 두 수신자는 `supreme33-kr,GWONUK`를 유지한다. 이재환은 최소10:15~10:30에 자신의 GitHub Notifications를 확인하고 답할 수 있어야 한다. 이번 가용성은 과거 실습 참여로 대체하지 않는다. 동일 시간 CICD PR79 시험은 다른 repo/labels이며 이 안은 해당 서버를 쓰지 않는다. 다만 같은 사람이 즉시 대응할 수 없으면 이 시험의 시작을 보류한다.

## 4. 관리 PC 실행 카드 — 한 단계씩 확인

환경: Windows PowerShell, 기존 로그인된 `gh`, Python3.11+ 및 위 승인 SHA의 읽기 도구. 새 증적 디렉터리에서 명령/rc/KST·UTC를 기록한다. 아래 `<...>`는 직접 조회해 고정할 값이며 빈칸/예시 ID로 실행하지 않는다. 변경 명령은 이 회차 실행 허용 후에만 수행한다.

### A. 시작 전

1. 아래 읽기에서 API 오류·목록 잘림을 0건으로 바꾸지 않는다. 활성 상태 queued/in_progress/requested/waiting/pending 다섯 상태를 각각 확인하고 `total_count`와 목록 길이를 대조한다. main·workflow·vars를 위 값과 비교한다.

```powershell
gh api repos/321Team/infra-ansible/commits/main
gh api repos/321Team/infra-ansible/actions/variables
gh api repos/321Team/infra-ansible/actions/runners
gh api 'repos/321Team/infra-ansible/actions/workflows/ansible-regression.yml/runs?status=queued&per_page=100'
```

나머지 네 활성 상태도 같은 URL의 `status`를 바꿔 읽는다. 기존 main을 변경하지 않도록 조정하고 Ansible Runner 공급·다른 regression dispatch를10:45까지 배제한다. 새 Runner를 막기 위해 labels/설정/서비스를 바꾸지는 않는다. 이 배제를 확보할 수 없으면 시작하지 않는다.

2. #61에 `O02 통제된 수신 시험 / 10:00~10:45 / 새 Run1개, 실제 장애 아님 / 공급하지 않음 / 10:30 취소`를 예고한다. 본문/기존 증적은 수정하지 않는다. 생성 전 Run 목록과 시각을 보존한다.

### B. 실제 대기1개 생성·식별

```powershell
gh workflow run ansible-regression.yml --repo 321Team/infra-ansible --ref main
gh api 'repos/321Team/infra-ansible/actions/workflows/ansible-regression.yml/runs?event=workflow_dispatch&per_page=100'
gh api repos/321Team/infra-ansible/actions/runs/<TEST_RUN>/attempts/1/jobs
```

Run의 event·actor GWONUK·생성 전후 시각·고정 SHA·새 ID가 일치하는 **유일한1개**를 선택한다. 단순 최신 Run을 선택하지 않는다. path는 `.github/workflows/ansible-regression.yml`, Attempt1, Job5labels는 self-hosted/Linux/X64/fds-ci/ansible-isolated, 상태 queued여야 한다. created_at은 Job 값을 사용한다. 생성 응답이 불명확하거나 후보가 여러 개면 추가 dispatch 없이 원본을 조사하고 인계한다. ID가 아직 없는 단계에서 임의 ID 취소는 하지 않는다.

### C. 실제 경고와 사람 수신

Job queued를 매분 읽어 상태를 확인하되 실제 시각을 조작하지 않는다. 기존 [queue-watch](https://github.com/321Team/infra-ansible/blob/ec15dcbd022942add199a8f4718c0f88105e880e/tools/ansible-ci-queue-watch.py)로 정확 Job/HEAD·Runner 상태를 읽고 rc와 JSON을 보존한다. rc2는 대응 필요이지 자동 공급 허용이 아니다.

```text
python -I -B tools/ansible-ci-queue-watch.py --job-id <TEST_JOB> --expected-source-sha ec15dcbd022942add199a8f4718c0f88105e880e --threshold-minutes 10 --output <NEW_PRIVATE_JSON> --strict
```

10분 경과 후 #61에 해당 Job의 봇 경고가 아직 없다면 10:20 이전에 한 번만 수행한다.

```powershell
gh workflow run ansible-queue-alert.yml --repo 321Team/infra-ansible --ref main -f notify=true
```

notify Run도 생성 전후 목록·actor·event·SHA·Attempt1로 정확히 고정한다. schedule은 정상 운영 그대로 두며 앞서 같은 상태를 발송하면 `UNCHANGED_NO_COMMENT`를 중복 방지 성공으로 기록하고 실제 게시한 schedule Run을 연결한다. 경고 관측·봇 댓글 모두 대상 시험 Run/Job이어야 한다. 다른 업무 경고가 섞이면 이 회차를 계속 확대하지 않는다.

이재환 회신 최소 필드: `내 GitHub Notifications에서 받은 시각(KST) / 봇 댓글 URL / 대상 Run·Job / queue-watch 분류·원본 / 이번에는 통제 시험이므로 공급하지 않고 해당 Run 취소로 해소`. 이메일/모바일 push 도착은 직접 확인한 경우에만 기록한다. 링크를 전달받아 댓글만 읽었다면 COMMENT_READ_ONLY이며 멘션 경로 수신 완료로 쓰지 않는다. 수신 지연은 기다린 시간을 그대로 기록한다.

### D. 소유 Run 취소·해소·증적

수신 확인 직후, 또는 늦어도10:30에 다음을 수행한다. 취소 직전에 Run ID·Attempt·SHA·event·소유를 다시 읽는다.

```powershell
gh run cancel <TEST_RUN> --repo 321Team/infra-ansible
gh api repos/321Team/infra-ansible/actions/runs/<TEST_RUN>
gh api repos/321Team/infra-ansible/actions/runs/<TEST_RUN>/attempts/1/jobs
```

API 접수 성공만으로 정리 완료로 쓰지 않는다. completed/cancelled와 시험 Job terminal을 확인한다. 이후10:35 이전에 아직 해소 알림이 없다면 C의 동일 notify 명령을 **해소용 새 Run1회**로 실행한다. 경고 때의 Run을 rerun하지 않는다. 종료 전 own 수동 notify가 queued/in_progress면 그 ID만 정상 cancel하고 terminal을 확인한다. 기존 schedule/다른 Run은 취소하지 않는다.

경고·해소 Run/Attempt/HEAD/Job, raw 관측 JSON, artifact ZIP의 API digest와 내려받은 SHA256, 내부 JSON sidecar, bot 댓글 URL/작성 시각, 실제 수신 회신, 취소 전후 REST 원본·rc를 새 로컬 디렉터리에 보존한다. 기존209/210·sources/sealed는 변경하지 않는다. 실제 증적 중앙 편입이 필요하면 기존 규칙대로 별도 독립 검토하고, 계획 PR을 증적 PR로 바꾸지 않는다.

## 5. 중단·예상 밖 실행·판정

- main/vars/labels 불일치, API 실패·잘림, 참여 불가, 기존 활성 Run·matching Runner 발견은 dispatch 전 STOP. 최신값 확인 없이 기존 관측을 재사용하지 않는다.
- 생성 후 unexpected in_progress/Runner ID 배정이 보이면 즉시 이 시험 Run만 정상 cancel하고 소유 Runner·Job을 기록한다. 다른 세션 Runner를 kill/delete하지 않는다. 서버 미실행을 더는 주장할 수 없으므로 해당 운영자에게 원본을 인계하고 정리 확인까지 NOT_CONFIRMED로 남긴다.
- 경고/수신/취소/해소 timeout, POST 응답 불명확은 추가 dispatch·재시도 없이 readback한다. 10:40까지 terminal 미확인은 이권욱에게 정확 ID·상태·마지막 오류를 인계한다. 강제 취소·권한 변경·새 공급으로 해결하지 않는다. 미확인 리소스를 방치한 채 정리 PASS를 선언하지 않는다.
- 실제 알림 엔진은 합성 입력을 받지 않는다. fake clock/가짜 bot marker/Run·Job·수신 시각 조작으로 시험하지 않는다. 봇 원문은 운영 코드 그대로이며 시작·종료 기록에서 통제 시험임을 명확히 한다.
- 기존 CI500분 유보를 훼손하거나 Harbor/DB 대응 인력이 겹치면 새 시험을 시작하지 않는다. 예정창이 지나면 자동 연장·재시도 없이 재배정한다.

| 판정 | 필요한 실제 근거 |
|---|---|
| ALERT_DELIVERY_VERIFIED | 실제 queued10분 + 해당 Job ATTENTION + bot COMMENT_POSTED·기존 멘션 + 이재환의 알림 화면 수신·판단 회신 |
| CLEANUP_VERIFIED | 소유 시험 Run/Job terminal + own 수동 notify terminal + 시험 Job 대기 부재. 공급·서버 실행0은 별도 사실 확인 |
| CLEAR_OBSERVED | 경고 이후 정상 읽기의 해소 상태와 봇 해소 댓글. 다른 업무 대기가 있으면 전체 NO_ALERT를 요구하거나 조작하지 않음 |
| 전체 O02 | 기존 제2운영자 실습·이번 한정 결과·운영 조건/한계를 연결해 기존 책임 범위에서 판정. 자동 Close 없음 |

수동 notify는 **실제 production 알림 엔진·게시·수신 경로**를 검증하지만 cron 시각 준수/연속 운영/야간 감시/SLA를 검증하지 않는다. 기존 schedule 실행 증적과 분리해 기록한다. 취소된 regression은 CI PASS가 아니고 기존 PR81 CI 성공을 대체하지 않는다. O02/#61 전체 AC나 C01 인수를 이번 결과 하나로 완료 처리하지 않는다.

## 6. 검토·채택 및 출처

문서 전용 제안으로 동일 코드 전수 재리뷰·새 공통 Lead GO를 요구하지 않는다. 기존 운영자 이재환에게 통제 시험 수용 여부와10:15~10:30 수신 가용성만 요청한다. 사용자의 이 회차 변경 범위 허용은 별도 기록하며, 계획 작성 요청을 runtime dispatch 허용으로 확대하지 않는다. 검토 또는 가용성 확인이10:00까지 끝나지 않으면 새 시험을 시작하지 않는다.

- [수동 Workflow 실행](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow): default branch의 workflow_dispatch와 저장소 write 필요.
- [Workflow Run 취소](https://docs.github.com/en/rest/actions/workflow-runs#cancel-a-workflow-run): 소유 Run을 특정해 취소하고 실제 종료 readback.
- Harbor 근거: 같은 프로젝트 `deliverables/p1-preapply-resume-20261012/PR62_H6_EXECUTION_20261014/H3_START_AVAILABILITY_20261014.md` 및 `H3_H4_NEXT_EXECUTION_CARD.md`의2026-10-14 08:52 KST 변경. H3 시작11:20, DB11:15까지, 종료미확정·45분후보·H4별도.
- 준비 시 조회: Ansible main 위 SHA, Runner0, enabled=true/threshold10/수신자2명. 이는 실행 직전 preflight를 대체하지 않는다.
