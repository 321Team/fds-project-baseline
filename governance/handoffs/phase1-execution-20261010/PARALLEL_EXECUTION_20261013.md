# Phase 1 병행 잔여 실행·인수안 — 2026-10-13

이권욱 / CODEX_ASSISTED. 기준 baseline main `8e909b107512ab5c90611c998bbb925d2b303ed3`, CICD main `2d8a14c55ea4b61f53b7ac6d682cd5e97575dda7`, Ansible main `2381e0228838971640788c3bf8b11385a9e52fc1`, K8S main `92c182fc58de999536e56d90012bb2686d9f07cf`. 현장 추가 조회04:26~04:29 KST.

[PR160/161 전체 인수 범위](README.md)와 [PR162 최소 검증안](MINIMUM_VALIDATION.md)의 후속이다. 기존 문서는 당시 준비 기록으로 보존한다. 이번에는 변경 없는 시험·코드 리뷰를 반복하지 않고 새 관측과 실제 남은 선택만 연결한다. AC·담당·Due·정본·Phase1 완료 여부는 바꾸지 않는다. Phase2 사전 작업은 없다.

## 1. 작업 순서와 중복 방지

| 순서 | 지금 진행하는 일 | 해당 단계 완료조건 / 독립 진행 |
|---|---|---|
| 1 | 기존 Push 입력의 독립 검토 수신 | [증적208][e208]의 목표hash13b50485·10:00/12:00 창. 사용자 실행 허용은 이미 수신. 새 Lead GO·PR전체 병합을 추가 gate로 만들지 않음 |
| 2 | Deploy 인증·기존 소스 bundle·복구 입력 준비 | 아래 §2. 인증 경로는 이번 읽기로 확인. 새 Push receipt·최종 대상/창·복구 범위가 필요. Push 전 가능한 준비는 계속 |
| 3 | OID03 경로와 ICR 부팅 잔여의 분리 | 아래 §3. OID02 실제 반입은 재수행하지 않음. 공급물·경로·보호 처분만 좁혀서 결정 |
| 4 | Runner 감시/알림과 O02 실운영 인수 | 아래 §4. 기존 분류기·운영자 카드는 재개발하지 않음. 실제 필요한 다음 Job에 제2운영자 인수를 결합 |
| 병행 | DB/DR/C01/Grafana 기존 회신 | [PR164][b164] D1/C1/C2/G1/G2 사용. 같은 질문을 새 PR에 복제하지 않음 |

Harbor 운영 manager/H6는 별도 구축 세션의 담당 범위다. 이 문서는 Harbor 구현·작업창을 점유하지 않는다. 실제 Push/Deploy/장애 시험은 그 변경·사후 관측과 비중첩을 직전에 확인한다.09:00은 이번 병행 작업의 정리 시각이며, 별도로 허용된 Push의10:00 시작한도·12:00 종료창을09:00으로 되돌리지 않는다.

이미 실제 종료한 APP4개 분산 복구, K8S17파일 교체, OID02 archive2개/8조합 반입, worker02 DNS 단일 회차와 MON IF06B canary는 각각 [증적208][e208]·[증적207][e207]의 원본을 소비한다. 리뷰 대기라는 이유로 재실행하지 않는다. 실제 실행 완료·증적 리뷰·AC 인수는 별개다.

## 2. Deploy — 인증 미확인 해소와 정확한 다음 단계

### 2.1 새로 확인한 기존 경로

[04:26 읽기 원본][newread]에서 CP1 server02의 기존 authorized_keys 공개 지문과 ansible01의 기존 id_ed25519.pub가 일치했다. 해당 키로 strict host-key를 유지한 정상 계정 로그인, 공개 CA 해시, 기존 kubeconfig를 사용한 named SA GET rc0를 확인했다. 새 키/신뢰/계정/RBAC를 만들지 않았다.03:13 다른 키(p1_ansible_ed25519)의 실패는 원본 이력으로 보존한다.

