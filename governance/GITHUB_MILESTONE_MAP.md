# GitHub Milestone Map

Version: 1.0 · 2026-09-10. 아래는 문서 매핑이며 실제 GitHub Milestone 생성·배정 완료 기록이 아니다.

## 카탈로그 기준

정본 [v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md)와 기존 MS Issue의 명칭/계획일을 유지한다. 이전 답변의 G2 Kubernetes Platform Ready, G3 Application & Pipeline Ready, G4 Validation & Handover 예시는 이 프로젝트 정본과 다르므로 사용하지 않는다.

| Record ID | GitHub 목표 명칭 | 계획일 | 출처 |
|---|---|---|---|
| MS-G0-01 | G0 Design Freeze | 2026-09-01 | [Issue](https://github.com/321Team/fds-project-baseline/issues/8) |
| MS-G1-01 | G1 Infrastructure Ready | 2026-09-07 | [Issue](https://github.com/321Team/fds-project-baseline/issues/18) |
| MS-G2-01 | G2 Security / Feature Ready | 2026-09-11 | [Issue](https://github.com/321Team/fds-project-baseline/issues/23) |
| MS-G3-01 | G3 Review Ready | 2026-09-18 | [Issue](https://github.com/321Team/fds-project-baseline/issues/29) |
| MS-P1-REVIEW-01 | Phase 1 Review | 2026-09-20 | [Issue](https://github.com/321Team/fds-project-baseline/issues/31) |
| MS-P1-CLOSE-01 | Phase 1 Close | 2026-09-23 | [Issue](https://github.com/321Team/fds-project-baseline/issues/32) |
| MS-P2-START-01 | Phase 2 Start | 2026-09-28 | [Issue](https://github.com/321Team/fds-project-baseline/issues/33) |
| MS-G4-01 | G4 Cloud / VPN Ready | 2026-10-08 | [Issue](https://github.com/321Team/fds-project-baseline/issues/39) |
| MS-G5-01 | G5 ROSA Application Ready | 2026-10-16 | [Issue](https://github.com/321Team/fds-project-baseline/issues/45) |
| MS-G6-01 | G6 Hybrid Integration Ready | 2026-10-22 | [Issue](https://github.com/321Team/fds-project-baseline/issues/53) |
| MS-DELIVERABLE-FREEZE-01 | Deliverable Freeze | 2026-10-23 | [Issue](https://github.com/321Team/fds-project-baseline/issues/54) |
| MS-P2-REVIEW-01 | Phase 2 Review | 2026-10-24 | [Issue](https://github.com/321Team/fds-project-baseline/issues/56) |
| MS-PROJECT-CLOSE-01 | Project Close | 2026-10-26 | [Issue](https://github.com/321Team/fds-project-baseline/issues/57) |

Milestone의 계획일은 Issue End나 실제 완료일을 변경하는 지시가 아니다. 주말 Review/Non-blocker/개인 휴가 조건을 유지한다. GitHub 날짜를 설정할 때 Asia/Seoul의 계획일을 보존하되, 이번 스크립트는 due_on과 Milestone state를 수정하지 않는다.

## 확정된 단일 매핑 — 44건

Gate의 구성 목록 또는 본문 명시 Milestone을 출처로 한다. 표의 배정은 단일 추적 경로이며 그 티켓만 닫히면 Gate가 PASS라는 뜻이 아니다. #16은 G1 중간검증과 G2 전체 Delivery를 구분해 최종 G2에 연결한다.

| Issue | Record ID | 목표 Milestone | 근거 |
|---|---|---|---|
| [#7](https://github.com/321Team/fds-project-baseline/issues/7) | D-SEC-01 | MS-G0-01 | - **Milestone:** G0 Conditional Pass 해소 |
| [#8](https://github.com/321Team/fds-project-baseline/issues/8) | MS-G0-01 | MS-G0-01 | https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md |
| [#9](https://github.com/321Team/fds-project-baseline/issues/9) | P1-LB-01 | MS-G1-01 | https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md |
| [#10](https://github.com/321Team/fds-project-baseline/issues/10) | P1-K8S-01 | MS-G1-01 | https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md |
| [#11](https://github.com/321Team/fds-project-baseline/issues/11) | P1-DB-01 | MS-G1-01 | - **Milestone:** G1 Infrastructure Ready |
| [#13](https://github.com/321Team/fds-project-baseline/issues/13) | P1-HBR-01 | MS-G1-01 | https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md |
| [#15](https://github.com/321Team/fds-project-baseline/issues/15) | P1-APP-01 | MS-G2-01 | https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md |
| [#16](https://github.com/321Team/fds-project-baseline/issues/16) | P1-CICD-01 | MS-G2-01 | - **Milestone:** G1 Runner/Registry 중간검증, G2 전체 Delivery |
| [#17](https://github.com/321Team/fds-project-baseline/issues/17) | P1-MON-01 | MS-G2-01 | - **Milestone:** MS-G2-01 — Security / Feature Ready |
| [#18](https://github.com/321Team/fds-project-baseline/issues/18) | MS-G1-01 | MS-G1-01 | - **Milestone:** MS-G1-01 — G1 Infrastructure Ready |
| [#19](https://github.com/321Team/fds-project-baseline/issues/19) | P1-SEC-01 | MS-G2-01 | https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md |
| [#20](https://github.com/321Team/fds-project-baseline/issues/20) | P1-E2E-01 | MS-G3-01 | - **Milestone:** G3 Review Ready |
| [#21](https://github.com/321Team/fds-project-baseline/issues/21) | P1-DR-01 | MS-G3-01 | - **Milestone:** G3 Review Ready |
| [#22](https://github.com/321Team/fds-project-baseline/issues/22) | P1-HA-01 | MS-G3-01 | - **Milestone:** G3 Review Ready |
| [#23](https://github.com/321Team/fds-project-baseline/issues/23) | MS-G2-01 | MS-G2-01 | - **Milestone:** MS-G2-01 — G2 Security / Feature Ready |
| [#24](https://github.com/321Team/fds-project-baseline/issues/24) | P1-DOC-01 | MS-G3-01 | - **Milestone:** G3 Review Ready |
| [#28](https://github.com/321Team/fds-project-baseline/issues/28) | DEC-CAL-P1-01 | MS-P1-REVIEW-01 | - **Milestone:** Phase 1 Review |
| [#29](https://github.com/321Team/fds-project-baseline/issues/29) | MS-G3-01 | MS-G3-01 | - **Milestone:** MS-G3-01 — G3 Review Ready |
| [#31](https://github.com/321Team/fds-project-baseline/issues/31) | MS-P1-REVIEW-01 | MS-P1-REVIEW-01 | - **Milestone:** MS-P1-REVIEW-01 — Phase 1 Review |
| [#32](https://github.com/321Team/fds-project-baseline/issues/32) | MS-P1-CLOSE-01 | MS-P1-CLOSE-01 | - **Milestone:** MS-P1-CLOSE-01 — Phase 1 Close |
| [#33](https://github.com/321Team/fds-project-baseline/issues/33) | MS-P2-START-01 | MS-P2-START-01 | - **Milestone:** MS-P2-START-01 — Phase 2 Start |
| [#35](https://github.com/321Team/fds-project-baseline/issues/35) | P2-IAC-01 | MS-G4-01 | - **Milestone:** G4 Cloud / VPN Ready |
| [#37](https://github.com/321Team/fds-project-baseline/issues/37) | P2-VPN-01 | MS-G4-01 | - **Milestone:** G4 Cloud / VPN Ready |
| [#38](https://github.com/321Team/fds-project-baseline/issues/38) | P2-ROSA-01 | MS-G5-01 | - **Milestone:** G5 ROSA Application Ready |
| [#39](https://github.com/321Team/fds-project-baseline/issues/39) | MS-G4-01 | MS-G4-01 | - **Milestone:** MS-G4-01 — G4 Cloud / VPN Ready |
| [#42](https://github.com/321Team/fds-project-baseline/issues/42) | DEC-P2-REG-01 | MS-G5-01 | - **Milestone:** G5 ROSA Application Ready |
| [#43](https://github.com/321Team/fds-project-baseline/issues/43) | P2-APP-01 | MS-G5-01 | - **Milestone:** G5 ROSA Application Ready |
| [#44](https://github.com/321Team/fds-project-baseline/issues/44) | P2-OADP-01 | MS-G6-01 | - **Milestone:** G6 Hybrid Integration Ready |
| [#45](https://github.com/321Team/fds-project-baseline/issues/45) | MS-G5-01 | MS-G5-01 | - **Milestone:** MS-G5-01 — G5 ROSA Application Ready |
| [#47](https://github.com/321Team/fds-project-baseline/issues/47) | P2-HYB-01 | MS-G6-01 | - **Milestone:** G6 Hybrid Integration Ready |
| [#49](https://github.com/321Team/fds-project-baseline/issues/49) | P2-DOC-01 | MS-DELIVERABLE-FREEZE-01 | - **Milestone:** Deliverable Freeze |
| [#50](https://github.com/321Team/fds-project-baseline/issues/50) | P2-E2E-01 | MS-G6-01 | - **Milestone:** G6 Hybrid Integration Ready |
| [#52](https://github.com/321Team/fds-project-baseline/issues/52) | DEC-CAL-P2-01 | MS-P2-REVIEW-01 | - **Milestone:** Phase 2 Review |
| [#53](https://github.com/321Team/fds-project-baseline/issues/53) | MS-G6-01 | MS-G6-01 | - **Milestone:** MS-G6-01 — G6 Hybrid Integration Ready |
| [#54](https://github.com/321Team/fds-project-baseline/issues/54) | MS-DELIVERABLE-FREEZE-01 | MS-DELIVERABLE-FREEZE-01 | - **Milestone:** MS-DELIVERABLE-FREEZE-01 — Deliverable Freeze |
| [#56](https://github.com/321Team/fds-project-baseline/issues/56) | MS-P2-REVIEW-01 | MS-P2-REVIEW-01 | - **Milestone:** MS-P2-REVIEW-01 — Phase 2 Review |
| [#57](https://github.com/321Team/fds-project-baseline/issues/57) | MS-PROJECT-CLOSE-01 | MS-PROJECT-CLOSE-01 | - **Milestone:** MS-PROJECT-CLOSE-01 — Project Close |
| [#59](https://github.com/321Team/fds-project-baseline/issues/59) | D-ARC-01 | MS-G0-01 | - **Milestone Contribution:** G0의 Architecture / Network / WBS 항목 중 Architecture `PASS` |
| [#60](https://github.com/321Team/fds-project-baseline/issues/60) | D-NET-01 | MS-G0-01 | - **Milestone Contribution:** G0의 Architecture / Network / WBS 항목 중 Network `PASS`; G1 선행조건 제공 |
| [#61](https://github.com/321Team/fds-project-baseline/issues/61) | D-WBS-01 | MS-G0-01 | - **Milestone Contribution:** G0의 Architecture / Network / WBS 항목 중 WBS `PASS` |
| [#62](https://github.com/321Team/fds-project-baseline/issues/62) | DEC-P1-ENTRY-01 | MS-G2-01 | - **Milestone:** G2 Security / Feature Ready |
| [#64](https://github.com/321Team/fds-project-baseline/issues/64) | DEC-P1-TLS-01 | MS-G1-01 | - **Milestone:** G1 Infrastructure Ready |
| [#65](https://github.com/321Team/fds-project-baseline/issues/65) | P1-ANS-01 | MS-G1-01 | - **Milestone:** G1 Infrastructure Ready |
| [#66](https://github.com/321Team/fds-project-baseline/issues/66) | P1-LNX-01 | MS-G1-01 | - **Milestone:** G1 Infrastructure Ready 선행 완료 |

## 매핑 보류 — 20건

| Issue | Record ID | 보류 사유 |
|---|---|---|
| [#4](https://github.com/321Team/fds-project-baseline/issues/4) | DEC-P1-FDS-01 | 미도입/유예 결정. 현재 G2 신규 기능 편입이 아님. 추적 Milestone 미확정. |
| [#5](https://github.com/321Team/fds-project-baseline/issues/5) | DEC-P1-TXN-01 | 미도입/유예 결정. 현재 G2 신규 기능 편입이 아님. 추적 Milestone 미확정. |
| [#6](https://github.com/321Team/fds-project-baseline/issues/6) | DEC-P1-ADMIN-01 | 미도입/유예 결정. 현재 G2 신규 기능 편입이 아님. 추적 Milestone 미확정. |
| [#12](https://github.com/321Team/fds-project-baseline/issues/12) | P1-DNS-01 | G1 Non-blocker. 추적 Milestone과 Gate 필수조건을 구분하여 별도 확정. |
| [#14](https://github.com/321Team/fds-project-baseline/issues/14) | ICR-D-NET-01-01 | 복수 인터페이스/Gate 영향, End TBD. 최종 추적 Milestone 미확정. |
| [#25](https://github.com/321Team/fds-project-baseline/issues/25) | P1-MON-02 | 본문 Phase 1 P1 / Close Tracking. 실제 Milestone 별도 확정. |
| [#26](https://github.com/321Team/fds-project-baseline/issues/26) | P1-DR-02 | 본문 Phase 1 P1 / Close Tracking. 실제 Milestone 별도 확정. |
| [#27](https://github.com/321Team/fds-project-baseline/issues/27) | P1-HA-02 | 본문 Phase 1 P1 / Close Tracking. 실제 Milestone 별도 확정. |
| [#30](https://github.com/321Team/fds-project-baseline/issues/30) | P1-REV-01 | Phase 1 Review / Close 중 GitHub 단일 대표 Milestone 확정 필요. |
| [#34](https://github.com/321Team/fds-project-baseline/issues/34) | P2-ARC-01 | Phase 2 Start / G4 중 GitHub 단일 대표 Milestone 확정 필요. |
| [#36](https://github.com/321Team/fds-project-baseline/issues/36) | P2-OCI-01 | OCI Go/No-Go는 Decision 레코드이며 실제 Milestone 등록 여부 미확인. |
| [#40](https://github.com/321Team/fds-project-baseline/issues/40) | DEC-P2-DNS-01 | G5 / G6 Non-blocking Decision. 단일 대표 Milestone 미확정. |
| [#41](https://github.com/321Team/fds-project-baseline/issues/41) | DEC-P2-OP-01 | G5 / Phase 2 P1. 단일 대표 Milestone 미확정. |
| [#46](https://github.com/321Team/fds-project-baseline/issues/46) | P2-CICD-01 | 본문 G5지만 Plan End 2026-10-19가 G5 2026-10-16 이후임. 일정/Gate 불일치 검토 후 확정. |
| [#48](https://github.com/321Team/fds-project-baseline/issues/48) | P2-DNS-01 | Phase 2 P1 / G6 Non-blocker. 단일 대표 Milestone 미확정. |
| [#51](https://github.com/321Team/fds-project-baseline/issues/51) | P2-OP-01 | Phase 2 P1. 실제 Milestone 미확정. |
| [#55](https://github.com/321Team/fds-project-baseline/issues/55) | P2-REV-01 | Phase 2 Review / Project Close 중 GitHub 단일 대표 Milestone 확정 필요. |
| [#58](https://github.com/321Team/fds-project-baseline/issues/58) | CR-P1-ANS-01-01 | 완료 CR은 후속 Gate를 자동 해제하지 않음. 대표 Milestone 미확정. |
| [#63](https://github.com/321Team/fds-project-baseline/issues/63) | DEC-P1-MON-01 | G0 변경 통제 / G2 선행 설계. 단일 대표 Milestone 확정 필요. |
| [#67](https://github.com/321Team/fds-project-baseline/issues/67) | P1-NET-01 | G0 근거 / G1 선행조건. 단일 대표 Milestone 확정 필요. |

## API 적용 통제

현재 Issue 64건에서 milestone=null은 확인했지만, 저장소에 Milestone 카탈로그가 없다는 뜻은 아니다. 현재 연결 도구에는 전체 Milestone 조회·생성 기능이 없다. 정상 인증된 gh에서 카탈로그를 조회하고 위 정확한 이름과 일정으로 대조한다. 단일 일치일 때만 서버 반환 number를 사용한다. 이름·번호를 임의 추측하지 않는다.

카탈로그 부재·중복·due_on 불일치면 해당 배정을 HOLD한다. 신규 Milestone 생성, 기존 일정/상태 변경은 이 자동 동기화에 포함하지 않는다. 실제 적용 후 GET Issue 응답으로 배정 확인 전까지 MAPPED_NOT_APPLIED를 유지한다.

