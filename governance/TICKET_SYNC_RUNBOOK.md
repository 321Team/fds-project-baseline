# Ticket synchronization runbook

## 실행 환경

작업용 PC 또는 관리 서버의 `321Team/fds-project-baseline` 체크아웃에서 실행한다. Ansible Playbook, kubeadm, 운영 서버 설정은 실행하지 않는다. GitHub Issue 자체는 Git commit/merge와 별개인 원격 기록이다.

필수: Python 3.9 이상(표준 라이브러리), GitHub CLI `gh` 및 기존에 로그인된 업무 계정. 인증 토큰을 파일/채팅/로그에 넣지 않는다. 다음 명령은 조회만 한다.

```bash
git remote get-url origin
gh auth status
python3 scripts/ticket-sync.py --help
```

origin이 `321Team/fds-project-baseline`인지 확인한다. 새 복제 디렉터리 경로를 임의로 기존 Ansible 디렉터리와 겹치지 않는다. 스크립트는 저장소를 고정하고 source map은 자신의 저장소 루트에서 읽는다.

## 1. 로컬 감사와 테스트

```bash
python3 -m unittest discover -s tests -p 'test_ticket_sync.py'
python3 scripts/ticket-sync.py audit --snapshot /검증된/issue-snapshot.json
```

감사 결과의 미확인 값과 native Type·Milestone 미적용을 확인한다. 메타데이터 무변경/라벨 일치만으로 전체 PASS를 선언하지 않는다. 원본 체크박스 및 종결 내용 검토는 별도의 근거 심사다.

## 2. 실제 상태 조회 및 계획 생성

```bash
python3 scripts/ticket-sync.py plan --output ticket-sync-plan.json
sha256sum ticket-sync-plan.json
```

조회 범위: 전체 Issue(모든 페이지, PR 제외), 기존 Label/Milestone, 조직에서 사용 가능한 Issue Type. 이번 연결 도구에 없는 native Type/Milestone 기능은 사용자의 정상 로그인 `gh` 환경에서만 수행한다. 403/404 또는 인증 실패 시 중단한다. 유료 플랜·권한 변경을 자동 요구하지 않는다.

계획의 `changes`, `unresolved`, `blockers`를 검토한다. `--native` 없이 계획하면 Label/Lead만 대상이다. native 동기화도 하려면 다음 명령을 사용한다.

```bash
python3 scripts/ticket-sync.py plan --native --output ticket-sync-native-plan.json
sha256sum ticket-sync-native-plan.json
```

정확한 기존 Type 이름이 없으면 잘못된 Task로 대체하지 않고 `type:*` 라벨을 유지하며 미반영으로 기록한다. Milestone이 없으면 자동 생성하지 않는다. `GITHUB_MILESTONE_MAP.md`의 검증된 카탈로그를 근거로 명시적 생성·설정 검토가 선행되어야 한다. 복수 Gate·미확정 20건은 건너뛰고 예외로 보고한다. 인가된 Type/Milestone 정의 또는 목표 매핑을 바꿨다면 새 계획을 생성한다.

## 3. 검토한 계획에 한해 반영

다음의 SHA는 앞 단계에서 확인한 계획 파일의 실제 64자리 SHA-256으로 바꾼다. 단순 명령 실행을 계획 승인으로 간주하지 않는다.

```bash
python3 scripts/ticket-sync.py apply \
  --plan ticket-sync-native-plan.json \
  --expect-sha256 <확인한_64자리_SHA256> \
  --confirm-repo 321Team/fds-project-baseline \
  --output ticket-sync-apply.json
```

24시간이 지난 계획, source map 변경, source Issue 변경, 카탈로그 변경은 중단한다. 전체 사전 점검 후 건별 재조회하고 변경을 적용한다. 응답을 다시 읽어 body/title/state/기존 수동 메타데이터 보존 여부를 확인한다. 기존 Label/Assignee 전체를 덮어쓰는 결과가 되지 않게 계획된 병합 집합만 적용한다.

실패하면 결과 파일의 적용 완료 번호부터 확인한다. 자동으로 main merge/Release/Notion update를 이어서 수행하지 않는다. 재실행 전 새 계획을 만든다.

## 4. 인계

- 정책 후보 PR: 독립 검토 전 정본 아님. `CURRENT.md` 및 Release 불변.
- 동기화 결과: 변경 전후 hash, 적용 Issue 번호·필드, 재조회 결과 및 남은 예외.
- Type fallback/native 미반영과 Milestone 미반영을 별도 계수.
- 원본 #59/#61 속성, #46 일정/G5 불일치 등은 정보 복원/결정 후 별도 승인 변경으로 처리.

API 참고: [Issue update](https://docs.github.com/en/rest/issues/issues#update-an-issue), [Milestones](https://docs.github.com/en/rest/issues/milestones), [Organization issue types](https://docs.github.com/en/rest/orgs/issue-types). GitHub 기능 지원과 현재 연결 도구의 기능 노출 범위는 서로 다르다.
