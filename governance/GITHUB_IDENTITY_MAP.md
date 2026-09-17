# GitHub Identity Map

2026-09-10 계정·배정 확인 이력. 2026-09-18 [Lead 위임 정책](REVIEW_AUTHORITY_POLICY.md) 추가: 기존 담당을 재배정하지 않고 각 업무 Lead에게 코드 외 절차의 판단을 위임한다.

| 실명 | GitHub 계정 | Issue 업무 배정 | 정본 권한 경계 |
|---|---|---|---|
| 이권욱 | GWONUK | Lead인 티켓의 Assignee | 기존 정본 운영·승인 규칙 적용 |
| 이하영 | hayeounglee | Lead인 티켓의 Assignee | 기존 정본 리뷰·승인 규칙 적용 |
| 이재환 | supreme33-kr | 기존 Application/Data/Monitoring/QA 업무 Issue 배정 보존 | 정본 승인·리뷰·병합·발행 역할 제외 |

근거: 사용자 2026-09-07 계정·역할 제한 확인과 현재 #4~67의 실제 Assignee. 정본 리뷰 소유권은 `.github/CODEOWNERS` 및 `RELEASE_POLICY.md §5`의 GWONUK/hayeounglee를 유지한다.

이 저장소의 운영 티켓에 Assignee가 있다는 이유로 정본 파일의 Lead/Reviewer 권한을 부여하지 않는다. 이재환의 기존 운영 Issue 배정은 업무 추적이며 정본 승인 권한이 아니다. Support는 기존 본문의 풀네임으로 유지하고 자동 배정·멘션·리뷰 요청을 하지 않는다. 현재 64건의 Lead↔Assignee 불일치는 0건이므로 이번 배정 변경은 없다.

향후 새 계정은 실명 유사성으로 추정하지 않고 사용자 확인/공식 프로젝트 기록과 현재 저장소 배정 가능 여부를 검증한다. GitHub 계정 변경은 권한 변경 승인과 별개다.

## 2026-09-18 절차 변경의 적용

위 정본 역할 제한은 업무 Lead의 자체 실행·검증·인수·종결을 금지한다는 뜻이 아니다. 이재환도 기존 Application/Data/Monitoring/QA 티켓의 Lead 범위에서 코드 외 절차를 결정한다. 정본 발행 담당과 계정 권한은 기존 범위를 유지한다. 독립 리뷰는 코드 병합 시에만 필수이며, 코드 외 절차에서 Support의 별도 승인을 의무화하지 않는다. 문서 전용 PR은 해당 문서 Lead가 결정하고, 정본 파일의 판단은 기존 정본 Lead가 맡는다. 이 개정으로 Assignee·CODEOWNERS·GitHub 권한을 변경하지 않는다.
