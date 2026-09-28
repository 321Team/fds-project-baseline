# Project #1 자동 동기화 — 운영 후보

대상: https://github.com/orgs/321Team/projects/1
원본: `321Team/fds-project-baseline`의 GitHub Issues 전체(open/closed, PR 제외).
기존 `TICKET_SYNC_POLICY.md`의 상단 속성표·식별·상태 검증 규칙을 재사용한다.
이는 프로젝트 표시 자동화이며 문서 정본 발행 또는 Runtime 인수 판정이 아니다.

## 동작

- 원본 이슈를 전체 페이지 조회하여 17개 속성, Record ID 중복, 제목/marker,
  본문 Status/상태 라벨/실제 state/state_reason, Lead/Assignee, Support, 날짜, Milestone을 검증한다.
- 신규 이슈도 같은 검증을 통과해야 포함한다. 일반 메모 등 규격 밖 이슈가 생기면 전체 실행 STOP.
- Project #1의 Status, Record ID, Phase, Priority, Support, Plan Start, Plan End,
  Schedule Note만 원본에서 갱신한다. Todo는 본문 To Do와 대응한다.
- 없는 사용자 필드는 첫 apply에서 생성한다. Status 필드와 필요한 상태 선택값은 기존 값이어야 한다.
  In Review/Blocked/Cancelled가 향후 사용되면 해당 옵션을 먼저 UI에서 추가한다.
- 신규 이슈를 연결하고 차이가 있는 필드만 갱신한다. TBD는 날짜 필드를 비운다.
- 제목/담당자/라벨/Milestone은 원본 이슈 필드를 그대로 사용한다.
- 뷰·그룹·필터·로드맵 설정, 프로젝트 이름/공개범위, 원본 body/AC/상태/라벨/담당자는 수정하지 않는다.
- 보관된 대상은 자동 복원하지 않고 STOP. 프로젝트에서 제거된 유효 이슈는 다시 추가된다.
- 삭제/이관된 이슈의 옛 프로젝트 카드는 자동 제거하지 않는다. 수동 확인 대상이다.
- 실행 시점(2026-09-28 변경, 주 1회):
  - 정기 실행: 매주 월요일 KST 08:17 전체 재대조 1회. 이슈 이벤트 트리거는 없다.
  - 이슈 생성·수정·라벨·담당자·Milestone·종료 등 모든 변경은 다음 정기 실행에서 반영한다.
    최대 약 7일 지연된다(스케줄 지연 제외).
  - 즉시 반영이 필요하면 Actions → FDS Project 1 Sync → Run workflow(main, `apply`)로 수동 실행한다.
    신규 이슈 발행, Status 변경, Gate·마감 직전 보드 확인 때는 수동 실행을 권장한다.
  - 변경 사유: 실행마다 전체 이슈를 재대조하므로 이벤트별 실행이 중복이었다.
    2026-09 GitHub Free 무료 한도 2,000분 중 1,235분을 사용했고, 이 저장소가 가장 많이 썼다.
    실행의 약 90%(665회 중 607회)가 이슈 이벤트였다.
  - 스케줄은 지연될 수 있어 실시간 SLA는 없다.
    보드 수동 변경은 다음 정기·수동 실행에서 원본 값으로 돌아간다.
- 이슈 본문과 라벨을 순차 수정하는 중간 상태에서 STOP할 수 있다. 수정 완료 후 재실행한다.
  이벤트 트리거를 없애 이 중간 상태 STOP의 빈도도 낮아진다.
  (참고: 2026-09 이슈 이벤트 실행 중 조회된 573회에서 246회가 failure였다.)
- 변경 직전 원본·프로젝트 값을 재조회하고 변경 후 다시 검증한다. API는 원자적 트랜잭션이 아니므로
  재조회와 쓰기 사이의 동시 수정 가능성이 완전히 사라지지는 않는다. 실행 중 수동 필드 편집은 피한다.
- API 실패/중단 시 부분 반영 가능. 자동 롤백하지 않고 결과 JSON의 journal을 확인한 후 재실행한다.
- 주기 실행까지 위 지연이 걸릴 수 있고(서비스 지연 제외), GitHub Actions 사용량 제한 시 실행되지 않는다.

## GitHub 웹에서 인증 등록

1. 조직 Settings → Developer settings → GitHub Apps → New GitHub App.
   이름 예: `321Team FDS Project Sync` (이미 사용 중이면 고유한 이름 사용).
   Homepage URL: `https://github.com/321Team/fds-project-baseline`.
   Webhook Active는 해제한다. 외부 서버·callback·사용자 OAuth 승인은 필요하지 않다.
2. 권한: Repository **Issues: Read-only**, Organization **Projects: Read and write**.
   Metadata 읽기는 기본 권한. 코드 checkout은 workflow의 GITHUB_TOKEN을 쓴다.
   설치 범위는 Only on this account. 다른 쓰기 권한은 필요하지 않다.
3. 앱 생성 → Install App → 321Team → Only select repositories → fds-project-baseline.
4. 앱 General 화면의 Client ID를 복사. Generate a private key로 PEM 다운로드.
5. 저장소 Settings → Secrets and variables → Actions에서 등록:

