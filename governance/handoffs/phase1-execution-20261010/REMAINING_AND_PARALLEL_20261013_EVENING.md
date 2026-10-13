# Phase 1 잔여 작업과 병행 착수 — 2026-10-13 저녁

이권욱 / CODEX_ASSISTED. 사용자 최신 지시의 범위는 **Phase 1**이다. baseline `c5c854efe3572f65bb2ef7b23dd32b61b7291e8e`, CICD `fadc07f18b5bf7febc8cf601fa138d8f35e9ccb4`. 티켓·리뷰·병합 및 GitHub 실행 준비 메타데이터 조회 기준은 18:54~18:57 KST다. 이후 사용자 승인에 따른19:15 TBS 시도와 결과는 §5에 추가했다. 초기 준비 시점과 실제 실행 결과를 구분한다.

기존 [병행 실행안](PARALLEL_EXECUTION_20261013.md), [최소 검증안](MINIMUM_VALIDATION.md), [APP·HA 카드](APP_HA_EXECUTION_CARD_20261013.md), [운영 인수 카드](SESSION_AND_HANDOVER.md)를 재사용한다. 과거 실행창·미실행 표기를 현재 승인/상태로 재사용하지 않는다. AC·책임자·일정·정본·Status/종결은 변경하지 않는다.

## 1. 잔여 목록

| 묶음 / 기존 책임 | 완료되어 다시 대기하지 않을 것 | 실제 잔여 / 완료조건 |
|---|---|---|
| APP·Delivery #15/#16 / 이재환·이권욱 | [PR76](https://github.com/321Team/infra-cicd/pull/76)·[PR77](https://github.com/321Team/infra-cicd/pull/77) 독립 승인·병합, 결합 main [CI SUCCESS](https://github.com/321Team/infra-cicd/actions/runs/38376834597), [실패·복귀 증적213](https://github.com/321Team/fds-project-evidence/pull/213) 병합 | 19:15 새 Run은 Source fetch exit128로 TBS 전 중단. 소스 접근 확인/복구 → 별도 새 TBS 회차 → 새 Push → 새 Deploy. 실패 차단·source→Harbor→manifest→Pod 대응 및 Delivery 인수 |
| HA·최종 회귀·DB #22/#20/#11 / 이재환 | 기존 앱 분산 복구·DR R02 인수, DB 증적211·요구별 대조 | 최종 배포 형상 → 허용된 최소 Worker Drain/복귀 → 최종 HTTP/Rule/DB/metrics 회귀 → DB 인수 판단. 실제 실행 범위/창은 별도 |
| Harbor #13 / 이하영 | r5 주소 정리, manager15파일 설치, 활성화 실패 후 허용된 정책 원복 | CLI/manager 쓰기 환경·SELinux lock 라벨 정합화와 실제 생성/readback → manager 재활성화 → H6/재시작·복구/로그·인수. 실패 Store/claim 보존 |
| K8S·ICR·SEC #10/#14/#19 / 이하영·이권욱 | K8S17파일 교체/보존28·OID02 반입·IF06B 관측, 증적207/208 | 실제 도구 호출·정책 rollback, 미입증 Allow/Deny, AC4c/d②/g·T14/T15, OID03·부팅 연속 보호·복합 AC 최소 보완 또는 유효한 처분 |
| MON·관리 접근 #17/#19 / 이재환·이하영, 보관/회수 이권욱 | MON23/23·Grafana 조회 증적212, 보관·회수 책임 확정 | 실제 인수·회수, 접근 배타성·감사 공백 처분, 필요한 Probe·최종 인수. 책임자 확정을 Secret 수령/회수 완료로 표시하지 않음 |
| Runner·운영 문서 #24/Ansible61 / 이권욱, 운영 추적 이재환 | O02 제2운영자 실습/정리·알림 활성화·증적209/210 | 첫 schedule/실제 알림 수신·처리, O01 제3자 핵심 Runbook 재현, As-built/Test/Evidence/Runbook/Known Issue·DOC Freeze |
| Ansible9 / 이권욱 | worker02 prepare/apply/reapply/동일값 rollback·증적208 | 다른 role·운영 wrapper/venv 전환·복귀·엔진 전체 인수. 원본=목표 회차는 장애 복원·재부팅 지속성 입증 아님 |
| G1/G2/G3·Review/Close #18/#23/#29~32 / 기존 Lead 유지 | 개별 완료·유효 처분 재사용 | 필수 하위 AC·증적·미결 처분 → 문서 Freeze/Review → Sign-off. PR 병합만으로 Gate 완료 금지 |

