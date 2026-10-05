# 이권욱 작업 점검 및 권장 실행 순서 — 2026-10-05

AI(Codex) 지원으로 작성한 작업용 초안이다. AC 인수, Runtime 승인, 정본 발행, 일정 확정 또는 티켓 종결을 대신하지 않는다.

## 조회 범위와 기준

- 조회 기준: 2026-10-05 23:47 KST. GitHub org 321Team, assignee GWONUK의 issue 전체 58건(열림 29 / 닫힘 29), 검색 incomplete_results=false, 1페이지 100개로 전체 회수.
- Phase 1 직접 배정 열린 항목 13건. 사용자의 CI/CD 후순위 지시에 따라 3건을 뒤로 미루고 10건을 우선 처리한다.
- 나머지 열린 16건은 Phase 2 및 프로젝트 종료 항목으로 목록에 보존한다. Notion·Projects 비공개 속성 또는 배정되지 않은 다른 시스템 작업까지 전수 확인한 것은 아니다.
- 기준 문서 CURRENT.md의 v3.1.21 및 기준 저장소 main 8e870c4c551506afef816ef19b94b381994c6386을 확인했다.
- 이슈 본문과 최신 댓글이 다른 경우 최신 증적을 함께 제시한다. 본문·AC·상태·담당자·일정을 이 문서로 변경하지 않는다.

## 실행 순서

| 순서 | 대상 | 현재 확인 | 다음 행동 / 완료 조건 |
|---|---|---|---|
| 0 | baseline #10의 담당자 의사결정 | 10/6 11:30–13:30 KST 중간 승인 대응 가능 시간 문의 있음. 사용자 응답 미확인 | 아래 CP 복구 승인 체크리스트 준비. 일정 가능 여부는 사용자 확인 후만 회신 |
| 1 | infra-ansible #9 | PR #70/#71 병합. 새 wrapper Runtime와 운영 엔진 전환 미실행 | ansible01 후보 엔진 4개 CLI 읽기 전용 확인 → 병합 helper 선택 동작 검증 → 승인된 범위의 canary. 운영 전환/실제 키 복구와 구분 |
| 2 | infra-ansible #62 → baseline #13 | AC-04 잔여. 문서 PR #67은 승인됐지만 Draft/명시적 HOLD | 임시 .50/.102 제거 선행조건, 대체 UI 접근안의 승인 여부, negative/persistence 증적을 대조. 방화벽 변경·임시 허용 제거는 승인된 작업창에서만 |
| 3 | baseline #14 | OID-02 원본 및 배포·재반입 경로 잔여. 담당 hayeounglee, 10/7 예정 | 원본 3종 및 이미지별 플랫폼·노드 배포 증적 확보 여부 확인. cache만으로 원본 증명 금지. Import/drain/egress 실행 승인으로 확대 금지 |
| 4 | evidence #4 | FUP-09 해결, FUP-04/05/06/07 원본 참조 잔여 | 04: 당시 Windows/VMware/관리 VM gateway 원본. 05: 당시 reviewer/approver·시각·범위. 06/07: 개별 회신 시각·WBS 실제 화면. 신규 시험으로 과거 증적 대체 금지 |
| 5 | baseline #18 | G1 종료 조건 판단 미완료 | 완료된 LB/DNS/ANS 등의 증적 재사용, K8S·Harbor·ICR 등 미완료 의존성별 수용/잔여 분리 |
| 6 | baseline #24 | 문서 Freeze 잔여 | 최신 코드/Runtime/증적 대응표와 누락 출처 정리. 정본 발행과 작업 초안 구분 |
| 7 | baseline #29 | G3 Review Ready 미확정 | #18/#24 및 다른 Lead의 잔여 AC·명시적 예외·수신 책임 점검 |
| 8 | baseline #30, #31 | Phase 1 Review / Close Execution 및 Review milestone | Review 자료와 실제 판정 기록 준비. 10/6 일정 도래만으로 완료 처리 금지 |
| 9 | baseline #32 | Phase 1 Close HOLD | 모든 필수 조건 또는 승인된 예외·이월의 수신자/AC/증적·위험 결정 확인 뒤 별도 종결 |
| 마지막 | baseline #16, infra-cicd #11, infra-ansible #61 | 사용자 지시로 후순위 | 현재 증적 보존. 우선 작업 후 남은 Push/Deploy/러너 운영 절차 재개 |

