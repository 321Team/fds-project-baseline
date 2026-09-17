# PR #73 리뷰 의견 대응

리뷰 원문: https://github.com/321Team/fds-project-baseline/pull/73#issuecomment-5713453681
작성자: 이하영 / hayeounglee · 2026-09-17 20:16:37 KST. 일반 댓글이며 GitHub APPROVED 제출과 구분한다.

| 요청 | 조치 | 확인 방법 |
|---|---|---|
| v19 전체 문서 세트·WBS·Manifest·SHA256SUMS·ZIP 완성 후 병합 | Baseline·67개 Description/원문·Ticket Pack·58행 WBS/9탭/2차트·WEB·Interface/Decision/CR·Milestone·아키텍처·Release Notes 완성. 결정적 ZIP 생성 | scripts/verify-v19-candidate.py, verify-canonical-release.sh, build-canonical-package.py |
| CURRENT의 v18 NOT PUBLISHED를 실제 발행 상태로 정정 | docs-v3.1.18 tag·2026-09-11 11:23:47 KST 발행·4 Asset 명시, 작성 당시 문구는 역사적 설명으로 분리 | CURRENT.md Publication evidence |

이번 검증은 STATIC 문서/원본/계산/해시 대조다. 외부 저장소의 제출 영수증 검증·MOCK 시험·CI 기록·코드 병합·Runtime·Gate를 각각 구분한다. 기존 v18 태그/Release/Asset은 불변이다.

기존 CI는 startup_failure이며 Jobs 0개였다. 로컬 검증을 CI PASS로 기록하지 않는다. 새 HEAD의 CI 결과는 PR에서 재조회한다.

REVIEW_PENDING: governance/RELEASE_POLICY.md §6의 최소 1인 독립 Reviewer 승인과 검토 HEAD 확인 후 수동 병합한다. 사용자 배포 지시는 수신했고 추가 사용자 허가는 요청하지 않는다. 내용 병합 후 CURRENT/발행 상태를 별도 최종화한다.
