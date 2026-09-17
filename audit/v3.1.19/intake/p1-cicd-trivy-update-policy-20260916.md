# P1-CICD-01 Trivy 갱신 운영안 — 사용자 채택 입력

상태: **APPROVED_INPUT / ADOPTED_BY_USER / IMPLEMENTATION_IN_PROGRESS**.
정본 상태: v3.1.19 후보 수집, NOT RELEASED. 발행 정본 v3.1.18 유지.

## 채택 근거와 변경 이유

2026-09-16 사용자가 “권장안으로 정본 후보에 등록하고, 착수”를 지시했다.
[infra-cicd #8](https://github.com/321Team/infra-cicd/issues/8)에 이 지시와 운영안을 기록했다.
바이너리 수동 설치·해시 고정과 도구 검증은 이미 관측됐으나, 바이너리 갱신 관리와
DB 준비 절차의 세부 운영 방식은 확정 근거가 없었다. 이 입력은 그 상세 운영안을 채택한다.

관련 기준:

- [발행 정본 P1-CICD-01](https://github.com/321Team/fds-project-baseline/blob/docs-v3.1.18/tickets/v3.1.18/descriptions/P1-CICD-01.md)
- [9/14 사용자 Scan Gate 결정](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-5659051242)
- [PATH 보강 PR #7](https://github.com/321Team/infra-cicd/pull/7)
- [상위 P1-CICD-01 #16](https://github.com/321Team/fds-project-baseline/issues/16)

## 채택한 세부 운영안

| 대상 | 운영 방식 | 기존 기준 연결 |
|---|---|---|
| Trivy 바이너리 | 검토한 버전·SHA-256 고정. 새 릴리스/보안 공지의 영향·출처·체크섬·옵션/종료코드 호환성·복구본을 기록하고 독립 리뷰 후 관리자가 교체한다. CI가 latest를 받아 실행하거나 관리자 권한으로 자기 갱신하지 않도록 한다. | 버전 고정·독립 리뷰·최소권한 |
| 취약점 DB | 실제 이미지 Scan 전 공식 공급원의 갱신 필요 여부 확인과 필요 시 갱신. 승인된 통신 경로를 사용하고 메타데이터·시각·DB 해시를 Run에 연결한 전용 사본을 검사에 사용한다. | 최신성·추적성·네트워크 통제 |
| DB 유효성 | NextUpdate는 갱신 필요 판단에 사용한다. 갱신이 필요한데 미갱신, 메타데이터 누락/이상, 미지원 스키마, 다운로드/갱신 오류면 실패 처리한다. NextUpdate를 공급자가 보장한 보안 만료 시각으로 주장하지 않는다. | DB 오류 실패/미검증 처리 |
| 배포 차단 | 미해결 HIGH/CRITICAL, 미승인 예외, 스캐너/DB 오류 시 Push·Deploy 차단. 오류 후 오래된 캐시로 우회해 PASS를 만들지 않는다. | 9/14 결정·CICD-AC-03/05/09 |
| 예외·증적 | CVE·Digest·사유·만료·승인자 단위 예외와 Source/Workflow SHA→Run/Attempt→Scan→Harbor/배포 Digest 추적을 유지한다. | CICD-AC-06/09 |
| 역할 | 이권욱 구현·최종 판정, 이하영 독립 기술 리뷰. Harbor Scanner는 P1-HBR, CI Scan/Digest는 P1-CICD 책임을 유지한다. | 기존 책임 경계 |

P1에서는 검토된 수동 바이너리 교체와 Workflow의 DB 선행 검사를 적용 방향으로 한다.
새 바이너리 자동 교체 cron/timer/Ansible 작업을 추가하지 않는다. 기존 외부 관리 작업이
있다는 사실 또는 없다는 사실은 아직 확인하지 못했다. 발견 시 중복 교체 경로를 확인하고
변경관리로 조정한다. 기존 OS 갱신 서비스를 끄지 않는다.

Trivy 0.74.0은 현재 검증한 버전이다. 무기한 유지 또는 최신 보안 적합성 재평가 완료라는
의미는 아니다. 새 고정 갱신 주기나 7일/30일 DB 캐시 유예는 이 채택에 없다.
수동 toolcheck의 고정 DB·예상 rc=10/1 결과를 실제 이미지 배포 승인으로 확대하지 않는다.

## 검증된 입력과 한계

- PATH 보강 후 [Run 35050018964/1](https://github.com/321Team/infra-cicd/actions/runs/35050018964): merge SHA
  `80d6968b8cf5d145bb37b685d92b3cccf4ecffa7`, 시스템 PATH·탐지 rc=10·DB 누락 rc=1·toolcheck PASS 로그 확인.
- 9/16 12:20 KST 보완 수집: 592개 파일에서 Trivy 참조 0, 제한 도달 없음, 남은 큐 0.
  링크 경로 기록 208개, 제외 기록 26개. 제외 영역·동적 호출·외부 구성관리 부재는 증명하지 않음.
- 수신 archive SHA-256 `93fa18aed7f464eadc311c648b8123aa8bb31a1ad297c99c25cff0ea374b746d`.
- 내부 audit.json SHA-256 `b5dbe23fa8abc4d8a4966df15658714dfc93405c7f0c9dcc074d4ab200aef294`.
  외부/내부 체크섬과 구성 검증 완료. 원시 운영 설정/비밀은 수집 입력에 복제하지 않음.
- 바이너리 root:root/0755 및 SHA-256
  `d89bcc6510a267f11b773398cbf1be5520ce39f9e8b6633178c4487f05b7d791` 일치.

## 구현·정본 편입 작업

1. infra-cicd에 운영 절차와 DB 선행 검사·실패 처리 테스트를 PR로 제출한다.
2. 독립 리뷰와 병합 후 실제 Runner에서 새 DB 준비 경로를 검증한다.
3. 승인된 앱 Source/Test 및 Harbor·K8S·SEC 인계와 연결해 실제 이미지 Scan과 Push/Deploy 차단을 검증한다.
4. v19 Baseline §10, P1-CICD Description/Ticket Pack, 관련 Decision 인계·Release Notes·WEB·Manifest에 통합한다.

이 입력은 새 AC, 네트워크 경로, RBAC 권한, Workload, 확정 일정 또는 자동 병합/발행 권한을
추가하지 않는다. 기존 CICD 관리 진척 50%·Runtime AC 1/10, DELIVERY_GATE=NOT_VERIFIED를 유지한다.
코드 독립 리뷰·병합·새 DB 경로 Runtime·v19 전체 묶음 생성과 최종 발행 리뷰는 별도 잔여다.
