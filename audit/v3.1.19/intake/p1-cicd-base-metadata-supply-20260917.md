# P1-CICD-01 OID-03 base metadata 수집 — 사용자 채택 입력

상태: **APPROVED_INPUT / ADOPTED_BY_USER / RUNTIME_NOT_EXECUTED**.
운영 정본: v3.1.18. v3.1.19 후보 수집이며 NOT RELEASED.

## 근거

사용자 이권욱은 실서버 선행 작업 중 1번 복구 후 로컬 점검을 실행했고,
이후 “우리 정본 및 정본 후보를 기준으로 권장안은/”을 요청했다.
Runner 두 Docker Hub 호스트·library/python metadata·최대60분·오류/redirect 중단
권장안에 대해 **“착수”**를 지시했다.
[infra-cicd #11 사용자 채택·범위·수집 준비 기록](https://github.com/321Team/infra-cicd/issues/11).

- 정본 [v18 §15.1.2 OID-03 / §15.2](https://github.com/321Team/fds-project-baseline/blob/docs-v3.1.18/baseline/FDS_Project_Implementation_Baseline_v3.1.18.md):
  사전 반입 또는 HTTPS Destination·Owner·Expiry, 미정의 인터페이스 기본 차단,
  한시 허용의 만료·제거 조건. OID-03 책임 이하영/이권욱 유지.
- [Trivy 채택 운영안](p1-cicd-trivy-update-policy-20260916.md): 승인 경로·오류 차단 유지.
  이 기존 입력이 Docker Hub/PyPI 접근 권한을 포괄 부여한 것은 아니다.
- [DEC-P1-EGRESS-01 #78](https://github.com/321Team/fds-project-baseline/issues/78):
  .56:3128은 Alertmanager→Discord 전용, CICD 공급으로 확대하지 않음.

## 이번 채택 범위

| 항목 | 값 |
|---|---|
| 실행 | cicd-runner01 / 10.250.10.20 / server01_cicd-runner UID1000, 이권욱 |
| HTTPS 목적지 | auth.docker.io:443, registry-1.docker.io:443 |
| 읽기 권한/대상 | repository:library/python:pull; python:3.12-slim root index 또는 manifest, linux/amd64 manifest 및 그 config 원본 |
| 시간 | 서버 첫 실제 실행 T0부터 최대60분. 시작·만료 기록 고정, 재실행 자동 연장 없음. 실제 시각은 아직 없음 |
| 경로 | 기존 resolver·mgmt-gw01 경로. TLS 검증 유지. proxy/CA override가 있으면 우회하지 않고 중단 |
| 중단 | 모든 redirect, TLS/HTTP 실패, 크기·digest 불일치, 만료. 추가 호스트가 필요하면 별도 범위 정의 또는 승인 환경에서 사전 반입 |
| 변경 | DNS/NAT/방화벽/CA/서비스 변경 없음. 미정의 egress Permanent 허용 금지. 추가 임시 규칙이 필요하면 실제 만료·제거 확인 |
| 후속 | layer·PyPI·빌드 의존성 공급은 별도 미확정. 전체 OID-03 공급 완료·앱 Source/Delivery 승인으로 확대하지 않음 |

60분은 이번 사용자 채택값이며 기존 정본의 고정 수치가 아니다.
로컬 추적값 P1-CICD-OID03-20260917-01은 신규 정본 D/IF 번호가 아니다.
이 입력은 사용자 수동 수집 범위 채택이며 이하영/이재환의 코드 리뷰를 생성하지 않는다.
클라이언트 host/path/time 제한은 네트워크 방화벽 집행·만료 증명이 아니다.
현재 NETWORK_ENFORCEMENT=NOT_VERIFIED이며 기존 차단을 우회하거나 광범위 허용하지 않는다.

## 준비 구현과 검증

[infra-cicd PR #17](https://github.com/321Team/infra-cicd/pull/17),
HEAD `1fb5ef3fdba0aa18aef16656c1ee736aaca3055b`.
계정 DB 홈·대상 확인, 표준 Python HTTPS, bounded raw 응답, token 비노출,
고정 작업창 재사용, 모든 redirect 중단, 새 owner-only 증적 파일만 생성한다.
임의 경로 입력·기존 파일/홈 chmod/chown/삭제·추출·정리·subprocess 없음.

- 신규14 + 기존Delivery22 = 로컬36 STATIC/MOCK PASS.
- [GitHub CI Run35144412110](https://github.com/321Team/infra-cicd/actions/runs/35144412110),
  Job104956698464 원본111 PASS(17+11+47+36), SOURCE_VALIDATION=PASS.
- 원격 추가3파일과 로컬 바이트 일치. 수집기 SHA-256:
  `5356bd4a0d9b924961e0b151b5921fd49d972a1e29d97f66fc16768a611ee187`.
- 기존 사용자 부재 대체 지시에 따라 이재환(supreme33-kr) 요청 등록.
  코드 독립 리뷰 PENDING, PR 미병합. PR별 시험 수를 합산하지 않는다.
- 위 시험 HTTP 응답은 합성 입력이다. 실제 registry 수집은 NOT_EXECUTED,
  actual base digest·raw 원본은 미수신. PR #16 전체 오프라인 검증은 별도다.

## 1번 로컬 점검 증적 인수

사용자 제출 화면 `b3de09d3-7d59-4108-b94e-604f6261bb0e.png`,
시각 2026-09-17T04:07:56+09:00, SHA-256
`3a4fdf70b5138e89dbb26eb628e7e7bfe85230ac434958c37f37a48e72d7cef3`.
홈 UID1000/mode0700/접근3종true, 서비스 loaded/active/running·PID14210,
User=server01_cicd-runner, 기본 경로10.250.10.1/ens160,
Python3.12.14/Podman6.1.0 확인. 증적은 사용자 제출 화면이며 원격 attestation이 아니다.
홈 내부 전체 복원·GitHub Online/신규 Job 수신·앱 Runtime으로 확대하지 않는다.
원본은 대화 첨부 수신 상태이며 GitHub evidence 원본 편입 완료를 주장하지 않는다.

## 후속과 편입 범위

1. 사용자가 고정 수집기를 대상 일반 계정에서 실행하고 원본 archive/sha256을 인계.
2. 원본 byte/hash/size/platform 검증 후 앱 두 Dockerfile pin·최종40자리 Source 승인.
3. layer/PyPI 공급·시험 범위·승인 Workflow를 연결해 실제 Test→Build→Scan.
4. 이후 Harbor Trust/Robot·Worker Pull·K8s 최소권한·실패 차단·복구 인수.
5. 최종 v19 Baseline OID-03 상태, CICD 설명/Interface·Release Notes/WEB/배포 묶음에 통합.

이번 targeted intake는 사용자 채택·도구 준비·복구 후 로컬 출력 인수만 수집한다.
다른 티켓 전수 조회나 Runtime 재실행이 아니며 Runtime AC1/10,
잠정 관리50%, 전체 DELIVERY_GATE=NOT_VERIFIED 유지.
v19 전체 묶음 NOT BUILT, Publication NOT READY이며 운영 정본 v18을 소급 수정하지 않는다.