Ansible #9와 Harbor #62는 Phase 1 연관 후속 작업이다. 기존에 닫힌 baseline ANS 항목을 다시 여는 근거 또는 자동적인 Phase 1 Close 차단으로 취급하지 않는다. 게이트 적용은 해당 AC와 명시적 결정에 따른다.

## 10/6 CP 복구: 의사결정 준비

근거: [기존 사전 승인](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5979476603), [중간 승인 가능 시간 문의](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5995948665), [MON 비중첩 확인](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5996275653).

- 기존 Runtime 사전 승인은 유지되며 새 설계 승인을 요구하는 단계가 아니다. PROTECTION_RESTORED_REVIEWED 중간 receipt 판단은 실제 증적 도착 후 별도 처리한다.
- 제안 작업창은 10/6 11:30–13:30 KST. SEC AC-04/05 실제 종료·정리 전이면 T0를 늦춘다. 사용자 참석 가능 여부를 대신 확정하지 않는다.
- 대상 control02(10.1.93.103), 비리더 조건. 직전 etcd 3/3·노드 6/6·LB/local readyz·CP2 Ready·각 CP etcd localhost·boot/restart/HEP/GNP/Felix·MON 23/23 및 up==0 없음·checkpoint2 경로/해시/호스트·working state/정본 SHA를 확인한다.
- leader 변경, 필수 fresh gate 불일치 또는 receipt 부족 시 STOP. firewalld 최대 60분 조건과 전체 T0+120 제안을 혼동하지 않는다.
- firewall 복구 및 보호 시험 → receipt 검토·사용자 중간 판단 → 승인 절차에 따른 node rollback → Calico 복구 → firewalld OFF 순서.
- 과거 PACKAGE_SHA256SUMS 불일치는 PR #56/#58 병합으로 수정됨. 이미 해결된 코드에 중복 수정하지 않는다. 실제 서버 작업 파일은 별도 확인한다.
- 실행 기준 3파일 SHA256:
  - RUNBOOK_FINAL.md: b5388dc52071952608e6bcd642cda4d5a3d6d4c7d6ee8e820e8d4330b32c25c3
  - cluster-change.py: e955a6f981dbcdc3acac1e97dcecca498f4441e23e6c7ae64bbfb4788f2df162
  - node-evidence.py: 8ce5854476ea7f4e85dafd38ec979392762a3d92e3ed1ff44e58e50119f79e9f

## Ansible의 다음 확인 범위

