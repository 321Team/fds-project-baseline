# FDS v3.1.18 — 정본 누적 이력·WBS·K8S 통합

> 게시 본문 초안. 최종화 PR 승인·병합, Tag/Assets 및 게시 후 검증은 아직 완료되지 않았다.

## 주요 변경

- v3.1.17 이후 누적된 DNS CR·Ansible 후속·종결 Decision 및 최신 K8S/ICR/SEC 이력을 문서 정본에 통합했다.
- Baseline, WBS/Gantt, Ticket Pack·64개 Description, 원문 증적, 감사, Release Notes·Manifest·WEB을 동기화했다.
- WBS는 9개 탭·55개 일정관리 항목·수식 2,209개·차트 2개다. 09-08/09-10 이하영 휴가, 주말 교육장 가용량 0과 평일 Fast Tracking 권장안을 반영했다.
- Kubernetes Worker 보완 기술 PASS, 수집기 PR #3 병합, PR #2 현장 mock 37/37·읽기 전용 inspect 115건, PR #4 로컬 mock 74건을 실제 Runtime 인수와 구분해 기록했다.
- 중복 선행 후보 baseline PR #3은 #69로 인계 후 종결했다.

## 승인과 무결성

- 내용 PR: [#69](https://github.com/321Team/fds-project-baseline/pull/69)
- 독립 Reviewer: 이하영 (`hayeounglee`), APPROVED, 2026-09-10T14:20:47Z
- 승인된 내용 HEAD: `04c1ca46dcf82f814d350b4d49539e3ba4d6a9b4`
- 내용 병합 커밋: `02be2150f7662319a3d796cdcb99f6d26aec5472`
- 최종화 승인·병합: 대기. 최종화 병합 커밋에 `docs-v3.1.18`를 고정한다.
- 로컬 내용 후보 정합성·WBS/ZIP 검증: PASS. 최종화 검증은 배포 묶음의 `audit/v3.1.18/finalization-validation.json` 참조.
- GitHub Actions: NOT RUN. CI PASS로 표시하지 않는다.
- Tag 및 배포 Asset 게시 검증: NOT RUN. 완료 전에는 게시 완료로 표시하지 않는다.

## 배포 파일

| Asset | 용도 |
|---|---|
| `FDS_v3.1.18_Canonical_Baseline_Release_Package.zip` | 정본 전체 배포 묶음 |
| `FDS_v3.1.18_Canonical_Baseline_Release_Package.zip.sha256` | ZIP 외부 SHA-256 |
| `SHA256SUMS` | 개별 파일 SHA-256 |
| `FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx` | 편집 가능한 WBS/Gantt 독립 원본 |

정본 ZIP 해시는 함께 배포하는 `.zip.sha256`을 기준으로 검증한다. XLSX는 저장소·Manifest·SHA256SUMS·ZIP·독립 Asset 5곳에서 같은 바이트여야 한다. 기존 v3.1.17 파일·Tag·Release 이력은 보존한다.

## 유지되는 잔여

NTP/egress·MTU 실측·CP2 재개 입력, 6/6 Ready·etcd·DNS/cross-node·host 보호·Storage·재부팅/복구·Runtime/Permanent 인수는 미완료다. CA/CI-CD·외부 알림은 별도 편입 입력이며 이번 K8S 파일 통합 범위에 포함되지 않았다. 문서 발행으로 운영 Gate·AC·Done을 자동 완료하지 않는다.

실제 Issue Description과 Type/Milestone/Label은 발행 후 최신 운영 이력을 대조한 별도 절차로 갱신한다.
