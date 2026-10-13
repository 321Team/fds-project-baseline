# Phase 1 DB·DR 인수안과 보관·관리 접근 잔여

작성: 2026-10-12 KST · 이권욱 · CODEX_ASSISTED. 기준 main `8e909b107512ab5c90611c998bbb925d2b303ed3`.

현행화: 2026-10-13 KST · 기준 main `b0a02109353616f3142ffd3b25228a8cdda04c8d`. PR164의 [MON 회신][reply-mon]·[SEC 회신][reply-sec]과 이권욱의 같은 날 C01 사용자 확인을 반영했다. 원래 작성 시점과 후속 확인을 구분한다.

이 문서는 기존 정본·실행·회신을 연결한 **처분·인수 검토안과 잔여 입력표**다. 문서 작성, PR 리뷰 요청, 실제 회신, 인수·종결을 구분한다. 기존 AC·Issue 체크·Status·Lead·일정·Release를 바꾸지 않는다. Phase 2 준비나 새 Runtime 허용은 포함하지 않는다.

## 1. 현재 판정과 작업 경계

| 대상 | 확인된 것 | 이 문서의 처리 | 남은 완료조건 |
|---|---|---|---|
| DB #11 W4 | 사전에 영향이 고지된 비밀번호 교체 창. 전체 HTTP 5xx는 NOT_MEASURED | 측정 공백을 그대로 인수하는 처분안. 현재 재시험으로 과거 0건을 만들지 않음 | 아래 W4 문안의 결과 수용 기록. DB 전체 Exit는 별도 AC 근거로 판단 |
| DR #21 | 9/29 격리 복구·비교·복구본 E2E, 담당자의 AC 체크 결정, Runbook 병합, D01 수령·비공개 대장 연결 회신 | 최종 인수 검토에 필요한 기존 근거 연결 완료. 새 Restore·대장 재요청 없음 | 아래 인수안의 결과 수용·종결 기록. D01 공유 ACL 미확인은 별도로 명시 |
| C01 archive 6개 | 수령·크기·해시·보관 책임 회신, 팀 3명 허용 기준, 이권욱의 승인 인원만 접근 가능하다는 확인 | 사용자 확인 수신 완료. 관리자·조회 경로 추가 질문 종료 | 기술적 실효 ACL 직접 대조는 `NOT_VERIFIED`로 구분. 사용자 확인을 새 ACL 시험이나 AC 인수로 표기하지 않음 |
| Grafana 관리 접근 | G1/G2 회신 수신. 관리 경로 사용 가능자 3명, Secret 사람 보관자·개인별 감사 근거 미확인 | 회신 수집 단계 종료. 미보유 자료 재요청 없이 남은 관리 책임·한계 정리 | 현재 자격증명 보관·회수 책임 및 감사 공백의 인수 판단. 자동 회전·권한 변경 없음 |