| 입력 | 확인값 / 적용 범위 |
|---|---|
| broker 실행자 | ansible01 / server01_ansible, 기존 HOME |
| CP1 대상·키 | `server02@10.1.93.102`, controller의 `/home/server01_ansible/.ssh/id_ed25519` |
| Runner 대상·키 | `server01_cicd-runner@10.250.10.20`, controller의 `/home/server01_ansible/.ssh/p1_ansible_ed25519`; [03:13 기존 성공 원본][runnerread] 재사용 |
| CP1 CA | `/home/server02/FDS_CICD_PublicCA.uua3ecs6/kubernetes-ca.pem` |
| Runner CA | `/home/server01_cicd-runner/runner-tls-a9c89a77-20261006/kubernetes-ca.pem` |
| CA SHA256 | `5e4462b48b67aa3c452119f02578feb5b2ace358782c9b050ba0ad2ea951a49c` |
| API / SA | `https://10.1.93.109:6443`, `ci-cd/cicd-runner-sa`, UID `8f1ddfef-7bec-4b15-8cb7-c4b1a068a176` |
| 검토 소스 bundle | source2d8a14c의 Git blob7개, SHA256 `8cfdcce5e4b5eb95001d27e35606e5121edf77d8c2c1f5f481016c79933baa5c`; [manifest와 원본][newread] |

이 인증 관측은 **native broker staging/TokenRequest/TokenReview/Runner SA 소비 성공이 아니다**. 임시 서버 파일 배치도 미실행이다. 기존07-module bundle은 remote source용이며, controller는 같은 commit의 검토된 broker·의존 모듈을 함께 사용한다. bundle만으로 모든 controller 실행파일을 받았다고 간주하지 않는다.

### 2.2 새 Push 후 한 번에 확정할 입력

현재 APP Source affbc69의 두 이미지 후보와 기존 TBS37890963668은 이미 확정돼 있다. [APP Lead 입력 결정][appinput]을 다시 승인받지 않는다. 그러나 **새 Push Run/Attempt·remote digest·정리까지 결속된 receipt는 아직 없다**. 옛 Push 결과나 Build Run으로 채우지 않는다.

1. 새 Push receipt 원문·SHA256·실제 실행 context와 두 이미지 remote digest를 대조한다. 미완료/부분 Push면 Deploy0, claim/증적 보존.
2. 실행 직전 두 Deployment의 UID·현재 image/spec·replica/readiness, SA UID·CA·현재 main SHA·동시 변경 부재를 다시 읽는다.03:10 스냅샷을 고정 최신값으로 쓰지 않는다.
3. 새 plan UUID, exact plan bytes/hash, 실제 Deploy 창과 복구 범위를 하나로 확정한다. v2 계획은 미래 Deploy Run ID를 요구하지 않는다. Run은 실제 dispatch 뒤 결속한다.
4. 승인 원문은 기존 코드가 검증하는 CICD11의 GWONUK exact JSON 한 건으로 연결한다. 이는 사용자의 구체 실행 결정 기록이며 새 타 담당자 Lead GO가 아니다. 이 PR의 문서 리뷰를 실제 배포·토큰 발급 허용으로 표시하지 않는다.
5. [기존 명령 카드][deploycard]의 `execute=false` → 별도 `execute=true` → broker 전달 → 결과/claim/cleanup 순서를 사용한다. false는 Runner에 증적 디렉터리를 만들며 pure-read가 아니다. true의 broker 대기120초·요청/최대token900초 및 Session 예산은 기존 코드 그대로다.

**복구 검토:** 현재 이전 digest는 engine `5e2a081c…67369`, API `a7093136…cc33`이다. 전체값은 [기존 관측][deliveryread]에 있다. 현재 코드에는 복귀 기능이 있으나 `allow_rollback`은 아직 승인값이 아니다. [APP27][app27]의 기존 설명대로 이전 이미지 복귀는 업무 포트 `/metrics` 노출도 복원한다. 정상/실패 시 DB TLS·업무 E2E/Ready·보안 종료 상태를 함께 정해야 하며, 단순 rollout Ready를 전체 인수로 쓰지 않는다. 이전 digest의 현재 공급 가능성·호환성 확인과 이 한계의 처리 범위만 검토한다. Source 전체 Unit/Build를 새로 반복하지 않는다.

실패·발급 결과 불명확이면 같은 plan/claim 삭제·재사용·자동 rerun을 하지 않는다. 해당 Workflow/result/journal과 실제 Deployment를 먼저 대조하고 회차 복구 범위 안에서 수동 인수한다. broker 종료만으로 token 미발급이나 Deploy 미실행을 단정하지 않는다.

## 3. OID03과 부팅 잔여 — 서로 다른 네 항목

