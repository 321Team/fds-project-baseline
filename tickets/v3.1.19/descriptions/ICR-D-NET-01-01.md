# ICR-D-NET-01-01 — Kubernetes Node Host Firewall / Monitoring Route

> v3.1.19 CANDIDATE / NOT RELEASED · 2026-09-17 20:28 KST

## 현행 속성

| Property | 입력값 |
|---|---|
| Record ID | ICR-D-NET-01-01 |
| Phase | Phase 1 |
| Category | Network / Interface Change Control |
| Type | Change Request |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-01 |
| End | 2026-09-21 |
| Calendar Days | 21 |
| Working Days | 15 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Kubernetes 6개 Node의 보호 공백 없는 firewalld→Calico named HEP/GNP 전환, 30080/9100/10250 최소 허용, 관리망 반환 경로와 IF-06B 정합화, Positive/Negative/Regression/Reboot/Rollback 및 무결성 Evidence 완료 |
| Related Decision IDs | D17; D18; D33; D34; D35 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline v3.1.19 CANDIDATE; GitHub #14 @ 2026-09-17T08:44:15Z; 원문 SHA256 8781857eee4de81d8e5c0df4360ace9516045ba3cf86a9d38ec69af4797b564e |
| Schedule Note | 09-21은 권장 Plan End이며 실제 종료일 확정이나 AC 완료가 아니다. 기존 End TBD 이력은 보존한다. CP→Worker·NTP·IF-16을 먼저, IF-06B·Negative/Reboot/Rollback·보호 인계를 후속 검증한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

## 상태와 인수 경계

CP1 CNI 제한 진단·회수·인수와 6대 최종 HEP/GNP 보호 전환을 구분한다. 운영 후보·영수증 소비자·CP2/CP3 인수 미결을 보존하며 6/6 Ready로 확대하지 않는다.

