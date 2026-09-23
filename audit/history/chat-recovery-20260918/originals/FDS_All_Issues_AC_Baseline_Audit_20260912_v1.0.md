# FDS 전체 이슈 AC 정본 정합성 전수 점검 v1.0

검토 기준 시각: 2026-09-12T08:55:45.252Z (UTC)

## 1. 결론

**기존 64개 이슈의 현행 AC 문구와 체크 상태는 발행 v3.1.18과 모두 일치한다. 다만 전체 66개 이슈를 “모두 v18 승인 AC”라고 부를 수는 없다. 신규 모니터링 CR 2건은 별도 승인 대기이며, Harbor 후속 리뷰에서는 필수 목표와 증적 형식·권고를 분리해야 한다.**

| 점검 항목 | 확인 결과 |
|---|---|
| 전체 범위 | `321Team/fds-project-baseline`의 Open·Closed 이슈 66건 |
| PR 제외 | issues API 75개 항목 중 Pull Request 9건 제외 |
| v18 기존 이슈 | #4~#67, 64건 |
| 현행 AC 비교 | 64/64 EXACT, 누락·변경·체크 상태 변경 0건 |
| v18 이후 신규 CR | #74·#75, 2건. PENDING_REVIEW / Runtime NOT VERIFIED |
| 현재 정식 발행 | docs-v3.1.18 |
| v19 | PR #73 Open/Draft, 미발행. 현행 정본을 대체하지 않음 |
| 이번 점검의 원격 변경 | 없음. 댓글·본문·AC·상태·PR을 수정하지 않음 |

이는 **요구사항 정합성 판정**이다. 구현 코드나 실제 환경이 모든 AC를 통과했다는 판정은 아니다.

## 2. 기준과 점검 방법

