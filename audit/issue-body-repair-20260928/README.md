# Issue 본문 손상·정합성 복구 준비 — #19 · #110 (2026-09-28)

지시: 2026-09-28 사용자(이권욱) — #19 본문 손상 및 #110 승인 전/후 불일치 확인 후 복구 착수.

이 PR/패킷은 **Issue 본문을 직접 쓰지 않는다**. [AGENTS.md](../../AGENTS.md) 및 [TICKET_SYNC_POLICY §5.1](../../governance/TICKET_SYNC_POLICY.md)에 따라 교체 본문·고정 plan·Lead 로컬 적용 스크립트만 준비한다.

## 1. 판정

### #19 P1-SEC-01
- 현재 Issue body에서 AGENTS.md 문제 사례 [B]와 같은 링크 손상 **3건**을 확인했다.
- 손상 대상:
  1. Gate2 실행 문서
  2. 점검 요약
  3. 선행 변경 기록 ICR-D-NET-01-01-ADV-20260910
- 2026-09-25 보존본 `audit/phase2-repo-bootstrap-20260923/evidence-path-followup-20260925/bodies/issue-19.md` 및 v3.1.19 설명에서는 세 링크가 정상이다.
- 교체 본문은 현재 본문의 정당한 최신 변경을 그대로 보존하고, 위 3개 Markdown 링크의 백틱 손상만 제거한다.
- Status/AC/요구사항/승인 의미 변경 없음.

### #110 DEC-P1-IMG-01
기계적 링크 손상은 없지만 승인 전 후보 설명과 최종 승인 계약이 같은 현재 본문 안에서 충돌한다.

확정 근거:
- Review Owner DEC-01~04 승인: issue comment `5852885654`
- Lead 추가조건 확인: issue comment `5855626610`
- Lead 승인 확정: issue comment `5856632297`
- `fds-msa#9`: HEAD `0bea0d4fa8ece5ecbf7aa5fd8f054fc24f5556cf`, merge `1c7f3651504097096c3a3fe4a86ac1973e169688`
- PR #9 변경에서 운영 계약 `USER 10001:999` 및 Runtime UID/GID 검증을 확인했다.

교체 원칙:
- candidate HEAD `88b494c...`의 UID `65532`는 **Historical candidate input**으로 보존한다.
- 현재 승인 운영 계약은 **10001:999**로 명확히 한다.
- 승인 전 "결정 필요/PR #9 미통합" 문구를 현재 승인·병합 상태와 정합화한다.
- Decision 완료를 on-prem Test→Build→Scan, Harbor Push, Kubernetes Deploy/Runtime PASS로 확대하지 않는다.

## 2. 적용 계획

`plan.json`에 각 Issue의 다음 값을 고정했다.
- issue number / Record ID
- 최신 `updated_at`
- 변경 전 body SHA-256 (LF)
- replacement file SHA-256
- title/state/labels
- 손상 신호 before/after

교체 파일:
- `bodies/issue-19.md`
- `bodies/issue-110.md`

## 3. Lead 로컬 적용

Windows PowerShell 5.1 + 로그인된 `gh` 기준:

```powershell
powershell -ExecutionPolicy Bypass -File .\apply-issue-body-repair.ps1
powershell -ExecutionPolicy Bypass -File .\apply-issue-body-repair.ps1 -Apply
```

Dry-run에서 다음이면 STOP:
- replacement SHA 불일치
- Issue `updated_at`이 plan과 다름
- `gh` 조회 실패

적용은 **담당자가 로컬 gh로 직접 수행**한다. AI/connector는 Issue body PATCH를 하지 않는다.

## 4. 적용 후 필수 재검증

1. Issue body SHA-256 = plan의 replacement SHA
2. #19: malformed link / 단독 ``` / `&lt;`·`&gt;` / footer 증가 없음
3. #110: UID/GID 현재 계약은 10001:999, 65532는 Historical candidate로만 남음
4. title/state/labels 불변
5. 다른 Issue 무변경
6. 결과를 `result.json` 또는 후속 감사 기록으로 남김

## 5. 현재 단계

- STATIC: 교체본문 생성 및 plan 고정
- ISSUE BODY APPLY: **NOT RUN — Lead 로컬 적용 대기**
- REVIEW: PR 독립 리뷰 요청
- PUBLICATION: 해당 없음
