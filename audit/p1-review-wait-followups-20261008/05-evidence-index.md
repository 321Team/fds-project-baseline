# 5. 본 세션 범위의 문서·증적 연결

CODEX_ASSISTED. [P1-DOC-01](https://github.com/321Team/fds-project-baseline/issues/24) 증분 연결표.
전 Phase1 AC 재판정이 아니며 별도 세션의 증적 원본을 복사·수정하지 않는다.
GitHub 조회 상태/HEAD는 source-snapshot.json, 기존 시험 수치는 아래 원본 기록에 근거한다.

| 대상 | 소스/증적 | 실제 확보 단계 | 남은 단계 |
|---|---|---|---|
| 새 APP Test/Build/Scan | [증적147](https://github.com/321Team/fds-project-evidence/pull/147) | 새 Run 실제 PASS; 이번 APP42파일 불변·인계26항목 MATCH | 현재 HEAD 리뷰/병합 판단, Push/Deploy 미실행 |
| Push 인계 | [CICD65](https://github.com/321Team/infra-cicd/pull/65) | 초안·현장 도구 조회 및 receipt 연결 | Robot/승인/fresh 입력, actual Push/원격 digest/정리 |
| Deploy Session | [CICD66](https://github.com/321Team/infra-cicd/pull/66) | 구현·합성/POSIX 시험527·CI | 독립 리뷰/병합/Runtime |
| Deploy Workflow/broker | [CICD67](https://github.com/321Team/infra-cicd/pull/67) | 구현·누적 시험552·CI | PR66 선행, 정확한 입력·Runtime/Health/E2E/rollback |
| Harbor 주소 후보 | [HBR12](https://github.com/321Team/infra-harbor-trivy/pull/12) | 단위10·CI·현장 읽기 전용 config delta 검증 | source 검토/소비 경로 구현·적용·자동기동 재시험 |
| Harbor 관측기 | [HBR13](https://github.com/321Team/infra-harbor-trivy/pull/13) | 단위19·CI | source 검토·현장 관측, 기동 순서/수신 성공 판정 별도 |
| DNS worker02 범위 | [Ansible74](https://github.com/321Team/infra-ansible/pull/74), [증적154](https://github.com/321Team/fds-project-evidence/pull/154) | source·양 엔진 syntax74/unit165·실제 CI Runner 정리 | 독립 리뷰·worker02 actual verify·role별 검증·운영 전환 |
| 운영 경로/HBR 오류/Deploy 준비 | [증적153](https://github.com/321Team/fds-project-evidence/pull/153) | 기존 원본 회수·선택 필드·원인 입력 및 준비표 | 독립 증적 검토/편입, 각 Runtime 잔여 |
| MON 후보 verify | [증적150](https://github.com/321Team/fds-project-evidence/pull/150) | 별도 후보 checkout의 제한된 verify | 검토/편입·운영 전환/전체 role 적용 별도 |
| Edge/P4 다른 세션 | [증적156](https://github.com/321Team/fds-project-evidence/pull/156), [최신 작업 기록](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6044114291) | 현재 구성 P4 완료 보고, 조기 전환 사전 준비 | 전환·전환 후 P4/C2/C3·종결은 해당 세션 기록으로 확인 |

누적 시험527과552는 합산하지 않는다. 19개 합성시험은 Harbor 현장 관측19회가 아니다.
PR 병합/증적 편입과 실제 Runtime 성공을 구분하며 승인되지 않은 위험 수용이나 Due 변경은 기입하지 않는다.
위 산출물이 다음 Freeze 입력이지만 P1-HA/P1-DR/P1-E2E 등 #24의 다른 선행조건은 이번 범위에서 검증하지 않았다.
따라서 정본/Freeze/Phase1 Close는 변경하지 않는다.

Edge 인증 전달 절차의 후속 중단/수정 기록6044215211은 [작업창 후보](06-window-candidates.md)에 반영했다.
이전 전달 파일과 민감 가능 출력은 이 준비 묶음의 소비/편입 대상이 아니다.

새 실제 실행 이후 갱신할 최소 항목: 사용 source/Run/Attempt, host/account, KST 시작·종료/rc,
원본 경로·hash, 성공/실패 범위, 정리/복구 및 잔여, 독립 증적 리뷰·편입 링크.
