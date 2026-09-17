# FDS v3.1.19 Release Notes

상태: RELEASED / FINALIZATION · 2026-09-17 20:28 KST

전체 67건 / 일정관리 58건 / 역사적 종결 9건 / Milestone 67/67건. 상태 집계: Done 18, In Progress 11, To Do 38.

## 승인 입력과 적용 경계

| 항목 | 반영한 값·결정 | 유지되는 경계 |
|---|---|---|
| PR #72 | v18 게시 사실·WEB 필수 배포·일정 유연성·#59/#61 08-26·#46 10-16·Milestone 배정 | 기존 v18 태그와 Asset 소급 변경 없음 |
| DEC-CAL-P1-01 #28 | 09-22 오후 평일 Review 일정 결정 Done | 실제 Review/G3/Close 승인 아님 |
| DEC-P1-EGRESS-01 #78 | server08 / egress-proxy01 / .56:3128, 2vCPU·2GiB·30GiB, .57 예비 유지 | #74 Squid·#75 NetworkPolicy/Secret Runtime 별도 |
| OID-01 | ansible01 10.250.10.10/32 + svc_ansible, 내부 SNAT 금지·기존 Return Route | HEP/GNP 실제 적용은 6/6 Ready 이후 별도 실행창 |
| Monitoring storage | worker03(.108), /home/fds-local-pv/{prometheus,grafana,alertmanager}; static local PV/WFFC/Retain/nodeAffinity | 단일 Worker non-HA, 경로·SELinux·공간 검증 및 Runtime 미완료 |
| PVC 초기값 | Prometheus 20Gi / Grafana 5Gi / Alertmanager 2Gi, Prometheus 15d·retention.size≤16GB | 사용률에 따른 조정 가능한 초기값 |
| NTP 결정 | control01 내부 chronyd, UDP123, offset≤100ms, 60초×6, sync lost≥5m FAIL, reboot≤5m 재동기화 | control01 upstream/time authority 미정; INPUT_INCOMPLETE/RUNTIME_HOLD |
| Harbor/CI 정책 | Worker pull-only 분리, Robot 유한 30일 결정·Never 미채택, Harbor Scanner 유지, HIGH/CRITICAL·Scanner/DB 오류 차단 | 실제 계정·소비자별 인수 별도 |
| Trivy 운영 | 검토 버전/SHA 고정·관리자 교체, Scan 전 DB 갱신 필요·유효성 검사, 오류 fail-closed | latest 자기 갱신·오래된 DB fallback·임의 유예기간 도입 없음 |
| ICR 단순화 | 기존 증적 재사용, 도구 qualification과 운영 보완 분리, 인수/영수증 연결 | 추가 VM 반복 시험·광역 허용·CP1/CP2/CP3 인수 예외 자동 승인 없음 |

근거: [PR72](https://github.com/321Team/fds-project-baseline/pull/72), [#28](https://github.com/321Team/fds-project-baseline/issues/28), [#78](https://github.com/321Team/fds-project-baseline/issues/78), [Lead 결정](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5697547621), [Harbor 결정](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5659049448), [CI 결정](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-5659051242). 세부 수집 문서 및 원문은 audit/v3.1.19/intake와 tickets/v3.1.19/sources에 보존한다.

## 승인·관측·보류 분류

APPROVED_INPUT은 확인된 사용자/Lead 결정의 명시 범위만 뜻한다. GitHub의 Merged는 코드 편입 사실이며 Runtime 인수가 아니다. PENDING_REVIEW/INPUT_INCOMPLETE 및 합성 시험·제출 영수증 검증은 그대로 표시한다. GitHub ticket lifecycle과 원문 체크상태를 보존했으며 이번 작업에서 운영 AC를 새로 체크하지 않았다. 새 D/IF 순번은 임의 발급하지 않고 DEC-P1-EGRESS-01·CR Record ID로 추적한다.

## 배포 구성

Baseline, 67개 Description/원문 source, Ticket Pack, WBS/Gantt 9개 탭, Interface/Decision/CR Register, Milestone Map, 아키텍처, WEB, Manifest, SHA256SUMS 및 ZIP 검증 결과를 함께 제공한다. 기존 v18 Release 및 태그는 보존한다.

## 발행 잔여

내용 HEAD `ce3f0c9704dc8316c078c0c427928a97b08e4408` 이하영 APPROVED 및 merge `f759d2d72cd4f943b19cbb3b46952f75ed0b8b09` 확인. 최종화 HEAD 독립 승인·병합 → Tag/Release Asset 업로드와 검증 → Publish가 남았다. 내용 승인과 실제 게시 완료를 구분한다.

배포 상태의 효력과 작성 시점은 `FDS_Release_Finalization_Record_v3.1.19.md` 및 CURRENT를 따른다.
