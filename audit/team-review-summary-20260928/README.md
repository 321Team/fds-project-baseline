# 1차 결과 검토·2차 방향 종합 의견 — 2026-09-28

> 성격: 팀 공유용 검토 의견(제안). 확정 사항이 아니다. 티켓 AC·Status·일정·담당은 바꾸지 않았다.
> 각 항목은 담당 Lead가 판단하고, 정본 후보 유입을 거쳐 티켓에 반영한다.
> 작성: 이권욱 요청, Claude Code 작성(AI 사용). 근거는 각 절의 링크를 따른다.

## 한눈에 보기

| # | 주제 | 핵심 의견 | 결정 주체 |
|---|---|---|---|
| 1 | 미구축 서비스 처리 | P0은 On-Prem에서 마무리한다. 공용 HA 정책은 2차에서 검증한다. On-Prem 고유 P1은 유예한다 | 각 티켓 Lead |
| 2 | CP 장애 시험 | 9/27 CP reboot 시험으로 **etcd 과반 유지와 leader 전환은 검증됨**. LB 경유 API, Workload, E2E는 미검증 | 이하영 (#27·#10) |
| 3 | LB 장애 전환 | 경로 차단 시험은 PASS. 그러나 **CP3 재부팅 중 LB 경유 요청 실패**가 관측됨 | 이권욱 (#9) |
| 4 | ROSA·RHOAI 비용 | 예산 기준을 "크레딧 한도"에서 **"자부담 상한"**으로 바꿔야 한다. RHOAI 최소 구성(2대)은 설치 조건 미달 가능성이 있다 | 팀 합의 (10-05) / 이하영 (#95) |
| 5 | Red Hat 제품 | ROSA 위에 구현된 제품은 **아직 없음**. 발표 때 "구현·계획·검토 중"을 구분해 표기한다 | — |

## 1. On-Prem 미구축 서비스 처리 방향

모든 항목을 On-Prem에서 끝낸 뒤 넘기자는 것이 아니다. 항목마다 따로 판단한다.

| 티켓 | 현재 상태 | 권장 | 이유 |
|---|---|---|---|
| #22 P1-HA-01 Worker Drain (P0) | AC 7/8, 증적 [evidence#57](https://github.com/321Team/fds-project-evidence/pull/57) 병합 | **On-Prem 마무리** | 남은 것은 가용성 기준 판정 1건. Phase 1 Gate 조건 |
| #21 P1-DR-01 PostgreSQL (P0) | 격리 복구 PASS, 복구 후 E2E·Runbook 미완 | **On-Prem 마무리** | 2차에서도 DB는 On-Prem에 남음 |
| #27 P1-HA-02 PDB·TopologySpread·Rolling Update | 미착수. 소스에 정의 없음 | **2차로 재계획 (P1 유지)** | Manifest는 두 플랫폼 공용이라 ROSA에서 한 번 검증. P0 티켓(#43)에 넣지 않는다 |
| #27 P1-HA-02 CP 1대 중단 | 부분 근거 있음 (아래 2절) | **보완 시험 1회 또는 Known Issue** | ROSA HCP에서는 관리형이라 N/A |
| #26 P1-DR-02 etcd | 0% | **유예 (Known Issue)** | kubeadm 고유. ROSA는 #44 OADP가 담당 |
| #26 P1-DR-02 Harbor | 0% | **D22(10-16) 결과를 보고 결정** | Harbor가 ROSA 이미지 공급원이 되면 중요도가 올라감 |
| #25 P1-MON-02 | 미착수 | **유예 유지** | HA/DR 범위가 아니고 공수가 가장 큼(3~5인일, 추정) |

공수(추정, 실측 아님)는 두 안을 비교하면 아래와 같다.
- 권장안: 약 4.5~6.5인일
- 전부 2차 새 티켓으로 전환: 약 8~12인일에, P0 Gate 미충족 위험까지 따른다

## 2. CP 장애 시험 검수 결과

근거: [evidence#55](https://github.com/321Team/fds-project-evidence/pull/55) `evidence/P1-K8S-01/cp-reboot-20260927/`. 2026-09-27 17:34~18:03 KST, CP 3대를 한 대씩 reboot했다.

| 구간 | 중단 중 관측 | 결과 |
|---|---|---|
| CP1 (17:49:50) | readyz `.102` 무응답, `.103`/`.104` ok. etcd `.102` unhealthy, `.103`/`.104` healthy | **2/3 과반 유지** |
| CP2 (leader) | leader가 control03으로 전환(term 15→16) | **leader 전환 확인** |
| CP3 (17:36:40) | LB `.109` 경유 요청 Timeout·TLS handshake timeout. 직접 접속은 정상 | **LB 경유 실패** |

**#27 AC 기준으로 남은 공백**
1. CP1 중단 중 LB 경유 API는 관측하지 않았다(직접 접속만)
2. 중단 중 Workload, E2E, DNS 관측이 없다. CoreDNS 2개가 모두 control01에 배치돼 있다
3. 사전 가용성 기준이 없고, 관측이 시점별 단일 스냅샷이다

**발표에 쓸 수 있는 표현**
- 사용 가능: "CP 1대 재부팅 시 etcd 과반 유지와 leader 전환 확인", "API LB 경로 장애 전환 검증(#9)"
- 사용 불가: "Control Plane HA 검증 완료"

## 3. LB 장애 전환 (#9)

- [evidence#60](https://github.com/321Team/fds-project-evidence/pull/60)은 LB→`.104` nft **경로 차단** 시험이다. 결과는 70회 중 67회 성공으로, 허용 기준(12회/24초) 이내다
- CP 노드 **재부팅** 때는 LB 경유 요청이 실패했다. 재부팅 중에는 TCP 연결은 받아지다가 TLS 단계에서 지연되므로, HAProxy가 DOWN을 판정하기 전 구간에서 실패했을 가능성이 있다(추정, 미검증)
- 확인 제안: 17:36 전후 HAProxy stats·로그로 DOWN 판정 시각과 실패 요청 시각을 대조한다. 필요하면 CP 재부팅 중 LB 경유 API를 연속 관측하는 시험을 1회 한다. #27 보완 시험과 함께 할 수 있다

## 4. HA/DR 증적 정합성

| 티켓 | 증적 | 확인 필요 |
|---|---|---|
| #10 P1-K8S-01 | cp-reboot, Worker reboot 등 병합 | 체크된 줄 4개에 "PARTIAL" 문구가 남아 있다. reboot 지속성 줄의 체크 변경 근거가 없다. 일부 근거 링크가 증적 저장소 밖을 가리킨다. README에 "독립 검토 미완료" 표기가 남아 있다 |
| #9 P1-LB-01 | Stage B 5개 폴더 병합 | 위 3절. 최종 Handoff 인수 잔여 |
| #22 P1-HA-01 | #57 병합 | 가용성 AC 판정 대기. 본문에 "PR #57 병합 전" 표기가 남아 있다 |
| #21 P1-DR-01 | #41 병합(콘솔 붙여넣기 6개) | 체크된 AC 3개의 원본이 약하다(성공한 `pg_restore` 화면 없음, 직접 비교 없음). 복구 후 E2E 없음 |
| #27 · #26 · #25 | 없음 | 미착수 |

- 9/20~21 실제 장애는 방화벽 누락으로 3CP 전체가 과반을 잃은 사고다. 이 동안 API는 완전히 불가했다. CP 장애 시험 근거로 쓸 수 없다

## 5. ROSA·RHOAI 비용 (요약)

상세: [#95 코멘트](https://github.com/321Team/fds-project-baseline/issues/95#issuecomment-5863864717). 단가는 웹 검색 요약 기준이며 공식 원문은 확인하지 못했다.

- **자부담 기준:** ROSA 서비스 요금, ACS, RHOAI 구독은 Marketplace로 청구돼 크레딧이 적용되지 않을 가능성이 크다. 기본 구성을 상시 가동(480h)하면 크레딧 대상은 $227, 자부담은 **$284**다
- **RHOAI 워커 대수:** 설치 조건이 노드당 "가용" 8 CPU·32GiB라 m5.2xlarge 2대로는 부족할 수 있다. 3대 기준이면 연장 PoC(40h)가 **$108**이다
- **아직 모름:** RHOAI 구독료. 무료 대안은 Developer Sandbox(30일, 하이브리드 연계 없음)다
- **삭제 누락 비용:** 하룻밤 $15~38, 주말 $66~167
- **10-05 회의 안건:** 자부담 상한과 결제 주체, 쿠폰 약관 확인

## 6. Red Hat 제품 현황

상세: [`audit/redhat-product-inventory-20260928/`](../redhat-product-inventory-20260928/README.md)

| 구분 | 제품 |
|---|---|
| 구현 (Phase 1, On-Prem) | Ansible, CentOS Stream 10 (Cockpit은 비활성) |
| 계획 (Phase 2, 미착수) | ROSA, OpenShift Route·SecurityContext, OADP, Operator 카탈로그 또는 oc-mirror |
| 검토 중 (#34 제안) | OpenShift GitOps, Compliance Operator, RHOAI, ACS 등 |

## 7. 정본 유입 시 반영 후보

모두 Lead 결정이 선행돼야 하며, 결정 전에는 반영하지 않는다.

| 대상 | 반영 후보 | 결정 |
|---|---|---|
| #27 | CP 중단 AC에 9/27 reboot 증적을 부분 근거로 연결. 보완 시험 또는 Known Issue 결정. PDB·TopologySpread·Rolling Update는 Phase 2 대상 P1로 재계획 | 이하영 |
| #26 | Harbor와 etcd 분리 여부. etcd는 유예, Harbor는 D22 연동 | 이하영 |
| #25 | 유예 유지를 Known Issue로 기록 | 이재환 |
| #9 | 재부팅 시나리오의 LB 전환 결과를 AC 범위에 포함할지 판단 | 이권욱 |
| #10 | PARTIAL 문구와 체크 상태 정합화, CoreDNS 분산 여부 | 이하영 |
| #22 · #21 | 가용성 기준 판정. 복구 후 E2E와 원본 보강 | 이재환 |
| #24 · #30~#32 | 유예 항목과 Known Issue 목록 반영 | 이권욱 |
| #34 · #38 · #35 | 워커 대수·AZ, machine pool 변수화, 자부담 상한 | 이권욱 · 이하영 |
| #95 | 비용 보정(K1~K10)을 결정 입력으로 사용 | 이하영 |

## 관련 기록

- 코멘트:
  - 비용: [#95](https://github.com/321Team/fds-project-baseline/issues/95#issuecomment-5863864717) 외 9건(2026-09-28)
  - HA 검수: [#27](https://github.com/321Team/fds-project-baseline/issues/27#issuecomment-5865744633), [#9](https://github.com/321Team/fds-project-baseline/issues/9#issuecomment-5865746669), [#10](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5865748496)
- 검수 기준: evidence main `5211dfe`, infra-kubernetes main `032c208`, Issue 조회 2026-09-28
- 미확인:
  - RHOAI 원본 비용 자료 v2
  - AWS·Red Hat 공식 단가 원문
  - 9/20~21 장애 원본 로그
  - 쿠버네티스 담당자 개인 세션 기록
