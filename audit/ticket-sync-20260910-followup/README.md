# Ticket synchronization follow-up — reviewed source drift

2026-09-10 · repository: 321Team/fds-project-baseline · Overall: PARTIAL

## 확인 결과

- 사용자 서버: `server01_ansible@ansible01`.
- 진단 수집: 2026-09-10 03:16:39–03:16:42 UTC (12:16:39–12:16:42 KST).
- 압축 파일 SHA-256 및 내부 JSON 4개 SHA-256 모두 PASS.
- 기존 계획과 비교 해시가 달라진 Issue: #10, #13, #14, #19, #65. 추가·누락 Issue 0건.
- 기존 매핑으로 독립 재분석: 64개 Issue, 52개 변경 후보, 차단 1건, 미해결 22건. 제공된 계획과 일치.
- 차단 사유: #13의 속성표 `Status`, `Schedule Note`가 기존 매핑과 불일치. 다른 네 Issue의 현재 속성표는 매핑과 일치한다.

이전 `stale plan: fingerprints` 실행은 결과 파일 생성 및 POST/PATCH 이전에 종료되었으므로 그 실행의 Issue 변경은 0건이다. 새 진단 계획의 52건은 적용 가능한 부분 집합이 아니며, 차단을 제거하기 전 전체 적용은 STOP이다.

## 검토한 #13 매핑 정정

| 필드 | 기존 매핑 | 검토 후 매핑 |
|---|---|---|
| Status | To Do | In Progress |
| Schedule Note | 이하영 08-28 휴가를 반영해 08-31 시작한다. TLS 결정 D19를 선행하고 Harbor HA/실제 Restore는 P1이다. | 이하영 08-28 휴가를 반영해 08-31 시작한다. TLS 결정 D19를 선행한다. Harbor HA는 P2, 실제 Backup/Restore는 P1-DR-02 범위다. |
| source_updated_at | 2026-09-09T12:00:20Z | 2026-09-10T03:15:50Z |

근거:

- [#13 현재 Issue](https://github.com/321Team/fds-project-baseline/issues/13): 첨부 스냅샷과 재조회한 본문·수정 시각·상태가 일치한다.
- [#13 상태 전환 기록](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5612102303): 실제 착수에 따른 In Progress 전환. Runtime Acceptance는 HOLD / NOT READY로 유지된다.
- [RELEASED v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md): §1.2에서 Harbor Backup/Restore를 P1-DR-02로 추적하고 §1.3에서 Harbor HA를 Phase 1 Scope Out으로 명시한다. 최신 Issue Schedule Note의 정정을 읽기 매핑에 반영하며 신규 HA 구현 승인으로 해석하지 않는다.

Issue 본문·라벨·상태를 수정하거나 과거 값으로 되돌린 작업이 아니다. 고정 매핑을 확인된 운영 기록에 맞춘 후보 변경이다. 스크립트의 source drift/fingerprint 검사, 정확한 계획 SHA 검증, 24시간 유효기간과 쓰기 경계는 그대로 유지한다. 나머지 63개 Record와 Milestone 목표 매핑은 변경하지 않았다.

## 검증 및 현재 범위

- 기존 단위 테스트: 18/18 PASS.
- 수정 매핑 + 첨부한 동일 Issue 스냅샷·카탈로그 재분석: 64개 Issue, 변경 후보 53건, 차단 0건, 미해결 22건.
- 변경 후보의 Issue 번호·Record ID·patch는 기존 검토 계획 53건과 정확히 일치한다. Type 28건(Decision 13 / Milestone 13 / Change Request 2), Milestone 44건, 두 필드 중복 대상 19개.
- 스냅샷 기준 이전 Task 34건 설정은 유지되고 나머지 확정 Type 28건과 Milestone 44건은 아직 미적용이다. 조직 Type 3종과 저장소 Milestone 13개는 생성 완료 증적이 있다.
- 미해결 22건: Milestone 매핑 HOLD 20건 + 원본 속성 미확인 #59/#61 2건. 전체 동기화 완료로 판정하지 않는다.
- 재분석은 업로드 스냅샷의 로컬 검증이다. 새 코드를 받은 사용자 서버에서 새 계획을 생성하고 현재 상태를 다시 검토해야 한다.
- 수정 이전 진단 계획은 STOP이고 매핑 SHA도 달라지므로 적용에 재사용하지 않는다.

## 증적 해시

```text
8b9e300b59a125d2066fc50b713568aa960d1968f5be9fc301fe75bf10315de3  FDS_Ticket_Sync_Stale_Plan_Diagnostic.tar.gz
b6a865de07d696f797de7c631d48956d95ec0e94c038d63825de28c38c95bcf2  ticket-sync-current-issues.json
fcde5e3b4faf4a8bcdf9a4ef79a57adfe5be344b0156cba72d40174c9cdd9dd2  ticket-sync-catalog.json
fcfbec2e9e9c751aa66703e1dbb5478b2b0b45e3f86e271a571d238636db1bb8  ticket-sync-native-plan.json (STOP; 적용 금지)
a6a1ec8449e0be9ee8511717d9d3eedb124a896280fdc986f7c81ddf5cb856ca  ticket-sync-plan-diff.json
```

정규화된 매핑 SHA-256:

```text
이전: 57af916fd728c654e241a6a4a0fd868317fbfc4ddeb3d6d9cb3490cb2852c22f
수정: a4132adbef075fd2706f2da22e4caa04084e1b1300b666b7b7d68099c9786d5b
```

## 체크섬과 정본 경계

이번 변경 파일 및 실행 코드 검증은 저장소 루트에서 다음 명령으로 수행한다.

```bash
sha256sum --check audit/ticket-sync-20260910-followup/SHA256SUMS
```

`audit/ticket-sync-20260910/`의 최초 감사 결과와 SHA256SUMS는 커밋 `78c1b3a71d85dad5468e30cd991e224cd2e5d1b2` 당시 기록으로 보존한다. 그 이전 체크섬의 map 항목을 수정된 매핑에 대입하여 검증하면 불일치가 나는 것이 정상이다. 최초 기록의 검증은 해당 원본 커밋에서 수행한다.

현재 변경은 PR #68 후보 브랜치에 한정된다. main, 기반 PR #3 브랜치, WBS, Release를 변경하지 않으며 merge를 수행하지 않는다. 실제 Issue 적용 결과가 제출되면 별도 후속 감사로 연결한다.
