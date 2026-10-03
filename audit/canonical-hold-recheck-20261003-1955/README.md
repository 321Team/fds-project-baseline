# 잔여 조건 재수집 — 2026-10-03 19:59 KST

CANDIDATE / NOT RELEASED. AI 사용: CODEX_ASSISTED.

18개 지정 Issue와 관련 5개 source PR, baseline PR112/main을 재조회했다. 전체 14개 저장소·78개 Issue·merged 257건을 다시 수집한 것은 아니다. sources.json은 Issue 본문, 선정한 최신/판정 댓글, PR HEAD·리뷰·checks 및 architecture 원문을 고정한 비원자적 스냅샷이다. 원본 Runtime 로그를 수신·재해시하거나 서버에서 실행한 작업이 아니다.

## 현재 판정과 완료조건

| 조건 | 확인한 변화 / 현재 판정 | 담당 및 다음 완료조건 |
|---|---|---|
| D21 결정 | OPEN → FINAL. OCI Primary NO-GO는 프로젝트 적합성 판단이며 AWS EC2+EIP Libreswan 단일 adapter 선택 | 이권욱 #36: 확정 입력을 #34/#35/#37 exact handoff. 결정 FINAL과 Issue Close를 분리 |
| D21 원본·발행 | HOLD_RAW_INTAKE. 최종 responder 기대값 8706 bytes / SHA256 `e5f754a3d66c6fe452605ff914a6294e87aa85bf6a345ec0fadb981f18745cb0`. `bdcd9564...` 중간값은 정본 아님 | 생산자 이권욱: final responder/initiator/Phase-A/cleanup 원본 전달 → 수신측 재해시·secret scan·manifest/registry → 독립 리뷰·별도 승인된 병합/발행. 현재 raw 재해시 NOT_VERIFIED |
| Architecture #34 | HOLD. PR8 `c421733e702c8923e26f6788fd8ade5e8657badf`에 리뷰 반영 revision2. 이전 HEAD COMMENTED와 의견은 최신 HEAD APPROVED가 아님 | 이권욱 및 독립 reviewer: supported version/type/pool, live requests/limits·N-1 capacity, management route/selector·양방향 DNS, source model/SLA, registry trust, managed recovery/관측, 비용 계약 확정과 재리뷰 |
| Stage-A #35 | NOT_READY. Terraform #3 exact HEAD APPROVED는 resource 0 scaffold/static 계약만. #2 리뷰 0, #3 checks 0 | 이하영: Freeze, exact backend/state/operator 권한·reviewed plan, subscription/link/STS-OIDC, ELB service-linked role, 이름별 quota와 비용 입력 충족. ELB 자동 생성 시도는 DENIED였으며 성공 생성이 아님 |
| W0 / PG03 | ROSA #2 draft, 리뷰 0, checks 0. admission/static/mock는 실제 Running/Ready 인수와 구분 | 이하영·이재환: 승인 image digest의 restricted-v2 arbitrary UID 실제 실행·health·filesystem·cleanup 증적. Shared OCP와 ROSA Runtime 별도 |
| P1 Close | HOLD. #29~#32 open, 10/6 Close 결과 없음. #15 local endpoint 보장 NOT_MET; #16 Harbor TLS/allowlist/audience 및 delivery 실행 미완; #19 rollback NOT_MET | 각 Lead → #30 Close Review: 실제 AC별 증적/잔여 Known Issue 처분. #19는 restart 관측, critical failure 누적, 모든 경로 cleanup, exact LB 결박 4건 수정·재검증 후 변경창 별도 판정 |
| 일정 정합 | #34 10/8 Freeze·#35 10/8 Stage-A 목표 유지. revision2의 pre-Freeze capacity checkpoint 제안 10/12 18:00은 앞선 목표와 충돌 | #34/#35/#38/#43 Leads: 입력 제출을 Freeze 이전으로 정렬하거나 정식 일정 변경. 제안은 미승인; 날짜/AC 자동 변경 없음. D21의 10/7~8 계획과 10/3 실제 결정은 별도 필드로 보존 |
| 정본 전체 재생성 | WBS STALE / FULL_RELEASE_SET NOT_GENERATED / PUBLICATION NOT_READY | baseline 담당: 최신 승인 설계·일정·CR/메타데이터·10/6 Close 결과 반영 → WBS/Baseline/Ticket Pack/Descriptions/Manifest/ZIP 생성·검증. 이번 delta는 그 입력 |

