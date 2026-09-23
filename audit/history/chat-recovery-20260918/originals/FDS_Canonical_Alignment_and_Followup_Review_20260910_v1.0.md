# FDS 정본 정합성 및 CP2·NTP 후속 검토 결과 v1.0

- 검토일: 2026-09-10. GitHub 반영 확인: 08:49 UTC / 17:49 KST.
- 주관: 이권욱. PR #2·#4 독립 리뷰어: 이하영(hayeounglee).
- 범위: 승인 정본과 현재 PR 코드·절차 대조, 제출 증적 검증, CP2 재개 분기와 NTP 미확정 입력 정리.
- 판정: **읽기 전용 검토 완료 / 현재 PR #2·#4 운영 적용 보류 / 정본·AC 유지**.
- 이 검토는 독립 리뷰 승인 또는 실서버 적용 결과가 아니다. 이 환경에서 lab SSH·방화벽 변경·join/reset은 수행하지 않았다.

## 1. 핵심 결론

기존 변경안에서 **D34 전환 순서와 ICR Runtime/Permanent 반영 순서의 불일치 2건**을 확인했다. PR 본문에 조건을 적는 것만으로 코드·실행 절차의 불일치가 해소되지는 않는다. 현재 HEAD의 적용 가능 판정을 보류하고 수정 요구사항을 기록했다.

CP2는 마지막 수집 기준으로 클러스터 미등록이지만 매니페스트가 남아 있는 분기에 해당한다. NTP는 6대가 같은 pool 설정을 사용하고 당시 선택 주소는 4종이다. 고정 NTP 목적지와 수치 인수조건은 조사한 기록에서 승인 근거를 찾지 못했다.

## 2. 검토 기준과 소스 고정

| 구분 | 고정 기준 |
|---|---|
| RELEASED 정본 | docs-v3.1.17 |
| baseline main | `2d93395a0e19ea67e5be199d7183a7edbaa6cf4c` |
| Baseline | FDS_Project_Implementation_Baseline_v3.1.17.md §6.6, §15, D34/D35 |
| 등록된 ICR 정본 | ICR-D-NET-01-01 Kubernetes Node Host Firewall / Monitoring Route Change v1.4 |
| PR #2 | `068661e076de02669170d3582f3d596d6e1a8eb3` |
| PR #4 | `de9a3a30fd691ac30a0e03c4212c21300653e088` |
| 소스 대조 | PR #2 변경 파일 15/15, PR #4 11/11 로컬 내용의 Git blob SHA가 GitHub와 일치 |
| 독립 리뷰 | PR #2·#4 모두 Ready, hayeounglee 요청 유지, 제출된 리뷰 각각 0건, 미병합 |

[RELEASED 정본](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md)과 그 문서 등록표의 ICR v1.4를 기준으로 삼았다. FDS_P1-K8S-01_Lead_Final_v4.0.md의 RUNBOOK §3·ICR_ADDENDUM·입력 및 시험 명세도 대조했다. 이 후속 문서는 전환 순서 교체를 **제안**하며 문서 작성 자체를 정본 변경 승인으로 보지 않는다고 명시한다.

검토 범위 내 정본, ICR v1.4, Lead Final v4.0 해당 절, GitHub #10/#14 본문과 #14 댓글, PR #2/#4에서 제안된 순서 변경의 확정 승인 기록은 확인되지 않았다. 확인되지 않은 승인을 새로 부여하거나 미발행 v3.1.18을 정본으로 취급하지 않았다.

## 3. 정합성 매핑 및 수정 요구사항

