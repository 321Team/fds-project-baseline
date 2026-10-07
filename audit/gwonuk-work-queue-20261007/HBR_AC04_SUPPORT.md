# Harbor AC04 Docker persistence 지원 인계 — 2026-10-07

CODEX_ASSISTED. 이권욱의 infra-ansible#62 지원 범위. #13 이하영 예정 기록6031540537의 source 정합성과 수신 조건을 대조했다. 새로운 Runtime GO/AC 인수가 아니다.

## 새 제출과 판정

Owner는 T0를15:50 이후, APP 실제 종료+10분으로 정하고 T0+5/+20/+30을 먼저 기록했다. 이는 예정이며 시작은 미확인이다.
#10 MTU 종료 보고6031350840와 #19 종료/회복 보고는 원본 검토 범위와 구분하여 비중첩 판단에 연결한다.
APP 종료가 늦어지면 실제 종료+10분과 새 시각 기록이 필요하며 오늘30분을 확보하지 못하면 미실행이다.

Owner 현장 checkout의 신고값 e1c4458cf95dacca76870d7b9b012f8615f6974a와 승인 source61a77ad2f984cbf9e74a95f779691e2831a5a2a6을 GitHub 원본으로 비교했다.
전체24커밋 차이 중 직접 verify playbook·정적 include3개·명시 config/inventory/group vars의 Git blob8/8은 동일하다.
동일 코드 근거 없이 전체 checkout을 main으로 바꾸는 조치를 선행하지 않는다.
runbook은 변경됐고 tools/verification-kit.py 등 다른 도구도 변경되어 저장소 전체/오래된 실행 지침이 같은 것으로 확대하지 않는다.
Docker restart 분기/수동 복구는 최신 v2+기존 GO를 따른다.

## 직접 verify 실행 소스 범위

| 파일 | 두 commit에서 동일한 Git blob | 판정 |
|---|---|---|
| ansible.cfg | 81a71a929087a672c3f432516d1569f4ebbac818 | 동일 |
| inventory/hbr.yml | 07a1628e81449af89cf32d9a40b1a4b306c6a916 | 동일 |
| inventory/group_vars/all.yml | fb5690fc61af8490cbad79e31cbaf7b2575e859a | 동일 |
| inventory/group_vars/hbr.yml | b6882247b83ac624a82282afa877d717c2481e1c | 동일 |
| playbooks/p1-hbr-01-ac04-verify.yml | 378c1c5079486a1d7125b9079a7490c377deb046 | 동일 |
| playbooks/tasks/p1-hbr-01-ac04-observe.yml | 7916834fc8de47a7aabdac2bc28ca4b026987349 | 동일 |
| playbooks/tasks/p1-hbr-01-ac04-forward-observe.yml | 8ad2d61ef71d7ac670ed14b72e36287afa4d88fe | 동일 |
| playbooks/tasks/p1-hbr-01-ac04-nft-verify.yml | ab83b18091e734279a1537cd70d9ebcf456e49c5 | 동일 |

verify의 include는 observe/forward-observe/nft-verify3개로 고정되어 있다. 이 경로는 역할/wrapper를 호출하지 않으며 builtin 모듈을 쓴다.
원래 prestate SHA 봉인검사를 먼저 수행하고 schema3/host/address/contract 결속 뒤 live guard를 검사한다.
같은 tracked Git blob은 현장 수정/추가 파일, ANSIBLE_CONFIG·실제 CLI/extra-vars·Ansible engine·전역 plugin/environment 및 새 서버 상태를 검증한 결과가 아니다.
이 항목들은 기존 시작 Gate에서 실제 상태를 기록한다. 자격정보 원문은 증적에 넣지 않는다.

## 현장 소스 확인 예시 — 읽기 전용, 기존 작업 위치에서만

ansible01 기존 승인 계정의 ~/p1-ans-01, 현재 쓰기 작업 없음, 승인 Git 객체가 이미 로컬에 있어야 한다.
아래는 source 확인 예시이며 실제 Harbor verify/restart를 실행하지 않는다. 기존 터미널의 shell option도 바꾸지 않는다.

~~~bash
bash -c '
approved_hbr_source=61a77ad2f984cbf9e74a95f779691e2831a5a2a6
cd "$HOME/p1-ans-01" || exit 1
git rev-parse HEAD || exit 1
git cat-file -e "$approved_hbr_source^{commit}" || exit 1
git diff --quiet "$approved_hbr_source" --   ansible.cfg inventory/hbr.yml inventory/group_vars/all.yml   inventory/group_vars/hbr.yml playbooks/p1-hbr-01-ac04-verify.yml   playbooks/tasks/p1-hbr-01-ac04-observe.yml   playbooks/tasks/p1-hbr-01-ac04-forward-observe.yml   playbooks/tasks/p1-hbr-01-ac04-nft-verify.yml
rc=$?
printf "VERIFY_SOURCE_DIFF_RC=%s\n" "$rc"
exit "$rc"
'
~~~

RC0은 해당 tracked 실행 파일의 source 정합성뿐이다. RC1/128/기타이면 경로/원인을 보존하고 같은-version 조건을 확인하기 전 시작하지 않는다.
diff 내용·Secret/vars 값 전체를 출력하지 않는다. 이 비교를 환경·계정·host/prestate·Runtime 성공으로 기록하지 않는다.
새 checkout/패치·package 재생성·engine 전환·server 설정 변경을 이 예시로 수행하지 않는다.

## 실제 수신·검증 항목

| 단계 | 기존 GO에서 수신할 원본 | 판정 경계 |
|---|---|---|
| START | exact 계정/host/T0·비중첩/공지·현재10객체·source/작업트리·guard hash/문법/live contract·TLS·실제 .26 negative 경로 | 미충족이면 시작하지 않음 |
| T0 | Docker restart1회의 명령/RC/실제 systemd job·daemon 상태 | CLI timeout은 daemon/job 종료가 아님 |
| +5 | A/B/C/D/E 분기, localhost1514 실제 TCP·logger/IPv4 binding, 허용1회 start/대상별 상태 | 수동 복구 성공을 자동기동 PASS로 쓰지 않음 |
| +20 | guard3rule/6set/hook·fresh Runner.20 TLS200와 .26 새 연결 실패/counter delta·서비스 상태 | timeout·누적counter만으로 DENY PASS 없음 |
| +30 | 잔존·복구/정리·health·실제 종료/인계·원본 hash | 미복구면 사고 인계. 신규 조치 중단·자동 연장 없음 |

E의 guard 재적재는 cdc84effbb370ac394408294e21a4d3cbb67c3d69e93ea53e86667d4326cf5cc 동일1316바이트 파일로 제한된다.
재적재 이후 fresh counter baseline을 사용하고 이전 누계와 연결하지 않는다.
Robot 발급/교체/폐기·임시 .50/.102 제거 HOLD 유지. 이번 지원에서 Harbor/서버 설정은 변경하지 않았다.
원본 편입은 기존 이재환 독립 증적 검토 뒤 각 AC에 대조한다.

## 근거

- Owner 일정: https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-6031540537
- 기존 조건부1회 GO: https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-6030619054
- MTU 종료: https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-6031350840
- GitHub compare: https://github.com/321Team/infra-ansible/compare/e1c4458cf95dacca76870d7b9b012f8615f6974a...61a77ad2f984cbf9e74a95f779691e2831a5a2a6
