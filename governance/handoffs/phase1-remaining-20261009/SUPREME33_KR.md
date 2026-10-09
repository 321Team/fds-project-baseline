# 이재환 인계 요청 — APP·DB·MON·HA

인계·업무 내용 검토: 이재환(@supreme33-kr) / 수신·잔여 통합 수행: 이권욱(@GWONUK)

이 문서 검토는 APP/DB/MON/QA의 사실·자료·시험 입력에 대한 업무 검토다. 정본 승인·발행 권한 부여가 아니다. 공통 원칙·회신 양식은 [README](README.md), 대기 중 진행은 [EXECUTION](EXECUTION.md)을 따른다.

[이재환의 23:07:58 KST 항목별 회신](https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6082572533)을 [수신 현황표](INTAKE_STATUS.md)에 반영했다. 아래 요청 중 이미 답변된 사실·보관 인수는 재요청하지 않고 남은 부분만 확인한다.

## 우선순위

1. J01~J02의 Delivery·Final Regression 입력. 이미 확정된 Source/시험 범위는 다시 승인받지 않는다.
2. J03의 dump 실제 인계와 J04의 관리 주체·감사 정보.
3. J05~J08의 잔여 관측·과거 한계·HA·운영 참여. 기존 근거가 있으면 링크만 제공하고 새 운영 시험을 인계 전제조건으로 요구하지 않는다.

