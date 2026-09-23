# FDS 전체 티켓 사양·기록 점검

점검일: 2026-09-14 23:54 KST 기준 조회. 작성: Codex 점검 보조. 실제 인수·승인·서버 시험을 수행한 결과서는 아니다.

## 1. 결론과 범위

**보완할 부분이 있다.** 큰 아키텍처와 역할 분담은 정해져 있으나, 실행값·객관적 인수 기준이 미결인 부분과 결정·구현·정본이 서로 다른 시점을 보여 주는 부분이 남아 있다. 아래 13개 보완 묶음은 새 결함 13건이라는 뜻이 아니다. 이미 추적 중인 미결 사항, 이번 대조에서 확인한 상충, 기록 연결 과제를 함께 정리했다.

| 점검 범위 | 결과 |
|---|---|
| 321Team 일반 Issue 전체 | 78개: Open 58 / Closed 20. 검색 incomplete_results=false |
| 저장소별 일반 Issue | baseline 67 / infra-ansible 6 / infra-db 2 / evidence 2 / infra-kubernetes 1 |
| 댓글 | 댓글 있는 Issue 21개, 총 137개 전 페이지 수집 |
| 열린 PR | 10개 본문·현재 HEAD·리뷰·댓글 대조 |
| 추가 구현 근거 | supreme33-kr/fds-msa main 및 병합 PR #2/#3, 관련 Manifest·계약·Migration·Rule 소스 |
| 담당자 | 미배정 0. 현재 Open의 Assignee는 이권욱 31 / 이하영 14 / 이재환 13 |
| 배정 정합성 | 구조화된 본문 Lead와 확인된 GitHub 계정의 불일치 없음 |
| baseline native 속성 | #78만 Issue Type·Milestone 미설정. 본문에는 Decision으로 기록됨 |
| 정본 | docs-v3.1.18, 2026-09-11 11:23:47 KST 발행. v3.1.19는 Draft 수집 단계 |

자료 우선순위는 발행 정본의 현행 사양 → 명시적인 후속 사용자 결정 → 실제 최신 PR/병합/실행 증적 → 작성 시점 기록 → 보관 원문의 순서로 대조했다. 과거 기록이 최신 운영 절로 명시적으로 대체된 경우에는 그것만으로 상충으로 집계하지 않았다. 모든 코드·서버·첨부 원본을 전수 실행 검증했다는 뜻은 아니다. 대화 검색은 일부 요약만 반환됐으므로 대화 전체와 로컬 보관물까지 누락이 없다고 보증하지 않는다.

