# CR-P1-MON-01-01 — Alertmanager Egress 프록시 서버 구성

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/74
Updated at: 2026-09-26T05:54:51Z
Source body SHA256: `55c5fa61248578203803e8494b02b95acbd2e60d72194e702f0fcb859f42d9c7`
GitHub: closed / completed
Current disposition: Source lifecycle/AC retained; no new acceptance by this publication.

| Property | Current source value |
|---|---|
| Record ID | CR-P1-MON-01-01 |
| Phase | Phase 1 |
| Category | Monitoring / Alerting Egress Change Control |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-11 |
| End | 2026-10-06 |
| Calendar Days | TBD — Start/End 확정 후 산정 |
| Working Days | TBD — 계획일·가용일 확정 후 산정, 교육장 주말 작업 0 |
| Lead | 이하영 |
| Support | 이재환 |
| Exit Criteria | discord.com 아웃바운드 확인, 프록시 전용 VM 확정, Squid/Nginx 구성 및 discord.com allowlist 적용, 고정 IP·포트를 [Issue B(#75)](https://github.com/321Team/fds-project-baseline/issues/75)에 전달 |
| Related Decision IDs | D17; D33; D34; D35 — 현행 영향 기준. 신규 CR 승인·신규 D-ID/Interface ID는 미확정 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | [발행 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18), 승인 SHA 72599ae49342b0fb8dbd3d8ee60314afb9f907bb; [P1-MON-01 #17](https://github.com/321Team/fds-project-baseline/issues/17); [방식·책임 논의 infra-kubernetes #5](https://github.com/321Team/infra-kubernetes/issues/5); [현황 보고 5632931284](https://github.com/321Team/infra-kubernetes/issues/5#issuecomment-5632931284); [후속 CR #75](https://github.com/321Team/fds-project-baseline/issues/75); 사용자 2026-09-11 속성 보완·추적 요청 및 담당·일정 확정 지시(공통 Lead 이하영/Support 이재환, #74 Start 2026-09-11·End TBD, #75 프록시 서버 선행으로 Start/End TBD) |
| Schedule Note | Lead 이하영·Support 이재환, Start 2026-09-11·End TBD. 프록시 배치와 고정 scheme/host/IP/port를 확정하여 #75에 인계한다. 종료일은 후속 계획에서 확정한다. 교육장 주말 작업은 배정하지 않는다. G2는 추적용 분류이며 기존 P0/G2 Acceptance에 필수 조건을 자동 추가하지 않는다. |

## Source checklist

- [x] 프록시로 쓸 VM 확정: [DEC-P1-EGRESS-01 #78](https://github.com/321Team/fds-project-baseline/issues/78)에 따라 server08의 신규 비-K8S `egress-proxy01`, CentOS Stream 10, `10.1.93.56`을 선택했다. 기존 3CP+3Worker를 프록시 전용으로 전환하지 않는다. [관리 경로·svc_ansible 검증](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5673246444)을 확보했다.
- [x] 프록시 소프트웨어 선정 및 설치: Squid 선정은 완료했다. PR12 병합과 [PR18](https://github.com/321Team/infra-ansible/pull/18) 코드 후속은 구분한다. PR18 HEAD `d5147ebff0febbb8ab2afca28fe64d68301e033c`의 두 엔진(2.16.19/2.21.3) [localhost·중단복원 모형 45/45씩](https://github.com/321Team/fds-project-evidence/blob/f3b5ea69f5119fc89e15f128c086f1c8eba97fea/evidence/infra-ansible-followup/cicd-runner01-podman-20260916T110635Z/README.md) 검증은 완료됐으나 실제 Squid 설치/apply·서비스 인수는 HOLD다. 과거 2.21.3 환경 차단을 현재 미해소 항목으로 반복하지 않는다. **→ 2026-09-26 Lead 인수로 완료: [판정·근거](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5842375641).** 위 문장은 당시 이력이다.
- [x] discord.com만 통과시키는 필터링(allowlist) 규칙 구성: 코드/모형 검증과 실제 source 관측·3128 리스너·허용/거부·경유 TLS·rollback/re-apply 검증을 분리하며 운영 결과는 미확인이다. **→ 2026-09-26 Lead 인수로 완료: [판정·근거](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5842375641).** 위 문장은 당시 이력이다.
- [x] 완료 후 고정 IP·포트 값을 Issue B에 전달: 계획 endpoint `http://10.1.93.56:3128`은 [#75](https://github.com/321Team/fds-project-baseline/issues/75)에 공유됐지만 실제 서비스 인수·운영 endpoint 인계 수락은 남아 있다. **→ 2026-09-26 Lead 인수로 완료: [판정·근거](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5842375641).** 위 문장은 당시 이력이다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- ansible-egress-status-20260923:start -->
## 2026-09-23 Ansible 적용·증적 편입 현황 갱신

- 9/22 `da7f2cc` 기준 Squid apply `changed=8`, 즉시 멱등성 `changed=0`, standalone verify `rc=0`은 기존 실행 원본으로 확인된 범위입니다. 아래의 Squid apply HOLD/미실행 문구는 이전 시점 이력입니다.
- [증적 PR19](https://github.com/321Team/fds-project-evidence/pull/19)는 9/23 독립 승인·병합 완료. [후속 증적 PR13](https://github.com/321Team/fds-project-evidence/pull/13)도 기존 승인 HEAD 그대로 병합했습니다.
- 적용 코드 [Ansible PR43](https://github.com/321Team/infra-ansible/pull/43)는 Open입니다. [Codex 보조 기술검토](https://github.com/321Team/infra-ansible/pull/43#pullrequestreview-5290139516)에서 코드 차단 결함은 발견하지 않았으나 **사람의 독립 승인·Lead 병합 판단은 미완료**입니다. 사후 검토를 사전 승인으로 소급하지 않습니다.
- README의 precheck `tree=clean` 오표기는 원본의 `tree=dirty`와 구분하도록 [증적 정정 PR21](https://github.com/321Team/fds-project-evidence/pull/21)에 반영했습니다. 이후 apply/verify의 clean·성공 기록과 원본 로그는 유지합니다.
- Worker 3대 Source 범위는 Pod 배치·taint 확인과 담당자 동의에 따른 후보 주소입니다. proxy에서 관측한 post-SNAT 3주소 전체의 원본 실측으로 확대하지 않습니다.
- endpoint 전달과 #75의 실전송 보고는 이미 있으므로 인계를 처음부터 반복하지 않습니다. #74의 **최종 서비스 인수·운영 인계 수락 판정은 기존 Lead 이하영이 담당**하며 이번 기록 갱신으로 AC를 체크하거나 종결하지 않습니다.

기존 담당·일정·상태·AC는 유지합니다. NTP 인수와 MON 전체 완료를 새 상호 선행조건으로 묶지 않습니다.
<!-- ansible-egress-status-20260923:end -->

<!-- ansible-review-followup:20260916:74:start -->
## 리뷰 반영 및 착수 조건 재점검 — 2026-09-16

**코드 리뷰 의견 반영 / Squid 실제 적용 HOLD.** [PR18](https://github.com/321Team/infra-ansible/pull/18) 최신 HEAD `d5147ebff0febbb8ab2afca28fe64d68301e033c`: apply/rollback 원본 백업 검증을 공통화하고 실제 call site의 파일/누락/심볼릭 링크/디렉터리 검사를 추가했습니다. 2.16.19 **45/45 기대결과 일치**(허용·거절·중단 모형 포함), 2.21.3은10개 통과 후 localhost preflight FAIL/환경 차단으로 behavioral NOT RUN입니다.

[새 증적](https://github.com/321Team/fds-project-evidence/blob/6a6a384c2870729d26767ec8d6e745ee75567ffe/evidence/infra-ansible-followup/review-20260916/README.md) / 증적 PR13 HEAD `6a6a384c2870729d26767ec8d6e745ee75567ffe`. 최신 코드·증적 독립 승인 전이며 Draft·미병합입니다. 실제 client source 실측·PR18 잔여 hardening 판단·서비스 인수·#75 운영 인계는 미완료입니다. 기존 PR12 승인·병합/관리 계정 검증과 담당·일정·AC는 유지합니다.

아래는 이전 HEAD·시점의 이력입니다.
<!-- ansible-review-followup:20260916:74:end -->

---

<!-- egress-postmerge-followup:20260916:start -->
## PR #12 병합 및 후속 수정 착수 — 2026-09-16

**PR #12는 09-16 12:10:45 KST 병합 완료입니다. Squid 실제 적용·서비스 인수는 HOLD를 유지합니다.** 아래 ab48f52/open/unmerged 기록은 당시 이력입니다.

- 병합 main `57e7cc740e7a406387848c52f4aa56b98c516168`. 기존 코드 승인·병합 기록을 보존합니다.
- 사용자 “착수”에 따라 [infra-ansible PR #18](https://github.com/321Team/infra-ansible/pull/18), HEAD `ca3a5b1c47364e5f929a13d253b956b5ed313e33`을 Draft로 게시했습니다. 정확한 egress_proxy 대상 비교, orphan 원본 백업 보호, apply/rollback 복원 필드 검증, 첫 rollback 변경 전 marker 무효화, 기존 firewall rule 보존 확인을 보완합니다.
- 고정 HEAD의 **2.16.19 localhost 검증 33개 기대결과 일치**. 실제 CLI·assert/copy/file 및 중단 모형이며 Squid/firewalld Runtime 시험이 아닙니다. 2.21.3 구문/대상 검사 후 localhost 사전시험은 검증 환경의 로컬 IPC EPERM으로 실패해 behavioral 재검증이 남습니다.
- [증적 PR #13](https://github.com/321Team/fds-project-evidence/pull/13). 코드·증적 모두 이하영 독립 리뷰 요청, 미승인·미병합. schema/hash·verify 입력 연결 등 범위 밖 hardening은 PR18 본문에서 추적합니다.
- 기존 svc SSH/Ansible/root become 검증 완료는 유지합니다. 실제 Alertmanager client source 실측, 수정본 리뷰·시험, Squid apply/allow-deny/TLS/logging/rollback/re-apply/idempotency 인수, #75 운영 인계는 미완료입니다.

이번 착수는 코드·격리 시험·증적 정리 범위이며 실제 서버 설정·AC·Lead/Support·일정·이슈 종결은 변경하지 않습니다.
<!-- egress-postmerge-followup:20260916:end -->

---

<!-- fds-egress-review:20260915-pr12:start -->
## PR #12 최신 수정본 검토 — 2026-09-15 / ab48f52

검토 HEAD `ab48f5258bb80b17c858fbfb68b992d0a69bfe62`, open/미병합. 930b903 이후 커밋4개(7b17c2d/de98239/746385b/ab48f52)를 대조했다. [공식 REQUEST_CHANGES](https://github.com/321Team/infra-ansible/pull/12#pullrequestreview-5206541386)는 **2026-09-15 15:50:58 KST** 등록. [DR01–DR08 통합 추적 댓글](https://github.com/321Team/infra-ansible/pull/12#issuecomment-5674377321)을 같은 ID로 갱신한다.

- **새 코드 수용:** DR01 add/remove 전체 rule 일치(8개 대조군), DR02 {},[]·외부 host/change 거절, DR03 -n 역조회 차단(ACL 모델10), DR06 IP/CIDR 범위(원문 조건식12), DR07 config4조합·기존 설치 service 사후 대조, DR08 모든 non-localhost recap·localhost-only 거절·run/입력hash/rc·finalize 표시. DR05 NO_PROXY/curlrc 수정 수용 유지.
- **DR07/P1 잔여:** active+disabled에서는 enable 변경만으로 start.changed=true가 되어 reload를 생략하고 새 checksum을 기록한다. 다음 실행도 stale 상태를 유지한다. apply M→rollback O→같은 입력 apply M도 rollback이 marker를 무효화하지 않아 reload를 생략한다. 원문 task/실제 Ansible 모듈+합성 systemctl·localhost marker copy 근거이며 실제 Squid 장애 관측은 아니다.
- **DR02/P1 잔여:** 식별자만 맞고 필드/규칙 이력이 없는 baseline을 수용하고, force:false 제거로 orphan 원본 A를 B로 덮어쓴다. 원본 보존·불일치 거절·schema/백업 일치 검증, standalone verify 입력 연결·baseline 전환 안내가 필요하다.
- **DR04/P1 잔여:** 원문 Host 헤더가 남아 있으며 %<A 추가로 비노출 기준을 충족하지 않는다. 공식 logformat상 %<A는 서버 FQDN/peer 이름, %<a가 실제 서버/peer IP다. 현재 주석의 의미와 보장을 정정해야 한다.
- **DR06/DR08 잔여:** 소수 port·client/domain dict를 수용, candidate diff/실측근거 미완료. 같은 timestamp의 독립 실행 로그 덮어쓰기와 정확한 expected target 집합 대조가 남는다. DR01 원래 규칙 보존 확인 및 DR07 신규 설치 사후 서비스·config hash/mode 검사도 통합 기준에 유지한다.
- **본문 갱신 수용:** .56 확정, handler 참조 제거, 실제 apply HOLD는 반영됐다. “대상 미정” 불일치는 해소. 다만 작성자 15:47:01 종합 보고의 코드 전 항목 완료와 본문의 승인됨/실측만 잔여 표현은 현재 코드 반례·REQUEST_CHANGES와 구분해야 한다.
- **검증 수준:** PR13파일+ansible.cfg blob 일치. de98239 48개, 746385b delta31개, ab48f52 delta17개 기록은 PASS/반례/모형/동일성 확인을 구분한 증적이다. 합산 전체 PASS 수가 아니다. syntax-check4/bash 및 변경된 apply syntax/bash 재확인. check runs/statuses 각각0. 실제 Squid parser/firewalld/lab apply·verify·rollback NOT RUN.
- **인계:** 관리 계정 svc SSH/Ansible/root become PASS·비-K8S .56 배치 유지. **Squid apply HOLD**, 실제 Source와 #74 서비스 인수 후 #75 운영 적용. 기존 AC·담당·일정·상태 유지. GWONUK 측 AI 보조 검토이며 이재환님의 승인을 대신하지 않는다. PR #9는 ICR #14에서 대응한다.
<!-- fds-egress-review:20260915-pr12:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** VM/OS/주소/DNS/관리 경로 완료 범위와 Squid apply HOLD 분리. 계정/복원결함/실측 Source ; A07/R03.

- 계정 인계에는 허용 공개키의 관리 참조·접속 Source·sudo/become 범위·inventory 그룹·회수 방법·svc SSH/module/become 결과가 필요하다. VMware Connect at power on·재부팅 후 네트워크/시간 지속성은 별도 미검증이다.

**프록시 As-built·운영 계정 인계 (A07)** — server08/egress-proxy01·2vCPU/2GiB/30GiB·ens160 .56/24·DNS .52/.53, DNS UDP/TCP4/4와 관리 .10→.56:22 runtime/permanent·반환 .10/32 via .58·관리자 SSH 결과를 자산/IP/IF/inventory에 연결한다. 2026-09-15 제출 증적 대조로 프록시 svc_ansible의 공개키 적용·sudo/root become·새 SSH·Ansible module 검증 PASS를 확인했다(단일 호스트, ok=5/failed=0). 권한은 이 프록시의 (root) NOPASSWD: ALL이며 키 접속 Source는 10.250.10.10으로 제한한다. [계정 실행·권한·회수 및 증적 검토](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5673246444)를 자산/IP/IF/저장소 inventory에 연결하는 문서 인계는 잔여다. Squid3128 적용은 rollback 결함/리뷰로 HOLD, 실제 Alertmanager source/selector·Secret 참조·허용/거부/복구·#75 인계는 잔여다.
근거: [배치/실측 #78](https://github.com/321Team/fds-project-baseline/issues/78) · [관리 경로](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663718791) · [계정](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663963879) · [변경 요청](https://github.com/321Team/infra-ansible/pull/12#pullrequestreview-5195815386)

**인계·관련 티켓:** [#75](https://github.com/321Team/fds-project-baseline/issues/75) · [#78](https://github.com/321Team/fds-project-baseline/issues/78).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-egress-decision:20260914 issue:78 -->
## 2026-09-14 사용자 결정 적용

[DEC-P1-EGRESS-01 #78](https://github.com/321Team/fds-project-baseline/issues/78)에 따라 **server08 / 신규 비-K8S VM egress-proxy01 / CentOS Stream 10 + Squid / 10.1.93.56:3128**을 채택한다. .56의 기존 VM 미사용은 사용자 확인으로, server08 자원·작업창 및 LAN 중복 미관측은 기존 증적으로 확인했다. 링크·게이트웨이·DNS·시간 동기화 및 관리 경로 보완 후 관리자 SSH 로그인 성공과 관련 영구 설정값 반영을 확인했다. svc_ansible의 새 SSH·Ansible module·root become 검증은 2026-09-15 제출 증적으로 통과했다. Squid 서비스 인수는 미완료다. .57은 예비로 유지하고 자동 전환하지 않는다.

Alertmanager→프록시→discord.com:443의 제한된 외부 송신과 최소 합성 알림만 허용한다. 직접 외부 egress·일반 프록시 사용·비밀정보 송신은 금지한다. Secret 생성/재발급은 이하영, 설정 인계/검증은 이재환의 기존 역할을 따른다. 기존 3CP+3Worker와 P1 비차단 범위·담당·TBD 일정은 유지한다.

다음은 저장소 inventory·As-built/Interface 계정 인계, PR #12 복원 결함 수정·실제 Alertmanager source 확인과 독립 리뷰다. 기존 '6대 중 전용 전환/배치 미정' 문구는 아래 원문 이력이며 현행 선택은 이 결정 블록을 따른다.

배치 결정과 실제 관리 경로 준비 결과는 아래 최신 실행 현황으로 추적한다. 기술 PR 승인·Squid 적용 및 원문 AC 완료는 미완료다.


<!-- fds-egress-progress:20260914-management-ssh-ready -->
## 최신 실행 현황 — 2026-09-15 관리 계정 검증 반영

[관리 계정 실행 증적 검토 PASS](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5673246444). 계정 외 기존 네트워크·DNS·시간 결과는 2026-09-14 제출 증적 기준이다.

[관리 경로 영구 설정 및 SSH 로그인 증적](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663718791)

[Ansible 관리 계정 사전 확인](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663805023) · [계정 생성·기존 control01 권한 확인 후속](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663963879)

| 구분 | 현재 상태 |
|---|---|
| VM·OS | server08 / egress-proxy01, 2 vCPU·2 GiB·30 GiB, CentOS Stream 10 최소 설치 |
| 네트워크 | ens160, 10.1.93.56/24, 기본 GW .254, DNS .52/.53, search fds.internal, MTU1500. VMware NIC Connected 보완 후 링크·GW 통신 복구 확인 |
| DNS | dns01·dns02 BIND ACL 및 firewalld ipset에 .56 반영, runtime/permanent membership 확인. 프록시에서 양 DNS UDP/TCP 직접 질의 4/4 성공 |
| 시간 동기화 | chronyc refresh 후 선택 소스 존재, tracking Leap status Normal 및 System clock synchronized=yes 확인. 승인된 고정 NTP 정책·장기 지속성은 미검증 |
| 관리 게이트웨이 | 관리 서버 → 신규 프록시 TCP 22 개별 허용 규칙을 mgmt-to-physical 정책의 만료 없는 runtime 및 permanent 설정에 반영. 양쪽 query=yes 확인 |
| 반환 경로 | 10.250.10.10/32 via 10.1.93.58 dev ens160. 임시 경로로 TCP22_RC=0 확인 후 ens160 NetworkManager 프로파일에 저장했으며 저장값·현재 경로 조회 확인 |
| 자동 연결 | connection.autoconnect=yes 확인. VMware Connect at power on 설정 및 재부팅 후 지속성은 별도 확인 필요 |
| SSH | sshd active/enabled 및 TCP 22 LISTEN 확인. ansible01에서 ED25519 호스트 키 등록 후 관리자 로그인 성공. 원격 hostname=egress-proxy01, 사용자=server08_egress-proxy01 확인 |
| Ansible | 2026-09-15 svc_ansible 공개키·sudo 적용 및 새 SSH 확인(10.250.10.10 → 10.1.93.56:22). core 2.16.19로 단일 호스트 module·hostname·Python 명령·root become/assert 5개 통과(ok=5, changed=0, unreachable=0, failed=0). 키 Source 제한 from=10.250.10.10,restrict 및 (root) NOPASSWD: ALL. 기존 Python 3.12.13 확인 이력 유지; 이번 로그는 정확한 버전 문자열 미출력 |
| 코드·리뷰 | PR #12 ab48f52, open/unmerged. [DR01–DR08 통합 검토](https://github.com/321Team/infra-ansible/pull/12#issuecomment-5674377321): DR03/DR05 수정 수용, DR01/02/06/07/08 부분 수용, DR04 잔여. 활성화 marker·원본 보존·schema·로그·증적 잔여로 [REQUEST_CHANGES](https://github.com/321Team/infra-ansible/pull/12#pullrequestreview-5206541386)(09-15 15:50:58 KST), Squid apply HOLD. 실제 Source·서비스 인수 잔여 |
| 인계 판정 | 관리 TCP/SSH 복구·영구 설정값과 svc 계정 SSH/Ansible/root become PASS 확인. 저장소 inventory·As-built/Interface 연결은 잔여. **Squid apply HOLD**, 실제 프록시 서비스 인수와 #75 endpoint 인계는 미완료 |

**다음 실행:** 계정·키 참조·권한·회수 절차의 저장소 inventory/As-built 인계 → PR #12 코드 보완·실제 Alertmanager source 확정·독립 리뷰 → Squid 적용/인수 → #75 인계. 관리 계정 검증은 완료했으며 재부팅 후 지속성은 아직 검증하지 않았다.

사용자 후속 지시에 따라 infra-kubernetes PR #9의 마스킹 수정·회귀시험·재리뷰는 [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14)에서 대응한다. 이 티켓은 프록시 준비와 infra-ansible PR #12를 추적한다.

사용자는 기존 18:30 작업창 이후에도 ‘지속적으로 가능’으로 후속 작업을 허용했고, 관련 내용의 본문·댓글 기록 및 동일 범위의 지속 갱신을 승인했다. Lead 이하영/Support 이재환, In Progress·End TBD 및 기존 원문 AC·승인 상태는 유지한다.

이전 NO-CARRIER·DNS 허용 누락·NTP 미동기화·TCP 시간 초과는 댓글의 장애 이력으로 보존한다. 게이트웨이 임시 규칙 삭제 시 NOT_ENABLED는 삭제 시점의 부재를 나타내며, 이후 runtime/permanent 추가·조회 성공을 확인했다. NTP 복구 전 증적의 게스트 시각은 미동기화 상태였고 복구 시 시간 역행 기록도 확인됐다.
<!-- /fds-egress-progress:20260914-management-ssh-ready -->


---

# CR-P1-MON-01-01 — Alertmanager Egress 프록시 서버 구성

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | CR-P1-MON-01-01 |
| Phase | Phase 1 |
| Category | Monitoring / Alerting Egress Change Control |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-11 |
| End | 2026-10-06 |
| Calendar Days | TBD — Start/End 확정 후 산정 |
| Working Days | TBD — 계획일·가용일 확정 후 산정, 교육장 주말 작업 0 |
| Lead | 이하영 |
| Support | 이재환 |
| Exit Criteria | discord.com 아웃바운드 확인, 프록시 전용 VM 확정, Squid/Nginx 구성 및 discord.com allowlist 적용, 고정 IP·포트를 [Issue B(#75)](https://github.com/321Team/fds-project-baseline/issues/75)에 전달 |
| Related Decision IDs | D17; D33; D34; D35 — 현행 영향 기준. 신규 CR 승인·신규 D-ID/Interface ID는 미확정 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | [발행 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18), 승인 SHA 72599ae49342b0fb8dbd3d8ee60314afb9f907bb; [P1-MON-01 #17](https://github.com/321Team/fds-project-baseline/issues/17); [방식·책임 논의 infra-kubernetes #5](https://github.com/321Team/infra-kubernetes/issues/5); [현황 보고 5632931284](https://github.com/321Team/infra-kubernetes/issues/5#issuecomment-5632931284); [후속 CR #75](https://github.com/321Team/fds-project-baseline/issues/75); 사용자 2026-09-11 속성 보완·추적 요청 및 담당·일정 확정 지시(공통 Lead 이하영/Support 이재환, #74 Start 2026-09-11·End TBD, #75 프록시 서버 선행으로 Start/End TBD) |
| Schedule Note | Lead 이하영·Support 이재환, Start 2026-09-11·End TBD. 프록시 배치와 고정 scheme/host/IP/port를 확정하여 #75에 인계한다. 종료일은 후속 계획에서 확정한다. 교육장 주말 작업은 배정하지 않는다. G2는 추적용 분류이며 기존 P0/G2 Acceptance에 필수 조건을 자동 추가하지 않는다. |

<!-- fds-cr-tracking:20260911 record-id:CR-P1-MON-01-01 -->
## 현행 추적·속성 검토 — 2026-09-11

- **운영 상태:** In Progress/Open 유지. **변경안:** PENDING_REVIEW. **실제 적용·Runtime 인수:** NOT VERIFIED. 기존 B안·Discord·DNS UDP/TCP53·monitoring-api 방식 합의와 최종 변경 승인·실행 인수는 구분한다.
- **대표 Milestone:** [G2 Security / Feature Ready](https://github.com/321Team/fds-project-baseline/milestone/3), 기존 P1-MON-01/#17 및 P1-SEC-01/#19에 따른 추적용 매핑. [G2 #23](https://github.com/321Team/fds-project-baseline/issues/23)의 09-21은 Gate 계획 목표이며 이 CR의 확정 End가 아니다. 기존 논의의 Phase 1 비차단 범위를 유지한다.
- **Lead/Support:** 사용자 2026-09-11 확정 지시에 따라 Lead는 이하영, Support는 이재환이다. 기존 TBD 기록을 이번 지시로 갱신한다. GitHub Assignee는 확인된 Lead 계정 hayeounglee로 설정하고 Support는 본문으로 관리한다. infra-kubernetes #5의 이하영 Secret 생성 역할과 이재환 receiver/config 인계 역할은 세부 실행·인계 항목으로 유지한다.
- **일정:** 사용자 2026-09-11 지시에 따라 Start는 2026-09-11, End는 TBD다. End 확정 전 Calendar/Working Days는 TBD로 유지한다. 교육장 주말 작업은 배정하지 않는다.
- **Decision/Risk:** D17/D33/D34/D35는 영향 검토 대상이지 새 예외 승인 기록이 아니다. RISK-04는 실제 Source/Return Path 오판, RISK-07은 증적 부재·완료 과대판정 위험을 연결한다. 근거: [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14), [Monitoring #17](https://github.com/321Team/fds-project-baseline/issues/17). 신규 D-ID·Interface ID는 임의 생성하지 않는다.
- **Type/Label:** 본문 Type=Change Request와 기존 type:change-request 포함 5개 라벨은 일치한다. 실제 GitHub Issue Type은 별도 확인·적용 대상이며 라벨만으로 native Type 완료를 표시하지 않는다.
- **정본 인계:** [v3.1.19 수집 PR #73](https://github.com/321Team/fds-project-baseline/pull/73)에 이 CR과 새 리뷰·후속 입력을 연결한다. 수집은 발행 v18의 소급 변경 또는 v19 발행이 아니다.

### 원문 보고와 현행 판정의 구분

아래의 확인 완료 항목은 담당자의 현황 보고로 보존한다. Worker01의 curl 성공은 그 Host에서의 연결 보고이며, Pod→프록시→Discord 경유·권한·변경 승인 또는 전체 네트워크의 MITM 부재를 증명하지 않는다. 학원 네트워크 관리자 승인 절차가 불필요한지 이번 자료만으로 확인할 수 없다. 3CP+3Worker 중 한 VM을 프록시 전용으로 전환하거나 새 VM/IP·port를 배정하는 것은 승인된 사실로 처리하지 않는다. 프록시 배치·기존 역할/자원 영향·실제 endpoint·allowlist·로그 마스킹·복구 및 #75 인계를 변경 검토에 포함한다.

퇴역한 IF-24(Alertmanager→monitor01), 현행 IF-06B(Prometheus→monitor01 Remote Write), 신규 Discord 프록시 egress는 각각 다른 경로다. 새 CR이 IF-24를 되살리거나 IF-06B를 대체하는 것으로 해석하지 않는다. 원문 체크·기존 승인·기존 티켓 AC를 자동 변경하지 않는다.

---

> **참고:** 기존 [P1-MON-01] (#17)에는 "IF-24 Alertmanager Webhook은 구성하지 않으며 Alertmanager는 외부 monitor01로 직접 송신하지 않는다"는 결정이 명시되어 있습니다. 본 CR은 Discord Webhook 수신을 위한 예외적 외부 egress 허용(프록시 경유)을 다루므로, 승인 시 해당 결정과의 정합화(D-ID 갱신 또는 예외 범위 명시)가 필요합니다.
>
> 본 이슈(A)는 **egress 프록시 서버 구성**을 다룹니다. Kubernetes 측 NetworkPolicy·podSelector·Secret 관리는 별도 [Issue B(#75)](https://github.com/321Team/fds-project-baseline/issues/75)에서 다룹니다.

---

### Scope

#### In Scope

- Alertmanager → discord.com(443/HTTPS) 아웃바운드 경로 허용 여부 검증
- 학원 내부망 egress 프록시 신규 구성(Squid/Nginx 등) 및 discord.com allowlist 규칙
- 프록시 전용 VM 선정
- 확정된 프록시 고정 IP·포트를 Issue B(NetworkPolicy)에 전달

#### Out of Scope

- Alertmanager podSelector·NetworkPolicy·Secret 관리 (Issue B)
- Alertmanager 외 다른 Pod/서비스의 일반 egress 정책 변경
- [P1-MON-01](#17) 본 Gate의 기존 Acceptance Criteria 변경

---

## Alertmanager egress용 프록시 서버 구성

### ✅ 확인 완료

- discord.com 아웃바운드(443, HTTPS): k8s-worker01에서 `curl -v https://discord.com` 테스트 완료. TLS 핸드셰이크 정상, 인증서 검증 정상(issuer: Google Trust Services, MITM 가로채기 없음), 실제 연결 성공. → 학원 내부망에서 discord.com으로 나가는 경로 자체는 막혀있지 않음을 확인.
- 사내 egress 프록시 존재 여부: 기존에 구성된 프록시는 없음. 신규로 직접 구성해야 함.
- 프록시 구성 가능 여부: 443 아웃바운드가 열려있으므로 VM 6대 중 하나에 팀이 직접 프록시(Squid/Nginx 등)를 구성하는 방식으로 진행 가능. 학원 네트워크 관리자 승인 절차 불필요.

### 확인/작업 현황 — 2026-09-18 증적 대조

- [x] 프록시로 쓸 VM 확정: [DEC-P1-EGRESS-01 #78](https://github.com/321Team/fds-project-baseline/issues/78)에 따라 server08의 신규 비-K8S `egress-proxy01`, CentOS Stream 10, `10.1.93.56`을 선택했다. 기존 3CP+3Worker를 프록시 전용으로 전환하지 않는다. [관리 경로·svc_ansible 검증](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5673246444)을 확보했다.
- [x] 프록시 소프트웨어 선정 및 설치: Squid 선정은 완료했다. PR12 병합과 [PR18](https://github.com/321Team/infra-ansible/pull/18) 코드 후속은 구분한다. PR18 HEAD `d5147ebff0febbb8ab2afca28fe64d68301e033c`의 두 엔진(2.16.19/2.21.3) [localhost·중단복원 모형 45/45씩](https://github.com/321Team/fds-project-evidence/blob/f3b5ea69f5119fc89e15f128c086f1c8eba97fea/evidence/infra-ansible-followup/cicd-runner01-podman-20260916T110635Z/README.md) 검증은 완료됐으나 실제 Squid 설치/apply·서비스 인수는 HOLD다. 과거 2.21.3 환경 차단을 현재 미해소 항목으로 반복하지 않는다. **→ 2026-09-26 Lead 인수로 완료: [판정·근거](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5842375641).** 위 문장은 당시 이력이다.
- [x] discord.com만 통과시키는 필터링(allowlist) 규칙 구성: 코드/모형 검증과 실제 source 관측·3128 리스너·허용/거부·경유 TLS·rollback/re-apply 검증을 분리하며 운영 결과는 미확인이다. **→ 2026-09-26 Lead 인수로 완료: [판정·근거](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5842375641).** 위 문장은 당시 이력이다.
- [x] 완료 후 고정 IP·포트 값을 Issue B에 전달: 계획 endpoint `http://10.1.93.56:3128`은 [#75](https://github.com/321Team/fds-project-baseline/issues/75)에 공유됐지만 실제 서비스 인수·운영 endpoint 인계 수락은 남아 있다. **→ 2026-09-26 Lead 인수로 완료: [판정·근거](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5842375641).** 위 문장은 당시 이력이다.

지금 확인/결정된 보안 설정 사항들을 change request로 만들 예정입니다.
미결된 내용을 확인해보시고, 추후 이에 대한 리뷰를 요청드리겠습니다.

---

### Dependency

- 선행/연동 기준: [P1-MON-01](#17) Alertmanager 배포 및 기존 "외부 미송신" 결정
- 참고: [P1-SEC-01](#19) 최소 egress 정책 논의
- 후속: 본 이슈에서 확정한 프록시 IP·포트는 [Issue B(#75)](https://github.com/321Team/fds-project-baseline/issues/75)의 NetworkPolicy `ipBlock`에 반영

---

Related to #17


