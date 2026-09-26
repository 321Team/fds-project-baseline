<!-- lb-pr10-review-response-20260924:issue-9:start -->
## PR10 독립 리뷰 대응 — 2026-09-24 KST

[이하영 독립 리뷰](https://github.com/321Team/infra-lb/pull/10#pullrequestreview-5301172238)가 **HOLD(CHANGES_REQUESTED)** 판정과 함께 2건을 지적했다. HAProxy `inter 2s fall 3`의 DOWN 판정 지연과 관측기의 "API 표본 1회 실패 즉시 STOP" 로직이 어긋나 정상 전환에서도 PASS_CANDIDATE 도달 확률이 낮다는 지적(리뷰어 추정 ~6%), 그리고 장애·복구 후 최소 잔여 작업창 검사가 150초로 실제 필요(160초)보다 10초 부족했다는 비차단 지적이다.

- **HEAD `2324388`**: `maximum_failed_samples`(1~20)·`maximum_continuous_failure_seconds`(1~30) 두 필드를 실행 입력에 **필수**(기본값 없음, Lead가 매 실행 확정)로 추가하고, 관측기(실시간)와 `run_stageb.py`의 분류 로직(원본 표본 재계산, 사후 이중 확인) 양쪽에서 동일 기준으로 판정하도록 수정했다. HAProxy 설정(`option redispatch`/`retries`)은 변경하지 않았다. 작업창 최소 잔여시간도 `165`초로 정정했다.
- **HEAD `909ed87`**: 실행 입력 스키마 두 개(`templates/EXECUTION_INPUTS.json` 상위 계획 체크리스트, `tools/stage-b/ansible/inputs.example.json` 실제 Ansible Runtime 입력)의 필드명이 달라 혼동 가능성이 있어 상호 참조만 추가. 판정 로직·값 변경 없음.
- `tools/stage-b` 전체 단위 테스트 **72/72 PASS**(native kubectl 미설치로 3건 skip은 기존과 동일), `sha256sum --check SHA256SUMS` 전체 PASS. 서버 실행·장애 주입은 수행하지 않았다.
- 이하영에게 새 HEAD `2324388` 기준 재검토를 요청했다. 재검토·병합·실제 장애 주입은 모두 미완료다.

**남은 순서**: PR10 재검토(이하영) → Lead 병합 판단 → `maximum_failed_samples`/`maximum_continuous_failure_seconds` 실제값 확정(Lead 판단) → ansible01→LB SSH 접근 확인(`run_stageb.py --check-access`) → `runtime-inputs.json` 나머지 필드(KST 작업창·OOB 참조 등) 확정 → 실제 장애 주입 실행 → 재부팅 지속성 시험 → LB-A-01 잔여 인수 조건 해소 및 최종 Handoff. 기존 담당·일정·상태·AC 체크는 유지한다.

<!-- lb-pr10-review-response-20260924:issue-9:end -->

---

<!-- lb-stageb-readiness-20260924:start -->
## 2026-09-24 KST — 복구 증적 보완 및 읽기 전용 잔여 점검 준비

- [infra-lb PR10](https://github.com/321Team/infra-lb/pull/10) 최신 HEAD `f71e5c8eb298473c7fcb13d2feb514d7ceafc4b1`. 수동 cleanup의 COMMANDS.json 소실을 재현/수정하고 누적 counter 중복·잘못된 nft table JSON 판정을 보완. Runtime v1.0은 v1.1로 대체.
- 전체 단위/native parser67건 PASS. 실제 Ansible 엔진의 inline LB1대 파싱 확인. 기존 조정 mock3건은 YAML 변경 없어 재사용. 운영 SSH/nft/장애/복구/CI는 미실행.
- [실행 전 점검 가이드](https://github.com/321Team/infra-lb/blob/f71e5c8eb298473c7fcb13d2feb514d7ceafc4b1/docs/runbooks/STAGE_B_READINESS_20260924.md): ansible01에서 기존 계정/키의 LB identity 조회, LB에서 nft --check+전후 stateless 비교. 별도 inventory 파일 없이 접속 가능 여부부터 확인하며 키·권한·known_hosts·저장소 inventory는 변경하지 않음. CP API 원본은 재사용.
- 읽기 전용 ZIP 및 외부 hash 준비. 현장 결과 archive/sidecar 총4개 수신 대기. Runtime용 연결 입력·작업창/OOB는 아직 미확인.
- 최신 GitHub 리뷰0/미병합. 수정 후 exactSHA 독립 리뷰와 Lead 병합/실행 판단이 남음. 실제 StageB·재부팅 지속성·LB-A-01·Handoff/AC는 미완료. 기존 담당/일정/상태/AC 체크 유지.

<!-- lb-stageb-readiness-20260924:end -->

<!-- lb-stageb-runtime-20260924:start -->
## 2026-09-24 KST — Stage B 실행 코드 검토 후보 작성

- 기존 LB05:10 / 인증 API05:44 원본 PASS에 이어 [infra-lb PR10](https://github.com/321Team/infra-lb/pull/10)에 **LB 단일 .104:6443 경로 주입·복구 및 Ansible CP 연속 관측**을 구현.
- exact HEAD: `eec6383be564d953ece55bf08c90aaeb829161ea`. CP 변경 없음. 새 성공 표본 lease10초, nft set최대60초 만료, 본 run marker 테이블 회수, 실제 DOWN/다른2UP/3UP 회복 및 인증 GET 표본 보존.
- Python/native-parser57건·실제 Ansible coordinator+로컬 mock3건 PASS. CI/nft native/kernel/현장 장애 Runtime은 NOT_RUN. 테스트 성공은 StageB/AC 인수 아님.
- PR10의 현재 분류는 **Runtime 코드/Pre-check 혼합**. REVIEW/MERGE 미완료. 현재 정책 §3/3.2에 따른 exactSHA 독립 리뷰·Lead 병합/실행 판단 필요.
- 현장 미확인: ansible01의 승인된 LB SSH/inventory/sudo 접근, .104 시험 선택·KST 작업창·OOB. 기존 inventory에 LB가 없어서 접근 권한을 있다고 가정하거나 새 키/권한을 생성하지 않음.
- 전달 검토 ZIP `FDS_P1_LB_01_StageB_Runtime_Review_20260924_v1.0.zip` 및 외부 sha256, ZIP SHA `bd5c70063fbbf9142b9b974cd12684f561c819bee26d48e2c38c57ddf9111f3f`.
- [실행·중단·회수 원문](https://github.com/321Team/infra-lb/blob/eec6383be564d953ece55bf08c90aaeb829161ea/docs/runbooks/STAGE_B_RUNTIME_20260924.md). 실제 장애/복구 시험·재부팅 지속성·LB-A-01/최종 Handoff 잔여. 기존 담당·일정·상태·AC 체크는 유지.

<!-- lb-stageb-runtime-20260924:end -->

<!-- lb-api-precheck-20260924T0544:start -->
## 2026-09-24 사전점검 완료 — LB 및 인증 API

[infra-lb PR10](https://github.com/321Team/infra-lb/pull/10)에 이번 현장 수신 판정을 연결했습니다. **사전점검 PASS이며 단일 backend 장애·복구 및 최종 인수는 미완료**입니다.

- **LB 05:10 KST:** backend3UP/L4OK, .109 출발 CP3대 TCP6443 성공, 설정/PID/서비스 전후 일치, firewalld/nft context 수집. 원본 `FDS_P1_LB_01_INJECTION_CONTEXT_20260923T201002Z_uplc2poj.tar.gz`, SHA256 `40cc4ce3184ebe1a5430842e0510eaa18a7ae4dca2b3ba165c8d981d9229d1e6`, manifest73개 확인.
- **API 05:44 KST:** ansible01 → control01(svc_ansible)의 기존 권한으로 LB `https://10.1.93.109:6443` 검증. TLS/IP SAN 유지, identity=`kubernetes-admin`, NodeList 정확한6대 Ready, readyz=`ok`, 명령7/7 rc0·stderr공란, 전후 route 동일. 외부 manifest8개와 중첩CP20개 확인.
- API 원본 `FDS_P1_LB_01_ANSIBLE_API_20260923T204452Z_qtbr72yi.tar.gz`, SHA256 `473b4e2f24308302c90e7256e5f917d1500f649f93e0d08b481e84cc41e1d9db`.
- 소스 `fc477bc1f47834b88d29f1c5d01e1d2629de84ab`, 실제 kubectl v1.36.4. 05:32의 Go-template 파싱 결함은 수정 후 현장 해소 확인. 이전 실패 원본 보존. Ansible dispatcher는 전달 묶음의 별도 source/hash로 추적.
- 두 자료는 서로 다른 시점의 짧은 사전점검이다. 장애 중 API 연속성·3UP 복구·지속성 또는 독립 REVIEW/MERGE/AC 인수를 뜻하지 않는다.

**다음 잔여:** LB .109에서 단일 backend(.104:6443 후보) 경로 장애 → 자동 DOWN 탐지 → control01 인증 API 표본 연속성 → 임시 객체 회수와3UP 회복. 정확한 주입/회수·관측 코드 및 해당 source 검토, 작업창·OOB 입력을 고정해야 합니다. CP Calico/서비스/etcd/VM을 변경하지 않습니다. 기존 Stage A/Join/DAD를 반복하거나 ICR 전체 종결을 새 선행조건으로 추가하지 않습니다.

기존 담당·일정·AC 체크·In Progress를 유지합니다. 이번 갱신은 제출 원본의 검토 기록이며 검토자의 서버 재실행/장애 주입이 아닙니다.
<!-- lb-api-precheck-20260924T0544:end -->

---

## LB 후속 전수 검수 — 2026-09-23 KST

[통합 대조표](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5794357232). 기존 성공 증거를 유지하고 남은 Stage B를 구분한다.

- **완료 유지:** Stage A Listener/Source Allowlist·수신 기록, 9/18 backend 3/3 UP/L4OK 및 LB→CP TCP 3/3, 9/21 LB 경유 API 복구 증거를 재사용한다.
- **이관/리뷰 진행 완료:** infra-lb [PR2](https://github.com/321Team/infra-lb/pull/2)·[PR3](https://github.com/321Team/infra-lb/pull/3)는 독립 승인·병합 완료다. 옛 “이관 PR 검토 대기”는 현행 차단이 아니다. PR3의 9/17 CP2/3 미준비 기록은 9/18 정상화보다 앞선 증거이며 새 장애로 판정하지 않는다.
- **실제 잔여:** backend 1대 장애 자동탐지 중 인증 API 연속성 → 복구 → backend 3/3 회복 증거, 최종 Handoff 인수 및 지속성 확인. 기존 도구/원본을 활용하고 Join·Stage A 전체 시험은 반복하지 않는다. 이번 검수에서는 장애 주입이나 서버 재시작을 실행하지 않았다.
- **MON 연계:** in-cluster 스택은 9/22 배포됐으나 monitor01의 IF-06A Blackbox와 IF-06B receiver/TLS 현장 인수는 별도 잔여다. 이를 LB 전체 후속의 새 선행조건으로 만들지 않는다.
- LB 실행·증적은 이권욱의 기존 범위, 최종 인수/관련 정책은 기존 Review Owner와 연결한다. 담당·일정·상태를 유지한다.

---

<!-- icr-management-recovery-20260921T140152:issue-9:start -->
## CP 복구 후 LB 후속 검증 범위 — 2026-09-21 14:01 KST

[ICR 원본·검증](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5755742235)에서 노드6대의 TCP10250 규칙13개 추가 영구 저장과 직접 CP API3×etcd Pod3의 관리 기능27/27 성공을 확인했습니다. 13:14 etcd health3/3 및 leader control03 관측도 [K8S #10](https://github.com/321Team/fds-project-baseline/issues/10)에 반영했습니다. 해당 관리 경로의 No route to host 차단은 시험 범위에서 해소됐습니다.

이번 시험은 직접 API .102/.103/.104 경유이며 LB .109를 경유한 새 시험이 아닙니다. 기존 9/18 backend3/3 증거와 9/21 12:16 LB readyz·12:33 Worker→LB TCP 결과를 유지합니다. 현재 HAProxy stats/backend 상태, 단일 backend 장애 중 인증 API 연속성·복구 및 재부팅은 별도 잔여입니다. HAProxy 설정 변경이나 해당 AC의 추가 완료 처리는 없습니다. ICR 전체 종결을 LB 후속의 새 선행조건으로 추가하지 않습니다. 기존 담당·일정·마일스톤·상태·AC 체크 유지.
<!-- icr-management-recovery-20260921T140152:issue-9:end -->

---

<!-- api-network-recovery-20260921T1240:issue-9:start -->
## LB 경유 API 회복 확인 — 2026-09-21 12:16~12:40 KST

사용자 실행 자료에서 12:16 CP1→LB 10.1.93.109:6443 readyz ok/RC0, CP3대 직접 및 Service API readyz도 성공했습니다. 12:33 Worker3대→LB TCP 모두 성공(같이 조회한 CP3대/Service 포함 총15/15 TCP 성공). 12:40:18 LB를 지정한 조회에서 노드6/6 Ready를 확인했습니다.

[복구 규칙 상세: K8S #10](https://github.com/321Team/fds-project-baseline/issues/10). CP 간 TCP2380/6443와 Worker→CP TCP6443의 /32 제한 규칙을 Runtime/Permanent에 저장했습니다. 이번 안내에는 HAProxy 설정 변경이 없습니다.

현재 LB stats의 backend3/3, 장애전환·연속성·재부팅 후 유지 시험은 미수행입니다. readyz/TCP 성공을 해당 AC의 PASS로 대체하지 않습니다. 실제 MON sender namespace는 부재로 확인되어 [MON #17](https://github.com/321Team/fds-project-baseline/issues/17)의 준비 작업에 연결합니다. 담당·상태·일정·기존 AC 체크 유지. 아래는 각 시점 이력.
<!-- api-network-recovery-20260921T1240:issue-9:end -->

---

<!-- cp23-etcd-recovery-20260921T1014:issue-9:start -->
## CP2/CP3 peer 단절 확인·Runtime 복구 준비 — 2026-09-21 10:14 KST

추가 로그에서 CP2·CP3의 etcd 실행/CrashLoopBackOff와 양 peer TCP2380 연결 실패, 합의 기반 읽기 실패/readyz503을 확인했습니다. [K8S #10](https://github.com/321Team/fds-project-baseline/issues/10)에 3CP 상호 주소 /32 제한 TCP2380 Runtime 복구 절차와 검증 범위를 기록했습니다. 로컬 구문·모의 6건 PASS이며 실제 서버 적용은 미수행입니다.

LB 설정 변경 없이 CP peer 복구 후 LB 경유 readyz/Node 조회부터 확인할 예정입니다. LB backend3/3·전체 복구는 미판정이며 담당·상태·일정·AC는 유지합니다.
<!-- cp23-etcd-recovery-20260921T1014:issue-9:end -->

---

<!-- cp3-peer-listener-20260921T0943:issue-9:start -->
## 3CP 현지 점검 추가 — 2026-09-21 09:42~09:43 KST

사용자 cp1/cp2/cp3.txt에서 CP 간 2380 TCP 6방향 모두 실패, 세 CP 모두 6443 리스너 미관측, CP2/CP3는 2379·2380 리스너도 미관측으로 확인됐습니다. 세 CP의 public Runtime/Permanent에는 LB .109→6443 허용이 있으나 CP peer 허용은 없습니다.

[상세 관측·파일 SHA256·후속: K8S #10](https://github.com/321Team/fds-project-baseline/issues/10). CP2/CP3 etcd 시작·종료 로그를 우선 확인하고 peer 통신 복구를 구체화합니다. LB 자체 상태/현재 backend 조회는 아직 없으며, 과거 backend3/3 PASS를 현재 정상으로 승계하지 않습니다. 이번에는 LB/서버 변경·복구·AC 판정을 수행하지 않았고 담당·상태·일정을 유지합니다.
<!-- cp3-peer-listener-20260921T0943:issue-9:end -->

---

<!-- cp1-etcd-peer-20260921T0043:issue-9:start -->
## CP1 etcd peer 통신 장애 관측 — 2026-09-21 00:34~00:43 KST

추가 로그에서 CP1 apiserver가 `error creating storage factory: context deadline exceeded`로 종료되고, CP1 etcd의 CP2(.103)·CP3(.104) `2380/TCP` 연결이 `no route to host/i/o timeout`으로 실패한 사실이 확인됐습니다. CP1 etcd의 합의 기반 읽기 실패와 readyz503도 관측됐습니다.

[첨부 범위·SHA256·상세 판정·다음 수집: K8S #10](https://github.com/321Team/fds-project-baseline/issues/10). 다음은 3CP 현지 포트·경로·방화벽 Runtime/Permanent 비교입니다. CP2/CP3 간 quorum과 LB backend 현재 상태는 미확인이며, CP1 장애만으로 LB EOF의 유일 원인을 확정하지 않습니다. LB 설정 변경·복구·AC 추가 판정 없이 기존 담당·상태·일정을 유지합니다.
<!-- cp1-etcd-peer-20260921T0043:issue-9:end -->

---

<!-- cp1-api-crash-20260921T0020:issue-9:start -->
## CP1 API 반복 종료 관측 추가 — 2026-09-21 00:20 KST

사용자 첨부 kubelet 로그에서 `kube-apiserver-k8s-control01`의 **CrashLoopBackOff / back-off 5m0s**가 확인됐습니다. static Pod manifest 4개는 존재하며 crictl 조회는 실행 파일을 찾지 못해 실패했습니다. 실제 apiserver 종료 원인·etcd 상태·CP2/CP3·현재 LB backend 상태는 아직 미확인입니다.

[상세 관측·첨부 SHA256·다음 수집: K8S #10](https://github.com/321Team/fds-project-baseline/issues/10). 다음은 control01의 apiserver·etcd 호스트 로그 읽기입니다. CP1의 반복 종료가 확인됐지만 LB EOF의 유일 원인 또는 LB 자체 정상으로 확대하지 않습니다. LB 설정 변경·복구·AC 추가 판정 없이 기존 담당·상태·일정을 유지합니다. 아래 00:08 기록은 당시 관측입니다.
<!-- cp1-api-crash-20260921T0020:issue-9:end -->

---

<!-- cp1-api-listener-20260921T0008:issue-9:start -->
## CP1 API 리스너 부재 확인 — 2026-09-21 00:08 KST

사용자가 제출한 화면 `2a217a52-b8bd-454b-9378-e1ae218fe209.png`의 표시 시각은 `2026-09-21T00:08:02+09:00`입니다. 앞서 안내한 control01 읽기 전용 비교 명령의 결과로 접수했습니다.

| 관측 | 화면 결과 | 확인 범위 |
|---|---|---|
| API LB .109:6443 | EOF, API_RC=1 | LB 경유 API 접근 실패 지속 |
| CP1 .102:6443 | Connection refused, API_RC=1 | CP1 직접 API 접근 실패 |
| CP1 로컬 TCP6443 | ss 헤더만 출력 | 해당 조회 시각의 6443 LISTEN 미관측 |
| kubelet/containerd | 둘 다 active/running | 서비스 프로세스 실행 중; API/etcd 컨테이너 정상까지 입증하지 않음 |

**판정:** kubeconfig 선택 문제에서 CP1 API 가용성 조사로 진행합니다. CP1에는 로컬 6443 리스너 부재가 확인되므로 kube-apiserver static Pod의 생성/실행/종료 원인과 etcd 상태를 우선 확인합니다. kube-apiserver 컨테이너의 종료·미생성·재시작 여부, CP2/CP3 상태 및 LB backend 상태는 아직 미확인입니다. LB 단독 장애, etcd quorum 상실, 인증서 또는 방화벽 원인으로 단정하지 않습니다.

**다음 최소 수집:** control01의 manifest 파일 목록, 기존 CRI 소켓을 통한 종료 포함 컨테이너 목록, 최근 kubelet 로그. API 실패 조회 반복 대신 호스트에서 읽기 전용으로 수집합니다. 파일 삭제/이동·reset/init/join·서비스 재시작·방화벽 변경·인증서 재발급은 수행하지 않았으며 현재 조치로 제시하지 않습니다.

**담당/영향:** CP 복구 판단은 기존 K8S Lead 이하영 범위, 이권욱은 원인 분리·네트워크/수집 지원을 이어갑니다. 실제 sender 식별과 IF-06B Source 관측은 미완료입니다. 9/18의 6/6 Ready·backend3/3 PASS는 과거 관측으로 보존하며 현재 정상으로 승계하지 않습니다. 기존 티켓 상태·담당·일정·AC 체크는 유지합니다. 화면 판독 결과이며 서버 원문 로그/원본 해시와 이번 추가 진단 결과는 아직 미수신입니다.
<!-- cp1-api-listener-20260921T0008:issue-9:end -->

---

<!-- api-lb-eof-20260920T2335:issue-9:start -->
## API LB 접근 실패 관측 — 2026-09-20 23:34~23:35 KST

사용자가 k8s-control01/server02에서 제출한 터미널 출력 기준입니다. `sudo kubectl --kubeconfig=/etc/kubernetes/admin.conf config current-context`는 `kubernetes-admin@kubernetes`를 출력했습니다. 이어진 namespace 조회의 `https://10.1.93.109:6443/api?timeout=15s`에서 EOF·TLS handshake timeout·최종 `Unable to connect to the server: EOF`가 발생했습니다.

- **확인:** 기존 localhost:8080 대상 문제는 이번 명령에서 해소되어 API LB 주소를 선택했습니다. context 출력은 로컬 설정 읽기이며 API 인증 성공을 뜻하지 않습니다.
- **미확인:** LB 현재 backend 상태, CP API/etcd 상태, 차단·경로·TLS 실패 원인. EOF만으로 방화벽이나 인증서 문제로 확정하지 않습니다.
- **영향:** monitoring-api namespace/Pod/Deployment/StatefulSet의 현재 존재 여부는 아직 확인하지 못했습니다. 실제 sender 식별 및 IF-06B Source 관측은 보류합니다.
- **다음:** 같은 control01에서 기존 admin.conf의 TLS 검증을 유지해 LB .109와 CP1 .102 각각 `/readyz?verbose` 읽기 전용 조회를 비교합니다. 요청별·프로세스별 시간을 제한하고 local6443 listener/kubelet/containerd 상태를 함께 확인합니다. 결과 전에는 HAProxy/노드 재시작·방화벽/NAT 변경·kubeconfig 수정·TLS 검증 생략을 수행하지 않습니다.
- **담당:** LB/네트워크 분리는 이권욱 범위, CP 서비스 문제가 확인되면 기존 K8S Lead 이하영과 연결합니다. MON Lead 이재환 역할은 유지합니다.

2026-09-18 backend3/3 PASS·6노드 관측은 당시 증적으로 보존하며 현재 정상 상태로 재사용하지 않습니다. 기존 AC 체크·Status·담당·일정은 변경하지 않았습니다. 이 기록은 사용자 붙여넣기 출력의 수신 기록이며 서버 원본 파일/해시·이번 추가 점검 결과는 아직 미수신입니다.
<!-- api-lb-eof-20260920T2335:issue-9:end -->

---

<!-- monitor01-approved-merged-20260920:issue-9:start -->
## 독립 승인·병합 완료 — 2026-09-20 KST

- [x] [PKI 증적 PR #18](https://github.com/321Team/fds-project-evidence/pull/18): 이재환/supreme33-kr가 HEAD `74745237108830e0c19912e960b2e26f0957f04b`를 [독립 승인](https://github.com/321Team/fds-project-evidence/pull/18#pullrequestreview-5260358774). **22:57:30 KST 병합**, merge `c97b13fa2910f740582076f7e7b56f0da42ddf31`.
- [x] [TLS 구성 후보 PR #3](https://github.com/321Team/infra-monitoring/pull/3): 같은 독립 검토자가 HEAD `05a8114308c510c678efd64b3443c133c36ab66f`를 [승인](https://github.com/321Team/infra-monitoring/pull/3#pullrequestreview-5260362147). **22:57:47 KST 병합**, merge `e520358bb0e4739762511f1a6b3cd7d8b83c57ae`.
- [x] 승인 후 HEAD 변경 없음·미해결 리뷰 스레드 0건 확인. 병합 tree 전체의 path/mode/blob이 승인 tree와 일치(증적 696파일·MON 47파일). [MON main CI](https://github.com/321Team/infra-monitoring/actions/runs/35515026751) **SUCCESS**, 위 merge SHA의 push 실행 확인.
- [ ] 실제 배포 입력 확정·native parser/서비스 통합·TLS/Auth/IF-06B/Blackbox 현장 인수.

이번 사용자 “후속 작업 착수” 지시로 정확한 승인 HEAD를 지정하여 두 PR을 수동 병합했습니다. 증적 PR의 CI 검사 0건은 NOT RUN이며 기존 무결성 검증·독립 편입 검토와 구분합니다. 아래 과거 Draft·리뷰/병합 대기 표현은 당시 이력입니다. PKI 현장 검증 완료 범위와 AC·티켓 상태·담당·일정은 유지합니다.

**LB 영향:** 기존 backend3/3 PASS를 유지합니다. monitor01→LB Blackbox, 단일 backend 장애 자동탐지·인증 API 연속성·복구는 별도 미완료 후속입니다. 이번 구성 병합은 이 시험의 성공 근거가 아닙니다.

실제 입력 항목과 실행/중단/복구 순서는 [MON #17](https://github.com/321Team/fds-project-baseline/issues/17)의 최신 인계표에 모았습니다.
<!-- monitor01-approved-merged-20260920:issue-9:end -->

---

<!-- monitor01-progress-sync-20260919:issue-9:start -->
## monitor01 연계 준비 진척 — 2026-09-19

- [x] monitor01 공개 인증서 발급/반환 및 현지 키·체인/IP/serverAuth 검증 완료: [PKI 증적 PR #18](https://github.com/321Team/fds-project-evidence/pull/18).
- [x] monitor01 TLS 수신 구성 후보와 정적/단위 CI 준비 완료: [TLS 구성 후보 PR #3](https://github.com/321Team/infra-monitoring/pull/3) · [CI #35442097555](https://github.com/321Team/infra-monitoring/actions/runs/35442097555) SUCCESS.
- [ ] monitor01→LB `10.1.93.109:6443`의 Blackbox 실제 시험 및 MON 인수. 인증서 발급과 수신 구성 후보의 CI 성공은 이 outbound 시험의 성공 근거가 아님.

기존 **LB backend3/3 PASS(2026-09-18 21:27 KST 관측)**와 담당·일정·상태·AC는 유지합니다. 단일 backend 장애 자동탐지·인증 API 연속성·복구는 기존 미실행 후속이며 이번 PKI 작업으로 완료 처리하지 않습니다. 같은 backend3/3 재수집을 요청하지 않습니다.

두 PR은 조회 현재 open/Draft·제출 리뷰 0건·미병합입니다. 상세 진행 및 잔여: [MON #17](https://github.com/321Team/fds-project-baseline/issues/17). 위 체크는 연계 준비 진척이며 LB 전체 인수 체크가 아닙니다.
<!-- monitor01-progress-sync-20260919:issue-9:end -->

---

<!-- lb-runtime-preflight-20260918T122733Z:start -->
## 최신 실측 — 2026-09-18 21:27 KST backend 3/3 PASS

사용자 제출 원본을 검증했습니다. **PRECHECK_READY**, 수집 구간 `21:27:33.782927–21:27:34.386833 KST`이며 현재 상태의 짧은 스냅샷입니다.

| 대상 | 전후 HAProxy stats | LB .109 출발 TCP6443 |
|---|---|---|
| k8s-control01 .102 | UP / L4OK / active weight1 | 연결 성공 |
| k8s-control02 .103 | UP / L4OK / active weight1 | 연결 성공 |
| k8s-control03 .104 | UP / L4OK / active weight1 | 연결 성공 |

- **무결성:** 원본 `FDS_P1_LB_01_STAGEB_PREFLIGHT_20260918T122733Z_6kk8lyhy.tar.gz`, SHA256 `579bee923366dae6568cfa69734227354c725cb6b0608b38fe9c3c79293e1151`; 제출 sidecar 일치·내부 manifest46/46·수집기 SHA256 `b4e211dac2cee0eb4c926f90ee818dc83c727401b95173cb18a9174283707476`(PR1 승인본) 일치.
- **원본 대조:** 명령20/20 rc0·stderr공란, 전후 상태 stdout8쌍 일치. 원본 stats CSV 및 TCP_PROBES.json을 RESULT.json과 별도로 대조하여3/3을 확인했습니다.
- **LB 상태:** HAProxy active, .109:6443 listener, 설정 구문검사 rc0, 주 설정 SHA `afd19086ab8529d621185c231fa3c588eaeeb2025a08445e90f28cf27b00504f` 일치, 추가 conf.d cfg 없음, 전후 PID/실행인자/설정 해시 일치. 수집기의 설정 변경 시도 없음.
- **판정 반영:** 현행 핵심 요구사항의 HAProxy TCP health/backend 검증 및 AC의 CP3 Backend 정상은 이 관측 범위로 충족 처리합니다. ICR AC와 별도이며 티켓 전체 In Progress는 유지합니다.
- **잔여:** 장애 자동탐지·인증 API 연속성·복구는 이번 자료의 `NOT_TESTED`입니다. 기존 CP1→LB 인증 API/6노드 조회 성공은 별도 시점 증거로 재사용합니다. Stage B 전체 완료·최종 Handoff·독립 인수로 확대하지 않습니다.
- **다음:** 현재3/3 수집의 동일 재실행은 요청하지 않습니다. 기존 failover 초안의 한 대상·주입/복구 방법·관측 조건을 구체화하는 후속으로 이동합니다. 과거 CP2/3 DOWN 및 이 아래 “수신 대기”는 당시 이력입니다.

<!-- lb-runtime-preflight-20260918T122733Z:end -->

<!-- lb-our-followup-20260918:start -->
## LB 담당 후속 착수 — 2026-09-18

사용자가 K8S 오너에게 역할 인계를 전달했고 “우리의 작업을 착수”하도록 지시했습니다. LB Lead 이권욱 범위에서 기존 승인·병합 수집기로 backend3/3 현장 확인을 준비했습니다. 15:56 KST 3CP+3Worker 6/6 Ready가 확인됐습니다. 남은 K8S 검증은 #10 오너 절차로 진행하며 이 작업을 새 선행 대기로 만들지 않습니다.

- **실행 소스:** [PR1 승인](https://github.com/321Team/infra-lb/pull/1#pullrequestreview-5231739996), approved HEAD `b3327c76fc3b7d8dd49cb8348b826bf75e7fc429` / merge `83d13e326c5e320cb5149eebfdbacfd09aa5af9c`.
- **재사용 수집기:** [collect_preflight.py](https://github.com/321Team/infra-lb/blob/83d13e326c5e320cb5149eebfdbacfd09aa5af9c/tools/stage-b/collect_preflight.py), SHA256 `b4e211dac2cee0eb4c926f90ee818dc83c727401b95173cb18a9174283707476`. 바이트 변경 없음.
- **실행 묶음:** `FDS_LB_Backend_Check_83d13e3_v1.0.tar.gz`, SHA256 `28df952dd5a0dd788761811ec22041cb869834a94d89d5b7f9bbe01187f8627c`. 수집기·실행 설명·출처·내부 체크섬 4개 파일 검증 완료.
- **현장 실행:** k8s-api-lb01 일반 계정에서 기존 `sudo -v` 후 Python 수집. 실제 서비스/설정, stats 전후 backend3/3, .109→CP3 TCP6443을 확인합니다. 설정 변경·reload·장애 주입은 없습니다.
- **판정:** 이번 LB 전용 수집 결과는 아직 제출되지 않아 backend별 현재 상태는 미확인입니다. PRECHECK_READY 또는 실패 자료의 ARCHIVE/SIDECAR를 받아 backend 현재 상태를 판단합니다. 13:04·15:56 CP1→LB 인증 API와 기존 DAD/CP 성공 증적은 재사용합니다.
- **후속 범위:** 장애 자동탐지·API 연속성·복구 시험은 실제 대상·주입/복구 명령·관측 조건이 확정된 별도 실행 범위입니다. 수동 MAINT/disable를 실제 DOWN 시험으로 대체하지 않습니다.

[중앙 권한 정책](https://github.com/321Team/fds-project-baseline/blob/b2e4612cf2e417b10e7f145c5b1e5f58dbe1b948/governance/REVIEW_AUTHORITY_POLICY.md)에 따라 코드 외 실행·결과 판단은 해당 Lead가 수행합니다. 동일 코드 실행마다 독립 승인을 추가하지 않으며, 코드 병합 및 증적 저장소 PR의 독립 리뷰는 유지합니다. AC·상태·담당·일정과 과거 증적은 변경하지 않았습니다.
### IF-16 완료 후 LB 실행 착수 — 2026-09-18

사용자 “착수” 지시에 따라 다음 현장 작업을 **LB backend3/3 읽기 전용 수집 1회**로 확정했습니다. ICR-AC-13은 edge01·harbor01·db01 3/3 RUNTIME_PASS이며 해당 경로 적용/조회는 반복하지 않습니다.

- 기존 배포 archive 외부 SHA 및 내부 manifest3/3을 재확인했습니다. 승인 소스와 배포본 변경 없음.
- 실행 위치: **k8s-api-lb01 일반 계정의 실제 홈(`$HOME`)**. `sudo -v` 다음 `python3 -I -B collect_preflight.py --run`; 실행 명령과 기존 두 배포 파일을 사용자에게 전달합니다.
- 실제 LB 실행 결과는 아직 미수신입니다. `STATUS`, `ARCHIVE`, `SIDECAR`를 받아 개별 CP3대의 stats/TCP 결과를 판정합니다. archive 준비를 Runtime PASS로 기록하지 않습니다.
- infra-lb PR2/3은 조회 현재 open·각 제출 review0건이며 과거 증적 편입 검토 상태입니다. 승인·병합된 PR1 수집기를 실행하는 새 차단 조건으로 추가하지 않습니다.
- [장애시험 초안](https://github.com/321Team/infra-lb/blob/83d13e326c5e320cb5149eebfdbacfd09aa5af9c/docs/runbooks/FAILOVER.md)의 실제 대상·주입/복구 방식은 아직 미확정입니다. 이번 수집과 장애주입을 자동 연결하지 않으며, 3/3 결과에 이어 한 대상의 관측·복구 실행안을 구체화합니다.

<!-- lb-our-followup-20260918:end -->

<!-- cp-join-upstream-20260918:start -->
## 상위 클러스터 상태 갱신 — 2026-09-18 15:56 KST

[새 실측 증적](https://github.com/321Team/infra-kubernetes/blob/ea4aef3c960fd79377225f7f037bc39cd04df469/ops/icr-followup-20260918/results/20260918T065614Z_zzi65aal/README.md)에서 **3CP+3Worker 6/6 Ready**를 확인했습니다. Calico-node6개+controller1개 Ready이며 기존 CP3 UID/IP/역할/Ready를 유지합니다. CP1→LB .109:6443에서 source .102/ens160, proxy 미사용·CA 검증 강제, kubernetes-admin 인증과 Node GET rc0으로 6개 노드를 반환했습니다.

**이 자료는 LB backend별3/3·장애복구 시험을 포함하지 않습니다.** 기존 승인 소스의 `FDS_LB_Backend_Check_83d13e3_v1.0` 묶음으로 LB 자체 backend/stats 및 .109→CP3 TCP6443을 확인하는 다음 범위는 그대로입니다. 같은 CP1 인증 조회·6/6 수집·과거 DAD를 반복할 필요는 없습니다. 이후 장애 자동탐지·API 연속성·복구 시험을 실제 주입/복구 계획에 따라 진행합니다.

기존 [12:33 CP Join 증적](https://github.com/321Team/infra-kubernetes/blob/5e9e09e7a1820c230bb5724ce05897c7689ef065/ops/cp-join-20260918/results/20260918T033022Z_16219c68779b3d13/README.md)에서 CP2/CP3 Join rc0·3CP Ready·etcd3voter/health3/3를 확인했습니다. etcd 건강은 당시 관측이며 이번 15:56 자료에서 재조회하지 않았습니다. [13:04 CP1→LB 인증 API 성공](https://github.com/321Team/infra-kubernetes/blob/22673b0ba5ee188a514c5643bc3df8e7999a2d5a/ops/icr-followup-20260918/results/20260918T040403Z_zgby6ckp/README.md)도 이전 이력으로 보존합니다.

과거 CP2/CP3 미가입·API 미기동을 이유로 LB 검증을 대기할 필요는 없습니다. Join 전 preflight DOWN/NOT_READY는 당시 이력입니다. 현재 backend별상태로 사용하지 않으며 LB 설정 변경·Stage B 완료·LB-A-01/티켓 종결을 이번 조회로 처리하지 않습니다.
<!-- cp-join-upstream-20260918:end -->

<!-- fds-lb-pr-migration:20260917:start -->
## LB 전용 PR 이관 완료 — infra-lb에서 후속 리뷰

2026-09-17 사용자 “PR 옮기는 작업 수행” 지시에 따라 원본 evidence PR 두 건의 미병합 변경과 후속 검토를 infra-lb로 이관했다.

| 원본 | 새 검토 위치 | 고정 검토 HEAD | 상태 |
|---|---|---|---|
| [evidence #14](https://github.com/321Team/fds-project-evidence/pull/14) | [infra-lb #2 — DAD](https://github.com/321Team/infra-lb/pull/2) | `4cdd94249ae8f68e7ed3921ab25150f5b5deb9b4` | Ready, 이하영 독립 검토·LB-A-01 조건 해소 판단 대기 |
| [evidence #15](https://github.com/321Team/fds-project-evidence/pull/15) | [infra-lb #3 — Stage B preflight](https://github.com/321Team/infra-lb/pull/3) | `a5191201a65cfbf38e9e2c9558aae5983eb9c5f7` | Ready, 이하영 편입 검토 대기; PRECHECK_NOT_READY 유지 |

- 원본 추가 파일 DAD **34/34**, preflight **52/52**가 원본 경로·Git blob SHA·byte 동일. 원격 대상 tree는 DAD **81/81**, Stage B **135/135** 파일 및 mode 대조 완료.
- 내부 manifest DAD29/29, preflight raw46/46·패키지51/51, 새 루트 manifest80/80·134/134 확인. NUL 구분 cmdline 보존.
- 원본 PR14/15는 양방향 링크와 고정 HEAD를 기록해 **이관 사유로 종료**했다. merged=false이며 브랜치·실제 대화 이력은 원래 위치에 보존한다. 새 PR에 원문·댓글 사본과 파일별 출처도 기록했다.
- 두 원본 PR의 이관 전 review submission은 0건. 새 PR 둘에 이하영(`hayeounglee`) 리뷰를 요청했으며 과거 승인을 자동 승계하지 않는다.
- 병합 순서: **#2 → main**, 이후 **#3의 base를 main으로 변경 → diff/HEAD/승인 확인**. #3을 #2 분기로 먼저 병합하지 않는다.
- [이관 대응표](https://github.com/321Team/infra-lb/blob/a5191201a65cfbf38e9e2c9558aae5983eb9c5f7/docs/PR_MIGRATIONS.md). 공통 FUP PR7·Ansible PR13·기존 병합 이력·다른 요구사항은 그대로 유지한다.
- 서버 재실행·설정 변경 없음. DAD 기술 PASS와 실제 인수는 구분하며 **Stage B 미완료 / P1-LB-01 In Progress**를 유지한다. 기존 AC를 완료로 바꾸지 않았다.

아래 소스 편입 및 수신 기록은 작성 당시 이력이다. 그 중 PR14/15를 evidence에서 계속 검토하거나 open으로 표시한 문구의 최신 상태는 이 상단 이관 기록을 따른다.
<!-- fds-lb-pr-migration:20260917:end -->

---

<!-- fds-lb-source-import:20260917:start -->
## LB 소스·기존 자료 편입 — 승인·main 병합 완료

- [infra-lb PR #1](https://github.com/321Team/infra-lb/pull/1), 최신 검토 HEAD `b3327c76fc3b7d8dd49cb8348b826bf75e7fc429`. 초기 소스 편입 `1f4a25493c24ea9d7925cbbeea2d27608fd7d1d2`에 추가 자료 24개·기존 문서 4개 보완을 등록했다. 전체 44개 파일.
- Stage A 가이드 v1.5, 완료 팩 v1.3의 LB 소스/문서, export/보완 소스, 노션 작업 기록 원본 **16개**를 보존했다. LB 대화 4개 구간과 원본 출처를 연결하고 증적 **134개**의 고정 경로·Git blob 목록을 정리했다.
- [자료·증적 목록](https://github.com/321Team/infra-lb/blob/b3327c76fc3b7d8dd49cb8348b826bf75e7fc429/docs/EVIDENCE_INDEX.md), [이관 대응표](https://github.com/321Team/infra-lb/blob/b3327c76fc3b7d8dd49cb8348b826bf75e7fc429/docs/MIGRATION_MAP.md), [인계 근거](https://github.com/321Team/infra-lb/blob/b3327c76fc3b7d8dd49cb8348b826bf75e7fc429/docs/STAGE_A_HANDOFF.md).
- 완료 팩 내부 manifest 12/12, 원본 보존 16/16, Bash 5개·Python 2개 구문, 새 문서 링크, 저장소 manifest 43/43 및 원격 Git blob 44/44 일치 확인. 기존 cfg·DAD/preflight 코드/테스트는 그대로이며 초기 테스트 45/45 결과를 재사용했다.
- [이하영 최신 HEAD APPROVED](https://github.com/321Team/infra-lb/pull/1#pullrequestreview-5231739996) 확인 후 사용자 조건부 병합 지시에 따라 **2026-09-17 14:56:24 KST 병합 완료**. 병합 commit `83d13e326c5e320cb5149eebfdbacfd09aa5af9c`, main 일치 및 검토 파일 44/44 보존 확인. CI 검사 0건·미실행은 로컬 검증과 구분한다. 증빙 PR14/15와 과거 승인 이력은 evidence에서 유지한다.
- `archive/`는 과거 자료 보존용이다. 이번 이관으로 서버 적용·추가 검사·DAD 최종 인수·Stage B 완료·기존 AC 및 In Progress 상태를 변경하지 않는다. main 브랜치 보호는 초기 확인에서 비활성이며 문서상 운영 정책과 구분한다.
<!-- fds-lb-source-import:20260917:end -->

---

<!-- fds-lb-stageb-preflight:20260917T031743Z:start -->
## 최신 Stage B 사전점검 — LB 정상·CP1 UP / CP2·CP3 미준비

**2026-09-17 12:17:43 KST 원본 수신 검증 완료. PRECHECK_NOT_READY / Stage B 미완료 / In Progress 유지.**

| 항목 | 실제 확인 |
|---|---|
| LB 설정·서비스·리스너 | 설정 구문 rc0, 기존 Stage A 주 설정 SHA 일치, HAProxy active, .109:6443 LISTEN |
| CP1 .102:6443 | HAProxy UP/L4OK, LB .109에서 TCP 연결 성공 |
| CP2 .103:6443 | HAProxy DOWN/L4CON, TCP Connection refused(errno111) |
| CP3 .104:6443 | HAProxy DOWN/L4CON, TCP Connection refused(errno111) |
| 수신 무결성 | 외부 SHA 일치, 내부46/46, 배포 수집기 바이트 일치 |
| 수집 실행 | 외부 조회20/20 rc0·stderr0; 별도 TCP는1성공·2거절; 전후 stdout8쌍 동일 |
| 후속 API·장애복구 | 인증 API/단일 backend 장애·복구 미수행 |

- [증적 PR15](https://github.com/321Team/fds-project-evidence/pull/15), 고정 HEAD `c6ed08bdd7d54901dffc709fc9fa0d75e961f68b`: 원본47파일 및 새 수신 검토를 등록하고 이하영(`hayeounglee`)에게 편입 리뷰를 요청했다. ready for review·미병합이며 최종 인수는 대기다.
- [수신 검토](https://github.com/321Team/fds-project-evidence/blob/c6ed08bdd7d54901dffc709fc9fa0d75e961f68b/evidence/P1-LB-01/stage-b/preflight-20260917T031743Z/README.md) · [검증 결과](https://github.com/321Team/fds-project-evidence/blob/c6ed08bdd7d54901dffc709fc9fa0d75e961f68b/evidence/P1-LB-01/stage-b/preflight-20260917T031743Z/VERIFICATION.json).
- **진척:** 기존 bootstrap 전3DOWN 이력에서 CP1의 현재 LB health와 TCP 연결 성공을 새 원본으로 확인했다. CP1 Ready·실제 인수·API 인증 성공으로 확대하지 않는다.
- **직접 후속:** [P1-K8S-01 #10](https://github.com/321Team/fds-project-baseline/issues/10)의 기존 CP1 인수 및 CP2/3 준비 흐름에 연결한다. CP2/3 실제 API listener·기동·LB source 접근 자료로 원인을 확인하고 관련 준비 완료 뒤 3/3 backend를 재점검한다. 원인 확정 전 LB 설정 변경이나 방화벽 해제를 지시하지 않는다.
- 전체 BACKEND 행 UP은 개별3서버 모두 UP을 의미하지 않는다. 이번 수신 자료로 CP2/3의 API 미기동·서비스 이상·방화벽 중 원인을 확정할 수 없다.
- 기존 Stage A Technical/Evidence PASS·조건부 인수 및 Permanent 해소 범위는 유지한다. DAD PR14의 인수 판단은 별도이며 이 기록이 최종 인수/병합을 대신하지 않는다.

아래 DAD·Stage A 기록은 해당 범위의 진행 이력으로 보존한다.
<!-- fds-lb-stageb-preflight:20260917T031743Z:end -->

---

<!-- fds-lb-acceptance-followup:20260917:v5:start -->
## 최신 상태 — 현재 시점 DAD PASS·원본 등록 / 이하영 인수 확인 대기

**Stage A Technical/Evidence PASS·조건부 인수 유지 / Permanent 조건 해소 / 현재 시점 DAD PASS·인수 확인 대기 / Stage B 미완료 / In Progress.**

- [현재 시점 재검사 승인](https://github.com/321Team/fds-project-evidence/issues/4#issuecomment-5699238203)에 따라 실행한 v1.1 원본을 수신했다. **2026-09-17 00:07:50~53 KST / 2026-09-16 15:07:50~53 UTC**의 별도 보완검사이며 파일명은 UTC 기준이다.
- [증적 PR #14](https://github.com/321Team/fds-project-evidence/pull/14), 검토 HEAD **`f74bda7eac39658c297a4dd5d1c590bd0717bcce`**. 원본 및 수신 검토를 등록하고 **이하영(`hayeounglee`)에게 공식 리뷰를 요청했다**. 현재 open·ready for review·미병합이며 실제 독립 승인·최종 인수 회신은 대기다.
- [원본 DAD 출력](https://github.com/321Team/fds-project-evidence/blob/f74bda7eac39658c297a4dd5d1c590bd0717bcce/evidence/P1-LB-01/stage-a/dad-supplement-20260916T150750Z/raw/05_dad.stdout.txt) · [명령/RC/시각](https://github.com/321Team/fds-project-evidence/blob/f74bda7eac39658c297a4dd5d1c590bd0717bcce/evidence/P1-LB-01/stage-a/dad-supplement-20260916T150750Z/raw/COMMANDS.json) · [수신 검증](https://github.com/321Team/fds-project-evidence/blob/f74bda7eac39658c297a4dd5d1c590bd0717bcce/evidence/P1-LB-01/stage-a/dad-supplement-20260916T150750Z/VERIFICATION.json) · [검토 안내](https://github.com/321Team/fds-project-evidence/blob/f74bda7eac39658c297a4dd5d1c590bd0717bcce/evidence/P1-LB-01/stage-a/dad-supplement-20260916T150750Z/README.md).

- **수신 검증:** 외부 체크섬·내부 **29/29**, 명령 **12/12 rc=0**. 사전 L2 통신 성공 후 **DAD 송신 3·응답 0·rc=0**, 전후 IP/MAC·링크·HAProxy·Listener 일치. 검토자가 서버에서 다시 실행한 결과가 아니라 사용자 제출 원본을 대조한 결과다.
- **도구 해시 한계:** sudo 바이너리는 mode `0o4111`로 일반 계정 읽기 권한이 없어 보조 Hash 미확인(도구 6/7). sudo 경유 3개 명령과 필수 증적 29개 Hash 검증은 정상이다. [이전 v1.0 STOP 기록](https://github.com/321Team/fds-project-evidence/issues/4#issuecomment-5699648290)은 보존한다.
- **다음:** 이하영이 PR #14의 고정 HEAD를 검토하고 새 증적 편입 및 LB-A-01 잔여 조건 해소 여부를 명시한다. 인수 회신과 이권욱의 최종 편입 결정·병합은 아직 대기다. 현재 결과만으로 같은 DAD 재실행을 요청하지 않는다.
- **Permanent — 해소 유지:** [9/16 인수 회신](https://github.com/321Team/fds-project-evidence/issues/4#issuecomment-5697474151)에 따른 9/9 Supplement의 7/7 Hash·5/5 조회 rc=0·허용 규칙 8개 일치 범위다.
- 과거 8/31 원본은 미확보 이력으로 남기며 현재 보완 결과를 과거 복구로 표시하지 않는다. Stage B Backend 3대 UP·인증 API·단일 backend 장애 시 지속/복구, Bootstrap·기존 AC·티켓 종결은 별도다.
- [FUP-09 상세 추적](https://github.com/321Team/fds-project-evidence/issues/4)에 동일 수신·검토 대기 상태를 반영했다.

아래 원본 미수신·실행 대기·STOP만 기재된 내용은 작성 당시 이력이다. 최신 판단은 이 상단 및 PR #14의 실제 리뷰를 따른다.
<!-- fds-lb-acceptance-followup:20260917:v5:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** Stage A 조건부 인수 유지. FUP-09 원본·Supplement 조건 판단과 Stage B를 구분 ; R04.

- 현재 Permanent Supplement의 수신·독립 승인·main 편입은 완료다. 이하영의 현재 Supplement 인수 조건 판단과 LB-A-01 DAD 원본/고정 참조만 추가 연결한다. Stage B/Bootstrap의 실제 준비·인수는 K8S 후속과 연결한다.

**종결 승인·원본 참조 (R04)** — P1-NET #67의 당시 Reviewer/Approver·일시/범위는 FUP-05의 기존 참조로 보완한다. FUP-04 최초 원본, FUP-06/07 개인별 회신/정확한 시각/WBS 열람, FUP-09 DAD 원본과 이하영의 Supplement 조건 판단은 잔여다. 현재 Permanent Supplement의 수신·독립승인·main편입은 완료돼 있다. 기존 Done·Stage A PASS·조건부 인수·Bootstrap HOLD를 보존하며 소급 승인 서명을 만들지 않는다.
근거: [#67](https://github.com/321Team/fds-project-baseline/issues/67) · [FUP 후속](https://github.com/321Team/fds-project-evidence/issues/4) · [매핑 PR #7](https://github.com/321Team/fds-project-evidence/pull/7)

**인계·관련 티켓:** [#10](https://github.com/321Team/fds-project-baseline/issues/10) · [#14](https://github.com/321Team/fds-project-baseline/issues/14).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-LB-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-LB-01 -->
# P1-LB-01 — Kubernetes API Load Balancer

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-LB-01 |
| Phase | Phase 1 |
| Category | Infrastructure / Load Balancer |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-09-17 |
| Calendar Days | 22 |
| Working Days | 16 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | IF-11/IF-11A/IF-06A Source Allowlist, `.109:6443→.102~.104:6443` Stage A Listener/Handoff와 Stage B Backend Health/API/Failover Evidence |
| Related Decision IDs | D02; D05; D27; D31; D34; D35 |
| Related Risk IDs | RISK-02; RISK-03; RISK-04 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #9 snapshot 2026-09-10T02:09:13Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | Stage B는 3CP API 기동 후 검증하며 09-17 G1 인수에 연결한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **In Progress / open**. 원본 갱신 시각: `2026-09-10T02:09:13Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

Stage A 기존 Technical/Evidence PASS 및 이하영의 조건부 인수는 유지한다. 증적 PR #6의 현재 Permanent Supplement는 독립 승인·main 편입 완료. 남은 조건은 이하영의 Supplement 인정 범위 판단과 LB-A-01 IP 중복검사 원본/고정 참조 연결이다. Stage B Backend 3대·인증 API·Failover/Recovery는 미완료이며 Ticket In Progress를 유지한다. 현재 후보 Plan: 2026-08-27 ~ 2026-09-17 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #9](https://github.com/321Team/fds-project-baseline/issues/9), Issue 갱신 시각 `2026-09-10T02:09:13Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

### User Story

인프라 담당자로서 단일 Kubernetes API Endpoint를 제공한다.

### Scope

#### In Scope

- `.109:6443` TLS pass-through
- CP `.102~.104:6443`
- IF-11 Runner `.20/32`, IF-11A Node 6대, IF-06A monitor01 `.30/32` Source Allowlist
- Stage A/Stage B Health/Failover

#### Out of Scope

- Application NodePort 30080 및 `externalTrafficPolicy: Local` 구현
- Kubernetes Node firewalld와 Calico HEP/GNP

### 핵심 요구사항

2026-09-18 증적 대조: 체크는 아래에 연결한 원 실행·수신 범위의 충족 사실이다. 기존 AC 조건·계획일·담당·In Progress 상태는 유지한다.

- [x] IF-11A 설계 승인 및 IF-06A 보존 계약 확인
- [x] IF-11/IF-11A/IF-06A `/32` Rule과 Zone-wide 6443 미개방을 검증한다. — 9/9 [Runtime](https://github.com/321Team/fds-project-evidence/blob/90093f88167055f81e8789d2a848f44ead0ee9ce/evidence/P1-LB-01/stage-a/supplement-20260909T072022Z/raw/03_public_runtime.txt)·[Permanent](https://github.com/321Team/fds-project-evidence/blob/90093f88167055f81e8789d2a848f44ead0ee9ce/evidence/P1-LB-01/stage-a/supplement-20260909T072022Z/raw/04_public_permanent.txt) 출력의 8개 규칙 일치·ports 공란과 [이하영 수용](https://github.com/321Team/fds-project-evidence/issues/4#issuecomment-5697474151) 확인. 재부팅 지속성 증거는 아니다.
- [x] Node 6대·Runner Positive와 ansible01 `.10` Negative를 검증한다. — 9/3 [Node 6/6](https://github.com/321Team/fds-project-evidence/blob/90093f88167055f81e8789d2a848f44ead0ee9ce/evidence/P1-LB-01/stage-a/received-20260907/16_positive_test_nodes.txt), [Runner rc0](https://github.com/321Team/fds-project-evidence/blob/90093f88167055f81e8789d2a848f44ead0ee9ce/evidence/P1-LB-01/stage-a/received-20260907/17_positive_test_runner.txt), [ansible01 TIMEOUT/rc1](https://github.com/321Team/fds-project-evidence/blob/90093f88167055f81e8789d2a848f44ead0ee9ce/evidence/P1-LB-01/stage-a/received-20260907/18_negative_test.txt). 기존 TCP Source 시험이며 인증 API 시험과 구분한다.
- [x] HAProxy TCP health와 Control Plane backend를 검증한다. — 2026-09-18 21:27 KST 사용자 제출 원본에서 stats 전후 개별3대 UP/L4OK·LB .109 출발 CP3대 TCP6443 연결 성공. 상단 원본 SHA/검증 기록 참조. 장애·복구 시험은 별도 미완료.
- [x] Stage A Listener Evidence를 P1-K8S Bootstrap 전에 전달한다. — 9/7 [제출 원본 검토](https://github.com/321Team/fds-project-evidence/blob/90093f88167055f81e8789d2a848f44ead0ee9ce/evidence/P1-LB-01/stage-a/received-20260907/19_stage_a_handoff_review.md)와 9/8 [실제 수신·조건부 인수](https://github.com/321Team/fds-project-evidence/pull/1#issuecomment-5582767564)를 연결한다. 자료 전달 완료와 아래 최종 Handoff 인수는 구분한다.

### Acceptance Criteria

- [x] Listener와 Source Allowlist PASS — 기존 [Stage A 기술 검토](https://github.com/321Team/fds-project-evidence/blob/90093f88167055f81e8789d2a848f44ead0ee9ce/evidence/P1-LB-01/stage-a/received-20260907/19_stage_a_handoff_review.md) 및 9/9 규칙 보완 범위. Stage B·DAD 최종 수용을 대신하지 않는다.
- [x] CP 3대 Backend 정상 — 2026-09-18 21:27 KST 전후 개별3대 UP/L4OK/active weight1 및 .109→.102/.103/.104 TCP6443 연결3/3 성공. 짧은 관측 시점의 정상이며 장애 중 API 지속 증거는 아님.
- [ ] Backend 1대 장애 시 API 지속 — 실제 단일 backend 장애 자동탐지·인증 API 연속성 및 복구 증적이 남았다.
- [ ] P1-K8S Bootstrap Handoff — 증적 전달·조건부 수신은 확인했다. [현재 DAD 원본](https://github.com/321Team/infra-lb/blob/4cdd94249ae8f68e7ed3921ab25150f5b5deb9b4/evidence/P1-LB-01/stage-a/dad-supplement-20260916T150750Z/README.md)의 LB-A-01 잔여 조건 수용과 실제 최종 인수 범위를 확인해 연결한다. 과거 원본 누락만을 이유로 완료된 Stage A 전체 시험을 반복 요구하지 않는다.

### Evidence

- HAProxy config validation, Listener/Allowlist, Backend health, failover, rollback
- `docs/evidence/P1-LB-01/`

### Dependency

- Blocked By: P1-LNX-01/P1-NET-01/P1-ANS-01 Done Evidence
- Blocks: P1-K8S-01 kubeadm init, P1-LB Stage B

### Decision / Risk Control

- Decision: D27/D34에 따라 API LB와 Application NodePort 책임을 분리하고 D35에 따라 IF-11A 승인·IF-06A 보존을 적용한다.
- Risk Control: Stage A는 backend가 없어도 Listener만 검증하며 Stage B에서 API/failover를 최종 판정한다.

### Review / Handoff

- Review Owner: 이하영
- Handoff: `.109:6443` Listener, Source Allowlist, Positive/Negative, SHA256/Commit Evidence를 P1-K8S에 전달한다.

### Scope Boundary

`externalTrafficPolicy: Local` Application NodePort 검증은 P1-APP/P1-SEC와 edge01 구성 담당이 수행한다.

### Completion Record

- Result: Stage A 기술/증적·9/18 backend3/3·9/21 API 복구 유지. 이관 PR2/3 독립 승인·병합 완료. 단일 backend 장애 중 인증 API 지속·복구·최종 Handoff 인수는 잔여.
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `43f83489672941dcc3652c2ca2366db2c8c4cacf90d77db8b023db2399c94201`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-LB-01 -->
# P1-LB-01 — Kubernetes API Load Balancer

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-LB-01 |
| Phase | Phase 1 |
| Category | Infrastructure / Load Balancer |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-09-07 |
| Calendar Days | 12 |
| Working Days | 8 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | IF-11/IF-11A/IF-06A Source Allowlist, `.109:6443→.102~.104:6443` Stage A Listener/Handoff와 Stage B Backend Health/API/Failover Evidence |
| Related Decision IDs | D02; D05; D27; D31; D34; D35 |
| Related Risk IDs | RISK-02; RISK-03; RISK-04 |
| Source | Baseline v3.1.15; P1-LB Stage A Guide v1.3; D35 IF-11A Approval Record; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | Stage A PASS 2026-09-03. Stage B target rebaselined to approved D36 G1 target 2026-09-07; remains In Progress until backend/auth/failover/recovery evidence is PASS. |

## 이관 기준 및 확인 사항

- 속성의 일정·담당·상태는 RELEASED v3.1.17 WBS(기준일 2026-09-04)를 우선 반영했다. 이후 별도 근거가 있는 변경만 아래에 명시한다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`
- `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md`
- `FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx`

---

## Description — 보관 입력본

> 원본: `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

### 🎯 User Story

인프라 담당자로서 단일 Kubernetes API Endpoint를 제공한다.

### 📌 Scope

#### In Scope

- `.109:6443` TLS pass-through
- CP `.102~.104:6443`
- IF-11 Runner `.20/32`, IF-11A Node 6대, IF-06A monitor01 `.30/32` Source Allowlist
- Stage A/Stage B Health/Failover

#### Out of Scope

- Application NodePort 30080 및 `externalTrafficPolicy: Local` 구현
- Kubernetes Node firewalld와 Calico HEP/GNP

### 📋 핵심 요구사항

- [x] IF-11A 설계 승인 및 IF-06A 보존 계약 확인
- [ ] IF-11/IF-11A/IF-06A `/32` Rule과 Zone-wide 6443 미개방을 검증한다.
- [ ] Node 6대·Runner Positive와 ansible01 `.10` Negative를 검증한다.
- [ ] HAProxy TCP health와 Control Plane backend를 검증한다.
- [ ] Stage A Listener Evidence를 P1-K8S Bootstrap 전에 전달한다.

### ✅ Acceptance Criteria

- [ ] Listener와 Source Allowlist PASS
- [ ] CP 3대 Backend 정상
- [ ] Backend 1대 장애 시 API 지속
- [ ] P1-K8S Bootstrap Handoff

### 🧪 Evidence

- HAProxy config validation, Listener/Allowlist, Backend health, failover, rollback
- `docs/evidence/P1-LB-01/`

### 🔗 Dependency

- Blocked By: P1-LNX-01/P1-NET-01/P1-ANS-01 Done Evidence
- Blocks: P1-K8S-01 kubeadm init, P1-LB Stage B

### ⚖️ Decision / Risk Control

- Decision: D27/D34에 따라 API LB와 Application NodePort 책임을 분리하고 D35에 따라 IF-11A 승인·IF-06A 보존을 적용한다.
- Risk Control: Stage A는 backend가 없어도 Listener만 검증하며 Stage B에서 API/failover를 최종 판정한다.

### 🔍 Review / Handoff

- Review Owner: 이하영
- Handoff: `.109:6443` Listener, Source Allowlist, Positive/Negative, SHA256/Commit Evidence를 P1-K8S에 전달한다.

### ⚠️ Scope Boundary

`externalTrafficPolicy: Local` Application NodePort 검증은 P1-APP/P1-SEC와 edge01 구성 담당이 수행한다.

### 📝 Completion Record

- Result: TBD
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용
````

</details>