실무 수행·결과 수용 책임은 [#30 이관 결정][transfer]을 따른다. 원 생산자의 사실 확인과 독립 증적 리뷰는 보존하되 별도의 Lead 구현 GO나 모든 항목의 일괄 회신을 공통 시작 gate로 추가하지 않는다. 문서 검토를 단계마다 별도 승인으로 나누지 않는다.

Harbor 수정·검증은 기존 구축 세션에서 수행한다. 이 문서 작업은 서버 변경 없이 병행하며 Harbor 코드를 수정하거나 작업창을 소비하지 않는다. MON [증적207][mon207]은 10/13 10:01:11 KST 병합 완료다. 증적 병합을 MON 전체 AC 인수로 확대하지 않는다.

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

### 인수 판단에 넘길 항목

[이재환 회신][reply-mon]은 W4 시간·미측정 표기에 사실 오류가 없고 한계를 보존하는 데 동의한다고 확인했다. 이 회신은 사실 대조이며 최종 인수 선언이 아니다. 위 처분 문안은 재시험 없이 판단할 수 있는 상태다.

DB 전체 종결에는 별도 대조가 필요하다. 10/13 조회한 #11에는 핵심 요구의 `transaction-api 승인 경로만 허용`·`Client와 fds-engine 직접 DB 차단`이 미체크인 반면, AC의 `미승인 Source 접속 거부`는 기존 Lead 판정으로 체크돼 있다. 9/23 설명의 DB 포트 전체 허용·edge 허용은 당시 이력이며 10/8 보안 변경 후 현재 정책으로 사용하지 않는다. 체크 상태를 임의로 되돌리거나 올리지 않는다.

다음 최소 작업은 #19/10월 원본에서 승인 Source·DB `client_addr`·현행 allowlist·정상 Listener와 Client/fds-engine의 정책 차단을 대응시키고, **그 대조로도 남는 행만** 최종 APP/SEC 회차에 연결하는 것이다. W4 문안 채택과 이 요구의 충족은 별도 판단이며, 이번 문서 갱신은 그 전체 대조 완료를 주장하지 않는다.

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
- D1은 [이재환 회신][reply-mon]으로 연결 완료다. 기존 PC-D01·SHARE-D01 비공개 대장에 [수용 기록][d01-review], 대상별 크기·해시·책임·접근 범위·기한·정본 위치·삭제 절차가 연결돼 있다고 확인했다. 기록 시각은 10/12 **10:33:18 KST SHARE-D01 크기·해시**, **10:33:28 KST SHARE-D01 NTFS ACL 및 PC-D01 크기·해시**로 정정됐다. 수행자 이재환, `Get-FileHash`·`Get-Acl` 읽기 성공 보고다.
- 이 회신은 생산자 보고이며 독립 재조회가 아니다. D01의 SMB 공유 수준 ACL은 미조회다. 비공개 대장 재요청·dump 재전송은 하지 않는다. 경로·dump·내용·base64를 PR에 게시하지 않는다. 아래 C01 6개 archive에 대한 사용자 확인을 D01 보조 사본으로 확대하지 않는다.

### 최종 인수 기록안 — 아직 미채택

> #21의 9/29 DR Lead 판정과 증적67의 격리 복구·원본/복구본 비교·복구본 R02 E2E·원복/정리를 인수 근거로 사용한다. 당시 남은 Runbook은 infra-db PR11 병합, D01 이전은 10/11 수신 기록, 보관 추적은 10/13 D1 회신으로 연결한다. D01 두 보조 사본의 기존 한시 보존 조건과 SMB 공유 ACL 미조회 한계를 명시한다. 전체 Rule 최종 회귀는 #20에서 별도로 판정한다. 이 범위의 수용·종결 여부는 #30 이관 책임자인 이권욱이 결정한다.

이 문안 준비·원 생산자의 사실 확인·이미 체크된 AC·Issue 종결을 구분한다. #21은 조회 당시 OPEN/In Progress이며 이번 작업으로 변경하지 않았다.

## 4. C01 — 원본 증적 6개 보관 접근, 사용자 확인 수신

대상은 [증적195][custody]의 기존 archive **6개**다. C01은 시스템 모듈명이 아니라 원본 증적의 보관·접근 확인 항목 ID다. 수령·해시·보관 책임 수락을 다시 요청하지 않는다.

2026-10-12 23:34 KST에 기존 Windows 접근 권한으로 6개 파일의 메타데이터·NTFS ACL만 다시 읽었다. 모두 크기가 기존 수신표와 같고 상속된 Everyone·BUILTIN Users `Allow FullControl`이 남아 있었다. 파일 내용을 읽거나 재해시·복사·이동·삭제하지 않았다. 이 읽기는 아직 독립 증적 PR에 편입되지 않은 로컬 진단이며 새 PASS의 근거로 쓰지 않는다.

공유 ACL 조회는 기존 인증 경로에서 성공하지 못했다. SMB 연결 조회는 접근 거부, 23:39 KST CIM 조회는 WinRM 인증/신뢰 구성 제한으로 종료됐다. 조회 실패를 ACL 없음으로 해석하지 않는다. TrustedHosts·WinRM·인증·권한을 변경하지 않았다.

[SEC 회신][reply-sec]의 허용 기준은 권욱·하영·재환 3명이며, 그 밖의 주체는 대상·사유를 정한 별도 결정이 필요하다. 2026-10-13 KST 이권욱은 이 문서 후속 작업 채팅에서 **“승인받은 인원만 접근 가능”**이라고 확인했다. 이를 사용자 확인으로 수신하고, 실제 공유 관리자·조회 경로를 묻던 추가 요청은 종료한다.

사용자 확인과 기술 검증은 구분한다. 공유 ACL·그룹 구성·NTFS를 결합한 직접 대조는 수행하지 않아 기존 기술 검증 표시는 `NOT_VERIFIED`다. 넓은 파일 ACL 관측이나 조회 실패를 외부 공개·유출로 단정하지 않으며, 사용자 확인을 공유 ACL 조회 성공·독립 검증·AC 인수로 바꾸지 않는다. 새 승인 주체 추가, ACL 조정, 인증 경로 변경은 수행하지 않았다. 공유 계층에 관한 새로운 상충 증거가 생기면 그 범위만 재확인한다.

## 5. Grafana — 이미 받은 입력과 남은 입력

기준 [관리 접근 원장][grafana]의 source `0dd0235b07d44ba7965490e3808e0a67a3bd903b`를 재조회했다. Secret 값·비밀번호·키·새 인증시험을 수집하지 않는다.

| 재사용 가능한 사실 | 남아 있는 한계 |
|---|---|
| 과거 승인 Runner .20 → 제한 SA `p1-mon-pf-verify` → localhost13000/정확 Grafana Pod3000, 회수·DENIED 증적130 | 당시 제한 경로 검증. 현존하는 모든 관리 경로의 배타성 아님 |
| control01 관리 kubeconfig 메타데이터와 ClusterRoleBinding/그룹 이름 | 파일0600이나 RBAC 이름이 실제 사람·사본 수·접근 경로·감사를 증명하지 않음 |
| `monitoring-api/grafana-admin-credentials`의 admin-user/admin-password 참조 위치(증적185) | 실제 암호 유효성·인적 보유자·회전/회수 이력 미검증 |
| J04에 과거 control01 admin.conf→Pod exec 관리자 API 사용 보고 | 생성자·과거 감사 원본 미확인 답변은 유지. 같은 과거 자료를 다시 만들라고 요구하지 않음 |

### 10/13 수신한 현재 사실과 남은 판단

- [MON 회신][reply-mon]: Grafana Deployment는 기술 소비자이며 Secret의 **사람 보관자는 미확인**이다. 이재환은 암호를 받거나 보관한 적이 없고, 9/30 이후 관리자 사용 이력은 기록이 없어 확인할 수 없다고 답했다.
- control01 노드 인증과 sudo `admin.conf` → exec/PF 경로는 팀 3명 모두 사용 가능하다고 MON·[SEC][reply-sec]가 확인했다. 개인별 사용 기록은 없다. 공유 인증 경로를 개인별 추적이 되는 경로로 표시하지 않는다.
- 비상 VM 콘솔은 각 물리 호스트 담당자가 사용하며 사전·사후 기록 절차와 사용 조건은 미정이다. 이 회신을 새 콘솔 접근 허용으로 해석하지 않는다.
- API audit 설정 근거는 저장소 검색에서 찾지 못했고, 실제 control01 설정은 새로 조회하지 않았다. 따라서 **근거 미보유**이며 실제 기능이 꺼졌다고 판정하지 않는다. 9/22 이후 호스트 로그인/sudo·Grafana 관리자 API 감사는 미수집이다.
- 임시 SA/Role/Binding 회수는 증적130 범위에서 완료다. 현재 Secret의 보관·회수 책임과 감사 공백의 인수 판단은 남는다. SEC는 G2를 미보유/확인 불가로 회신했고 MON도 책임을 확정하지 않았으므로 새 책임자를 임의 배정하지 않는다.

G1/G2 회신 수집은 완료이며 같은 미보유 자료를 다시 요구하지 않는다. 이권욱이 위 한계를 기준으로 관리 책임·추가 확인이 필요한 최소 범위를 결정할 수 있게 연결했다. 신규 Secret 회전·계정 삭제·RBAC 변경을 자동 채택하지 않는다.

## 6. 회신 수신 상태와 남은 판단

회신을 받은 항목은 대기로 남기지 않는다. 비공개 위치·주체 상세·원본은 기존 제한 보관경로를 사용하고 PR에는 논리 ID, 시각, 확인 범위와 참조만 적는다. 사실 회신을 새 서버 실행·최종 인수로 표시하지 않는다.

| ID | 수신 상태 / 근거 | 완료로 인정할 범위와 남은 한계 |
|---|---|---|
| D1 | 수신 완료: [이재환 대장 연결·시각 정정][reply-mon] | 보존 추적성 연결. D01 공유 ACL 미조회 유지 |
| C1 | 관리자·조회 경로 추가 요청 종료: 이권욱 사용자 확인, §4 | 공유 ACL 원본을 직접 조회한 것은 아님. 기술 검증 `NOT_VERIFIED` |
| C2 | [SEC의 팀 3명 기준][reply-sec] + 이권욱의 승인 인원만 접근 가능 확인 수신 | 사용자 확인 범위 완료. 직접 그룹/실효 ACL 대조·AC 인수와 구분 |
| G1 | MON·SEC 회신 수신: [MON][reply-mon] / [SEC][reply-sec] | 경로 사용 가능자 확인. Secret 사람 보관자·비상 콘솔 사용 조건 미확정 |
| G2 | 미보유/미수집 범위 회신 수신: [MON][reply-mon] / [SEC][reply-sec] | 감사 공백과 현 자격증명 보관·회수 책임의 판단 필요 |

W4·DR 사실 오류 없음 회신은 연결했다. 사실 오류가 없다는 기술 검토를 인간의 최종 인수 선언으로 대체하지 않는다. 통합 판단은 #30의 이권욱이 맡으며 새 담당 선택 질문을 만들지 않는다.

## 7. 권장 처리 순서·완료 기록

1. §2 W4 처분과 §3 DR 인수안을 이권욱의 결과 수용 판단에 사용한다. DB 전체 종결은 §2의 별도 요구 대조 뒤 판단한다. DR은 기존 판정·후속 완료 근거를 재사용한다.
2. D1·C01·G1/G2의 회신 수집은 위 표로 정리했다. 미보유 과거 원본 재요청과 새 Restore를 추가하지 않는다. Grafana의 실제 관리 책임·감사 한계 판단은 독립적으로 진행한다.
3. W4 처분은 #11, DR 최종 인수·보관 경계는 #21, Grafana 접근 잔여는 #17/#19, C01 사용자 확인은 #30에 연결할 수 있다. 본 문서 PR만으로 Issue 상태·AC·종결을 갱신한 것은 아니다.
4. 수용 결정을 기록할 때 확인 범위·한계·담당·근거를 함께 남긴다. 이번 C01 확인을 D01이나 Grafana로 확대하지 않는다.

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
[reply-mon]: https://github.com/321Team/fds-project-baseline/pull/164#issuecomment-6135167475
[reply-sec]: https://github.com/321Team/fds-project-baseline/pull/164#issuecomment-6136134045