| ID | 기준과 관측 | 판정 | 담당·후속 |
|---|---|---|---|
| CA-01 | D34: Calico 설치 전 6대 firewalld OFF. PR #2 CP-PORTS §5: GNP/named HEP 검증 후 인계. PR #4는 CP1 보완·join 흐름을 전제로 함 | **운영 적용 보류 사유** | #14 이권욱 작성, #10 이하영 검토. 승인 정본을 유지하는 복구·정합화 절차를 먼저 구체화. Lead Final의 교체 제안을 승인된 절차로 승격하지 않음 |
| CA-02 | ICR v1.4: Runtime 시험·리뷰 후 Permanent. PR #2 apply_transaction과 PR #4 plan_for: permanent→runtime | **운영 적용 보류 사유** | #14 및 PR #2/#4. Runtime 적용, 시험 증적·리뷰, Permanent 반영을 별도 단계로 수정. 단순 루프 순서 교체로 해결되지 않음 |
| CA-03 | 11:30 KST CP1: calico-node Running, firewalld active, HEP 0/GNP 0 | **보호 인수 미완료** | #10/#14 현재 재관측, #19 보안 인수. 과거 수집으로 설치 당시 전체 실행 순서나 현재 상태까지 단정하지 않음 |
| CA-04 | PR #2 D34·독립 승인 자동 검사 없음. PR #4 승인 JSON은 사람의 기록이며 GitHub 승인을 인증하지 않음 | **수동 통제와 코드 보장의 경계 명시** | 운영자는 실제 리뷰 URL·HEAD·적용 조건을 대조. 현재 본문 조건이 코드 차단 기능이라고 표시하지 않음 |
| CA-05 | CP /32→2379–2380·10250 범위는 IF-12A/12B와 부합 | **범위 정합, Runtime 인수 미완료** | #10 CA/Auth·etcd health·logs/exec/port-forward, #14 실제 Source/Positive/Negative. IF-06 Prometheus·IF-06B를 별도로 유지 |
| CA-06 | CP2 Node/member 부재, CP 매니페스트 3개 잔존, 표준 etcd data·kubelet 설정 부재 | **잔여 구성 검토 분기** | #10 이하영 재개 판단, 이권욱 증적 정리 지원. 정리 대상·보존·복구를 특정하기 전 join/reset 반복 금지 |
| CA-07 | 같은 chrony pool 설정, 당시 선택 IP 4종. 고정 목적지·수치 AC 승인 미확인 | **결정 입력 미완료** | #14 목적지·운영 주체, #10 동기화 인수조건, #19 최소 egress 연계 |

### CA-01: 전환 순서

D34의 HEP/GNP 적용 순서는 **Bootstrap Allow → canary Worker → Worker 확대 → Control Plane**이다. PR #2의 CP1 방화벽 보완 canary는 다른 작업이며 이 순서를 대체하지 않는다.

