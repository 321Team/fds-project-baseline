# Issue 본문 손상 복구 지침 — #9 · #74 · #75 (fds-project-baseline)

작성: 2026-09-25 KST, infra-dns 리뷰 세션(session_01SFzFYjUSi1GuzmLpUSqLtS)
대상: 정본 세션(fds-project-baseline 담당). 적용과 병합 판단은 이권욱(Lead)이 한다.
관련: [baseline PR #105](https://github.com/321Team/fds-project-baseline/pull/105), 9/23 기록 [`audit/phase2-repo-bootstrap-20260923/README.md`](https://github.com/321Team/fds-project-baseline/blob/main/audit/phase2-repo-bootstrap-20260923/README.md) §3

아래에서 **[확인]**은 이 세션이 GitHub에서 직접 조회한 사실, **[추정]**은 근거는 있지만 확정하지 않은 판단, **[요청]**은 정본 세션이 할 작업이다.

---

## 1. 무엇이 손상됐나 [확인]

2026-09-25에 Issue 68건 전체 본문을 대조했다. 아래 두 손상이 **#9·#74·#75 세 건에만** 함께 있다.

| 손상 유형 | 증상 | 영향 |
|---|---|---|
| A. HTML 엔티티화 | `<`가 `&lt;`로, `>`가 `&gt;`로 바뀜. `<!-- 마커 -->`, `<details>`, `</details>` 등이 대상 | 관리 마커가 화면에 문자열로 노출되고, 보관 원문 접기(`<details>`)가 풀리며, 보관 원문 SHA-256 대조가 깨진다 |
| B. 링크 표기 삽입 | 링크 앞뒤에 ``` `` ```가 삽입됨. 위치가 불규칙함(`](``https…)에서```, `…md``)`, ``` ``[텍스트](…)`` ```) | 링크가 코드 표기로 깨진다. 9/23 #11·#16 손상과 같은 유형이다 |

| Issue | 제목 | 마지막 수정(UTC) | `&lt;`/`&gt;` | ``` `` ``` 표기 | 보관 원문 해시 |
|---|---|---|---|---|---|
| #9 | [P1-LB-01] Kubernetes API Load Balancer | 2026-09-24T18:02:47Z | 51 / 55 | 32 (링크 15개) | **불일치** |
| #74 | [CR-P1-MON-01-01] Alertmanager Egress 프록시 서버 구성 | 2026-09-23T11:14:20Z | 12 / 12 | 4 (링크 2개) | 보관 원문 없음 |
| #75 | [CR-P1-MON-01-02] Alertmanager Egress Kubernetes 보안 설정 | 2026-09-24T17:54:53Z | 12 / 12 | 4 (링크 2개) | 보관 원문 없음 |

- 관찰 본문 SHA-256(LF 기준):
  - #9 `c8b3a9e8460e231bdf47e5b58172c812387d93fea2f173b1369e11d2fd0e54c4`
  - #74 `de777be149529e2ae790634d20607fbf462b4dba55fc0b6593b9014f1525945d`
  - #75 `956174a2f97a360b2b4bb878815192477d8c945d9ceb97c7df05331bdccc7cc1`
- 다른 65건에는 이 손상이 없다. #7·#35의 footer와 #19의 기존 보관 원문 해시 불일치는 별개 사항이다(PR #105 기록).

## 2. 원인 [추정]

- 9/23 기록 §3에서 세션 GitHub 쓰기 경로(에이전트 프록시)가 본문을 바꾼 사례가 있었다. footer 추가와 링크 ``` `` ``` 삽입이다. 이번 B 유형이 그것과 같다.
- #9와 #75는 2026-09-25 02:54~03:02 KST에 수정됐다. **9/23 이후에도 세션 경로로 Issue 본문을 쓴 작업이 있었을 가능성이 높다.** 어느 세션이 수정했는지는 이 세션에서 확인하지 않았다.
- A 유형(`&lt;`)은 9/23 기록에 없는 새 유형이다. 같은 경로에서 생겼는지는 미확인이다.

## 3. 먼저 할 일 — 추가 손상 방지 [요청]

1. **세션(GitHub MCP·프록시) 경로로 Issue 본문을 쓰는 작업을 모두 멈춘다.** 진행 중인 세션이 있으면 본문 수정을 중단시킨다. 코멘트는 이번 조사에서 손상이 관찰되지 않았다(#12 코멘트 확인).
2. 각 Issue의 편집 이력으로 손상을 만든 편집(시각·편집자)을 특정한다(§4-1).
3. 본문 교체는 9/23과 같이 **Lead 로컬 `gh`**로만 한다. [TICKET_SYNC_POLICY §5](https://github.com/321Team/fds-project-baseline/blob/main/governance/TICKET_SYNC_POLICY.md)는 자동 동기화에서 본문 쓰기를 금지한다.

## 4. 복구 절차 [요청]

### 4-1. 손상 전 원문 확보 (필수)

Lead PC에서 편집 이력을 조회한다. 조회만 하며 쓰기는 없다.

```powershell
gh api graphql -f query='query($o:String!,$r:String!,$n:Int!){repository(owner:$o,name:$r){issue(number:$n){lastEditedAt userContentEdits(first:30){nodes{createdAt editedAt editor{login} diff}}}}}' -F o=321Team -F r=fds-project-baseline -F n=9 > edits-9.json
```

- #74와 #75도 같은 방법으로 조회한다.
- 각 편집의 `editedAt`, `editor`, `diff`로 **처음 `&lt;` 또는 ``` ``https ```가 나타난 편집**과 그 직전 버전을 찾는다.
- `diff` 필드가 전체 본문인지 변경 요약인지는 **이 세션에서 확인하지 않았다**. 전체 본문이 아니면 웹 UI의 "edited ▾" 이력에서 해당 버전을 연다.
- **손상 편집이 정당한 새 내용도 함께 추가했을 수 있다.** 예를 들어 #9의 9/25 03:02 편집이나 #75의 9/25 02:54 편집이다. 이 경우 직전 버전으로 되돌리기만 하면 새 내용이 사라진다. "직전 버전 + 그 편집의 정당한 추가분(손상만 제거)"을 기준 본문으로 삼는다.

### 4-2. 복구 후보와 대조

이 키트의 `candidates/issue-<번호>.repair-candidate.md`는 관찰 본문에 아래 규칙만 적용한 **후보**다(`candidates.json`에 해시 수록).

- 규칙: `&lt;`를 `<`로, `&gt;`를 `>`로 되돌리고, 단독 ``` `` ```를 제거한다. ```` ```` ```` 코드 펜스는 유지한다.
- 후보 검증 결과 [확인]:
  - **#9 후보는 보관 원문 SHA-256이 기록값과 일치한다.** 관찰 본문은 불일치다. A 유형 복원이 보관 원문 범위에서 정확하다는 근거다.
  - 세 후보 모두 남은 ``` `` ``` 표기 0, http·앵커가 아닌 Markdown 링크 0이다.
  - #9는 줄 첫머리 `<details>` 1개가 복원된다.
- 한계 [추정]:
  - 현행 영역에서는 원래 있던 문자인지 삽입된 문자인지를 규칙만으로 판단할 수 없다. 예를 들어 원문에 문자 그대로 적힌 `&gt;`나 ``` `` ```는 규칙으로 구분되지 않는다.
  - **후보를 그대로 적용하지 말고**, 4-1의 기준 본문과 `diff`를 내어 차이가 손상 제거뿐인지 확인한다.

### 4-3. 적용 (9/23 절차 그대로)

1. 확정 본문을 `bodies/issue-<번호>.md`(UTF-8, LF)로 저장한다.
2. `plan.json`을 만든다. 9/23 형식에 따라 Issue별로 다음을 적는다.
   - `number`
   - `updated_at`: 적용 직전 재조회 값
   - `before_sha256_lf`
   - `file`
   - `file_sha256`
3. 9/23 [`apply-evidence-path.ps1`](https://github.com/321Team/fds-project-baseline/blob/main/audit/phase2-repo-bootstrap-20260923/evidence-path-batch/apply-evidence-path.ps1)을 그대로 쓴다. 점검(`DRY RUN ready=3`)을 먼저 하고 `-Apply`로 반영한다. 계획 이후 수정이 있으면 `STOP`한다.

### 4-4. 반영 후 확인 기준

- 재조회 본문(LF)이 확정 본문과 같다(SHA-256).
- `&lt;`·`&gt;` 0건, 단독 ``` `` ``` 0건, footer 없음.
- #9는 보관 원문 SHA-256이 기록값과 같다.
- 제목·상태·라벨이 바뀌지 않았다.
- 같은 시간대에 다른 Issue가 변경되지 않았다.

## 5. #9 후속 — 증적 경로 반영 [요청]

- #9 P1-LB-01은 9/23 증적 경로 일괄 반영의 누락 대상이다. 손상 때문에 PR #105 계획에서 보류됐다.
- 복구가 끝나면 PR #105의 7건과 같은 형식으로 반영한다.
  - 상단에 `fds-evidence-path:20260923:v1` 마커 절을 넣는다.
  - 현행 영역 `` `docs/evidence/P1-LB-01/` `` 1곳을 `` `321Team/fds-project-evidence:evidence/P1-LB-01/` ``로 바꾼다.
  - 보관 원문 안의 같은 경로(2번째 출현)는 **바꾸지 않는다.**
- 복구와 경로 반영은 두 번에 나눠 적용한다. 각 변경을 따로 검증할 수 있게 하기 위해서다.

## 6. 기록 [요청]

- 결과는 `audit/phase2-repo-bootstrap-20260923/` 아래 새 폴더(예: `issue-body-repair-20260925/`)에 남긴다.
  - 손상 편집 특정 결과(시각·편집자)
  - 기준 본문 출처
  - plan
  - 결과
- 상위 `SHA256SUMS`를 갱신하고, PR로 정본 Lead가 판단한다. PR #105에 이어 붙여도 된다.
- 원인 경로(세션 쓰기)가 확인되면 재발 방지 문구를 운영 기록에 추가한다. 예: "Issue 본문 교체는 로컬 `gh`만 사용한다."

## 7. 키트 구성

| 파일 | 내용 |
|---|---|
| `REPAIR_GUIDE_issue-9-74-75.md` | 이 지침 |
| `candidates.json` | 관찰 시각·관찰 본문 해시·손상 수치·후보 해시·후보 검증 결과. 상태: **CANDIDATE, 편집 이력 대조 전 적용 금지** |
| `candidates/issue-9.repair-candidate.md` | #9 후보(SHA-256 `9a8da1a0…64dd3`) |
| `candidates/issue-74.repair-candidate.md` | #74 후보(SHA-256 `3ef0a477…649b1`) |
| `candidates/issue-75.repair-candidate.md` | #75 후보(SHA-256 `ef53343b…c6087`) |

후보는 2026-09-25 관찰 본문을 기준으로 했다. 그 뒤 Issue가 수정됐으면 후보를 다시 만든다.