- GitHub lifecycle: open; Milestone: G2 Security / Feature Ready
- 일정은 조정 가능한 계획이며 실제 완료일·Gate 승인일과 구분한다.
- 원문·후속 댓글: [원본 티켓](https://github.com/321Team/fds-project-baseline/issues/14), [고정 수집본](../sources/issue-14.json).
- 상위 속성표는 이 후보의 현행 표다. 아래 원문은 수집 시점의 변경/승인/AC 이력이며 과거 버전 문구를 현재 발행 상태로 사용하지 않는다.

## 원문 보존

<details>
<summary>수집한 GitHub 본문 전체 — SHA256 8781857eee4de81d8e5c0df4360ace9516045ba3cf86a9d38ec69af4797b564e</summary>

<!-- fds-icr-followup:2026-09-15:start -->
## 진행률·후속 보완 — 2026-09-17

**현재 위치:** 정본 v18·v19 승인 입력에 따른 진단 단순화와 운영 보완 준비를 유지한다. 최신 PR #11 HEAD `ed53205`는 배포 인수 양식의 오래된 생산자 pin·runbook·manifest를 수정했고 **61/61 STATIC/MOCK PASS**다. 실행 코드·방화벽 정책·원 영수증·상태 비교는 변경하지 않았다. [독립 리뷰](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5700011880)에서 9/17 00:25 KST `ed53205` 인수 양식·명세 증분을 댓글 승인했다. 현재 HEAD formal APPROVED·운영 실행 승인은 별개이며, Join 일정 확정은 아래 선행조건 해소 전 보류다. 후속 [Draft PR #13](https://github.com/321Team/infra-kubernetes/pull/13) `ac30186`에 원 영수증 인계 검사·읽기 전용 일괄 수집·public 유지 후보 생성을 구현했다(**109/109 STATIC/MOCK**, 별도 공식 함수 매치 18건). 후보는 고정 veth 목록이며 새 Pod/Join 지속 정책이 아니다. 실제 적용/회수·후속 연결·kernel 검증은 미완료다. PR #11 승인 소스와 새 리뷰 요청 보류를 유지한다. R5 격리 normal **6개 흐름·원복·disarm·unit 정리 완료**, R6 `1c9d17e` **286/286 STATIC/MOCK**는 보존하며 R6 실제 VM 검증은 미수행이다. 추가 범용 기능·VM 반복 시험은 보류한다. 실제 Calico는 최신 현장 증거 기준 **3/5 PASS·직접 Pod HTTP 2건 FAIL**이다. 운영 허용 범위·HOST/외부 경로 보존·유지 기간·회수 종료 상태·Positive/Negative/Regression·새 상태 영수증/소비자 구현은 미완료다. 기존 zone안과 새 /26·고정 veth 집합안은 미승인 후보이며 기존 제한 진단 승인을 승계하지 않는다. **CP1 인수·CP2/CP3 실제 변경/Join·AC 보류**. Worker 준비는 병행, **HEP/GNP Runtime은 6/6 Ready 후 별도 승인/실행창**이다. [v19 후보 수집](https://github.com/321Team/fds-project-baseline/blob/48b8d836e74a723ea145360f63456de0d4183f96/audit/v3.1.19/intake/icr-cni-simplification-20260916.md)은 준비 보완 기록이며 운영 정본은 v3.1.18이다. 아래 과거 기록은 당시 이력이다.

**진행률:** 핵심 요구사항 **2/11(18.2%)**, 전체 AC **0/20(0%)** 유지. 서로 다른 분모이므로 합산하지 않는다. 하단 현행 Description의 선행 완료 13건과 AC-01/08/10/19/20 부분 완료 판정은 유지한다. 아래 격리 시험 준비 체크는 별도 준비 이력이며 요구사항·AC 완료에 가산하지 않는다. 전체 작업량의 가중 진행률은 미정이다.

- **PR #9:** 이하영이 최신 HEAD `b3f3374ba71a754f15f69a5cc3a471bd61c79424`를 정식 APPROVED하고 JSON 마스킹 Must-fix 해소를 확인했다. **2026-09-15 10:15:44 KST 병합 완료**, merge `c08b798c858dfdabb2e9e4d58716d299fd2d5084`. 승인 코드와 main tree 동일 확인. 기존 Node 71 / Worker 21 / locale 2 PASS 유지; 해당 HEAD의 CI status/check run/workflow는 0건으로 CI PASS는 아니다. [독립 재검증](https://github.com/321Team/infra-kubernetes/pull/9#pullrequestreview-5204506470) · [병합 기록](https://github.com/321Team/infra-kubernetes/pull/9#issuecomment-5673182602)
- **CNI 도구:** 기존 `--until` 수동 입력을 제거하고, 로컬 사전 점검 후 실행 시작 기준 최대 20분·마지막 3분 정리/사후 확인을 구현한 개정 키트 배포. 원격 잔여시간 승계·시계 변동·명령 및 snapshot 제한·정리 실패·증적 마스킹 등 로컬/모의시험 14 PASS. 이전 본문의 ‘자동 제한 미구현’은 9월 14일 당시 기록이다.
- **현장 상태:** 2026-09-15 **10:22:11–10:22:48 KST**, `p3dmjivl` CNI 실제 시험 완료. **3/5 PASS / 전체 FAIL**: Pod IP 직접 HTTP 양방향 2개는 `Host is unreachable`; Service HTTP·양쪽 Pod DNS 3개는 PASS. 외부·내부 2개·키트 8개 해시 일치, Kubernetes 명령 31개 rc=0·잘림 없음. 임시 Namespace 삭제 후 부재 확인, 전후 firewalld는 CP1 최종 재적용 기준과 동일, CP1 Ready·API 정상 및 시스템 Pod 9개 UID/재시작 수 동일. [결과 검토](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5673301524)
- **후속 진단 — 10:39 KST:** `7aqtz7d4` 무결성·수집기 소스 일치. 26개 조회 중 23개 rc=0·3개 rc=1·잘림 0. **STATIC: firewalld가 DNAT는 선행 허용하나 cali→cali 직접 전달을 reject하는 경로 확인**. 실제 실패 당시 packet trace는 미확보이므로 특정 패킷 hit/유일 원인 확정과 구분한다. CP1 Ready·API 정상, 시스템 Pod 9개 UID/재시작 수 및 Trial Namespace 부재 유지. `vxlan.calico`의 NM-managed=yes는 별도 설정 대조 대상으로 기록한다. [진단 검토](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5673425463)
- **보완 수집 완료 — 10:53 KST:** `kav4i4cv` 외부·내부·수집기 해시 일치, **3/3 rc=0·stderr/잘림 없음**. 실제 iptables 소유 패키지·native 규칙·NetworkManager 디스크 설정 확보로 추가 수집을 마쳤다. iptables-save 호출 오류는 해소됐으며 디스크 설정과 실행 중 데몬 반영은 구분한다. 새 CNI 시험·서버 변경·건강 재확인은 없고 마지막 건강 확인은 10:39 KST다. [보완 검토](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5673570001)
- **보완 설계 PR 승인·병합:** [infra-kubernetes #10](https://github.com/321Team/infra-kubernetes/pull/10)의 HEAD `c073f837b324b50e14bfeda92b01e8ed150d4d3d`에 이하영의 [정식 APPROVED](https://github.com/321Team/infra-kubernetes/pull/10#pullrequestreview-5205541379)가 등록됐고, [13:39 KST 댓글](https://github.com/321Team/infra-kubernetes/pull/10#issuecomment-5674822164)에서 추가 인터페이스 제한 설계를 조건 없이 수용했다. **2026-09-15 13:45:20 KST 병합 완료**, merge `085b0a3ea0ce9e47b4f52c72bf765e4ba8f8e5ef`; 병합 tree와 승인 HEAD tree 동일 확인. 설계 문서·proposal JSON 2개만 변경했고 해당 HEAD의 commit status/check run은 각 0건으로 CI PASS는 아니다. 시험 Pod의 정확한 /32 주소 사용은 실행기 구현 시 반영 권고이며 착수 차단 조건이 아니다. 기존 진단용 예외 4조건과 완전 회수·consumer 확장 제외를 유지한다. **설계 REVIEW/MERGE 완료; 실행기는 아래 별도 PR로 제출했으며 새 운영 CP1 진단 변경은 미착수**. 문서/JSON의 승인 대기 표시는 제출 당시 기록이며 [현재 승인·병합 기록](https://github.com/321Team/infra-kubernetes/pull/10#issuecomment-5674870196)을 우선한다.
- **진단 실행기 구현·리뷰 요청:** [infra-kubernetes PR #11](https://github.com/321Team/infra-kubernetes/pull/11), HEAD `101cdb28248839f88ca8f7e33d3c0a505bb55218`에 실행기·독립 systemd 회수·영속 변경 의도/복원·증적·운영 절차를 제출하고 이하영(hayeounglee)에게 코드 리뷰를 요청했다. 시험 Pod의 정확한 veth 2개와 양방향 /32 TCP8080 제한을 구현했다. **STATIC/MOCK 83개 PASS**(모의 변경 24위치 직전/직후 중단 48개 포함); 기존 helper/controller·영수증·consumer는 변경하지 않았다. **Linux 통합시험·CP1 Runtime은 미수행**, 현재 실행 환경의 systemd/네트워크 capability 부재를 명시했다. 해당 HEAD check run은 확인 시점 0건이며 CI PASS로 집계하지 않는다. 실제 격리 통합 증적·고정 실행 HEAD 리뷰·실행 결정이 남아 있다. CP1 물리/터널 등 비-peer Negative는 NOT_TESTED이며 mock 또는 구조 확인으로 실제 packet hit를 대체하지 않는다. [운영 절차·실행 조건](https://github.com/321Team/infra-kubernetes/blob/101cdb28248839f88ca8f7e33d3c0a505bb55218/docs/runbooks/CP1_CNI_DIAGNOSTIC.md).
- **독립 리뷰 후속·격리 시험 준비:** [이하영 검토 댓글](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5675589656)은 상황·코드 검토이며 정식 APPROVED는 아직 미확보다. PR #11 준비 수집기 제출 HEAD `69c0a7e883861ac437e8312fca5e301b33103745`에 읽기 전용 후보 VM 수집기·시험 절차를 반영했다. **새 준비 경계 시험 6개 PASS**, 현재 환경 준비 수집은 **PREPARATION_BLOCKED**로 확인했고 전달·내부 해시 검증 완료. 기존 실행 core/node/controller/helper는 `101cdb2`와 동일하며 83개 모의시험을 재수행하지 않았다. **실제 격리 통합시험 진입점·시험 데이터 출처의 별도 구현/검토가 남아 있다**. 준비 수집은 qualification·실행 승인·AC를 생성하지 않으며 새 Linux 통합시험·CP1 변경은 미수행이다. [후속 기록](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5675696910) · [현장 준비 절차](https://github.com/321Team/infra-kubernetes/blob/69c0a7e883861ac437e8312fca5e301b33103745/docs/runbooks/CNI_ISOLATED_INTEGRATION.md).
- **격리 시험 호스트 선택:** 사용자 여유 자원 확인 후 **물리 server04**로 확정했다. 기존 CP3는 유지하고 별도 cp1-cni-lab을 준비한다. PR #11 HEAD `cb7fc695c294273bfd17106b89bcddf310e29750`에 [복사·격리·첫 부팅 절차](https://github.com/321Team/infra-kubernetes/blob/cb7fc695c294273bfd17106b89bcddf310e29750/docs/runbooks/CNI_ISOLATED_INTEGRATION.md)를 반영했다. 가이드만 변경했으며 실행/수집 코드는 동일하다. **제출 캡처로 시험 VM 등록·자원/LAN Segment 설정, 복제 디스크의 부모 참조/CID 연결, 첫 부팅·콘솔 로그인까지 확인했다. 17:46 준비 수집의 conntrack 미탐지는 오프라인 보완 후 18:20 새 증적에서 해소됐다. PREPARATION_REVIEW_REQUIRED이며 실제 통합시험은 미수행**이다. [선택 기록](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5676019368). 기존 진입점 구현·독립 승인·실제 증적 조건과 AC 보류는 유지한다.
- **인수 판정:** CP1 최종 ACCEPTED와 CP2 변경은 보류 유지. 기존 승인·병합·방화벽 적용/복구 증적 및 CNI 3/5 PASS·2건 FAIL 기록은 보존한다. 이번 진단의 PASS/FAIL·회수 완료로 어떤 AC도 완료 처리하지 않는다. policy 유지·최종 재적용·인수 연결과 이번 예외의 후속 consumer 확장 계획을 제거했으며, 회수 후 원 CP1 receipt.after로 복원한다. 진단 결과로 CNI 장애 해소를 가정하지 않는다.
- **커널 컴포넌트 후속 제출:** PR #11 HEAD `3f2b8c200313b329ef71e6b2f5977be509810a5d`에 새 격리 namespace/private firewalld·합성 peer 기반 실행기와 독립 회수·증적·가이드를 추가했다. **로컬 STATIC/MOCK 117 PASS = 진단 83 + 준비 6 + 신규 경계 28**. 기존 생산/준비 소스는 동일하다. 실제 VM 실행·CI PASS·정식 APPROVED는 미확보이며, 실제 VM NIC/터널/Calico 및 생산 adapter·복구 통합은 잔여 범위다. 전체 7개 흐름·6개 복구는 NOT_TESTED 유지, qualification·AC 완료를 생성하지 않는다. [후속 제출·리뷰 범위](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5678431122).
- **추가 inspect 검토 — 19:47:37 KST:** HEAD `3f2b8c200313b329ef71e6b2f5977be509810a5d`의 소스 4개 해시·참조 패키지 및 두 제출 JSON의 VM 식별 바인딩 일치. execution_approved=false, operator/snapshot_reference/review_url 미작성 초안 확인. 준비 완료이며 변경·패킷·회수 시험 성공이나 qualification/AC로 집계하지 않는다. 정식 리뷰 0건·미병합, 기존 리뷰 요청 유지. 기존 설치·준비 수집·동일 소스 inspect는 반복하지 않는다. [검토 근거](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5679020154).
- **재개 순서:** conntrack 보완·새 준비 증적·시험 snapshot·새 소스 추가 inspect 대조 완료 → K11-01~05 보완·회귀 제출 완료 → 새 HEAD 독립 해소 의견 확인 → 변경 소스 inspect/v2 decision 대조 → normal 한 건의 실제 packet/trace·회수 증적 검토 → 나머지 컴포넌트 복구 시나리오 및 실제 Calico·VM NIC/터널·생산 adapter 통합 경로 구현/검증 → 전체 격리 통합 증적·고정 실행 HEAD·실행 결정 확인 → 제한 진단·완전 회수·원 상태 복원 기록. Worker HEP/GNP 준비·검토·승인된 작업은 병행하며 이 진단을 선행조건이나 일정 지연 요인으로 두지 않는다. 운영 수정·CP1 최종 인수·CP2 적용 판단은 별도 승인된 수정/보호 전환안과 해당 상태의 실제 증적에 따른다. 최대 20분/마지막 3분 회수는 PR #11에 구현·모의 검증했으며 실제 Linux 동작 검증이 남았다. 완료된 보완 조회를 반복하지 않는다.

### 격리 시험 VM 준비 — 제출 캡처 확인 (2026-09-15)

근거는 채팅에 제출된 16:15:26 프로세스 조회와 파일명 기준 16:23:44·16:24:44·16:25:01·16:25:19 설정 캡처다. **준비 화면 관측이며 Linux 통합시험 또는 운영 CP1 증적이 아니다.** 아래 체크는 별도 사전 준비 기록으로, 기존 AC/핵심 요구사항 완료 수에 합산하지 않는다.

- [x] 사용자 선택 및 여유 자원 확인: 물리 **server04**, 기존 CP3 유지, 별도 시험 VM 배치.
- [x] 복제 폴더 안의 설정 파일 및 VMware 등록 확인: 표시 이름 **cp1-cni-lab**. 실제 관측 위치는 계획 경로 아래 `server02` 하위 폴더의 `server02.vmx`다. 폴더·파일 이름 유지 자체는 오류가 아니다. 전체 파일 무결성·디스크 독립성까지 확인한 것은 아니다.
- [x] 설정 화면에서 **CPU 4개, RAM 8192MB(8GB), NVMe 가상 디스크 250GB** 표시 확인. 250GB는 가상 디스크 용량이며 호스트 잔여 용량/실사용량이 아니다.
- [x] 설정 화면의 NIC **1개**, 연결 방식 **LAN segment → FDS-CNI-LAB**, **Connect at power on 체크** 확인. Bridged/NAT/Host-only/Custom은 선택되지 않았다. 18:19 제출 설정 화면에서도 FDS-CNI-LAB 및 Connected/Connect at power on 체크를 확인했다. 실제 격리 패킷 검증은 미수행이다.
- [x] 요약 화면의 **Powered off** 확인. 앞선 프로세스 조회에는 기존 VM 경로만 보였고 시험 복제본 경로는 없었다. `Connected`가 비활성인 것만으로 전원 OFF VM의 연결 실패를 판정하지 않는다.
- [x] **디스크 참조 확인:** 17:04/17:08 제출 캡처에서 연결 VMDK가 새 복제 폴더에 있고, 기본 디스크와 snapshot 3개의 parent 참조·CID 연결 및 데이터 파일 참조가 일치함을 확인했다. 외부 원본/백업 경로 직접 참조 없음. descriptor 확인 범위이며 디스크 전체 바이트 무결성·복원 시험은 아니다. [추가 검토](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5677481742).
- [x] **CD/DVD 권고 조치 확인:** 17:04 제출 캡처에서 ISO 선택 해제 및 CD/DVD Connect at power on 해제 확인. NIC의 Connect at power on은 별도 설정으로 유지한다.
- [x] **첫 부팅·준비 수집 제출:** 17:13 제출 캡처의 시험 VM 첫 부팅·콘솔 로그인·기존 hostname/IP·인터페이스/서비스 관측, 후속 고정 소스 반입·해시 4개 통과와 17:46:28 KST 준비 ARCHIVE/SIDECAR 제출·무결성 검토 완료. 당시 결과는 PREPARATION_BLOCKED였으며 conntrack 준비 차단은 아래 18:20 후속 증적에서 해소됐다. 실제 통합시험은 미실시. [검토](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5677481742).
- [x] **설치 전 시험 VM 복원점 확보:** Snapshot Manager 제출 화면에서 `FDS_CNI_LAB_PRE_CONNTRACK_20260915`, 생성 시각 18:18:15 KST 확인. 복원 실행 시험 완료를 뜻하지 않는다. [후속 검토](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5677964030)
- [x] **conntrack 오프라인 보완·새 준비 수집 검토:** 18:20:48 KST 증적 무결성·고정 소스·판정 재계산 일치, PREPARATION_REVIEW_REQUIRED / blockers=[]. 설치 완료는 별도 화면으로 확인했다. [후속 검토](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5677964030)
- [x] **커널 컴포넌트 진입점·검증 기록 제출:** HEAD `3f2b8c200313b329ef71e6b2f5977be509810a5d`에 격리 namespace/private firewalld·합성 peer 실행 및 소유 자원 회수·증적 수집을 구현했다. 로컬 STATIC/MOCK 117개 PASS(기존 83 + 준비 6 + 신규 28). 전체 통합시험 완성을 뜻하지 않는다. [제출 기록](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5678431122).
- [x] **새 소스 추가 inspect·결정 초안 검토:** 19:47:37 KST 수집 JSON 2개의 소스 4개 해시·참조 패키지·VM 식별 바인딩 일치. 실행 승인 false 및 담당자/스냅샷/리뷰 근거 미작성 초안 상태를 확인했다. [검토 기록](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5679020154).
- [x] **보완본 독립 코드 리뷰:** 21:45:58 KST 이하영 댓글로 HEAD `164f8d5`의 K11-01~05 해소 및 KERNEL_COMPONENT_ONLY normal 1회 진행 가능 의견 확인. 정식 APPROVED와 구분한다.
- [ ] **normal 실행 입력·후속 개선:** 새 source inspect·v2 reviewed_bundle_sha256/실행 결정 대조. UUID 반출 보호(High), stop/self-cleanup 경합(Medium) 별도 추적. 실제 Runtime 증적 및 정식 APPROVED는 미확보.
- [ ] **격리 커널 컴포넌트 실제 시험:** normal 한 건의 packet/trace·회수 검토 후 남은 중단·기한·재시도·재부팅 시나리오 및 증적 검토.
- [ ] **전체 격리 통합시험:** 실제 Calico·VM NIC/터널 fixture 및 생산 adapter·복구 경로 구현/검증, 전체 흐름 7개·복구 6개 증적과 qualification 독립 검토.

**리뷰 재확인 — 현재:** PR #11 HEAD `164f8d5514add1c845657e1abc500ababf37b1e9`, OPEN/미병합. **2026-09-15 21:45:58 KST 이하영 독립 댓글에서 K11-01~05 모두 해소, 해당 HEAD의 normal 1회 진행 가능 의견 확인.** 정식 GitHub APPROVED는 아직 없다. 별도 잔여는 UUID 평문 증적 반출 보호(High)와 강제 stop/self-cleanup 경합(Medium)이며, 후속 회수 시나리오/운영 승인으로 확대하지 않는다. 로컬 STATIC/MOCK 170 PASS 유지, 실제 VM 시험 미실행. auto_open이 존재하지 않는다는 비차단 설명은 CPython 원본·로컬 확인 근거로 정정했다. [독립 리뷰](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5680386800) · [후속 판정·정정](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5680440454).

### 격리 시험 VM 첫 부팅·준비 수집 — 17:46 당시 이력 (18:20 후속으로 준비 차단 해소)

**시험 VM 준비 수집 완료 / PREPARATION_BLOCKED.** `FDS_CNI_Integration_Preflight_7h73lmek`의 수집 시각은 **2026-09-15 17:46:28 KST**다. 운영 CP1의 새 상태 확인이나 실제 통합시험 결과가 아니다. [검토 기록](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5677481742)

- 외부 SHA256·내부 JSON 2개 체크섬·collector/core/node/helper 4개 소스·bundle hash 일치. 저장된 관측값으로 판정 함수를 재적용해 결과 일치 확인.
- 조회 12개 중 11개 실행: rc=0 10개, container 미감지의 정상 rc=1 1개. conntrack 버전 조회 1개 미실행; 시간초과·출력 잘림 없음.
- CentOS Stream 10/VMware, PID1 systemd, root 및 NET_ADMIN/NET_RAW, 기존 지정 패키지 4종 일치, firewalld/NM active 및 SELinux Enforcing 확인. 자동 확인 범위의 다른 준비 차단 없음.
- 남은 자동 준비 문제는 **conntrack 실행파일 미탐지**다. `MISSING_TOOL:conntrack`과 `INCOMPLETE_OR_FAILED_QUERY:conntrack_version`은 같은 미탐지에서 나온 두 표기다. 패키지 미설치·파일 유실 중 어느 경우인지는 아직 미확정이다.
- 다음은 시험 VM의 conntrack-tools 설치/파일 상태 조회 → 필요한 오프라인 보완 범위 확정이다. 현재 성공한 준비 조회 전체는 반복하지 않는다. 실제 변경 시험 전 복원점, 격리 통합시험 진입점·시험 데이터 출처의 구현/검토 및 패킷·독립 회수 시험은 남아 있다.
- 흐름 7개·회수 6개는 전부 NOT_TESTED. 실제 격리 통신, qualification, 실행 승인, AC 완료를 생성하지 않는다. PR #11 HEAD `cb7fc695c294273bfd17106b89bcddf310e29750` 변경 없음, 정식 리뷰 0건/APPROVED 미확보. CP1 최종 인수·CP2 변경 보류 및 Worker 병행 조건 유지.

Archive SHA256: `f12f456ee294f24e3fd4b3859772b84be89dbb7468f77c6c22c94b3c12234498`.

### 격리 시험 VM 오프라인 보완 후 재검토 — 2026-09-15 18:20 KST

**자동 준비 차단 해소 / PREPARATION_REVIEW_REQUIRED.** `FDS_CNI_Integration_Preflight_3873_0a1` 수집 시각 **18:20:48 KST**. [검토 기록](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5677964030)

- 외부 SHA256·내부 JSON 2개 해시·collector/core/node/helper 4개 고정 소스·bundle hash 일치. 저장된 관측값으로 판정을 재계산해 결과 동일 확인.
- 조회 12개 모두 실행: rc=0 11개, container 미감지의 정상 rc=1 1개. conntrack v1.4.8 조회 성공, blockers=[], 시간초과·출력 잘림·수집 오류 없음. 지정 참조 패키지 4종 일치, firewalld/NM active 및 SELinux Enforcing 유지.
- 별도 화면에서 RPM 4개 설치와 참조 패키지 유지, 설치 전 시험 snapshot 생성을 확인했다. 앞선 미설치 사유는 해소됐다. 화면·준비 수집으로 snapshot 복원 시험이나 실제 네트워크 격리까지 증명하지 않는다.
- 실제 흐름 7개·회수 6개는 모두 NOT_TESTED. qualification_created / execution_authorized / acceptance_criteria_credit / runtime_integration_executed는 false. 운영 CP1의 새 건강 증적이 아니다.
- 다음 작업은 실제 격리 통합시험 진입점과 시험 데이터 출처 구현·독립 리뷰, 이후 패킷 경로·독립 회수 시험이다. 기존 설치·준비 수집은 반복하지 않는다. PR #11 HEAD `cb7fc695c294273bfd17106b89bcddf310e29750` 변경 없음, OPEN/미병합·정식 리뷰 0건/APPROVED 미확보. CP1 최종 인수·CP2 보류 및 Worker 병행 유지.

Archive SHA256: `697a25eb763dead7464f1a374d5202e07ec4cf55de110d46c48683a65c74397a`.

기존 AC·상태·담당·일정·사양 점검 결과는 유지한다.
<!-- fds-icr-followup:2026-09-15:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** NTP·CNI trial·CP1 인수·CP2 조사/보호 경계와 IF 경로 ; A01/A02/A06. PR #9는 ICR 대응.

- CP1 최종 재적용 run 20260914T095827Z-7938c6e73fbd와 18:59 KST TCP6/6을 보존한다. 실제 CNI trial·최종 인수 전에는 전체 CP1 ACCEPTED/6노드 완료로 상향하지 않는다.
- PR #9는 ICR에서 대응한다. UTF-8/zone 수정의 수용 범위는 유지하고 accessToken/refreshToken/dbPassword/clientSecret/client-key/tls.key 등의 비밀값 마스킹 회귀와 serviceAccountToken 참조 객체 보존을 검증한 새 HEAD로 재검토한다.

**NTP 실행·인수 입력 (A01)** — 승인 시간 소스·운영 주체, 노드별 Source/Return·UDP123, 허용 오프셋·표본 주기/횟수·실패 처리·지속성 결과를 확정한다. `100ms·60초×6`은 미승인 초안이다. 해당 변경/인수 전 입력이며 읽기 전용 준비 전체의 신규 중단 조건이 아니다.
근거: [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14) · [K8S #10](https://github.com/321Team/fds-project-baseline/issues/10) · [SEC #19](https://github.com/321Team/fds-project-baseline/issues/19)

**CNI·MTU·CP1 인수 (A02)** — CP1 제한 Runtime 적용/롤백/최종 재적용과 TCP6/6 기록은 유지하되 최종 ACCEPTED는 CNI 회귀와 이하영 인수 회신 대기다. MTU1450은 후보이며 cross-node 실측으로 확정한다. trial의 시작부터 최대20분·마지막3분 정리 방향과 현재 `--until` 방식의 구현 차이를 추적한다. CP2 조사·보존/정리/재개 결정은 별도다.
근거: [CP1 인수 보류](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5662853042) · [ICR](https://github.com/321Team/fds-project-baseline/issues/14) · [PR #9 리뷰](https://github.com/321Team/infra-kubernetes/pull/9#pullrequestreview-5197580718)

**OID·IF-06B 경로 인계 (A06)** — OID-01 관리자 Source/Identity, OID-02 CP/Calico/system image source/Digest·pull 경로, OID-03 bootstrap 반입 또는 최소 HTTPS 목적지/Owner/Expiry를 해당 실행 전에 확정한다. IF-06B는 in-cluster Prometheus→monitor01 10.250.10.30:443으로 주소/방향이 확인됐다. 실제 Source/Return·TLS path/auth·Secret 참조·self-metric allowlist와 긍정/부정 결과가 필요하다. heartbeat=1·5분 단절 탐지는 확정값이며 OID-04 관리망 DNS N/A를 확대하지 않는다.
근거: [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14) · [MON #17](https://github.com/321Team/fds-project-baseline/issues/17) · [SEC 부분 수용](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5654476728)

**인계·관련 티켓:** [#10](https://github.com/321Team/fds-project-baseline/issues/10) · [#17](https://github.com/321Team/fds-project-baseline/issues/17) · [#19](https://github.com/321Team/fds-project-baseline/issues/19).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-cp1-cni-progress:2026-09-14:start -->
## 현재 운영 정리 — 2026-09-14

**In Progress 유지. CP1 Runtime 적용·복구·재적용 증적 검토 완료, 최종 인수 및 후속 노드 적용은 미완료.** 아래 9월 10일·12일의 소스/리뷰/미적용 표현은 당시 이력이며 현재 상태는 이 절과 연결된 최신 리뷰를 따른다.

### 완료·관측·준비 내역

| 구분 | 현재 확인 결과 |
|---|---|
| CP1 Runtime | 승인창 안에서 최초 적용 6개 → 제한된 허용/차단·기능 확인 → 별도 승인 rollback 6개 회수·원상복구 → 18:58 최종 재적용 6개 → 18:59 기본 상태·대상 통신 6/6 확인. 재적용 최종 run은 `20260914T095827Z-7938c6e73fbd`. Permanent 변경 미시도. [최종 증적 검토](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5662356251) |
| 증적 범위 | 최초 적용 때의 Negative·기능 증적과 재적용 이후 Positive·기본 상태 증적을 구분한다. 전체 CNI 회귀·재부팅 지속성·보호 전환 인수로 확대하지 않는다 |
| PR 상태 | [PR #2](https://github.com/321Team/infra-kubernetes/pull/2), [#4](https://github.com/321Team/infra-kubernetes/pull/4), [#8](https://github.com/321Team/infra-kubernetes/pull/8) 병합 완료. PR #3 기존 병합 완료 유지. 코드 병합과 Runtime 인수는 별개 |
| CP2 사전 점검 | `FDS_Node_Firewall_kivd3bsc`에서 외부/내부 무결성, 입력·소스·계획·정책 해시 검증 및 INSPECTION 생성 완료. 조회 기록 90개 rc=0, stderr·잘림 없음. CP1 방화벽이 최종 재적용 after와 동일. CP2 적용·Permanent·가입 미시도 |
| CP2 잔여 구성 | 기존 static manifest 3개 메타데이터 유지. 삭제/reset/재가입 미시행. 원 join 실패 단계·비표준 데이터 경로는 미확정이며 [P1-K8S-01 #10](https://github.com/321Team/fds-project-baseline/issues/10)에서 보존·재개 판단 |
| CNI 사전 수집 | `75ewn8ke`와 `v7nd98wj` 무결성 확인. 최신 수집에서 Kubernetes 조회 5개 성공, 시스템 Pod 9개 Running/Ready. crictl을 검사한 표준 경로에서 찾지 못해 이미지 캐시 직접 조회 미실시. 미설치/런타임 장애로 단정하지 않음. 재첨부 `v7nd98wj.tar(1).gz`는 같은 파일이며 새 실행이 아님 |
| CNI 실행안 | `FDS_CP1_CNI_Trial_20260914.zip` 준비·사용자 배포 완료. 임시 namespace 1개·Pod 2개·Service 1개, Pod 양방향/Service/DNS 및 정리·기본 상태 비교. 모의시험 6개·로컬 HTTP/DNS 판독 3개 확인. **실서버 실행 미수행**, 단일 노드이므로 cross-node는 NOT_TESTED |


### 승인·후속 실행 기준

- CP1 최종 인수는 **ACCEPTED 보류**: 이하영님은 CNI 회귀시험 결과 제출 후 최종 인수를 명시했다. [인수 조건](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5662853042)
- PR #9 HEAD `ccad9ce56c480cd3f5978e81257a8bb456aeac2c`에 **COMMENTED 리뷰 1건 / APPROVED 없음 / 미병합**. JSON 마스킹은 **Must-fix**이며, 사용자 지시 **“pr9번은 icr에서 대응”**에 따라 수정·회귀시험·독립 재리뷰를 이 ICR에서 추적한다. base/HEAD 직접 비교에서 accessToken·refreshToken·dbPassword는 신규 노출 회귀, clientSecret·client-key·tls.key는 기존 누락으로 구분했다. 광범위한 키 치환으로 serviceAccountToken 설정 객체·참조 구조를 지우지 않아야 한다. 관련 현행 시험 7 PASS, 실제 Ansible CLI 통합 1 SKIP(로컬 CLI 부재); 전체 64/21 시험·checksum manifest와 새로운 현장 실행은 이번 재검토 범위 밖이다. [이하영 리뷰](https://github.com/321Team/infra-kubernetes/pull/9#pullrequestreview-5197580718) · [재현·재검토 기록](https://github.com/321Team/infra-kubernetes/pull/9#issuecomment-5663953906)
- 기존 방화벽 작업의 19:00 KST 종료는 해당 실행창의 이력이다. CNI 시험의 별도 종료시각 입력은 Kubernetes 필수조건이나 새 Gate 요구가 아니라 시험 도구의 제한이다. 후속 운영 방향은 **실행 시작부터 최대 20분, 마지막 3분 정리**로 자동 제한하는 것. 다만 배포한 Trial ZIP은 아직 `--until` 입력 방식이며 자동 20분 방식의 코드 반영·검증은 미완료다. 이를 구현·실행 완료로 기록하지 않는다.
- CNI 시험 실제 실행 → 결과·범위 검토 → CP1 명시적 최종 인수, 그리고 PR #9 보완·승인 이후 CP2 제한 적용/검증을 진행한다. 가입·잔여 구성 정리 및 전체 보호 전환은 각각의 기존 절차를 따른다.

### 전체 잔여 범위

6대 가입·노드별 방화벽 후속 적용·named HEP/GNP 보호 전환, NTP·IF-06B·IF-16 및 전체 허용/차단/회귀/재부팅/복구 인수는 기존 AC로 계속 추적한다. HEP/GNP 미구성 관측을 최종 보호 인계 완료로 해석하지 않는다. 담당·일정·마일스톤·기존 AC 체크는 보존하며, 이번 갱신으로 완료일·새 승인·실행 결과를 생성하지 않는다.
<!-- fds-cp1-cni-progress:2026-09-14:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:14 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** G2 Security / Feature Ready (GitHub #3)
- **배정 성격:** WBS 기반 대표 추적 항목 · 이권욱 사용자 지시에 따른 지정.
- **배정 근거:** WBS Plan End 2026-09-21과 P1-SEC-01·P1-MON-01 및 G2 Runtime 영향에 따라 G2를 대표 추적 Milestone으로 배정한다. G1 관련 선행조건과 미결 Interface, Positive/Negative/Regression/Reboot/Rollback 증적·독립 리뷰 요건을 유지한다.
- **출처:** [발행 정본 v3.1.18 WBS · WBS/Fast Track Plan 시트](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/wbs/FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx)
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 근거 기록. 기존 상태·AC·담당·Start/End·Gate 요건과 보관 이력을 유지하며 새로운 Gate 필수조건을 추가하지 않는다.

---

<!-- fds-notion-migration:2026-09-09 record-id:ICR-D-NET-01-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:ICR-D-NET-01-01 -->
# ICR-D-NET-01-01 — Kubernetes Node Host Firewall / Monitoring Route

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | ICR-D-NET-01-01 |
| Phase | Phase 1 |
| Category | Network / Interface Change Control |
| Type | Change Request |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-01 |
| End | 2026-09-21 |
| Calendar Days | 21 |
| Working Days | 15 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Kubernetes 6개 Node의 보호 공백 없는 firewalld→Calico named HEP/GNP 전환, 30080/9100/10250 최소 허용, 관리망 반환 경로와 IF-06B 정합화, Positive/Negative/Regression/Reboot/Rollback 및 무결성 Evidence 완료 |
| Related Decision IDs | D17; D18; D33; D34; D35 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline/Ticket Pack v3.1.18; GitHub #14; PR #2/#3/#4/#8 병합 기록; PR #9 b3f3374 승인·merge c08b798; CP1 최종 재적용·CP2 inspect·CNI 준비 및 p3dmjivl 실측 FAIL 증적. 원 정본 수집 이력: audit/v3.1.18/k8s-intake-20260910.json |
| Schedule Note | 09-21은 권장 Plan End이며 실제 종료일 확정이나 AC 완료가 아니다. 기존 End TBD 이력은 보존한다. CP→Worker·NTP·IF-16을 먼저, IF-06B·Negative/Reboot/Rollback·보호 인계를 후속 검증한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |


<!-- fds-icr-progress:2026-09-12:start -->
## 진행 이력 — 2026-09-12

**현재 판정: In Progress / 구현·증적 보완 진행, 실제 Runtime 적용·운영 인수 미완료.**

발행 정본 v3.1.18과 기존 AC를 적용한다. 이번 갱신은 GitHub 이슈·PR·리뷰 기록의 동기화이며 새 서버 시험 결과가 아니다. 아래 현장 실측·제출 증적의 기준일은 **2026-09-10**이다. PR #4의 추가 보고서는 **2026-09-12 15:49 KST 등록 / 문서 작성일 2026-09-10**으로 구분한다.

### 완료·확보된 항목

| 대상 | 확인된 진행 상황 | 증적·현재 PR 상태 |
| --- | --- | --- |
| 설계·정본 | D34/D35에 따른 6개 Node firewalld→Calico named HEP/GNP 전환 설계와 IF-06B·IF-16 계약 확정. 운영 기록을 v3.1.18에 반영 | 설계 승인 범위 유지. Runtime AC는 별도 인수 |
| CP 진단·실행 도구 | ansible01에서 Linux 모의시험 **37/37 PASS**, CP 읽기 전용 **115개 조회 rc=0**, 증적 무결성 확인 기록 확보. 실제 실행 source는 `afc246d2db041c68de5014972107484dad122558` | [PR #2](https://github.com/321Team/infra-kubernetes/pull/2) 최신 HEAD `097ddb56d87b229a9eb465f72ea9f55d16524c51`. 증적 편입 완료, **Open / 미병합**. [현장 검토·증적](https://github.com/321Team/infra-kubernetes/blob/097ddb56d87b229a9eb465f72ea9f55d16524c51/docs/change/ICR-D-NET-01-01/ONSITE_REVIEW_20260910.md) |
| Worker·시간 속성 보완 | supplement **24개 조회**, 내부 **8/8 체크섬**, 6대 시간 속성, Worker 3대 kubelet의 config.yaml 부재 오류, Cockpit socket/service 총 6 unit mask·9090 listener 부재 확인 | [PR #3](https://github.com/321Team/infra-kubernetes/pull/3) **2026-09-10 병합 완료**, merge `7d44afc3afff4d322cb4dbeff4433d61e23e111a`. 동일 supplement 추가 재수집은 잔여에서 제외 |
| 후속 Node 변경·복구 도구 | 최신 PR #2 실행 결과·실제 인수 기록 연계, Runtime 전용 변경·복구, 정책 대조·초기 상태·실행 통제 보완 제출. 로컬 Linux 모의시험 **74개 PASS 기록**(PR #4 55 + Worker 회귀 19) | [PR #4](https://github.com/321Team/infra-kubernetes/pull/4) 최신 HEAD `75d476edc33d6368fe4ab07e78fc51759e81a6fc`. **새 HEAD 독립 재검토 대기 / Open / 미병합 / 실서버 미적용**. [보완 제출 기록](https://github.com/321Team/infra-kubernetes/pull/4#issuecomment-5618296177) |

PR #2와 PR #4의 지정 리뷰어는 **이하영(hayeounglee)**이며, 2026-09-12 조회 시 두 PR의 GitHub 정식 리뷰 제출은 각각 **0건**, `APPROVED`는 미확보다. Conversation 리뷰 의견은 이미 수신했다. 모의시험·수집 PASS와 PR #3 병합은 변경 적용·ICR 전체 운영 인수 승인으로 확대하지 않는다.

### 마지막 현장 상태와 추가 보고

- **CP1:** 단일 Ready Node·etcd voter 1개, learner 없음, API readyz 성공. Calico Running / firewalld active / HEP·GNP 0으로 최종 보호 인계는 미완료.
- **통신:** CP2/CP3→CP1 TCP 2379/2380/10250 **0/6**, 기존 CP→Worker 10250 시험 **0/9**. Worker→API LB TCP **3/3**은 당시 TCP 범위의 부분 증적이다. 15:34 supplement는 TCP·firewall·chrony source를 재조회하지 않았다.
- **CP2 가입:** [9월 12일 등록된 이하영 보고](https://github.com/321Team/infra-kubernetes/pull/4#issuecomment-5644293796)에 `check-etcd` 단계의 `context deadline exceeded`가 기재됐다. 이를 리드 보고로 연결하며, 원본 전체 join 로그·실제 etcd data 경로·잔여 구성에 따른 보존/정리/재개 판단은 P1-K8S-01에서 대조한다. 본 갱신으로 CP3/Worker 가입이나 Gate 완료를 새로 판정하지 않는다.
- **NTP:** 기존 수집 기록은 6대 동일 chrony pool 설정과 당시 선택 IP 4종이다. 추가 보고의 “6대가 전부 서로 다른 서버” 표현은 해당 보고의 표 및 기존 수집 결과와 일치하지 않는다. 고정 목적지·운영 주체·수치 인수조건이 미결이라는 사실을 추적한다.

근거: [PR #2 현장 결과](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5617144005), [PR #3 실측·보완 기록](https://github.com/321Team/infra-kubernetes/pull/3), [리드 추가 보고](https://github.com/321Team/infra-kubernetes/pull/4#issuecomment-5644293796). 현장 상태는 해당 실측 시점의 기록이며 9월 12일 재측정 결과가 아니다.

### 최신 리뷰 대조·미완료 항목

| 항목 | 현재 상태·다음 확인 |
| --- | --- |
| PR #2 리뷰 후속 | [이하영의 9월 10일 리뷰](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5617927881)에 D34 정합성 승인 근거, `source_commit` 일치 조건에 따른 긴급 롤백 대비책, PR 본문 상태 정돈 요청이 있다. 기존 ADV-20260910·v3.1.18 반영 근거와 연결해 명시적으로 답변·확인하고 최신 HEAD의 독립 판정을 확보한다. 이는 이미 허용된 문서·코드 준비를 다시 미승인으로 돌리는 조치가 아니다 |
| PR #4 보완본 재검토 | 9월 12일 등록 보고서의 스키마 불일치·Permanent→Runtime 지적은 보완 전 소스에 대한 설명이다. `75d476e`에 최신 계약 연계와 Runtime 전용 단계 보완이 제출됐다. **보완 제출 / 독립 재검토·실서버 검증 대기**로 추적하며 해결 승인 완료로 처리하지 않는다 |
| 실제 제한 적용·확대 | CP1 Runtime apply/rollback·독립 인수 미완료. CP2/CP3·Worker 대상별 변경·복구 및 가입은 선행 결과와 잔여 상태 확인 후 판단. Permanent 승격 및 최종 보호 인계 종료 절차는 후속 결정·구현 대상 |
| NTP·보호 | #14 고정 NTP 목적지·운영 주체, #10 동기화 수치 인수조건, #19 최소 egress 연계가 미결. Cockpit 잔여 방화벽 허용 제거와 6대 HEP/GNP 적용·허용/차단·회귀 검증이 남음 |
| IF-06B / ICR-AC-12 | **BLOCKED** — Receiver/TLS/Auth/Payload Allowlist, 실제 Source/Return Path 및 비승인 egress 차단 인수 미완료 |
| IF-16 / ICR-AC-13 | **FAIL — DRIFT** — edge/harbor/db의 `10.250.10.0/24 via 10.1.93.58` 반환 경로 교정·검증 미완료. Worker 경로 회귀, mgmt-gw Forward/Firewall/NAT·내부 SNAT 미사용 검증도 남음 |
| 전체 인수 | 나머지 ICR AC는 기존 `NOT VERIFIED` 유지. Positive/Negative/Regression/Reboot/Rollback, 전체 Evidence Index·SHA256SUMS·비밀정보 검사 및 독립 리뷰·Lead 최종 승인 미완료 |

### 재개 순서

1. **PR #2 리뷰 후속 확인과 PR #4 최신 보완본 재검토**를 진행한다. 이미 확보한 현장 Linux 모의시험·Worker supplement를 증적 부족 사유로 반복 요구하지 않는다.
2. **CP1 실행 직전** 최신 inspect, 대상·소스·입력 일치, 보호·콘솔·백업·복구·평일 작업창·실행 결정을 확인한다. 기존 시점의 inspect를 현재 apply 입력으로 재사용하지 않는다.
3. 승인 범위의 **CP1 제한 Runtime 적용·기능/허용·차단/회귀·복구 검증과 독립 인수**를 진행한다.
4. CP1 인수와 PR #4 최신 HEAD 리뷰 결과에 따라 **CP2/CP3·Worker 대상별 변경·복구 및 P1-K8S-01 가입 재개**를 판단한다. CP2 잔여 구성의 보존/정리 결정은 #10에 연결한다.
5. 최종 HEP/GNP 보호 전환, IF-16·IF-06B, 재부팅 지속성·복구·전체 인수 증적을 기존 AC에 연결한다. HEP/GNP 전환은 **Bootstrap Allow→canary Worker→Worker 확대→CP** 순서를 유지하며 CP 통신 보완 순서와 구분한다.

현재 담당 **Lead 이권욱 / Support 이하영·이재환**, **Start 2026-09-01 / Plan End 2026-09-21**, 대표 Milestone **G2 Security / Feature Ready**를 유지한다. 일정은 조정 가능한 계획 목표이며 실제 종료일·승인은 미확정이다.
<!-- fds-icr-progress:2026-09-12:end -->

<details>
<summary>2026-09-10 정본 수집·통합 당시 기록 — 이력 보존</summary>

## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **In Progress / open**. 원본 갱신 시각: `2026-09-10T11:57:13Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.
- 수집된 운영 댓글은 원래 위치에 보존한다. 신규 구현 제출/리뷰 요청은 실행 PASS나 승인으로 간주하지 않는다.
  - [5617728652](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5617728652) · 2026-09-10T11:09:38Z
  - [5618299581](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5618299581) · 2026-09-10T11:57:13Z

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

PR #2 실행 source afc246d의 현장 Linux 모의시험 37/37·CP 읽기 전용 115개 조회가 검증됐고 최신 HEAD는 097ddb56d87b229a9eb465f72ea9f55d16524c51이다. Worker 보완 24개 조회·내부 8/8 체크섬과 시간·kubelet 원인·Cockpit mask 증적 PASS, PR #3 merge 7d44afc3afff4d322cb4dbeff4433d61e23e111a를 반영한다. 과거 CP→Worker TCP 0/9 및 Worker→LB TCP 3/3은 당시 부분 증적이다. PR #4 75d476edc33d6368fe4ab07e78fc51759e81a6fc는 최신 영수증/실제 인수 연결·Runtime 전용 변경/복구로 보완됐고 로컬 모의시험 74개 PASS 기록이 있다. 새 HEAD 독립 리뷰·실제 CP1 canary·후속 노드 적용/복구는 미완료이며 Permanent 승격은 미구현이다. NTP 목적지/운영 주체·동기화 기준, Cockpit 잔여 방화벽 허용 제거, HEP/GNP·IF-06B·IF-16 및 ICR AC-01~20은 잔여다. 실제 종료일 미확정·이전 End TBD 이력을 보존한다. 현재 후보 Plan: 2026-09-01 ~ 2026-09-21 (조건부 목표).

근거: [Issue #14](https://github.com/321Team/fds-project-baseline/issues/14), Issue 갱신 시각 `2026-09-10T05:03:39Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

이전 후보 출처: [Worker/NTP 검토·잔여 작업](https://github.com/321Team/infra-kubernetes/blob/3309866766236bbdbe20b9e2ae1d8fd6f9233bcd/docs/change/ICR-D-NET-01-01/RESIDUAL_WORK_20260910.md). 원래 수집본은 보존하고 `audit/v3.1.18/followup-20260910.json`에 추가 기록을 고정했다. 이번 정본 보완은 연결된 검토 기록의 반영이며 서버 재시험은 아니다.

## 2026-09-10 K8S 최신 이력 통합

- PR #2: 실행 source `afc246d2db041c68de5014972107484dad122558`, 증적 편입 HEAD `097ddb56d87b229a9eb465f72ea9f55d16524c51`. 현장 Linux **모의시험 37/37**, CP **읽기 전용 조회 115개**의 검증 기록을 반영한다. Runtime apply/rollback 증적은 아니다.
- Worker: 15:34 KST 보완 증적에서 6대 시간 속성, Worker kubelet의 config.yaml 부재 오류, Cockpit 6 unit mask 및 9090 listener 부재를 확인했다. 같은 supplement의 추가 재수집은 잔여에서 제외한다. TCP·firewall·chrony source를 재조회한 결과는 아니다.
- PR #3: `3309866766236bbdbe20b9e2ae1d8fd6f9233bcd`의 수집기 소스가 **Merged**, merge `7d44afc3afff4d322cb4dbeff4433d61e23e111a`. 병합을 클러스터·방화벽 운영 인수로 해석하지 않는다.
- PR #4: 최신 `75d476edc33d6368fe4ab07e78fc51759e81a6fc`에서 최신 PR #2 영수증·실제 인수 연결, Runtime 전용 변경/복구, 정책·상태·실행 통제를 보완했다. 로컬 Linux **모의시험 74개**(PR #4 55+Worker 회귀 19) PASS 기록이며 새 HEAD 리뷰·실서버 검증은 미완료다. 구 소스의 계약/순서 지적은 보존하되 보완 미착수로 표시하지 않는다.
- PR #2/#4는 이하영의 최신 HEAD 독립 리뷰와 실제 Runtime 인수가 남는다. 현재 구현은 Runtime 전용이며 Permanent 승격은 미구현이다. CP2 재개·6대 가입·etcd 3 Member·DNS/cross-node·NTP·HEP/GNP·Storage·재부팅/복구는 기존 미완료 상태다.
- 09-11의 완료된 Worker supplement 재수집 문구를 CP1 보호/복구·inspect 준비로 교체한다. PR #2/#4 재리뷰를 연결하며 날짜·담당·배정 인일·휴가·주말 가용량·Gate/AC는 유지한다.

고정 출처·당시 본문·이전 후보 값은 `audit/v3.1.18/k8s-intake-20260910.json`, 자세한 조건은 `releases/v3.1.18/FDS_K8S_Candidate_Integration_20260910.md`에 기록한다. 이 통합은 후보 문서 갱신이며 운영 적용·정본 발행이 아니다.

</details>

### 미결 사양과 실행 조건

현재 3CP+3Worker·kubeadm·Calico·static local PV 범위를 유지한다. 추가 노드·플랫폼 도입 결정은 없다. NTP 목적지/운영 주체(#14), 동기화 수치 인수조건(#10), 최소 egress(#19)는 해당 변경·인수 전에 확정한다. `100ms·60초×6`은 미승인 초안이고 MTU 1450도 실측 확정 전 후보값이다. CP2 실패 단계는 2026-09-12 등록된 리드 보고에 `check-etcd`로 기재됐다. 원본 전체 join 로그와 실제 data 경로를 대조하고 보존/정리/재개 방식은 #10에서 판단한다.

발행 D34의 Calico 설치 전 firewalld OFF 이력과 실제 CP1 공존 drift를 구분한다. ADV-20260910에 따라 사유·기간·보호·복구·종료조건을 기록한 제한적 선행 준비를 이어간다. 최종 6대 firewalld disabled/inactive 및 named HEP/GNP 목표, Bootstrap Allow→canary Worker→Worker 확대→CP의 보호 전환 순서를 유지한다. CP 통신 canary가 HEP 전환 순서를 대체하지 않는다.

PR #2/#4 코드 승인·병합과 CP1 제한 Runtime 적용·복구·재적용 증적 검토는 완료했다. PR #9 새 HEAD 독립 승인·병합을 확인했으며 CP1 CNI 회귀와 실제 최종 인수 이후 후속 대상의 실행·복구/가입을 판단한다. Runtime 시험·리뷰 이후의 Permanent 또는 최종 보호 인계 종료 절차는 별도 결정·구현 대상이다. 승인 JSON을 실제 GitHub 리뷰 인증으로 해석하지 않는다. NTP 미결을 모든 준비의 전역 중단 조건으로 만들거나 기존 시간 동기화 선행조건을 면제하지 않는다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

### User Story

네트워크 및 보안 담당자로서 Kubernetes Node의 호스트 방화벽 통제를 firewalld에서 Calico named HostEndpoint와 GlobalNetworkPolicy로 전환한다. 이를 통해 관리망과 Monitoring 경로의 실제 Source/Return Path를 정본 Interface 계약과 일치시키고, 승인된 최소 통신만 재현 가능하게 허용한다.

---

### Scope

#### In Scope

- Kubernetes 6개 Node의 보호 전환 후 firewalld 비활성화 검증
- Calico named HostEndpoint, `expectedIPs`, Bootstrap Allow 및 최소 허용 GNP
- NodePort 30080, node-exporter 9100, kubelet 10250의 승인 Source 허용과 비승인 Source 차단
- Control Plane 관리 기능과 Harbor Pull 회귀 검증
- IF-06B Prometheus Remote Write 경로의 TLS/Auth/Payload Allowlist 및 egress 차단
- IF-16 관리망 반환 경로, Source Preservation 및 내부 SNAT 미사용 검증
- Reboot 지속성, Rollback 재현성, Evidence 무결성 및 비밀정보 미노출 검증

#### Out of Scope

- 설계 승인만으로 Runtime PASS를 선언하는 행위
- 관측되지 않은 Source IP 또는 추정 경로를 기준으로 허용 정책 확정
- 평문 Token, Password 또는 Private Key의 Evidence 저장
- ICR 외 기능 티켓의 완료 상태 자동 상향

---

### 핵심 요구사항

**2026-09-15 증적 재대조:** 완료 **2/11(18.2%)**, 부분 완료 **5건**, 미검증 **2건**, 차단 **1건**, FAIL **1건**. 아래 체크는 각 요구사항 전체 범위의 충족 여부이며, 부분 실적과 남은 범위를 같은 항목에 표시한다. 세부 근거는 바로 아래 선행 작업 및 Acceptance Criteria와 연결한다.

- [x] firewalld 비활성화와 Calico named HEP/GNP 전환 설계를 D34/D35 기준으로 확정한다. **완료 — 설계 확정 범위. 실제 보호 전환 완료는 AC-02/03/18에서 별도로 판정**.
- [x] IF-06B와 IF-16의 정본 Interface 계약을 유지한다. **완료 — 계약 유지 범위. 실제 통신·인증·경로 검증과 drift 시정 완료를 뜻하지 않음**.
- [ ] Kubernetes 6개 Node의 변경 전 상태와 SHA-256 Evidence를 확보한다. **PARTIAL — 6대 방화벽·리스너 수집/무결성 및 Worker 3대 경로 확보. CP2/CP3 경로와 최초 변경 전 CP 경로 근거 연결은 미완료**. 현재 CP1 경로 조회로 과거 변경 전 증적을 대체하지 않는다. → AC-01.
- [ ] named HEP/`expectedIPs`와 Bootstrap Allow를 승인안대로 적용한다. **NOT VERIFIED — 실제 HEP/GNP 보호 인계 미실시. CP1 제한 Runtime 규칙과 격리 시험 VM 준비는 이 항목의 완료 근거가 아님**. → AC-02/03.
- [ ] 30080/9100/10250에 대해 승인 Source 허용과 비승인 Source 차단을 검증한다. **NOT VERIFIED — 요구된 NodePort·Prometheus·Workload 범위의 허용/차단 검증 미완료**. CP1 제한 관리 Source 시험을 이 범위에 합산하지 않는다. → AC-04/05/06/07.
- [ ] Control Plane 관리 기능, Harbor Pull 및 Worker Route 회귀를 검증한다. **PARTIAL — CP1 최초 적용 단계의 logs/exec/port-forward 증적 확보. 전체 Control Plane 회귀, Worker Harbor Pull/Pod 시작 및 Route 회귀 인수는 미완료**. → AC-08/09/14.
- [ ] IF-06B Receiver/TLS/Auth/Payload Allowlist와 실제 Source/Return Path를 검증한다. **BLOCKED — 실제 Receiver·인증·Payload·허용/차단·양방향 경로 검증 및 인수 미완료**. → AC-11/12/15/16/17.
- [ ] IF-16 edge/harbor/db Route Drift를 시정한다. **FAIL — DRIFT 유지. 시정 및 재검증 완료 증적 없음**. → AC-13.
- [ ] Reboot 지속성과 Rollback 재현성을 검증한다. **PARTIAL — CP1 제한 Runtime 6개 rollback·baseline 복구 재현 완료. 전체 보호/경로 변경의 rollback 및 최종 정책 reboot 지속성 미완료**. 백업 준비 중 재기동은 최종 정책 지속성 시험과 구분한다. → AC-18/19.
- [ ] Evidence Index·SHA256SUMS·비밀정보 검사를 완료한다. **PARTIAL — 제출본별 SHA 검증과 PR #9 마스킹 보완·시험·독립 승인/병합 완료. 전체 최종 Evidence Index·SHA256SUMS 및 비밀정보 검사 종결은 미완료**. → AC-01/20.
- [ ] 고정 Commit/Artifact에 대한 독립 리뷰와 Lead 최종 승인을 완료한다. **PARTIAL — 관련 PR #2·#3·#4·#8·#9·#10 병합 기록 확보. PR #11 최신 HEAD의 정식 리뷰는 0건/APPROVED 미확보이며, CP1 최종 인수와 전체 ICR Lead 최종 승인은 미완료**. CNI 실제 시험 3/5 PASS·직접 Pod 통신 2건 FAIL 및 CP1 ACCEPTED/CP2 변경 보류를 유지한다.

---

### 확인된 선행 작업 — 2026-09-15 체크 반영

아래 체크는 명시된 범위의 완료 실적이다. 전체 AC 완료율에 합산하지 않으며, 과거 수집 성공과 현재 실행 입력의 유효성을 구분한다.

- [x] CP 3대 변경 전 방화벽·리스너 수집과 무결성 확인 — 115개 조회 정상. [고정 증적 검토](https://github.com/321Team/infra-kubernetes/blob/097ddb56d87b229a9eb465f72ea9f55d16524c51/docs/change/ICR-D-NET-01-01/ONSITE_REVIEW_20260910.md)
- [x] Worker 3대 방화벽·리스너·경로 수집, 6대 시간 속성 및 Worker Cockpit mask 보완 — full 99개 조회와 supplement 24개 조회의 역할을 구분하고 시간 속성 공백 해소. [PR #3 증적](https://github.com/321Team/infra-kubernetes/pull/3)
- [x] CP1 백업·콘솔·보호·복구 준비 근거 검토 — 현장 진술과 제출 문서 수용 범위이며 독립 VM 복원 시험 완료는 아니다. [리뷰](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5660719866)
- [x] CP1 제한 Runtime 최초 적용 — 승인된 규칙 6개 성공, Permanent 유지. [적용 기록](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5661850300)
- [x] CP1 적용 후 Positive 통신 — 대상 TCP 0/6→6/6, CP1 Ready/API/etcd 확인. [결과](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5661885959)
- [x] 제한된 관리 Source Negative — 해당 3개 대상 포트 timeout, SSH 정상. 전체 비승인 Source 시험은 아니다. [결과](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5661942617)
- [x] CP1 logs/exec/port-forward·host DNS 기능 증적 확보 — 최초 적용 단계의 결과이며 전체 CP·Pod 간 CNI 인수는 아니다. [결과](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5662024773)
- [x] 별도 승인 CP1 rollback — 원실행 Runtime 6개 회수와 baseline 복구 확인. [실행 연결](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5662361174)
- [x] CP1 최종 재적용·영수증 연결 — `20260914T095827Z-7938c6e73fbd`, 18:58 재적용과 18:59 TCP 6/6·상태 확인. [최종 증적 검토](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5662356251)
- [x] CP2 읽기 전용 inspect — `kivd3bsc`의 90개 저장 조회 정상, INSPECTION 생성·CP1 최종 방화벽 일치 확인. CP2 적용은 미실시.
- [x] PR #2·#3·#4·#8 코드 병합 완료 — 각각의 승인 범위로 인정하며 Runtime 인수와 구분.
- [x] PR #9 마스킹 보완·독립 승인·병합 — 승인 HEAD `b3f3374`, merge `c08b798`. Node 71 / Worker 21 / locale 2 PASS 유지. [병합 기록](https://github.com/321Team/infra-kubernetes/pull/9#issuecomment-5673182602)
- [x] CNI 사전 수집 검토와 자동 20분/마지막 3분 정리 키트 준비 — 개정본 로컬·모의시험 14 PASS. 후속 실제 시험은 아래 별도 결과로 추적. [준비 기록](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5673076052)

**CNI 실제 시험 결과 — 2026-09-15:** `p3dmjivl` **3/5 PASS, 직접 Pod 통신 2건 FAIL**. 정리·전후 firewalld/기존 Pod 상태 확인 완료. 실행 완료를 통신/AC 완료로 체크하지 않는다. [검토](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5673301524)

**직접 남은 후속:** CP1 직접 Pod 통신 실패 원인 진단·보완·CNI 재시험, CP1 최종 인수, CP2 이후 단계별 적용. 전체 보호·Monitoring/Route·재부팅·증적 종결은 아래 AC로 추적한다.

---

### Acceptance Criteria

**2026-09-15 재확인:** 완료 **0건**, PARTIAL **5건(AC-01/08/10/19/20)**, NOT VERIFIED **13건**, BLOCKED **1건(AC-12)**, FAIL **1건(AC-13)**. 하단 ‘갱신 전 원문 보관’은 당시 기록이며 현재 체크·부분 판정은 이 절을 따른다.

**산정 기준:** 아래 원래 AC 20개 중 전체 요구 범위를 충족한 항목만 완료로 센다. 현재 **0/20 = 0%**이며, 이는 전체 인수조건 충족률이다. 수행한 작업량이 0%라는 의미가 아니다. 핵심 요구사항은 원래 상위 11개 중 설계·계약 2개 완료(**18.2%**); 준비/코드/부분 Runtime을 합친 공수 가중 진행률은 정의되지 않아 임의로 추정하지 않는다.

- [ ] `ICR-AC-01` — 6개 Node 변경 전 firewall/listener/route 설정과 SHA Evidence를 확보한다. 현재: **PARTIAL — 방화벽·리스너 6대 수집 및 무결성 확인, Worker 3대 경로 수집 확인. CP1 현재 경로는 2026-09-15 진단에서 추가 확보했으나 최초 변경 전 경로 증적을 소급 대체하지 않음. CP2/CP3 경로 및 최초 변경 전 CP 경로 근거는 미확인**. 이미 확보한 수집 전체를 반복하지 않으며 부족한 route 증적의 기존 자료 연결/보완만 필요.
- [ ] `ICR-AC-02` — firewalld가 disabled/inactive이고 Calico Pod/Node 통신이 정상이다. 현재: **NOT VERIFIED — CP1은 제한 Runtime 규칙 적용 상태이며 firewalld→HEP/GNP 최종 전환 미실시**. 전환 전 CNI 시험은 **3/5 PASS·직접 Pod 통신 2건 FAIL**로 정상 통신 인수도 미완료다.
- [ ] `ICR-AC-03` — named HEP/`expectedIPs`/Bootstrap Allow가 승인안과 일치한다. 현재: **NOT VERIFIED — named HEP/GNP 적용·최종 보호 인계 미실시**.
- [ ] `ICR-AC-04` — `.50 → Worker:30080`은 허용되고 비승인 Source는 차단된다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-05` — Prometheus에서 Worker node-exporter 9100 Target이 `UP`이다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-06` — Prometheus에서 Worker kubelet 10250을 CA+SA로 인증한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-07` — 비승인 Workload의 9100/10250 접근이 차단된다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-08` — Control Plane의 logs/exec/port-forward가 정상이다. 현재: **PARTIAL — CP1 최초 적용 단계의 logs/exec/port-forward 성공 증적 확보. 전체 Control Plane 회귀·재적용 후 인정 범위와 최종 인수 미완료**.
- [ ] `ICR-AC-09` — Worker에서 Harbor `.54:443` Pull과 Pod 시작이 성공한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-10` — Cockpit 9090이 노출되지 않는다. 현재: **PARTIAL — Worker 3대 cockpit.socket/service 총 6 unit masked·inactive/dead, 9090 listener 부재 확인. 잔여 firewall cockpit 허용 정리 및 전체 범위의 비노출 인수 미완료**.
- [ ] `ICR-AC-11` — monitor01에서 Cluster Workload로 신규 Ingress를 시작할 수 없다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-12` — IF-06B Remote Write의 TLS/Auth/Payload Allowlist가 충족되고 비승인 Egress가 차단된다. 현재: **BLOCKED**.
- [ ] `ICR-AC-13` — edge/harbor/db에 `10.250.10.0/24 via .58`가 적용되고 `.30` route-get이 통과한다. 현재: **FAIL — DRIFT**.
- [ ] `ICR-AC-14` — Worker 3대에서 동일 경로 조회 회귀가 통과한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-15` — mgmt-gw IP Forward/Zone/Policy/NAT가 승인안과 일치하고 내부 SNAT가 없다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-16` — monitor01 `.30:443` Receiver/Protocol/TLS/Auth가 정본과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-17` — 패킷 관찰의 실제 Source와 양방향 Return Path가 정본과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-18` — Reboot 후 정책이 유지되고 재시험이 통과한다. 현재: **NOT VERIFIED — 백업 준비 중 CP1 재기동 확인은 최종 정책 적용 후 Reboot 지속성 시험을 대체하지 않음**.
- [ ] `ICR-AC-19` — Rollback을 재현할 수 있다. 현재: **PARTIAL — CP1 제한 Runtime 6개 rollback 및 baseline 복구 재현 완료. 전체 ICR 보호·경로 변경의 복구 검증 미완료**.
- [ ] `ICR-AC-20` — Evidence에 평문 비밀정보가 없다. 현재: **PARTIAL — 제출본별 SHA 무결성 확인 및 마스킹 보완·합성값 시험 완료. PR #9 새 HEAD 독립 승인·병합 완료, 전체 최종 Evidence 비밀정보 검사 미완료**.

---

### 검증 및 증적

- 설계·정본 매핑은 승인 범위 유지. 현행 v3.1.18의 전체 ICR 목표와 AC 문구를 유지한다.
- CP/Worker 변경 전 수집, CP1 최초 적용·Positive/제한된 Negative·기능·rollback·재적용, CP2 inspect는 위 완료 체크와 원 실행/검토 링크로 추적한다.
- 최신 코드: PR #2·#3·#4·#8·#9 병합 완료. PR #9 승인 HEAD `b3f3374`, merge `c08b798`; 새 HEAD 정식 APPROVED 및 Must-fix 해소 확인.
- CNI 개정 키트의 로컬/모의시험 14 PASS와 실서버 `p3dmjivl` 시험 **3/5 PASS·전체 FAIL**을 구분한다. 임시 자원 정리·전후 기본 상태 동일은 확인됐으나 CP1 최종 인수는 보류한다. [실측 검토](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5673301524). 재첨부 `v7nd98wj.tar(1).gz`는 원본과 같은 준비 자료로 새 실행에 산입하지 않는다.
- IF-06B는 **BLOCKED**, IF-16은 **FAIL — DRIFT** 유지. 전체 Evidence Index·비밀정보 검사·보호 인수는 미완료.


---

### Dependency

- P1-LB-01 Stage A Evidence의 공식 Handoff
- P1-K8S-01 Calico Ready 및 Port Matrix 검증
- Prometheus 실제 Source 관찰
- IF-06B Receiver/TLS/Auth 및 관리망 Forward/Return Path 확정
- IF-16 edge/harbor/db Route Drift 시정
- 본 ICR은 P1-SEC-01, P1-MON-01 및 G2 Runtime 판정에 영향을 준다.

---

### Decision / Risk Control

- `D17`: Kubernetes Host 보호의 Mandatory Control을 유지한다.
- `D18`: 승인된 서비스 진입 경로와 NodePort 범위를 유지한다.
- `D33`: IF-06B Prometheus Remote Write 계약을 유지한다.
- `D34`: firewalld 비활성화와 Calico named HEP/GNP 전환 설계를 적용한다.
- `D35`: 중복 Interface를 정리한 v1.4 매핑과 설계/Runtime 상태 분리를 유지한다.
- `RISK-04`: 실제 Source 및 Return Path 오판 위험을 route, tcpdump, conntrack Evidence로 통제한다.
- `RISK-07`: 증적 부재와 완료 상태 과대판정을 Evidence Index, SHA-256, 독립 리뷰로 통제한다.
- IF-06B 부분 차단을 티켓 전체 `Blocked`로 과장하지 않되, Runtime Evidence 없이 `Done`으로 상향하지 않는다.

---

### Review / Handoff

- PR #2·#4는 이하영의 정식 APPROVED 및 병합 기록 확인. PR #3·#8 병합 완료도 각 코드 범위로 인정한다.
- PR #9 `b3f3374ba71a754f15f69a5cc3a471bd61c79424`는 이하영의 새 정식 APPROVED 및 수정 요청 해소 확인 후 병합했다. 승인 범위는 코드이며 CNI Runtime·CP1 인수는 별도다.
- CP1 최초 적용→검증→rollback→재적용 증적 연결을 완료했으며, 이하영은 [CNI 회귀 결과 제출 전 ACCEPTED 보류](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5662853042)를 명시했다.
- 다음 순서: CP1 CNI 시험/정리·전후 상태 확인 → CP1 최종 인수 → CP2 이후 단계별 적용 조건 확인. CP2 잔여 구성·join/reset은 #10의 별도 판단 범위를 유지한다.
- 최종 ICR 인수에는 전체 AC, Evidence Index·SHA256SUMS·비밀정보 검사, 독립 리뷰 및 Lead 승인이 필요하다. 완료한 동일 범위의 모의시험·supplement를 이유 없이 재수집하지 않는다.


---

### Completion Record

- 확인 기준: **2026-09-15 GitHub·보관 증적 대조**, 현장 증적의 원 실행일은 각 항목에 유지.
- 원래 핵심 요구사항: **2/11 완료(18.2%)**. 전체 AC: **0/20 완전 충족(0%)**, AC-01/08/10/19/20은 부분 증적 확보.
- 선행 작업 완료 체크: **13건**. 이 항목은 전체 공수 가중 진행률이나 AC 수에 합산하지 않는다.
- CP1 제한 Runtime 적용·복구·재적용: **증적 검토 완료**. CNI 실제 시험·CP1 최종 ACCEPTED·후속 노드 적용: **미완료**.
- IF-06B: **BLOCKED**, IF-16: **FAIL — DRIFT**.
- 코드 PR #2·#3·#4·#8·#9: **병합 완료**. PR #9의 마스킹 수정 요청은 독립 재검증으로 해소 확인.
- ICR 전체 독립 인수·Lead 최종 승인: **미완료**.
- 최종 판정: **In Progress / open 유지**. Plan End **2026-09-21**은 조정 가능한 목표이며 실제 완료일 미확정.

원래 ICR-AC-01~20의 PASS Evidence 또는 승인된 N/A 근거, IF-06B·IF-16 후속, 전체 검증·무결성·독립 인수 조건을 충족한 뒤 Done 여부를 판정한다.

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `ecf1ff1e9764f9f8452c231a8befc77cfa05864717fa0cedb5375f12a5133ef6`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-k8s-review-response-20260910:start -->
### 2026-09-10 Kubernetes 신규 리뷰 검토 — CA별 실행 조건 연결

[PR #4 리뷰 대조 답변 / CA-01~07 전체 매핑](https://github.com/321Team/infra-kubernetes/pull/4#issuecomment-5617452251)을 반영합니다. **In Progress·기존 AC 미완료를 유지하며 PR #4 병합·운영 적용은 보류합니다.** 코드·문서 보완은 기존 사용자 선행 허용과 ADV-20260910 이력에 따라 진행할 수 있습니다.

| 구분 | 현재 처리 |
|---|---|
| 호환성 | PR #2 최신 `097ddb5`는 v2/Runtime 6개, PR #4 `de9a3a3`는 구 v1/12개 검증이므로 보완 필요. 구 `068661e` 자체는 v1이라는 사실을 정정 기록 |
| CA-01/03/04 | CP1 실제 Runtime 전 보호·예외 실행·복구/콘솔/백업·작업창과 정확한 HEAD의 실제 독립 리뷰/실행 결정 필요. 최신 상태·입력으로 확인 |
| CA-02 | PR #2 Runtime-only 유지. PR #4 Permanent 선반영은 적용 전 코드 차단사항으로 처리하고 Runtime 시험·리뷰 뒤 별도 단계로 분리 |
| CA-05 | 승인된 /32·포트 범위를 유지하고 변경 후 통신·TLS/Auth·Negative·기능·회귀 인수. 변경 전 TCP PASS를 요구하는 순환 조건으로 만들지 않음 |
| CA-06 | CP2 잔여 상태·실제 data 경로·원래 join 실패 단계는 #10과 연계. 해당 대상 작업 범위와 join/config 동결을 명시 |
| CA-07 | #14 NTP 목적지/운영 주체, #10 동기화 인수 기준, #19 최소 egress 결정. 초안 수치는 정본 AC가 아니며 기존 시간 선행조건은 유지 |
| 다음 | PR #2 최신 HEAD 독립 리뷰와 PR #4 계약·Runtime 단계·정책/상태 검증 보완을 병행. 실제 CP1 Runtime 인수 후 후속 노드의 제한 실행·검증으로 연결 |

현장 Linux 37개 모의시험 및 CP 115개 실제 조회는 확보됐으나 Runtime 인수는 미완료입니다. PR #4 현재31개 시험은 mock입니다. 이번 검토는 리뷰 답변과 이력 정리이며 코드·정본 변경, 승인·병합, 실서버 적용은 수행하지 않았습니다. 아래 이전 시점 기록은 보존하며 현재 판단은 위 답변을 우선합니다.
<!-- fds-k8s-review-response-20260910:end -->

<!-- fds-pr2-onsite-verified-20260910:start -->
### 2026-09-10 현장 증적 검증 완료 — Runtime 인수 별도

PR #2의 현장 Linux 요청은 **증적 확보·검증 완료**로 갱신했습니다. 테스트37/37, 기존 요청19개 식별자 포함, 일반37+snapshot78=115개 조회 rc0, 체크섬 외부 내부13/13·중첩5/5 일치입니다. 실행 source afc246d와 증적 편입 HEAD `097ddb56d87b229a9eb465f72ea9f55d16524c51`를 구분하며 코드·테스트·정책은 변경하지 않았습니다.

CP1 단일 구성·CP2/3→CP1 TCP0/6·HEP/GNP0은 여전히 남습니다. 다음은 이하영의 새 HEAD 독립 리뷰와 실제 보호/복구·평일 변경창·실행 결정입니다. 만료된 입력 또는 source 변경 시 새 inspect를 사용합니다. PR #4 계약·Permanent 단계·NTP·IF-06B/IF-16 등 기존 잔여와 In Progress/AC 미완료를 유지합니다.

[현장 검토서](https://github.com/321Team/infra-kubernetes/blob/097ddb56d87b229a9eb465f72ea9f55d16524c51/docs/change/ICR-D-NET-01-01/ONSITE_REVIEW_20260910.md) · [Linux 실행 기록](https://github.com/321Team/infra-kubernetes/blob/097ddb56d87b229a9eb465f72ea9f55d16524c51/docs/change/ICR-D-NET-01-01/ONSITE_TEST_20260910.json) · [점검 요약](https://github.com/321Team/infra-kubernetes/blob/097ddb56d87b229a9eb465f72ea9f55d16524c51/docs/change/ICR-D-NET-01-01/ONSITE_INSPECTION_SUMMARY_20260910.json)

아래 “현장 실행 미확보” 문구는 이전 시점 이력이며 위 최신 증적 상태를 적용합니다.
<!-- fds-pr2-onsite-verified-20260910:end -->

<!-- fds-pr2-onsite-start-20260910:start -->
### 현장 검증 후속 착수 — 2026-09-10

[PR #2 착수 기록](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5616733058)에 현장 Linux 테스트·읽기 전용 점검의 증적 수집 준비를 등록했습니다. 보조 수집기 모의 검증 8개 PASS이며 현장 실행 결과는 아직 미확보입니다. 제출 후 실행 기록·증적 검토 및 Git 편입을 진행합니다.

PR #4의 영수증·Runtime 인수·Permanent 단계·복구 계약 보완표를 정리했습니다. 구현·확대 적용 완료는 아닙니다. v18의 실제 후보 파일 편입과 발행도 후속으로 남습니다. 기존 독립 리뷰 요청·정본·AC·In Progress 판정을 유지합니다.
<!-- fds-pr2-onsite-start-20260910:end -->

<!-- fds-pr2-remediation-20260910:start -->
## 2026-09-10 최신 후속 — 사용자 선행 허용·PR #2 보완

사용자 지시에 따라 정당한 차이의 v18 발행 전 선행 준비를 허용하고 [선행 변경 기록 ICR-D-NET-01-01-ADV-20260910](https://github.com/321Team/infra-kubernetes/blob/afc246d2db041c68de5014972107484dad122558/docs/change/ICR-D-NET-01-01/ADVANCE_CHANGE_RECORD_20260910.md)에 근거·범위·위험·종료조건을 기록했습니다. 현행 v3.1.17과 기존 AC·Done 이력은 유지합니다. [PR #1](https://github.com/321Team/infra-kubernetes/pull/1)은 `08b32e7`로 병합했고, [PR #2](https://github.com/321Team/infra-kubernetes/pull/2) 새 HEAD는 `afc246d2db041c68de5014972107484dad122558`입니다.

- ICR Lead 이권욱 / 독립 PR #2 Reviewer 이하영. 최신 재점검 검토서·요약·해시와 Linux 실행 기록을 Git 편입했습니다. 새 소스 모의 테스트 37/37 PASS; 현장 실행·Runtime AC 완료는 미확인입니다.
- CA-01: 이미 공존 중인 단일 CP1에서 보호 공백을 피하기 위한 제한적 Runtime canary 준비를 선행합니다. 실제 공존 안전성은 보호/백업/콘솔/복구·변경창·새 Calico/firewall 관측으로 검토합니다.
- CA-02: PR #2를 Runtime 6개 후보만 변경하도록 수정했습니다. Permanent 승격은 구현하지 않았으며 시험·독립 리뷰 후 별도 판단합니다.
- 다음은 새 HEAD 이하영 리뷰, ansible01 Linux 확인·새 inspect, 실제 실행 기록의 조건 확인입니다. 운영자 승인 JSON은 실제 GitHub 리뷰를 자동 인증하지 않습니다.
- PR #4 현 소스는 구 v1 12개 receipt와 Permanent 선반영을 전제하므로 적용 보류입니다. #10/#19와 새 계약·시험·보호 인계를 후속 조정합니다. NTP 목적지/운영 주체, IF-06B/IF-16 등 기존 잔여는 유지합니다.

현재: **In Progress / 선행 구현·증적 보완 완료 / 새 HEAD 리뷰 및 Runtime 조건 미완료**. 아래 기존 “HEAD 유지·읽기 전용만 가능” 문구는 당시 판단이며 위 승인·새 커밋으로 갱신합니다.
<!-- fds-pr2-remediation-20260910:end -->

<!-- fds-canonical-audit-20260910:start -->
### 2026-09-10 정본 정합성 검토 결과 — 현재 HEAD 적용 보류

기준: [RELEASED docs-v3.1.17 / D34·D35](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md), 정본 등록 ICR-D-NET-01-01 v1.4. **정본·기존 AC를 보존하며, 아래 불일치를 해결하기 전 현재 PR #2·#4의 apply 및 운영 적용 가능 판정을 보류합니다.**

| ID | 확인 결과 | 수정·후속 조건 |
|---|---|---|
| CA-01 | D34는 Calico 설치 전 firewalld OFF. PR #2 CP-PORTS §5는 HEP/GNP 검증 후 인계로 서술하며 PR #4가 이 흐름을 전제함 | Lead Final v4.0 RUNBOOK §3 / ICR_ADDENDUM의 순서 변경은 제안이며 자체 승인 아님. 조사한 정본·#10/#14 기록에서 해당 변경의 승인 근거 미확인. 정본을 유지하는 복구·정합화 절차로 수정 필요 |
| CA-02 | ICR v1.4는 Runtime Positive/Negative/Regression + Reviewer 승인 뒤 Permanent 반영을 요구하지만, PR #2 apply_transaction 및 PR #4 plan_for는 permanent→runtime 순서 | 단순 반복 순서 교체로 해결되지 않음. Runtime 적용·시험 영수증·실제 리뷰와 별도 Permanent 반영 단계로 분리하고 소유권/복구/CP1 인수 계약을 함께 수정 필요 |
| CA-03 | 09/10 11:30 KST CP1 원본 로그: calico-node 1/1 Running, firewalld active, HEP 0/GNP 0 | 승인된 보호 인계 완료로 볼 수 없음. 현재값 재관측과 보호·콘솔·복구 경로를 검토. 즉시 firewalld OFF 또는 HEP 일괄 생성으로 처리하지 않음 |
| CA-04 | PR #2에는 D34/독립 리뷰의 자동 검증이 없고, PR #4 승인 JSON은 사람의 기록이며 GitHub 승인을 인증하지 않음 | 본문 조건은 수동 운영 통제. 코드가 D34 불일치를 자동 차단한다고 표현하지 않음 |
| CA-05 | CP/32→2379–2380·10250은 IF-12A/12B 범위와 부합하지만 통신·CA/Auth·Negative·기능 인수는 미완료 | 포트 범위 일치를 엔진·적용 순서 승인 또는 IF-06 Prometheus 인수로 확대하지 않음 |
| CA-06 | CP2는 마지막 CP1 Node/member 목록에 없지만 API/controller/scheduler manifest 3개 잔존. 표준 etcd data와 kubelet 설정은 부재 | #10에서 잔여 구성 검토 분기. 원래 join 출력·구성/실제 data 경로를 확인하고 정리·보존·복구 범위를 정함. 무조건 join/reset/member remove 금지 |
| CA-07 | 6대 chrony 설정은 같은 pool이며 당시 선택 IP는 4종. 고정 NTP 목적지와 수치 인수조건 승인 근거 미확보 | #14 목적지·운영 주체·수명주기 기록, #10 동기화 인수조건 검토, #19 최소 egress 연계. PR #4의 100 ms/60초×6 제안값은 정본 AC가 아님 |

검토 소스: PR #2 `068661e076de02669170d3582f3d596d6e1a8eb3` 15/15 파일, PR #4 `de9a3a30fd691ac30a0e03c4212c21300653e088` 11/11 파일이 GitHub blob SHA와 일치. 제출 증적 4묶음의 외부 SHA와 내부 29/29 체크섬 일치. 이 결과는 증적 무결성·정합성 분석이며 Runtime PASS가 아닙니다.

PR #2·#4는 이하영(hayeounglee) 리뷰 요청 상태이고 제출된 독립 리뷰는 각각 0건입니다. 기존 소스 HEAD와 정본·WBS·AC·Done 이력을 유지합니다. 현재 수행 범위는 읽기 전용 분석·수정 요구사항 작성·후속 증적 준비입니다.

상세 결과서: `FDS_Canonical_Alignment_and_Followup_Review_20260910_v1.0.md`. 과거의 “CP1 canary 인수 후 확대” 안내는 위 정합성 선행조건을 충족할 때만 유효합니다.
<!-- fds-canonical-audit-20260910:end -->

<!-- fds-notion-migration:2026-09-09 record-id:ICR-D-NET-01-01 -->
# ICR-D-NET-01-01 — Kubernetes Node Host Firewall / Monitoring Route

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

<!-- fds-cp-followup-20260910:start -->

### 2026-09-10 — 정본 보존 우선 조건

사용자 지시에 따라 승인 정본 v3.1.17(`2d93395a0e19ea67e5be199d7183a7edbaa6cf4c`)을 직접 대조했습니다. D34의 Calico 설치 전 firewalld OFF 및 named HEP/GNP 보호 통일, HEP/GNP 적용 순서를 유지합니다. IF-12A/12B 포트 범위 일치만으로 현재 firewalld 보완 절차의 운영 승인을 갈음하지 않습니다. [PR #2](https://github.com/321Team/infra-kubernetes/pull/2)·[PR #4](https://github.com/321Team/infra-kubernetes/pull/4)에 D34 설치·인계 순서와 보완안의 정합성 확인 조건을 추가했습니다. 이 관계와 승인 근거가 확인되기 전에는 독립 코드 리뷰만으로 apply 가능 판정을 하지 않습니다. PR #4는 이하영(hayeounglee) 리뷰 요청/Ready 상태이며 소스 HEAD는 유지합니다.

지금 권장 범위는 정본→실행 절차→증적의 읽기 전용 대조, CP2 기존 상태·미확정 재개 조건 정리, NTP 기존 승인 기록·부족 입력 확인입니다. NTP 서버·공급 방식·수치 초안은 확정된 정본/AC가 아니며 임의 채택하지 않습니다. 기존 담당·상태·AC와 정본/WBS는 유지합니다.


### 2026-09-10 후속 구현 착수 결과

Worker 결합 변경(필요 통신 허용 + Cockpit 잔여 방화벽 예외 제거)과 CP2·CP3의 단일 노드 적용·영수증·복구 도구, join 재개 절차 및 NTP 결정안을 [infra-kubernetes PR #4](https://github.com/321Team/infra-kubernetes/pull/4)에 Draft로 등록했습니다. HEAD `de9a3a30fd691ac30a0e03c4212c21300653e088`, 로컬 모의 검증 31/31 PASS. 실제 노드 적용은 미실행입니다. 수집 PR #3은 보완 증적 확인 후 Ready for review로 전환했습니다. PR #2 이하영 독립 리뷰와 CP1 canary 인수 후 대상별 최신 입력으로 진행합니다. NTP endpoint 승인은 미확보이며 전체 ICR 인수·보호 전환 상태는 유지합니다.


### 2026-09-10 15:34 KST — Worker 보완 증적 검증 완료

- [PR #3 최신 검토 기록](https://github.com/321Team/infra-kubernetes/pull/3): **보완 증적 기술 검증 PASS / 운영 인수 HOLD 유지**. 내부 8/8 체크섬 및 6대 identity·실행 소스 일치, 24개 조회 rc=0·잘림/누락 0.
- 6대 Asia/Seoul·NTPSynchronized=yes 및 시간 속성 확보. Worker 3대 kubelet 오류 원인·Cockpit 마스크 상태 확인 완료. 본 보완 범위의 추가 재수집은 불필요.
- 6대 시간 속성 누락(WF-05) 해소. 고정 NTP 기본/대체 목적지 결정(WF-04), 최소 통신 보완(WF-01), 이전 수집에서 확인된 Cockpit 잔여 허용 정리는 계속 진행.
- Worker kubelet 원인은 config.yaml 부재로 확인되어 #10의 가입/구성 절차로 인계. 이번 supplement는 방화벽·TCP 재시험을 하지 않았으며 이전 관측을 현재 재시험 PASS로 처리하지 않음.
- 다음은 PR #2 이하영 리뷰, 적용 창의 최신 CP1 입력·canary 검증, 후속 노드 통신·가입/인수 단계. PR #2/#3 소스는 이번 검토로 변경하지 않았으며 승인·병합·Runtime 적용·티켓 종결은 수행하지 않음.
- 배포 검토서: `FDS_Worker_Supplement_Review_20260910_v1.0.md`. 기존 제출 전·미수집 상태 기록은 아래 이력으로 보존하며, 본 항목의 최신 상태를 우선 적용.


### 2026-09-10 — Worker 제출 증적 검토 및 제한 보완

- [PR #3 검토 기록](https://github.com/321Team/infra-kubernetes/pull/3): 제출 archive/내부 8개 체크섬 및 6대 identity 확인. **무결성 PASS / 증적 완전성 PARTIAL / 운영 인수 HOLD**.
- 99개 query rc=0이나 6대 시간 속성 출력이 비어 있었음. 수집기 결함을 v1.1에서 수정하고 필요한 시간·Worker 진단만 보완하는 supplement 모드를 준비. 로컬 테스트 19/19 PASS, 수정본 실서버 실행은 남음.
- CP→Worker kubelet 연결 0/9 및 Worker 방화벽 허용 누락을 확인. kubelet listener 부재도 동반하므로 포트 보완만으로 정상화 완료를 판정하지 않음. 최소 source/목적지 범위 후보와 Cockpit 잔여 허용 정리를 후속 변경 대상으로 기록.
- 6대 NTP는 동일 pool 설정이나 선택 서버가 총 4종이며 Leap Normal. 고정 기본/대체 목적지 승인은 미완료. #10과 인수 기준을 확정하고 필요 시 별도 Ansible 변경으로 연결.
- Worker→LB TCP 연결 3/3 성공은 이번 범위의 부분 증적이며 전체 클러스터·보안 AC 완료 근거가 아님. PR #2는 이하영 리뷰 요청 상태를 유지하며 해당 소스는 변경하지 않음.
- [현재 잔여 작업·담당 및 보완 범위](https://github.com/321Team/infra-kubernetes/blob/3309866766236bbdbe20b9e2ae1d8fd6f9233bcd/docs/change/ICR-D-NET-01-01/RESIDUAL_WORK_20260910.md). Runtime 변경·승인·병합·티켓 종결 미실행.


### 2026-09-10 — 리뷰어 지정 및 잔여 증적 수집 준비

- [infra-kubernetes PR #2](https://github.com/321Team/infra-kubernetes/pull/2)를 Ready for review로 전환하고, 사용자 지정 리뷰어 **이하영(hayeounglee)**에게 요청 완료. 검토 HEAD는 `068661e076de02669170d3582f3d596d6e1a8eb3` 유지. 리뷰 승인·병합·운영 적용은 미완료.
- Worker 방화벽·6대 NTP 후속 증적 수집기를 [Draft PR #3](https://github.com/321Team/infra-kubernetes/pull/3)로 준비. 로컬 모의 테스트 15/15 PASS, 배포 키트·체크섬 준비. 실제 서버 실행과 결과 제출은 남음.
- #14는 수집·통신 보완 및 NTP 목적지 결정 조정을 진행. PR #2 검토 후 CP1 canary, 이후 CP2/CP3·Worker 순서의 별도 적용 검토로 연결. NTP 승인값은 아직 미정.
- [잔여 작업·담당·시작 조건 및 NTP 결정표](https://github.com/321Team/infra-kubernetes/blob/e83524b9097cee52e254a40fbe3db238eed801a9/docs/change/ICR-D-NET-01-01/RESIDUAL_WORK_20260910.md). 기존 다른 범위의 상태와 종결 조건은 유지.

## 최신 재점검 판정 — 2026-09-10 13:56 KST

**v1.1 수집기 재점검 및 변경 전 사전 증적 검증 PASS.** 제출본 archive/sidecar·내부 5/5 체크섬 일치, 일반/snapshot 조회 110개 기록 rc=0, gaps·실패 질의 없음. 필요한 snapshot 입력이 완성됐고 기존 수집기 결함은 해소됐다.

검토 대상은 [PR #2](https://github.com/321Team/infra-kubernetes/pull/2)의 HEAD `068661e076de02669170d3582f3d596d6e1a8eb3` 그대로다. 별도 소스 변경 없이 재점검 결과를 연결했다. 검토서 `FDS_CP1_Canary_Reinspection_Review_20260910_v1.0.md` 배포 완료.

**다음:** 동일 HEAD의 독립 리뷰·실행 결정 → 15분 이내 최신 inspect 입력으로 CP1 canary → 전후 검증. 실제 변경·운영 인수는 아직 미실행이므로 In Progress와 나머지 AC 상태를 유지한다. 아래 수집기 수정 및 재점검 대기 내역은 이전 시점 이력이다.


## 추가 검토 및 도구 수정 — 2026-09-10

첫 읽기 전용 점검 증적을 검토했고, 수집기의 정책 출력 처리 결함을 수정했다. v1.1은 정책명 전용 조회, 사전 점검 원문·오류 보존, 미완료 상태 집계를 반영한다. 로컬 회귀 검증 포함 30개 테스트 PASS. 수정 소스 HEAD: `068661e076de02669170d3582f3d596d6e1a8eb3`.

[검토서](https://github.com/321Team/infra-kubernetes/blob/068661e076de02669170d3582f3d596d6e1a8eb3/docs/change/ICR-D-NET-01-01/CP1_CANARY_REVIEW_20260910.md) · [수정 PR #2](https://github.com/321Team/infra-kubernetes/pull/2) · [v1.1 실행 절차](https://github.com/321Team/infra-kubernetes/blob/068661e076de02669170d3582f3d596d6e1a8eb3/docs/runbooks/ICR-D-NET-01-01-CP1-CANARY-KIT.md).

다음 단계는 v1.1 읽기 전용 재점검이다. 완전한 사전 점검, 고정 HEAD 독립 리뷰·실행 결정, 실제 적용·전후 검증은 남아 있다. 이슈 상태와 미완료 AC를 유지하며 아래 버전별 준비 내역은 이력으로 보존한다.


## 진행 업데이트 — 2026-09-10 CP 통신 보완 착수

근거: 2026-09-10 11:30:59 KST 수집본 `FDS_CP_Log_Collection_glrr0dsq.tar.gz`, SHA-256 `265e7d3fe04c8c215b8c76847bac769c5445682d788c3f9ad2bf9afef100c594`. 압축파일 및 내부 8/8 체크섬 일치. [고정 검토서](https://github.com/321Team/infra-kubernetes/blob/8975ca0c45dd9aee6d4930b16315223f86215e1d/docs/change/ICR-D-NET-01-01/CP_LOG_REVIEW_20260910.md).

**착수 범위:** 이권욱 Lead, 이하영·이재환 Support. CP 3대의 public/ens160에서 IF-12A 및 IF-12B 일부의 최소 허용 보완안을 작성했다.

| 항목 | 진행 |
|---|---|
| 변경 전 증적 | CP 3대 수집·무결성 검토 완료. Worker 및 기타 ICR 대상은 잔여 |
| 확인된 누락 | CP Source .102/.103/.104 → CP의 TCP 2379–2380 / 10250 허용 없음 |
| 정책·변경안 | CP Source 각각 /32, 노드별 6개 × Runtime/Permanent = 총 36개 추가 후보 |
| 기존 규칙 보존 | SSH 서비스와 LB .109/32→6443 유지. 이미 있는 규칙은 추가·회수 후보에서 제외 |
| 검증 | 입력 무결성·잘못된 대상/zone·/24 확대 거부 등 기존 11개 + 신규 실행 도구 14개 = 25개 자동 테스트 PASS |
| 형상관리 | [infra-kubernetes Draft PR #2](https://github.com/321Team/infra-kubernetes/pull/2), HEAD `0325ee798ef7bdc4e6dc582362043d899c1f3641` |
| 실행/복구 | CP1 canary→CP2→CP3, query/add 영수증과 정확한 회수 절차 작성 |
| Runtime | 실제 방화벽 적용·join·보호 인계 미실행. 독립 리뷰 및 전후 검증 남음 |

CP2 잔여 구성·etcd 등록 상태는 [#10](https://github.com/321Team/fds-project-baseline/issues/10)에서 병행 확인한다. 10.1.93.0/24 전체 허용, CP 직접 6443, 고정 NTP 목적지, Worker 3대, HEP/GNP 전환은 이번 CP 계획에 자동 포함하지 않았다. NTP는 3개 CP의 선택 서버가 같고 Leap Normal이지만 고정 목적지 승인 근거는 아직 없다.

**다음:** 고정 HEAD 검토 → 현재 identity/zone/규칙·NM 상태 확인 → CP1 canary의 전후 증적 확보. 순차 적용 후 Worker·NTP·HEP/GNP 및 ICR의 기존 IF-06B/IF-16 잔여 작업을 이어간다. ICR-AC-01은 6대 전체 기준으로 여전히 미충족이며, 기타 AC·독립 리뷰·Runtime PASS와 종료일을 상향하지 않는다. **In Progress 유지.**
### CP1 실행 도구 후속 착수 — 2026-09-10

[Draft PR #2](https://github.com/321Team/infra-kubernetes/pull/2)의 HEAD를 `0325ee798ef7bdc4e6dc582362043d899c1f3641`로 갱신했다. 기본 `inspect`는 CP 3대 읽기 전용 진단이며, 명시적 적용·복구는 CP1만 구현했다. 15분 이내 점검 해시·현재 firewall/NM·CP1 단일 Node/etcd member 조건을 검사하고, 쓰기 전 영구 작업 기록 및 확인된 추가 규칙만의 역순 복구를 구현했다.

- 로컬 자동 테스트 **25개 PASS**, 원본 zone 출력 6건 파싱 성공, 원격 산출물 14개 Git blob SHA 일치.
- 배포본: `FDS_CP1_Canary_Kit_v1.0.zip`, SHA-256 `ee2cf8fb5ccb333e2524e81ce3edd1ec6a8821c6a6824d953916428c4ea23d6e`. 내부 SOURCE_LOCK에 전체 HEAD·파일 해시 고정.
- [실행 절차](https://github.com/321Team/infra-kubernetes/blob/0325ee798ef7bdc4e6dc582362043d899c1f3641/docs/runbooks/ICR-D-NET-01-01-CP1-CANARY-KIT.md).
- **현재 실행 요청은 ansible01의 읽기 전용 inspect다.** 새 수집 결과, 현 HEAD 독립 리뷰·실행 결정, CP1 canary 적용·전후 검증은 미완료다. 준비 도구의 PASS를 Runtime PASS로 올리지 않는다.
- CP2/CP3 적용·join, Worker, NTP 고정, HEP/GNP/보호 인계 및 기존 ICR 잔여 범위는 계속 후속으로 관리한다.

<!-- fds-cp-followup-20260910:end -->

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | ICR-D-NET-01-01 |
| Phase | Phase 1 |
| Category | Network / Interface Change Control |
| Type | Change Request |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-01 |
| End | TBD — Runtime Evidence 완료 후 확정 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Kubernetes 6개 Node firewalld 비활성화와 Calico named HEP/GNP 적용, 30080/9100/10250 최소 허용, 관리망 반환 경로와 IF-06B 정합화, Positive/Negative/Regression/Reboot/Rollback 및 무결성 Evidence 완료 |
| Related Decision IDs | D17; D18; D33; D34; D35 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | ICR-D-NET-01-01...v1.4.md`; `FDS_Project_Implementation_Baseline_v3.1.17.md`; Interface Register IF-06B/IF-16; 2026-09-08 연결된 321Team GitHub 검색 결과; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | Read-only와 설계 승인은 완료됐으나 Runtime Evidence는 미확인이다. IF-06B는 Receiver/TLS/Auth·반환 경로·실제 Source 관찰이 미완료이고, IF-16은 edge/harbor/db 경로 Drift가 남아 있다. End와 기간은 추정하지 않고 `TBD`를 유지하며 Positive/Negative/Regression/Reboot/Rollback 증적과 독립 리뷰 후 완료를 판정한다. |

## 이관 기준 및 확인 사항

- 속성의 일정·담당·상태는 RELEASED v3.1.17 WBS(기준일 2026-09-04)를 우선 반영했다. 이후 별도 근거가 있는 변경만 아래에 명시한다.
- 2026-09-08 Notion 배포안의 속성·본문을 반영했다. 원 정본 v3.1.17은 소급 변경하지 않는다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md`
- `FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx`
- `CR-P1-ANS-01-01_ICR-D-NET-01-01_Notion_배포안_2026-09-08.md`

---

## Description — 보관 입력본

> 원본: `CR-P1-ANS-01-01_ICR-D-NET-01-01_Notion_배포안_2026-09-08.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

### 🎯 User Story

네트워크 및 보안 담당자로서 Kubernetes Node의 호스트 방화벽 통제를 firewalld에서 Calico named HostEndpoint와 GlobalNetworkPolicy로 전환한다. 이를 통해 관리망과 Monitoring 경로의 실제 Source/Return Path를 정본 Interface 계약과 일치시키고, 승인된 최소 통신만 재현 가능하게 허용한다.

---

### 📌 Scope

#### In Scope

- Kubernetes 6개 Node의 firewalld 비활성화 검증
- Calico named HostEndpoint, `expectedIPs`, Bootstrap Allow 및 최소 허용 GNP
- NodePort 30080, node-exporter 9100, kubelet 10250의 승인 Source 허용과 비승인 Source 차단
- Control Plane 관리 기능과 Harbor Pull 회귀 검증
- IF-06B Prometheus Remote Write 경로의 TLS/Auth/Payload Allowlist 및 egress 차단
- IF-16 관리망 반환 경로, Source Preservation 및 내부 SNAT 미사용 검증
- Reboot 지속성, Rollback 재현성, Evidence 무결성 및 비밀정보 미노출 검증

#### Out of Scope

- 설계 승인만으로 Runtime PASS를 선언하는 행위
- 관측되지 않은 Source IP 또는 추정 경로를 기준으로 허용 정책 확정
- 평문 Token, Password 또는 Private Key의 Evidence 저장
- ICR 외 기능 티켓의 완료 상태 자동 상향

---

### 📋 핵심 요구사항

- [x] firewalld 비활성화와 Calico named HEP/GNP 전환 설계를 D34/D35 기준으로 확정한다.
- [x] IF-06B와 IF-16의 정본 Interface 계약을 유지한다.
- [ ] Kubernetes 6개 Node의 변경 전 상태와 SHA-256 Evidence를 확보한다.
- [ ] named HEP/`expectedIPs`와 Bootstrap Allow를 승인안대로 적용한다.
- [ ] 30080/9100/10250에 대해 승인 Source 허용과 비승인 Source 차단을 검증한다.
- [ ] Control Plane 관리 기능, Harbor Pull 및 Worker Route 회귀를 검증한다.
- [ ] IF-06B Receiver/TLS/Auth/Payload Allowlist와 실제 Source/Return Path를 검증한다.
- [ ] IF-16 edge/harbor/db Route Drift를 시정한다.
- [ ] Reboot 지속성과 Rollback 재현성을 검증한다.
- [ ] Evidence Index·SHA256SUMS·비밀정보 검사를 완료한다.
- [ ] 고정 Commit/Artifact에 대한 독립 리뷰와 Lead 최종 승인을 완료한다.

---

### ✅ Acceptance Criteria

- [ ] `ICR-AC-01` — 6개 Node 변경 전 firewall/listener/route 설정과 SHA Evidence를 확보한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-02` — firewalld가 disabled/inactive이고 Calico Pod/Node 통신이 정상이다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-03` — named HEP/`expectedIPs`/Bootstrap Allow가 승인안과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-04` — `.50 → Worker:30080`은 허용되고 비승인 Source는 차단된다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-05` — Prometheus에서 Worker node-exporter 9100 Target이 `UP`이다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-06` — Prometheus에서 Worker kubelet 10250을 CA+SA로 인증한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-07` — 비승인 Workload의 9100/10250 접근이 차단된다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-08` — Control Plane의 logs/exec/port-forward가 정상이다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-09` — Worker에서 Harbor `.54:443` Pull과 Pod 시작이 성공한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-10` — Cockpit 9090이 노출되지 않는다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-11` — monitor01에서 Cluster Workload로 신규 Ingress를 시작할 수 없다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-12` — IF-06B Remote Write의 TLS/Auth/Payload Allowlist가 충족되고 비승인 Egress가 차단된다. 현재: **BLOCKED**.
- [ ] `ICR-AC-13` — edge/harbor/db에 `10.250.10.0/24 via .58`가 적용되고 `.30` route-get이 통과한다. 현재: **FAIL — DRIFT**.
- [ ] `ICR-AC-14` — Worker 3대에서 동일 경로 조회 회귀가 통과한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-15` — mgmt-gw IP Forward/Zone/Policy/NAT가 승인안과 일치하고 내부 SNAT가 없다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-16` — monitor01 `.30:443` Receiver/Protocol/TLS/Auth가 정본과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-17` — 패킷 관찰의 실제 Source와 양방향 Return Path가 정본과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-18` — Reboot 후 정책이 유지되고 재시험이 통과한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-19` — Rollback을 재현할 수 있다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-20` — Evidence에 평문 비밀정보가 없다. 현재: **NOT VERIFIED**.

---

### 🧪 검증 및 증적

- `ICR-D-NET-01-01` v1.4의 설계와 정본 ID 매핑: **APPROVED**
- firewalld 비활성화와 Calico HEP/GNP 전환 전략: **설계 승인**
- IF-06B 계약 유지: **정본 결정 완료, Runtime BLOCKED**
- IF-16: **DRIFT — edge/harbor/db Remediation Pending**
- 연결된 `321Team` GitHub 범위에서 `ICR-D-NET-01-01`, `IF-06B`, `HostEndpoint`, `management_return_route`, `30080/9100/10250` 관련 코드 또는 PR 증적: **검색 결과 없음**
- 6개 Node Runtime Evidence, Positive/Negative/Regression/Reboot/Rollback 결과: **미확인**
- Evidence Index, SHA256SUMS 및 비밀정보 검사 결과: **미확인**

설계 승인과 Runtime Acceptance를 합산하여 PASS로 처리하지 않는다. 검색 결과가 없다는 사실만으로 구현 실패를 단정하지 않으며, 검증 가능한 Evidence가 제출될 때까지 `NOT VERIFIED`로 관리한다.

---

### 🔗 Dependency

- P1-LB-01 Stage A Evidence의 공식 Handoff
- P1-K8S-01 Calico Ready 및 Port Matrix 검증
- Prometheus 실제 Source 관찰
- IF-06B Receiver/TLS/Auth 및 관리망 Forward/Return Path 확정
- IF-16 edge/harbor/db Route Drift 시정
- 본 ICR은 P1-SEC-01, P1-MON-01 및 G2 Runtime 판정에 영향을 준다.

---

### ⚖️ Decision / Risk Control

- `D17`: Kubernetes Host 보호의 Mandatory Control을 유지한다.
- `D18`: 승인된 서비스 진입 경로와 NodePort 범위를 유지한다.
- `D33`: IF-06B Prometheus Remote Write 계약을 유지한다.
- `D34`: firewalld 비활성화와 Calico named HEP/GNP 전환 설계를 적용한다.
- `D35`: 중복 Interface를 정리한 v1.4 매핑과 설계/Runtime 상태 분리를 유지한다.
- `RISK-04`: 실제 Source 및 Return Path 오판 위험을 route, tcpdump, conntrack Evidence로 통제한다.
- `RISK-07`: 증적 부재와 완료 상태 과대판정을 Evidence Index, SHA-256, 독립 리뷰로 통제한다.
- IF-06B 부분 차단을 티켓 전체 `Blocked`로 과장하지 않되, Runtime Evidence 없이 `Done`으로 상향하지 않는다.

---

### 🤝 Review / Handoff

- 현재 Review 상태: Runtime Evidence 제출 전이므로 독립 기술 리뷰 미착수
- Reviewer: Evidence 고정 후 별도 지정 및 승인 필요
- Lead 최종 승인: 미완료
- Handoff 전 필수 조치:
  1. 6개 Node와 mgmt-gw/monitor01/edge/harbor/db의 변경 전 Evidence 수집
  2. 승인된 HEP/GNP와 Route 변경안을 고정 Commit으로 구성
  3. Positive/Negative/Regression 시험 수행
  4. Reboot 지속성 및 Rollback 시험 수행
  5. Evidence Index·SHA256SUMS·비밀정보 검사 완료
  6. 독립 리뷰와 Lead 승인 후 상태와 종료일 확정

---

### 🏁 Completion Record

- Acceptance: **미달성**
- Runtime Evidence: **미확인**
- IF-06B: **BLOCKED**
- IF-16: **FAIL — DRIFT**
- 독립 Reviewer 승인: **미완료**
- Lead 최종 승인: **미완료**
- 최종 판정: **In Progress 유지**
- End / Calendar Days / Working Days: **TBD 유지**

`ICR-D-NET-01-01`은 2026-09-08 기준 완료 조건을 충족하지 않았다. ICR-AC-01~20의 PASS Evidence 또는 승인된 N/A 근거, IF-06B 차단 해소, IF-16 Drift 시정, Positive/Negative/Regression/Reboot/Rollback 결과, Evidence 무결성, 독립 리뷰 및 Lead 승인을 모두 확보한 후에만 `Done`으로 상향한다.
````

</details>


</details>
