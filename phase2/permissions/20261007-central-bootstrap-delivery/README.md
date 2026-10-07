# 중앙 bootstrap 후보 배포 묶음 — 2026-10-07

AI 보조: Codex. 책임: #35, 연계: #37. 상태: 후보 모의 시험 PASS / 독립 리뷰 요청 대상 / AWS·사람 역할 부여 NOT_RUN.

[소스·실행·중단/복구 절차](../20261007-central-bootstrap/README.md)를 먼저 확인한다. 이 archive는 helper, template, Agent 비교 입력, provenance, 시험, README, source manifest의 7개 파일을 원문 바이트 그대로 포함한다. 실제 수집 자료·credential은 없다. 이전 collector 설치가 필요하지 않다.

이 디렉터리의 archive와 sidecar를 검토·병합 SHA로 고정해 함께 다운로드한다. 아래 값과 source SHA256SUMS를 확인한 뒤 같은 리뷰 소스를 실행한다. 패키지 수신·해시 일치가 독립 리뷰 또는 AWS 적용 완료를 뜻하지 않는다.

- archive: `fds-central-bootstrap-20261007.tar.gz`
- SHA-256: `10fb148bb96f7e093efaa87dfec9c2cf969e023051644e0c784f0aaaf8323cf1`
- test: Python unittest 14건 PASS (mock), source policy content 변경 0, template 4개 자원·Retain 검사 PASS
- 실제 AWS validate/create/readback/runtime: NOT_RUN

새 CloudFormation 구현 제안과 IAM runtime 코드이므로 REVIEW_AUTHORITY_POLICY §2·§3·§4의 독립 리뷰·Lead 판단을 따른다. Reviewer 지정 후 실제 승인·병합·적용은 별도 상태로 기록한다. 기존 PR #147의 중앙 시뮬레이션 수신 결과를 다시 실행할 필요는 없다.
