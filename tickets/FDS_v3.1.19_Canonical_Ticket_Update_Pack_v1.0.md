# FDS v3.1.19 Canonical Ticket Update Pack

상태: CANDIDATE / NOT RELEASED. 기준 2026-09-17 20:28 KST.

전체 67건 / 일정관리 58건 / 역사적 종결 9건 / Milestone 67/67건. 상태 집계: Done 18, In Progress 11, To Do 38.

각 Description과 source JSON은 Record ID로 연결한다. 원문 AC를 새로 체크하거나 운영 티켓을 변경하지 않았다. #59/#61 08-26 정정, #46 10-16 계획 및 전체 Milestone 배정을 반영했다. #25~27 구현 TBD·Close 인계 목적을 유지한다.

| Record | Status | Plan Start | Plan End | Lead | Milestone | 인수 경계 |
|---|---|---|---|---|---|---|
| [DEC-P1-FDS-01](https://github.com/321Team/fds-project-baseline/issues/4) | Done | 2026-09-08 | 2026-09-09 | 이재환 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P1-TXN-01](https://github.com/321Team/fds-project-baseline/issues/5) | Done | 2026-09-08 | 2026-09-09 | 이재환 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P1-ADMIN-01](https://github.com/321Team/fds-project-baseline/issues/6) | Done | 2026-09-08 | 2026-09-09 | 이하영 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [D-SEC-01](https://github.com/321Team/fds-project-baseline/issues/7) | Done | 2026-08-26 | 2026-09-01 | 이하영 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-G0-01](https://github.com/321Team/fds-project-baseline/issues/8) | Done | 2026-08-26 | 2026-09-01 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-LB-01](https://github.com/321Team/fds-project-baseline/issues/9) | In Progress | 2026-08-27 | 2026-09-17 | 이권욱 | G1 Infrastructure Ready | Stage B 사전점검은 CP1 UP, CP2/CP3 연결 거절로 기록됨. infra-lb 이관과 코드·증적 편입을 Stage B Failover 인수와 구분한다. |
| [P1-K8S-01](https://github.com/321Team/fds-project-baseline/issues/10) | In Progress | 2026-08-27 | 2026-09-17 | 이하영 | G1 Infrastructure Ready | 3CP+3Worker/etcd/DNS/cross-node/Storage 및 재부팅·복구 최종 인수 미완료. OID-01·Storage·NTP downstream 결정은 수용하되 upstream 입력과 Runtime 승인 경계를 유지한다. |
| [P1-DB-01](https://github.com/321Team/fds-project-baseline/issues/11) | In Progress | 2026-08-28 | 2026-09-17 | 이재환 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-DNS-01](https://github.com/321Team/fds-project-baseline/issues/12) | Done | 2026-08-28 | 2026-09-03 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-HBR-01](https://github.com/321Team/fds-project-baseline/issues/13) | In Progress | 2026-08-31 | 2026-09-17 | 이하영 | G1 Infrastructure Ready | HBR 수정 PR #2 병합은 코드 편입이다. Worker Pull-only Robot·유한 만료·인증서/Scanner·소비자별 Runtime 인수는 책임 티켓의 실제 증적으로 구분한다. |
| [ICR-D-NET-01-01](https://github.com/321Team/fds-project-baseline/issues/14) | In Progress | 2026-09-01 | 2026-09-21 | 이권욱 | G2 Security / Feature Ready | CP1 CNI 제한 진단·회수·인수와 6대 최종 HEP/GNP 보호 전환을 구분한다. 운영 후보·영수증 소비자·CP2/CP3 인수 미결을 보존하며 6/6 Ready로 확대하지 않는다. |
| [P1-APP-01](https://github.com/321Team/fds-project-baseline/issues/15) | In Progress | 2026-09-01 | 2026-09-18 | 이재환 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-CICD-01](https://github.com/321Team/fds-project-baseline/issues/16) | In Progress | 2026-09-01 | 2026-09-18 | 이권욱 | G2 Security / Feature Ready | 공급 및 base probe 제출 Runtime PASS와 로그인 Git 수신 검증을 보존한다. 실제 앱 Test/Build/Scan·Push·Deploy 미실행, Delivery 미검증. 소스 CI/코드 병합은 앱 Runtime 인수가 아니다. |
| [P1-MON-01](https://github.com/321Team/fds-project-baseline/issues/17) | In Progress | 2026-09-07 | 2026-09-18 | 이재환 | G2 Security / Feature Ready | worker03 static local PV/PVC 초기값 20/5/2Gi 승인 입력 반영. 전용 metrics listener의 담당자 실행 보고와 정본 클러스터 통합 Runtime 인수를 구분한다. 14개 Runtime AC+필수 보조통제 2개 유지. |
| [MS-G1-01](https://github.com/321Team/fds-project-baseline/issues/18) | To Do | 2026-09-17 | 2026-09-17 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-SEC-01](https://github.com/321Team/fds-project-baseline/issues/19) | In Progress | 2026-09-04 | 2026-09-21 | 이하영 | G2 Security / Feature Ready | SEC PR #7 보완은 코드 검토 단계다. TLS 우회·key rotation reload 입증·mount assert 등 잔여 지적과 최신 독립 승인 미확인을 유지한다. Runtime PASS 상향 없음. |
| [P1-E2E-01](https://github.com/321Team/fds-project-baseline/issues/20) | To Do | 2026-09-11 | 2026-09-22 | 이재환 | G3 Review Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-DR-01](https://github.com/321Team/fds-project-baseline/issues/21) | To Do | 2026-09-11 | 2026-09-21 | 이재환 | G3 Review Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-HA-01](https://github.com/321Team/fds-project-baseline/issues/22) | To Do | 2026-09-11 | 2026-09-21 | 이재환 | G3 Review Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-G2-01](https://github.com/321Team/fds-project-baseline/issues/23) | To Do | 2026-09-21 | 2026-09-21 | 이하영 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-DOC-01](https://github.com/321Team/fds-project-baseline/issues/24) | To Do | 2026-09-11 | 2026-09-22 | 이권욱 | G3 Review Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-MON-02](https://github.com/321Team/fds-project-baseline/issues/25) | To Do | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 | 이재환 | Phase 1 Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-DR-02](https://github.com/321Team/fds-project-baseline/issues/26) | To Do | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 | 이하영 | Phase 1 Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-HA-02](https://github.com/321Team/fds-project-baseline/issues/27) | To Do | TBD — P0 인수 후 재계획 | TBD — 구현 유예 권장 | 이하영 | Phase 1 Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-CAL-P1-01](https://github.com/321Team/fds-project-baseline/issues/28) | Done | 2026-09-11 | 2026-09-11 | 이권욱 | Phase 1 Review | 09-22 오후 평일 Review 일정 결정 Done. 실제 Phase 1 Review·G3·Close 수행/승인은 별도이며 초기 계획 날짜는 이력으로 유지한다. |
| [MS-G3-01](https://github.com/321Team/fds-project-baseline/issues/29) | To Do | 2026-09-22 | 2026-09-22 | 이권욱 | G3 Review Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-REV-01](https://github.com/321Team/fds-project-baseline/issues/30) | To Do | 2026-09-22 | 2026-09-23 | 이권욱 | Phase 1 Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-P1-REVIEW-01](https://github.com/321Team/fds-project-baseline/issues/31) | To Do | 2026-09-22 | 2026-09-22 | 이권욱 | Phase 1 Review | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-P1-CLOSE-01](https://github.com/321Team/fds-project-baseline/issues/32) | To Do | 2026-09-23 | 2026-09-23 | 이권욱 | Phase 1 Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-P2-START-01](https://github.com/321Team/fds-project-baseline/issues/33) | To Do | 2026-09-28 | 2026-09-28 | 이권욱 | Phase 2 Start | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-ARC-01](https://github.com/321Team/fds-project-baseline/issues/34) | To Do | 2026-09-28 | 2026-09-28 | 이권욱 | Phase 2 Start | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-IAC-01](https://github.com/321Team/fds-project-baseline/issues/35) | To Do | 2026-09-28 | 2026-10-08 | 이권욱 | G4 Cloud / VPN Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-OCI-01](https://github.com/321Team/fds-project-baseline/issues/36) | To Do | 2026-09-28 | 2026-10-02 | 이권욱 | G4 Cloud / VPN Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-VPN-01](https://github.com/321Team/fds-project-baseline/issues/37) | To Do | 2026-10-01 | 2026-10-08 | 이권욱 | G4 Cloud / VPN Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-ROSA-01](https://github.com/321Team/fds-project-baseline/issues/38) | To Do | 2026-10-06 | 2026-10-16 | 이하영 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-G4-01](https://github.com/321Team/fds-project-baseline/issues/39) | To Do | 2026-10-08 | 2026-10-08 | 이권욱 | G4 Cloud / VPN Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P2-DNS-01](https://github.com/321Team/fds-project-baseline/issues/40) | To Do | 2026-10-12 | 2026-10-16 | 이권욱 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P2-OP-01](https://github.com/321Team/fds-project-baseline/issues/41) | To Do | 2026-10-12 | 2026-10-16 | 이하영 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P2-REG-01](https://github.com/321Team/fds-project-baseline/issues/42) | To Do | 2026-10-12 | 2026-10-16 | 이하영 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-APP-01](https://github.com/321Team/fds-project-baseline/issues/43) | To Do | 2026-10-12 | 2026-10-16 | 이재환 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-OADP-01](https://github.com/321Team/fds-project-baseline/issues/44) | To Do | 2026-10-15 | 2026-10-22 | 이하영 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-G5-01](https://github.com/321Team/fds-project-baseline/issues/45) | To Do | 2026-10-16 | 2026-10-16 | 이하영 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-CICD-01](https://github.com/321Team/fds-project-baseline/issues/46) | To Do | 2026-10-16 | 2026-10-16 | 이권욱 | G5 ROSA Application Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-HYB-01](https://github.com/321Team/fds-project-baseline/issues/47) | To Do | 2026-10-16 | 2026-10-22 | 이재환 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-DNS-01](https://github.com/321Team/fds-project-baseline/issues/48) | To Do | 2026-10-19 | 2026-10-20 | 이권욱 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-DOC-01](https://github.com/321Team/fds-project-baseline/issues/49) | To Do | 2026-10-19 | 2026-10-23 | 이권욱 | Deliverable Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-E2E-01](https://github.com/321Team/fds-project-baseline/issues/50) | To Do | 2026-10-19 | 2026-10-22 | 이재환 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-OP-01](https://github.com/321Team/fds-project-baseline/issues/51) | To Do | 2026-10-19 | 2026-10-20 | 이하영 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-CAL-P2-01](https://github.com/321Team/fds-project-baseline/issues/52) | To Do | 2026-10-22 | 2026-10-22 | 이권욱 | Phase 2 Review | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-G6-01](https://github.com/321Team/fds-project-baseline/issues/53) | To Do | 2026-10-22 | 2026-10-22 | 이권욱 | G6 Hybrid Integration Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-DELIVERABLE-FREEZE-01](https://github.com/321Team/fds-project-baseline/issues/54) | To Do | 2026-10-23 | 2026-10-23 | 이권욱 | Deliverable Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P2-REV-01](https://github.com/321Team/fds-project-baseline/issues/55) | To Do | 2026-10-23 | 2026-10-26 | 이권욱 | Project Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-P2-REVIEW-01](https://github.com/321Team/fds-project-baseline/issues/56) | To Do | 2026-10-23 | 2026-10-23 | 이권욱 | Phase 2 Review | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [MS-PROJECT-CLOSE-01](https://github.com/321Team/fds-project-baseline/issues/57) | To Do | 2026-10-26 | 2026-10-26 | 이권욱 | Project Close | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [CR-P1-ANS-01-01](https://github.com/321Team/fds-project-baseline/issues/58) | Done | 2026-09-04 | 2026-09-07 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [D-ARC-01](https://github.com/321Team/fds-project-baseline/issues/59) | Done | 2026-08-24 | 2026-08-26 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [D-NET-01](https://github.com/321Team/fds-project-baseline/issues/60) | Done | 2026-08-24 | 2026-08-26 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [D-WBS-01](https://github.com/321Team/fds-project-baseline/issues/61) | Done | 2026-08-24 | 2026-08-26 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P1-ENTRY-01](https://github.com/321Team/fds-project-baseline/issues/62) | Done | 2026-08-27 | 2026-08-31 | 이권욱 | G2 Security / Feature Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P1-MON-01](https://github.com/321Team/fds-project-baseline/issues/63) | Done | 2026-08-31 | 2026-08-31 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [DEC-P1-TLS-01](https://github.com/321Team/fds-project-baseline/issues/64) | Done | 2026-08-27 | 2026-08-31 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-ANS-01](https://github.com/321Team/fds-project-baseline/issues/65) | Done | 2026-08-27 | 2026-09-01 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-LNX-01](https://github.com/321Team/fds-project-baseline/issues/66) | Done | 2026-08-24 | 2026-08-26 | 이권욱 | G1 Infrastructure Ready | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [P1-NET-01](https://github.com/321Team/fds-project-baseline/issues/67) | Done | 2026-08-27 | 2026-08-27 | 이권욱 | G0 Design Freeze | 현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다. |
| [CR-P1-MON-01-01](https://github.com/321Team/fds-project-baseline/issues/74) | In Progress | 2026-09-11 | TBD | 이하영 | G2 Security / Feature Ready | egress-proxy01 .56 배치·관리 계정 준비 및 Ansible 점검 증적과 Squid 서비스/Alertmanager 실제 Source·인수 후속을 구분한다. End TBD 유지. |
| [CR-P1-MON-01-02](https://github.com/321Team/fds-project-baseline/issues/75) | In Progress | TBD | TBD | 이하영 | G2 Security / Feature Ready | 프록시 #74 인수 후 실제 selector·NetworkPolicy·Secret·발송/거부/복구 인수. 초안 준비와 실제 운영 적용을 구분하며 Start/End TBD 유지. |
| [DEC-P1-EGRESS-01](https://github.com/321Team/fds-project-baseline/issues/78) | Done | 2026-09-14 | 2026-09-21 | 이권욱 | G2 Security / Feature Ready | Decision 범위 Done(2026-09-16): .56 전용 배치·정책·예약/자산·자원 영향·#74/#75 인계조건 확정. Squid/NetworkPolicy Runtime 및 G2 승인은 별도. |

## 개별 Description

- [DEC-P1-FDS-01](v3.1.19/descriptions/DEC-P1-FDS-01.md)
- [DEC-P1-TXN-01](v3.1.19/descriptions/DEC-P1-TXN-01.md)
- [DEC-P1-ADMIN-01](v3.1.19/descriptions/DEC-P1-ADMIN-01.md)
- [D-SEC-01](v3.1.19/descriptions/D-SEC-01.md)
- [MS-G0-01](v3.1.19/descriptions/MS-G0-01.md)
- [P1-LB-01](v3.1.19/descriptions/P1-LB-01.md)
- [P1-K8S-01](v3.1.19/descriptions/P1-K8S-01.md)
- [P1-DB-01](v3.1.19/descriptions/P1-DB-01.md)
- [P1-DNS-01](v3.1.19/descriptions/P1-DNS-01.md)
- [P1-HBR-01](v3.1.19/descriptions/P1-HBR-01.md)
- [ICR-D-NET-01-01](v3.1.19/descriptions/ICR-D-NET-01-01.md)
- [P1-APP-01](v3.1.19/descriptions/P1-APP-01.md)
- [P1-CICD-01](v3.1.19/descriptions/P1-CICD-01.md)
- [P1-MON-01](v3.1.19/descriptions/P1-MON-01.md)
- [MS-G1-01](v3.1.19/descriptions/MS-G1-01.md)
- [P1-SEC-01](v3.1.19/descriptions/P1-SEC-01.md)
- [P1-E2E-01](v3.1.19/descriptions/P1-E2E-01.md)
- [P1-DR-01](v3.1.19/descriptions/P1-DR-01.md)
- [P1-HA-01](v3.1.19/descriptions/P1-HA-01.md)
- [MS-G2-01](v3.1.19/descriptions/MS-G2-01.md)
- [P1-DOC-01](v3.1.19/descriptions/P1-DOC-01.md)
- [P1-MON-02](v3.1.19/descriptions/P1-MON-02.md)
- [P1-DR-02](v3.1.19/descriptions/P1-DR-02.md)
- [P1-HA-02](v3.1.19/descriptions/P1-HA-02.md)
- [DEC-CAL-P1-01](v3.1.19/descriptions/DEC-CAL-P1-01.md)
- [MS-G3-01](v3.1.19/descriptions/MS-G3-01.md)
- [P1-REV-01](v3.1.19/descriptions/P1-REV-01.md)
- [MS-P1-REVIEW-01](v3.1.19/descriptions/MS-P1-REVIEW-01.md)
- [MS-P1-CLOSE-01](v3.1.19/descriptions/MS-P1-CLOSE-01.md)
- [MS-P2-START-01](v3.1.19/descriptions/MS-P2-START-01.md)
- [P2-ARC-01](v3.1.19/descriptions/P2-ARC-01.md)
- [P2-IAC-01](v3.1.19/descriptions/P2-IAC-01.md)
- [P2-OCI-01](v3.1.19/descriptions/P2-OCI-01.md)
- [P2-VPN-01](v3.1.19/descriptions/P2-VPN-01.md)
- [P2-ROSA-01](v3.1.19/descriptions/P2-ROSA-01.md)
- [MS-G4-01](v3.1.19/descriptions/MS-G4-01.md)
- [DEC-P2-DNS-01](v3.1.19/descriptions/DEC-P2-DNS-01.md)
- [DEC-P2-OP-01](v3.1.19/descriptions/DEC-P2-OP-01.md)
- [DEC-P2-REG-01](v3.1.19/descriptions/DEC-P2-REG-01.md)
- [P2-APP-01](v3.1.19/descriptions/P2-APP-01.md)
- [P2-OADP-01](v3.1.19/descriptions/P2-OADP-01.md)
- [MS-G5-01](v3.1.19/descriptions/MS-G5-01.md)
- [P2-CICD-01](v3.1.19/descriptions/P2-CICD-01.md)
- [P2-HYB-01](v3.1.19/descriptions/P2-HYB-01.md)
- [P2-DNS-01](v3.1.19/descriptions/P2-DNS-01.md)
- [P2-DOC-01](v3.1.19/descriptions/P2-DOC-01.md)
- [P2-E2E-01](v3.1.19/descriptions/P2-E2E-01.md)
- [P2-OP-01](v3.1.19/descriptions/P2-OP-01.md)
- [DEC-CAL-P2-01](v3.1.19/descriptions/DEC-CAL-P2-01.md)
- [MS-G6-01](v3.1.19/descriptions/MS-G6-01.md)
- [MS-DELIVERABLE-FREEZE-01](v3.1.19/descriptions/MS-DELIVERABLE-FREEZE-01.md)
- [P2-REV-01](v3.1.19/descriptions/P2-REV-01.md)
- [MS-P2-REVIEW-01](v3.1.19/descriptions/MS-P2-REVIEW-01.md)
- [MS-PROJECT-CLOSE-01](v3.1.19/descriptions/MS-PROJECT-CLOSE-01.md)
- [CR-P1-ANS-01-01](v3.1.19/descriptions/CR-P1-ANS-01-01.md)
- [D-ARC-01](v3.1.19/descriptions/D-ARC-01.md)
- [D-NET-01](v3.1.19/descriptions/D-NET-01.md)
- [D-WBS-01](v3.1.19/descriptions/D-WBS-01.md)
- [DEC-P1-ENTRY-01](v3.1.19/descriptions/DEC-P1-ENTRY-01.md)
- [DEC-P1-MON-01](v3.1.19/descriptions/DEC-P1-MON-01.md)
- [DEC-P1-TLS-01](v3.1.19/descriptions/DEC-P1-TLS-01.md)
- [P1-ANS-01](v3.1.19/descriptions/P1-ANS-01.md)
- [P1-LNX-01](v3.1.19/descriptions/P1-LNX-01.md)
- [P1-NET-01](v3.1.19/descriptions/P1-NET-01.md)
- [CR-P1-MON-01-01](v3.1.19/descriptions/CR-P1-MON-01-01.md)
- [CR-P1-MON-01-02](v3.1.19/descriptions/CR-P1-MON-01-02.md)
- [DEC-P1-EGRESS-01](v3.1.19/descriptions/DEC-P1-EGRESS-01.md)