1. [정식 v18 릴리즈](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)와 태그 대상 `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`를 확인했다.
2. 전체 이슈를 state=all, per_page=100으로 수집했다. 75개 항목이 반환되어 단일 페이지 범위 내 전수 확인이며 PR 9건을 제외했다.
3. [정본 레코드](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/canonical-records.json)의 64개 Record ID와 이슈 번호를 매핑했다.
4. 각 이슈의 현행 Acceptance Criteria/AC 절을 같은 버전의 개별 Description과 비교했다. 공백 정규화 전의 추출 문자열이 모두 일치했고, 체크 표시도 그대로 비교했다.
5. `갱신 전 원문 보관`의 `<details>` 내부는 당시 이력으로 분리했다. 그 안의 오래된 AC·미발행 표현을 현행 AC로 중복 집계하지 않았다. 문서의 복수 AC 절은 포함하되 중첩 구간은 중복 집계하지 않았다.
6. 정본 Description 64개와 Baseline 원본의 Git blob 해시를 조회한 main tree와 대조했다. 태그→main 비교에서 변경은 PR #72의 후속 audit 파일에 한정되어 발행본 문서와 일치함을 확인했다.
7. 신규 CR 본문의 Scope·Exit Criteria·작업 목록, AC 관련 후속 리뷰 댓글과 [v19 PR #73](https://github.com/321Team/fds-project-baseline/pull/73)의 수집/승인 경계를 별도 검토했다. 관련 이슈·PR 댓글 41개를 수집했으며, 코드 블록 자체의 실행 검증은 하지 않았다.
8. 종료 전 전체 이슈를 재조회했다. 점검 중 변경된 #16은 최신 본문으로 다시 비교했으며 CICD-AC-01~10은 일치했다.

조회 main: `58f72f78faa237cbdc9ceae6460d25407550c1a7`. v19 Draft HEAD: `89a3dbc86ac3034f2e1c720f9828523980cc24ee`.

## 3. 범위·해석 정리가 필요한 항목

### AC-AUD-01 — HBR-06: 기존 통제 목표와 증적 형식의 구분

대상: [#13 후속 리뷰](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5633336598), [9/12 대체안](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5644173115).

**사실:** v18 [P1-HBR-01 Description](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-HBR-01.md)에는 `Image Digest·Scan 결과·Credential fingerprint Evidence 확보`, 비밀정보 비노출, AC-05의 4/4 Digest 추적, 회전·Fingerprint·Secret Scan·SHA-256 후속 증적이 포함돼 있다. [P1-CICD-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-CICD-01.md)의 CICD-AC-06은 Commit→Run/Attempt→Image→Digest→Deployment/실제 Pod의 역추적을 요구한다. 따라서 “이 요구들이 전부 정본 밖의 신규 요구”라는 해석은 맞지 않는다.

**구분:** 별도 인계표 파일, 모든 항목을 하나의 신규 체계로 묶는 방식, 지속 스캐닝 시스템은 위 통제 목표와 동일하지 않다. 고정 양식이나 새 자동화 체계를 추가 AC로 삼을 근거는 확인되지 않았다. 기존 리뷰도 동일 목적 파일의 재사용과 CI 증적 생산의 중복 배정 금지를 명시한다.

| 쟁점 | 검토 판단 / 권장 처리 |
|---|---|
| 별도 provenance/인계표 | 필수 형식으로 강제하지 않는다. 기존 README·CI Run 링크·Manifest·Pod 결과가 서로 추적 가능하면 한 곳에서 참조하는 방식으로 간소화 가능 |
| 4/4 Digest이면 Commit/승인 추적 생략 | 불가. 같은 이미지 바이트의 일치와 어떤 Source/CI 실행·승인으로 배포됐는지는 별도 사실이다. #16의 기존 추적 AC를 삭제하지 않는다 |
| CI 증적 생산 담당 | #16/P1-CICD-01에서 생산하고 #13은 연결·인수한다. Harbor 담당자에게 같은 CI 체계의 재구축을 요구하지 않는다 |
| Secret Scan | 지속 서비스 신규 구축을 강제하지 않는다. 제출 직전 1회성 점검도 제출물·로그의 범위와 결과가 확인되면 검토 가능. 현재 미실행을 PASS로 바꾸지는 않는다 |
| Credential fingerprint·회전/폐기 | 기존 식별·수명주기 근거는 유지한다. 새 플랫폼을 만들 필요는 없으나 생성일·회전 여부 한 줄만으로 기존 식별 요구가 충족되는지는 내용 대조가 필요 |
| SHA-256 | 기존 `99_SHA256SUMS.txt` 재사용 가능. 새 체크섬 체계를 별도로 만들 필요 없음 |
| 도구/DB 버전 등 상세 필드 | 실제 Scan 재현에 필요한 기존 출력은 링크로 재사용한다. 모든 실행·티켓에 같은 고정 필드를 무조건 추가하는 독립 완료 조건으로 확대하지 않는다 |

위 간소화는 **권장 판단**이며 대체안 전체 승인 또는 HBR Runtime PASS가 아니다. HBR-01~05는 [infra-harbor-trivy PR #2](https://github.com/321Team/infra-harbor-trivy/pull/2)에 수정 제출됐고 HBR-06은 별도 협의로 남아 있다. 조회 HEAD `7539e65c9d1ab21528391b44b44c836198b08b8e`, Open/미병합, 공식 PR 리뷰 0건이었다. 이번 점검은 그 수정 코드의 재리뷰가 아니다.

### AC-AUD-02 — Robot Token Never: 승인 사실관계 확인 필요

**사실:** v18 Baseline §16의 P1-HBR-01 기록과 현행 본문은 Robot Token Never를 승인 대기 제안으로 구분한다. 반면 [9/12 댓글](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5644173115)의 대체안에는 `Never, 승인된 예외`로 적혀 있다.

**판정:** 조회한 정본·관련 댓글·PR 리뷰에서 이 표현을 뒷받침할 별도 예외 승인 근거를 확인하지 못했다. 실제 승인이 전혀 없다고 단정하는 것이 아니라, 현재 근거 연결이 부족하다는 지적이다.

**권장:** 승인자·대상 Robot·예외 범위·승인 기록을 연결하거나 `승인 대기`로 표현을 정리한다. 이번 감사로 Never를 승인하거나 이를 필수 AC로 추가하지 않는다.

### AC-AUD-03 — #74·#75: 정본 밖 변경안이지만 현재 AC의 무단 변경은 아님

[CR-P1-MON-01-01 #74](https://github.com/321Team/fds-project-baseline/issues/74)는 Discord egress 프록시, [CR-P1-MON-01-02 #75](https://github.com/321Team/fds-project-baseline/issues/75)는 Kubernetes NetworkPolicy·selector·Secret·알림 경로를 다룬다. v18의 64개 레코드에는 포함되지 않는다.

- 두 본문은 PENDING_REVIEW, Runtime NOT VERIFIED와 기존 P0/G2 AC 미변경을 명시한다. G2 Milestone은 추적용이지 새 필수 통과조건이 아니다.
- 독립 Acceptance Criteria 절은 없으나 Exit Criteria와 Scope·작업 목록은 있다. 이를 “완료 조건이 전혀 없다”고 판정하지 않는다.
- 승인 전 프록시 endpoint·실제 selector·Secret 수명주기·발송 데이터·허용/차단/실패/복구의 기대값과 근거를 확인 가능한 CR AC로 정리하는 것을 권장한다.
- 기존 6대 중 한 VM을 프록시 전용으로 전환하는 표현은 3CP+3Worker 요구와 충돌할 수 있다. 본문 상단에서 이미 미승인으로 제한했으므로 확정 배치로 해석하지 않는다.
- RETIRED IF-24는 Alertmanager→monitor01 Webhook이다. 새 Discord 프록시 경로와 같지 않으며 IF-06B Remote Write의 대체도 아니다. 새 변경안은 별도 계약·승인을 거쳐 차기 정본에 편입한다.

### AC-AUD-04 — #16: 운영 진행 기록 추가와 AC 변경의 구분

점검 중 [P1-CICD-01 #16](https://github.com/321Team/fds-project-baseline/issues/16)이 갱신됐다. CA 보호 환경·신규 Root 계획·별도 백업 매체 준비 지연·OS 디스크 40GB 실측 등의 운영 기록이 추가됐지만 기존 CICD-AC-01~10의 문구·체크 상태는 유지됐다.

이 기록은 발행 후 운영 입력이며 본문도 정본 사양 변경·발행 완료가 아니라고 구분한다. CA 자원·프로파일·백업 순서 변경의 근거와 영향은 차기 정본 수집 대상으로 관리하되 새 CA 매개변수를 기존 모든 티켓의 추가 AC로 전파하지 않는다. 별도 백업 요구를 삭제하거나 미검증 단계를 완료로 보지 않는다.

## 4. 불필요한 범위 확대를 막기 위한 판정 원칙

- HBR-01~06·SEC-01~08·K8S-F01~06은 리뷰 지적/후속 추적 ID다. 기존 AC 개수를 자동 증가시키는 새 제품 사양 ID가 아니다.
- Secret 비노출, 올바른 TLS/권한 시험 판정, RETIRED 경로 제거, 실제 NIC·보호 전환·복구, 암호화·RBAC 검증은 기존 v18 요구를 충족시키기 위한 보완이다. 일정이 촉박하다는 이유만으로 삭제하지 않는다.
- 반대로 특정 도구·새 시스템·별도 문서 양식 자체를 완료 조건으로 추가할 때는 정본 근거와 실제 필요를 설명해야 한다. 동일한 증명력을 가진 기존 산출물 재사용을 허용한다.
- 과거 #4~#6 댓글의 보류/관리 UI·세션 15/60분 등 제안은 현재 종결 Decision의 현행 유지·유예 판정을 대체하지 않는다.
- NTP `100ms·60초×6`, MTU 1450, Robot Never, 미확정 Scan Threshold를 승인된 고정값으로 쓰지 않는다. 필요한 실행/인수 단계의 입력 확정과 모든 준비 업무를 중단시키는 전역 조건은 구분한다.
- #25~#27 등의 P1 Known Issue/Close 추적과 P0 Gate를 분리한다. 일정·Milestone 변경은 AC 상향이나 Runtime 완료가 아니다.

## 5. 66개 이슈 전수표

EXACT는 현행 AC 절의 문구·체크 상태가 발행 Description과 일치한다는 뜻이다. Runtime PASS를 의미하지 않는다. Record ID 링크는 비교한 고정 커밋의 원문이다.

| 이슈 | Record ID / 정본 원문 | GitHub 상태 | AC 대조 | 비고 |
|---|---|---|---|---|
| [#4](https://github.com/321Team/fds-project-baseline/issues/4) | [DEC-P1-FDS-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-P1-FDS-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#5](https://github.com/321Team/fds-project-baseline/issues/5) | [DEC-P1-TXN-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-P1-TXN-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#6](https://github.com/321Team/fds-project-baseline/issues/6) | [DEC-P1-ADMIN-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-P1-ADMIN-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#7](https://github.com/321Team/fds-project-baseline/issues/7) | [D-SEC-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/D-SEC-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#8](https://github.com/321Team/fds-project-baseline/issues/8) | [MS-G0-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-G0-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#9](https://github.com/321Team/fds-project-baseline/issues/9) | [P1-LB-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-LB-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#10](https://github.com/321Team/fds-project-baseline/issues/10) | [P1-K8S-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-K8S-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#11](https://github.com/321Team/fds-project-baseline/issues/11) | [P1-DB-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-DB-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#12](https://github.com/321Team/fds-project-baseline/issues/12) | [P1-DNS-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-DNS-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#13](https://github.com/321Team/fds-project-baseline/issues/13) | [P1-HBR-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-HBR-01.md) | open | EXACT | 본문 AC 일치. HBR-06 증적 형식·Never 승인 주장 별도 검토 |
| [#14](https://github.com/321Team/fds-project-baseline/issues/14) | [ICR-D-NET-01-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/ICR-D-NET-01-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#15](https://github.com/321Team/fds-project-baseline/issues/15) | [P1-APP-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-APP-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#16](https://github.com/321Team/fds-project-baseline/issues/16) | [P1-CICD-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-CICD-01.md) | open | EXACT | 진행 중 갱신 재대조; CICD-AC-01~10 보존 |
| [#17](https://github.com/321Team/fds-project-baseline/issues/17) | [P1-MON-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-MON-01.md) | open | EXACT | 14개 Runtime AC와 필수 보조통제 2개 구분 유지 |
| [#18](https://github.com/321Team/fds-project-baseline/issues/18) | [MS-G1-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-G1-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#19](https://github.com/321Team/fds-project-baseline/issues/19) | [P1-SEC-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-SEC-01.md) | open | EXACT | 본문 AC 일치; SEC-01~08은 검토 지적 ID |
| [#20](https://github.com/321Team/fds-project-baseline/issues/20) | [P1-E2E-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-E2E-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#21](https://github.com/321Team/fds-project-baseline/issues/21) | [P1-DR-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-DR-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#22](https://github.com/321Team/fds-project-baseline/issues/22) | [P1-HA-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-HA-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#23](https://github.com/321Team/fds-project-baseline/issues/23) | [MS-G2-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-G2-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#24](https://github.com/321Team/fds-project-baseline/issues/24) | [P1-DOC-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-DOC-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#25](https://github.com/321Team/fds-project-baseline/issues/25) | [P1-MON-02](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-MON-02.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#26](https://github.com/321Team/fds-project-baseline/issues/26) | [P1-DR-02](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-DR-02.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#27](https://github.com/321Team/fds-project-baseline/issues/27) | [P1-HA-02](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-HA-02.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#28](https://github.com/321Team/fds-project-baseline/issues/28) | [DEC-CAL-P1-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-CAL-P1-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#29](https://github.com/321Team/fds-project-baseline/issues/29) | [MS-G3-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-G3-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#30](https://github.com/321Team/fds-project-baseline/issues/30) | [P1-REV-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-REV-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#31](https://github.com/321Team/fds-project-baseline/issues/31) | [MS-P1-REVIEW-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-P1-REVIEW-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#32](https://github.com/321Team/fds-project-baseline/issues/32) | [MS-P1-CLOSE-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-P1-CLOSE-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#33](https://github.com/321Team/fds-project-baseline/issues/33) | [MS-P2-START-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-P2-START-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#34](https://github.com/321Team/fds-project-baseline/issues/34) | [P2-ARC-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-ARC-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#35](https://github.com/321Team/fds-project-baseline/issues/35) | [P2-IAC-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-IAC-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#36](https://github.com/321Team/fds-project-baseline/issues/36) | [P2-OCI-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-OCI-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#37](https://github.com/321Team/fds-project-baseline/issues/37) | [P2-VPN-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-VPN-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#38](https://github.com/321Team/fds-project-baseline/issues/38) | [P2-ROSA-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-ROSA-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#39](https://github.com/321Team/fds-project-baseline/issues/39) | [MS-G4-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-G4-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#40](https://github.com/321Team/fds-project-baseline/issues/40) | [DEC-P2-DNS-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-P2-DNS-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#41](https://github.com/321Team/fds-project-baseline/issues/41) | [DEC-P2-OP-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-P2-OP-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#42](https://github.com/321Team/fds-project-baseline/issues/42) | [DEC-P2-REG-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-P2-REG-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#43](https://github.com/321Team/fds-project-baseline/issues/43) | [P2-APP-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-APP-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#44](https://github.com/321Team/fds-project-baseline/issues/44) | [P2-OADP-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-OADP-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#45](https://github.com/321Team/fds-project-baseline/issues/45) | [MS-G5-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-G5-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#46](https://github.com/321Team/fds-project-baseline/issues/46) | [P2-CICD-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-CICD-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#47](https://github.com/321Team/fds-project-baseline/issues/47) | [P2-HYB-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-HYB-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#48](https://github.com/321Team/fds-project-baseline/issues/48) | [P2-DNS-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-DNS-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#49](https://github.com/321Team/fds-project-baseline/issues/49) | [P2-DOC-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-DOC-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#50](https://github.com/321Team/fds-project-baseline/issues/50) | [P2-E2E-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-E2E-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#51](https://github.com/321Team/fds-project-baseline/issues/51) | [P2-OP-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-OP-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#52](https://github.com/321Team/fds-project-baseline/issues/52) | [DEC-CAL-P2-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-CAL-P2-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#53](https://github.com/321Team/fds-project-baseline/issues/53) | [MS-G6-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-G6-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#54](https://github.com/321Team/fds-project-baseline/issues/54) | [MS-DELIVERABLE-FREEZE-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-DELIVERABLE-FREEZE-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#55](https://github.com/321Team/fds-project-baseline/issues/55) | [P2-REV-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P2-REV-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#56](https://github.com/321Team/fds-project-baseline/issues/56) | [MS-P2-REVIEW-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-P2-REVIEW-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#57](https://github.com/321Team/fds-project-baseline/issues/57) | [MS-PROJECT-CLOSE-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/MS-PROJECT-CLOSE-01.md) | open | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#58](https://github.com/321Team/fds-project-baseline/issues/58) | [CR-P1-ANS-01-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/CR-P1-ANS-01-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#59](https://github.com/321Team/fds-project-baseline/issues/59) | [D-ARC-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/D-ARC-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#60](https://github.com/321Team/fds-project-baseline/issues/60) | [D-NET-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/D-NET-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#61](https://github.com/321Team/fds-project-baseline/issues/61) | [D-WBS-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/D-WBS-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#62](https://github.com/321Team/fds-project-baseline/issues/62) | [DEC-P1-ENTRY-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-P1-ENTRY-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#63](https://github.com/321Team/fds-project-baseline/issues/63) | [DEC-P1-MON-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-P1-MON-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#64](https://github.com/321Team/fds-project-baseline/issues/64) | [DEC-P1-TLS-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/DEC-P1-TLS-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#65](https://github.com/321Team/fds-project-baseline/issues/65) | [P1-ANS-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-ANS-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#66](https://github.com/321Team/fds-project-baseline/issues/66) | [P1-LNX-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-LNX-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#67](https://github.com/321Team/fds-project-baseline/issues/67) | [P1-NET-01](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/descriptions/P1-NET-01.md) | closed | EXACT | 현행 AC 문구·체크 상태 일치 |
| [#74](https://github.com/321Team/fds-project-baseline/issues/74) | CR-P1-MON-01-01 | open | 별도 CR / 승인 대기 | v18 미포함 CR; PENDING_REVIEW, 기존 G2 AC 추가 아님 |
| [#75](https://github.com/321Team/fds-project-baseline/issues/75) | CR-P1-MON-01-02 | open | 별도 CR / 승인 대기 | v18 미포함 CR; PENDING_REVIEW, #74 인계 선행 |

## 6. 후속 권장안 및 제한

1. 기존 64개 AC는 유지한다. 정본 일치만으로 완료 체크를 상향하지 않는다.
2. #13의 HBR-06 답변은 “필수 통제 목표 유지 + 증적 형식 간소화 가능 + Never 승인 근거 확인”으로 분리한다.
3. #74/#75와 #16 운영 델타는 v19 수집 입력으로 유지하고 승인·Runtime 상태를 분리한다.
4. 이번 요청은 점검이므로 이슈 댓글·본문 수정, PR 승인·병합, v19 편입 작업은 실행하지 않았다.

본 전수 범위는 `fds-project-baseline`의 66개 이슈다. 조직 내 다른 모든 저장소의 전체 이슈 전수 점검이나 Notion 실시간 원문 대조를 뜻하지 않는다. 관련 외부 PR은 AC 범위·승인 주장 확인에 필요한 메타데이터만 확인했으며 코드 결함 해소 여부와 실제 운영 증적 재검증은 별도다.
