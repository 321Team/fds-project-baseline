# O01 AC07 문서 정정 확인과 Probe223 후속 준비

2026-10-15 KST · 문서 Lead/자료 준비 이권욱 · CODEX_ASSISTED.

| 순서 | 대상 | 현재 상태 |
|---|---|---|
| 1 | AC07 문서 정정 | [CICD PR85](https://github.com/321Team/infra-cicd/pull/85) 이하영 승인 후 10:19:32 KST 병합, merge `0b0412a293dfb00fa1437d484ca012d1a4898412` |
| 2 | [AC07 정정본 확인](AC07_CORRECTION_CONFIRMATION.md) | 원 수행자 이재환의 정정 안내 확인 결과 미수신 |
| 3 | [Probe223 오프라인 세션](PROBE223_SESSION.md) | 고정 입력·명령·기대값과 작성자 사전검증 준비 완료. 수행자 선택·참여·일시와 실제 새 수행은 미확정 |
| 4 | [결과 제출](PROBE223_RESULT_TEMPLATE.md) | 미작성 템플릿. 실제 수행 뒤 기록 |

[AC07 1차 수신·검토 기록](https://github.com/321Team/fds-project-baseline/issues/24#issuecomment-6181949828)에 결과 양식과 첨부5(출력/meta4·보조 스크립트1)의 해시를 남겼다. 사용자·수행자가 제공한 원본은 보존한다. PR85 병합은 문서 정정 완료이며, 원 수행자의 이해 확인이나 O01 전체 인수와 구분한다.

이재환은 Probe223과 운영 코드 K8S86의 기존 독립 리뷰에서 동일 판정기를 이미 실행했다. 같은 사람의 추가 수행은 재확인으로 기록하고 신규 초견 판독과 구분한다. 이전 리뷰 참여만으로 O01 AC에 새 결격 기준을 만들지는 않는다. 새로운 참여자의 재현 가능성을 확인하는 목적이라면 이하영을 후보로 제안하며, 실제 직접 관여 여부·참여 수락·시간은 확인 전이다.

기존 AC07 입력과 같은 evidence `43e26384ae422f2017f1e96e6c1bb5fe46d087d4`를 유지한다. Phase 2 및 새 서버 접속·장애 주입·토큰 발급은 범위 밖이다. 새 실측이 필요한 핵심 검증은 이후 해당 AC·대상·선행·복구를 고정한 별도 작업으로 판단한다. 오프라인 두 사례만으로 전체 O01을 축소하지 않는다.

작성자 점검은 [AUTHOR_PRECHECK.json](AUTHOR_PRECHECK.json), [stdout](AUTHOR_PRECHECK.stdout.txt), [stderr](AUTHOR_PRECHECK.stderr.txt)에 기록했다. 제3자 새 수행 결과가 아니다. 원본 연결은 [SOURCE_INDEX.json](SOURCE_INDEX.json)을 따른다. 문서 인계·판정 기록은 [DOC #24](https://github.com/321Team/fds-project-baseline/issues/24)에 연결하며 기존 AC·Status·일정은 변경하지 않는다.
