# ICR/CNI 진단 단순화 — 사용자 채택 입력 및 운영 보완 준비

상태: **APPROVED_INPUT_WORKFLOW_ONLY / OPERATIONAL_REMEDIATION_PREPARATION / RUNTIME_HOLD**.
운영 정본은 v3.1.18이며 v19 후보 전체 묶음·발행은 완료되지 않았다.

## 출처

- 사용자 지시(현재 대화): “정본 및 후보 근거해서 수용 할 수 있는 부분을 적용하고 착수”.
- [리뷰어 개선·예외 요청](https://github.com/321Team/infra-kubernetes/pull/11#issuecomment-5698266772), 작성자 hayeounglee, 수정 2026-09-16T13:38:37Z. 예외 승인 요청이며 R6 코드/운영 실행의 승인 이벤트가 아니다.
- [정본 §6.6/6.6.1·Interface Register](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/baseline/FDS_Project_Implementation_Baseline_v3.1.18.md).
- [최신 Lead 입력](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5697547621) 및 [기존 후보 수집](p1-k8s-mon-lead-inputs-20260916.md).
- [반영 문서·운영 준비표](https://github.com/321Team/infra-kubernetes/blob/447a26781a402bae12ebab820b8625e00e6c1dcc/docs/change/ICR-D-NET-01-01/CNI_SCOPE_SIMPLIFICATION_20260916.md); infra-kubernetes 변경 447a26781a402bae12ebab820b8625e00e6c1dcc, 문서 4개, 실행 코드/policy 변경 0.

## APPROVED_INPUT — 이번 사용자 채택 범위

1. PR #11 신규 범용 기능·daemon 확장·VM 재반입/추가 시험을 보류하고 R5 증적·R6 소스를 보존한다.
2. 운영 CNI 최소 보완과 PR #11 진단 실행기 qualification 후속을 분리한다. 진단 도구 전체 완성을 모든 대안의 공통 AC로 추가하지 않는다.
3. 기존 CNI Positive 5개와 적용/복구 증적을 재사용하되 해당 변경의 Negative·Regression·복구·인수는 유지한다.
4. 규칙 명세·유지 기간·복구 종료 상태·증적·소비자 영수증 호환성을 하나의 변경 묶음으로 준비한다.
5. Worker 준비·검토 병행. HEP/GNP 실제 적용은 기존 Lead 입력대로 6/6 Ready 이후 별도 승인·실행창.
6. source/current state/window가 달라진 경우 필요한 입력만 갱신하며 같은 완료 증적의 반복 수집을 요구하지 않는다.

## PENDING_DECISION — 승인으로 편입하지 않는 범위

- cali 전체/Pod subnet 포괄 허용, 전체 ACCEPT, 보호 공백을 만드는 일괄 firewalld OFF.
- 5/5 Positive만으로 CP1 ACCEPTED·전체 ICR AC·CP2/CP3 적용을 자동 승인.
- 기존 진단 예외의 인수 금지·완전 회수 조건 면제.
- 새 CNI 상태를 이전 CP1 receipt.after로 위장하거나 소비자 상태 일치 검사를 삭제.
- PR #11 R6 소스 독립 승인·production qualification·새 Runtime·병합.
- control01 upstream/time authority 미확정 상태의 NTP 형상 적용, 6/6 이전 HEP/GNP Runtime.

## 후속의 정확한 범위

CP1 새 CNI 상태는 기존 `run-node-firewall.py::cp1_state_gate`의 receipt.after 완전 일치 검사에서 거절될 수 있다.
실제 rule을 확정한 뒤 새 변경 상태의 증적/인수·소비자 계약을 함께 준비한다. 기존 영수증을 수정하지 않는다.

CP2/CP3는 IF-12A TCP2379–2380·IF-12B TCP10250의 승인 CP /32 범위다.
LB .109→CP TCP6443은 **IF-12**이며 도구는 기존 규칙을 보존한다. 6443 추가 도구로 기록하지 않는다.
실제 CP1 Runtime 인수와 노드별 새 inspect/복구/작업창 조건을 충족한 뒤 CP2→검토→CP3 순서로 진행한다.
Join/reset·Node/etcd membership·NTP·최종 보호 인계는 각 기존 조건을 유지한다.
전체 ICR AC 0/20을 CP1 제한 Runtime 인수의 추가 전제처럼 부과하지 않으며 두 판정을 구분한다.

## 검증과 발행 상태

정본/후보 동일 baseline blob, 소스의 receipt 비교 조건, 내부 문서 링크와 문서 변경 4개를 대조했다.
새 코드 시험·실서버 명령·운영 적용은 수행하지 않았다. R6 286/286은 기존 STATIC/MOCK 결과다.
코드/Runtime/독립 REVIEW/병합/발행 상태와 기존 AC·Done을 상향하지 않는다.
후보 수집은 Baseline/Ticket Pack/Interface/WBS/배포 ZIP 전체 통합이나 정본 개정을 의미하지 않는다.

## 2026-09-16 후속 준비 — 배포 인수 계약 결함 제거

사용자 “착수”에 따라 [infra-kubernetes ed53205](https://github.com/321Team/infra-kubernetes/commit/ed53205fb142c86715281cbe4eca6a44b0171c90)에 인수 양식·안내문·체크섬·회귀시험 및 [연계 명세](https://github.com/321Team/infra-kubernetes/blob/ed53205fb142c86715281cbe4eca6a44b0171c90/docs/change/ICR-D-NET-01-01/CP1_HANDOFF_PREPARATION_20260916.md)를 반영했다.

- 현재 검증기는 CP1 생산자 `264b273` / helper `a09efb38…`를 요구하지만 배포 양식은 구 `f0388b1` / `0454a238…`였다. 양식과 runbook을 현재 계약에 맞추고 관련 source manifest를 갱신했다.
- 배포 양식을 직접 읽는 3개 시험을 추가했다. 변경 전 28개 중 failure 1·error 1로 재현, 변경 후 관련 2개 파일 **61/61 STATIC/MOCK PASS**. 미검증·구 source 입력은 계속 거부된다. 실행 helper/controller·생산자·방화벽 policy·원 영수증·상태 비교는 변경하지 않았다.
- 원 영수증 → 새 변경 before/after → 실제 인수 → 후속 소비자와 만료/회수를 한 묶음으로 검증할 연계 명세를 작성했다. 새 운영 상태용 소비자 구현은 아직 없고, 이번 수정 양식을 CNI 운영 인수 지원으로 해석하지 않는다.
- 기존 승인 진단은 정확한 시험 Pod 2개 /32·TCP8080·최대 20분·같은 창 완전 회수다. 이 상태를 미래 Pod/Join 운영 보완으로 유지할 수 없으므로 추가 진단을 반복하지 않는다.
- 새 운영 허용 범위·보호·유지 기간·회수 종료 상태의 결정이 남았다. cali/Pod subnet 포괄 허용·진단 인수 전용·기존 검증 우회는 계속 PENDING_DECISION이다.

분류: **PREPARATION_FIX_IMPLEMENTED / CONTRACT_SPECIFIED / OPERATIONAL_SCOPE_PENDING**.
이번 결과는 기존 사용자 채택 절차의 구현 현황이며 새 독립 리뷰·Runtime·CP1 인수·CP2 실행·AC·정본 발행의 승인 입력을 추가하지 않는다. 새 VM 시험/반입·현장 증적 재업로드 요청 없음.
