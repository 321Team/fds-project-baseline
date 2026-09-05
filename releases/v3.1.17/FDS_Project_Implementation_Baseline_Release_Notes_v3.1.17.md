# FDS Project Implementation Baseline Release Notes v3.1.17

> Release date: 2026-09-04 candidate  
> Decision: D37  
> Status: READY FOR REVIEW  
> Previous released baseline: v3.1.16

## Release purpose

v3.1.17은 개발 구현 릴리즈가 아니라 정본 저장소 운영과 문서 무결성 보정을 위한 Release Candidate다. Private `321Team/fds-project-baseline` 저장소의 release branch와 Pull Request를 통해 검토하며, 승인 전에는 v3.1.16이 운영 정본이다.

## Changes

- v3.1.15/D35와 v3.1.16/D36 원본 이력을 버전별 디렉터리에 보존했다.
- WBS/Gantt의 담당자 영문 표기를 `GU LEE`, `GU/HY LEE`로 정정했다.
- P1-K8S Source를 Preflight v1.1로, ICR Source를 ICR v1.4/Baseline v3.1.17로 정정했다.
- P1-LB Stage B Plan End를 승인된 D36 G1 목표인 2026-09-07로 정렬했다.
- `CR-P1-ANS-01-01`을 별도 상태 레코드로 추가하고 `In Review`로 기록했다.
- 정적 WEB Snapshot, SHA-256 목록, 배포 ZIP, sidecar hash, 무결성 감사 문서를 추가했다.
- Pull Request에서 해시·금지 확장자·민감정보 패턴을 검사하는 GitHub Actions workflow를 추가했다.

## Explicit non-claims

- `CR-P1-ANS-01-01` Merge 또는 Runtime PASS를 선언하지 않는다.
- P1-LB Stage B, G1, G2 완료를 선언하지 않는다.
- OID-02/03을 임의 종결하지 않는다.
- Draft PR 승인 전 v3.1.17을 `RELEASED`로 표시하지 않는다.

## Release gates

| Gate | Required result |
|---|---|
| Local artifact integrity | PASS |
| Spreadsheet formula and render QA | PASS |
| Secret-pattern scan | PASS |
| GitHub Actions `canonical-integrity` | PASS |
| CODEOWNERS review | 1 approval minimum |
| `main` protection Ruleset | Active |
| Final merge and release tag | Pending |

**RELEASE_NOTES_VERDICT=READY_FOR_REVIEW**
