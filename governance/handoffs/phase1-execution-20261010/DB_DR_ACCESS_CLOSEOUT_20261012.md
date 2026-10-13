# Phase 1 DB·DR 인수안과 보관·관리 접근 잔여

작성: 2026-10-12 KST · 이권욱 · CODEX_ASSISTED. 기준 main `8e909b107512ab5c90611c998bbb925d2b303ed3`.

이 문서는 기존 정본·실행·회신을 연결한 **처분·인수 검토안과 잔여 입력표**다. 문서 작성, PR 리뷰 요청, 실제 회신, 인수·종결을 구분한다. 기존 AC·Issue 체크·Status·Lead·일정·Release를 바꾸지 않는다. Phase 2 준비나 새 Runtime 허용은 포함하지 않는다.

## 1. 현재 판정과 작업 경계

| 대상 | 확인된 것 | 이 문서의 처리 | 남은 완료조건 |
|---|---|---|---|
| DB #11 W4 | 사전에 영향이 고지된 비밀번호 교체 창. 전체 HTTP 5xx는 NOT_MEASURED | 측정 공백을 그대로 인수하는 처분안. 현재 재시험으로 과거 0건을 만들지 않음 | 아래 W4 문안의 결과 수용 기록. DB 전체 Exit는 별도 AC 근거로 판단 |
| DR #21 | 9/29 격리 복구·비교·복구본 E2E, 담당자의 AC 체크 결정, Runbook 병합, D01 수령 | 기존 근거를 최종 인수에 연결. 새 Restore를 필수 잔여로 추가하지 않음 | D01 기존 비공개 보관대장 연결과 최종 인수 기록. 미검증 보관 접근은 따로 표시 |
| C01 archive 6개 | 수령·크기·해시·보관 책임 회신 확보. NTFS에 넓은 상속 Allow | `NOT_VERIFIED` 유지, 공유 권한·실제 허용 주체만 보완 | 공유 ACL, 파일 ACL, 그룹/주체 범위, 승인된 허용 대상의 대조 |
| Grafana 관리 접근 | 과거 제한 PF·회수, 관리자 경로와 Secret 참조 위치·권한 메타데이터 | 이미 모른다고 답한 과거 이력은 재요청하지 않음. 현 관리 주체·경로·감사 범위를 완성 | 아래 G1/G2의 현재 사실과 확인 불가 범위에 따른 인수 판단 |

