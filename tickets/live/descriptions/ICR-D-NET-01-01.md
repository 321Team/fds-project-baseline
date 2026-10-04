<!-- fds-canonical-live:v3.1.21 record-id:ICR-D-NET-01-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/ICR-D-NET-01-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 해당 업무의 기존 AC·Exit Criteria와 실행/인수 구분을 유지한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:ICR-D-NET-01-01:end -->

<!-- oid02-contract-20261001:start -->
## 2026-10-01 OID-02 Decision Contract — CR #130 CHG-01 반영

- **Decision:** CP/Calico/kube-system Image Registry `system_images.mode` = preloaded / approved_registry / external.
- **Owner:** 이하영. Support/Decision tracking: 이권욱(#14 Lead).
- **Due:** 2026-10-07.
- **완료조건:**
  1. mode 값과 선택 사유 기록
  2. 선택 경로 승인(B=IF-10 확대 CR, C=OID-03 egress 승인 등)
  3. renderer `system_images.mode` 실제 입력 반영
  4. 대상 이미지 목록·digest·출처 기록
  5. #14의 `BLOCKED / OID-02·03` 해제 근거 기록
- HBR 입력은 #13/#130에 연결하며 미결정을 PASS로 승격하지 않는다.
- **Phase 1 Close 경계:** 2026-10-06 시점에 미완료이면 완료로 간주하지 않고 #30/#31/#32에서 `APPROVED DEFERRED` 여부와 Owner/Due를 명시적으로 판정한 경우에만 10-07로 이월한다.
<!-- oid02-contract-20261001:end -->

## 전수 검수·후속 착수 — 2026-09-23 KST

[전체 대조표·근거·담당별 후속](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5794357232). 이 블록과 아래 갱신한 AC가 현재 판정이며, 날짜가 앞선 진행 블록은 당시 이력이다. 발행 정본은 [v3.1.20](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.20).

- **이미 진행:** 3CP+3Worker Join/Ready, etcd 3/3, 9/21 CP 관리 기능 27/27, IF-16/Worker route PASS를 유지한다. [9/22 Gate2](https://github.com/321Team/infra-kubernetes/blob/2d35809313c70731c58d210b37ef29ed0a300883/docs/evidence/P1-SEC-01/GATE2_RUNTIME_EXECUTION_20260922.md)에는 6대 firewalld disabled/inactive·ens160 HEP 6개·GNP 6개가 기록돼 있다. [MON 실제 배포](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5772337466)도 완료 보고가 있어 “보호 전환 미실시/MON 미배포”를 현재 차단으로 사용하지 않는다.
- **현재 실패:** node-exporter 1/3 UP·2대 timeout, kubelet/cadvisor 6대 DOWN. 동일 노드 worker03의 TLS IP SAN 오류와 교차 노드 5대 timeout을 분리한다. [보고 근거](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5788504815); GNP/실제 Source 대조 전에는 원인을 확정하지 않는다.
- **AC 집계:** 3 RUNTIME_PASS / 8 PARTIAL / 2 FAIL(담당자 Runtime 보고 기준) / 6 NOT_VERIFIED / 1 BLOCKED. 신규 PASS는 없으며 전체 구축 공수의 진행률이 아니다.
- **실제 후속 착수:** [MON PR7](https://github.com/321Team/infra-monitoring/pull/7)로 저장소에 남은 fds→fds-app 참조 drift를 수정했다. 3개 manifest의 6개 참조·README, YAML 13개 파싱·다른 의미 변경 0·[CI SUCCESS](https://github.com/321Team/infra-monitoring/actions/runs/35856917623/job/107167471022). 독립 리뷰·병합·현장 적용은 남았다. [K8S PR21](https://github.com/321Team/infra-kubernetes/pull/21)의 selector/order는 이미 수정돼 있어 설명만 바로잡았다.
- **우리 담당 다음 범위:** 현재 Prometheus Pod/노드/IP/SA와 실제 HEP/GNP·NetworkPolicy 조회 → 승인 Source 범위 대조 → IF-06B receiver 입력 및 실제 수신 Source/return path 검증. LB는 단일 backend 장애·복구 시험을 별도로 진행한다. 기존 Join·route·방화벽 복구를 재실행하지 않는다.
- NTP는 별도 채팅의 [Ansible PR44](https://github.com/321Team/infra-ansible/pull/44)를 연결한다. 구축 지원 사실만으로 운영 담당이 이관된 것으로 보지 않으며 기존 담당·일정·open 상태를 유지한다. 이번 검수는 저장소/제출 증적 대조로, 새 실서버 실행은 하지 않았다.

---

<!-- icr-management-recovery-20260921T140152:issue-14:start -->
## CP 관리 경로 복구 및 AC-08 실측 통과 — 2026-09-21 14:01 KST

- **13:59:25–14:00:16:** CP1/CP2/CP3/Worker1/2/3에 이번 TCP10250 /32 제한 규칙 **2/1/1/3/3/3 = 13개** 영구 저장과 Runtime/Permanent 확인 성공. 앞서 확인한 CP1→CP2/CP3 2개를 포함한 TCP10250 복구 규칙은15개. 이전 CP2380/6443·Worker→CP6443의21개 저장 기록과 구분합니다.
- **14:01:47–52:** 직접 API .102/.103/.104 각각→etcd Pod3개의 고유9조합에서 logs9/9, exec9/9, localhost port-forward 및 CA·클라이언트 인증 HTTPS /health9/9, **27/27 성공**.
- **AC-08: PARTIAL → RUNTIME_PASS.** 현재 AC 집계 **3 PASS(08/13/14) · 4 PARTIAL(01/10/19/20) · 12 NOT_VERIFIED · 1 BLOCKED(12)**, Runtime 조건 충족3/20. 전체 인수·종결·독립 승인과 구분합니다.
- [사용자 실행 원본7개·SHA256·조합/성공표시 검증](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5755742235). 제공한 스크립트의 현장 실행 바이트 해시는 로그에 없어 배포본과의 일치까지 주장하지 않습니다. Worker 재실행의 ADDED=0은 기존 Runtime 규칙 확인이며 최초 추가 영수증 복구를 요구하지 않습니다.

**후속:** 이하영(K8S/SEC)의 SEC-06 정책 보완·검토 및 API 적용 준비와 이권욱(ICR)의 host firewalld 전환·관리/반환 경로·회귀/복구 검증을 공동 작업창에서 연결합니다. 현재 firewalld 유지 상태의 복구 성공을 HEP/GNP 전환 완료로 처리하지 않습니다. Prometheus CA+SA·비승인 Source 차단·Worker Harbor Pull/Pod 시작·IF-06B·재부팅 인수는 각 기존 AC에 남습니다. NTP 후속은 기존 별도 작업으로 유지합니다.

사용자 “각 티켓에 갱신” 요청에 따른 증적 반영입니다. 담당·계획일·마일스톤·open 상태 및 다른 AC 판정은 유지합니다. 아래 날짜가 있는 이전 진행 블록은 각 관측 시점의 이력입니다.
<!-- icr-management-recovery-20260921T140152:issue-14:end -->

---

<!-- monitor01-approved-merged-20260920:issue-14:start -->
## 독립 승인·병합 완료 — 2026-09-20 KST

- [x] [PKI 증적 PR #18](https://github.com/321Team/fds-project-evidence/pull/18): 이재환/supreme33-kr가 HEAD `74745237108830e0c19912e960b2e26f0957f04b`를 [독립 승인](https://github.com/321Team/fds-project-evidence/pull/18#pullrequestreview-5260358774). **22:57:30 KST 병합**, merge `c97b13fa2910f740582076f7e7b56f0da42ddf31`.
- [x] [TLS 구성 후보 PR #3](https://github.com/321Team/infra-monitoring/pull/3): 같은 독립 검토자가 HEAD `05a8114308c510c678efd64b3443c133c36ab66f`를 [승인](https://github.com/321Team/infra-monitoring/pull/3#pullrequestreview-5260362147). **22:57:47 KST 병합**, merge `e520358bb0e4739762511f1a6b3cd7d8b83c57ae`.
- [x] 승인 후 HEAD 변경 없음·미해결 리뷰 스레드 0건 확인. 병합 tree 전체의 path/mode/blob이 승인 tree와 일치(증적 696파일·MON 47파일). [MON main CI](https://github.com/321Team/infra-monitoring/actions/runs/35515026751) **SUCCESS**, 위 merge SHA의 push 실행 확인.
- [ ] 실제 배포 입력 확정·native parser/서비스 통합·TLS/Auth/IF-06B/Blackbox 현장 인수.

이번 사용자 “후속 작업 착수” 지시로 정확한 승인 HEAD를 지정하여 두 PR을 수동 병합했습니다. 증적 PR의 CI 검사 0건은 NOT RUN이며 기존 무결성 검증·독립 편입 검토와 구분합니다. 아래 과거 Draft·리뷰/병합 대기 표현은 당시 이력입니다. PKI 현장 검증 완료 범위와 AC·티켓 상태·담당·일정은 유지합니다.

**ICR 영향:** AC12 BLOCKED와 AC16 미인수, AC13/14 RUNTIME_PASS 및 기존 집계는 유지합니다. 다음은 실제 송신 Source/return route와 monitor01:443 수신 통합·허용/차단 결과 인계입니다.

실제 입력 항목과 실행/중단/복구 순서는 [MON #17](https://github.com/321Team/fds-project-baseline/issues/17)의 최신 인계표에 모았습니다.
<!-- monitor01-owner-start-20260920:issue-14:start -->
### 후속 책임과 권욱님 착수 범위 — 2026-09-20 KST

사용자 “누가 해야 하는지 확인하고 본인 범위이면 착수” 지시에 따라 기존 Lead/Support를 재확인했습니다.

| 작업 | 기존 담당 | 이번 상태 |
|---|---|---|
| MON 실행 방식·버전/artifact·receiver 포트/저장 경로/서비스 계정 확정과 서비스 통합·배포 | 이재환(MON Lead), HBR 입력 협업 | 실제 값 인계 필요 |
| 클러스터 송신 workload·Secret/Root mount·NetworkPolicy 연계 | 이재환(MON) · 이하영(K8S/SEC) | 실제 송신 대상과 참조 확인 필요 |
| CA 발급·공개 반환·PKI 검증 지원 | 이권욱 | 완료, 기존 키/인증서·증적 재사용 |
| IF-06B Source/반환 경로·host/gateway 정책 확인 및 필요한 최소 보완 | 이권욱(ICR Lead), K8S/MON 협업 | 아래 읽기 전용 송신 식별 단계 준비 완료·현장 출력 대기 |

**우리의 다음 현장 단계:** 기존에 정본 6노드 클러스터의 `kubectl` 조회가 정상 동작하던 **k8s-control01 터미널/계정**에서 아래만 실행합니다. 전체 클러스터/Worker 경로 재수집 대신 `monitoring-api`의 실제 송신 workload를 식별합니다.

```bash
date -Is
kubectl config current-context
kubectl -n monitoring-api get pods -o wide
kubectl -n monitoring-api get deployment,statefulset
```

조회 대상/현재 context가 예상과 다르거나 Forbidden·연결 오류가 나면 후속 접근/변경 없이 오류를 반환합니다. Namespace/Prometheus workload가 없으면 임시 k3s나 다른 Pod로 대체하지 않고 MON/K8S 담당의 정본 sender 준비에 연결합니다. 이름만으로 sender를 확정하지 않고 해당 workload/컨테이너와 Remote Write 담당을 대조합니다. Secret 값·kubeconfig 본문·개인키는 수집하지 않습니다.

출력으로 실제 sender를 고정한 뒤 monitor01에서 해당 전송의 Source와 return path를 확인합니다. Pod IP·Worker host route의 source를 receiver가 관측한 Source로 입력하지 않습니다. sender가 준비되면 TLS 서비스 완성 전에도 제한된 연결 시도의 패킷 헤더로 Source를 확인할 수 있으므로 TLS 인수 완료를 이 식별 단계의 선행조건으로 추가하지 않습니다. 상세 능동 연결/관측은 sender 식별 후 범위를 고정합니다.

기존 Worker3의 `.30 via .58 / source .105·.107·.108` route-get 및 AC14 RUNTIME_PASS는 해당 관측 범위로 재사용합니다. 이 기록은 새 원격 실행/패킷 관측·방화벽/NAT/route 변경·Runtime PASS가 아니며, 기존 AC12/16·티켓 상태·담당·일정은 유지합니다.
<!-- monitor01-owner-start-20260920:issue-14:end -->
<!-- monitor01-approved-merged-20260920:issue-14:end -->

---

<!-- monitor01-progress-sync-20260919:issue-14:start -->
## monitor01 PKI 완료·IF-06B 통신 인수 잔여 — 2026-09-19

진행 체크는 이번 하위작업의 완료 범위이며 기존 요구사항·AC 합격 체크와 구분합니다. 기존 담당·일정·티켓 상태와 과거 기록은 유지합니다. 아래의 서명 전·반환 전 표현은 작성 당시 이력이며 이 갱신을 최신 기준으로 읽습니다.

- [x] monitor01 인증서 CA 서명 및 공개 반환 완료: 원본 SHA256 2/2, 현지 `PUBLIC_KEY_MATCH=PASS`·`CHAIN_IP_SERVER_PURPOSE=PASS` 확인. ca01 XFS unmount·`fds-ca inactive` 확인. VM 전원 OFF는 미확인. 근거: [PKI 증적 PR #18](https://github.com/321Team/fds-project-evidence/pull/18).
- [x] IF-06B 수신 구성 후보 작성: [TLS 구성 후보 PR #3](https://github.com/321Team/infra-monitoring/pull/3), HEAD `05a8114308c510c678efd64b3443c133c36ab66f`. 정적 검사·단위시험 13/13 및 [CI #35442097555](https://github.com/321Team/infra-monitoring/actions/runs/35442097555) SUCCESS. 서버에 설치하거나 경로·방화벽을 변경한 결과는 아님.
- [ ] 수신 구성 독립 검토 및 실제 입력 인계: 관측 송신 Source·return route, 실행 모델/버전·digest, receiver port/저장 경로, Auth·Root 참조.
- [ ] monitor01:443 TLS/Auth/localhost receiver 적용과 IF-06B 허용·차단/heartbeat 단절·복구 실제 시험. 송신 측 relabel만으로 receiver의 임의 payload 차단까지 입증하지 않음.

**AC 판정:** ICR-AC-12는 **BLOCKED 유지**, AC16도 서비스·통신 인수 미완료입니다. AC13/14 RUNTIME_PASS 및 집계 **2 PASS·5 PARTIAL·12 NOT_VERIFIED·1 BLOCKED**를 변경하지 않습니다. 기존 LB/IF-16/반환 경로 증거는 재사용하며 동일 현황 수집을 다시 요구하지 않습니다.

**PR 조회:** 구성 PR #3·증적 PR #18 모두 open/Draft, 제출 리뷰 0건, 미병합. 상세 확인 범위와 후속 순서: [MON #17](https://github.com/321Team/fds-project-baseline/issues/17).
<!-- monitor01-progress-sync-20260919:issue-14:end -->

---

<!-- icr-lb-monitor-received-20260918:start -->
## LB 준비 충족·monitor01 수신 구성 잔여 — 2026-09-18

- **LB:** 21:27:33–34 KST 원본 `FDS_P1_LB_01_STAGEB_PREFLIGHT_20260918T122733Z_6kk8lyhy.tar.gz`, SHA256 `579bee923366dae6568cfa69734227354c725cb6b0608b38fe9c3c79293e1151`, 내부46/46·승인 수집기 일치. 전후 backend3/3 UP/L4OK, .109→CP3대 TCP6443 성공. [LB #9](https://github.com/321Team/fds-project-baseline/issues/9)의 해당 요구사항·AC에 반영했습니다. 단일 backend 장애 중 API 유지·복구는 미실행입니다.
- **monitor01:** 사용자 화면에서 ens160 `10.250.10.30/24 UP`, host TCP443/9115 listener 미관측, `*:9090 systemd(pid1)`, 조회한 MON 서비스0 loaded를 확인했습니다. 후속 사용자 출력에서 `[::]:9090 cockpit.socket → cockpit.service`, cockpit.socket enabled를 확인했습니다. 조회한 MON 서비스 unit은 나타나지 않았고 현재 사용자/root의 Podman 목록은 각각 비어 있습니다. Docker 미설치나 다른 사용자·비표준 실행의 부재를 단정하지 않습니다. 화면 SHA256 `2bcd4435034ea0d04422d1803841a4a61906c08a62b64d3acffa0d3ad02c2084`; 촬영시각은 표시되지 않았습니다. [MON #17](https://github.com/321Team/fds-project-baseline/issues/17)에 실제 관측과 최소 식별 후속을 연결했습니다.
- **AC 영향:** AC13/14 RUNTIME_PASS와 전체 집계2PASS·5PARTIAL·12NOT_VERIFIED·1BLOCKED는 유지합니다. LB 자체 AC 충족을 ICR AC 추가 PASS로 합산하지 않습니다. AC12 IF-06B는 계속 BLOCKED, AC16은443수신 및 Receiver/TLS/Auth 완료 근거가 부족합니다. monitor01의9090만으로 K8S6Node Cockpit AC10을 변경하지 않습니다.
- **다음 우리 범위:** 동일 LB/IF16/monitor01 현황 재수집 대신 LB 단일 backend 장애·복구 실행안과 monitor01 전용 TLS 프로파일·공개 CSR/인증서 인계를 준비합니다. K8S Join/보호 전환 담당과 MON Lead 역할을 유지합니다.


**소스 구현·검증 완료:** [infra-pki PR3](https://github.com/321Team/infra-pki/pull/3), 최신 HEAD `f778af0dc8178608edc8ddef509d01d3a81990fe`. 기존 프로파일 후보 `5c9459c`에 monitor01 현지 키·CSR 생성/재사용 도구와 기존 CA 서명·반환 검증 절차를 추가했습니다. 같은 PR에서 신규7파일(프로파일2·실행도구1·시험2·문서2)의 검토·병합을 완료했습니다. IP SAN은 `10.250.10.30` 하나, CA:FALSE/serverAuth이며 키는 monitor01에 보관하고 공개 CSR·receipt·해시만 내보냅니다.

- LOCAL: 관련 격리 시험 **20/20 PASS**, Python AST·문서 Bash 구문 PASS.
- CI: [source-validation #35349450313](https://github.com/321Team/infra-pki/actions/runs/35349450313) **SUCCESS**. 위 HEAD에 대한 PR 병합 테스트에서 정적31파일 및 전체31/31 시험 PASS, 원격7파일과 검증 소스 Git blob 일치.
- REVIEW/MERGE: [supreme33-kr의 독립 APPROVED](https://github.com/321Team/infra-pki/pull/3#pullrequestreview-5248507791), 2026-09-18 22:50:36 KST, 대상 HEAD `f778af0dc8178608edc8ddef509d01d3a81990fe` 확인. 차단 지적·미해결 thread 없음. ens160 참고사항은 기존 monitor01 현장 출력의 ens160/10.250.10.30과 대조했습니다. 2026-09-19 01:22:01 KST 병합 완료, merge `2be575329349973babd2fa392f22c69b34c76253`. 동일 승인 소스의 실행마다 독립 승인을 추가하지 않습니다.
- MAIN CI: [source-validation #35368045592](https://github.com/321Team/infra-pki/actions/runs/35368045592) **SUCCESS**, merge 커밋에서 정적31파일·전체31/31 시험 PASS를 job log로 확인했습니다.
- DISTRIBUTION: `FDS_MONITOR01_CSR_f778af0_v1.0.tar.gz`, SHA256 `c2f7ba2a599c7b050860cce14986908128fa8cc1b38e7ecc503bd5fd5a903c87`. 병합 소스9파일과 Git blob 9/9 일치, 내부11파일 hash·외부 hash·archive12members 원본 일치 및 기본 PLAN_ONLY 실행 PASS. 실행 로직 변경 없이 승인 파일과 배포 설명·기록을 묶었습니다. 해당 배포 준비 당시에는 monitor01 CSR 생성/CA 서명/TLS 배포 모두 NOT RUN이었으며, 후속 CSR 수신 결과는 아래에 기록합니다.
- RUNTIME: monitor01 키·CSR 생성은 CREATED receipt 및 수신 CSR 검증으로 확인했습니다. ca01 서명·설치·TLS/Auth/Remote Write는 **NOT RUN**입니다.
- 후속: 기존 CA 서명·공개 반환물 검증 → MON Lead의 TLS proxy/localhost receiver 연동. CSR 생성만으로 Runtime AC를 PASS 처리하지 않습니다.

**CSR Runtime 수신·검증 완료 — 2026-09-19:** 사용자 제출 `FDS_MONITOR01_CSR_09f8u69y.tar.gz` / SHA256 `11be49b5909bcef4ca8a0700d32407b8cddd6c78f9f15e18fc294f8c8cac6c32`. receipt는 monitor01/server01_monitor, `CREATED`, 생성 **01:51:16 KST**를 기록합니다.
- 외부 SHA·공개파일3개 allowlist·내부2/2 hash, CSR 자기서명, RSA3072, Subject `CN=monitor01,OU=Monitoring,O=FDS,C=KR`, IP SAN `10.250.10.30` 하나를 수신 원본으로 검증했습니다.
- 요청 ID / CSR SHA: `37fda6d9fb99f101bf213a8e6a070c3e6dce3ba5238b54f178d9c62c8ddd3fa1`. PEM 공개키 SHA `bf57594c8523171e05df87a118daf6b06e0cac1af91914c5cecf25e71e9313a9`가 receipt와 일치합니다.
- 실행 소스 SHA `433a34d0953d26cfc3427b977df208ef3336a8d982f0be386cac9937ad156300` 및 CSR/Leaf 프로파일 hash가 병합 `2be575329349973babd2fa392f22c69b34c76253`와 일치합니다. 개인키는 수신하지 않았고, 현지 키 일치는 승인 실행기의 receipt 근거입니다.
- 오프라인 CA 입력 `FDS_MONITOR01_CA_37fda6d9_v1.0.iso` / SHA256 `ce4a62e40233abeacc36d4cd20fa15103755c9108422a36876223615348d07ca` 준비. 승인 문서 Bash블록2개 그대로, ISO9파일 readback·내부8hash·Bash구문 PASS. CA 서명은 실행하지 않았습니다.
- 후속은 ca01 기존 보호 볼륨·현재 시각·동일 요청 발급 여부를 확인하고, Lead가 선택한 유효 일수로 기존 CA 서명 → 공개 Leaf/Root 반환 검증 → MON Lead 연동입니다. 재서명으로 우회하거나 CA 대장을 초기화하지 않습니다.
- **상태:** CSR 생성·공개 인계 검증 완료 / CA 서명·TLS 배포 NOT RUN / IF-06B·ICR-AC12/16 인수 미완료. 기존 AC 체크·담당·일정은 유지합니다.
<!-- icr-lb-monitor-received-20260918:end -->

<!-- icr-our-route-start-20260918:start -->
### 다음 우리 담당 실행 — LB backend3/3, IF-06B 연동 준비

IF-16 AC13 3/3 충족 후 사용자 “착수” 지시에 따라 [LB #9](https://github.com/321Team/fds-project-baseline/issues/9)의 승인된 읽기 전용 수집을 다음 현장 작업으로 안내합니다. 기존 package SHA와 내부 manifest를 확인했으며 실제 실행 결과는 대기입니다. 동일 경로·6/6 Ready·CP1 인증 API·DAD 수집은 반복하지 않습니다.

IF-06B는 [infra-monitoring main 73b9432](https://github.com/321Team/infra-monitoring/tree/73b9432e8c793f64469ea708c14018f010ad74c1) 및 [MON #17](https://github.com/321Team/fds-project-baseline/issues/17)을 대조했습니다. E-CANON Monitoring 및 monitor01 수신 구성의 구현·현장 증거가 아직 확보되지 않았습니다. 정해진 목적지 `10.250.10.30:443`·heartbeat=1·5분 단절 탐지는 유지하며 실제 source/return, TLS path/auth의 비밀값을 제외한 참조, receiver 및 허용 payload의 실행 증거를 연결합니다. MON Lead 이재환·Support 이권욱 범위와 기존 AC12/15/16/17 판정은 유지합니다. LB 점검과 이 입력 확인은 병행하며 서로의 새 선행 대기를 만들지 않습니다.

## 우리 담당 후속 진행 — 2026-09-18 db01 NIC 수정 병합·접근 복구

사용자의 “승인 완료됨 진행” 지시에 따라 ICR Lead 이권욱 범위의 IF-16 승인본 병합과 현장 배포 준비를 완료했습니다.

| 작업 | 확인된 현재 상태 | 다음 실행 |
|---|---|---|
| IF-16 edge/harbor/db | PR18 승인·병합 이력 유지. **db01 v1.0 적용 안내 철회**, [NIC 수정 PR19](https://github.com/321Team/infra-kubernetes/pull/19) 승인·병합 및 v1.1 배포본 제공 | AC13 3/3 충족 및 edge 비활성 프로필 자동연결 해제 확인 완료. 경로 작업 종료 |
| LB backend3/3 | 기존 승인 수집기 바이트 그대로 실행 묶음 제공, [#9 기록](https://github.com/321Team/fds-project-baseline/issues/9) | k8s-api-lb01 현장 수집. 같은 CP1 API/DAD 반복 없음 |
| mgmt-gw·IF-06B | 실제 Forward/NAT/TLS/Auth/Payload 결과 미확인 | Monitoring #17의 Receiver·인증/정책 입력과 연결 |
| Worker 경로 | AC14 Runtime PASS·15:56 6/6 Ready 증거 재사용 | 같은 상태 재수집·Worker 재가입 없음 |

아래 REVIEW~IF-16 실행 검증은 최초 PR18 배포 이력입니다. 최신 수정본은 이어지는 PR19 완료 기록을 따릅니다.

- **REVIEW:** [hayeounglee 승인 #5245389244](https://github.com/321Team/infra-kubernetes/pull/18#pullrequestreview-5245389244), 16:37:43 KST, 정확한 HEAD `11cfd36cff489fe1351afc4f5c5dd97eb3a111e4`.
- **MERGE:** 16:40:19 KST, commit [e26aface3a930d9a814f9fac0e6105c11cd78a75](https://github.com/321Team/infra-kubernetes/commit/e26aface3a930d9a814f9fac0e6105c11cd78a75). 병합된 6개 파일은 승인 HEAD의 Git blob과 모두 일치합니다. 미해결 리뷰 thread·댓글·충돌은 확인되지 않았습니다.
- **STATIC/MOCK:** 기존20/20 PASS와 소스 manifest 검증 재사용. CI check runs/statuses 0건은 NOT RUN입니다.
- **PUBLICATION:** `FDS_IF16_Route_11cfd36_v1.0.tar.gz`와 SHA256 제공. archive SHA256 `ea06a5ad881331c433607244951d631b47c06c88d401b78c71a6f8be4db5c327`, 파일9개/배포 manifest8개 일치. 승인된 기존6개 파일을 그대로 보존하고 실행기가 소비하지 않는 배포 기록·안내만 추가했습니다.
- **SOURCE:** `if16_route.py` SHA256 `4c4190e0711b9ecad29959471ef3de587f9f7d3ccea4e8399733f7b92842c8ec`.
- **IF-16 실행 검증:** 이 검토 환경에는 현장 SSH 키가 없고, 승인된 경로 실행기의 실제 적용 영수증·재부팅 시험은 아직 확보하지 못했습니다. 아래 db01 방화벽 복구 현장 결과와 구분하며 AC13과 전체 AC를 일괄 PASS로 상향하지 않습니다.

기존 PR18의 공통 ens160 가정은 db01에 맞지 않아 아래와 같이 정정합니다. 수정 PR19는 edge/harbor ens160, db01 ens192를 명시하고 누락된 IF-16 경로만 대상으로 합니다. --apply가 최신 상태 검사·원본 JSONL 기록·추가·route-get 확인을 한 번에 수행하므로 별도 plan/inspect 업로드/authorization/타이머 입력을 요구하지 않습니다. 한 호스트 성공 후 다음 호스트로 진행하고 실패하면 로그와 정확한 JSONL 영수증을 보존합니다. 본인 추가가 확인되는 변경만 보상하며 불명확한 상태는 PARTIAL_REVIEW_REQUIRED입니다.

[중앙 권한 정책](https://github.com/321Team/fds-project-baseline/blob/b2e4612cf2e417b10e7f145c5b1e5f58dbe1b948/governance/REVIEW_AUTHORITY_POLICY.md)에 따라 승인·병합된 동일 코드 실행마다 독립 승인을 추가하지 않습니다. 기존 CP 유지 계약·방화벽·타이머·Worker/HEP/GNP·담당·정본 AC·일정·Done 상태는 변경하지 않았습니다.

### PR19 수정본 승인·병합·배포 준비 완료

- **REVIEW:** [hayeounglee APPROVED #5245982139](https://github.com/321Team/infra-kubernetes/pull/19#pullrequestreview-5245982139), 2026-09-18 17:52:24 KST, 현재 HEAD `3898d0ea0116dcb8698c149193ac77050d51cc80`와 일치. 차단 의견·inline 댓글 없음.
- **MERGE:** 18:08:39 KST, [c2c0bf28ebfe7ba32586e3873d387cf3c524c220](https://github.com/321Team/infra-kubernetes/commit/c2c0bf28ebfe7ba32586e3873d387cf3c524c220). 병합 결과와 승인 HEAD의 6개 Git blob 모두 일치.
- **STATIC/MOCK:** 기존 32/32 결과 재사용, local source manifest5/5 일치. CI check runs/statuses0건은 **NOT RUN**.
- **PUBLICATION:** `FDS_IF16_Route_3898d0e_v1.1.tar.gz` 및 동일 이름 `.sha256` 제공. archive SHA256 `82ad04a7876c8badb330011be241f7df201ec74e589272163fb5125c75e41f9d`. 실행 소스 SHA256 `534ce709fe2cfe7e13e0da882202649d3dc9710c1121faf4cda770b45ce51f46`. 승인된 기존6파일을 그대로 보존하고 비실행 배포 안내·release record만 추가. package manifest8/8 및 archive9개 파일 확인.
- **현장 적용 범위:** edge01/harbor01은 ens160, db01은 ens192. db01의 정상 기존 kernel 경로와 별도 방화벽 TCP22/WinSCP 복구가 이미 확인됐으므로 접속 복구를 위한 --apply 반복은 요청하지 않음. edge/harbor 중 IF-16 미완료 호스트에 새 묶음 사용. db01 NM 저장 상태는 해당 잔여 확인이 필요할 때 기본 읽기 전용 모드 사용 가능; 추가 승인 문서·타이머 절차 없음.
- **RUNTIME 후속:** 사용자 제공 v1.1 실행 화면 2건에서 archive 및 package SHA256 검사 성공 후 `STOP: Multiple profiles bind ens160`, `APPLY_RC=2`를 확인했습니다. 첫 화면은 edge01, 두 번째 화면은 호스트명이 보이지 않아 harbor01로 확정하지 않습니다. 승인 소스의 initial collect에서 중단된 출력이므로 이 실행기의 네트워크 변경 명령 전 중단입니다. journal/lock/로그 파일 생성은 가능하며 시스템 전체 무변경을 뜻하지 않습니다. 재부팅·경로 적용 성공 및 전체 AC13/ICR PASS는 아닙니다.

### 현장 중단: ens160 저장 프로필 조건 확인

- `310ff985-4609-4613-b6f1-1c620c5098f0.png`: 프롬프트 `server08@edge01`, receipt `/var/lib/fds/if16-routes/20260918T092045Z_af1f7e35747242128c84922106e00050.jsonl`, `Multiple profiles bind ens160`, RC2.
- `adce69f3-c600-451e-9536-7bec76307fc9.png`: 호스트명 미표시, receipt `/var/lib/fds/if16-routes/20260918T092055Z_03da9263ad7042f2888ddbff32e2415b.jsonl`, 동일 오류, RC2. 두 번째 호스트는 다음 hostname 출력으로 식별합니다.
- 승인 소스는 활성 ens160 프로필 1개 식별과 IP/프로필 검사를 통과한 다음, 저장된 ethernet 프로필 전체에서 ens160 바인딩 UUID 목록이 활성 UUID 하나와 정확히 일치하는지 검사합니다. 비활성·autoconnect=no 프로필도 이 목록에 포함하므로 이 STOP만으로 네트워크 설정 자체가 잘못됐다고 판정하지 않습니다. 실제 프로필 목록이 없으므로 중복 수·백업 여부·설정 조회 중 변동 여부는 미확인입니다.
- `apply()`의 최초 `snapshot()`가 변경 처리 이전에 실행되고, 이 지점의 Stop은 최상위 `STOP`으로 출력됩니다. 변경 처리 이후 실패는 별도 복구 상태를 반환합니다. 이번 출력에서는 경로 추가·NM 프로필 수정 전 중단으로 판정합니다. 영수증·lock·로그 등의 파일 생성은 이미 있을 수 있습니다.
- 다음 작업은 해당 호스트의 hostname·활성 UUID·ens160 저장 프로필의 autoconnect/priority/timestamp/IP/route 설정 및 현재 kernel route를 한 번에 읽기 전용으로 확인하는 것입니다. 빈 영수증 재수집·apply 반복을 요구하지 않습니다. 실제 목록 없이 프로필 삭제·자동연결 해제·검사 우회·NM 재시작을 안내하지 않습니다. 기존 승인 소스와 배포본은 수정하지 않았습니다.
- [NetworkManager 공식 설명](https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nm-settings-nmcli.html): 여러 연결 프로필 보유 자체는 지원되는 구성이며, 자동 연결 후보 선택은 autoconnect/priority/최근 연결 시점의 영향을 받습니다. 현장 후보의 설정을 확인한 뒤 필요한 수정 범위를 판단합니다.

### 최신 IF-16 현장 확인 — edge01·harbor01 경로 조건 충족

2026-09-18 사용자가 제공한 두 호스트의 전체 읽기 전용 출력 기준입니다. nmcli 버전은 둘 다 `1.58.0-1.el10`이며 Codex가 서버에 직접 접속해 재수집한 것은 아닙니다.

| 호스트 | 활성 프로필 / UUID | 저장된 IF-16 경로 | Runtime 및 .30 route-get |
|---|---|---|---|
| edge01 | `fds-edge01` / `fa5bbb7a-dca3-4a93-b89f-51b1b0cdf152` | `10.250.10.0/24 via 10.1.93.58`, profile table0 / metric-1 | kernel `via .58 dev ens160 proto static metric100`; `.30 via .58 dev ens160 src 10.1.93.50` 확인 |
| harbor01 | `fds-harbor01` / `3094c330-0b11-4463-9409-29c11bca6fcb` | `10.250.10.0/24 via 10.1.93.58 metric100`, profile table0 / metric-1 | kernel `via .58 dev ens160 proto static metric100`; `.30 via .58 dev ens160 src 10.1.93.54` 확인 |
| db01 | 기존 kernel 경로 및 신규 .30 조회 | NM 저장 상태는 별도 미확인 | `via .58 dev ens192 metric101` 및 `.30 via .58 dev ens192 src 10.1.93.55` 확인. AC13 호스트 조건 충족 |

- 두 호스트 모두 활성 프로필 `autoconnect=yes / priority100`, 주소·게이트웨이 정상, policy rule은 기본 local/main/default입니다. 경로를 새로 추가할 필요가 없습니다. 기존 v1.1 apply를 반복하거나 table/metric을 바꿔 실행기 검사를 통과시키지 않습니다.
- 두 호스트의 비활성 `ens160` UUID는 `6b9f0643-4a4e-324d-a969-9e5393d7e0bf`이고 `autoconnect=yes / priority-999`, 주소는 모두 `10.1.93.54/24`입니다. **edge01에서는 다른 호스트 주소**이므로 해당 비활성 UUID의 `connection.autoconnect=no`만 설정하도록 안내합니다. 현재 활성 주소 충돌을 관측한 것은 아닙니다. harbor01의 비활성 주소는 자기 주소와 같고 우선순위가 낮으므로 이번에 수정하지 않습니다. 후속 첨부에서 edge01의 해당 UUID에 `connection.autoconnect no`를 설정하고 조회 `no`를 확인했습니다.
- **ICR-AC-13: RUNTIME_PASS — edge/harbor/db 3/3 조건 충족.** 후속 db01 `.30` route-get의 gateway .58 / device ens192 / source .55까지 확인했습니다. 새 경로 적용 영수증·NM 프로필 재작성·재부팅·코드 재승인을 이 AC의 추가 조건으로 두지 않습니다. 재부팅 검증은 기존 AC18의 별도 범위입니다.
- 비활성 프로필 자동연결 해제 후에도 v1.1은 저장 프로필 전체를 세므로 STOP할 수 있습니다. 이는 운영 경로 증거와 실행기 적용 가능성의 차이이며, 이번 이미 정상인 두 경로를 수정할 이유가 되지 않습니다. 기존 승인 소스·배포본은 보존합니다.

### AC13 최종 현장 확인 — IF-16 3/3 충족

2026-09-18 후속 사용자 첨부를 직접 확인했습니다.

| 대상 | 확인한 결과 | 판정 |
|---|---|---|
| db01 | `ip -4 route get 10.250.10.30` → `10.250.10.30 via 10.1.93.58 dev ens192 src 10.1.93.55 uid 1001` | 기존 kernel 경로와 합쳐 AC13 해당 호스트 충족 |
| edge01 비활성 ens160 프로필 | UUID `6b9f0643-4a4e-324d-a969-9e5393d7e0bf`의 `connection.autoconnect no` 설정 후 조회 `no` | 잘못된 .54 주소 프로필의 자동 연결 해제 확인 |

- db01 원본: `281b1b85-e43f-4f78-b7ac-c212dd686ebc.png`, SHA256 `c40571e21ccce5e1889f1deb4ded8d853b6f7c07ce3ecb86e9c3b69fc63fea10`.
- edge01 원본: `e9547919-03b9-457b-89d3-838499577f54.png`, SHA256 `210759051a56fa80c6aad237fb7af03a6fe243a215e800369dc8e5a3e91a8934`.
- 앞서 받은 edge01·harbor01의 `10.250.10.0/24 via .58` kernel 경로 및 `.30` route-get(source .50/.54)과 이번 db01 결과를 합쳐 **ICR-AC-13 RUNTIME_PASS, 3/3 충족**으로 판정합니다. 경로를 새로 추가한 실행 성공을 뜻하지 않으며 정상 기존 상태의 관측을 근거로 합니다.
- edge01 비활성 프로필의 자동 연결 해제는 실제 사용자 실행 결과입니다. Harbor 프로필 수정·경로 재적용·NM 재시작은 요청하거나 실행하지 않았습니다.
- 추가 v1.1 실행·동일 route-get 반복은 필요 없습니다. db01 NM 저장 상태, 재부팅 지속성(AC18), mgmt-gw Forward/NAT(AC15), 실제 패킷 source 보존(AC17), 전체 ICR 인수는 별도 범위입니다. 이번 결과로 티켓 전체를 Done으로 변경하지 않습니다.

### db01 결함·SSH 장애 분리

사용자 제공 현장 출력에서 db01 관리망 `10.1.93.55/24`는 **ens192**, 스토리지망 `10.250.40.20/24`는 **ens160**입니다. 전 호스트 ens160 가정과 이에 따른 v1.0 db01 배포 안내는 구현·검증 누락으로 정정했습니다. [PR18 본문 정정](https://github.com/321Team/infra-kubernetes/pull/18)을 게시했고 승인본·과거 해시는 보존합니다.

- **반환 경로:** 제공된 kernel route `10.250.10.0/24 via .58 dev ens192 metric101`과 Ansible .10 route-get/source .55가 확인됩니다. db01을 현재 route 누락으로 단정하지 않습니다. 후속 `.30` route-get도 ens192/source .55로 확인돼 AC13은 3/3 충족입니다. NM Persistent·재부팅은 별도 미확인입니다.
- **코드 수정:** [PR19](https://github.com/321Team/infra-kubernetes/pull/19), HEAD `3898d0ea0116dcb8698c149193ac77050d51cc80`, 소스 SHA256 `534ce709fe2cfe7e13e0da882202649d3dc9710c1121faf4cda770b45ce51f46`. db ens192를 수집·프로필 선택·추가/보상·검증에 연결했고 ens160 storage 및 기존 정상 경로를 보존합니다. STATIC/MOCK32/32(기존20+NIC12) PASS. hayeounglee의 해당 HEAD 승인 확인 후 병합했고 아래와 같이 v1.1 배포본을 제공했습니다. 후속 사용자 실행 2건은 아래 기록한 ens160 저장 프로필 검사에서 네트워크 변경 전 STOP입니다.
- **장애 인과관계:** 원본 코드의 두 NIC MOCK은 첫 ens160 주소 조회 후 STOP/경로 변경0건입니다. 이 도구는 firewalld/sshd를 변경하지 않습니다. 원본 실행 영수증 없이 실제 장애 유발을 단정하지 않습니다.
- **SSH 차단 위치 확인:** 사용자가 추가 제공한 public list-all에서 services 없음·ports5432/tcp·SSH rich rule은 .29/32만 확인됐습니다. 출력 시각17:35:06–17:35:14 동안 Ansible `10.250.10.10 → 10.1.93.55:22` SYN8건이 db01 ens192에 도착했고, 매번 db01이 ICMP admin-prohibited를 반환했습니다(16 packets, drop0). **DB 호스트 필터 거부가 확인됐고 public의 Source 허용 누락과 일치**합니다. 정확한 nft reject 규칙까지 식별한 것은 아닙니다. 반환 경로 누락으로 해석하지 않습니다. 첨부 WinSCP는 .55 연결 timeout이며 사용자가 출발지를 **server01 Host 10.1.93.23**으로 확인했습니다. .23의 유입 패킷은 별도 수집하지 않았으며, 후속 사용자 메시지에서 WinSCP 접속 성공을 확인했습니다.
- **최소 복구 안내:** DB 콘솔에서 Ansible `10.250.10.10/32`와 WinSCP `10.1.93.23/32` 각각으로부터 목적지 `10.1.93.55/32 TCP22`만 허용하는 두 rich rule을 public Runtime에 추가하고, Ansible TCP/SSH 및 WinSCP 접속 확인 후 같은 두 규칙만 Permanent에 저장합니다. reload·전체 SSH 서비스 개방·route 변경·고정 회수 타이머는 필요 없습니다. nc Connected는 TCP 접근 복구이며 SSH 인증/SFTP 성공으로 확대하지 않습니다. 기존 .29/32 SSH 허용은 보존합니다. 허용 범위를 /24나 전체 ssh 서비스로 넓히지 않습니다. IF07 K8s6대 승인 승계를 주장하지 않고 현재 사용자 요청의 db 관리 접근 복구로 기록합니다. **후속 현장 결과:** Ansible `nc -vz -w 3 -s 10.250.10.10 10.1.93.55 22`가 두 번 Connected(각 0.01초)이며 사용자가 WinSCP 접속 성공을 보고했습니다. Ansible SSH 인증/자동화 실행까지 확인한 것은 아닙니다. 다만 Permanent 저장 두 명령은 `INVALID_RULE: empty rule`로 실패했습니다. 첨부 화면에서 `$DB_SSH_ANSIBLE_RULE`·`$DB_SSH_WINSCP_RULE`이 빈 인자로 전달된 것이 원인이며, 변수 정의와 저장 명령을 나눠 안내한 점을 보완하여 전체 규칙 문자열을 직접 넣는 두 Permanent add와 동일 두 query를 안내합니다. **영구 저장 후속 확인 완료:** 사용자 첨부 `a6d7a749-b396-4b29-9bd2-73c8507d18dd.png`에서 db01 `server08` 터미널의 두 literal `--permanent --zone=public --add-rich-rule` 및 동일 규칙의 `--query-rich-rule`이 순서대로 `success`, `success`, `yes`, `yes`를 출력했습니다. Ansible `10.250.10.10/32`·WinSCP `10.1.93.23/32` 각각에서 목적지 `10.1.93.55/32 TCP22`를 허용하는 두 규칙의 Permanent 존재를 확인했습니다. 앞선 TCP22·WinSCP 접속 결과와 합쳐 **이번 db 관리 접근 방화벽 복구 조치는 완료**로 기록합니다. 추가 reload·재부팅 시험을 요청하지 않습니다. 재부팅 지속성 실증이나 Ansible SSH 인증·플레이북 성공, IF-16 전체 AC 완료를 뜻하지 않습니다.

호스트 명령은 사용자가 현장에서 수행했으며 위 연결 결과는 사용자 제공 증거입니다. Codex가 실제 서버에 접속하거나 규칙을 추가한 것은 아닙니다.
<!-- icr-our-route-start-20260918:end -->

<!-- icr-cp1-workday-20260918:start -->
## 최신 CP Runtime·Join 결과 — 2026-09-18 12:33 KST

**CP2·CP3 실제 Join 성공,3CP Ready/etcd3voter·health3/3 확인. CP 구축을 막던 CP2 잔여 구성·미가입 상태는 해소됐습니다.**

기존 CP1 Job `c564ae97530dfe80`에서 Join Job `16219c68779b3d13`의 Runtime 소유권 인계가 성공했습니다. **기존15:15 KST 자동 회수 타이머는 인계 단계에서 정지됐고 Runtime 해시는 전후 동일**했습니다. 성공한3CP의 연결을 유지하며 명시적인 대체 보호 인계 또는 membership에 따른 철수로 종료합니다. 과거의 “15:15 회수 예정”을 현재 상태로 사용하지 않습니다.

CP2는 root전용 백업 후 manifest3개를 격리하고12:31:09 Join rc0, CP3는 초기 정리 없이12:32:44 Join rc0입니다. 마지막12:33:36.720KST 관측에서3CP Ready·3voter·learner0·etcd health3/3를 확인했습니다. 임시 인증정보는REVOKED, 전체종료12:33:37입니다.

[검증·원본 증적](https://github.com/321Team/infra-kubernetes/blob/5e9e09e7a1820c230bb5724ce05897c7689ef065/ops/cp-join-20260918/results/20260918T033022Z_16219c68779b3d13/README.md) · [통합 사후 검토 요청](https://github.com/321Team/infra-kubernetes/pull/16#issuecomment-5724813354). archive SHA3108ecac…ba3262, 내부15/15 및 승인 실행기 바이트 일치. source `bab9608557205b3bf5294b729d0960517d7a2847`는 그대로입니다.

**인계:** Kubernetes의 Worker 가입/후속 구축과 LB3/3 검증으로 이어갑니다. CP1시험·복구 자산 점검·CP방화벽 적용·Join을 되풀이하지 않습니다.

independent_acceptance=PENDING, cp1_accepted=false를 유지합니다. 이번 성공으로 전체 ICR AC를 체크하거나 종결하지 않습니다. 실패 회수 시험·cross-node CNI·Worker·LB3/3/전환·HEP/GNP·Permanent/reboot 지속성은 별도입니다. 타이머/Runtime 동일 확인은 Join 전 인계 시점의 원본 결과이며 현재 서버 재조회가 아닙니다.
<!-- icr-cp1-workday-20260918:end -->

<!-- icr-ac-followup-20260918:start -->
## AC 확인·현장 후속 결과 — 2026-09-18 15:56 KST

[현장 원본·검증 결과](https://github.com/321Team/infra-kubernetes/blob/ea4aef3c960fd79377225f7f037bc39cd04df469/ops/icr-followup-20260918/results/20260918T065614Z_zzi65aal/README.md) / archive SHA256 `5f743db12061f47bac8b5cf4fcc41014e6c749159cf938371d7d56e51ced90a4`. 외부·내부6/6 체크섬, 배포 수집기 및 원본 기반 summary 재계산이 일치합니다. 검토자가 새 서버 명령을 실행한 것은 아닙니다.

| 항목 | 현재 확인 결과 |
|---|---|
| 클러스터 | **3CP+3Worker 6/6 Ready**, 기존 CP3 UID/IP/역할/Ready 유지 |
| Calico | calico-node6개+controller1개 Running/Ready |
| Worker3 | kubelet·containerd active/running, kubelet/CA·Calico CNI 파일 존재 |
| LB | CP1→.109:6443 CA 검증·인증 Node GET 성공. backend별3/3·failover NOT_TESTED |
| **AC-14** | **Runtime PASS 유지** — Worker3 .30 route-get rc0, source .105/.107/.108 및 gateway .58 일치 |

Worker 미가입 상태는 해소됐으며 Join·동일6/6 수집을 반복하지 않습니다. `join_executed:false`는 수집기 동작 범위이며 미가입 판정이 아닙니다. Worker Join 실행자·시각·소스·임시 자격증명 회수는 이번 자료로 확인할 수 없습니다.

**현재 AC 충족 증거는 2/20(AC13·14)**, PARTIAL5/NOT_VERIFIED12/BLOCKED1입니다. 후속 db01 .30 조회까지 확인해 AC13을 RUNTIME_PASS로 갱신했습니다. 이는 구현 진행률이 아닙니다. 새 자료가 firewalld disabled/inactive·HEP/GNP 적용·Pod/Service 실제 통신을 조회하지 않았으므로 AC02/03을 임의 완료하지 않습니다. [15:56 기준 AC 대조 이력](https://github.com/321Team/infra-kubernetes/blob/ea4aef3c960fd79377225f7f037bc39cd04df469/ops/icr-followup-20260918/AC_REVIEW.md). 최신 판정은 이 티켓의 현재 AC 절을 따릅니다. AC14에 “최종 보호 전환 이후에만 인정”을 추가하지 않는 정정도 유지합니다.

**현재 우리 후속:** LB backend3/3·장애복구와 IF-06B Receiver/TLS/Auth/Source 입력 연결입니다. IF-16은 edge/harbor/db 3/3의 기존 경로 및 .30 조회로 AC13을 충족했고, edge 비활성 잘못된 주소 프로필의 자동 연결 해제도 확인했습니다. 동일 경로 작업은 반복하지 않습니다. K8S/SEC 오너 이하영님은 가입 후 남은 K8S 검증과 기존 SEC-06 정책 잔여를 진행합니다. [담당 분리와 SEC-06 현재 소스 확인](https://github.com/321Team/infra-kubernetes/blob/ea4aef3c960fd79377225f7f037bc39cd04df469/ops/icr-followup-20260918/WORKER_HANDOFF.md).

6/6 선행 상태는 확보됐고 HEP/GNP·firewalld 보호 전환은 양쪽 담당이 같은 작업창에서 연결합니다. 현재 SEC-06의 전달 트래픽·LB .109 허용 누락 등 기존 코드 지적을 완료로 바꾸지 않습니다. 전체 ICR AC를 K8S 후속의 추가 선행조건으로 두지 않고 성공한 CP1 시험·CP Join·백업을 반복하지 않습니다. 고정90분은 원래 AC 조건이 아닙니다.

코드 외 실행·결과·최종 인수는 [중앙 권한 정책](https://github.com/321Team/fds-project-baseline/blob/b2e4612cf2e417b10e7f145c5b1e5f58dbe1b948/governance/REVIEW_AUTHORITY_POLICY.md)에 따라 담당 Lead가 판단합니다. 코드 병합과 증적 저장소 PR의 독립 검토는 별도 유지합니다. 이번 검토는 Runtime 변경·새 승인·티켓 종결을 수행하지 않았습니다.

[13:04 이전 관측](https://github.com/321Team/infra-kubernetes/blob/22673b0ba5ee188a514c5643bc3df8e7999a2d5a/ops/icr-followup-20260918/results/20260918T040403Z_zgby6ckp/README.md)과 기존 CP 실행 계약·증적은 이력으로 보존합니다.
<!-- icr-ac-followup-20260918:end -->

---

아래 내용은 해당 시점의 검토·준비 이력입니다. 최신 CP1 현황은 위 기록을 기준으로 합니다.

<!-- fds-icr-followup:2026-09-15:start -->
## 진행 이력 — 2026-09-17 (현재 판정은 상단 9/18 및 AC 절 참조)

**당시 위치:** 정본 v18·v19 승인 입력에 따른 진단 단순화와 운영 보완 준비를 유지한다. 최신 PR #11 HEAD `ed53205`는 배포 인수 양식의 오래된 생산자 pin·runbook·manifest를 수정했고 **61/61 STATIC/MOCK PASS**다. 실행 코드·방화벽 정책·원 영수증·상태 비교는 변경하지 않았다. [독립 리뷰](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5700011880)에서 9/17 00:25 KST `ed53205` 인수 양식·명세 증분을 댓글 승인했다. 현재 HEAD formal APPROVED·운영 실행 승인은 별개이며, Join 일정 확정은 아래 선행조건 해소 전 보류다. 후속 [Draft PR #13](https://github.com/321Team/infra-kubernetes/pull/13) `ac30186`에 원 영수증 인계 검사·읽기 전용 일괄 수집·public 유지 후보 생성을 구현했다(**109/109 STATIC/MOCK**, 별도 공식 함수 매치 18건). 후보는 고정 veth 목록이며 새 Pod/Join 지속 정책이 아니다. 실제 적용/회수·후속 연결·kernel 검증은 미완료다. PR #11 승인 소스와 새 리뷰 요청 보류를 유지한다. R5 격리 normal **6개 흐름·원복·disarm·unit 정리 완료**, R6 `1c9d17e` **286/286 STATIC/MOCK**는 보존하며 R6 실제 VM 검증은 미수행이다. 추가 범용 기능·VM 반복 시험은 보류한다. 실제 Calico는 최신 현장 증거 기준 **3/5 PASS·직접 Pod HTTP 2건 FAIL**이다. 운영 허용 범위·HOST/외부 경로 보존·유지 기간·회수 종료 상태·Positive/Negative/Regression·새 상태 영수증/소비자 구현은 미완료다. 기존 zone안과 새 /26·고정 veth 집합안은 미승인 후보이며 기존 제한 진단 승인을 승계하지 않는다. **CP1 인수·CP2/CP3 실제 변경/Join·AC 보류**. Worker 준비는 병행, **HEP/GNP Runtime은 6/6 Ready 후 별도 승인/실행창**이다. [v19 후보 수집](https://github.com/321Team/fds-project-baseline/blob/48b8d836e74a723ea145360f63456de0d4183f96/audit/v3.1.19/intake/icr-cni-simplification-20260916.md)은 준비 보완 기록이며 운영 정본은 v3.1.18이다. 아래 과거 기록은 당시 이력이다.

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
| Source | Baseline/Ticket Pack v3.1.18; GitHub #14; PR #2/#3/#4/#8 병합 기록; PR #9 b3f3374 승인·merge c08b798; CP1 최종 재적용·CP2 inspect·CNI 준비 및 p3dmjivl 실측 FAIL 증적. 원 정본 수집 이력: audit/v3.1.18/k8s-intake-20260910.json; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
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

- 현재 발행 Baseline v3.1.19의 설계·Interface와 아래 AC를 적용한다. 아래 9/15 이전 진행 문단과 하단 원문 보관은 당시 이력이며, 현재 실행 상태는 상단 9/18 및 현재 AC 절을 따른다.
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

**2026-09-23 재대조:** 핵심 요구사항 전체 범위 완료는 기존 3/11을 유지한다. HEP/GNP 적용·MON 배포 및 9100/10250 실패 보고를 부분 실적과 잔여에 반영했다. 이 집계는 전체 구축 공수의 진행률이 아니다.

- [x] firewalld 비활성화와 Calico named HEP/GNP 전환 설계를 D34/D35 기준으로 확정한다. **완료 — 설계 확정 범위. 실제 보호 전환 완료는 AC-02/03/18에서 별도로 판정**.
- [x] IF-06B와 IF-16의 정본 Interface 계약을 유지한다. **완료 — 계약 유지 범위. 실제 통신·인증·경로 검증과 drift 시정 완료를 뜻하지 않음**.
- [ ] Kubernetes 6개 Node의 변경 전 상태와 SHA-256 Evidence를 확보한다. **PARTIAL — 6대 방화벽·리스너 수집/무결성 및 Worker 3대 경로 확보. CP2/CP3 경로와 최초 변경 전 CP 경로 근거 연결은 미완료**. 현재 CP1 경로 조회로 과거 변경 전 증적을 대체하지 않는다. → AC-01.
- [ ] named HEP/`expectedIPs`와 Bootstrap Allow를 승인안대로 적용한다. **PARTIAL — 9/22 6대 firewalld 비활성·ens160 HEP 6개/GNP 6개 존재 보고 확보. actual expectedIPs·v4 적용본/승인본 일치 및 전체 보호 인수는 잔여**. → AC-02/03.
- [ ] 30080/9100/10250에 대해 승인 Source 허용과 비승인 Source 차단을 검증한다. **FAIL 항목 포함 — NodePort 적용/PR21 후보는 확보했으나 9100 1/3 UP·10250 6대 DOWN 보고로 복합 요구 미충족. 승인/비승인 전체 시험은 잔여**. → AC-04/05/06/07.
- [ ] Control Plane 관리 기능, Harbor Pull 및 Worker Route 회귀를 검증한다. **PARTIAL — AC08 9/21 관리 기능27/27 및 AC14 Worker route PASS 유지. 9/22 Harbor Pull·앱/MON Running 보고를 추가 반영하되 지정 Worker별 Pull/Pod 시작 증거 연결은 남음**. → AC-08/09/14.
- [ ] IF-06B Receiver/TLS/Auth/Payload Allowlist와 실제 Source/Return Path를 검증한다. **BLOCKED — 실제 Receiver·인증·Payload·허용/차단·양방향 경로 검증 및 인수 미완료**. → AC-11/12/15/16/17.
- [x] IF-16 edge/harbor/db Route Drift를 시정한다. **완료 — 세 호스트의 `10.250.10.0/24 via .58` Runtime 경로와 `.30` route-get의 올바른 NIC/source(.50/.54/.55) 확인**. → AC-13. edge 비활성 잘못된 주소 프로필의 자동 연결 해제도 확인. 재부팅·Forward/NAT·packet source 검증은 각 별도 AC로 추적한다.
- [ ] Reboot 지속성과 Rollback 재현성을 검증한다. **PARTIAL — CP1 제한 Runtime 6개 rollback·baseline 복구 재현 완료. 전체 보호/경로 변경의 rollback 및 최종 정책 reboot 지속성 미완료**. 백업 준비 중 재기동은 최종 정책 지속성 시험과 구분한다. → AC-18/19.
- [ ] Evidence Index·SHA256SUMS·비밀정보 검사를 완료한다. **PARTIAL — 제출본별 SHA 검증과 PR #9 마스킹 보완·시험·독립 승인/병합 완료. 전체 최종 Evidence Index·SHA256SUMS 및 비밀정보 검사 종결은 미완료**. → AC-01/20.
- [ ] 고정 Commit/Artifact에 대한 독립 리뷰와 Lead 최종 승인을 완료한다. **PARTIAL — 기존 병합·리뷰 이력과 PR15/16의 고정 코드 승인을 보존. CP1 최신 5/5·CP2/CP3 Runtime·실제 Join 및 [3CP/etcd3/3](https://github.com/321Team/infra-kubernetes/blob/5e9e09e7a1820c230bb5724ce05897c7689ef065/ops/cp-join-20260918/results/20260918T033022Z_16219c68779b3d13/k8s-control03_AFTER.json)은 제출 증적에서 확인했으나 전체 ICR 최종 인수는 미완료**. 과거 3/5 FAIL·CP2 변경 보류는 당시 이력이며 현재 차단으로 반복하지 않는다. 새 코드 변경 및 증적 저장소 PR의 독립 리뷰는 유지하고, 동일 코드 실행/결과에 불필요한 새 승인 회차를 추가하지 않는다.

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

**현재 직접 남은 후속:** Kubernetes 오너의 기존 Worker Join·자격증명 회수 기록 연결 및 남은 CoreDNS·cross-node·스토리지 검증, LB 오너의 backend3/3·장애/복구 검증, IF-16 완료 기록 연결, Monitoring의 실제 Source/Receiver/TLS/Auth와 연결한 IF-06B 시험. 완료한 CP1 5-flow·CP2/CP3 적용/Join은 재실행 선행조건으로 두지 않는다. 최종 HEP/GNP 보호 인계·Negative·Reboot·Rollback·증적 종결은 아래 AC로 추적한다.

---

### Acceptance Criteria — 2026-09-23 전수 대조 반영

현재 발행 정본은 [docs-v3.1.20](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.20)이다. 기존 ICR-AC-01~20 조건과 과거 원 실행일을 유지하고 [전수 대조](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5794357232)에서 9/22~23 후속 증거를 연결했다. 정본 발행과 Runtime 인수는 별도다.

현재 Runtime 증거 충족 **3/20(AC08/13/14)**, PARTIAL **8건(01/02/03/04/09/10/19/20)**, FAIL **2건(05/06, 담당자 Runtime 보고 기준)**, NOT_VERIFIED **6건(07/11/15/16/17/18)**, BLOCKED **1건(12)**. 신규 PASS는 없고 전체 구축 공수의 진행률이 아니다. Join·6대 Ready·MON 배포 등 실제 구현 완료는 별도 실적으로 유지한다.

- [ ] `ICR-AC-01` — 6개 Node 변경 전 firewall/listener/route 설정과 SHA Evidence를 확보한다. 현재: **PARTIAL** — 기존 6대 방화벽·리스너와 Worker 3대 route 증거 재사용. 확인한 CP2/3 resume·Join 증적에는 route 수집이 없어 최초 변경 전 CP route 원본 연결이 남음. 새 조회를 과거 증거로 대체하지 않음.
- [ ] `ICR-AC-02` — firewalld가 disabled/inactive이고 Calico Pod/Node 통신이 정상이다. 현재: **PARTIAL** — 9/22 firewalld 6대 disabled/inactive·HEP/GNP 존재와 Gate2 네트워크 9/9 보고 확보. 전체 Calico Pod/Node 통신 및 현재 보호 인수는 남음. 과거 “firewalld 유지/전환 미실시”는 현재 상태가 아님.
- [ ] `ICR-AC-03` — named HEP/`expectedIPs`/Bootstrap Allow가 승인안과 일치한다. 현재: **PARTIAL** — ens160 HEP 6개·GNP 6개 존재와 적용 보고 확보. actual expectedIPs·v4 적용 정책과 승인 manifest의 대응 및 Bootstrap Allow 정합성 인수는 남음.
- [ ] `ICR-AC-04` — `.50 → Worker:30080`은 허용되고 비승인 Source는 차단된다. 현재: **PARTIAL** — NodePort 적용 보고 및 PR21의 worker selector/order 50 후보 확인. .50 허용/비승인 Source 차단 실측과 독립 인수는 남음.
- [ ] `ICR-AC-05` — Prometheus에서 Worker node-exporter 9100 Target이 `UP`이다. 현재: **FAIL — 담당자 Runtime 보고 기준**. 9/22~23 node-exporter 1/3 UP·2대 timeout으로 3대 UP 조건 미충족. 이번 검수에서 독립 재현하거나 GNP 원인을 확정한 것은 아님.
- [ ] `ICR-AC-06` — Prometheus에서 Worker kubelet 10250을 CA+SA로 인증한다. 현재: **FAIL — 담당자 Runtime 보고 기준**. kubelet/cadvisor 6대 DOWN; worker03 IP SAN 오류와 다른 5대 timeout. Worker 3대 CA+SA 인증 조건 미충족, 네트워크와 serving 인증서 조치를 구분.
- [ ] `ICR-AC-07` — 비승인 Workload의 9100/10250 접근이 차단된다. 현재: **NOT_VERIFIED** — 비승인 Workload의 9100/10250 차단 시험 필요.
- [x] `ICR-AC-08` — Control Plane의 logs/exec/port-forward가 정상이다. 현재: **RUNTIME_PASS** — 2026-09-21 14:01:47–52 KST CP1에서 직접 API3개×etcd Pod3개의 고유9조합을 검증하여 logs9/9·exec9/9·port-forward+CA/클라이언트 인증 HTTPS health9/9, 총27/27 성공. [원본7개·SHA256·검증](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5755742235). 9/21 해당 구성에서 조건을 충족했으며 이후 HEP/GNP 전환의 영향 회귀·전체 ICR 인수·재부팅 지속성은 별도다.
- [ ] `ICR-AC-09` — Worker에서 Harbor `.54:443` Pull과 Pod 시작이 성공한다. 현재: **PARTIAL** — 9/22 Harbor Pull·앱/MON Pod Running 보고 확보. 지정 Worker별 Harbor Pull 및 실제 Pod 시작 증거 연결은 남음. 승인 digest/이미지 보안 인수는 MON/HBR에서 별도 추적.
- [ ] `ICR-AC-10` — Cockpit 9090이 노출되지 않는다. 현재: **PARTIAL** — 기존 Worker 3대 masked/inactive·리스너 부재 증거와 9/22 Cockpit 미청취 6/6 보고 재사용. 전체 범위 비노출 인수와 정책 정합성은 남음.
- [ ] `ICR-AC-11` — monitor01에서 Cluster Workload로 신규 Ingress를 시작할 수 없다. 현재: **NOT_VERIFIED** — monitor01의 Cluster Workload 신규 Ingress 차단 증거 필요.
- [ ] `ICR-AC-12` — IF-06B Remote Write의 TLS/Auth/Payload Allowlist가 충족되고 비승인 Egress가 차단된다. 현재: **BLOCKED** — in-cluster sender 실제 기동으로 예전 미배포 의존성은 해소. monitor01 Receiver/TLS/Auth/Payload allowlist·비승인 Egress·실제 Source/Return Path 인수는 미완료.
- [x] `ICR-AC-13` — edge/harbor/db에 `10.250.10.0/24 via .58`가 적용되고 `.30` route-get이 통과한다. 현재: **RUNTIME_PASS — 3/3 호스트 조건 충족**. 2026-09-18 사용자 제공 edge01·harbor01의 kernel 경로 및 `.30 via .58 dev ens160 src .50/.54`, db01의 기존 kernel 경로 및 후속 `.30 via .58 dev ens192 src .55`를 확인했다. 근거·원본 파일 SHA256은 상단 최종 현장 확인에 기록했다. 정상 기존 경로의 관측으로 조건을 충족했으며 새 적용 영수증을 요구하지 않는다. edge 비활성 잘못된 주소 프로필의 autoconnect=no도 후속 조회로 확인했다. 재부팅은 AC18, Forward/NAT는 AC15, 실제 packet source는 AC17의 별도 조건이다.
- [x] `ICR-AC-14` — Worker 3대에서 동일 경로 조회 회귀가 통과한다. 현재: **RUNTIME_PASS** — 2026-09-18 13:04 KST .30 route-get3/3 rc0, source .105/.107/.108 및 gateway .58 일치. [원본·검증](https://github.com/321Team/infra-kubernetes/blob/22673b0ba5ee188a514c5643bc3df8e7999a2d5a/ops/icr-followup-20260918/results/20260918T040403Z_zgby6ckp/README.md). 최종 보호 전환 이후에만 인정한다는 추가 조건은 원문에 없어 제거. Lead의 전체 ICR 인수 및 이후 관련 변경의 회귀는 별도. [15:56 후속 원본](https://github.com/321Team/infra-kubernetes/blob/ea4aef3c960fd79377225f7f037bc39cd04df469/ops/icr-followup-20260918/results/20260918T065614Z_zzi65aal/README.md)에서도 Worker3의 동일 source/gateway·route-get rc0을 재확인했으며 PASS를 유지한다.
- [ ] `ICR-AC-15` — mgmt-gw IP Forward/Zone/Policy/NAT가 승인안과 일치하고 내부 SNAT가 없다. 현재: **NOT_VERIFIED** — mgmt-gw Forward/Zone/Policy/NAT와 내부 Source 보존 인수 필요.
- [ ] `ICR-AC-16` — monitor01 `.30:443` Receiver/Protocol/TLS/Auth가 정본과 일치한다. 현재: **NOT_VERIFIED** — PKI/구성 후보 병합은 완료했으나 9/22 Lead 보고에서 monitor01 receiver/TLS/IF-06B 미착수. 실제 Receiver/Protocol/TLS/Auth 인수는 남음.
- [ ] `ICR-AC-17` — 패킷 관찰의 실제 Source와 양방향 Return Path가 정본과 일치한다. 현재: **NOT_VERIFIED** — sender가 기동돼 실제 Pod 식별·Source 조회는 시작 가능. monitor01 수신 패킷 Source와 양방향 Return Path 실측은 미확보.
- [ ] `ICR-AC-18` — Reboot 후 정책이 유지되고 재시험이 통과한다. 현재: **NOT_VERIFIED** — 최종 보호·경로 정책의 Reboot 지속성 미검증. 현재 CP Runtime 유지나 백업 준비 중 재기동은 대체 증거가 아님.
- [ ] `ICR-AC-19` — Rollback을 재현할 수 있다. 현재: **PARTIAL** — 기존 CP1 실제 Runtime rollback·baseline 복구 증거 재사용. 최신 Join은 성공하여 rollback 호출 없음. 전체 ICR 변경의 복구 재현성은 남음. 90분 제한은 이 AC의 요구가 아님.
- [ ] `ICR-AC-20` — Evidence에 평문 비밀정보가 없다. 현재: **PARTIAL** — 기존 제출본별 SHA·마스킹·비밀정보 검사 결과 유지. 새 Gate2 원본은 서버 보관 경로/해시만 문서에 있어 이번 검수에서 원문 미수신. 전체 최종 Evidence 종결은 남음.

---

### 검증 및 증적

- 설계·정본 매핑은 승인 범위를 유지하고 현행 v3.1.19의 전체 ICR 목표와 AC 문구를 적용한다. 아래 9/15 CNI/코드 기록은 이력이다. 최신 5/5·CP2/CP3 Runtime·3CP Join 증거 및 남은 인수는 상단과 현재 AC 절을 따른다.
- CP/Worker 변경 전 수집, CP1 최초 적용·Positive/제한된 Negative·기능·rollback·재적용, CP2 inspect는 위 완료 체크와 원 실행/검토 링크로 추적한다.
- 최신 코드: PR #2·#3·#4·#8·#9 병합 완료. PR #9 승인 HEAD `b3f3374`, merge `c08b798`; 새 HEAD 정식 APPROVED 및 Must-fix 해소 확인.
- CNI 개정 키트의 로컬/모의시험 14 PASS와 실서버 `p3dmjivl` 시험 **3/5 PASS·전체 FAIL**을 구분한다. 임시 자원 정리·전후 기본 상태 동일은 확인됐으나 CP1 최종 인수는 보류한다. [실측 검토](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5673301524). 재첨부 `v7nd98wj.tar(1).gz`는 원본과 같은 준비 자료로 새 실행에 산입하지 않는다.
- IF-06B는 **BLOCKED**, IF-16 AC13은 **RUNTIME_PASS — edge/harbor/db 경로·.30 조회 3/3 확인**. 전체 Evidence Index·비밀정보 검사·보호 인수는 미완료.


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
- 현재 후속: 성공한6/6 Ready와 Runtime을 유지한 채 기존 Worker Join·임시 인증정보 회수 기록을 연결하고 CoreDNS/cross-node/스토리지 및 LB Stage B를 진행한다. 이전 CP1 인수 대기를 새 선행조건으로 부과하지 않는다. HEP/GNP의6/6 Ready 선행 상태는 확보됐으며, 잔여 정책 수정과 최종 보호 인계는 기존 Lead 조건을 따른다.
- 최종 ICR 인수에는 전체 AC, Evidence Index·SHA256SUMS·비밀정보 검사, 독립 리뷰 및 Lead 승인이 필요하다. 완료한 동일 범위의 모의시험·supplement를 이유 없이 재수집하지 않는다.


---

### Completion Record

- 확인 기준: **2026-09-23 GitHub·제출 증적 전수 대조**. 기존 Runtime 원 실행일(9/18·9/21)과 9/22~23 담당자 보고를 구분하며 이번 실서버 신규 실행은 없음.
- 원래 핵심 요구사항 전체 범위 완료 **3/11 유지**. AC는 **3 PASS / 8 PARTIAL / 2 FAIL(보고 기준) / 6 NOT_VERIFIED / 1 BLOCKED**. 전체 구축 공수의 진행률이 아니며 상세 증거/잔여는 현재 AC 절 참조.
- 선행 작업 완료 체크: **9/15 당시13건**. 이 항목은 전체 공수 가중 진행률이나 AC 수에 합산하지 않는다.
- CP1 기존 적용/복구 및 최신 5/5·HOST/외부 회귀, CP2/CP3 Runtime, 실제 Join·3CP Ready/etcd3/3: **증적 검토 완료**. CP1 Runtime 유지 인계 및 기존 timer 중지 확인. 15:56 후속 원본에서 Worker 포함6/6 Ready는 확인됐으며, Lead 결과 인수·ICR 최종 AC는 미완료.
- IF-06B: **BLOCKED**, IF-16 AC13: **RUNTIME_PASS — edge/harbor/db 3/3 조건 충족, edge 비활성 잘못된 주소 프로필 자동 연결 해제 확인**.
- 코드 PR #2·#3·#4·#8·#9: **병합 완료**. PR #9의 마스킹 수정 요청은 독립 재검증으로 해소 확인.
- AC14 Worker3대 경로 조회: **13:04 PASS 및 15:56 후속 PASS 유지**. [15:56 원본](https://github.com/321Team/infra-kubernetes/blob/ea4aef3c960fd79377225f7f037bc39cd04df469/ops/icr-followup-20260918/results/20260918T065614Z_zzi65aal/README.md)에서6/6 Ready·Calico-node6/controller1 Ready·Worker kubelet/containerd active 및 CP1→LB 인증 성공 확인. Lead의 전체 ICR 인수·Lead 최종 승인: **미완료**.
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