- 근거: [#9 최신 후속 정리](https://github.com/321Team/infra-ansible/issues/9#issuecomment-5994763415).
- PR #71 merge 1b09980ac3569cadbd26522a4a31d0c0e89191b1, review HEAD d40589e06149a2da8738630ce5da058760fb0b99. PR #70 merge edef9523dca35a9a799fa715718bd915849f7bd2.
- 후보 경로: /home/server01_ansible/ansible-candidate.8oCqVUwx/result/runtime/venv-2.21.3/bin
- 실제 ansible01에서 4 CLI의 --version 결과·종료 코드·경로를 먼저 확인한다. 이는 PRECHECK이며 운영 전환 PASS가 아니다.
- 에이전트에서 기존 SSH trust로 접속 시 호스트 키 미등록으로 차단됨. StrictHostKeyChecking을 낮추거나 임의 신뢰하지 않았다.
- 실제 키 복구는 미실행. backup과 current가 동일한 경우 인위적인 장애나 동일 바이트 덮어쓰기로 복구 성공을 만들지 않는다. worker01 제외.
- 기존 worker02 changed=0 두 차례 및 SSH PASS를 새로운 wrapper Runtime로 잘못 재표기하지 않는다.

## 주요 의존성 및 완료 판단의 한계

- [Harbor 최신 조건](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5996597464): .50 정리는 #19 이관/robot 정리 조건, .102 정리는 IF09·push/scan/admin 완료 및 제거 기록/동일 L2 negative 조건. 대체 UI 경로는 제안이며 승인된 것으로 간주하지 않는다.
- [ICR 잔여](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5994756924): 일부 노드 cache만으로 전체 공급 증적을 대체하지 않는다.
- DB #11은 특정 범위 NOT MET / RISK ACCEPTED이며 후속 #47 및 10/20 재점검 조건이 있다. 전체 보안 예외로 확대하지 않는다.
- SEC #19의 PSA/RBAC 증적 잔여, MON #17의 미확인 항목, APP #15/E2E #20 최종 회귀, DR #21 문서/기존 dump 이관, HA #22 Exit 완료를 각 Lead 책임으로 연결한다. 사용자에게 이들 실행 책임을 임의 재배정하지 않는다.
- LB #9 등 이미 종결된 항목은 기존 인수 근거를 재사용한다. 새로운 위험이나 변경이 없는 동일 시험 반복은 권장하지 않는다.
- CI/CD 최신 Test·Build·Scan과 evidence 수집 PASS는 Push/Deploy/Delivery Gate PASS가 아니다. PR #52 초안을 보존하며 이전 만료 승인을 재사용하지 않는다.

## 열린 PR 확인 범위

작성자 GWONUK의 열린 PR 5건: infra-cicd #52(후순위), infra-ansible #67(명시적 Draft/HOLD), baseline #137·infra-terraform #3·infra-rosa #2(Phase 2). review-requested GWONUK 열린 PR 검색 결과는 0건이었다. 문서 작성 뒤 새 PR은 이 조회 수에 포함되지 않는다.

## 직접 배정 issue 전체 목록

아래 상태와 updated_at은 조회 당시 스냅샷이다. 권장 순서는 위 표만 적용한다.

| 저장소 / 번호 | 상태 | 제목 | updated_at (UTC) |
|---|---|---|---|
| [infra-ansible #62](https://github.com/321Team/infra-ansible/issues/62) | open | [P1-HBR-01][AC-04] harbor01 443 Source allowlist remediation | 2026-10-04T06:49:17Z |
| [fds-project-baseline #120](https://github.com/321Team/fds-project-baseline/issues/120) | open | [DEC-P2-GITOPS-01] OpenShift GitOps (Argo CD) 도입 범위 결정 | 2026-10-04T06:02:51Z |
| [infra-ansible #61](https://github.com/321Team/infra-ansible/issues/61) | open | 자체 러너 CI 운영 절차 보완 (PR #60 ephemeral 러너 공급·감시·런북) | 2026-10-04T06:56:21Z |
| [fds-project-baseline #109](https://github.com/321Team/fds-project-baseline/issues/109) | closed | [DEC-P1-MON-02] Alertmanager Discord 제한 Egress·발송 범위·Secret Lifecycle 결정 | 2026-10-04T06:02:40Z |
| [infra-dns #8](https://github.com/321Team/infra-dns/issues/8) | closed | [P1-DNS-01 후속] 수집기 모의 시험 코드 저장소 편입 (리뷰 비차단 의견) | 2026-09-27T13:19:30Z |
| [infra-dns #7](https://github.com/321Team/infra-dns/issues/7) | closed | [P1-DNS-01 후속] 방화벽 재기동 지속성, dns service 정의, UDP/TCP 53 실제 패킷 시험 | 2026-09-30T12:01:48Z |
| [infra-dns #6](https://github.com/321Team/infra-dns/issues/6) | closed | [P1-DNS-01 후속] 원 named.conf/include 파일 구조와 TSIG 키 참조 구조 확보 | 2026-09-28T05:17:48Z |
| [infra-dns #5](https://github.com/321Team/infra-dns/issues/5) | closed | [P1-DNS-01 후속] Zone 운영 반영 Runbook과 저장소-서버 drift 확인 | 2026-09-27T13:11:51Z |
| [infra-kubernetes #23](https://github.com/321Team/infra-kubernetes/issues/23) | closed | [edge01 마이그레이션] Worker NodePort 30080 외부노출 — P1-SEC-01 승인 전 보류 (완료 처리 불가) | 2026-09-27T09:25:59Z |
| [infra-ansible #40](https://github.com/321Team/infra-ansible/issues/40) | closed | [NTP 후속] kube-proxy/Calico OUTPUT predecessor drift 재검토 (6/6 호스트) | 2026-09-22T02:21:22Z |
| [infra-ansible #33](https://github.com/321Team/infra-ansible/issues/33) | closed | [NTP 후속] kernel topology STOP receipt에 기대값·실제값 차이 보존 | 2026-09-21T10:11:41Z |
| [infra-cicd #11](https://github.com/321Team/infra-cicd/issues/11) | open | P1-CICD-01: 승인 앱 인계와 Test·Build·Scan·Push·Deploy 연결 | 2026-10-05T13:50:57Z |
| [infra-cicd #8](https://github.com/321Team/infra-cicd/issues/8) | closed | P1-CICD-01: Trivy 바이너리 자동 갱신 경로와 운영 방식 확인 | 2026-09-23T20:02:03Z |
| [fds-project-baseline #78](https://github.com/321Team/fds-project-baseline/issues/78) | closed | [DEC-P1-EGRESS-01] Alertmanager 전용 프록시 배치·예약 IP 사용 결정 | 2026-10-04T06:02:33Z |
| [fds-project-baseline #67](https://github.com/321Team/fds-project-baseline/issues/67) | closed | [P1-NET-01] Bridged Multi-MAC Smoke Test / Source Preservation | 2026-10-04T06:02:22Z |
| [fds-project-baseline #66](https://github.com/321Team/fds-project-baseline/issues/66) | closed | [P1-LNX-01] CentOS Stream 10 Linux / Network Baseline | 2026-10-04T06:02:19Z |
| [fds-project-baseline #65](https://github.com/321Team/fds-project-baseline/issues/65) | closed | [P1-ANS-01] Ansible Inventory / OS-Node Bootstrap — Closed Update | 2026-10-04T06:02:15Z |
| [fds-project-baseline #64](https://github.com/321Team/fds-project-baseline/issues/64) | closed | [DEC-P1-TLS-01] Harbor / Edge TLS Trust Decision | 2026-10-04T06:02:10Z |
| [fds-project-baseline #63](https://github.com/321Team/fds-project-baseline/issues/63) | closed | [DEC-P1-MON-01] Kubernetes-Integrated Hybrid Monitoring Architecture | 2026-10-04T06:02:06Z |
| [fds-project-baseline #62](https://github.com/321Team/fds-project-baseline/issues/62) | closed | [DEC-P1-ENTRY-01] Edge Service Exposure Decision | 2026-10-04T06:02:02Z |
| [fds-project-baseline #61](https://github.com/321Team/fds-project-baseline/issues/61) | closed | [D-WBS-01] WBS / Backlog / Interface Management Freeze | 2026-10-04T06:01:59Z |
| [fds-project-baseline #60](https://github.com/321Team/fds-project-baseline/issues/60) | closed | [D-NET-01] Physical / Management Network Design Freeze | 2026-10-04T06:01:55Z |
| [fds-project-baseline #59](https://github.com/321Team/fds-project-baseline/issues/59) | closed | [D-ARC-01] Phase 1 Logical / Physical Architecture Design Freeze | 2026-10-04T06:01:35Z |
| [fds-project-baseline #58](https://github.com/321Team/fds-project-baseline/issues/58) | closed | [CR-P1-ANS-01-01] Ansible Kubernetes Node DNS Resolver 변경 | 2026-10-04T06:01:30Z |
| [fds-project-baseline #57](https://github.com/321Team/fds-project-baseline/issues/57) | open | [MS-PROJECT-CLOSE-01] Project Close | 2026-10-04T06:01:26Z |
| [fds-project-baseline #56](https://github.com/321Team/fds-project-baseline/issues/56) | open | [MS-P2-REVIEW-01] Phase 2 Review | 2026-10-04T06:01:23Z |
| [fds-project-baseline #55](https://github.com/321Team/fds-project-baseline/issues/55) | open | [P2-REV-01] Phase 2 Review / Project Close Execution | 2026-10-04T06:01:19Z |
| [fds-project-baseline #54](https://github.com/321Team/fds-project-baseline/issues/54) | open | [MS-DELIVERABLE-FREEZE-01] Deliverable Freeze | 2026-10-04T06:01:15Z |
| [fds-project-baseline #53](https://github.com/321Team/fds-project-baseline/issues/53) | open | [MS-G6-01] G6 Hybrid Integration Ready | 2026-10-04T06:01:12Z |
| [fds-project-baseline #52](https://github.com/321Team/fds-project-baseline/issues/52) | open | [DEC-CAL-P2-01] Phase 2 Review Schedule Decision | 2026-10-04T06:01:08Z |
| [fds-project-baseline #49](https://github.com/321Team/fds-project-baseline/issues/49) | open | [P2-DOC-01] Cloud / Hybrid Deliverable Freeze | 2026-10-04T06:00:58Z |
| [fds-project-baseline #48](https://github.com/321Team/fds-project-baseline/issues/48) | open | [P2-DNS-01] Hybrid DNS Implementation Conditional | 2026-10-04T06:00:54Z |
| [fds-project-baseline #46](https://github.com/321Team/fds-project-baseline/issues/46) | open | [P2-CICD-01] Runner to ROSA Delivery | 2026-10-04T06:00:46Z |
| [fds-project-baseline #42](https://github.com/321Team/fds-project-baseline/issues/42) | open | [DEC-P2-REG-01] ROSA Image Registry Source Decision | 2026-10-04T06:40:09Z |
| [fds-project-baseline #40](https://github.com/321Team/fds-project-baseline/issues/40) | open | [DEC-P2-DNS-01] Hybrid DNS Scope Decision | 2026-10-04T10:08:44Z |
| [fds-project-baseline #39](https://github.com/321Team/fds-project-baseline/issues/39) | open | [MS-G4-01] G4 Cloud / VPN Ready | 2026-10-04T06:00:03Z |
| [fds-project-baseline #36](https://github.com/321Team/fds-project-baseline/issues/36) | open | [P2-OCI-01] OCI Relay Go / No-Go | 2026-10-04T05:59:52Z |
| [fds-project-baseline #34](https://github.com/321Team/fds-project-baseline/issues/34) | open | [P2-ARC-01] Hybrid / OCI / AWS / ROSA Architecture Freeze | 2026-10-04T05:59:45Z |
| [fds-project-baseline #33](https://github.com/321Team/fds-project-baseline/issues/33) | open | [MS-P2-START-01] Phase 2 Start | 2026-10-04T05:59:41Z |
| [fds-project-baseline #32](https://github.com/321Team/fds-project-baseline/issues/32) | open | [MS-P1-CLOSE-01] Phase 1 Close | 2026-10-04T05:59:38Z |
| [fds-project-baseline #31](https://github.com/321Team/fds-project-baseline/issues/31) | open | [MS-P1-REVIEW-01] Phase 1 Review | 2026-10-04T05:59:34Z |
| [fds-project-baseline #30](https://github.com/321Team/fds-project-baseline/issues/30) | open | [P1-REV-01] Phase 1 Review / Close Execution | 2026-10-05T12:49:28Z |
| [fds-project-baseline #29](https://github.com/321Team/fds-project-baseline/issues/29) | open | [MS-G3-01] G3 Review Ready | 2026-10-04T05:59:27Z |
| [fds-project-baseline #28](https://github.com/321Team/fds-project-baseline/issues/28) | closed | [DEC-CAL-P1-01] Phase 1 Weekend Review Decision | 2026-10-04T05:59:23Z |
| [fds-project-baseline #24](https://github.com/321Team/fds-project-baseline/issues/24) | open | [P1-DOC-01] Architecture / Test / Runbook Freeze | 2026-10-05T12:50:00Z |
| [fds-project-baseline #18](https://github.com/321Team/fds-project-baseline/issues/18) | open | [MS-G1-01] G1 Infrastructure Ready | 2026-10-04T05:58:22Z |
| [fds-project-baseline #16](https://github.com/321Team/fds-project-baseline/issues/16) | open | [P1-CICD-01] GitHub Actions / Self-hosted Runner Delivery | 2026-10-05T13:43:31Z |
| [fds-project-baseline #14](https://github.com/321Team/fds-project-baseline/issues/14) | open | [ICR-D-NET-01-01] Kubernetes Node Host Firewall / Monitoring Route | 2026-10-05T12:48:04Z |
| [fds-project-baseline #12](https://github.com/321Team/fds-project-baseline/issues/12) | closed | [P1-DNS-01] Internal DNS Primary/Secondary | 2026-10-04T05:58:00Z |
| [fds-project-baseline #9](https://github.com/321Team/fds-project-baseline/issues/9) | closed | [P1-LB-01] Kubernetes API Load Balancer | 2026-10-05T12:47:25Z |
| [fds-project-baseline #8](https://github.com/321Team/fds-project-baseline/issues/8) | closed | [MS-G0-01] G0 Design Freeze | 2026-10-04T05:57:42Z |
| [fds-project-evidence #4](https://github.com/321Team/fds-project-evidence/issues/4) | open | [증적 후속] FUP-04/05/06/07 잔여 참조 및 FUP-09 조건부 인수 반영 | 2026-10-01T06:48:54Z |
| [infra-ansible #10](https://github.com/321Team/infra-ansible/issues/10) | closed | [PR4 운영 적용] 승인 main SSH 수정의 6대 순차 적용·멱등성·신규 SSH 검증 | 2026-09-14T15:18:27Z |
| [infra-ansible #9](https://github.com/321Team/infra-ansible/issues/9) | open | [P1-ANS-01 연관] ansible-core 2.16.19 → 2.21.3 운영 전환 영향 검토·검증 | 2026-10-05T12:48:29Z |
| [infra-ansible #8](https://github.com/321Team/infra-ansible/issues/8) | closed | [PR4 후속] 검증 키트의 완전한 재현 가능한 배포 구성 | 2026-09-15T00:54:58Z |
| [infra-ansible #7](https://github.com/321Team/infra-ansible/issues/7) | closed | [PR4 후속] 서버 검증 결과 구조화 및 누락·실패 판정 강화 | 2026-09-15T00:54:03Z |
| [infra-ansible #6](https://github.com/321Team/infra-ansible/issues/6) | closed | [PR4 후속] SSH 회귀 시험의 Ansible 내부 API 의존 제거 | 2026-09-15T00:53:56Z |
| [infra-ansible #5](https://github.com/321Team/infra-ansible/issues/5) | closed | [P1-CICD-01 연관] infra-ansible CI 회귀 시험과 실패 차단 연동 | 2026-09-26T09:40:59Z |