H05 교차 인계: [evidence#34](https://github.com/321Team/fds-project-evidence/issues/34)의 옛 `robot$fds-ci` 생성 이력에 따라, 알고 있는 사용처·현재 관리 주체·삭제/30일 재발급 원본만 연결한다. 현재 credential을 보유한다고 가정하지 않으며 비밀값을 요청하지 않는다. Harbor 정책 입력은 H05와 함께 소비한다.

## J01 — APP 공급물·승인 후보의 실제 인수

- 연결: [APP 입력 확정](https://github.com/321Team/infra-cicd/issues/11#issuecomment-6074515472), [baseline#15](https://github.com/321Team/fds-project-baseline/issues/15), [evidence#189](https://github.com/321Team/fds-project-evidence/pull/189), [#190](https://github.com/321Team/fds-project-evidence/pull/190), [#195](https://github.com/321Team/fds-project-evidence/pull/195).
- 재사용: Source `affbc69beef9967f7977d09a6fec14f7fb6c0e94`, tool `8eac4c982076e3c219840a13686b15c46879981f`, 승인 consumer config, 원 ZIP/내부 Manifest, TBS51건·이미지2개 결과. APP PR29 설명 변경을 새 실행 Source로 바꾸지 않는다.
- 제공할 차이만: 기존 비공개 공급 ZIP의 보관 주체·접근 위치·목록/크기/해시·수령 확인, 승인 후 변경/누락, 만료 처리에 관한 기존 결정. 원 ZIP은 이미 이권욱 보관본이 있으면 재전송하지 않는다.
- GitHub Actions 다운로드 artifact `11585741989`의 보존 만료는 **2026-10-16 08:32:03 KST**다([공급 Run](https://github.com/321Team/fds-msa/actions/runs/37859961937)). 이미 수신·무결성 검증한 비공개 ZIP의 보존기간이나 실행 적격성과 구분한다. 사용 시점에는 승인 Source/설정, scan DB·report 최신성, TLS·Robot/Token 및 실행 계획의 유효성을 각각 확인한다. 다운로드 만료만으로 보존본 폐기·재빌드를 요구하거나 무기한 실행 가능하다고 판단하지 않는다.
- 완료: 실제 접근·원 Manifest 대조와 책임/보존기간 확인. 소스/공급도구 승인의 재승인은 필요하지 않다. 보존기간과 실행 artifact 유효기간은 다르다.
- 미제공 시: 유효성/완전성 미확인 공급물을 소비하는 실행만 대기. 기존 승인 소스·배포 plan·음성 시험 입력 준비 진행.

## J02 — 업무·E2E의 고정 입력과 판정 기준

- 연결: [baseline#20](https://github.com/321Team/fds-project-baseline/issues/20), [#15](https://github.com/321Team/fds-project-baseline/issues/15), [#4](https://github.com/321Team/fds-project-baseline/issues/4), [#5](https://github.com/321Team/fds-project-baseline/issues/5), [#6](https://github.com/321Team/fds-project-baseline/issues/6).
- 제공: 현 후보와 맞는 계약/fixture 참조, 정상·Rule·engine timeout/error·DB 저장 실패·미승인 경로·복구의 고정 입력/예상 HTTP·DB row/result·metric, 테스트 데이터 정리 방식과 기존 알려진 한계. KST/UTC·timestamp 입력과 판정 기준을 구분한다.
- 재사용: engine Unit16+Contract15/API Contract20, API Unit NOT_APPLICABLE의 기존 확정. 새 사업 규칙·보류·운영 UI·멱등성 기능을 추가하지 않는다.
- 고정 기준 재사용: [evidence#68](https://github.com/321Team/fds-project-evidence/pull/68)의 `criteria.txt` SHA256 `8aad7cc215137b97168230926d0e9655eba4dd3386944bf6efc06bfc83aae8d8`(P01~P05/N01~N07, DB22행·metrics 기대값)과 회신의 Rule/시각 입력 주의를 새 회차에 연결한다. naive 시각의 TZ 의존성은 담당자 추정이므로 구현/기준과 대조할 확인 항목으로 남기며 새 AC로 추가하지 않는다.
- 제공: 업무 포트 metrics 미노출과 전용 metrics 유지의 기대 결과, 기존 실패/복구 시험의 버전·대상·유효한 재사용 범위. 과거 Initial E2E를 최신 Final Regression으로 표시하지 않는다.
- 완료: 이권욱이 배포 회차의 성공·실패·복구를 사전에 고정된 기대값으로 판정할 수 있음. 시험 후 합격 기준을 바꾸지 않는다.
- 미제공 시: 해당 업무/Rule 판정만 대기. 이미 확정된 입력과 독립적인 CI/배포 준비는 계속한다.

## J03 — DR dump의 약속된 비공개 인계

- 연결: [baseline#21](https://github.com/321Team/fds-project-baseline/issues/21), [infra-db#1](https://github.com/321Team/infra-db/issues/1), [evidence#8](https://github.com/321Team/fds-project-evidence/issues/8), [DR Runbook PR11](https://github.com/321Team/infra-db/pull/11).
- 재사용: Runbook HEAD `18437f6e7636aee8ac0adb396ef34f70e8edecc0`, merge `cca6055316724b0bf9fa313925c04b54612e032e`. 이미 승인·병합된 Runbook을 다시 작성/승인할 필요는 없다.
- 제공: 9/3 원 dump 5,206B의 원본 위치·SHA256·생성 시각/DB 버전·연관 Manifest. 다른 백업의 3,596B 값과 혼용하지 않는다. 9/29 복구 시험 파일과도 구분한다.
- 실제 인계: 기존 약속된 db01 `/var/lib/pgsql/fds-evidence/` 비공개 수신 여부, postgres 소유·디렉터리0700/파일0600에 대한 실제 확인 기록과 수신 해시, PC 원본의 보존/처리 결정. 아직 전달하지 않았다면 미전달로 명시하고 기존 승인 경로로 이권욱에게 인계한다.
- 완료: 원본↔수신본의 식별·해시·권한/위치와 책임/보존 상태가 확인됨. 파일 전달을 새 Restore 성공으로 기록하지 않는다. 원본 삭제는 인계 확인 없이 수행하지 않는다.
- 미제공 시: 해당 DR 인계/최종 인수만 대기. 기존 restore·Row/Rule/E2E 증적 검토와 다른 실행 준비 진행.

## J04 — Grafana 관리 주체·자격증명 보관·감사

- 연결: [baseline#17](https://github.com/321Team/fds-project-baseline/issues/17), [MON PR42](https://github.com/321Team/infra-monitoring/pull/42), [evidence#175](https://github.com/321Team/fds-project-evidence/pull/175), [#185](https://github.com/321Team/fds-project-evidence/pull/185).
- 재사용: 과거 승인 PF 성공, ClusterIP 및 Secret 참조 위치의 수집. `monitoring-api/grafana-admin-credentials`를 찾았다는 사실을 실제 보유자·유효 암호 확인으로 확대하지 않는다.
- 제공: 실제 관리 principal·승인 운영자/단말·정상/비상 경로, credential의 실제 보관 주체/승인된 전달 참조, 회전·회수·감사 이력과 미확인 영역. Secret 값·admin.conf·개인키·비밀번호는 PR에 올리지 않는다.
- 역할: 이재환은 실제 사용·보관 사실을 전달하고, H03/H04의 정책 경계와 함께 이권욱이 잔여 통제/판정을 정리한다. 철회된 Grafana 예외를 승인으로 사용하지 않는다.
- 수신된 한계: 과거 임시 SA 접근과 회수, control01→Pod exec 관리자 사용은 회신으로 연결됐지만 앱 Secret의 원 생성자·보관자·회전/회수 이력은 미확인이다. 클러스터/비상 credential 메타데이터는 H03의 실제 보유자에게서 확인한다. 회신의 Secret 회전 제안은 구현·채택 결정이 아니다.
- 완료: 관측 사실·실제 사람/접근 경로·미확인 권한을 구분해 최소 추가 확인 범위를 정할 수 있음.
- 미제공 시: 권한 회수/접근 배타성의 완료 판정만 대기. 기존 문서·정책·공개 참조 대조와 비의존 작업 계속.

## J05 — MON/IF06B 잔여와 ICR 회차의 관측 입력

- 연결: [IF06B 잔여 정정](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6072071555), [baseline#14](https://github.com/321Team/fds-project-baseline/issues/14), [#17](https://github.com/321Team/fds-project-baseline/issues/17), [#19](https://github.com/321Team/fds-project-baseline/issues/19).
- 재사용: Source/401·gateway 원본, Discord Firing08:57/Resolved08:58, Probe 정의/Ready·격리 exec 관측, 기존 인수된 Target/관측 자료. 오래된 본문의 DOWN·미병합 문구를 최신 실패로 재사용하지 않는다.
- 제공: 최신 유효한 Target/로그/관측 경로와 원본 위치, MON의 관리 접근 배타성·edge01 HTTPS/API LB TCP Probe 실패/복구 외부 관측·IF06B의 남은 입력, 관측 계정의 승인 경로/권한, canary 자동 회수·Console에 대해 이미 정해진 사항.
- 책임 정정: Node 재기동·정책 지속성은 **#14 ICR-AC-18(이권욱)**이며 #17의 새 AC가 아니다. #17 Status의 포괄적인 Node 표현보다 실제 AC와 이번 회신을 따른다. 이재환에게는 필요한 회차의 전후 `up` 23/23 등 기존 관측 사실/경로만 연결받고, 회차 준비·수행은 이권욱이 맡는다.
- H04와 분리: 정책 귀속 기준은 기존 AC/결정에 맞추고 관측자는 실제 포인트·계정·로그 가능 범위를 넘긴다. 8443을 여는 우회는 이번 인계 내용이 아니다.
- 완료: 어느 행을 기존 근거로 닫고 어느 행을 새 관측해야 하는지 구분 가능. Prometheus Pod 재시작과 Node 재기동을 같은 시험으로 보지 않는다.
- 미제공 시: 해당 관측/재기동 회차만 대기. 사전 증적 분석·다른 영역 준비 진행.

## J06 — DB·과거 원본 공백의 사실 확인

- 연결: [baseline#11](https://github.com/321Team/fds-project-baseline/issues/11), [DB 접근통제 종료](https://github.com/321Team/fds-project-baseline/issues/11#issuecomment-6063472395), [infra-kubernetes#45](https://github.com/321Team/infra-kubernetes/issues/45), [evidence#4](https://github.com/321Team/fds-project-evidence/issues/4).
- 재사용: DB 접근통제 위험수용 종료와 기존 schema/Source, W4 Edge9파일·1,217기록 및 선택 수집. 종료된 위험수용의 재승인을 요구하지 않는다.
- 제공: W4 20:26:49~20:27:52의 미측정/수집 범위와 남은 원본의 존재 여부, 기존 원문 경로/시각, FUP 중 담당 생산 자료의 유실·콘솔 제출 한계. 알고 있는 사실만 확인하고 없는 원본을 새로 만들지 않는다.
- 완료: 미측정 사실과 영향이 특정되고 이권욱이 AC 충족/미충족·제한 처분을 판단할 수 있음. 오류0 샘플을 W4 전체 5xx0으로 확대하지 않는다.
- 미제공 시: 증거 부족을 명시하고 해당 인수 판단만 보류. 현재 시험으로 과거 원본을 소급 복원하는 재작업을 시작하지 않는다.

## J07 — HA 현재 형상과 기존 시험의 적용 범위

- 연결: [baseline#22](https://github.com/321Team/fds-project-baseline/issues/22), [K8S PR65](https://github.com/321Team/infra-kubernetes/pull/65), [baseline#15](https://github.com/321Team/fds-project-baseline/issues/15).
- 재사용: [evidence#92](https://github.com/321Team/fds-project-evidence/pull/92)의 **10/2 worker02 Drain/uncordon 재시험 1회**와 수용된 `/readyz` GET 표본. [원 AC 판정](https://github.com/321Team/fds-project-baseline/issues/22#issuecomment-5965966537)의 AC8/8은 그 범위로 유지한다. **9/27 결과는 NOT VERIFIED** 이력으로 보존하며 성공 근거나 검증된 비교 기준에 합산하지 않는다. 과거 1회 절차 예외도 새 회차로 승계하지 않는다.
- 제공: 시험 당시 manifest/digest·분산 상태·요청 간격/관찰 구간·허용 오류·복구 기준과 원본, 10/7 분산 형상 변경과 비교 가능한 입력, 당시 지적된 한계와 유효 판정. 10/8 철회된 Close 요청을 승인으로 올리지 않는다.
- 완료: 변경 영향 평가와 필요한 최소 재시험/제한 처분을 정할 수 있음. 현재 형상 재시험이 필요하면 이권욱이 회차를 준비한다. 모든 과거 시험을 자동 반복하지 않는다.
- 미제공 시: HA 최종 인수만 대기. 배포 준비·기존 원본 대조는 계속. Drain을 Node 재기동이나 데이터 Restore로 대신하지 않는다.

## J08 — 제3자 Runbook 재현·Runner 운영 인수

- 연결: [DOC#24](https://github.com/321Team/fds-project-baseline/issues/24), [Runner#61](https://github.com/321Team/infra-ansible/issues/61).
- 제공: APP/DB/MON/QA 영역에서 이미 수행한 제3자 재현의 대상·버전·실행자·원본, 필요한 추가 참여 가능 여부와 역할에 맞는 대체자 제안. 두 번째 Runner 운영자가 이미 있다면 실제 절차 인수·정리 결과를 연결한다.
- 현재 미지정인 역할은 미지정으로 유지한다. 이름을 적거나 Runbook을 읽은 것만으로 실습 완료를 표시하지 않는다. 이재환에게 정본 발행 승인이나 모든 영역 재실행을 요구하지 않는다.
- 완료: 필요한 제3자/운영 인수 주체와 실제 확인 범위를 기록하거나, 해당 잔여/일정을 식별함.
- 미제공 시: 독립 준비와 이미 검토된 범위의 허용 작업은 계속. 제3자 확인이 필요한 최종 AC만 대기한다.
