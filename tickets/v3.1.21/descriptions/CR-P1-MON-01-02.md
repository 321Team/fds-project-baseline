# CR-P1-MON-01-02 — Alertmanager Egress Kubernetes 보안 설정 (NetworkPolicy)

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/75
Updated at: 2026-09-26T10:57:29Z
Source body SHA256: `3b32fad976218661d8fa77b8f22b3d89abf7e5da76f2463b5966f8263298702c`
GitHub: closed / completed
Current disposition: Source lifecycle/AC retained; no new acceptance by this publication.

| Property | Current source value |
|---|---|
| Record ID | CR-P1-MON-01-02 |
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
| Exit Criteria | Alertmanager 전용 NetworkPolicy(Egress) 작성·적용, podSelector 라벨 확정, Secret 주입·회전·폐기 절차 확정, 검증(허용/차단/알림 전송) 완료 및 Support Review 완료 |
| Related Decision IDs | D17; D33; D34; D35 — 현행 영향 기준. 신규 CR 승인·신규 D-ID/Interface ID는 미확정 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | [발행 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18), 승인 SHA 72599ae49342b0fb8dbd3d8ee60314afb9f907bb; [P1-MON-01 #17](https://github.com/321Team/fds-project-baseline/issues/17); [방식·책임 논의 infra-kubernetes #5](https://github.com/321Team/infra-kubernetes/issues/5); [현황 보고 5632931284](https://github.com/321Team/infra-kubernetes/issues/5#issuecomment-5632931284); [선행 CR #74](https://github.com/321Team/fds-project-baseline/issues/74); 사용자 2026-09-11 속성 보완·추적 요청 및 담당·일정 확정 지시(공통 Lead 이하영/Support 이재환, #74 Start 2026-09-11·End TBD, #75 프록시 서버 선행으로 Start/End TBD) |
| Schedule Note | Lead 이하영·Support 이재환. #74의 프록시 서버 구성 완료와 고정 proxy endpoint 인계가 선행조건이므로 Start/End는 TBD다. 인계 후 실제 selector·Secret·정책·시험에 반영한다. 초안 준비는 병행 가능하며 착수일 확정으로 간주하지 않는다. 교육장 주말 작업은 배정하지 않는다. G2는 추적용 분류이며 기존 P0/G2 Acceptance에 필수 조건을 자동 추가하지 않는다. |

## Source checklist

- [x] [Issue A (#74)](https://github.com/321Team/fds-project-baseline/issues/74)에서 확정된 프록시 IP·포트를 NetworkPolicy `ipBlock`에 반영: 계획값 `10.1.93.56:3128`은 결정·공유됐다. 실제 서비스 인수 뒤 정책 적용·연결 검증은 잔여이며 초안 준비는 병행 가능하다.
- [x] podSelector 실제 라벨 확정: `app: alertmanager`는 가정값이다. 이관된 [infra-monitoring 참고본](https://github.com/321Team/infra-monitoring/blob/73b9432e8c793f64469ea708c14018f010ad74c1/docs/CANONICAL_GAPS.md)을 정본 배포로 간주하지 않고 실제 Pod·Manifest와 대조해야 한다.
- [x] Secret 주입·회전·폐기 절차: [기존 결정 #78](https://github.com/321Team/fds-project-baseline/issues/78)에 따라 생성/재발급 주체는 이하영, 설정 인계/검증은 이재환이다. 정기 회전 여부·주입/폐기 절차 및 검증은 잔여다. 역할 자체를 미정으로 반복하지 않는다.
- [x] 검증 계획·실행: 프록시 경유 허용 / 비승인 목적지·직접 외부 경로 차단 / 알림 발생·해소 / 전송 실패·복구를 확인한다. [#74 선행 코드의 두 엔진 localhost 회귀](https://github.com/321Team/fds-project-evidence/blob/f3b5ea69f5119fc89e15f128c086f1c8eba97fea/evidence/infra-ansible-followup/cicd-runner01-podman-20260916T110635Z/README.md)는 완료됐으나 Alertmanager→Squid→Discord 실제 결과가 아니며 운영 적용 HOLD는 유지한다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- fds-status-sync:20260926 -->
## 현재 상태 동기화 — 2026-09-26 KST

- GitHub State: **Closed / Completed**
- 본문 Status: **Done**
- Label: `status:done`
- 종결 근거: AC ①~④ 충족 + [DEC-P1-MON-02 #109](https://github.com/321Team/fds-project-baseline/issues/109) 등록 완료.
- 아래의 `In Progress/Open/HOLD` 표현은 해당 시점의 이력이며 현재 상태를 덮어쓰지 않습니다.

<!-- ansible-review-followup:20260916:75:start -->
## 리뷰 반영 및 착수 조건 재점검 — 2026-09-16

**#74 서비스 인수 선행 / 운영 적용 HOLD.** [PR18](https://github.com/321Team/infra-ansible/pull/18) `d5147ebff0febbb8ab2afca28fe64d68301e033c`에 백업 검증 공통화 리뷰 의견을 반영했고, 2.16.19 localhost45개 기대결과가 일치했습니다. 2.21.3 환경 차단 및 최신 코드·증적 독립 승인 대기는 남았습니다. [새 검증·착수 조건](https://github.com/321Team/fds-project-evidence/blob/6a6a384c2870729d26767ec8d6e745ee75567ffe/evidence/infra-ansible-followup/review-20260916/README.md).

정책/selector/Secret 참조 초안 준비는 기존 범위에서 병행 가능하지만, 실제 client source와 #74 서비스 인수 없이 운영 적용하지 않습니다. 이번에는 실제 Squid/Alertmanager 설정·Secret·AC·담당·일정·종결 상태를 변경하지 않았습니다.

아래는 이전 HEAD·시점의 이력입니다.
<!-- ansible-review-followup:20260916:75:end -->

---

<!-- egress-postmerge-dependency:20260916:start -->
## 선행 프록시 코드 후속 현황 — 2026-09-16

[infra-ansible PR #12](https://github.com/321Team/infra-ansible/pull/12)는 **09-16 12:10:45 KST 병합 완료**입니다. 아래 open/unmerged 표현은 당시 이력입니다. 후속 복원·멱등성 보완은 [PR #18](https://github.com/321Team/infra-ansible/pull/18) `ca3a5b1`, 검증 증적은 [evidence PR #13](https://github.com/321Team/fds-project-evidence/pull/13)으로 착수했고 각각 Draft/독립 리뷰 대기입니다.

2.16.19 localhost 33개 기대결과 일치는 실제 프록시 인수가 아닙니다. 2.21.3 behavioral 시험도 검증 환경의 로컬 IPC 제한으로 미완료입니다. **#74 실제 source 실측·Squid 서비스 인수 전까지 #75 운영 적용 HOLD**를 유지합니다. 기존 정책/selector/Secret/시험 초안 준비는 병행 가능하며 실제 운영 Manifest·Secret·NetworkPolicy는 변경하지 않았습니다. 기존 AC·담당·일정·Open 상태를 유지합니다.
<!-- egress-postmerge-dependency:20260916:end -->

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

**이 티켓의 점검 결과:** #74 인수 후 운영 적용. 실제 selector/NetworkPolicy/Secret 참조·전달/거부/복구 증거 ; A07.

- #74 인수 전에도 설정 초안은 준비할 수 있다. 운영 적용은 #74 서비스 인수 뒤에 실제 Pod selector/관측 Source·CoreDNS·3128·discord.com:443 CONNECT·최소 합성 payload·Secret 참조와 허용/거부/복구 결과를 연결한다. Secret 생성/회전은 이하영, 설정 인계/검증은 이재환 역할을 유지한다.

**인계·관련 티켓:** [#17](https://github.com/321Team/fds-project-baseline/issues/17) · [#74](https://github.com/321Team/fds-project-baseline/issues/74) · [#78](https://github.com/321Team/fds-project-baseline/issues/78).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-egress-decision:20260914 issue:78 -->
## 2026-09-14 사용자 결정 적용

[DEC-P1-EGRESS-01 #78](https://github.com/321Team/fds-project-baseline/issues/78)에 따라 **server08 / 신규 비-K8S VM egress-proxy01 / CentOS Stream 10 + Squid / 10.1.93.56:3128**을 채택한다. .56의 기존 VM 미사용은 사용자 확인으로, 자원·작업창·LAN 중복 미관측은 기존 증적으로 확인했다. ens160의 .56/24 반영, 링크·게이트웨이·DNS·시간 동기화 및 관리자 SSH 복구를 확인했다. svc_ansible의 공개키·sudo 적용과 새 SSH·Ansible module·root become 검증은 2026-09-15 제출 증적으로 통과했다. 프록시 서비스 인수는 미완료다. .57은 예비로 유지하고 자동 전환하지 않는다.

Alertmanager→프록시→discord.com:443의 제한된 외부 송신과 최소 합성 알림만 허용한다. 직접 외부 egress·일반 프록시 사용·비밀정보 송신은 금지한다. Secret 생성/재발급은 이하영, 설정 인계/검증은 이재환의 기존 역할을 따른다. 기존 3CP+3Worker와 P1 비차단 범위·담당·TBD 일정은 유지한다.

#74 인수 전 정책·시험 초안은 병행 가능하다. .56:3128은 계획값으로 반영하고 실제 운영 적용은 #74 endpoint 인수 후 진행한다. 실제 podSelector/Source·TLS·Secret 참조는 구현자가 확인한다.

이번은 사용자의 권장안 적용 지시에 따른 결정 기록이며 기술 PR APPROVED·실서버 실행·AC 완료를 뜻하지 않는다.


<!-- fds-egress-dependency:20260914-management-ready -->
## 최신 선행조건 현황 — 2026-09-15 관리 계정 검증 반영

[선행 관리 계정 실행 증적 검토 PASS](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5673246444). 계정 외 기존 네트워크·DNS·시간 결과는 2026-09-14 제출 증적 기준이다.

[선행 #74](https://github.com/321Team/fds-project-baseline/issues/74) · [관리 경로·영구 설정](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663718791) · [계정 준비 후속](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663963879)

- server08 / 비-K8S 전용 egress-proxy01 / CentOS Stream 10 / 10.1.93.56/24 준비. VMware NIC 연결 보완 후 링크·게이트웨이 복구, 양 DNS UDP/TCP 질의 성공, 시간 동기화 및 ansible01의 관리자 SSH 로그인 확인.
- 관리 TCP 22 허용 규칙(runtime/permanent)과 반환 경로 `10.250.10.10/32 via 10.1.93.58`의 NetworkManager 저장값, autoconnect=yes 확인. 재부팅 후 지속성은 미검증.
- svc_ansible 공개키·sudo 적용 및 ansible01(10.250.10.10) → egress-proxy01(10.1.93.56)의 새 계정 SSH·Ansible module/root become 검증 PASS(core 2.16.19, ok=5/changed=0/unreachable=0/failed=0). 단일 프록시 관리 계정 검증이며 실제 Alertmanager 경유 통신·Kubernetes/Secret 검증은 포함하지 않는다.
- 계획 endpoint는 **http://10.1.93.56:3128**. 실제 3128 리스너·allowlist·차단·경유 TLS·장애/복구 및 서비스 인수는 미완료다. 관리 SSH 성공을 Alertmanager→프록시 경로 성공으로 확대하지 않는다.
- infra-ansible PR #12 ab48f52, open/unmerged. [DR01–DR08 통합 검토](https://github.com/321Team/infra-ansible/pull/12#issuecomment-5674377321): DR03/DR05 수정 수용, DR01/02/06/07/08 부분 수용, DR04 잔여. 활성화 marker·원본 보존·schema·로그·증적 잔여로 [REQUEST_CHANGES](https://github.com/321Team/infra-ansible/pull/12#pullrequestreview-5206541386)(09-15 15:50:58 KST), Squid apply HOLD. 관리 계정 PASS 유지. #74 실제 Source/서비스 인수 후 #75 운영 적용. 본문 .56 확정/HOLD 반영은 수용, 전체 코드 완료는 아님.
- 실제 Alertmanager podSelector·프록시가 관측하는 client source·최소 정책·Secret 주입/회전/폐기·허용/차단/합성 알림 시험 초안은 병행 가능하다. **운영 적용 및 endpoint 인계 수락은 #74 서비스 인수 후** 진행한다.
- infra-kubernetes PR #9의 수정·재리뷰는 사용자 지시에 따라 [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14)에서 대응한다.
- In Progress/Open, Lead 이하영 / Support 이재환, Start/End TBD 유지. 기존 AC·Support Review·Secret 작업은 미완료 상태를 보존한다.
<!-- /fds-egress-dependency:20260914-management-ready -->


---

# CR-P1-MON-01-02 — Alertmanager Egress Kubernetes 보안 설정 (NetworkPolicy)

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | CR-P1-MON-01-02 |
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
| Exit Criteria | Alertmanager 전용 NetworkPolicy(Egress) 작성·적용, podSelector 라벨 확정, Secret 주입·회전·폐기 절차 확정, 검증(허용/차단/알림 전송) 완료 및 Support Review 완료 |
| Related Decision IDs | D17; D33; D34; D35 — 현행 영향 기준. 신규 CR 승인·신규 D-ID/Interface ID는 미확정 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | [발행 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18), 승인 SHA 72599ae49342b0fb8dbd3d8ee60314afb9f907bb; [P1-MON-01 #17](https://github.com/321Team/fds-project-baseline/issues/17); [방식·책임 논의 infra-kubernetes #5](https://github.com/321Team/infra-kubernetes/issues/5); [현황 보고 5632931284](https://github.com/321Team/infra-kubernetes/issues/5#issuecomment-5632931284); [선행 CR #74](https://github.com/321Team/fds-project-baseline/issues/74); 사용자 2026-09-11 속성 보완·추적 요청 및 담당·일정 확정 지시(공통 Lead 이하영/Support 이재환, #74 Start 2026-09-11·End TBD, #75 프록시 서버 선행으로 Start/End TBD) |
| Schedule Note | Lead 이하영·Support 이재환. #74의 프록시 서버 구성 완료와 고정 proxy endpoint 인계가 선행조건이므로 Start/End는 TBD다. 인계 후 실제 selector·Secret·정책·시험에 반영한다. 초안 준비는 병행 가능하며 착수일 확정으로 간주하지 않는다. 교육장 주말 작업은 배정하지 않는다. G2는 추적용 분류이며 기존 P0/G2 Acceptance에 필수 조건을 자동 추가하지 않는다. |

<!-- fds-cr-tracking:20260911 record-id:CR-P1-MON-01-02 -->
## 현행 추적·속성 검토 — 2026-09-11

- **운영 상태:** In Progress/Open 유지. **변경안:** PENDING_REVIEW. **실제 적용·Runtime 인수:** NOT VERIFIED. 기존 B안·Discord·DNS UDP/TCP53·monitoring-api 방식 합의와 최종 변경 승인·실행 인수는 구분한다.
- **대표 Milestone:** [G2 Security / Feature Ready](https://github.com/321Team/fds-project-baseline/milestone/3), 기존 P1-MON-01/#17 및 P1-SEC-01/#19에 따른 추적용 매핑. [G2 #23](https://github.com/321Team/fds-project-baseline/issues/23)의 09-21은 Gate 계획 목표이며 이 CR의 확정 End가 아니다. 기존 논의의 Phase 1 비차단 범위를 유지한다.
- **Lead/Support:** 사용자 2026-09-11 확정 지시에 따라 Lead는 이하영, Support는 이재환이다. 기존 TBD 기록을 이번 지시로 갱신한다. GitHub Assignee는 확인된 Lead 계정 hayeounglee로 설정하고 Support는 본문으로 관리한다. infra-kubernetes #5의 이하영 Secret 생성 역할과 이재환 receiver/config 인계 역할은 세부 실행·인계 항목으로 유지한다.
- **일정:** 사용자 2026-09-11 지시에 따라 프록시 서버 구성을 선행조건으로 두고 Start/End는 TBD로 유지한다. #74의 프록시 구성 완료와 고정 endpoint 인계 후 일정을 확정한다. Calendar/Working Days는 TBD이며 교육장 주말 작업은 배정하지 않는다.
- **Decision/Risk:** D17/D33/D34/D35는 영향 검토 대상이지 새 예외 승인 기록이 아니다. RISK-04는 실제 Source/Return Path 오판, RISK-07은 증적 부재·완료 과대판정 위험을 연결한다. 근거: [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14), [Monitoring #17](https://github.com/321Team/fds-project-baseline/issues/17). 신규 D-ID·Interface ID는 임의 생성하지 않는다.
- **Type/Label:** 본문 Type=Change Request와 기존 type:change-request 포함 5개 라벨은 일치한다. 실제 GitHub Issue Type은 별도 확인·적용 대상이며 라벨만으로 native Type 완료를 표시하지 않는다.
- **정본 인계:** [v3.1.19 수집 PR #73](https://github.com/321Team/fds-project-baseline/pull/73)에 이 CR과 새 리뷰·후속 입력을 연결한다. 수집은 발행 v18의 소급 변경 또는 v19 발행이 아니다.

### 원문 보고와 현행 판정의 구분

#74 endpoint 인수 전 정책 초안·시험 설계는 진행할 수 있다. 실제 적용 전에는 scheme/host/IP/port, fds-msa의 고정 소스·실제 podSelector, 설치 Alertmanager 버전의 receiver/프록시/Secret 참조 스키마, 주입·회전·폐기·발송 데이터·Positive/Negative/실패·복구를 확인한다. 원본의 app: alertmanager 가정과 Discord 방식 합의는 실제 Manifest 검증 또는 Runtime PASS가 아니다.

퇴역한 IF-24(Alertmanager→monitor01), 현행 IF-06B(Prometheus→monitor01 Remote Write), 신규 Discord 프록시 egress는 각각 다른 경로다. 새 CR이 IF-24를 되살리거나 IF-06B를 대체하는 것으로 해석하지 않는다. 원문 체크·기존 승인·기존 티켓 AC를 자동 변경하지 않는다.

---

> **참고:** 기존 [P1-MON-01] (#17)에는 "IF-24 Alertmanager Webhook은 구성하지 않으며 Alertmanager는 외부 monitor01로 직접 송신하지 않는다"는 결정이 명시되어 있습니다. 본 CR은 Discord Webhook 수신을 위한 예외적 외부 egress 허용의 Kubernetes 측 통제(NetworkPolicy)를 다루므로, 승인 시 해당 결정과의 정합화(D-ID 갱신 또는 예외 범위 명시)가 필요합니다.
>
> 본 이슈(B)는 **Kubernetes NetworkPolicy·podSelector·Secret 관리**를 다룹니다. egress 프록시 서버 자체의 구성은 [Issue A (#74)](https://github.com/321Team/fds-project-baseline/issues/74)에서 다룹니다.

---

### Scope

#### In Scope

- Alertmanager 전용 신규 Egress NetworkPolicy 작성 (Namespace: `monitoring-api`, CNI: Calico)
- Alertmanager → 사내 egress 프록시(고정 IP) 단일 `ipBlock` 허용
- DNS egress 허용 (UDP/TCP 53, kube-dns selector로 목적지 제한)
- Discord 알림 채널 구성 (`discord_configs` 네이티브 사용, 별도 변환 파드 불필요)
- podSelector 라벨 확정 및 Secret 주입·회전·폐기 절차 수립
- 검증 계획 수립 및 실행 (허용/차단/알림 흐름)

#### Out of Scope

- egress 프록시 서버 자체의 구성·소프트웨어 선정 ([Issue A](https://github.com/321Team/fds-project-baseline/issues/74))
- Alertmanager 외 다른 Pod/서비스의 NetworkPolicy 변경
- [P1-MON-01](#17) 본 Gate의 기존 Acceptance Criteria 변경

---

## Alertmanager egress용 쿠버네티스 보안 설정

### ✅ 결정 완료

- Egress 방식: Alertmanager → 사내 egress 프록시(고정 IP) 단일 ipBlock (B안)
- DNS egress: Alertmanager 전용 신규 NetworkPolicy 필요, UDP/TCP 53 둘 다, kube-dns selector로 목적지 제한
- Namespace: `monitoring-api`
- CNI: Calico
- 알림 채널: Discord 네이티브 `discord_configs` 사용 (변환 파드 불필요)

### 확인/작업 현황 — 2026-09-18 증적 대조

- [x] [Issue A (#74)](https://github.com/321Team/fds-project-baseline/issues/74)에서 확정된 프록시 IP·포트를 NetworkPolicy `ipBlock`에 반영: 계획값 `10.1.93.56:3128`은 결정·공유됐다. 실제 서비스 인수 뒤 정책 적용·연결 검증은 잔여이며 초안 준비는 병행 가능하다.
- [x] podSelector 실제 라벨 확정: `app: alertmanager`는 가정값이다. 이관된 [infra-monitoring 참고본](https://github.com/321Team/infra-monitoring/blob/73b9432e8c793f64469ea708c14018f010ad74c1/docs/CANONICAL_GAPS.md)을 정본 배포로 간주하지 않고 실제 Pod·Manifest와 대조해야 한다.
- [x] Secret 주입·회전·폐기 절차: [기존 결정 #78](https://github.com/321Team/fds-project-baseline/issues/78)에 따라 생성/재발급 주체는 이하영, 설정 인계/검증은 이재환이다. 정기 회전 여부·주입/폐기 절차 및 검증은 잔여다. 역할 자체를 미정으로 반복하지 않는다.
- [x] 검증 계획·실행: 프록시 경유 허용 / 비승인 목적지·직접 외부 경로 차단 / 알림 발생·해소 / 전송 실패·복구를 확인한다. [#74 선행 코드의 두 엔진 localhost 회귀](https://github.com/321Team/fds-project-evidence/blob/f3b5ea69f5119fc89e15f128c086f1c8eba97fea/evidence/infra-ansible-followup/cicd-runner01-podman-20260916T110635Z/README.md)는 완료됐으나 Alertmanager→Squid→Discord 실제 결과가 아니며 운영 적용 HOLD는 유지한다.

지금 확인/결정된 보안 설정 사항들을 change request로 만들 예정입니다.
미결된 내용을 확인해보시고, 추후 이에 대한 리뷰를 요청드리겠습니다.

---

### Dependency

- 선행 기준: [Issue A (#74)](https://github.com/321Team/fds-project-baseline/issues/74) 프록시 IP·포트 확정
- 연동 기준: [P1-MON-01](#17) Alertmanager 배포 및 기존 "외부 미송신" 결정
- 참고: [P1-SEC-01](#19) 최소 egress 정책 논의

---

Related to #17, #74