실무 수행·결과 수용 책임은 [#30 이관 결정][transfer]을 따른다. 원 생산자의 사실 확인과 독립 증적 리뷰는 보존하되 별도의 Lead 구현 GO나 모든 항목의 일괄 회신을 공통 시작 gate로 추가하지 않는다. 문서 검토를 단계마다 별도 승인으로 나누지 않는다.

Harbor PR55의 수정·검증은 기존 구축 세션에서 수행한다. 이 문서 작업은 서버 변경 없이 병행하며 Harbor 코드를 수정하거나 작업창을 소비하지 않는다. MON [증적207][mon207]은 런타임 종료 뒤 편입 리뷰 단계이고, 남은 독립 리뷰를 Harbor 코드 작업의 시작 조건으로 삼지 않는다.

## 2. DB W4 — 그대로 사용할 처분 문안

> RUN `20261008T1930`의 W4 구간(2026-10-08 20:26:49~20:27:52 KST, 63초)은 전체 HTTP 5xx가 `NOT_MEASURED`다. 현재 확인된 원본으로 당시 전체 오류 건수나 무중단을 소급 산정할 수 없다. 이 한계를 보존하고 해당 구간을 5xx 0건·무중단·가용성 성공의 근거로 사용하지 않는다.
>
> [사전 창 승인][db-go]은 DB→Secret 갱신 사이 새 DB 연결 실패와 503/5xx 가능성을 명시했고 maxUnavailable=0을 무중단 보장으로 해석하지 않았다. 현재 [DB AC·Exit][db-ticket]는 교체 중 전체 5xx 0건을 별도 조건으로 두지 않는다. 따라서 이 측정 공백만으로 이미 검증한 Schema/Migration·저장/조회·접근차단·기본 Backup 근거를 무효화하지 않는다. 새 현재 시험으로 과거 공백을 메우지 않고 기존 관측 한계를 최종 기록에 남기는 안을 채택한다.
>
> [접근통제 위험수용 종료][db-risk-closed]는 기존 결정대로 유지한다. 그 종료는 W4 가용성 입증이나 fds-engine 직접 DB 접근 차단 판정이 아니다. DB 전체 AC·Exit 및 최종 종결은 해당 근거와 잔여를 별도로 대조한다. 새 위험수용, 영향이 없었다는 판정, 미측정 항목의 PASS 전환은 하지 않는다.

### 근거와 재작업을 생략하는 이유

- [창 결과][db-result]: W0~W6 정상 종료, W3/W4 거래 HTTP201·DB 각 1행, rollout 3/3, MON23/23. 전체 W4 5xx 미측정은 결과 보고에도 명시되어 있다.
- [J06 수신표][intake]: 이재환이 아는 추가 원본 없음. Worker 로그·Pod 잔존 한계, Prometheus 일부 표본, Edge 9파일·1,217기록을 전체 오류 분모로 사용하지 않는다. J06을 모든 생산자의 원본 유실 확인으로 확대하지 않는다.
- Edge에서 W4 일치 기록 0은 전체 요청 0·전체 5xx 0이 아니다. 알려진 양성 요청 1건을 추가로 찾더라도 그 경로·시각의 기록 가능성만 보완한다. 이번 처분에는 새 Edge 조회를 필수로 추가하지 않는다.
- `fds-engine` 직접 DB 접근과 승인 경로만 허용하는 요구는 W4 문안으로 완료 처리하지 않는다. [#11][db11]·[#19][sec19]의 기존 별도 증적을 소비한다.

## 3. DR — 기존 요구사항과 실제 증적 대응

주 근거는 [증적67 병합본][dr-evidence]과 [당시 DR 담당자 판정][dr-accept]이다. 9/15 기록의 미검증 사항을 새 미완료로 복원하지 않고, 9/29에 실제 보완된 범위만 연결한다.

| 기존 요구·AC | 직접 확인한 원본 / 후속 결정 | 적용 범위 |
|---|---|---|
| Backup 시각·Source DB 버전 | `db01/dr-rehearsal.log`: 9/29 12:15:55~57, `show server_version`·`select version()` 16.14, dump rc0 | 도구 버전을 서버 버전으로 대신한 것이 아님 |
| Backup 정상 생성·검증 | 같은 로그: 51,491 B, SHA256 `ffc96357cfa0b933892591ccf715296ced74752412cb405a8fe8325fe4139f4a`, TOC | 9/29 복구에 사용한 dump. D01과 다름 |
| 빈 격리 대상 Schema/Data 복구·순서 | `createdb rc0`, `pg_restore rc0`; 확장→테이블→데이터→PK→인덱스→ACL | 운영 원본에 직접 restore하지 않음 |
| Row/Rule 결과 일치 | revision0003·1,209행·행 전체 MD5 동일, 인덱스/소유자/대표 3건 FDS 결과 일치 | 같은 서버·동일 세션 설정의 당시 비교 |
| Restore 후 E2E | edge01 원본: HTTP201, R02 triggered; db01 복구본 oid32882에 1행 저장, 앱 세션이 복구본 사용 | R02 거래 1건. 전체 Rule Final Regression으로 확대하지 않음 |
| 원본 보존·원복·정리 | `e2e-swapback.log`·`cleanup.log`: 원본 oid16389, 1,209행·MD5 동일, 격리 DB drop rc0, readyz 3대200 | 당시 원복 완료. 새 현재 Runtime 시험 아님 |
| Credential·Backup 접근 통제 | postgres peer, 디렉터리0700, `perm-fix.log`에서 파일0644→0600, 해시 유지 | db01 당시 원본 통제. 현재 외부 보조 사본의 실효 ACL은 별도 |
| Runbook | [infra-db#11 병합][runbook-pr] `cca6055316724b0bf9fa313925c04b54612e032e`, [문서][runbook] | 10/8 이후 과거 .50 허용·옛 credential을 복원하지 않는 전제 포함 |
| D01 수령 | [10/11 수신 확인][d01-received]: 5,206 B·기존 SHA, db01 postgres·0700/0600·읽기 rc0 | 제공된 readback 대조. 이번 세션의 db01 직접 조회 아님 |

**권장 인수 범위:** 9/29 담당자가 위 복구본 E2E를 #21 AC 충족으로 체크한 [결정][dr-accept]을 유지한다. 당시 남긴 Runbook·D01 전달은 이후 근거로 연결된다. 전체 Rule 최종 회귀는 #20의 잔여이며 R02 1건으로 대신하지 않는다. 기존 결정과 모순되는 새 증거가 없는 한 #21을 위해 같은 Restore를 반복하지 않는다. 최종 인수 기록에는 이 범위와 아래 보관 한계를 함께 적는다.

### D01과 9/29 dump의 구분·보존

- D01: 9/3 `fdsdb_backup_20260903.dump`, **5,206 B**, SHA256 `80962dcd41c8afe3920c7194e8b5e2a4531ee901b4027aad1d47209ed4a46f3d`. 9/15 복구 기록과 10/11 이전의 대상이다.
- 9/29 DR dump: **51,491 B**, 위 표의 `ffc96357…` 대상. 당시 복구·E2E의 원본이다. 두 dump의 시험·이전·보존 증거를 서로 치환하지 않는다.
- [보존 결정 보완][d01-retain]과 [수용 기록][d01-review]: 이미 있던 PC-D01·SHARE-D01 두 사본만 일시 보존. 추가 복제·재공유·Git 게시·다른 dump로 확대하지 않는다.
- 10/26은 자동 삭제일이 아니다. 삭제 직전 정확한 대상/해시, 최신 회수 일정, 소비 종료, db01까지 회수할 때의 최종 원본 처분을 확인한다. 조회 실패를 부재로 처리하지 않는다.
- 두 사본의 ACL 읽기는 생산자 보고이며 이번 독립 확인은 아니다. 이미 요청한 **비공개 대장**의 존재·시각·수행자·조회 근거를 연결한다(D1). 경로·dump·내용·base64를 PR에 게시하지 않는다. C01 archive 6개의 보관 결정이 D01에 자동 적용되는 것은 아니다.

## 4. C01 — 완료로 올릴 수 없는 정확한 부분

대상은 [증적195][custody]의 기존 archive **6개**다. 수령·해시·보관 책임 수락을 다시 요청하지 않는다. 기존 [10/11 수집 기록][collected]의 `NOT_VERIFIED`를 유지한다.

2026-10-12 23:34 KST에 기존 Windows 접근 권한으로 6개 파일의 메타데이터·NTFS ACL만 다시 읽었다. 모두 크기가 기존 수신표와 같고 상속된 Everyone·BUILTIN Users `Allow FullControl`이 남아 있었다. 파일 내용을 읽거나 재해시·복사·이동·삭제하지 않았다. 이 읽기는 아직 독립 증적 PR에 편입되지 않은 로컬 진단이며 새 PASS의 근거로 쓰지 않는다.

공유 ACL 조회는 기존 인증 경로에서 성공하지 못했다. SMB 연결 조회는 접근 거부, 23:39 KST CIM 조회는 WinRM 인증/신뢰 구성 제한으로 종료됐다. 조회 실패를 ACL 없음으로 해석하지 않는다. TrustedHosts·WinRM·인증·권한을 변경하지 않았다.

따라서 **파일 ACL이 넓다는 사실은 확인됐으나, 승인 사용자만 접근 가능하다는 실효 범위는 미확인**이다. 파일 ACL만으로 외부 공개나 실제 유출을 단정하지 않는다. C1/C2를 받아 공유 계층과 파일 계층, 그룹/주체를 함께 대조한다. 허용 대상 밖 접근이 실제 확인되면 그때 최소 조정안을 준비하고 해당 변경 범위를 판단한다. 지금 ACL을 임의로 고치지 않는다.

## 5. Grafana — 이미 받은 입력과 남은 입력

기준 [관리 접근 원장][grafana]의 source `0dd0235b07d44ba7965490e3808e0a67a3bd903b`를 재조회했다. Secret 값·비밀번호·키·새 인증시험을 수집하지 않는다.

| 재사용 가능한 사실 | 남아 있는 한계 |
|---|---|
| 과거 승인 Runner .20 → 제한 SA `p1-mon-pf-verify` → localhost13000/정확 Grafana Pod3000, 회수·DENIED 증적130 | 당시 제한 경로 검증. 현존하는 모든 관리 경로의 배타성 아님 |
| control01 관리 kubeconfig 메타데이터와 ClusterRoleBinding/그룹 이름 | 파일0600이나 RBAC 이름이 실제 사람·사본 수·접근 경로·감사를 증명하지 않음 |
| `monitoring-api/grafana-admin-credentials`의 admin-user/admin-password 참조 위치(증적185) | 실제 암호 유효성·인적 보유자·회전/회수 이력 미검증 |
| J04에 과거 control01 admin.conf→Pod exec 관리자 API 사용 보고 | 생성자·과거 감사 원본 미확인 답변은 유지. 같은 과거 자료를 다시 만들라고 요구하지 않음 |

**G1/G2는 현재 운용 사실의 빈칸을 채우는 요청**이다. 이미 제출한 원장·J04/H03에 답이 있으면 그 위치만 연결하고, 확인 불가면 그 범위와 현재 책임자를 명시한다. 신규 Secret 회전·계정 삭제·RBAC 변경을 자동 채택하지 않는다. 현재 관리 접근을 제한했다고 선언하려면 그 변경 범위·소비자·복귀를 구체화해야 하며 이번 문서 작업에 포함되지 않는다.

## 6. 한 번에 회신받을 항목

이 PR의 같은 댓글에 해당 행만 회신하면 된다. 기존 답변이 있으면 링크로 대체한다. 비공개 위치·주체 상세·원본은 기존 제한 보관경로를 사용하고 PR에는 논리 ID, 시각, 확인 범위와 참조만 적는다. 담당자의 독립 리뷰를 새 서버 실행·최종 인수로 표시하지 않는다.

| ID | 회신 대상 / 정확히 필요한 내용 | 완료로 인정할 범위 |
|---|---|---|
| D1 | 이재환: 기존 PC-D01·SHARE-D01 비공개 대장에 [수용 기록][d01-review]의 시각·수행자·조회 방법/결과·접근 범위가 연결되어 있는지. 이미 있으면 참조, 없으면 미보유 범위만 | 보존 추적성. 새 dump 전달·ACL 재수집·Restore 요구 아님 |
| C1 | 실제 공유 서버 관리자(신원 미확정): C01 대상 공유의 **공유 ACL**, 확인 시각/서버/공유 식별과 조회 성공 여부. 이권욱이 기존 접근 경로로 연결 | 파일 ACL과 결합할 공유 계층 사실. 관리자 확인 없이 임의 배정하지 않음 |
| C2 | C1의 관리자와 기존 보관자: 허용 계정/그룹의 실제 범위와 승인된 접근 대상 목록의 대응. 상세는 비공개로 보관 | “승인 사용자만 접근” 주장 검증. 공유명·읽기 성공·해시만으로 대체 불가 |
| G1 | 이재환(MON)·이하영(SEC): 현재 Grafana 직접 관리자/Secret 소비, control01 관리자 인증·Pod exec/PF, 비상 콘솔 각각의 실제 책임자·사용 주체·접근 조건. 이미 답한 항목은 링크 | 인적 주체와 기술 principal의 연결. credential 값·개인키·token 불필요 |
| G2 | 같은 담당자: G1 경로의 기존 감사 근거 종류·대상 기간·확인자·참조, 기록 없음/미보유이면 그 범위. 현재 관리 자격증명의 회수/보관 책임 | 현재 감사·회수 공백 판정. 과거 미보유 로그 재생성·일률적 회전 요구 아님 |

W4 처분과 DR 대응표에 **사실 오류가 있으면 해당 행과 기존 근거를 함께 정정**해 달라고 요청한다. 사실 오류가 없다는 기술 검토를 인간의 최종 인수 선언으로 대체하지 않는다. 통합 판단은 #30의 이권욱이 맡으며 새 담당 선택 질문을 만들지 않는다.

## 7. 권장 처리 순서·완료 기록

1. 이 PR에서 W4 문안·DR 대응표를 확인하고 기존 결정/증적과 모순되는 부분만 수정한다. 수령 완료·이미 승인된 AC를 다시 시험하지 않는다.
2. D1·C1/C2·G1/G2는 위 표로 한 번에 연결한다. 이미 없다고 답한 과거 원본은 `미보유` 상태로 유지한다. 각 항목은 독립 처리하고 전부 수신할 때까지 다른 작업을 멈추지 않는다.
3. W4 처분은 #11, DR 최종 인수안·보관 경계는 #21, Grafana 실제 접근 잔여는 #17/#19, C01은 #30에 이 PR을 연결한다. Issue 본문을 다시 쓰지 않는다.
4. 확인된 범위의 결과 수용·남은 한계·담당·근거를 한 기록에 남긴다. C01/Grafana 미확인을 PASS로 승격하지 않는다. 기준을 충족하지 못하면 영향과 최소 조치만 구체화한다.

검증: 발행 티켓과 최신 이관 결정, DR 원본 로그·담당자 AC 판정, Runbook 병합, D01 수령/보존 결정, DB 창 승인/결과/위험수용 종료, 현 접근 원장을 대조했다. 신규 제품 MOCK/Runtime 시험 없음. 로컬 ACL 읽기는 위 제한 그대로이며 독립 증적 편입 완료가 아니다. 문서 PR CI는 실제 실행 결과를 PR에서 별도 확인한다.

[transfer]: https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6082618226
[intake]: ../phase1-remaining-20261009/INTAKE_STATUS.md
[collected]: COLLECTED_INPUTS_20261011.md
[db-ticket]: ../../../tickets/v3.1.21/descriptions/P1-DB-01.md
[db11]: https://github.com/321Team/fds-project-baseline/issues/11
[sec19]: https://github.com/321Team/fds-project-baseline/issues/19
[db-go]: https://github.com/321Team/fds-project-baseline/issues/11#issuecomment-6058586541
[db-result]: https://github.com/321Team/fds-project-baseline/issues/11#issuecomment-6059222263
[db-risk-closed]: https://github.com/321Team/fds-project-baseline/issues/11#issuecomment-6063472395
[dr-evidence]: https://github.com/321Team/fds-project-evidence/tree/2c8f4a36bba58ec4acbf29c95fdfd8abc1ec56bc/evidence/P1-DR-01/received-20260929T0315Z
[dr-accept]: https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5883179488
[runbook-pr]: https://github.com/321Team/infra-db/pull/11
[runbook]: https://github.com/321Team/infra-db/blob/cca6055316724b0bf9fa313925c04b54612e032e/docs/P1-DR-01_BACKUP_RESTORE_RUNBOOK.md
[d01-received]: https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-6109887386
[d01-retain]: https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-6116230888
[d01-review]: https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-6118714979
[custody]: https://github.com/321Team/fds-project-evidence/pull/195
[grafana]: https://github.com/321Team/infra-monitoring/blob/0dd0235b07d44ba7965490e3808e0a67a3bd903b/docs/GRAFANA_ACCESS_LEDGER_20261009.md
[mon207]: https://github.com/321Team/fds-project-evidence/pull/207