| 종류 | 이름 | 값 |
|---|---|---|
| Variable | FDS_PROJECT_APP_CLIENT_ID | 생성한 앱의 Client ID |
| Secret | FDS_PROJECT_APP_PRIVATE_KEY | PEM 파일 전체 내용(시작/끝 줄 포함) |
| Variable | FDS_PROJECT_SYNC_ENABLED | 초기에는 `false` |

개인키는 GitHub Secret에 직접 등록한다. 채팅·Issue·PR·커밋에 넣지 않는다.
현재 대화 연결은 앱 생성/Secret 등록/Projects 편집을 수행할 수 없다.

## 활성화 순서

1. 저장소 기존 정책대로 독립 리뷰·HEAD 확인 후 PR을 수동 병합한다. 이 후보는 main을 직접 수정하지 않는다.
2. Project → … → Workflows에서 Auto-add 외 Status를 바꾸는 기본 workflow와
   Status→close/reopen, Auto-archive를 꺼 이 자동화와 충돌하지 않게 한다.
   특히 기본 `Item closed → Done`은 Cancelled 구분을 검증하지 않으므로 끈다.
   Auto-add는 유지 가능하지만 이 코드가 신규 항목 추가도 처리하므로 필수는 아니다.
3. 저장소 Actions → FDS Project 1 Sync → Run workflow → main / mode `check`.
4. 결과 `CHECK_READY`, source_summary와 missing_fields/plan 확인. 첫 실행은 미생성 필드가 있어도 계획 가능.
5. Run workflow → main / mode `apply`. `SYNC_VERIFIED`와 실제 보드 값을 확인한다.
6. Variable `FDS_PROJECT_SYNC_ENABLED=true`로 변경한다. 이후 주기 실행 활성화.
7. 이후 정상적인 이슈 갱신 한 건에서 자동 실행 결과를 확인한다. 시험 목적으로 AC/완료 상태를 바꾸지 않는다.

## 결과·복구

- CHECK_READY: 읽기 전용 계획 검증 성공. 쓰기 없음.
- SYNC_VERIFIED: 그 실행 시점 전체 대상 원본과 프로젝트 필드 재검증 성공.
- STOP: 인증/형식/충돌/동시 수정/API 문제. 성공으로 해석하지 않는다.
- remote_write_state=PARTIAL_OR_UNKNOWN: 요청된 쓰기의 일부 또는 전부가 적용됐을 수 있음.
- Actions의 `project-1-sync-...` artifact에 plan/journal/result 보존(7일, 현재 저장소 상한과 동일).
  본문 전체는 저장하지 않지만 Support/계획/상태가 포함되므로 저장소 접근 범위 내에서 취급한다.
- 앱 생성 단계에서 실패하면 결과 파일이 없을 수 있다. 해당 Actions 단계 오류를 확인한다.
- 자동 동기화 중지: `FDS_PROJECT_SYNC_ENABLED=false`. 진행 중인 실행은 Actions에서 별도 취소.
- Secret 갱신은 앱 키 재발급 후 같은 Secret 이름으로 교체한다.

## 검증 범위

로컬 단위/모의 API 검증은 실제 GitHub App·Projects 실행 검증과 다르다.
원격 check/apply 전에는 자동 동기화 적용 완료로 판정하지 않는다.

공식 참고:
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/automating-projects-using-actions
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-built-in-automations
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows

## Actions 경고 2건 보완

- `actions/checkout`과 `actions/upload-artifact`는 각각 공식 `v7.0.1`의 전체 Commit SHA로 고정한다.
  두 고정 Commit의 `action.yml`에서 `runs.using: node24`를 확인했다.
  `actions/create-github-app-token`의 기존 고정 SHA와 권한은 유지한다.
- Upload Artifact의 `archive: true`를 명시해 기존 ZIP 형식과 Artifact 이름을 유지한다.
  `retention-days: 7`로 현재 저장소 보관 상한과 맞춘다. 기존 Artifact의 만료일을 연장하지 않는다.
- checkout은 `persist-credentials: false`를 유지한다. 이 워크플로는
  `schedule`·`workflow_dispatch`에서 main 코드만 실행하므로(2026-09-28 이전에는 `issues` 포함),
  v7의 fork PR checkout 허용 옵션을 추가할 필요가 없다.
- 로컬 구조 검증만으로 경고 해소를 확정하지 않는다. 독립 리뷰·병합 후
  새 main에서 `check`를 실행해 `CHECK_READY`, Node.js 20 경고 없음,
  보관기간 상한 경고 없음, 결과 ZIP 다운로드 및 7일 보관을 확인한다.
  기존 실행 기록의 경고는 소급 삭제하지 않는다.

공식 버전 근거:
- https://github.com/actions/checkout/releases/tag/v7.0.1
- https://github.com/actions/checkout/blob/3d3c42e5aac5ba805825da76410c181273ba90b1/action.yml
- https://github.com/actions/upload-artifact/releases/tag/v7.0.1
- https://github.com/actions/upload-artifact/blob/043fb46d1a93c77aae656e7c1c64a875d1fc6a0a/action.yml
