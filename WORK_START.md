# 같은 사양과 같은 작업 상태에서 시작하기

Work는 계획·판단·통합 검토를, Cloud Codex는 구현·반복 검증을 담당한다.
두 도구의 공통 기준은 이 저장소와 관련 GitHub 기록이다.

| 항목 | 읽을 위치 |
|---|---|
| 발행 사양 | `handoff/baseline.lock.json` → docs-v3.1.18의 고정 Commit |
| 현재 작업 상태 | Task에 지정한 Issue/댓글/PR/Review를 GitHub에서 새로 조회 |
| 공통 작업 규칙 | `AGENTS.md`, `handoff/OPERATING_RULES.md` |
| 기준 결정 | `handoff/DECISIONS.md` |
| 인계 양식 | `handoff/task.template.json`, `handoff/RESULT_TEMPLATE.md` |
| 다음 작업과 현재 도입 범위 | `handoff/NEXT_ACTIONS.md` |
| Cloud 준비·공용 PC | `handoff/CLOUD_SETUP.md` |
| 효과 측정 | `handoff/MEASUREMENT.md`, `handoff/measurement.csv` |

## 현재 발행 기록과 역사 기록 구분

2026-09-11 조회에서 docs-v3.1.18은 Release ID 386739994로 발행되어 있으며
Tag는 `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`를 가리킨다.
이는 조회 시점 기록이다. 이후 작업에서는 검증기를 통해 재확인한다.

v3.1.18의 `CURRENT.md`에 남아 있는 NOT PUBLISHED 문구와 README의 후보 설명은
발행 전 준비 시점의 기록이다. 사후 문구 수정으로 이미 발행된 Checksum을 바꾸지 않는다.
현재 발행 여부는 실제 Release/Tag/Assets와 승인 기록으로 확인한다. Kubernetes 저장소의
`docs/UPSTREAM_LOCK.json`에 있는 v3.1.17 역시 2026-09-09 인계 당시 기록이며,
현재 사양 선택에는 이 공통 lock과 실시간 검사를 사용한다. 파일 사이의 다른 충돌은
임의로 해결하지 않고 Work에서 영향과 승인 근거를 확인한다.

## 작업 흐름

1. 승인된 공통 지침 Commit을 Work와 Codex가 함께 연다. 아직 Draft PR의 파일이면
   도입 준비·검증에만 사용하고 운영 적용 완료로 표시하지 않는다.
2. Task를 채운다. 한 Record ID/한 목적, 저장소, 허용 경로, AC, 관련 Issue·PR,
   증적 위치와 검사 명령을 지정한다. `task.template.json` 자체는 빈 필드 때문에 실행되지 않는다.
3. GitHub 정상 인증이 가능한 신뢰 환경에서 receipt를 만든다.

```bash
python scripts/shared_context.py capture --task /tmp/task.json --out /tmp/context-start.json
python scripts/shared_context.py check --receipt /tmp/context-start.json --worktree /path/to/task-repository
```

4. 같은 Task와 receipt를 Work와 Codex에 제공한다. task SHA/context_id가 다르면
   진행하지 않는다. cloud checkout과 증적 경로는 receipt에 기록된 Commit으로 읽는다.
   검사기는 대상 checkout의 origin, base 조상 관계, 허용 경로 밖 변경도 확인한다.
   작업 branch HEAD는 별도 기록한다. 모호한 업무 판단은 Work의 결정 기록으로 확정한다.
5. 지정 범위 구현과 필요한 검증 후 동일 check를 다시 실행한다. 새 상태가 감지되면
   덮어쓰지 않고 차이를 검토한 뒤 새 Task/receipt로 재인계한다.
6. `RESULT_TEMPLATE.md` 형식으로 변경 Commit·검사·증적·미완료 Gate를 남긴다.
   Draft PR → 정확한 HEAD 독립 검토 → 수동 병합. 배포·현장 실행은 별도 기존 Gate를 따른다.

Receipt는 관측한 상태의 식별값이며 승인이나 서명이 아니다. GitHub와 편집 사이에
원자적 잠금을 거는 기능이 없으므로 최종 실행 직전에도 기존 티켓 승인 절차를 따른다.
