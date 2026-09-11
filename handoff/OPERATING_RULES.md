# 역할과 공통 출처

| 작업 | 주 작업 장소 | 판단/완료 근거 |
|---|---|---|
| 목적·범위·AC·WBS·Gantt·일정·우선순위 | Work | 발행 Baseline와 승인된 CR/결정 |
| 보안·아키텍처 판단·티켓 관계·통합 검토 | Work | 승인 기록, 실제 Issue/PR, 수신 증적 |
| Ansible·Python·Shell·YAML·Workflow 구현 | Cloud Codex | Task 허용 경로와 정확한 source HEAD |
| 정적/모의검증·Checksum·재현 패키징·PR 초안 | Cloud Codex | 실행 명령·환경·결과·생성물 Hash |
| VMware·OS·노드·네트워크·배포 시험 | 교육장 승인 실행 환경 | 실제 로그·실행 시각·대상·검토 |
| 발표·문서 최종 구성·종료 판단 | Work | 위 결과 통합, 독립 승인 및 잔여 Gate |

## 출처의 우선순위는 필드별로 정한다

- 계획/설계/담당/일정/AC: 발행 정본 + 해당 필드를 바꾸는 승인된 CR.
- 실제 진행/시험/승인: Issue 본문과 댓글, PR의 정확한 HEAD와 Review,
  `fds-project-evidence`의 수신 Commit·파일·SHA-256.
- labels/Project/Notion/웹 상태 화면: 파생 표시. 상태 정본으로 역수입하지 않는다.
- 대화/로컬 사본/과거 인수 문서: 보조 정보. 조회할 수 없으면 UNVERIFIED로 멈춘다.
- 코드가 존재함, main 병합됨, 설계 승인됨, 서버에 적용됨은 각각 다른 사실이다.

## 상태 기록 규칙

| 필드 | 허용 표현 예 | 필요한 증거 |
|---|---|---|
| STATIC / MOCK | PASS, FAIL, NOT_RUN | 명령·대상 Commit·환경·출력 |
| CI | PASS, FAIL, NOT_RUN | 실제 Actions Run URL 및 Commit |
| RUNTIME | PASS, FAIL, NOT_RUN, UNVERIFIED | 실제 대상·로그·수신 Commit/Hash |
| REVIEW | APPROVED, CHANGES_REQUESTED, PENDING | 독립 검토자·review ID·대상 HEAD |
| MERGE / PUBLICATION | DONE, PENDING | 실제 merge SHA / Tag·Release·Asset 검증 |

STATIC/MOCK PASS로 CI/RUNTIME/REVIEW를 채우지 않는다. 기존 Done 티켓은
수집 부족을 이유로 자동 재개하지 않는다. PR #68의 내용 반영과 PR 병합 상태,
티켓 속성 동기화는 별개이며 각각 확인한다. 이번 도입은 티켓 64건의 속성을 변경하지 않는다.

## 차단과 재인계

검증기는 발행 Tag·Release Asset 메타데이터·보호 파일 Git blob과 Task에서 지정한
저장소 base HEAD, Issue/댓글/PR/Review의 의미 있는 필드를 관측한다. 종료 전에
같은 값인지 확인한다. live mode는 두 차례 읽기 결과가 다를 때에도 중단한다.
새 canonical Release, tag 이동, asset 교체, base 변경, 댓글/검토 변화, 인증 실패,
누락된 항목, 8시간을 넘긴 receipt는 재검토 후 새 receipt가 필요하다.

Task 밖의 새로운 관련 Issue/PR, 외부 Notion 수정, 서버 Runtime 변화는 자동으로
모두 탐지하지 않는다. 작업 시작 시 열린 PR을 검토하고 관련 참조를 Task에 포함한다.
watch 항목을 바꾸면 Task Hash도 바뀌므로 양쪽에 다시 전달한다. 실제 동시 편집을
잠그는 기능은 없으며 관측 이후 변경 가능성은 정확한 HEAD 최종 확인으로 다룬다.

`capture --api-export`는 인증된 Connector 조회 응답을 오프라인 검증하는 경로다.
SNAPSHOT_ONLY receipt를 생성하며 `check`의 실행 전 Gate를 통과할 수 없다.
임의 JSON/로컬 fixture/Hash 일치만으로 GitHub 인증·승인 진위를 주장하지 않는다.

## 패키지

기존 정본 ZIP은 `python scripts/build-canonical-package.py v3.1.18 /tmp/canonical-kit`로 만든다.
이 공통 인계 Kit는 `python scripts/build-handoff-kit.py --out /tmp/handoff.zip`으로
별도 생성한다. 파일 목록/Hash가 고정된 `handoff/KIT_SHA256SUMS`만 포함한다.
같은 입력은 같은 ZIP Hash가 되어야 한다. 실제 로그·자격증명·다운로드 API 원문·
개인 자료를 Kit에 포함하지 않는다. checksum은 작성자 신원이나 Runtime 승인이 아니다.