[PR #2 CP 포트 절차 §5](https://github.com/321Team/infra-kubernetes/blob/068661e076de02669170d3582f3d596d6e1a8eb3/docs/runbooks/ICR-D-NET-01-01-CP-PORTS.md)의 “최종 인계” 표현은 D34의 설치 선행조건을 충분히 반영하지 않는다. Lead Final v4.0 RUNBOOK §3과 ICR_ADDENDUM은 firewalld 유지→Calico·6대 join→노드별 인계를 **순서 변경 제안**으로 명시한다. 정본을 훼손하지 말라는 이번 지시에 따라 이 제안을 채택하거나 정본 문구를 덮어쓰지 않는다.

이미 Calico가 관측된 CP1을 즉시 firewalld OFF로 바꾸는 것은 과거 순서를 복원하는 조치가 아니다. 현재 보호 경로·필수 통신·콘솔·복구 상태를 먼저 확인하고 현재 상태에서 정본 목표로 복귀하는 구체적인 절차를 검토해야 한다. CP1이 유일한 Node/voter였던 증적을 고려하여 무조건 재설치·reset·재부팅도 선택하지 않았다.

### CA-02: Runtime 검증 뒤 Permanent 반영

- [PR #2 cp-canary-node.py](https://github.com/321Team/infra-kubernetes/blob/068661e076de02669170d3582f3d596d6e1a8eb3/scripts/cp-canary-node.py)의 apply_transaction은 Permanent부터 편집한다.
- [PR #4 node-firewall.py](https://github.com/321Team/infra-kubernetes/blob/de9a3a30fd691ac30a0e03c4212c21300653e088/scripts/node-firewall.py)의 plan_for 역시 Permanent부터 작업 목록을 만든다.
- ICR v1.4의 핵심 요구사항·착수 가능 판정·구현 검증 순서는 Runtime Positive/Negative/Regression과 Reviewer 승인을 Permanent보다 앞에 둔다.

수정 시 필요한 계약은 다음과 같다. 이는 기존 ICR 요건을 구현에 반영하는 요구사항이며 새 정본 AC를 추가한 것이 아니다.

| 수정 대상 | 필요한 동작 |
|---|---|
| Runtime 단계 | 해당 plane의 작업·소유권·전후 상태만 기록하고 시험·리뷰 전 Permanent를 변경하지 않음 |
| 시험·검토 연결 | 정확한 노드·소스·정책·Runtime 영수증과 실제 Positive/Negative/Regression 결과 및 Reviewer 기록을 연결 |
| Permanent 단계 | 검토된 Runtime 상태와 현재 상태가 일치하는지 재확인하고 해당 변경만 반영 |
| 실패·복구 | Runtime/Permanent별 확실히 소유한 변경만 회수. 불명확한 작업은 조사 대상 유지 |
| PR #4 CP1 인수 | 현재의 “PR #2 고정 소스 + 12개 작업 영수증” 계약을 새 단계와 일관되게 재설계 |
| 검증·배포 | 승인 전 Permanent 변경 0건, drift/불명확 영수증 차단을 검증하고 변경된 HEAD로 독립 리뷰·배포 해시 갱신 |

현재 코드를 고치지 않고 두 plane의 순서만 문서에서 바꾸거나, 기존 12개 작업 영수증을 분리된 단계의 인수 증적으로 재사용해서는 안 된다. 이번에는 검토 대상 HEAD를 유지하고 위 수정 요구사항을 등록했다.

## 4. CP1·CP2 증적과 재개 분기

### 관측 시점

| 시각 | 증적·직접 확인 |
|---|---|
| 09/10 11:30 KST | glrr0dsq의 CP1 calico_pods rc=0: kube-system/calico-node-bqzx2, 1/1 Running. firewalld active. HEP/GNP 조회 rc=0, items=[] |
| 09/10 13:56 KST | jvgkgfm9 inspect: CP1만 Node Ready·etcd voter, API readyz 정상. CP2·CP3에서 CP1 2379/2380/10250 TCP 0/6, errno 113 |
| 09/10 15:11 KST | Worker full: CP→Worker 10250 TCP 0/9, Worker→LB6443 3/3 TCP. kubelet 설정·리스너와 방화벽을 함께 판단해야 함 |
| 09/10 15:34 KST | Worker supplement: kubelet 설정 부재로 재시작 반복, 10250 부재. Worker 3대 Cockpit 두 unit mask·inactive, 9090 부재. 6대 NTP 동기 상태 확인 |

Calico 관측은 단순 Ready 상태의 추측이 아니라 원본 calico_pods 조회 결과다. HEP/GNP 수는 11:30 시점이며 13:56·15:34 자료에서 다시 조회한 값으로 표시하지 않는다. TCP errno 113만으로 전체 실패의 유일한 원인을 확정하지 않는다.

### CP2(10.1.93.103), 13:56 KST

| 항목 | 관측 | 판단 |
|---|---|---|
| CP1 Node/member 목록 | CP1만 존재, CP2 없음 | 당시 CP2 미등록 |
| kube-apiserver.yaml | root, regular, 0600, 3659 bytes | 기존 진행 흔적 |
| kube-controller-manager.yaml | root, regular, 0600, 2939 bytes | 기존 진행 흔적 |
| kube-scheduler.yaml | root, regular, 0600, 1726 bytes | 기존 진행 흔적 |
| 세 파일 mtime | 09/09 12:52:32 UTC / 21:52:32 KST | 수정 시점 메타데이터이며 내용 검증 아님 |
| etcd.yaml·/var/lib/etcd·member | 부재 | 표준 경로에서만 확인 |
| kubelet config.yaml·kubeadm-flags.env·kubelet.conf·bootstrap-kubelet.conf | 모두 부재 | 정상 join 완료 근거 없음 |
| 원래 join stdout·실제 구성 | 미확보 | 최종 실패 원인·정리 대상을 확정할 수 없음 |

**선택한 분기: Node/member 없음 + 잔여 구성 있음.**

#10에서 기존 구성의 실제 주소·버전·data 경로를 민감정보 보호하에 확인하고 보존할 자료, 정리할 경로, 복구 방법을 정한 후 재개 방법을 검토한다. 표준 경로의 부재를 사용자 지정 data-dir 부재로 확대하지 않는다. 토큰·kubeconfig·인증서 본문은 PR/이슈에 게시하지 않는다.

실행 전 새 Node UID/member ID·name·peerURL·learner 및 API 상태와 CP2 메타데이터를 다시 확인해야 한다. jvgkgfm9는 inspect 결과이고 15분 유효 입력 기간도 지났으므로 apply 영수증이나 새 변경의 입력으로 쓰지 않는다.

## 5. NTP 승인 기록과 후속 입력

### 확인된 사실

15:11 KST full 수집에서 6대 chrony 설정 해시는 모두
`147346c1b876b87dfad3bd436c62bc137c36723137ed5b647cf376a9f54e66aa`로 같았다.

설정은 `pool 2.centos.pool.ntp.org`, `sourcedir /run/chrony-dhcp`이며 그 수집 시 DHCP sourcedir에는 파일이 없었다. “6대가 서로 다른 NTP 설정을 사용한다”는 판단은 이 증적과 맞지 않는다.

| 노드 | 15:11 KST 선택 source |
|---|---|
| CP1 | 1.230.135.74 |
| CP2 | 1.230.135.74 |
| CP3 | 1.230.135.74 |
| Worker01 | 3.39.176.65 |
| Worker02 | 193.123.243.2 |
| Worker03 | 211.108.117.211 |

위 주소들은 **관측값**이다. 고정 목적지 승인 목록으로 채택하지 않았다. 당시 chronyd active·Leap Normal이었으며 15:34 KST 보완에서 6/6 NTPSynchronized=yes 등을 확인했다. 보완 수집은 chrony source와 방화벽·TCP를 다시 조회하지 않았다. 개별 offset을 노드 간 실제 시차로 환산하지 않는다.

### 담당 매핑과 미확정 값

| 입력 | 주관·연계 | 현재 상태·필요 기록 |
|---|---|---|
| 승인 NTP endpoint | #14 이권욱, #10 이하영 검토 | 서버 주소/FQDN·실제 허용 IP 범위와 승인 근거 미확보 |
| NTP 운영 주체 | #14 조정 | 제공자·운영 담당자, 장애·교체·종료 및 DNS 주소 변경 처리 미확정 |
| 동기화 인수조건 | #10 이하영, #14 연계 | offset·관측 기간·허용 상태·실패/복구 기준의 승인 미확인 |
| 최소 egress·응답 정책 | #14 구현, #19 보안 검토 | 실제 승인 목적지와 Source/정책·응답 증적이 필요 |
| 설정 배포 | 승인된 입력을 받은 후 별도 후속 | 기존 #65 P1-ANS-01 Done 유지. 현재 common role·인수 완료 이력을 소급 변경하지 않음 |

PR #4 NTP_DECISION_PROPOSAL의 **100 ms, 60초 간격 6회, Stratum 1~15, Reach 비영(非零)**은 미승인 제안값이다. 이번 작업의 정본 AC나 자동 PASS 기준으로 사용하지 않는다. DNS .52/.53, 시험 예시 192.0.2.123/32도 실제 NTP 서버로 지정하지 않았다. 내부/외부 NTP 아키텍처 역시 임의 선정하지 않았다.

## 6. 증적 무결성

| 제출 묶음 | 외부 SHA-256 | 내부 체크섬 |
|---|---|---|
| FDS_CP_Log_Collection_glrr0dsq.tar.gz | `265e7d3fe04c8c215b8c76847bac769c5445682d788c3f9ad2bf9afef100c594` | 8/8 |
| FDS_CP1_Canary_jvgkgfm9.tar.gz | `45a23e3039a37edf4ee17a540263a1a3c558ab1e0d50b7aa2f783f0fa8f61b55` | 5/5 |
| FDS_Worker_Followup__fqs5007.tar(1).gz | `cfbc39b698b7198ec7c3853d8c783527aeb241a5347a0378cc1152ce0481d42e` | 8/8 |
| FDS_Worker_Supplement_mse3803h.tar.gz | `38fa093a0ed2d28fe782932bf4ee694fa3d1007f5c0f3a1baee36097a1aa8b0b` | 8/8 |

외부 SHA는 제공된 sidecar와 각각 일치하며 내부 합계는 29/29다. Worker 중복 업로드의 파일명 (1) 차이는 원본 파일명과 내용 해시를 구분해 처리했다. 해시 일치는 무결성 확인이며 수집 범위 밖의 운영 성공을 증명하지 않는다.

PR #4의 기존 31/31 모의 테스트 PASS는 코드의 해당 분기 검증 기록이다. 이 정본 정합성 검토를 통과했다는 의미로 사용하지 않았다. 이번에는 문서·증적 분석을 위해 불필요한 모의 테스트를 재실행하지 않았다.

## 7. 실제 반영과 다음 작업

| 대상 | 반영 내용·확인 |
|---|---|
| [PR #2](https://github.com/321Team/infra-kubernetes/pull/2) | CA-01~07 및 현재 HEAD 적용 보류 기록. 소스 HEAD·Ready·리뷰 요청 보존 |
| [PR #4](https://github.com/321Team/infra-kubernetes/pull/4) | 동일 정합성 조건과 Permanent 단계·CP1 인수 계약 수정 요구 등록 |
| [#14](https://github.com/321Team/fds-project-baseline/issues/14) | 전체 매핑·수정 요구·NTP 미확정 입력 기록 |
| [#10](https://github.com/321Team/fds-project-baseline/issues/10) | CP2 잔여 구성 분기·Kubernetes 재개 선행조건 기록 |
| [#19](https://github.com/321Team/fds-project-baseline/issues/19) | 실제 HEP/GNP 미구현 관측과 Cockpit 증적 경계·NTP 정책 연계 기록 |

5건 모두 본문 재조회로 반영을 확인했다. PR의 HEAD/base/상태/리뷰 요청과 이슈의 제목/상태/담당자/라벨/마일스톤은 보존했다. 정본 저장소 코드·WBS·기존 AC·Done 이력은 변경하지 않았다. 각 본문의 `fds-canonical-audit-20260910` 블록이 이번 검토 결과이며, 과거 적용 순서 안내보다 우선하는 후속 조건으로 기록했다.

다음 작업 우선순위는 (1) CA-01에 대한 현재 상태·보호 경로 및 정본 복귀 절차 구체화, (2) CA-02 단계 분리 수정과 정확한 새 HEAD 독립 리뷰, (3) CP2 실제 구성·원래 join 증적 보완, (4) NTP 승인 입력 확정이다. 런타임 실행은 정합성 해결, 실제 독립 리뷰와 기존 ICR의 실행 조건이 충족된 뒤 판단한다.