[DR #21](https://github.com/321Team/fds-project-baseline/issues/21)은 인수·종결을 유지한다. D01 두 사본의 한시 보존·삭제 조건과10/26 재점검은 자동 삭제 허가가 아니다. W4 전체 HTTP5xx `NOT_MEASURED`, C01 승인 인원 접근 사용자 확인과 직접 실효 ACL `NOT_VERIFIED`를 구분한다. #25~27은 기존 Phase2 이월 결정의 P1 우선순위 항목이며 현재 Phase1 P0 필수 차단으로 합산하지 않는다.

## 2. 병행할 준비와 직렬로 실행할 변경

| 병행 묶음 | 지금 가능한 준비 | 실제 변경 시 중첩 금지/의존성 |
|---|---|---|
| A. 이미지 공급·배포 | 승인 source/config/검사 코드 pin, 새 빌드 카드, Push/Deploy 인계 필드 | 동일 Runner 중복 작업·이전 출력/claim 재사용 금지. Push/Deploy는 Harbor 변경·사후 관측과 비중첩 확인 |
| B. Harbor 복구 | 최신 실패/원복 기록과 실행 환경·label/readback 계획 검토 | manager/H6·Docker/VM 재시작을 APP Push/Deploy/회귀와 동시에 수행하지 않음 |
| C. K8S·SEC·MON | 기존 AC별 재사용/미검증 행, 관리 접근·감사 처분 준비 | 앱 회귀·HA와 정책 변경/노드 재부팅/Probe 장애 주입을 중첩하지 않음 |
| D. 운영 인수·문서 | O01 대상·제3자 적격성/접근·원복 조건, Runner schedule 읽기 확인, 증적 목록 | O02를 O01로 대체하거나 알림 수신을 합성 dispatch로 대체하지 않음 |

Harbor manager/H6 미완료 자체를 새 Delivery Gate로 추가하지 않는다. Registry 서비스 사용 가능성·변경/사후 관측 비중첩은 실행 직전에 확인한다. 문서/조회 병행과 실제 서버 변경의 동시 실행은 구분한다.

## 3. 새 Test/Build/기동/Scan 실행 준비 카드

| 항목 | 확정된 입력 / 이번 읽기의 한계 |
|---|---|
| 대상 | `cicd-runner01/server01_cicd-runner`, UID1000, 기존 rootless Podman. 18:57 GitHub 조회 online·busy=false는 서버 파일·공간·서비스 전수 검증이 아님 |
| 소스 | CICD `fadc07f18b5bf7febc8cf601fa138d8f35e9ccb4`, APP 승인 `affbc69beef9967f7977d09a6fec14f7fb6c0e94` 및 [APP27 승인](https://github.com/321Team/fds-msa/pull/27#pullrequestreview-5465278143). APP 최신 main으로 자동 교체하지 않음 |
| config | `config/app-build-scan.json`, schema3, SHA256 `72eb52594048aa713ade12621f4545def0395f3f1603adec7bab3385b24f13e3` |
| workflow | `.github/workflows/app-test-build-scan.yml`, SHA256 `40a5dcd56b0bb6feb816bb297eb27bb747524181e914dcf514d614492ace2982`. dispatch가 실제 실행이며 `execute=false` 입력 없음 |
| 인증 | `CICD_APP_SOURCE_READ_TOKEN` 등록 존재만 조회. Secret 값 조회/재등록/회전·실제 인증 검증 없음 |
| 공급 | config의 affbc69 공급 경로·manifest·tool pin 유지. 원본 재수집/덮어쓰기 없이 회차에서 실제 바이트·권한 검사 |
| 이력 | TBS 최신 Run은10/9 `37890963668`; 병합 후 새 TBS 없음. 과거 결과/이미지를 수정본 빌드로 재사용하지 않음 |
| 단계 | source/config/workflow/기동 코드6파일의 Git blob·SHA256 확인, STATIC/메타데이터 READ 완료. 새 TBS/기동/Scan/Push/Deploy NOT_RUN |

**제안 범위:** 새 TBS Run1회로 기존 두 앱의 Test → Build/save → 비루트 기동·파일 읽기·listener 분리 → Scan·증적 보존을 확인한다. Push·Deploy·Token 발급·HA/재부팅·DB 변경·Harbor manager 변경은 포함하지 않는다. 실패 시 자동 rerun 없이 출력·로그·CID/정리 상태를 보존한다.

**사용자 승인·해당 1회 소진.** [승인 기록](https://github.com/321Team/fds-project-baseline/pull/168#issuecomment-6143263724)에 따라 아래 창에서 새 Run을 실행했고 Source fetch 실패로 종료했다. 기존17:00 Deploy 창과 추가 Run, 이번 창의 남은 시간을 재실행 허가로 사용하지 않는다.

**승인된 이번 회차 창:** 2026-10-13 **19:15~22:40 KST**, 실제 Job 시작 마감 **19:25 KST**, TBS1회·자동 재실행 금지. 최종 시작부터180분 및 결과/정리15분을 확보한 범위로 사용자 승인됐다. 19:25까지 선행조건/실제 시작을 확인하지 못하면 실행하지 않고, queued 상태면 취소한다. 22:40은 수집/정리까지의 종료 상한이며 실행 중 오류·종료 초과 위험에는 추가 단계 중단·원본/소유 자원 상태를 인계한다. 창 경과를 자동 연장으로 처리하지 않는다.

1. 확정 창에서 main/config hash, 실제 계정/UID·동시 작업 부재·공급물/공간/Podman·정상 인증을 재확인한다. 필요한 영향 범위만 재검증한다.
2. 기존 main의 `app-test-build-scan.yml`을 신규 Run1회 시작하고 actual Run/Attempt/Job·source·시각을 결속한다. 별도 자동 dispatch 코드를 추가하지 않는다.
3. [병합된 검사](https://github.com/321Team/infra-cicd/blob/fadc07f18b5bf7febc8cf601fa138d8f35e9ccb4/docs/final-image-startup-gate-20261013.md)의 UID10001/GID999, network=none/read-only/cap-drop, 실제 `/app` 읽기, 업무/metrics listener 검증을 두 이미지 각각의 archive/config/manifest와 결속한다.
4. 두 서비스 기동 PASS·자기 CID 정리 후 Scan 진행을 actual result/steps로 확인한다. 실패/timeout/cleanup 불확실/해시 변경이면 후속 Scan/Push/Deploy STOP. 원본/claim 삭제·자동 재실행 없음.
5. 성공한 새 Run/context·OCI/archive/config/manifest·Scan·로그/정리 receipt를 다음 Push 입력으로 넘긴다. 아직 없는 digest·Run·승인값은 채우지 않는다.

이 검사는 제한된 이미지 기동 검증이다. DB readiness·앱 거래·운영 NetworkPolicy·Kubernetes Runtime·APP/E2E 인수는 별도다. 실패를 피하려고 UID·SELinux·CA·방화벽 등을 완화하지 않는다. 실제 환경이 예상과 다르면 원본을 남기고 해당 회차를 중단한다. 현재 앱을 변경하지 않는 빌드 단계의 실패를 운영 앱 롤백으로 처리하지 않는다.

## 4. 최종 회귀와 운영 인수의 준비

새 TBS → 새 Push/원격 digest/정리 → fresh Deployment·SA·CA·복귀 image → 새 plan UUID·actual 창/복귀 범위 → Deploy → 최소 Worker HA/복귀 → Final Regression → DB 최종 판단 순서다. 기존 claim1/checkpoint9·실패 원본은 보존한다.

- HA: 기존 APP·HA 카드/V07의 Worker 단일 회차·PDB/local PV·오류/관찰 기준 유지. 전수 reboot·control01 drain을 추가하지 않음.
- 회귀: V08의 criteria/fixture, 새 RUN 사전 DB0행, 유효22건 및 I01 분기 유지. I01이201이면23행·save/evaluated+23,422이면22행·+22. 도구 pin과 앱 source를 분리하고 동일 최종 형상·RUN·HTTP/Rule/DB/metrics·KST/UTC 원본으로 연결.
- 복귀: 이전 이미지의 업무 포트 metrics 노출도 복원된다는 한계를 기록. Ready만으로 업무 E2E·보안 인수를 선언하지 않음. 복귀/정리 조건 상실 시 추가 변경 중단·실제 상태/원본 인계.
- O01: 기존 카드의 적격 제3자·핵심 대상·정상 접근·원복·실제 명령/rc·원본·정리를 충족해야 함. 새 참여자/일정을 임의 확정하지 않고 해시 확인을 전체 재현으로 집계하지 않음.
- Runner: 18:55 GitHub schedule 조회0건. 이재환의 [기존 추적 계획](https://github.com/321Team/infra-ansible/issues/61#issuecomment-6140626975)을 유지하며 완료 CI rerun·수동 notify로 대체하지 않음. 조회0건의 원인은 이번에 확인하지 않음.

최초 준비 단계의 수행은 읽기 검증·실행 카드/병행 목록·[6개 티켓 잔여 현행화](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6142901586)다. 실제 파일 배치·dispatch·권한 변경·서버 시험·인수/종결은 하지 않았다. 이 문단까지는 최초 준비 이력이다. 이후 승인된 실행 결과와 현재 다음 조건은 §5를 따른다. Push/Deploy는 성공한 새 결과 수신 뒤 정확한 입력으로 판단한다. 이미 채택한 W4·C01 확인·보관 책임자는 다시 질문하지 않는다. 문서 복구는 변경 커밋 revert다.

## 5. 승인된 TBS 시도와 현재 차단사항 — 19:15~19:17 KST

[Run38382090974/Attempt1](https://github.com/321Team/infra-cicd/actions/runs/38382090974), Job115244770236이19:15:23 시작해19:15:34에 FAILURE로 종료했다. source/config/Runner는 승인값과 일치했고 `SOURCE_PRIVATE_FETCH_FAILED`(Git exit128)로 Test/Build/기동/Scan에 도달하지 못했다. **새 이미지 성공 여부는 미검증**, Push·Deploy는 미실행이다. [증적 PR215](https://github.com/321Team/fds-project-evidence/pull/215)는 실패 원본 편입·독립 검토 대기이며 성공 증적이 아니다.

- 서버 result·원본 manifest·source 단계 로그와 GitHub Run/Job 로그를 수신해 해시를 대조했다. handoff/build-scan 디렉터리 없음·사후 Worker0을 확인했다. 서버 원본은 보존했고 자동 재실행·Token 발급·Secret 변경은 하지 않았다.
- GitHub에 전용 Secret이 등록돼 있고 문자열 형식 검사는 통과했지만, 실제 권한/만료/조직 승인·401/403 등 실패 원인은 미확인이다. 검토된 코드가 인증 원문을 폐기하므로 exit128만으로 만료라고 단정하지 않는다.
- 읽기 후속 확인에서 Runner DNS·TLS·github.com HTTP200, 익명 Private Git endpoint401을 확인했다. 익명401을 실패한 인증 fetch의 응답으로 인용하지 않는다. 승인 Source Commit은 별도 워크스테이션 인증 경로에서 존재를 확인했다.
- **다음 선행조건:** 기존 발급·관리 경로에서 `CICD_APP_SOURCE_READ_TOKEN`의 대상321Team/fds-msa·Contents Read-only·유효 기간·조직 승인 확인 및 필요한 최소 조치 → 새 Run 수/창 결정. 토큰 값·hash·화면을 채팅/기록으로 받지 않는다. 일반 사용자 gh 인증이나 과거 checkout으로 우회하지 않는다.
- Runner schedule 읽기 조회는19:12에도0건이다. 기존 이재환 추적 계획은 유지한다. Harbor/SEC/MON의 문서·증적 대조와 O01 준비는 소스 접근 차단과 독립적으로 진행할 수 있으며 실제 인수 완료는 아니다.

이번 작업의 완료 범위는 Phase1 잔여 목록·6개 티켓 현행화, 승인된 TBS1회 시도·실패 원본 회수, 읽기 원인 분리와 증적 PR 준비다. 현재 잔여 순서는 **소스 접근 → 새 TBS → Push → Deploy → 최소 HA/복귀 → 최종 앱 회귀 → DB 판단 → DOC/Review/Sign-off**다. W4·C01·DR 기존 처분과 담당자/AC/Status는 유지한다.
