<!-- fds-canonical-live:v3.1.21 record-id:P1-SEC-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/P1-SEC-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 관련 추적 항목 **TS13**. 원본 AC와 각 항목의 환경·선행조건·중단/복구·증적 기준을 함께 적용한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:P1-SEC-01:end -->

<!-- cr126-disposition-20261002:start -->
## 2026-10-02 CR #126 최종 Disposition — WITHDRAWN / NO CHANGE

- CR-P1-SEC-01-02(#126)은 Lead 철회 및 Review Owner 재검토에 따라 **WITHDRAWN / NO CHANGE**.
- #19 SEC-AC-02 `Allow 흐름 PASS / Deny 흐름 FAIL` 원문은 변경하지 않는다.
- 기존 병합 Evidence는 동일 원본을 재사용할 수 있으나, 이 CR의 Aggregator Matrix 구조는 effective change로 적용하지 않는다.
- 원 AC 기준 미충족 흐름은 AC 삭제 없이 `NOT MET / Known Issue`로 Close Review에 인계한다.
- 정본 영향: 변경 없음. 철회 이력만 추적한다.
<!-- cr126-disposition-20261002:end -->

<!-- cr125-effective-20261001:start -->
## 2026-10-01 CR #125 승인 구조 반영 — Secret AC 처리

CR-P1-SEC-01-01(#125) Review Owner 최종 재검토 결과, 변경구조를 차기 정본 후보 입력으로 수용한다.

- Secretbox encryption / 3CP 동일 Config / etcd 원문 비노출: P1 유지
- **backup: P1 필수 / 증적 미충족**
- **rollback: P1 필수 / 증적 미충족**
- preventive rotation: P1에서 **NOT MET / RISK ACCEPTED**
- future KMS v2 rotation/compromise 교체: 실제 Receiver Record/Owner/Window/성공조건/Evidence path가 생성된 경우에만 후속 연결
- P2 수신 Record가 없으므로 현재 상태를 `P2 승계 완료`로 표현하지 않는다.
- 노출 키/DB credential은 preventive rotation과 합치지 않고 P1 Residual Risk로 별도 유지한다.

#125/#128 통합 Change Matrix 기준으로 P1 요구가 소실되는 항목은 없다.

### Acceptance 경계
이 구조 반영은 AC-05를 PASS로 올리지 않는다.
backup/rollback Runtime evidence가 확보되기 전까지 해당 항목은 NOT MET 상태이며, Phase 1 Close 시 사실 상태로 분류한다.
<!-- cr125-effective-20261001:end -->

<!-- cr127-disposition-20261001:start -->
## 2026-10-01 CR #127 최종 Disposition — NO CHANGE

- CR-P1-SEC-01-03(#127)의 B안(source-preservation을 AC-04 밖으로 이동)은 Review Owner 재딥리뷰에서 **REJECTED / NO CHANGE**.
- 기존 기준 유지: `.50/32 → Worker:30080` source-preservation은 SEC-AC-04/핵심요구4의 필수 하위조건.
- clean immutable 재수집 evidence #86은 독립 exact-head 승인·병합 완료로 Positive source-preservation 근거로 사용 가능.
- 단, #86 병합만으로 비승인 Source Negative, Edge Cutover, SEC 전체 종결을 PASS로 승격하지 않는다.
- 정본 영향: AC 축소 없음. 차기 정본에는 `CR rejected / original AC retained` 이력만 반영한다.
<!-- cr127-disposition-20261001:end -->

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23 (누락분 2026-09-25 반영)

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P1-SEC-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P1-SEC-01/`
- 이 티켓은 2026-09-23 일괄 반영(49건)의 대상 추출에서 누락되어 2026-09-25 같은 형식으로 반영했다(“Evidence Path:” 표기 없이 경로만 적힌 형식). 근거: `audit/phase2-repo-bootstrap-20260923/evidence-path-followup-20260925/`.
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

## 현행 보호 전환·보안 후속 검수 — 2026-09-23 KST

[전체 대조표·후속](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5794357232). 과거 “보호 미적용/모든 Runtime 미실시” 기록은 현재 상태를 대표하지 않는다.

- **적용 보고 확보:** [Gate2 실행 문서](https://github.com/321Team/infra-kubernetes/blob/2d35809313c70731c58d210b37ef29ed0a300883/docs/evidence/P1-SEC-01/GATE2_RUNTIME_EXECUTION_20260922.md)에 6대 firewalld disabled/inactive, HEP 6개(ens160)·GNP 6개, Namespace/PSA·LimitRange·RBAC·NetworkPolicy·3CP Secretbox 최초 구성 기록이 있다. [Gate2 네트워크 시나리오 9/9](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5772355948) 보고도 연결한다. 실제 적용 v4와 PR7 후보의 일치·전체 SEC AC 인수는 별도다.
- **현재 기능 실패:** [Prometheus 9100/10250 실측 보고](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5788504815)를 반영한다. node-exporter 1/3 UP 및 kubelet/cadvisor 6대 DOWN. worker03 IP SAN 오류와 교차 노드 timeout을 분리하며 GNP deny/actual source 대조 전 원인을 확정하지 않는다. 최소 승인 Prometheus 범위와 비승인 Workload 차단을 함께 검증한다.
- **NodePort 후속:** [PR21](https://github.com/321Team/infra-kubernetes/pull/21) HEAD a85536c6732acd48228dd4e40adc2cf425f696b6에는 worker selector와 order 50, preDNAT/applyOnForward, .50/32 Allow/나머지 30080 Deny가 이미 반영돼 있다. 설명의 “selector 미확인”을 정정했다. Draft/open·제출 리뷰 0건, 실제 승인/비승인 통신 및 복구는 미인수.
- **Secretbox 코드 잔여:** PR7 현 HEAD 2d35809313c70731c58d210b37ef29ed0a300883에서 기존 B1~B4는 미해소. 이후 변경 3파일은 Gate2 문서·namespace·securitycontext이며 회전 스크립트는 그대로다. [9/22 제한 리뷰](https://github.com/321Team/infra-kubernetes/pull/7#pullrequestreview-5276138112)와 다른 제한 범위 APPROVED를 전체 스크립트 승인으로 확대하지 않는다.
- **비밀정보 후속:** Gate2 문서에 보고된 Secretbox 키·DB 비밀번호 노출 후 교체 결과와 CP1 history 정리 결과는 미확인. SEC Lead 이하영/DB Lead 이재환의 기존 범위에서 회전·정리 결과를 연결한다. 최초 암호화 성공은 안전한 키 회전·backup·rollback의 증거가 아니며 비밀값 제출은 요구하지 않는다.
- [MON PR7](https://github.com/321Team/infra-monitoring/pull/7)는 앱 namespace 참조만 수정한 CI 성공 후보다. 정책/serving 인증서 문제를 해결한 것으로 기록하지 않는다. 기존 담당·계획·open 상태와 완료 체크는 유지하며 현재 증거를 부분 실적으로 반영한다.

---

<!-- icr-management-recovery-20260921T140152:issue-19:start -->
## 호스트 관리 통신 회복·SEC-06 후속 연결 — 2026-09-21 14:01 KST

[ICR 원본·검증](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5755742235): CP3→Node6 TCP10250 18/18(13:43), 이번 /32 source→/32 destination TCP10250 규칙13개 영구 저장(13:59–14:00), 직접 API3×etcd Pod3 관리 기능27/27(14:01) 성공. ICR-AC08은 현재 구성에서 RUNTIME_PASS이며 SEC 전체 통제의 인수는 아닙니다.

[PR7](https://github.com/321Team/infra-kubernetes/pull/7)은 이번 조회에서도 open/미병합, HEAD `7a840cf013be61e5891c4848f8732d4358208423`입니다. 확인한 [Bootstrap 정책](https://github.com/321Team/infra-kubernetes/blob/7a840cf013be61e5891c4848f8732d4358208423/manifests/calico/01-bootstrap-allow.yaml)의 LB .109 명시 허용 누락, order:0/applyOnForward:true 및 6노드 상호 포트 범위에 관한 기존 SEC-06 잔여를 이 결과로 해소 처리하지 않습니다.

**다음:** 이하영(K8S/SEC)이 정책·manifest 보완/검토 및 API 적용을, 이권욱(ICR)이 호스트 방화벽 전환·관리/반환 경로·허용/차단·복구 검증을 공동 작업창에서 연결합니다. 확보한 정상 경로를 전환 회귀의 기준으로 재사용합니다. 현재 firewalld 유지와 최종 HEP/GNP 보호 전환은 별개이며, 비승인 Source 차단·Prometheus CA+SA·재부팅·Secretbox 등 기존 SEC AC는 유지합니다. NTP 구축/공식 검증의 담당이나 승인 범위를 이 갱신으로 이전하지 않습니다. 담당·일정·상태·리뷰 승인/병합 상태 유지.
<!-- icr-management-recovery-20260921T140152:issue-19:end -->

---

<!-- monitor01-approved-merged-20260920:issue-19:start -->
## 독립 승인·병합 완료 — 2026-09-20 KST

- [x] [PKI 증적 PR 321Team/fds-project-baseline#18](https://github.com/321Team/fds-project-evidence/pull/18): 이재환/supreme33-kr가 HEAD `74745237108830e0c19912e960b2e26f0957f04b`를 [독립 승인](https://github.com/321Team/fds-project-evidence/pull/18#pullrequestreview-5260358774). **22:57:30 KST 병합**, merge `c97b13fa2910f740582076f7e7b56f0da42ddf31`.
- [x] [TLS 구성 후보 PR 321Team/fds-project-baseline#3](https://github.com/321Team/infra-monitoring/pull/3): 같은 독립 검토자가 HEAD `05a8114308c510c678efd64b3443c133c36ab66f`를 [승인](https://github.com/321Team/infra-monitoring/pull/3#pullrequestreview-5260362147). **22:57:47 KST 병합**, merge `e520358bb0e4739762511f1a6b3cd7d8b83c57ae`.
- [x] 승인 후 HEAD 변경 없음·미해결 리뷰 스레드 0건 확인. 병합 tree 전체의 path/mode/blob이 승인 tree와 일치(증적 696파일·MON 47파일). [MON main CI](https://github.com/321Team/infra-monitoring/actions/runs/35515026751) **SUCCESS**, 위 merge SHA의 push 실행 확인.
- [ ] 실제 배포 입력 확정·native parser/서비스 통합·TLS/Auth/IF-06B/Blackbox 현장 인수.

이번 사용자 “후속 작업 착수” 지시로 정확한 승인 HEAD를 지정하여 두 PR을 수동 병합했습니다. 증적 PR의 CI 검사 0건은 NOT RUN이며 기존 무결성 검증·독립 편입 검토와 구분합니다. 아래 과거 Draft·리뷰/병합 대기 표현은 당시 이력입니다. PKI 현장 검증 완료 범위와 AC·티켓 상태·담당·일정은 유지합니다.

**SEC 영향:** 코드의 독립 검토 완료를 반영합니다. payload 제한은 sender relabel이며 proxy의 protobuf 본문 검사 또는 유효 인증정보 보유자의 비허용 payload 차단은 입증하지 않았습니다. 실제 Secret/Root 참조·권한과 TLS/Auth·허용/거부 인수는 잔여입니다.

실제 입력 항목과 실행/중단/복구 순서는 [MON 321Team/fds-project-baseline#17](https://github.com/321Team/fds-project-baseline/issues/17)의 최신 인계표에 모았습니다.
<!-- monitor01-approved-merged-20260920:issue-19:end -->

---

<!-- monitor01-progress-sync-20260919:issue-19:start -->
## monitor01 PKI 검증·TLS 보안 검토 인계 — 2026-09-19

진행 체크는 이번 하위작업의 완료 범위이며 기존 요구사항·AC 합격 체크와 구분합니다. 기존 담당·일정·티켓 상태와 과거 기록은 유지합니다. 아래의 서명 전·반환 전 표현은 작성 당시 이력이며 이 갱신을 최신 기준으로 읽습니다.

- [x] monitor01 IP SAN `10.250.10.30`·serverAuth 인증서 발급/공개 반환과 원본 SHA256 2/2 확인. 현지 키 일치 및 체인·IP·서버 목적 검증 PASS. CA 볼륨 unmount/비활성 확인(전원 OFF 미확인). 근거: [PKI 증적 PR 321Team/fds-project-baseline#18](https://github.com/321Team/fds-project-evidence/pull/18).
- [x] 보안 검토 가능한 TLS 수신·송신 구성 후보 확보: [TLS 구성 후보 PR 321Team/fds-project-baseline#3](https://github.com/321Team/infra-monitoring/pull/3), HEAD `05a8114308c510c678efd64b3443c133c36ab66f`. 정적/단위시험 및 [CI #35442097555](https://github.com/321Team/infra-monitoring/actions/runs/35442097555) SUCCESS.
- [ ] NGINX/Basic Auth 후보의 독립 코드 검토와 실제 Source·인증정보/Secret·Root mount·권한·실행 버전 입력 확정. NGINX/Basic Auth는 이번 구현 제안으로, 이미 승인된 방식으로 기록하지 않음.
- [ ] TLS·인증·Source/경로 허용 및 거부·heartbeat 단절/복구 실제 검증과 SEC 인수.

**검토 경계:** 후보는 Source 제한·인증·정확한 POST 경로와 송신 측 heartbeat-only relabel을 제공합니다. proxy는 protobuf 본문을 검사하지 않으므로 유효한 인증정보를 가진 다른 송신자의 비허용 payload까지 receiver가 차단한다고 판정할 수 없습니다. 이 차이를 독립 검토에서 다룹니다.

구성 PR 321Team/fds-project-baseline#3·증적 PR #18은 모두 open/Draft·제출 리뷰 0건·미병합입니다. 기존 SEC 부분 수용/AC, HEP/GNP·Secretbox 등 다른 잔여는 유지하며 PKI 검증을 정책 적용·전체 SEC 완료로 확대하지 않습니다. 연계: [MON 321Team/fds-project-baseline#17](https://github.com/321Team/fds-project-baseline/issues/17) · [ICR 321Team/fds-project-baseline#14](https://github.com/321Team/fds-project-baseline/issues/14).
<!-- monitor01-progress-sync-20260919:issue-19:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 기존 SEC-01~08 부분 수용 유지. 현재 HEAD·키/오류판정/최종 보호·실제 render 입력 ; A05/A06/R03.

- SEC PR #7의 해소된 Service80→8000·MON DNS·HEP 파일 분리·주소/방향 등은 재요구하지 않는다. 키 실제 로드/복호화·비밀파일/구키 제거, API/exec/Endpoint/RBAC 오류 판정, 최종 HEP 보호·복구와 실제 APP/MON render/Runtime 잔여를 해당 PR에서 추적한다.

**NTP 실행·인수 입력 (A01)** — 승인 시간 소스·운영 주체, 노드별 Source/Return·UDP123, 허용 오프셋·표본 주기/횟수·실패 처리·지속성 결과를 확정한다. `100ms·60초×6`은 미승인 초안이다. 해당 변경/인수 전 입력이며 읽기 전용 준비 전체의 신규 중단 조건이 아니다.
근거: [ICR 321Team/fds-project-baseline#14](https://github.com/321Team/fds-project-baseline/issues/14) · [K8S 321Team/fds-project-baseline#10](https://github.com/321Team/fds-project-baseline/issues/10) · [SEC 321Team/fds-project-baseline#19](https://github.com/321Team/fds-project-baseline/issues/19)

**정본 Monitoring 배포 입력 (A05)** — 현재 main의 prometheus.yaml은 임시 fds/업무포트·latest·emptyDir 설정이며 “실6Node의 Prometheus는 monitor01” 주석은 현행 정본과 다르다. E-K3S 참고와 E-CANON 적용 source/overlay·render SHA를 구분한다. monitoring-api/monitoring-node·metrics9091/9090·고정 Digest·SA와 3종 PVC의 SC/PV/Worker/host path/용량/UID/fsGroup·Resource 인계를 기록한다. WaitForFirstConsumer·Retain·15일 목표/PVC80% 상한은 이미 정해진 값이다.
근거: [MON 321Team/fds-project-baseline#17](https://github.com/321Team/fds-project-baseline/issues/17) · [현재 Prometheus 소스](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/kubernetes/monitoring/prometheus.yaml)

**OID·IF-06B 경로 인계 (A06)** — OID-01 관리자 Source/Identity, OID-02 CP/Calico/system image source/Digest·pull 경로, OID-03 bootstrap 반입 또는 최소 HTTPS 목적지/Owner/Expiry를 해당 실행 전에 확정한다. IF-06B는 in-cluster Prometheus→monitor01 10.250.10.30:443으로 주소/방향이 확인됐다. 실제 Source/Return·TLS path/auth·Secret 참조·self-metric allowlist와 긍정/부정 결과가 필요하다. heartbeat=1·5분 단절 탐지는 확정값이며 OID-04 관리망 DNS N/A를 확대하지 않는다.
근거: [ICR 321Team/fds-project-baseline#14](https://github.com/321Team/fds-project-baseline/issues/14) · [MON 321Team/fds-project-baseline#17](https://github.com/321Team/fds-project-baseline/issues/17) · [SEC 부분 수용](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5654476728)

**인계·관련 티켓:** [#10](https://github.com/321Team/fds-project-baseline/issues/10) · [#14](https://github.com/321Team/fds-project-baseline/issues/14) · [#15](https://github.com/321Team/fds-project-baseline/issues/15) · [#17](https://github.com/321Team/fds-project-baseline/issues/17).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 321Team/fds-project-baseline#24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-SEC-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-SEC-01 -->
# P1-SEC-01 — Kubernetes Security Controls

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-SEC-01 |
| Phase | Phase 1 |
| Category | Security / Kubernetes |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-04 |
| End | 2026-09-21 |
| Calendar Days | 18 |
| Working Days | 10 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | PSA/SecurityContext/Default Deny/RBAC/HEP-GNP/Secretbox/LimitRange/Probe와 `.50/32→30080` 포함 Positive·Negative·Rollback Evidence PASS |
| Related Decision IDs | D12; D17; D18; D19; D27; D31; D34 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08 |
| Source | Baseline/Ticket Pack v3.1.18; GitHub 321Team/fds-project-baseline#19; K8S PR 321Team/fds-project-baseline#2 097ddb5, 321Team/fds-project-baseline#3 merge 7d44afc, 321Team/fds-project-baseline#4 75d476e; audit/v3.1.18/k8s-intake-20260910.json; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 09-10 휴가 추가 후 기존 09-04~11 가용일은 4일. 권장 종료 09-21로 확장한 전체 계획창의 가용일은 10일이며 잔여 공수를 뜻하지 않는다. Runtime 검증은 플랫폼·앱 인수와 연계한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **In Progress / open**. 원본 갱신 시각: `2026-09-11T00:14:08Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.
- 수집된 운영 댓글은 원래 위치에 보존한다. 신규 구현 제출/리뷰 요청은 실행 PASS나 승인으로 간주하지 않는다.
  - [5613475033](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5613475033) · 2026-09-10T05:05:52Z
  - [5627308483](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5627308483) · 2026-09-11T00:13:48Z
  - [5627311915](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5627311915) · 2026-09-11T00:14:08Z
- 최신 제출본의 후속 검토와 Runtime 인수는 계속 별도 진행한다. 기존 6개 Runtime AC와 완료 HOLD를 유지한다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

Manifest/Prework GO와 In Progress를 유지한다. D17/D34 설계 승인과 별도로 Runtime AC는 PASS 0 / FAIL 0 / NOT VERIFIED 6, 완료 HOLD다. PR 321Team/fds-project-baseline#2 현장 증적에서 CP1 Calico Running·firewalld active·HEP/GNP 각각 0을 확인했다. Worker Cockpit socket/service 6 unit mask·9090 listener 부재는 보완 증적 PASS이나 잔여 방화벽 허용 제거·CP 포함 전체 Gate 0는 별도다. PR 321Team/fds-project-baseline#3 수집기 병합 및 PR 321Team/fds-project-baseline#4 75d476edc33d6368fe4ab07e78fc51759e81a6fc Runtime 전용 보완/74개 로컬 모의시험 기록을 연결하되 실제 보호 전환·차단·회귀·재부팅·복구 인수로 확대하지 않는다. 최신 HEAD 독립 리뷰, 실제 보호·콘솔·백업·복구·변경창 확인, NTP 승인 egress와 전체 Platform Ready가 남는다. 현재 후보 Plan: 2026-09-04 ~ 2026-09-21 (조건부 목표).

근거: [Issue 321Team/fds-project-baseline#19](https://github.com/321Team/fds-project-baseline/issues/19), Issue 갱신 시각 `2026-09-10T05:05:52Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 2026-09-10 K8S 최신 이력 통합

- PR 321Team/fds-project-baseline#2: 실행 source `afc246d2db041c68de5014972107484dad122558`, 증적 편입 HEAD `097ddb56d87b229a9eb465f72ea9f55d16524c51`. 현장 Linux **모의시험 37/37**, CP **읽기 전용 조회 115개**의 검증 기록을 반영한다. Runtime apply/rollback 증적은 아니다.
- Worker: 15:34 KST 보완 증적에서 6대 시간 속성, Worker kubelet의 config.yaml 부재 오류, Cockpit 6 unit mask 및 9090 listener 부재를 확인했다. 같은 supplement의 추가 재수집은 잔여에서 제외한다. TCP·firewall·chrony source를 재조회한 결과는 아니다.
- PR 321Team/fds-project-baseline#3: `3309866766236bbdbe20b9e2ae1d8fd6f9233bcd`의 수집기 소스가 **Merged**, merge `7d44afc3afff4d322cb4dbeff4433d61e23e111a`. 병합을 클러스터·방화벽 운영 인수로 해석하지 않는다.
- PR 321Team/fds-project-baseline#4: 최신 `75d476edc33d6368fe4ab07e78fc51759e81a6fc`에서 최신 PR 321Team/fds-project-baseline#2 영수증·실제 인수 연결, Runtime 전용 변경/복구, 정책·상태·실행 통제를 보완했다. 로컬 Linux **모의시험 74개**(PR 321Team/fds-project-baseline#4 55+Worker 회귀 19) PASS 기록이며 새 HEAD 리뷰·실서버 검증은 미완료다. 구 소스의 계약/순서 지적은 보존하되 보완 미착수로 표시하지 않는다.
- PR 321Team/fds-project-baseline#2/#4는 이하영의 최신 HEAD 독립 리뷰와 실제 Runtime 인수가 남는다. 현재 구현은 Runtime 전용이며 Permanent 승격은 미구현이다. CP2 재개·6대 가입·etcd 3 Member·DNS/cross-node·NTP·HEP/GNP·Storage·재부팅/복구는 기존 미완료 상태다.
- 09-11의 완료된 Worker supplement 재수집 문구를 CP1 보호/복구·inspect 준비로 교체한다. PR 321Team/fds-project-baseline#2/#4 재리뷰를 연결하며 날짜·담당·배정 인일·휴가·주말 가용량·Gate/AC는 유지한다.

고정 출처·당시 본문·이전 후보 값은 `audit/v3.1.18/k8s-intake-20260910.json`, 자세한 조건은 `releases/v3.1.18/FDS_K8S_Candidate_Integration_20260910.md`에 기록한다. 이 통합은 후보 문서 갱신이며 운영 적용·정본 발행이 아니다.

### 미결 사양과 실행 조건

현재 3CP+3Worker·kubeadm·Calico·static local PV 범위를 유지한다. 추가 노드·플랫폼 도입 결정은 없다. NTP 목적지/운영 주체(#14), 동기화 수치 인수조건(#10), 최소 egress(#19)는 해당 변경·인수 전에 확정한다. `100ms·60초×6`은 미승인 초안이고 MTU 1450도 실측 확정 전 후보값이다. CP2 원래 join 단계·비표준 data 경로와 보존/정리/재개 방식은 실제 조사 후 판단한다.

발행 D34의 Calico 설치 전 firewalld OFF 이력과 실제 CP1 공존 drift를 구분한다. ADV-20260910에 따라 사유·기간·보호·복구·종료조건을 기록한 제한적 선행 준비를 이어간다. 최종 6대 firewalld disabled/inactive 및 named HEP/GNP 목표, Bootstrap Allow→canary Worker→Worker 확대→CP의 보호 전환 순서를 유지한다. CP 통신 canary가 HEP 전환 순서를 대체하지 않는다.

PR 321Team/fds-project-baseline#2 최신 HEAD 리뷰·실행 창의 inspect·보호/콘솔/백업/복구·실행 결정 후 CP1 제한 Runtime을 검증한다. 실제 CP1 인수 및 PR 321Team/fds-project-baseline#4 최신 HEAD 리뷰 후 후속 대상의 실행·복구/가입을 판단한다. Runtime 시험·리뷰 이후의 Permanent 또는 최종 보호 인계 종료 절차는 별도 결정·구현 대상이다. 승인 JSON을 실제 GitHub 리뷰 인증으로 해석하지 않는다. NTP 미결을 모든 준비의 전역 중단 조건으로 만들거나 기존 시간 동기화 선행조건을 면제하지 않는다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5613475033)

---

### User Story

Kubernetes 보안 담당자로서 D-SEC-01 승인 설계를 Manifest와 Runtime Policy로 구현하고 최소권한과 기본차단을 증명한다.

### Scope

#### In Scope

- Namespace/PSA/version label
- SecurityContext/SA/RBAC
- Workload NetworkPolicy
- Calico named HEP/GNP 및 preDNAT NodePort
- Secretbox at-rest encryption
- LimitRange/Resource presence/Probe verification
- cicd-runner-sa Role/TokenRequest 정책

#### Out of Scope

- Self-hosted Runner 설치·GitHub 등록·Service·Workflow 운영
- Application 코드와 Monitoring Workload 자체 구현
- P2 Admission Policy·Image 서명 강제·KMS v2

### 핵심 요구사항

**2026-09-23 대조:** PR7 현 HEAD 2d35809313c70731c58d210b37ef29ed0a300883와 Gate2 실제 적용 보고를 대조했다. 적용 v4·기존 PR7 후보·PR21의 범위를 구분하며 전체 요구 조건의 충족 여부를 체크한다.

- [x] kube-system enforce Privileged, audit/warn Restricted — **PARTIAL/전체 정합성 미확인**. 9/22 업무 Namespace 4개 PSA 적용과 v1.36 실측값 반영 보고 확보. kube-system 실제 label 및 승인 예외 범위는 별도 연결 필요; 과거 placeholder를 현재 업무 Namespace 미적용 근거로 사용하지 않음.
- [x] CoreDNS 실제 Manifest dry-run — **NOT_RUN**. 3CP/Calico Ready 또는 코드 파싱으로 실제 Manifest dry-run을 대신하지 않음.
- [x] monitoring-node 신규 Workload 생성 제한 — **PARTIAL**. Namespace/PSA·SA·RBAC 및 node-exporter 실제 배포 보고 확보. 비승인 신규 Workload 생성 제한 Negative 결과는 남음.
- [x] `.50/32→Worker:30080`만 preDNAT 허용 — **PARTIAL**. Gate2 NodePort 적용 보고·PR21 worker selector/order50 후보 확인. 승인/비승인 Source의 실제 Allow/Deny와 복구 인수는 남음.
- [x] Prometheus `nodes/metrics`와 `/metrics`만, `nodes/proxy`·Secret 금지 — **PARTIAL**. MON 9/23 본문에 실제 바인딩 ClusterRole 3개 조회·쓰기/Secrets 권한 0건 보고. 전체 승인 리소스/SA 권한 대응과 Positive/Negative 결과 연결은 남음.
- [x] Runner는 기존 2개 Deployment get/update/patch만 허용 — **PARTIAL**. RBAC 적용 보고와 기존 resourceNames 제한 후보는 확보. 실제 Runner RoleBinding·기존 Deployment 대상 및 긍정/부정 권한 시험은 남음.
- [ ] Secretbox key root-only, 3CP 동일 Config, etcd 원문 비노출 — **PARTIAL + 회전 코드 차단**. Gate2 최초 구성·3CP 적용·enc prefix 검증 보고를 인정한다. 현 PR7 회전 코드의 curl -sk·변경/재시작/load 증명·readOnly 강제·CP 기본값 잔여 및 키 노출 후 교체 확인은 별도 미완료.

### Acceptance Criteria

**복합 Runtime AC 전체 충족 확인은 0/6 유지하되, 실제 적용·부분 시험과 보고된 실패를 아래에 반영한다.** PR7 현 HEAD 2d35809의 제한 범위 APPROVED와 기존 B1~B4 잔여를 구분한다. 6노드 보호/Namespace·RBAC·NetworkPolicy·최초 Secretbox 구성을 미실시로 되돌리지 않으며, 최초 암호화를 rotation/rollback 인수로 확대하지 않는다.

- [x] PSA 위반 Pod 차단 — **NOT_VERIFIED**. 실제 Kubernetes Minor에 맞춘 label/render와 위반 Pod 거부 증거 필요.
- [x] Allow 흐름 PASS / Deny 흐름 FAIL — **PARTIAL / 실패 항목 포함**. Gate2 네트워크9/9와 MON 9/23 앱 NetworkPolicy 허용4흐름·fds-engine→DB 차단 보고 확보. 전체 Matrix는 미완료이며 Prometheus host 9100/10250에는 실제 실패가 남음.
- [x] SA별 `kubectl auth can-i` Positive/Negative PASS — **PARTIAL**. RBAC 적용과 MON 관련 실제 role 읽기 전용/Secrets0 확인 보고 확보. 각 SA에 대한 can-i yes/no·rc 전체 증거는 별도 연결 필요.
- [x] NodePort/9100/10250 HEP/GNP PASS — **FAIL 항목 포함 / 전체 미충족**. HEP/GNP·NodePort 적용 보고 및 PR21 후보 확보. node-exporter 1/3 UP·2 timeout, kubelet/cadvisor6대 DOWN(동일 노드 TLS IP SAN·교차 노드 timeout)으로 9100/10250 조건 미충족. actual source/정책 대조 후 조치·비승인 Workload 차단 인수 필요.
- [ ] Secret encryption·backup·rotation·rollback PASS — **PARTIAL / rotation NOT MET·RISK ACCEPTED(P1, 이권욱 확인 https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5846722659)**. 최초 Secretbox 3CP 구성·암호화 prefix 보고 확보. B1~B4 회전 코드, 노출 후 안전한 교체, 새 키 load/복호화·backup·rollback 증거는 남음.
- [x] Probe 장애 주입과 Endpoint 제외 PASS — **NOT_VERIFIED**. Endpoint 제외/복원 assert 후보를 실제 APP/MON에 실행한 증거 미확보.

### Evidence

- `321Team/fds-project-evidence:evidence/P1-SEC-01/`
- 비밀정보는 fingerprint 또는 마스킹만 기록

### Dependency

- Blocked By Runtime: P1-K8S Platform Ready
- Related: ICR-D-NET-01-01, P1-APP, P1-MON, P1-CICD

### Decision / Risk Control

- Decision: D17/D34와 D-SEC-01 v1.0을 구현 기준으로 사용한다.
- Risk Control: HEP/GNP는 Bootstrap Allow와 canary를 먼저 적용하고 Secretbox key는 Git/Evidence에서 제외한다. Deployment patch 우회 위험은 P1 Residual Risk로 유지한다.

### Review / Handoff

- Review Owner: 이권욱, 이재환
- Handoff: SA/RBAC/TokenRequest 정책은 P1-CICD에, Probe·Resource 검증 결과는 P1-APP/P1-MON에 전달한다.

### Completion Record

- Result: IN PROGRESS — HEP/GNP·PSA/RBAC/NetworkPolicy·최초 Secretbox 적용 보고 확보. 전체 SEC AC 0/6, 부분 검증/9100·10250 실패 및 키 회전·노출 후속 잔여.
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: Review Owner 이권욱·이재환 / Runtime 승인 미완료

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `b58be1e2b305c25a2d5aef6c34126315b2c53dd9bdda6a47da6f1d799386081a`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-pr2-onsite-verified-20260910:start -->
### 2026-09-10 현장 증적 검증 완료 — Runtime 인수 별도

PR #2의 현장 테스트37/37과 읽기 전용 수집 증적을 검증해 `097ddb56d87b229a9eb465f72ea9f55d16524c51`에 편입했습니다. 현재 CP1 Calico Running + firewalld active + HEP/GNP0을 다시 관측했습니다. IPPool의 VXLAN CrossSubnet·IPIP Never·natOutgoing=true만 확인했으며 BGP/MTU·전체 D34 인수로 확대하지 않습니다.

Lead 이하영 및 Support 이권욱·이재환이 #14의 보호/복구·관리/CNI 검토를 이어 진행합니다. Runtime apply/rollback·보호 인계·SEC AC는 미완료이며 기존 Manifest/Prework GO와 Runtime 조건부 판정을 유지합니다.

[현장 검토서](https://github.com/321Team/infra-kubernetes/blob/097ddb56d87b229a9eb465f72ea9f55d16524c51/docs/change/ICR-D-NET-01-01/ONSITE_REVIEW_20260910.md) · [Linux 실행 기록](https://github.com/321Team/infra-kubernetes/blob/097ddb56d87b229a9eb465f72ea9f55d16524c51/docs/change/ICR-D-NET-01-01/ONSITE_TEST_20260910.json) · [점검 요약](https://github.com/321Team/infra-kubernetes/blob/097ddb56d87b229a9eb465f72ea9f55d16524c51/docs/change/ICR-D-NET-01-01/ONSITE_INSPECTION_SUMMARY_20260910.json)

아래 “현장 실행 미확보” 문구는 이전 시점 이력이며 위 최신 증적 상태를 적용합니다.
<!-- fds-pr2-onsite-verified-20260910:end -->

<!-- fds-pr2-remediation-20260910:start -->
## 2026-09-10 최신 후속 — 사용자 선행 허용·PR 321Team/fds-project-baseline#2 보완

사용자 지시에 따라 정당한 차이의 v18 발행 전 선행 준비를 허용하고 [선행 변경 기록 ICR-D-NET-01-01-ADV-20260910](https://github.com/321Team/infra-kubernetes/blob/afc246d2db041c68de5014972107484dad122558/docs/change/ICR-D-NET-01-01/ADVANCE_CHANGE_RECORD_20260910.md)에 근거·범위·위험·종료조건을 기록했습니다. 현행 v3.1.17과 기존 AC·Done 이력은 유지합니다. [PR 321Team/fds-project-baseline#1](https://github.com/321Team/infra-kubernetes/pull/1)은 `08b32e7`로 병합했고, [PR 321Team/fds-project-baseline#2](https://github.com/321Team/infra-kubernetes/pull/2) 새 HEAD는 `afc246d2db041c68de5014972107484dad122558`입니다.

- SEC Lead 이하영 / Support 이권욱·이재환: 공존 중인 CP1의 관리·CNI 보호 및 복구 검토를 #14와 연결합니다. HEP/GNP 0이라는 과거 관측을 승인된 보호 상태로 소급하지 않습니다.
- PR #2는 Runtime 6개 후보만 변경하며 Permanent 쓰기·승격 기능을 제거했습니다. 새 HEAD 37/37 로컬 모의 테스트 PASS는 보호·보안 Runtime AC PASS가 아닙니다.
- named HEP/GNP, Bootstrap Allow→canary Worker→Worker 확대→CP, 6대 firewalld disabled/inactive 최종 목표를 유지합니다. 공존의 대상·기간·보호/복구·종료조건은 실제 증적과 검토가 필요합니다.
- PR 321Team/fds-project-baseline#4 구 v1 receipt·Permanent 선반영 계약은 후속 수정 전 적용 보류입니다. Worker unit mask 증적과 방화벽 예외 제거, IF-12B와 IF-06 인수를 각각 구분합니다.

현재: **Manifest/Prework GO / Runtime 조건부 / SEC AC 미완료 유지**. 아래 기존 HEAD·보류 범위는 당시 이력입니다.
<!-- fds-pr2-remediation-20260910:end -->

<!-- fds-canonical-audit-20260910:start -->
### 2026-09-10 정본 정합성 후속 — 보호 인수 미완료

[PR 321Team/fds-project-baseline#2](https://github.com/321Team/infra-kubernetes/pull/2)·[PR 321Team/fds-project-baseline#4](https://github.com/321Team/infra-kubernetes/pull/4)의 D34 전환 순서 및 ICR v1.4 Runtime→시험·리뷰→Permanent 순서 불일치를 확인하여 현재 HEAD의 운영 적용 가능 판정을 보류했습니다. 상세 수정 항목 CA-01~07은 [#14](https://github.com/321Team/fds-project-baseline/issues/14)에 기록했습니다.

09/10 11:30 KST CP1 원본 로그는 calico-node 1/1 Running + firewalld active + HEP 0/GNP 0입니다. 이 시점의 보호 인계는 미완료이며 최신 상태 재관측이 필요합니다. 즉시 firewalld OFF로 소급 정합화하지 않습니다. Worker 3대의 15:34 KST Cockpit unit mask·9090 부재 증적은 유지하되, 이를 방화벽 예외 제거 또는 HEP/GNP 인수로 확대하지 않습니다. IF-12B CP→Node 10250과 IF-06 Prometheus→9100/10250도 별도 인수입니다.

NTP 목적지·운영 주체는 321Team/fds-project-baseline#14, 동기화 인수조건은 #10과 연계하며 승인값이 확정된 뒤 최소 egress 정책에 반영합니다. 현재 보안 AC·G2·기존 Done 판정은 변경하지 않습니다. 상세 결과서: `FDS_Canonical_Alignment_and_Followup_Review_20260910_v1.0.md`.
<!-- fds-canonical-audit-20260910:end -->

<!-- fds-notion-migration:2026-09-09 record-id:P1-SEC-01 -->
# P1-SEC-01 — Kubernetes Security Controls

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

<!-- fds-cp-followup-20260910:start -->

### 2026-09-10 후속 구현 착수 결과

[infra-kubernetes PR 321Team/fds-project-baseline#4](https://github.com/321Team/infra-kubernetes/pull/4)에 Worker의 기존 Cockpit mask를 보존하면서 잔여 방화벽 예외를 제거·복구하는 결합 변경을 준비했습니다. 31/31 로컬 모의 검증 PASS, 실제 제거·보호 전환은 미실행입니다. 기존 Worker mask 증적과 runtime/permanent 예외 제거 증적을 구분합니다. NTP 승인 목적지 결정과 Calico HEP/GNP·Positive/Negative·관리 경로·복구/재부팅 인수는 별도 조건이며 현재 보안 AC 판정은 유지합니다.


### 2026-09-10 15:34 KST — Worker 보완 증적 검증 완료

- [PR 321Team/fds-project-baseline#3 최신 검토 기록](https://github.com/321Team/infra-kubernetes/pull/3): **보완 증적 기술 검증 PASS / 운영 인수 HOLD 유지**. 내부 8/8 체크섬 및 6대 identity·실행 소스 일치, 24개 조회 rc=0·잘림/누락 0.
- 6대 Asia/Seoul·NTPSynchronized=yes 및 시간 속성 확보. Worker 3대 kubelet 오류 원인·Cockpit 마스크 상태 확인 완료. 본 보완 범위의 추가 재수집은 불필요.
- Worker 3대 cockpit.socket/service 총 6개 unit의 LoadState·UnitFileState=masked, inactive/dead 및 9090 미리스닝 확인. Worker 마스크 증적 부족은 해소.
- 이전 방화벽 Cockpit 잔여 허용 제거는 #14에 유지. CP 포함 전체 노드 Cockpit 검증 및 HEP/GNP·기존 6개 SEC Runtime AC 완료로 확대하지 않음. 전체 Runtime 인수 HOLD 유지.
- 다음은 PR 321Team/fds-project-baseline#2 이하영 리뷰, 적용 창의 최신 CP1 입력·canary 검증, 후속 노드 통신·가입/인수 단계. PR 321Team/fds-project-baseline#2/#3 소스는 이번 검토로 변경하지 않았으며 승인·병합·Runtime 적용·티켓 종결은 수행하지 않음.
- 배포 검토서: `FDS_Worker_Supplement_Review_20260910_v1.0.md`. 기존 제출 전·미수집 상태 기록은 아래 이력으로 보존하며, 본 항목의 최신 상태를 우선 적용.


### 2026-09-10 — Worker 제출 증적 검토 및 제한 보완

- [PR 321Team/fds-project-baseline#3 검토 기록](https://github.com/321Team/infra-kubernetes/pull/3): 제출 archive/내부 8개 체크섬 및 6대 identity 확인. **무결성 PASS / 증적 완전성 PARTIAL / 운영 인수 HOLD**.
- 99개 query rc=0이나 6대 시간 속성 출력이 비어 있었음. 수집기 결함을 v1.1에서 수정하고 필요한 시간·Worker 진단만 보완하는 supplement 모드를 준비. 로컬 테스트 19/19 PASS, 수정본 실서버 실행은 남음.
- Worker 3대에 Cockpit 서비스의 방화벽 허용이 남아 있으나 현재 listener는 없음. socket/service mask 여부는 이번 범위에서 미수집으로, 321Team/fds-project-baseline#10 Gate 0·#14 허용 정리와 연결해 보완 필요.
- Worker kubelet 연결 실패·listener 부재 및 고정 NTP 결정 미완료를 보호 인계의 선행 미완료 항목으로 연결. 기존 SEC Runtime AC의 상태·개수는 이 수집으로 변경하지 않음.
- Worker→LB TCP 연결 3/3 성공은 이번 범위의 부분 증적이며 전체 클러스터·보안 AC 완료 근거가 아님. PR #2는 이하영 리뷰 요청 상태를 유지하며 해당 소스는 변경하지 않음.
- [현재 잔여 작업·담당 및 보완 범위](https://github.com/321Team/infra-kubernetes/blob/3309866766236bbdbe20b9e2ae1d8fd6f9233bcd/docs/change/ICR-D-NET-01-01/RESIDUAL_WORK_20260910.md). Runtime 변경·승인·병합·티켓 종결 미실행.

## 진행 업데이트 — 2026-09-10 호스트 보호 선행상태

근거: 2026-09-10 11:30:59 KST 수집본 `FDS_CP_Log_Collection_glrr0dsq.tar.gz`, SHA-256 `265e7d3fe04c8c215b8c76847bac769c5445682d788c3f9ad2bf9afef100c594`. 압축파일 및 내부 8/8 체크섬 일치. [고정 검토서](https://github.com/321Team/infra-kubernetes/blob/8975ca0c45dd9aee6d4930b16315223f86215e1d/docs/change/ICR-D-NET-01-01/CP_LOG_REVIEW_20260910.md).

CP1의 Calico node/컨트롤러는 Running이나 HostEndpoint와 GlobalNetworkPolicy는 각각 0개다. CP 3대 firewalld는 active이며, 조회한 클러스터에는 CP1 한 대만 Ready다. 따라서 named HEP/GNP, NodePort/9100/10250 Positive·Negative 및 보호 인계 AC는 미완료다.

최소 CP 통신 보완은 [#14](https://github.com/321Team/fds-project-baseline/issues/14) / [infra-kubernetes Draft PR 321Team/fds-project-baseline#2](https://github.com/321Team/infra-kubernetes/pull/2)에서 착수했다. 이 계획의 테스트 PASS는 보안 정책 Runtime PASS를 뜻하지 않는다.

**후속:** 이하영 Lead, 이권욱·이재환 Support가 #10의 클러스터 준비와 #14의 변경 범위를 인계받아 Bootstrap Allow, named HEP/expectedIPs, 승인 Source·비승인 Source, 관리/클러스터 기능 및 복구 시험을 확인한다. 보호 정책 준비와 검증 전에 firewalld를 일괄 중지하는 실행으로 이어가지 않는다. **`In Progress`로 전환하되 Runtime AC 미완료 상태를 유지한다.**
### 선행 도구 진행 연계 — 2026-09-10

#14의 CP1 점검·제한 적용·복구 도구를 [PR 321Team/fds-project-baseline#2, HEAD `0325ee798ef7bdc4e6dc582362043d899c1f3641`](https://github.com/321Team/infra-kubernetes/pull/2)에 추가했다. 로컬 테스트 25개 PASS이며 현재 단계는 읽기 전용 점검 결과 확보다. 실서버 미적용, HEP/GNP 및 Positive/Negative·보호 인계 AC 미완료 상태를 유지한다.

<!-- fds-cp-followup-20260910:end -->

<!-- p1-sec-review-sync-20260910:start -->
## 리뷰·진행상황 동기화 — 2026-09-10

### 근거 구분

| 구분 | 확인 결과 | 현재 효력 |
|---|---|---|
| D-SEC-01 6차 리뷰 | 2026-09-01 초기 판정은 `Revision Required / In Review` | 후속 D17/D34 승인으로 대체됨 |
| D-SEC-01 최종 승인 | [#7](https://github.com/321Team/fds-project-baseline/issues/7): 2026-09-01 `Done / PASS`, 정본 v3.1.14 반영 후 v3.1.17에서 유지 | P1-SEC-01 설계·Scope 선행조건 해소 |
| P1-SEC-01 착수 범위 | `Manifest/Prework GO / Runtime Platform Ready 조건부` | 문서·Manifest·검증 준비 진행 가능 |
| Runtime 선행조건 | [P1-K8S-01 321Team/fds-project-baseline#10](https://github.com/321Team/fds-project-baseline/issues/10)은 In Progress이며 전체 3CP+3Worker Platform Ready 미완료 | Runtime 적용·Acceptance 완료 차단 |
| 호스트 보호 연계 | [ICR 321Team/fds-project-baseline#14](https://github.com/321Team/fds-project-baseline/issues/14) / [infra-kubernetes PR 321Team/fds-project-baseline#2](https://github.com/321Team/infra-kubernetes/pull/2)에서 읽기 전용 점검·제한·복구 도구 준비 | Prework 진행 근거이며 HEP/GNP Runtime PASS는 아님 |

### 현재 판정

- **Ticket Status:** `In Progress / Open`
- **Implementation Gate:** `Manifest/Prework GO / Runtime 조건부`
- **Runtime Acceptance:** `PASS 0 / FAIL 0 / NOT VERIFIED 6`
- **완료 판정:** `HOLD / NOT READY` — 실제 적용·Positive/Negative·Rollback Evidence 확보 전 `Done` 금지

`In Progress`는 설계 승인 이후 Manifest/Prework와 선행도구 연계가 실제 진행된 상태를 나타낸다. P1-K8S Platform Ready 미완료와 보안 Runtime 증적 부재는 착수를 취소하는 사유가 아니라 Runtime 적용 및 `Done` 전환의 차단사항이다.

### Acceptance Criteria 현황

| AC | 검증 대상 | 상태 | 남은 증적 |
|---|---|---|---|
| SEC-AC-01 | PSA 위반 Pod 차단 | NOT VERIFIED | 실제 Kubernetes Minor에 맞춘 PSA label 및 위반 Pod 거부 결과 |
| SEC-AC-02 | Allow 흐름 PASS / Deny 흐름 FAIL | NOT VERIFIED | Default Deny와 승인·비승인 통신 Matrix 실행 결과 |
| SEC-AC-03 | SA별 `kubectl auth can-i` Positive/Negative | NOT VERIFIED | App/Monitoring/CI SA 최소권한 실제 결과 |
| SEC-AC-04 | NodePort/9100/10250 HEP/GNP | NOT VERIFIED | named HEP/expectedIPs, preDNAT, canary 및 복구 결과 |
| SEC-AC-05 | Secret encryption·backup·rotation·rollback | NOT VERIFIED | 3CP secretbox 구성과 etcd 원문 비노출·복구 결과 |
| SEC-AC-06 | Probe 장애 주입과 Endpoint 제외 | NOT VERIFIED | App/Monitoring Probe 장애·회복 Runtime 결과 |

### 책임 및 인계

- **Lead 이하영:** P1-SEC-01 Manifest/Policy 구현, 보안 Runtime Test Matrix와 Evidence 취합.
- **Support/Review Owner 이권욱·이재환:** 정본·Interface 영향성, Positive/Negative/복구 증적 검토.
- **P1-CICD-01 인계:** P1-SEC-01은 SA/RBAC/TokenRequest·TTL 정책을 제공하고, P1-CICD-01은 Token 주입·갱신·로그 마스킹을 검증한다.
- **P1-APP/P1-MON 인계:** SecurityContext, ServiceAccount, NetworkPolicy, Probe 및 metrics 권한 계약을 실제 Workload와 공동 검증한다.

### 다음 조치

- [ ] P1-K8S #10의 3CP+3Worker Platform Ready 및 실제 Kubernetes Minor 인수
- [ ] 승인된 D-SEC-01 기준의 전체 적용 Manifest와 검증 Matrix 고정
- [ ] HEP/GNP를 Bootstrap Allow → canary → 노드별 확대 순서로 적용하고 firewalld 보호 공백 방지
- [ ] PSA/SecurityContext/Default Deny/RBAC의 Positive·Negative 시험
- [ ] 3CP secretbox backup·rotation·rollback 및 etcd 원문 비노출 검증
- [ ] NodePort/9100/10250 및 Probe 장애·복구 시험
- [ ] 비밀정보를 제외한 원본 Evidence, AC Matrix 및 SHA-256 무결성 자료 제출
<!-- p1-sec-review-sync-20260910:end -->

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-SEC-01 |
| Phase | Phase 1 |
| Category | Security / Kubernetes |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-04 |
| End | 2026-09-11 |
| Calendar Days | 8 |
| Working Days | 6 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | PSA/SecurityContext/Default Deny/RBAC/HEP-GNP/Secretbox/LimitRange/Probe와 `.50/32→30080` 포함 Positive·Negative·Rollback Evidence PASS |
| Related Decision IDs | D12; D17; D18; D19; D27; D31; D34 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08 |
| Source | Baseline v3.1.15; D-SEC-01 Security Design Baseline v1.0; ICR v1.4; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 09-04 이재환 지원 부재는 이권욱이 커버한다. Lead 이하영 일정은 유지하며 D34/D35 및 P1-K8S-01 Gate 결과를 반영한다. |

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

Kubernetes 보안 담당자로서 D-SEC-01 승인 설계를 Manifest와 Runtime Policy로 구현하고 최소권한과 기본차단을 증명한다.

### 📌 Scope

#### In Scope

- Namespace/PSA/version label
- SecurityContext/SA/RBAC
- Workload NetworkPolicy
- Calico named HEP/GNP 및 preDNAT NodePort
- Secretbox at-rest encryption
- LimitRange/Resource presence/Probe verification
- cicd-runner-sa Role/TokenRequest 정책

#### Out of Scope

- Self-hosted Runner 설치·GitHub 등록·Service·Workflow 운영
- Application 코드와 Monitoring Workload 자체 구현
- P2 Admission Policy·Image 서명 강제·KMS v2

### 📋 핵심 요구사항

- [ ] kube-system enforce Privileged, audit/warn Restricted
- [ ] CoreDNS 실제 Manifest dry-run
- [ ] monitoring-node 신규 Workload 생성 제한
- [ ] `.50/32→Worker:30080`만 preDNAT 허용
- [ ] Prometheus `nodes/metrics`와 `/metrics`만, `nodes/proxy`·Secret 금지
- [ ] Runner는 기존 2개 Deployment get/update/patch만 허용
- [ ] Secretbox key root-only, 3CP 동일 Config, etcd 원문 비노출

### ✅ Acceptance Criteria

- [ ] PSA 위반 Pod 차단
- [ ] Allow 흐름 PASS / Deny 흐름 FAIL
- [ ] SA별 `kubectl auth can-i` Positive/Negative PASS
- [ ] NodePort/9100/10250 HEP/GNP PASS
- [ ] Secret encryption·backup·rotation·rollback PASS
- [ ] Probe 장애 주입과 Endpoint 제외 PASS

### 🧪 Evidence

- `docs/evidence/P1-SEC-01/`
- 비밀정보는 fingerprint 또는 마스킹만 기록

### 🔗 Dependency

- Blocked By Runtime: P1-K8S Platform Ready
- Related: ICR-D-NET-01-01, P1-APP, P1-MON, P1-CICD

### ⚖️ Decision / Risk Control

- Decision: D17/D34와 D-SEC-01 v1.0을 구현 기준으로 사용한다.
- Risk Control: HEP/GNP는 Bootstrap Allow와 canary를 먼저 적용하고 Secretbox key는 Git/Evidence에서 제외한다. Deployment patch 우회 위험은 P1 Residual Risk로 유지한다.

### 🔍 Review / Handoff

- Review Owner: 이권욱, 이재환
- Handoff: SA/RBAC/TokenRequest 정책은 P1-CICD에, Probe·Resource 검증 결과는 P1-APP/P1-MON에 전달한다.

### 📝 Completion Record

- Result: STARTED — Manifest/Prework 및 호스트 보호 선행도구 연계 / Runtime Not Verified
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: Review Owner 이권욱·이재환 / Runtime 승인 미완료
````

</details>
