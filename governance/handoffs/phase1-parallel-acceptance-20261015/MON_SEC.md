# MON·SEC 요구사항 및 증적 대조

2026-10-15 KST · CODEX_ASSISTED. MON Lead 이재환, SEC Lead 이하영, 통합 대조 이권욱. 아래 번호 M01~M14/B01~B02는 정본 순서에 붙인 문서 내 대조번호이며 새 AC가 아니다. 기존 체크·인수 상태를 임의 변경하지 않는다.

기준: [MON 발행 Description](../../../tickets/v3.1.21/descriptions/P1-MON-01.md), [SEC 발행 Description](../../../tickets/v3.1.21/descriptions/P1-SEC-01.md), [현행 MON](https://github.com/321Team/fds-project-baseline/issues/17), [현행 SEC](https://github.com/321Team/fds-project-baseline/issues/19). 과거 Description의 실패·미실행 표기보다 유효한 후속 결정과 최신 증적의 해당 범위를 우선한다.

## 1. MON 14개와 필수 보조통제 2개

‘기존 근거 유지’는 새 인수 또는 현재 서버 정상 재확인이 아니다. 기존 근거를 폐기하지 않고 변경 영향과 남은 판단을 연결한다는 뜻이다.

| 대조 | 원 요구사항 요지 | 확인 근거·현재 처리 | 남은 일 |
|---|---|---|---|
| M01 | 앱·KSM·node-exporter·kubelet·self Target UP | #17 기존 근거와 증적207의 전·중·후 23/23, 223 회복을 유지 | 과거 9/23 DOWN을 현재 장애로 재기록하지 않음. 최종 형상 인수 시 해당 시점 연결 |
| M02 | 거래와 API/FDS/DB·K8S/Node metrics | 기능224의 거래/DB/metrics, 부하228의 8,400건 집계와 resource 원본 연결 | 기능의 거래별 대조와 부하의 집계 대조를 구분 |
| M03 | 기본 Dashboard 3종·Datasource Health | #17의 기존 구축/조회 근거 유지 | 새 화면이나 로그인 시험을 수행한 것은 아님. 최종 버전·Runbook 연결 |
| M04 | Grafana ClusterIP, 외부 노출 형식 제한 | 기존 #17 및 212의 ClusterIP3000·hostNetwork=false·Ready1/1 | 212의 선택 필드 조회만으로 모든 Ingress/프록시 경로 부재를 새로 확정하지 않음 |
| M05 | 승인 관리 PF 성공·비승인 접근 실패 | 기존 PF 성공과 212 관리 경계 조회·이권욱 보관/회수 책임 확정 유지 | 실제 접근 배타성·회수 범위·개인별 감사 공백 판단 잔여. G1/G2의 미보유 과거 로그 재요청 금지 |
| M06 | node-exporter PSA·HostPath·보안·digest·collector | #17 기존 확보 범위 유지; 207의 현재 Target 관측 연결 | Target UP을 모든 보안 필드 재확인으로 확대하지 않음 |
| M07 | Prometheus/KSM 쓰기·Secret 읽기 금지 | #17 기존 RBAC와 SEC-AC03 인수 재사용 | AC07은 Runner용이므로 MON SA 권한의 대체 증거가 아님 |
| M08 | NP 긍정/부정·9100 Host 허용목록 | #17/#19 기존 흐름별 근거와 보완 기록 유지 | SEC-AC02/04의 남은 행과 연결. 오래된 실패 수치나 철회 집계 재사용 금지 |
| M09 | edge /metrics 차단·내부 scrape | 기존 외부 차단·전용 listener 근거 및 최종 이미지 기능/부하 기록 연결 | 새 이미지의 Client→edge 경로 영향은 APP D-04에서 판단 |
| M10 | Prometheus 재시작 후 PVC·query 유지 | #17의 기존 재시작/연속 query_range 근거 유지 | 문서 버전·현 형상 차이가 있을 때만 영향 재검토; 재시작 반복 없음 |
| M11 | Test Alert Firing→수신→Resolved | #17에 편입된 증적180의 Discord Firing08:57/Resolved08:58 유지 | 이 수신을 monitor01 외부 통보로 확대하지 않음 |
| M12 | heartbeat 5분 단절 감지·정상 복귀 | #17 기존 실증 및 207 사후 heartbeat/alert 관측 유지 | 207의 짧은 표본을 새 5분 단절 시험이라고 표시하지 않음 |
| M13 | edge HTTPS 또는 API LB TCP Probe 실패·복구 | #17의 기존 Probe 근거 유지 | APP engine HTTP223은 다른 대상. 기존 외부 Probe와 혼합하지 않음 |
| M14 | Resource/PVC/Retention/단일 replica 한계·복구 절차 | 기존 Runbook·제한 기록 유지 | D-02의 worker03 감시 장애영역·IF24 부재와 최종 처분 연결 |
| B01 | KSM livez/readyz·Monitoring 공식 Probe | 기존 정의/Ready·격리 exec 증적173/177 유지 | 223은 실제 engine HTTP 한 사례. 나머지 컴포넌트의 요구/증거 대응을 확인해 필요한 최소 범위만 결정 |
| B02 | IF06B receiver·TLS/Auth·payload·return route·IF24 부재 | Source/401 기존 성공, 207의 443 양성·8443 gateway 구간 관측·만료 회수·정리 재사용 | 특정 nft rule 유일 귀속·모든 실패 경로를 입증한 것으로 확대하지 않음. 전체 인수 판단 잔여 |

## 2. SEC 6개 AC

[10/7 Review Owner 인수](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6033026240)와 #19의 후속 보완을 함께 적용한다. 당시 ‘누락6행 미검증’은 이후 증적144의 관측 공백 해소와 구분한다.

| AC | 유지하는 판정·이번 보완 | 잔여·다음 완료조건 |
|---|---|---|
| AC01 PSA 위반 차단 | 기존 MET/ACCEPTED 유지 | 변경 영향 없으면 재시험하지 않음 |
| AC02 Allow/Deny | PARTIAL/NOT_VERIFIED 및 기존 행별 결정 유지. IF03/IF13A·IF05C 보완과 IF06B207 연결 | 원 Matrix의 미입증 행만 Source/대상/허용·거부/시각/rc/증거/처분으로 확정. 철회된 MET6/RISK7/NOT_MET2 집계 사용 금지 |
| AC03 SA별 can-i | 기존 MET/ACCEPTED 유지. Runner 실제 SSAR25(허용6·거부19)·GET2 및 앱/RBAC 불변을 231로 추가 연결. #16 AC07 인수 확인 | can-i는 권한 판단, GET은 해당 실제 호출 결과. 금지 mutation/exec 직접 실행 또는 모든 권한 전수 검증으로 확대하지 않음 |
| AC04 NodePort/9100/10250·보호 | 증적144 방식B 누락6행·IF12B CP02/03 관측 보완, 기존 source-preservation 근거 유지 | 부팅 연속 보호와 현 정책 인수 잔여. 과거 CP3대 한정 위험수용을 Worker·현6대에 확대하지 않음. 일괄 재부팅 요구 없음 |
| AC05 Secret 복합 | 기존 encryption MET·control03 rollback MET 유지. backup 보완 성공과 CR125 예방 rotation NOT MET/RISK ACCEPTED를 각각 보존 | 백업 존재/해시·설정 복원을 etcd 전체 복구 가능성으로 확대하지 않음. 제출된 backup 보완의 정확 범위→아직 없는 복구 검증/처분을 분리. 복합 AC 전체 체크 유지 |
| AC06 Probe | 173 격리 exec·177 정의/Ready에 **223 실제 engine HTTP 실패→Endpoint 제외→kubelet 재시작→회복**을 추가 연결 | 전체 Probe 범위 인수는 별도. 223에 기록된 관측기 rc1·HTTP 최초 회복시각 미확정 한계 유지 |

AC07의 명목 TTL900초·논리 참조 해제를 서버의 실제 만료 거부로 표시하지 않는다. AC08 만료401→새 토큰200·잔존 검사와 AC09는 기존 CICD 트랙에서 진행한다. 이번 문서가 새 시험 선행 Gate를 추가하지 않는다.

## 3. 다음 검증을 결정할 최소 입력

| 잔여 | 생산/판단 책임 | 기존 자료로 먼저 끝낼 일 | 추가 실행이 필요한 경우의 범위·중단/복구 |
|---|---|---|---|
| Grafana 배타성·감사 | 이재환(MON), 이하영(SEC), 이권욱(보관·통합 판단) | 기존 3명 관리경로·보관 책임·미보유 감사 기록을 그대로 사용해 현재 허용자/경로/회수 시점과 공백의 영향·처분 후보를 한 표로 정리 | 비밀값 수집 없이 승인 경로 1개/비승인 경로 1개의 실제 입력을 고정. 대상·권한·창이 없으면 실행 안 함. 실패 시 세션 종료·원본 보존, 계정/감사 설정을 자동 변경하지 않음 |
| Allow/Deny·부팅 | 이하영, 이권욱(ICR) | 이미 관측한 행을 제외하고 남은 원 Matrix 행과 정확 현재 정책 차이만 지정 | 공유 K8S/Harbor 변경과 비중첩. 대상/콘솔/복구점 불명 시 중단. 새 전역 방화벽·6대 재부팅을 기본안으로 삼지 않음 |
| Secret backup | 이하영 | 기존 snapshot/설정사본·복구 보완의 산출물/판정 범위를 분리하고 안전한 검증 환경을 지정 | 운영 etcd 복원·키 회전 자동 착수 금지. 검토된 정확 소스·격리 대상·민감자료 반출 제외·복귀/정리 기준을 먼저 완성 |
| Probe 잔여 | 이재환(MON), 이하영(SEC) | 각 요구를 정의·정상·격리 실패·실제 HTTP 실패 증거에 대응. 충족 근거가 있으면 재사용 | 부족한 대상만 한 회차 카드로 구체화. 다른 변경/거래 writer와 겹치거나 관측 불가면 중단, 승인된 해당 대상 복귀만 수행 |

위는 실행 준비·범위 정리이며 새 Runtime 승인이나 새 위험수용이 아니다. 인수 판단에 필요한 미확인 항목을 남기되, 이 표 전체를 독립 작업의 공통 차단조건으로 쓰지 않는다.

## 4. 최신 근거

- [IF06B207](https://github.com/321Team/fds-project-evidence/pull/207), merge `3d9826959c2351bdacc84e413246ef21145b3d68`
- [Grafana212](https://github.com/321Team/fds-project-evidence/pull/212), merge `44beaf0f4b44b0286b26e1d08196db8223ef7a1e`
- [HTTP Probe223](https://github.com/321Team/fds-project-evidence/pull/223), merge `ddd1e38c1c07d7d0dd99281df8e619c317db764b`
- [AC07 증적231](https://github.com/321Team/fds-project-evidence/pull/231), merge `72375108ec743455ae49c68b1398d211dcc1b669`; [AC07 인수 기록 #16](https://github.com/321Team/fds-project-baseline/issues/16)
- [CR125](https://github.com/321Team/fds-project-baseline/issues/125), [기존 실행/부팅 경계](../phase1-execution-20261010/PARALLEL_EXECUTION_20261013.md)