기준: [발행 Release](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18), [고정 정본 소스](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/baseline/FDS_Project_Implementation_Baseline_v3.1.18.md), [릴리즈 정책](https://github.com/321Team/fds-project-baseline/blob/main/governance/RELEASE_POLICY.md), [계정 대응](https://github.com/321Team/fds-project-baseline/blob/main/governance/GITHUB_IDENTITY_MAP.md).

## 2. 사양·인수 조건 보완

### A01 — NTP 목적지와 수치 인수조건: 기존 미결

**관측:** #10/#14/#19와 정본 §6.6은 NTP 목적지·운영 주체·최소 egress·동기화 수치의 확정을 요구한다. `100ms·60초×6`은 명시적으로 미승인 초안이다. 프록시의 chrony 정상화는 그 호스트의 당시 상태이며 6노드 정책 확정이 아니다.

**필요 기록:** 승인 시간 소스, 운영자, Node/VM별 적용 범위, 실제 Source/Return Route 및 UDP 123 경로, 허용 오프셋·표본 주기/횟수·불합격 처리, 지속성 검증 결과. 값은 담당자가 실측과 요구 수준을 근거로 정한다.

**담당/시점:** 이권욱(#14 경로·기록) + 이하영(#10 인수조건·#19 통제), 해당 변경·최종 인수 전. NTP 미결을 읽기 전용 준비 전체의 중단 사유로 확대하지 않는다.

근거: [#14](https://github.com/321Team/fds-project-baseline/issues/14), [#10](https://github.com/321Team/fds-project-baseline/issues/10), [#19](https://github.com/321Team/fds-project-baseline/issues/19).

### A02 — CNI/MTU와 CP1 인수: 미결값과 구현 차이 구분

**관측:** BGP Disabled + VXLANCrossSubnet + natOutgoing=true는 확정이다. MTU 1450은 후보다. CP1 제한 Runtime 적용·롤백·최종 재적용과 TCP 6/6은 기록돼 있으나 이하영의 최종 CP1 ACCEPTED는 CNI 회귀 결과 전까지 보류다. 단일 CP1의 Pod/Service/DNS 시험은 cross-node MTU·최종 HEP·재부팅 검증을 대체하지 않는다.

**필요 기록:** CNI 실제 버전/이미지·설정 SHA, 실측 MTU와 경로 시험, 선택 모드 유지 또는 변경 근거, CNI trial 결과와 최종 CP1 인수 회신. CP2 원래 join 실패 단계·비표준 data 경로의 보존/정리/재개 판단도 아직 별도다.

시간 정책은 다시 만들 필요가 없다. 최신 기록의 방향은 시작부터 최대 20분, 마지막 3분 정리다. 다만 배포된 trial 도구는 여전히 `--until` 입력 방식이며 자동 20분 계산의 구현·시험은 미완료다. 과거 19:00 시각을 현재 고정 마감이나 새로운 Kubernetes Gate로 쓰지 않는다.

**담당/시점:** 이권욱 ICR 도구·증적 / 이하영 K8S 인수. PR #9의 JSON 비밀값 마스킹 보완은 ICR에서 대응한다. CP2 적용·join 허가와 단순 수집기 수정을 구분한다.

근거: [CP1 인수 보류](https://github.com/321Team/infra-kubernetes/pull/2#issuecomment-5662853042), [#14 최신 기록](https://github.com/321Team/fds-project-baseline/issues/14), [PR #9 리뷰](https://github.com/321Team/infra-kubernetes/pull/9#pullrequestreview-5197580718).

### A03 — Worker Drain의 합격 기준: 시험 전 확정 필요

**관측:** #22는 “허용 오류 기준과 관찰 구간 명시”, “승인된 가용성 기준 충족”을 요구하지만 현재 본문·댓글·정본에서 승인된 숫자와 판정표를 확인하지 못했다. “최소 2 Worker”는 임시 단일노드 시험이 불충분하다는 설명이며, 정본의 3 Replica·Worker 분산 요구를 낮추는 승인이 아니다.

**필요 기록:** 시험 URL/요청 유형, 요청 간격·전체 관찰 구간·drain 전후 구간, 허용 실패 건수/비율 또는 최대 연속 실패 시간, 응답시간을 판정에 사용할지, Local endpoint 확인, 재배치·uncordon 완료 조건, 기대값과 승인자. 무중단을 주장하려면 그 표현과 허용 오류 기준이 일치해야 한다.

**담당/시점:** 이재환 Lead, 이하영 Support; 이권욱은 QA/G3 인수 기준 대조. 정본 3Worker 시험 전에 확정. P1-HA-02는 별도 유예 범위다. 새 RPO/RTO나 Production SLA를 P0 필수 요구로 추가하지 않는다.

근거: [#22](https://github.com/321Team/fds-project-baseline/issues/22), [임시 k3s 시험의 한계](https://github.com/321Team/fds-project-baseline/issues/22#issuecomment-5612847714), [P1-HA-02 #27](https://github.com/321Team/fds-project-baseline/issues/27).

### A04 — 앱 계약·Rule·시간대: 소스는 있으나 현재 계약 표기가 맞지 않음

**관측:** 접근 가능한 권위 구현 후보는 `supreme33-kr/fds-msa` main `01758583c03bcbf45c96eb9d7b868cee4a2ed9df`다. 과거 `321Team/fds-msa` 접근 실패를 소스 부재로 계속 적으면 안 된다.

| 항목 | 확인된 구현·문서 | 보완할 기록 |
|---|---|---|
| 계약 문서 | Internal Contract v1.0은 DRAFT, P1-MSA-01 참조, 실패 정책 OPEN ISSUE, 옛 `/health`·`/ready` 설명 | 현재 #15/P1-APP-01과 `/livez`·`/readyz`, 현재 API/OpenAPI·소스 SHA·소유자를 연결 |
| FDS 엔진 실패 | client 코드는 fail-open, connect 1초/read 2초, 평가 생략 기록 | 현재 동작의 승인/검증 범위와 timeout·응답·DB 저장·metric 기대 결과표 |
| DB 저장 실패 | transaction-api 코드는 rollback·실패 metric·HTTP 500 | 엔진 실패와 구분한 고정 fixture·E2E 결과, 관측 알림 제안의 채택 여부 |
| R04 | rules.py는 9/3 팀 결정 주석, KST 01:00≤시각<05:00, 100만원 이상 | 해당 결정 출처와 Rule 버전·경계값 fixture를 #15/#20에 연결 |
| 시간 처리 | 계약은 ISO8601 UTC 전송, API는 UTC 서버 시각, Rule은 KST 변환·naive 입력 UTC 간주, Migration은 timezone=True | 입력 offset/무시간대 처리·저장 자료형·DB session timezone·판정 시간대·표시 시간대를 구분한 단일 표 |

UTC 전송과 KST 판정은 함께 사용할 수 있으므로 그 자체를 오류로 판정하지 않았다. 쟁점은 코드의 “확정” 주석, 계약의 DRAFT, DB 티켓의 “시간대 미정”을 연결하는 현재 승인 근거와 적용 범위가 없는 것이다. 현재 값을 새로 추정하거나 과거 초안으로 되돌릴 이유는 없다.

**담당/시점:** 이재환 구현·계약 소스와 fixture, 이하영 실패/보안 검토, 이권욱 정본·E2E 연결. #4/#5/#6의 현행 유지·기능 확대 유예 종결은 유지한다. 새 hold/release/reject·운영 UI·세션 TTL·멱등성 저장소는 이번 보완에 추가하지 않는다.

근거: [계약 문서](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/docs/transaction-api_fds-engine_contract_v1.0.md), [Rule](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/fds-engine/app/rules.py), [API](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/transaction-api/app/main.py), [FDS client](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/transaction-api/app/fds_client.py), [DB 후속](https://github.com/321Team/infra-db/issues/1), [#4](https://github.com/321Team/fds-project-baseline/issues/4), [#5](https://github.com/321Team/fds-project-baseline/issues/5).

### A05 — Monitoring: 임시 실증 파일과 정본 배포 파일의 경계

**관측:** 정본은 monitoring-api의 Prometheus/Alertmanager/Grafana, monitoring-node의 node-exporter, static local PV, 고정 Digest, 내부 metrics 9091/9090을 요구한다. 현재 앱 main의 prometheus.yaml은 임시 `fds` Namespace·`latest`·emptyDir·업무 포트 scrape를 사용한다. 임시용이라는 설명은 있으나 “실 6Node에서는 Prometheus가 monitor01에 위치”라는 주석은 현재 정본 구조와 맞지 않는다. 이 파일을 정본 배포 파일로 재사용하면 사양이 갈린다.

**필요 기록:** E-K3S 참고 소스와 E-CANON 적용 소스/overlay를 구별하고, 정본 render 결과의 SHA·Digest·Namespace·포트·SA/권한을 고정한다. 3종 PVC별 SC/PV/호스트 경로·Worker/nodeAffinity·용량·UID/fsGroup·writable path와 Resource 값을 K8S/MON/SEC 간 인계한다. 구현 예시 값이 존재한다는 사실을 정본 승인값으로 승격하지 않는다.

이미 정해진 값은 유지한다: `WaitForFirstConsumer`, `Retain`, 단일 지정 Worker 비-HA, Prometheus 15일 목표·PVC 80% 상한. PVC 재시작 보존과 용량/기간 결과가 필요한 것이며 보존 정책 자체가 전부 미정인 것은 아니다.

**담당/시점:** 이재환 #17 Manifest/PVC/retention, 이하영 #10 SC/PV·#19 보안, 이권욱 IF 경로·정본 동기화. 정본 배포 전.

근거: [#17](https://github.com/321Team/fds-project-baseline/issues/17), [현재 Prometheus 소스](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/kubernetes/monitoring/prometheus.yaml), [SEC PR #7](https://github.com/321Team/infra-kubernetes/pull/7).

### A06 — 경로별 입력: OID-01~03·IF-06B 실행 계약

| 경로 | 확정된 경계 | 남은 입력·기록 | 담당 |
|---|---|---|---|
| OID-01 관리자→API LB | Runner IF-11과 별도 관리자 허용을 구분 | 실제 관리자 Source IP·Identity·허용/거부 결과. 후보 장비명만으로 승인 완료 처리하지 않음 | 이하영·이권욱, MON Runtime 전 |
| OID-02 시스템 이미지 | IF-10은 Worker만 포함 | CP/Calico/kube-system 이미지의 Harbor 또는 외부 source, 태그/불변 Digest·trust·pull 경로 | 이하영, K8S 인수 전 |
| OID-03 bootstrap egress | 미정의 목적지 Permanent 허용 금지 | 오프라인 반입 또는 HTTPS 목적지·Owner·Expiry·제거 조건 | 이하영·이권욱, 해당 설치 전 |
| IF-06B Remote Write | In-cluster Prometheus→monitor01 10.250.10.30:443, 전용 CA leaf/IP SAN·제한 payload | 실제 sender/source/return, TLS 수신 path·auth 방식·Secret 참조·self-metric allowlist·긍정/부정 결과 | 이재환 구현, 이권욱 경로, 이하영 보안 |

monitor01 주소·방향은 이미 확인됐으므로 “주소 미정”을 재요구하지 않는다. Watchdog `fds_monitoring_heartbeat=1`, `absent_over_time(...[5m])`와 P0 5분 탐지는 이미 정의돼 있다. OID-04 관리망 DNS는 P1 N/A이며 프록시 .56의 물리망 DNS 허용이 ansible01 .10의 DNS 허용으로 확대되는 것은 아니다.

근거: [정본 §11·§15 Interface/OID](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/baseline/FDS_Project_Implementation_Baseline_v3.1.18.md), [#14](https://github.com/321Team/fds-project-baseline/issues/14), [SEC 부분 수용](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5654476728).

### A07 — 프록시: 실제 구성 기록과 운영 계정 계약

**실제로 확인된 최신 상태:** server08의 비-K8S VM egress-proxy01, 2 vCPU/2 GiB/30 GiB, ens160 `10.1.93.56/24`, GW .254, DNS .52/.53, .57 예비. 링크 정상과 양 DNS UDP/TCP 4/4 성공. 관리 `10.250.10.10→.56:22` runtime/permanent 허용, 반환은 `.10/32 via .58`, 관리자 SSH 성공. svc_ansible 생성·암호 잠금·.ssh/restorecon·Python 확인까지 진행됐다.

**필요 기록은 두 갈래다.**

1. 이미 실행된 VM 배치·D16 주소 할당·DNS ACL/ipset·관리 ACL·/32 반환 경로·host key 확인을 현재 As-built, IP/Interface, 운영 inventory에 연결한다. v18 예약값을 소급 수정하지 않고 v19에 반영한다. 물리노드의 기존 /24 반환 경로와 신규 프록시의 /32 경로를 혼동하지 않는다.
2. 프록시용 공개키의 관리 참조·허용 접속 Source·sudo/become 범위·inventory 그룹·모듈 검증·회수 방법을 정한다. 기존 control01의 `(root) NOPASSWD:ALL` 확인은 프록시에 동일 권한을 부여했다는 뜻이 아니다. 공개키·sudo·svc SSH·Ansible module/become는 아직 미완료다.

Squid `http://10.1.93.56:3128`은 계획 endpoint다. PR #12의 active+disabled rollback 설정 재로드 결함은 CHANGES_REQUESTED 상태이며 apply HOLD다. 실제 Alertmanager Pod selector·프록시 관측 Source·3128 allowlist, Discord CONNECT, Secret 참조·허용/거부/복구 증적과 #75 인계가 남는다. Webhook 값 자체는 기록하지 않는다. Connect at power on·재부팅 후 지속성도 미검증이다.

**담당/시점:** 이권욱 #78 배치·자산·관리 경로/인계, 이하영 #74/#75 Lead·Secret, 이재환 설정 인계·검증/독립 리뷰. P1 부가기능이며 P0 ICR/CICD 작업과 충돌하면 유예한다.

근거: [#78](https://github.com/321Team/fds-project-baseline/issues/78), [관리 경로 결과](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663718791), [계정 준비 결과](https://github.com/321Team/fds-project-baseline/issues/74#issuecomment-5663963879), [PR #12 변경 요청](https://github.com/321Team/infra-ansible/pull/12#pullrequestreview-5195815386), [#75](https://github.com/321Team/fds-project-baseline/issues/75).

## 3. 결정·증적·정본 기록 보완

### R01 — Harbor/CA/CICD 정책의 현재값 동기화

Robot 토큰 Never 미채택·유한 30일, 사고/담당 변경/단계 인계 시 회전, Harbor Scanner 유지, 미해결 Critical/High의 Push·Deploy 차단은 이미 사용자 결정으로 남아 있다. 스캔/DB 갱신 오류는 실패 또는 미검증으로 처리하며 예외는 CVE·Digest·사유·만료·승인자로 기록한다. “정책 미선택” 상태를 계속 유지하기보다 #13/#16·구현 입력·v19에 같은 값으로 연결한다.

CA는 server01의 ca01, 2 vCPU/4 GiB, OS 40 GiB + CA 2 GiB LUKS2·오프라인 구성 결과를 실제 자산 기록에 반영한다. PR #2 준비안의 OS 20 GiB와 차이를 명시한다. 새 Root 선택과 Root/leaf 발급 완료는 다르다. 별도 암호화 백업·복구는 Harbor 적용/trust 배포 전에 필요하며, 백업 매체 부재를 모든 오프라인 준비의 금지로 바꾸지 않는다.

**담당:** 이권욱 CA/CICD·정본, 이하영 Harbor·보안. HBR-AC05의 Workflow/Source SHA·Run ID/Attempt·Scan Digest·Negative Gate·Push 제어·Manifest Digest patch·이전 승인 Digest 복구 증적은 기존 CICD 책임대로 연결한다.

근거: [Harbor 결정](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5659049448), [CICD 결정](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-5659051242), [#16](https://github.com/321Team/fds-project-baseline/issues/16), [CICD PR #2](https://github.com/321Team/infra-cicd/pull/2), [PR #3](https://github.com/321Team/infra-cicd/pull/3).

### R02 — DB Migration 병합 기록과 운영/복구 증거 구분

앱 PR #2는 9/11 12:01:53 KST에 `84a79c8550d23737b15eda3aacb8950ceafd8d17`로 병합됐고 0002가 main에 있다. PR #3도 같은 날 병합됐다. infra-db #1 및 evidence #8의 “0002 PR 병합 필요”는 현재 상태와 다르다. **병합 대기를 해소하되 운영 적용·새 DB 재현·정본 E2E까지 완료로 올리면 안 된다.**

0002 자체는 기존 db01에서 컬럼 확인 후 stamp 또는 조건부 변경을 판단하도록 적혀 있다. 운영 대상·schema fingerprint·alembic 현재/목표 revision·변경 방식·백업/롤백·신규 환경 upgrade 결과를 #11/#21에 연결한다. 9/3 dump의 원본 URI·크기/해시·Source DB 버전·생성 시각·독립 확인·restore 후 Row/Rule/E2E 결과는 별도 증적이다. 기존 “파일 헤더 확인”을 전체 복구 검증으로 확대하지 않는다.

**담당:** 이재환 Lead, 이권욱 검증 지원·정본 연결.

근거: [앱 PR #2](https://github.com/supreme33-kr/fds-msa/pull/2), [0002 소스](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/alembic/versions/0002_add_fds_evaluation_columns.py), [infra-db #1](https://github.com/321Team/infra-db/issues/1), [evidence #8](https://github.com/321Team/fds-project-evidence/issues/8), [#21](https://github.com/321Team/fds-project-baseline/issues/21).

### R03 — 최신 리뷰 HEAD·수용 범위·원본 보관 연결

Ansible #6/#7은 독립 승인·병합 후 Closed다. #8의 실제 새 Linux localhost fixture PASS가 제출돼 있으며 더 이상 “실제 Linux 시험 미실행”이 아니다. 반면 코드 PR #16은 이하영 COMMENTED, 증적 PR #12는 formal review 0·검토 댓글 1이고 두 PR 모두 미병합이다. 작성 측 검증과 리뷰어가 직접 확인한 범위가 다르므로 둘을 보존해야 한다.

전체 711개 파일 압축본은 로컬 보관, 이번 원격 편입은 원문 81+검토 6=87개다. PR 본문에 **팀 공용 전체 압축 URI 미등록**이 명시돼 있다. 원본 보유자·고정 URI·SHA256·접근 가능 여부와 리뷰어의 원본 대조 범위를 연결하면 된다. 이미 제출된 Linux 결과 전체를 이유 없이 재실행시키지 않는다.

기록 정정도 필요하다. #8의 리뷰 0 표현은 현재 COMMENTED 결과로 갱신 대상이다. evidence PR #12 검토 댓글의 “이 PR” 링크는 `infra-ansible/pull/12`로 잘못 연결돼 있어 실제 `fds-project-evidence/pull/12`로 정정할 필요가 있다. SEC PR #7은 본문에 옛 `4454098…` HEAD·검토 대기 표기가 남지만 실제 HEAD는 `122e3b4…`이고 부분 수용/잔여 HOLD 리뷰가 존재한다. 기존 댓글은 보존하고 현재 검토 요약에서 바로잡는다.

**담당:** 이권욱 Ansible 제출·증적 연결, 이하영 해당 독립 리뷰/SEC 본문, 이재환 evidence 매핑 리뷰. 다른 PR의 알려진 보완도 아래 PR 표에서 실제 HEAD와 함께 추적한다.

근거: [Ansible #8](https://github.com/321Team/infra-ansible/issues/8), [코드 PR #16](https://github.com/321Team/infra-ansible/pull/16), [코드 독립 검토](https://github.com/321Team/infra-ansible/pull/16#pullrequestreview-5198204062), [증적 PR #12](https://github.com/321Team/fds-project-evidence/pull/12), [잘못된 연결이 포함된 댓글](https://github.com/321Team/fds-project-evidence/pull/12#issuecomment-5665807328), [SEC PR #7](https://github.com/321Team/infra-kubernetes/pull/7).

### R04 — 종료 티켓의 승인·원본 참조

#67/P1-NET-01은 Done/PASS지만 현재 Completion Record의 Reviewer/Approver가 미입력이다. evidence #4/FUP-05가 이미 당시 승인자·일시·범위의 원본 참조를 추적한다. 새 승인자를 소급 기입하지 않고 당시 기록을 연결하거나 확인 불가 범위를 유지한다.

FUP-04 최초 원본/Windows·VMware·관리 경로 자료, FUP-06/07 개인별 승인 회신·정확한 시각·WBS 바이너리 열람, FUP-09 LB-A-01 DAD 원본 및 이하영의 Supplement 조건 판단도 잔여다. 현재 Permanent Supplement 수신·독립 승인·main 편입은 이미 완료됐으므로 다시 “Permanent 증적 없음”으로 쓰지 않는다. P1-LB Stage A PASS·조건부 인수·Bootstrap HOLD를 구분한다.

**담당:** 이권욱 기존 자료·승인 참조, 이하영 LB 조건 판단, 이재환 새 매핑 리뷰. 기존 종료 범위의 기술 PASS를 재개하는 과제가 아니다.

근거: [#67](https://github.com/321Team/fds-project-baseline/issues/67), [evidence #4](https://github.com/321Team/fds-project-evidence/issues/4), [evidence PR #7](https://github.com/321Team/fds-project-evidence/pull/7), [LB #9](https://github.com/321Team/fds-project-baseline/issues/9).

### R05 — CURRENT와 v19 실제 파일 편입

main CURRENT.md는 Current RELEASED v3.1.18이라고 쓰면서 Published date NOT PUBLISHED, tag/assets 미생성, main은 v3.1.17이라는 준비 당시 문구를 함께 담고 있다. 실제 Release는 9/11 발행됐다. 이 불일치는 **발행 메타데이터 정정** 대상이며 Release 미발행으로 되돌릴 근거가 아니다.

v19 PR #73 HEAD는 `89a3dbc…`, 변경 파일 9개이며 마지막 실제 수집 파일은 9/11 20:34 KST다. 9/14 결정은 PR 댓글에 연결됐지만 파일·전체 배포 묶음 갱신과 같지 않다. repository-sources.json에는 `supreme33-kr/fds-msa`가 없어 현재 앱 계약/병합 증거 수집도 빠질 수 있다.

**필요 기록:** 발행시각/tag/승인·merge SHA의 현재값, 78개 최신 Issue와 10개 열린 PR, CP1 최종 재적용·CNI 인수 보류, CP2 조사 범위, Ansible #6/#7 종결·#8 실제 시험/리뷰, #78 프록시 실측, Harbor 정책, CA As-built, 앱 PR #2/#3 병합을 실제 수집 파일에 편입. Baseline/WBS/Ticket/Completion/Notes/Manifest/해시·배포 묶음의 대응을 검증한다. Draft 수집 단계의 불완전성 자체가 잘못은 아니며 정본 발행 전 해소가 필요하다.

**담당:** 이권욱 #24/#73, 이하영 독립 정본 리뷰. 이재환은 구현·증적 리뷰 역할이며 baseline 정본 merge 권한으로 확대하지 않는다.

근거: [CURRENT.md](https://github.com/321Team/fds-project-baseline/blob/main/CURRENT.md), [실제 Release](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18), [PR #73 파일](https://github.com/321Team/fds-project-baseline/pull/73/files), [수집 저장소 목록](https://github.com/321Team/fds-project-baseline/blob/89a3dbc86ac3034f2e1c720f9828523980cc24ee/audit/v3.1.19/intake/repository-sources.json).

### R06 — 새 Decision 속성·보조 ID·Risk 출처

#78의 실제 GitHub Issue Type·Milestone은 null이다. 본문 Decision과 native Type을 맞추고 기존 Phase/Gate 연결 원칙에 따라 Milestone 또는 비차단 분류 근거를 남긴다. D/IF 신규 번호는 레지스터 충돌 검사 후 부여하고 기존 D16 의미를 바꾸지 않는다. #74/#75는 이미 Change Request Type 동기화가 완료됐으므로 다시 할당하지 않는다.

앱 Contract의 P1-MSA-01, infra-db #1의 P1-DB-03/P1-DB-05는 현재 67개 baseline Record ID와 바로 대응하지 않는다. 기존 로컬 하위 작업 ID인지 현재 #15/#11의 세부 항목인지 매핑을 명시한다. 무조건 신규 티켓으로 생성할 필요는 없다.

#4/#5/#6은 RISK-05/07/09 정의의 현행 연결을 확인하지 못해 역사적 참조로 제한한다는 문구를 이미 갖고 있다. 이 제한은 유지한다. 실제 위험 수용 시에는 현행 정의·Owner·영향·수용자·승인 출처를 먼저 연결하고 ID만으로 승인 근거를 만들지 않는다.

**담당:** 이권욱 메타데이터/레지스터, 이재환 앱·DB ID 매핑, 이하영 보안 위험 검토. 구현 저장소의 native Type/Milestone 미설정을 baseline과 동일한 규칙 위반으로 일괄 분류하지 않았다.

근거: [#78](https://github.com/321Team/fds-project-baseline/issues/78), [#74/#75 Type 완료 기록](https://github.com/321Team/fds-project-baseline/pull/73#issuecomment-5633784102), [infra-db #1](https://github.com/321Team/infra-db/issues/1), [#4](https://github.com/321Team/fds-project-baseline/issues/4).

## 4. 미정이어도 현재 누락으로 보지 않은 것

| 항목 | 현재 판정 | 확정 시 남길 내용 |
|---|---|---|
| P1-MON-02 / DR-02 / HA-02 | P0 보호를 위해 후속 유예. 신규 P0 차단으로 만들지 않음 | 재착수·납기·인수 조건; 9/23 인계·9/28 결정 목표를 구현 완료일로 사용하지 않음 |
| #28 Phase 1 Review 일정 | 9/22 오후는 권장안, 참석자·시간·승인 미확정 | 실제 참석자/AM·PM·선행조건을 확정하고 Review/G3/Close 연계. 옛 9/20 주말안을 되살리지 않음 |
| #52 Phase 2 Review 일정 | 후속 결정 티켓 존재 | 교육장 주말 작업 0 원칙과 실제 참석 가능한 평일 계획 |
| P2 아키텍처/OCI/ROSA/Registry/DNS/Operator | D21/22/23/26 결정과 구현 티켓의 조건부 의존 관계가 존재 | Region/Version/CIDR·단일 Primary/Fallback·비용/권한·상태 Cancelled/N/A의 근거를 실행 전 확정 |
| P2-OADP #44 | 미래 구현 단계의 대상·주기·보존기간 미확정 | 대상/제외, Schedule/Retention, 격리 Restore 또는 허용 대체검증의 사유·승인자·기대결과. Backup 성공만으로 종결하지 않음 |
| DB 실패 알림 제안 | infra-db #2는 기본 동작 확인·룰/시연 추가 제안 단계 | P0 기본 관측 또는 P1 고도화 중 편입 위치, Rule 임계값/기간/수신·해소·복구 시험, #17/#25/#20 연결. 현재 ACK/승인으로 간주하지 않음 |
| DB 시연 동영상 | infra-db #2 댓글은 업로드 실패 표시와 시간표만 있음 | 영상이 인수 증거로 필요하면 실제 파일/고정 링크·원본 해시를 연결. 시간표를 첨부 수신 증거로 사용하지 않음 |
| 미완료 티켓 Completion Record | Completed Date/Reviewer 미입력은 미완료 단계의 정상 템플릿일 수 있음 | 실제 완료·검토 시 이름·시각·정확한 HEAD·범위·증거 기록 |

근거: [#25](https://github.com/321Team/fds-project-baseline/issues/25), [#26](https://github.com/321Team/fds-project-baseline/issues/26), [#27](https://github.com/321Team/fds-project-baseline/issues/27), [#28](https://github.com/321Team/fds-project-baseline/issues/28), [#44](https://github.com/321Team/fds-project-baseline/issues/44), [#52](https://github.com/321Team/fds-project-baseline/issues/52), [DB 알림 제안](https://github.com/321Team/infra-db/issues/2), [영상 미첨부 기록](https://github.com/321Team/infra-db/issues/2#issuecomment-5614439427).

## 5. 이권욱이 직접 챙길 순서

| 순서 | 직접 챙길 일 | 완료를 확인할 구체적 기록 |
|---|---|---|
| 1 | ICR의 PR #9 마스킹 보완·CNI trial 시간 동작·NTP/MTU/CP2 판단 연결 | 수정 HEAD·경계/회귀 결과·실제 CNI 결과·이하영 CP1 인수 회신. 승인된 보호 상태와 후속 실행 범위를 분리 |
| 2 | CICD/CA 진행과 HBR·SEC 미결 리뷰 입력 조정 | CA 실제 구성/발급/백업 단계, 30일·Critical/High 정책 일치, 승인 SHA·Scan/Push/Deploy/Digest/복구 증적 |
| 3 | 이재환의 APP/DB/MON 계약 인계 확인 | A03~A06의 단일 현재 계약표·정본 render SHA·가용성 합격 기준. 구현을 대신 맡는 배정이 아님 |
| 4 | Ansible #8 리뷰 범위·원본 참조 마무리, 이어 #5 CI → #9 운영 전환 | #16/증적 #12의 실제 승인·병합 여부, 전체 원본 URI/접근. #6/#7 재작업 없음 |
| 5 | P0와 충돌하지 않는 프록시 #78 기록/관리 계정 인계 | As-built·IP/IF·관리 /32 route·svc_ansible 권한/검증·#74→#75 인계 |
| 6 | 정본/증적 마감 | CURRENT 정정, PR #73 실제 파일 편입, #67/FUP 승인 참조, #78 native 속성·ID 매핑, Review/Close 실제 일정 |

이권욱의 Open Assignee 31개를 동시에 실행해야 할 31개 업무로 해석하지 않는다. 다수는 후속 Milestone·P2·조건부 Decision이다. 현재 직접 실행 축은 ICR/CICD와 Ansible 후속이며, APP/DB/MON/SEC/HBR은 담당자의 산출물·입력·독립 리뷰·인수를 조정하는 역할을 구분한다.

## 6. 전체 78개 티켓별 대조표

아래의 “종결 유지”는 과거 승인·완료 범위를 유지한다는 뜻이며 이번 점검에서 서버 PASS를 새로 부여한 것이 아니다. “계획 단계”도 현재 실행값이 모두 확정됐다는 뜻은 아니다. 이 표의 A/R 번호는 본 보고서 내부 참조이며 새 GitHub Ticket·Decision ID가 아니다.

| 티켓 / Record | 상태 | Lead | 대조 결과·필요 기록 |
|---|---|---|---|
| [baseline #4](https://github.com/321Team/fds-project-baseline/issues/4) [DEC-P1-FDS-01] 거래 보류 도입 범위·판정·평가 실패·Gate 편입 결정 | Closed | 이재환 | 종결 유지. 현행 탐지·기록/확대 유예. 기존 Rule·실패 근거는 A04, Risk 출처는 R06로 인계. |
| [baseline #5](https://github.com/321Team/fds-project-baseline/issues/5) [DEC-P1-TXN-01] 거래 상태·API 응답·재시도·데이터 정합성 계약 결정 | Closed | 이재환 | 종결 유지. 기존 API/DB 계약 유지. 새 상태·멱등성 TTL 추가 대상 아님. A04/R02/R06의 현재 소스 연결. |
| [baseline #6](https://github.com/321Team/fds-project-baseline/issues/6) [DEC-P1-ADMIN-01] 보안 시연 범위·테스트 전제·조건부 운영 통제 결정 | Closed | 이하영 | 종결 유지. 신규 관리 UI/역할·15/60분 세션 초안은 미채택. 기존 보안시험은 #19/#20에서 유지. |
| [baseline #7](https://github.com/321Team/fds-project-baseline/issues/7) [D-SEC-01] Security Design Scope / Approval Review | Closed | 이하영 | 설계 승인 종결 유지. 실제 SEC Runtime 완료는 #19에서 별도 판정; A06/R03. |
| [baseline #8](https://github.com/321Team/fds-project-baseline/issues/8) [MS-G0-01] G0 Design Freeze | Closed | 이권욱 | G0 종결 유지. 후속 변경은 A07/R01/R05의 v19 변경 이력으로 연결. |
| [baseline #9](https://github.com/321Team/fds-project-baseline/issues/9) [P1-LB-01] Kubernetes API Load Balancer | Open | 이권욱 | Stage A 조건부 인수 유지. FUP-09 원본·Supplement 조건 판단과 Stage B를 구분; R04. |
| [baseline #10](https://github.com/321Team/fds-project-baseline/issues/10) [P1-K8S-01] kubeadm 3CP + 3Worker / Calico | Open | 이하영 | NTP 수치/MTU·CNI·CP2 판단, 6/6 Ready·etcd 3Member·Storage·최종 보호 잔여; A01/A02/A05/A06. |
| [baseline #11](https://github.com/321Team/fds-project-baseline/issues/11) [P1-DB-01] PostgreSQL External VM | Open | 이재환 | 0002 병합 완료와 운영 적용/신규 DB 재현 분리. 시간대·Source 거부·dump 근거; A04/R02. |
| [baseline #12](https://github.com/321Team/fds-project-baseline/issues/12) [P1-DNS-01] Internal DNS Primary/Secondary | Closed | 이권욱 | DNS 원 종결 유지. 신규 프록시 .56 ACL/ipset 4/4 결과는 #78/#74·As-built에 연결; A07/R05. |
| [baseline #13](https://github.com/321Team/fds-project-baseline/issues/13) [P1-HBR-01] Harbor / Trivy Registry | Open | 이하영 | 30일 Robot·Scanner·Critical/High 정책은 결정됨. 구현 잔여·정본 반영·Runtime 증거; R01/R03. |
| [baseline #14](https://github.com/321Team/fds-project-baseline/issues/14) [ICR-D-NET-01-01] Kubernetes Node Host Firewall / Monitoring Route | Open | 이권욱 | NTP·CNI trial·CP1 인수·CP2 조사/보호 경계와 IF 경로; A01/A02/A06. PR #9는 ICR 대응. |
| [baseline #15](https://github.com/321Team/fds-project-baseline/issues/15) [P1-APP-01] transaction-api / fds-engine | Open | 이재환 | 접근 가능한 앱 repo/고정 SHA와 현재 계약·Rule·Probe·실패 fixture 연결; A04. 정본 배포는 별도. |
| [baseline #16](https://github.com/321Team/fds-project-baseline/issues/16) [P1-CICD-01] GitHub Actions / Self-hosted Runner Delivery | Open | 이권욱 | CA As-built·발급/백업 단계·현재 Scan 정책·Delivery 증거 연결; R01/R03. Ansible #5/#8/#9 의존. |
| [baseline #17](https://github.com/321Team/fds-project-baseline/issues/17) [P1-MON-01] Kubernetes-Integrated Hybrid Monitoring 구축 및 검증 | Open | 이재환 | 임시 fds Manifest와 정본 monitoring-api/monitoring-node 배포 분리. PV/retention·IF06B; A05/A06. |
| [baseline #18](https://github.com/321Team/fds-project-baseline/issues/18) [MS-G1-01] G1 Infrastructure Ready | Open | 이권욱 | G1은 #9/#10/#11/#13 및 실제 인수 근거로 판정. 계획 날짜나 문서 발행으로 PASS 처리하지 않음. |
| [baseline #19](https://github.com/321Team/fds-project-baseline/issues/19) [P1-SEC-01] Kubernetes Security Controls | Open | 이하영 | 기존 SEC-01~08 부분 수용 유지. 현재 HEAD·키/오류판정/최종 보호·실제 render 입력; A05/A06/R03. |
| [baseline #20](https://github.com/321Team/fds-project-baseline/issues/20) [P1-E2E-01] Initial / Final E2E & Regression | Open | 이재환 | 현재 API/Rule/실패·Negative의 고정 기대값과 정본 E2E 연결; A04/A05. Critical 0·증적 승인 유지. |
| [baseline #21](https://github.com/321Team/fds-project-baseline/issues/21) [P1-DR-01] PostgreSQL Backup / Restore | Open | 이재환 | 격리 Restore·원본 해시/버전·revision/Row/Rule·복구 E2E 기록; R02. 새 RPO/RTO 요구 추가 없음. |
| [baseline #22](https://github.com/321Team/fds-project-baseline/issues/22) [P1-HA-01] Worker Drain Continuity | Open | 이재환 | 허용 오류·요청 간격/관찰 구간·복구 합격 기준 확정 필요; A03. 임시 k3s 참고 로그는 AC 아님. |
| [baseline #23](https://github.com/321Team/fds-project-baseline/issues/23) [MS-G2-01] G2 Security / Feature Ready | Open | 이하영 | G2 실제 APP/SEC/CICD/MON 결과와 결함 상태 연결. 설계 승인과 Runtime 완료 분리. |
| [baseline #24](https://github.com/321Team/fds-project-baseline/issues/24) [P1-DOC-01] Architecture / Test / Runbook Freeze | Open | 이권욱 | 현재 계약/As-built·WBS/Ticket/Evidence/Notes·Manifest 전체 대응; A04~A07/R01~R06. |
| [baseline #25](https://github.com/321Team/fds-project-baseline/issues/25) [P1-MON-02] Dashboard / Alert Enhancement | Open | 이재환 | P1 고도화/HA·보존 확대 후속. #17 기본 Dashboard/Alert 중복 금지; DB 알림 편입은 선택 필요. |
| [baseline #26](https://github.com/321Team/fds-project-baseline/issues/26) [P1-DR-02] Harbor / etcd Backup and Restore | Open | 이하영 | Harbor/etcd 격리 복구 후속 유예. 대상/버전·원본·복구 결과는 착수 전 고정; P0 자동 차단 아님. |
| [baseline #27](https://github.com/321Team/fds-project-baseline/issues/27) [P1-HA-02] Platform Resilience P1 Validation | Open | 이하영 | P1 회복력 후속 유예. 가용성 기준은 착수 전에 확정; A03의 P0 범위와 분리. |
| [baseline #28](https://github.com/321Team/fds-project-baseline/issues/28) [DEC-CAL-P1-01] Phase 1 Weekend Review Decision | Open | 이권욱 | 9/22 오후 권장안과 실제 참석자/시각 승인 분리. 옛 주말안은 현재 실행 일정 아님. |
| [baseline #29](https://github.com/321Team/fds-project-baseline/issues/29) [MS-G3-01] G3 Review Ready | Open | 이권욱 | G3는 Final E2E/DR/HA/문서·결함 결과로 판정; A03/A04/R02/R05 의존. |
| [baseline #30](https://github.com/321Team/fds-project-baseline/issues/30) [P1-REV-01] Phase 1 Review / Close Execution | Open | 이권욱 | Review 실행·회신·미결 Owner/Due를 실제 기록. 사전 자료 준비와 Review 완료 구분. |
| [baseline #31](https://github.com/321Team/fds-project-baseline/issues/31) [MS-P1-REVIEW-01] Phase 1 Review | Open | 이권욱 | 실제 Phase 1 Review 개최/판정/남은 조건 연결. #28/#30 확정 결과 의존. |
| [baseline #32](https://github.com/321Team/fds-project-baseline/issues/32) [MS-P1-CLOSE-01] Phase 1 Close | Open | 이권욱 | 실제 Close 근거·잔여 인계·승인 연결. 계획 종료일만으로 Closed 처리하지 않음. |
| [baseline #33](https://github.com/321Team/fds-project-baseline/issues/33) [MS-P2-START-01] Phase 2 Start | Open | 이권욱 | Phase 1 Close·Phase 2 착수 조건 확인. 현재 병행 실행 대상으로 추가하지 않음. |
| [baseline #34](https://github.com/321Team/fds-project-baseline/issues/34) [P2-ARC-01] Hybrid / OCI / AWS / ROSA Architecture Freeze | Open | 이권욱 | 계획 단계. P2 CIDR·IF17~20·Region/배치·D21~23/26·Gate 기준은 설계 Freeze 전에 고정. |
| [baseline #35](https://github.com/321Team/fds-project-baseline/issues/35) [P2-IAC-01] AWS / ROSA Terraform IaC | Open | 이권욱 | 계획 단계. AWS 10.20.0.0/16 유지. State/권한/버전·승인 Plan·비용/복구 기록은 Apply 전에 확정. |
| [baseline #36](https://github.com/321Team/fds-project-baseline/issues/36) [P2-OCI-01] OCI Relay Go / No-Go | Open | 이권욱 | 계획 단계. OCI Go/No-Go 및 단일 Fallback·비용/일정/보안 승인 기록. 체크포인트와 완료일 구분. |
| [baseline #37](https://github.com/321Team/fds-project-baseline/issues/37) [P2-VPN-01] OCI Relay / AWS Site-to-Site VPN | Open | 이권욱 | 계획 단계. 승인 Transit·UDP500/4500/NAT-T·Source/Route와 복구 결과를 확정안에 연결. |
| [baseline #38](https://github.com/321Team/fds-project-baseline/issues/38) [P2-ROSA-01] ROSA Platform / Security | Open | 이하영 | 계획 단계. 실제 ROSA Region/Version/Quota·권한·예외·관리/업무 경로는 구축 전에 고정. |
| [baseline #39](https://github.com/321Team/fds-project-baseline/issues/39) [MS-G4-01] G4 Cloud / VPN Ready | Open | 이권욱 | G4는 OCI/IaC/VPN 실제 결과 및 예외 기록으로 판정. 현재 P0 작업창을 별도 배정하지 않음. |
| [baseline #40](https://github.com/321Team/fds-project-baseline/issues/40) [DEC-P2-DNS-01] Hybrid DNS Scope Decision | Open | 이권욱 | 조건부 결정. IP endpoint 또는 Hybrid DNS·적용/유예/N/A 근거를 D23으로 기록. |
| [baseline #41](https://github.com/321Team/fds-project-baseline/issues/41) [DEC-P2-OP-01] Operator Supply Chain Scope Decision | Open | 이하영 | 조건부 결정. Direct 또는 Mirror 공급망·Owner/Due·#51 Cancelled/구현 기준을 D26으로 기록. |
| [baseline #42](https://github.com/321Team/fds-project-baseline/issues/42) [DEC-P2-REG-01] ROSA Image Registry Source Decision | Open | 이하영 | 조건부 결정. Harbor 또는 Cloud Registry·Digest/Trust/경로/비용/Fallback을 D22로 기록. |
| [baseline #43](https://github.com/321Team/fds-project-baseline/issues/43) [P2-APP-01] ROSA Application Deployment | Open | 이재환 | 계획 단계. P2 승인 Registry/Digest·Namespace/Source·DB/Probe·보안 계약으로 배포; A04 후속 참조. |
| [baseline #44](https://github.com/321Team/fds-project-baseline/issues/44) [P2-OADP-01] OADP / S3 Backup | Open | 이하영 | 계획 단계. Backup 대상/제외·주기/보존과 Restore 또는 승인 대체검증의 기준·사유를 사전 기록. |
| [baseline #45](https://github.com/321Team/fds-project-baseline/issues/45) [MS-G5-01] G5 ROSA Application Ready | Open | 이하영 | G5는 실제 ROSA/앱/보안 인수 근거로 판정. P1 임시 실증 재사용 시 환경·범위 제한. |
| [baseline #46](https://github.com/321Team/fds-project-baseline/issues/46) [P2-CICD-01] Runner to ROSA Delivery | Open | 이권욱 | 계획 단계. ROSA API/SA·Token/Registry/Digest·성공/차단/복구 증거 계약을 실행 전에 고정. |
| [baseline #47](https://github.com/321Team/fds-project-baseline/issues/47) [P2-HYB-01] Hybrid DB / Registry Integration | Open | 이재환 | 계획 단계. 승인 ROSA Source→DB·Registry 경로, D22/D23와 거부시험. P1 허용을 자동 확장하지 않음. |
| [baseline #48](https://github.com/321Team/fds-project-baseline/issues/48) [P2-DNS-01] Hybrid DNS Implementation Conditional | Open | 이권욱 | 조건부 구현. D23 선택 이후 DNS Query/Route·거부/복구 검증 또는 Cancelled 근거. |
| [baseline #49](https://github.com/321Team/fds-project-baseline/issues/49) [P2-DOC-01] Cloud / Hybrid Deliverable Freeze | Open | 이권욱 | 계획 단계. P2 설계·실제 설정·시험·비용/삭제·인계의 고정 참조와 배포 묶음 대응. |
| [baseline #50](https://github.com/321Team/fds-project-baseline/issues/50) [P2-E2E-01] Hybrid E2E / Regression | Open | 이재환 | 계획 단계. D22/D23 반영 Hybrid 정상/Rule/Negative/터널 복구·Critical0의 고정 케이스. |
| [baseline #51](https://github.com/321Team/fds-project-baseline/issues/51) [P2-OP-01] Operator Supply Chain Implementation Conditional | Open | 이하영 | 조건부 구현. D26 선택 이후 ImageSet/Package/Channel·Digest/Trust·Catalog Ready 또는 Cancelled 근거. |
| [baseline #52](https://github.com/321Team/fds-project-baseline/issues/52) [DEC-CAL-P2-01] Phase 2 Weekend Review Decision | Open | 이권욱 | 계획 단계. 평일 Review 참석·시각·승인 근거. 주말 작업을 자동 배정하지 않음. |
| [baseline #53](https://github.com/321Team/fds-project-baseline/issues/53) [MS-G6-01] G6 Hybrid Integration Ready | Open | 이권욱 | G6는 Hybrid/E2E/복구·미결 결함 결과 연결. 미래 계획 날짜와 실제 승인 분리. |
| [baseline #54](https://github.com/321Team/fds-project-baseline/issues/54) [MS-DELIVERABLE-FREEZE-01] Deliverable Freeze | Open | 이권욱 | 최종 산출물 Freeze의 실제 버전·참조·접근·검토 기록 필요. R05 원칙을 P2에 적용. |
| [baseline #55](https://github.com/321Team/fds-project-baseline/issues/55) [P2-REV-01] Phase 2 Review / Project Close Execution | Open | 이권욱 | 계획 단계. 프로젝트 Review 실행·결함/잔여 수용·Close 인계의 실제 승인 기록. |
| [baseline #56](https://github.com/321Team/fds-project-baseline/issues/56) [MS-P2-REVIEW-01] Phase 2 Review | Open | 이권욱 | 계획 단계. P2 Review 실제 개최·판정·승인 참조 연결. |
| [baseline #57](https://github.com/321Team/fds-project-baseline/issues/57) [MS-PROJECT-CLOSE-01] Project Close | Open | 이권욱 | 계획 단계. 최종 Close·보관/인계·비용 리소스 종료 확인을 실제 결과로 기록. |
| [baseline #58](https://github.com/321Team/fds-project-baseline/issues/58) [CR-P1-ANS-01-01] Ansible Kubernetes Node DNS Resolver 변경 | Closed | 이권욱 | DNS resolver 변경 종결 유지. 신규 프록시 DNS는 #74/#78 별도 변경; A07. |
| [baseline #59](https://github.com/321Team/fds-project-baseline/issues/59) [D-ARC-01] Phase 1 Logical / Physical Architecture Design Freeze | Closed | 이권욱 | 원 Architecture Freeze 종결 유지. ca01/proxy01 현재 배치 차이는 R01/A07/R05로 추가. |
| [baseline #60](https://github.com/321Team/fds-project-baseline/issues/60) [D-NET-01] Physical / Management Network Design Freeze | Closed | 이권욱 | 원 Network Freeze 종결 유지. 새 .56 관리/DNS/반환 경로·IF 변경을 A07/R05로 추적. |
| [baseline #61](https://github.com/321Team/fds-project-baseline/issues/61) [D-WBS-01] WBS / Backlog / Interface Management Freeze | Closed | 이권욱 | 원 WBS/Interface Freeze 종결 유지. 새 #78/보조 ID·현재 계획/상태 수집은 R05/R06. |
| [baseline #62](https://github.com/321Team/fds-project-baseline/issues/62) [DEC-P1-ENTRY-01] Edge Service Exposure Decision | Closed | 이권욱 | Edge exposure 결정 종결 유지. Service80→8000·Local topology는 APP/LB/HA 구현 검증과 연결. |
| [baseline #63](https://github.com/321Team/fds-project-baseline/issues/63) [DEC-P1-MON-01] Kubernetes-Integrated Hybrid Monitoring Architecture | Closed | 이권욱 | MON 아키텍처 결정 종결 유지. 임시 소스의 외부 Prometheus 주석은 A05에서 정정. |
| [baseline #64](https://github.com/321Team/fds-project-baseline/issues/64) [DEC-P1-TLS-01] Harbor / Edge TLS Trust Decision | Closed | 이권욱 | TLS Trust 결정 종결 유지. CA 실제 자산·새 Root 발급/backup·현재 승인 endpoint/SAN은 R01. |
| [baseline #65](https://github.com/321Team/fds-project-baseline/issues/65) [P1-ANS-01] Ansible Inventory / OS-Node Bootstrap — Closed Update | Closed | 이권욱 | P1-ANS 원 종결 유지. #6/#7도 Closed. #8/#5/#9 후속을 원 구축 미완료로 바꾸지 않음; R03. |
| [baseline #66](https://github.com/321Team/fds-project-baseline/issues/66) [P1-LNX-01] CentOS Stream 10 Linux / Network Baseline | Closed | 이권욱 | Linux 원 종결 유지. NTP 정책·K8S 보호 전환은 후속 #14/#10/#19; A01/A02. |
| [baseline #67](https://github.com/321Team/fds-project-baseline/issues/67) [P1-NET-01] Bridged Multi-MAC Smoke Test / Source Preservation | Closed | 이권욱 | 기술 종결 유지. 실제 과거 Reviewer/Approver·시각/범위의 원본 참조 미확인; R04. |
| [baseline #74](https://github.com/321Team/fds-project-baseline/issues/74) [CR-P1-MON-01-01] Alertmanager Egress 프록시 서버 구성 | Open | 이하영 | VM/OS/주소/DNS/관리 경로 완료 범위와 Squid apply HOLD 분리. 계정/복원결함/실측 Source; A07/R03. |
| [baseline #75](https://github.com/321Team/fds-project-baseline/issues/75) [CR-P1-MON-01-02] Alertmanager Egress Kubernetes 보안 설정 (NetworkPolicy) | Open | 이하영 | #74 인수 후 운영 적용. 실제 selector/NetworkPolicy/Secret 참조·전달/거부/복구 증거; A07. |
| [baseline #78](https://github.com/321Team/fds-project-baseline/issues/78) [DEC-P1-EGRESS-01] Alertmanager 전용 프록시 배치·예약 IP 사용 결정 | Open | 이권욱 | 배치/IP 결정과 실제 구성은 기록됨. As-built/IF·svc 권한 인계 및 native Type/Milestone; A07/R06. |
| [fds-project-evidence #4](https://github.com/321Team/fds-project-evidence/issues/4) [증적 후속] FUP-04/05/06/07 잔여 참조 및 FUP-09 조건부 인수 반영 | Open | 이권욱 | FUP04/05/06/07 원본·승인/접근과 FUP09 조건 판단·DAD 참조; R04. 편입 완료분 재요구 없음. |
| [fds-project-evidence #8](https://github.com/321Team/fds-project-evidence/issues/8) [Evidence] P1-DB-01 증적 등록 현황 및 잔여 후속 항목 | Open | 이재환 | 코드 병합 완료 반영·사람 검토/Source·occurred_at·백업 원본/정본 DB 인수 연결; A04/R02. |
| [infra-ansible #5](https://github.com/321Team/infra-ansible/issues/5) [P1-CICD-01 연관] infra-ansible CI 회귀 시험과 실패 차단 연동 | Open | 이권욱 | CI 회귀·실패 차단은 #8 승인/병합 및 Runner 입력 이후. 실제 Actions 실행 0을 완료로 올리지 않음; R03. |
| [infra-ansible #6](https://github.com/321Team/infra-ansible/issues/6) [PR4 후속] SSH 회귀 시험의 Ansible 내부 API 의존 제거 | Closed | 이권욱 | Closed 유지. 내부 API 의존 제거 코드·증적·문서의 승인/병합 완료. 재작업 요구 없음. |
| [infra-ansible #7](https://github.com/321Team/infra-ansible/issues/7) [PR4 후속] 서버 검증 결과 구조화 및 누락·실패 판정 강화 | Closed | 이권욱 | Closed 유지. 구조화 판정·실제 6대 읽기 16/16 증적 승인/병합 완료. 엔진 전환과 구분. |
| [infra-ansible #8](https://github.com/321Team/infra-ansible/issues/8) [PR4 후속] 검증 키트의 완전한 재현 가능한 배포 구성 | Open | 이권욱 | 실제 새 Linux fixture PASS. 현재 코드 COMMENTED·증적 댓글·미병합, 원본 공용 URI 미등록; R03. |
| [infra-ansible #9](https://github.com/321Team/infra-ansible/issues/9) [P1-ANS-01 연관] ansible-core 2.16.19 → 2.21.3 운영 전환 영향 검토·검증 | Open | 이권욱 | 운영 2.21.3 전환은 별도 영향/호환/롤백·실행 기록 필요. #8 새 venv PASS와 구분; R03. |
| [infra-ansible #10](https://github.com/321Team/infra-ansible/issues/10) [PR4 운영 적용] 승인 main SSH 수정의 6대 순차 적용·멱등성·신규 SSH 검증 | Closed | 이권욱 | Closed 유지. 승인 main SSH 수정의 6대 apply·멱등성·SFTP와 독립 승인 범위 보존. |
| [infra-db #1](https://github.com/321Team/infra-db/issues/1) [P1-DB-01] db01 PostgreSQL 구축 · 스키마 · 마이그레이션 · 백업 작업 내역 | Open | 이재환 | 0002 병합 대기 문구 정정, 운영 적용/시간대·신규 DB/원본 해시 잔여 구분; A04/R02/R06. |
| [infra-db #2](https://github.com/321Team/infra-db/issues/2) [관측/DB] db01 장애 시 거래 저장 실패 탐지·알림 공백 — 동작 확정 + 알림 룰 추가 제안 | Open | 이재환 | DB fail-close 구현과 미채택 알림/4번째 시연 제안 구분. 실제 영상 미첨부; A04/§4. |
| [infra-kubernetes #5](https://github.com/321Team/infra-kubernetes/issues/5) [P1-K8S 연관] Alertmanager egress 허용 요청 — 이상거래 탐지 알림 외부 통지 (E-CANON 대상) | Closed | 이하영 | 요청 이관 종결 유지. 실제 프록시/NetworkPolicy 구현은 #74/#75/#78. 옛 예시 IP를 현행값으로 사용하지 않음. |

## 7. 열린 PR 10개 — 배정·리뷰 상태

검토 결과를 실제 최신 HEAD와 연결했다. COMMENTED의 부분 수용을 전체 APPROVED로 바꾸지 않았다. 아래 잔여는 현재 리뷰에서 추적 중인 항목이며 이번 점검이 새 코드 실행 시험을 한 것은 아니다.

| PR | HEAD | 현재 리뷰/준비 상태 | 남은 일 |
|---|---|---|---|
| [fds-project-evidence #12](https://github.com/321Team/fds-project-evidence/pull/12) | `1ffdd67a2cd1fc5f67ac5829b049ca01a90bcb13` | Formal review 0 / 검토 댓글 1 / Ready / 미병합 | 87개 편입 범위·전체 원본 URI·링크 오류·수용 범위. R03. |
| [infra-ansible #16](https://github.com/321Team/infra-ansible/pull/16) | `d2d46bd95ece3935373303187ef47cfc5e3e2eb7` | 이하영 COMMENTED / Ready / 미병합 | 실제 Linux 제출 결과와 리뷰어 확인 범위·원본 참조 연결, 독립 승인/병합 여부 추적. #8 Open. |
| [infra-kubernetes #9](https://github.com/321Team/infra-kubernetes/pull/9) | `ccad9ce56c480cd3f5978e81257a8bb456aeac2c` | 이하영 COMMENTED / 미병합 | UTF-8/zone 수정 수용, JSON 비밀값 변형 키 마스킹 Must-fix. 서비스 계정 참조 객체의 과도한 삭제도 방지. 이권욱 ICR 대응. |
| [infra-ansible #12](https://github.com/321Team/infra-ansible/pull/12) | `6cf520fcb3d7b1ed9c8eb00eebb0d7394f8e4aea` | 이재환 CHANGES_REQUESTED / GWONUK 부분 수용 / 미병합 | active+disabled rollback config 반영, 실제 .56 입력·source·계정 준비/인수. VM 미생성이라는 과거 리뷰 상황은 최신 #78로 대체. |
| [infra-harbor-trivy #2](https://github.com/321Team/infra-harbor-trivy/pull/2) | `e4f4143be35ffdf7f1d966e010de450e35bedde8` | GWONUK COMMENTED / 부분 수용·HOLD / 미병합 | HBR-01~05 해소분 유지, 남은 검증·실제 Harbor/CI 연계 입력과 Runtime. R01. |
| [infra-kubernetes #7](https://github.com/321Team/infra-kubernetes/pull/7) | `122e3b412369c6ec6795c6ab72722b89fa21354e` | GWONUK COMMENTED / 부분 수용·HOLD / 미병합 | 키 로드/복구·비밀파일, 오류 판정, 최종 HEP 보호/통신·APP/MON render/Runtime. 옛 HEAD 요약 정정. |
| [fds-project-baseline #73](https://github.com/321Team/fds-project-baseline/pull/73) | `89a3dbc86ac3034f2e1c720f9828523980cc24ee` | Draft / formal review 0 / 미병합 | 9/14 실제 수집 파일·앱 repo·전체 v19 bundle 반영 후 독립 정본 리뷰. R05. |
| [infra-cicd #3](https://github.com/321Team/infra-cicd/pull/3) | `9775f3ff61a04be73e179cb0808e5bd844fe0193` | Draft / formal review 0 / 미병합 | CA 준비·모의 Delivery 차단 결과의 한계 유지, 실제 실행 입력/검증 후 리뷰 가능한 범위 확정. |
| [fds-project-evidence #7](https://github.com/321Team/fds-project-evidence/pull/7) | `1324522e1b59244634033e619bc5ddafaf44fa60` | Draft / formal review 0 / 미병합 | 이재환 새 FUP 매핑 검토와 원본/승인 참조 수신. 기존 승인된 편입분은 유지. |
| [infra-cicd #2](https://github.com/321Team/infra-cicd/pull/2) | `5f575fc8bfbd68d29fc3995fe68bceb87f1b194b` | Ready / formal review 0 / 미병합 | CA OS20→실제40GiB·현재 Root/정책/CSR 입력 연결, 준비안의 독립 검토와 실제 증거 분리. |

## 8. 기록 보완 시 공통 입력

기존 Issue/PR의 현재 요약과 담당 산출물에 아래 값만 연결하면 된다. 새 티켓을 일괄 생성하거나 보관 이력을 덮어쓸 필요는 없다.

| 구분 | 최소 기록 |
|---|---|
| 사양 결정 | 항목, 확정값/허용범위, 적용 환경/Source·Destination, 결정 근거·담당·시각, 관련 Ticket/IF/D ID |
| 구현 인계 | 저장소·경로·전체 SHA, render/배포 입력, 실제 image digest·버전, 승인값과의 차이 |
| 시험/인수 | TC·기대값, 실제 Source/대상·시각/시간대, 결과/오류·종료 코드, 원본 URI·해시, 수용 범위·미검증 범위 |
| 리뷰 | Reviewer 실명, 정확한 HEAD, COMMENTED/APPROVED/CHANGES_REQUESTED, 근거 permalink, 실제 확인한 범위 |
| 실행 결과 | 승인/실행/rollback/최종 상태, 운영 원본 보존, 추후 해제/회수 조건과 Owner |
| 정본 편입 | 원 결정·Issue/PR → Baseline/WBS/Ticket/As-built/Interface/Evidence/Notes/Manifest의 대응 |

이번 작업은 점검 보고서 작성까지 수행했다. GitHub 본문·댓글·담당·속성·승인·서버 설정은 변경하지 않았다.
