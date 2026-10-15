# 문서 정합화와 O01 제3자 재현 준비

2026-10-15 KST · CODEX_ASSISTED. 문서 Lead 이권욱, 기술 입력은 기존 업무 담당자. [#24](https://github.com/321Team/fds-project-baseline/issues/24)의 P0 Evidence 연결·As-built 차이·제3자 재현·Critical 문서 결함0 조건을 구체화한 준비 문서다. O01 수행자·시각은 미정이며, 이미 완료한 Runner O02를 O01 전체 완료로 표시하지 않는다.

## 1. 기존 문서에 연결할 최신 상태

| 대상 | 현재 반영할 내용 | 유지할 경계 |
|---|---|---|
| MON·SEC 인수표 | 207 IF06B, 212 Grafana, 223 실제 HTTP Probe, 231 Runner 권한을 [대조표](MON_SEC.md)에 연결 | 전체 AC 신규 인수 없음. 과거 DOWN/미실행을 현재 장애로 복제하지 않음 |
| APP/E2E | 224 기능·228 부하 병합, 233 D03 격리 성공/편입 대기를 [인수안](APP_E2E.md)에 연결 | D02/D04/I01·Critical0/최종 승인 잔여 |
| DB·DR | #11·#21 CLOSED 및 기존 인수 범위 반영 | W4·D01 보존/접근 한계는 유효한 결정대로 유지 |
| CICD | #16 AC05·AC07 인수 완료, AC08·09 기존 트랙 | AC07을 실제 만료 거부·rollback 성공으로 확대하지 않음 |
| Harbor·Ansible | 현재 후보 변경은 해당 PR의 단계 그대로 참조 | 미병합/미적용 후보를 최종 As-built로 기입하지 않음 |
| 인계/보관 | 기존 O02·Runner 운영 분리, Known Issue의 기존 Owner/Due/재검토 조건 유지 | O01 수행자·새 Due·자동 삭제일을 임의 지정하지 않음 |

기존 10/13 문서와 정본의 과거 시점 기록은 보존하고 이 후속을 연결한다. 파일 전체 재작성이나 최신 실행 원본의 덮어쓰기는 하지 않는다. 최종 source/digest와 현재 운영 설정은 Freeze 직전 해당 담당의 마지막 유효 결과로 고정한다.

<a id="grafana-cicd-followup-20261015"></a>

### 1.1 Grafana·CICD 확정 기록 연결 — 2026-10-15

**기준 시각: 2026-10-15 19:49:46 KST.** 다음은 위 초기 준비표와 아래 실행 준비 카드의 작성 당시 상태에 추가하는 후속 기록이다. 기존 원본·AC·명령은 보존하고 확정된 범위만 소비한다. 기존 O01 수행 범위는 [PR238 병합본 O01_COVERAGE](https://github.com/321Team/fds-project-evidence/blob/3bc75f62cffa23fc5184660b9564eaefa55ad18f/evidence/P1-DOC-01/o01-receipts-20261015/O01_COVERAGE.md)를 재사용하며, 이 문서에서 새 수행이나 전체 인수를 선언하지 않는다.

| 대상 | 확정 기록·소비 범위 | 유지할 경계 |
|---|---|---|
| Grafana 관리 접근·감사·C1 | [SEC 정정 18:54:33](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6189359354)을 반영한 [#30 사용자 승인 한정 처분](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6189715333)이 19:14:40 KST부터 유효. PF 기술배타성 NOT_MET + 한정 NOT_MET_RISK_ACCEPTED, E1/E2/E4 조건부 예외·E3 정상 사용 금지, 과거 감사 공백 한정수용, C1 APPROVED_DEFERRED | 실제 회전·인계·회수 완료가 아님. 미검증 데이터 경로·사람 사본 위험과 결정문의 기존 사용자/위치·발동·기록·비상 조건을 보존. 새 서버 작업·권한 확대의 포괄 승인 아님 |
| CICD 최종 인수·정본 인계 | [19:46:40 중앙 최종 결정](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-6190258707)에 따라 AC01~10·전체 Delivery 인수 완료. [infra-cicd #11](https://github.com/321Team/infra-cicd/issues/11)·[baseline #16](https://github.com/321Team/fds-project-baseline/issues/16)은 각각 19:47:54·19:47:58 KST Closed/completed 확인. AC02 한정수용, [AC09 Lead 단회 한정수용](https://github.com/321Team/infra-cicd/issues/11#issuecomment-6187579176), [증적 PR240 편입](https://github.com/321Team/fds-project-evidence/pull/240)을 유지 | AC09 원본 PATCH NOT_MEASURED·엄격 시각상한 UNPROVEN·사전 DB0행 미수집과 16:20 위험수용 종료를 유지. AC09 실제 실행 소스 fddc76e1c261cd938f06211b7ed035fdcb32e606의 결과를 새 실행 권한으로 재사용하지 않음. 정본 관리 인계와 새 Release 발행은 구분 |
| 정상 Health/E2E 소비 | [19:21 최종판단 요청](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-6189833532)에 대한 [APP Lead 이재환 19:36:55 회신](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-6190096759): 기존 169+234+224/228의 D04 결합을 정상 Health/E2E로 소비 가능하며 그 소비에 추가 필수 조건 없음 | 현행 이미지의 새 Client→edge POST나 전체 include/정책 동등성 실측이 아님. I01 naive/미래 이력, D02/D03 및 전체 APP Critical0·종결은 별도 잔여. 위 CICD AC03·AC10 최종 수용을 APP/E2E 전체 인수로 확대하지 않음 |

CICD의 독립 리뷰 범위도 최종 결정대로 보존한다. PR219의 실행 결과 HEAD 승인과 최종 결합 HEAD의 추가 APPROVED 부재를 구분하며, PR10은 COMMENTED 기술검토다. transport의 원본 `PURE_READ_PRECHECK` 오표기는 소급 수정하지 않고 실제 POST 2건으로 계상하며 다음 사용 전 표시 수정·검토 의무를 유지한다. APP·HBR·Ansible의 별도 잔여 및 O01/Freeze·전체 Phase 1은 이 CICD 종결로 완료하지 않는다.

Grafana 위험 소유·기록 보관/집계는 이권욱, 사용 기록 검토는 Phase 1 최종 인수 전 SEC 이하영이다. C1의 5종 트리거(ClusterIP 외 노출, 상시 PF 신설, 팀원 변경/이탈, 사본 유출 의심, Worker 셸 접근자의 보고된 E1 보유 3명 밖 확대)와 재검토·미래 회전의 PARTIAL 복구/세션 검증 조건은 확정 처분 원문을 따른다. 접근자가 3명뿐이거나 모든 접근에 클러스터 자격증명이 필수라고 단정하지 않는다.

**O01/Freeze의 정확한 잔여:** F1은 Architecture/As-built·Test/Evidence Index·전체 핵심 Runbook의 최종 제출 목록과 Source/Version, 실제 형상 차이·유효 Change/Known Issue 연결의 확정이다. F2는 AC07·Probe223·O02의 기존 재사용 범위와 미대응 핵심 절을 요구에 대응한 DOC Review 판정이다. 특히 [MON Runbook 고정본](https://github.com/321Team/infra-monitoring/blob/0dd0235b07d44ba7965490e3808e0a67a3bd903b/docs/RUNBOOK_P1_MON_01_20261002.md)의 §4.2 PVC 재바인딩·§4.4 Silence·§5.1 객체 Rollback 및 §5 미실행 행은 문서화와 실제 재현을 구분해 판단해야 한다. NOT_RUN을 전수 현장시험의 새 필수조건으로 바꾸지 않는다. F1/F2, 다른 필수 인수 입력·미해결 책임, 문서 Critical0·Version/Source·Review 및 인계가 남아 **O01 전체·DOC Freeze·문서 Critical0는 미판정**이다. 아래 기존 Freeze 조건은 그대로 적용한다.

## 2. O01 실행 준비 카드

이 카드는 제3자가 따라갈 절차의 준비안이다. 작성자의 오프라인 확인을 제3자 실습으로 집계하지 않는다. 이미 성공한 장애 주입/배포를 재현 실적 확보 목적으로 반복하지 않는다.

| 단계 | 환경·실행 위치와 순서 | 정상 판정 | 실패 시 중단·복구 |
|---|---|---|---|
| A. 입력 고정 | 제3자의 로컬 검토 디렉터리. baseline의 이 문서 PR 최종 SHA, evidence의 승인/병합 SHA, 필요한 Python 버전을 기록. `SOURCE_INDEX.json`에서 대상만 선택 | source·증적·상태·실행 회차가 서로 대응. 아직 열린233은 검토 후보로 구분 | HEAD/원본 불일치면 해당 항목 사용 중단. 기존 자료 삭제/재다운로드 덮어쓰기 없이 별도 후보 보존 |
| B. 증적 탐색 | 고정 evidence checkout에서 README→원본→판정기를 따라가 대상·시각·명령·rc·실패/복구를 설명 | 제3자가 실제 성공과 MOCK/정의·조회·한계를 구분하고 원본을 찾을 수 있음 | 경로/의존성/판정 근거가 끊기면 문서 결함으로 기록; 서버 재시험으로 대체하지 않음 |
| C. 오프라인 재판독 | 아래 기존 판정기를 검토 후 로컬에서 실행. 원본은 읽기 전용으로 취급. 생성물은 별도 검토 폴더 | 기존 범위와 동일한 판정 및 raw 근거 확인. 해시 일치를 Runtime 성공으로 대체하지 않음 | 비정상 rc/불일치 시 이후 대상 중단, stdout/stderr·환경 보존. 제품/원본 수정 없음 |
| D. 운영 Runbook 검토 | 해당 서비스의 기존 실행·복귀 문서를 읽어 대상/계정/정확 경로/버전/선행조건/정상/중단/복구/정리 점검 | 운영 입력이 미정인 부분은 명시, 안전하게 실행할 수 있는 단계와 변경 단계를 구분 | 운영 입력·권한·복구점이 없으면 실제 명령을 실행하지 않음 |
| E. 현장 핵심 재현 | O01의 아직 덮이지 않는 필수 현장 범위가 확인될 때만 대상·수행자·고정 소스·비중첩 창·복구 조건을 완성 | 실제 수행자가 직접 남긴 명령/시각/rc/원본·결과가 그 범위에 결속 | 같은 Runner·공유 서비스 점유/관측 불가/대상 불일치면 중단. 해당 회차에 정한 복구만 수행 |
| F. 인수 | 수행자가 재현 결과와 문서 결함을 #24에 연결, 문서 Lead가 남은 P0/Known Issue와 함께 검토 | 재현한 범위·미실행 범위·결함 처분이 명시됨 | 오프라인 판정 성공만으로 O01 전체·DOC Freeze·Phase1 Close 승인 금지 |

### 검토한 기존 오프라인 진입점

실행 위치는 **고정 커밋으로 받은 fds-project-evidence 저장소 루트**다. Python3와 각 README의 의존성이 필요하다. 이번 문서 작업에서는 아래 명령을 새로 실행하지 않았다. 실행 전에 해당 소스가 로컬 원본을 읽는 판정기인지 다시 확인한다.

```text
python -I -B evidence/P1-K8S-01/http-probe-runtime-20261014T0950/verify_result.py evidence/P1-K8S-01/http-probe-runtime-20261014T0950
python -B evidence/P1-CICD-01/ac07-native-runtime-20261014/verify.py
```

- 첫 명령은 증적223의 원문 명령이다. 정상 결과 `HTTP_PROBE_RUNTIME_PASS_WITH_RECORDED_OBSERVATION_LIMITS`와 관측 한계를 함께 읽는다.
- 두 번째는 증적231의 원문 명령이다. 고정25권한·GET2·전후 불변/정리 등 해당 범위를 재판독한다. 만료401 검증을 새로 얻는 명령이 아니다.
- D03은 PR233 독립 편입 이후 그 README의 `verify.py`와 원본 case-result/DB rollback/cleanup을 연결한다. 미병합 후보의 판정을 최종 봉인 증적으로 표시하지 않는다.
- 파일 바이트의 SHA256 일치는 무결성 검증이며, 기존 실행의 실제성과 요구조건 대응은 원본과 판정 내용을 별도로 확인한다.

## 3. 최종 Freeze 체크

- P0별 AC→증적→실제 실행→검토·병합→인수 범위를 연결한다. 이 문서의 작성 완료를 AC 완료로 세지 않는다.
- 최신 운영 IP/Port/이미지·source·도구·정책과 As-built를 비교하고 차이는 유효한 변경/기존 Known Issue에 연결한다.
- 새 미완료 항목은 풀네임 Owner·Due 또는 재검토 조건을 확정해야 한다. 이 문서가 임의 일정을 부여하지 않는다.
- Harbor·CICD·Ansible의 마지막 실제 변경이 발생하면 그 영향 행과 관련 Runbook만 갱신한다.
- O01 제3자 결과와 Critical 문서 결함 처분, 해당 Gate/Review 결과가 모인 뒤 #24→#30의 Freeze/Close를 판단한다. 현재는 준비 단계다.

이 문서는 금융 규제 준수 완료를 주장하지 않으며, 서버 설정·보안 통제·비밀값을 변경하거나 수집하지 않는다.