## 새로 확인한 리뷰 진척과 한계

- Terraform #3 `ebfc56e25125784187e36a0c1dd2ca0463e82acd`: hayeounglee APPROVED. plan/apply/runtime 승인 아님.
- Evidence #104 `feea4288f96d92c3e058d59d8dbf7f124c8bfdf8`: supreme33-kr APPROVED, evidence-layout check SUCCESS (run37102502442). pre-VPN/HTTPS 범위이며 최종 D21 raw·production Child SA 증명이 아님. PR은 open/draft이고 미병합.
- Architecture #8: supreme33-kr COMMENTED @9850a32, hayeounglee 의견 뒤 c421733 revision2. 최신 HEAD 재승인 PENDING, checks 0은 CI PASS가 아님.
- source model은 사전 승인된 제한 inventory reconciliation 후보로 보완됐으나 모델 선택·구현·권한·SLA는 PENDING. EgressIP/전용 subnet 대안의 지원 검증도 미완.
- 양방향 Resolver·Harbor HCP CA·AZ 고정 PVC·복합장애·ELB role·quota가 설계에 추가됐다. 문서 반영을 실제 구성·시험 PASS로 올리지 않는다.
- 비용 최신 입력은 교육장 한도 및 일일 사용 리포트. 한도·기간·서울 전체 비용·잔여 가동시간은 미확인이다. 과거 deep review의 400/450/500와 최신 권장안의 권위 차이를 정렬해야 하며 별도 교육장 승인 또는 팀 Billing 권한을 새 선행조건으로 추가하지 않는다.

## 메타데이터와 생성 규칙

#125: Calendar Days/Working Days 없음. #128: Calendar Days/Working Days/Support/Related Risk IDs/Schedule Note 없음, 본문 Todo와 GitHub closed/not_planned 차이. #130: Calendar Days/Working Days/Related Risk IDs/Schedule Note 없음. 값 추정·Issue 본문 수정 없이 후속 동기화 대상으로 유지한다.

입력 HEAD baseline `ccaa841c39b75497d17e793b79b248b41c5308e4`, main `67ba6cf8a7f187e2dfcf188e4b2c55a853993778`, compare ahead94/behind0. 기존 전체 수집 시각 11:53은 보존하고 targeted recheck 시각/범위를 별도 저장한다. candidate intake의 D21만 FINAL로 정정하면서 ISSUE36_CLOSE와 D21_EVIDENCE_PUBLICATION을 별도 HOLD로 명시한다. 두 candidate README와 schedule.json에 이 delta를 연결한다. 기존 발행 v3.1.20과 CURRENT.md는 변경하지 않는다.

직렬화 규칙: UTF-8/no BOM/LF, JSON indent2·non-ASCII 보존·마지막 LF. sources.json은 고정 입력으로부터 생성하며 선택 댓글만 보존한 범위를 명시한다. candidate.diff는 입력 HEAD 대비 unified diff이다. SHA256SUMS는 자기 자신을 제외한 이번 변경 파일 바이트를 검증한다. 해시 일치는 AC/Runtime 성공을 뜻하지 않는다.

STATIC=원문/상태·일정·해시/secret-pattern 대조; MOCK=신규 미실행; CI=source PR별 위 범위; RUNTIME=미실행; REVIEW=수집 및 기술 판정, 독립 승인 대체 아님; MERGE/PUBLICATION=미실행. D21 mismatch-PSK pathcheck 기록은 production 인증 tunnel/Child SA 성공이 아니다.

## 주요 원본

- [D21 FINAL](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-5965637169), [최종 raw/hash](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-5965598580), [raw intake HOLD](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-5966287996)
- [Architecture revision2](https://github.com/321Team/fds-project-architecture/blob/c421733e702c8923e26f6788fd8ade5e8657badf/phase2/reviews/20261003-resource-fit-recommended-design.md), [최신 handoff](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-5968501337)
- [capacity 제출 제안](https://github.com/321Team/fds-project-baseline/issues/43#issuecomment-5968501105), [계정/비용 입력](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5968500974)
- [P1 rollback 4 blockers](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5964381954), [Delivery Runtime](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-5964396337), [local endpoint 보장](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-5947435592)