| 항목 | 현재 근거 | 이번 처리 |
|---|---|---|
| OID02 두 system image | [02:18~02:20 실제 export/import][oid02], 현재 캐시를 복구 공급원으로 채택한 사용자 결정 | archive2개·8반입·6노드 cache 완료를 소비. 최초 공급 출처는 여전히 미확인으로 보존 |
| OID03 bootstrap/추가 egress | 기존 A06·[OID 결정 추적][oiddecision]의 미결 항목 | 새 외부통신이 필요한지와 승인할 공급 경로를 해당 소비 회차별로 결정. 아래 설치 관측은 입력일 뿐 |
| ICR-AC18 재부팅 후 지속성 | 기존 [V06](MINIMUM_VALIDATION.md#v06--icr-reboot-지속성과-oid-입력), 원래 K8S T16 | 기존 원본과 현재 정책 차이를 먼저 대조. 필요한 정확 노드/관측/복구 계획만 준비. 전체6노드 반복을 자동 추가하지 않음 |
| K8S AC4d② 부팅 중 연속 보호 | [SEC Lead의 기존 잔여 리스크 수용][bootrisk], H03에 Review Owner 확인 기록 없음 | 재부팅 후 정상과 구별. 기존 수용을 없었던 것으로 되돌리지 않고 Review Owner 인수 판단에 연결. 이 문서가 추가 bootstrap 방화벽을 자동 개발·도입하지 않음 |

04:28~04:29 [6노드 읽기][newread]에서 kubeadm/kubelet/kubectl `1.36.4-150500.1.1`, containerd.io `2.3.5-1.el10`의 RPM DB 소유 정보를 확인했다. 지정 cache `/var/cache/dnf`는 각28파일이며 관련 RPM0이었다. 다른 보관소 전체 부재를 증명하지 않는다. CP3대의 기존 경로에서 crictl을 찾지 못했고 Worker3대에는 RPM에 속하지 않은 파일이 있었다. 임의 도구 설치·업그레이드를 추가하지 않는다.

**권장 경로:** 기존 승인된 preloaded 모델과 이번 복구 공급원을 우선 소비한다. OID03에서 새 패키지 반입이 실제 필요한 경우에만 위 정확 버전·필수 의존성·원본/서명·SHA·반입 경로·소비/회수 책임을 갖춘 오프라인 공급안을 완성한다. 현재 설치 파일이나 RPM DB를 원 RPM archive로 치환하지 않는다. 외부 HTTPS가 불가피하다고 확인되면 그때 Source/Destination/port/Owner/Expiry와 회수 조건을 제한해 제안한다. 이 PR은 egress 개방이나 OID03 N/A/완료 결정이 아니다.

control01 drain 제한은 기존 결정의 해제 기록 없이 자동 해제하지 않는다. 현재 소프트웨어 설치·사전 이미지 적재만으로 재설치/재부팅 성공을 선언하지 않는다. 부팅의 별도 bootstrap 보호를 새 Phase1 필수 개발로 추가하거나 Phase2 작업을 끌어오지 않는다.

### 이번 검토에서 필요한 좁은 회신

- 이하영: 이미 없다고 답한 과거 공급 출처를 재요청하지 않는다. **알고 있는 현재 재사용 가능 패키지 공급원/경로가 있는 경우만 참조**를 연결한다. 없다면 미보유 범위를 유지하고 이권욱이 새 오프라인 공급안을 준비한다.
- Review Owner 이권욱: 기존 SEC 부팅 리스크 수용의 범위·한계·잔여 표기를 최종 인수안에서 어떻게 연결할지 기록한다. 문서 PR 리뷰를 대신 인수한 것으로 처리하지 않는다.
- 위 미결을 순수 읽기, 준비물 작성, 독립 Runner 작업의 공통 gate로 삼지 않는다. 실제 reboot/새 egress의 구체 실행 허용은 해당 대상·변경·복구점이 정해진 안에서만 판단한다.

## 4. Runner — 남은 운영 기능과 O02를 한 회차에 결합

[Ansible61][a61]과 main의 [운영자 카드][opcard]를 대조했다. `ansible-ci-queue-watch.py`는 **Job 하나를 한 번 조회**하고 JSON/rc0·2·1을 반환한다. scheduler·담당 알림 발송은 구현하지 않는다. 이미 있는 source/HEAD 대조·중복 공급 방지·STOP·실패 분류·정리는 재개발하지 않는다.

현재 미결은 감시 실행 위치/주기·threshold·담당/대체자·연락 경로·실패 시 전달과 **제2운영자의 실제 공급/인증/회수**다. 원 담당자가 참여 의사를 확정하지 않았다는 기존 사실을 유지한다. 이름 배정·문서 열람이나 이권욱의 재실행을 두 번째 사람의 실적으로 세지 않는다.

준비 순서:

1. 기존 읽기 분류기를 재사용하는 최소 감시·상태변경 알림 방식을 별도 구현/검토한다. 토큰 발급·Runner 등록/삭제·Job rerun/cancel 자동화나 상시 ansible-isolated Runner는 추가하지 않는다. 지속 배치·권한/연락 경로는 검토 전에 켜지 않는다.
2. 업무상 실제 필요한 다음 Ansible 변경 PR의 exact HEAD/Run/Attempt/Job이 생기면 회차 카드를 고정한다. 제2운영자는 자신의 기존 정상 계정/인증 경로를 사용하고 승인된 v1.3 공급·회수 절차를 수행한다. 특정한 실제 Job이 없을 때 참여 시간·시행 완료를 꾸미지 않는다.
3. 같은 회차에서 감시 판단→담당 전달/수신→preflight→필요한 공급→실제 regression/upload→정리의 각 증거를 연결한다. 완료된 PR75/76/77 Job을 교육/증적 확보만을 위해 재실행하지 않는다.
4. 회차 뒤 Runner/proxy/workspace·양단 token packet 부재, raw/archive/hash 보관, 실제 참여자와 인수 범위를 기록한다. ephemeral Runner0은 정상일 수 있고 CI PASS/공급·정리/운영 이중화 인수는 따로 판정한다.

O01 제3자 Runbook 재현과 O02는 증거·적격성이 맞는 경우 같은 실제 작업을 소비할 수 있지만, 둘을 자동 동일 완료로 처리하지 않는다. C01 공유 실효 ACL은 [PR164][b164]에서 계속 받으며 Runner 기능 구현의 선행조건으로 확대하지 않는다.

## 5. 검토·완료 경계

이 PR은 구체 입력·원본 연결·최소 후속 범위의 검토안이다. 검토자는 이하영(K8S/SEC/OID 경계), 이재환(APP 복귀·업무 회귀/운영 인수)이다. 기존 확정값·미보유 자료를 반복 회신할 필요 없이 **사실 오류, 알려진 현재 공급원, 실제 복귀 검증에 추가로 필요한 항목**만 해당 절에 남긴다. 운영자 참여는 실제 Job 카드가 나온 뒤 기존 약속대로 확인한다.

STATIC: 새 문서와 링크·고정 소스 대조. RUNTIME_READ:04:26 정상 CP1 인증/SA GET 및04:28~29 6노드 metadata 수집. 신규 Token/배포/재부팅/정책/Runner 공급은 미실행. 읽기 원본 검토는 [증적208][e208], DB/DR/C01/Grafana는 [PR164][b164]를 사용한다. 이번 문서 때문에 변경 없는 소스 전체를 재리뷰하거나 새 공통 GO를 추가하지 않는다.

[e208]: https://github.com/321Team/fds-project-evidence/pull/208
[e207]: https://github.com/321Team/fds-project-evidence/pull/207
[b164]: https://github.com/321Team/fds-project-baseline/pull/164
[newread]: https://github.com/321Team/fds-project-evidence/blob/ca36895cba0a1ebbb43df6b25480ffdf9b11c236/evidence/P1-CICD-01/parallel-readiness-20261013T0426/README.md
[runnerread]: https://github.com/321Team/fds-project-evidence/blob/e4d934bb2b15c1027db2389989bf5238064462f5/evidence/P1-CICD-01/delivery-runner-readiness-20261013T031012/runner-auth/receipt.json
[deliveryread]: https://github.com/321Team/fds-project-evidence/blob/e4d934bb2b15c1027db2389989bf5238064462f5/evidence/P1-CICD-01/delivery-runner-readiness-20261013T031012/INPUTS.observed.json
[oid02]: https://github.com/321Team/fds-project-evidence/blob/a7083cf8e86980b4bce9c48c9b24bfb3ff0bf2c3/records/p1-oid02-preload-20261013.md
[appinput]: https://github.com/321Team/infra-cicd/issues/11#issuecomment-6074515472
[app27]: https://github.com/321Team/fds-msa/pull/27
[deploycard]: https://github.com/321Team/infra-cicd/blob/2d8a14c55ea4b61f53b7ac6d682cd5e97575dda7/docs/deploy-workflow-handoff.md
[oiddecision]: https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6035816841
[bootrisk]: https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5855751710
[a61]: https://github.com/321Team/infra-ansible/issues/61
[opcard]: https://github.com/321Team/infra-ansible/blob/2381e0228838971640788c3bf8b11385a9e52fc1/docs/runbooks/Ansible-CI-Operator-Card.md
