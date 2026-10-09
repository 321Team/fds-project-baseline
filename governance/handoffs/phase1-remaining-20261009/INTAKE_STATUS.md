# Phase 1 실제 수신 현황과 다음 작업

작성: 이권욱 / CODEX_ASSISTED · 2026-10-09 KST, 회신 현행화 2026-10-10 KST

## 기준 시점·판정 단위

- AC/Status는 [README의 정본·소스 기준](README.md), 22:08:28 KST 현행화 조회를 사용한다. 이 표는 AC·Status를 변경하지 않는다.
- 인적 회신은 10/9 [H01 보관 인수][h-custody]·[H02~H07][h-reply], 10/10 01:23:18 KST [R1/R2][h-r12]·01:27:12 KST [J03/H05 정정][j-correction]까지 반영했다. J의 다른 행은 [10/9 23:07:58 회신][j-reply]을 유지한다. 인계 PR160은 HEAD `151a60536e6c18a9f6f3b0a1d20bf61db950b763`의 두 담당자 리뷰 후 merge `068411bd3bef2747587933a2b0b137810affb903`로 병합됐다. 후속 문서 리뷰·Runtime·AC 인수는 별도다.
- 이권욱 세션의 읽기 검증: 22:50~22:52 KST 원본 6묶음의 로컬/공유 사본 12개 크기·외부 SHA256 일치, K8S 내부 38/38·APP ZIP 내부 125/125 확인. APP raw 내부 69 payload는 이번에 전수 재검사하지 않았으며 [증적195][custody]의 기존 검증을 재사용한다. 도구 검증은 지정 보관자의 사람 인수나 공유 권한 검증을 대신하지 않는다.
- 상태는 **기존 근거 재사용 / 사실 회신 수신 / 일부 수신·추가 입력 대기 / 보관 인수 회신 완료 / 한계 처분 필요**로 구별한다. 사실 회신은 제공자가 확인한 범위이며 서버 현재 상태를 독립 실측했다는 뜻이 아니다.
- 모든 행의 수신 검증·새 회차 준비·실행·범위 내 결과 판정은 이권욱이 담당한다. 기존 생산자/보관자는 별도로 표기한다. 완료 입력은 재요청하지 않으며 모든 행의 동시 완료를 요구하지 않는다.

## 이하영 관련 입력 — 사실 회신 반영, 현장 입력 별도

세부 제출·완료 기준은 [H01~H07](HAYEOUNGLEE.md)을 따른다.

| ID · 기존 AC/잔여 | 현재 확인·근거 | 남은 최소 입력 · 실제 제공자 | 막히는 작업 / 계속할 작업 |
|---|---|---|---|
| H01 · #10 원본 보관/형상 복구 | **보관 인수 회신 완료**. [H01][h-custody]에서 162,981B·SHA256 및 실제 보관 인수 확인. 내부38건은 기존 검증 재사용 | 보관 인수 재요청 없음. C01 유효 접근통제와 현장 backup/restore는 별도 | 보관 인수 회신 대기 해소 / 파일 분석·복구안 계속. 서버 복구 성공 아님 |
| H02 · #10 17파일 교체 및 별도 AC4·T14/T15/전체 Exit | **기대값·한계 회신 수신**. [H02][h-reply]: 17개 system_u:object_r:usr_t:s0, root:root·0750·기본 ACL·추가 ACL/capability 없음이라는 목표. 변경17/유지28/control02 제외, AC3·5 ACCEPTED 유지 | 이권욱: 실패 시 복귀 context, 실제 호출/동시 작성자 배제·fresh backup/restore. AC4의 c·d②·e와 위험수용 제안 g, T14/T15 NOT_VERIFIED/CAPTURE_INVALID 및 처분7건 별도 | 해당 파일 쓰기·relabel 및 미입증 AC 인수 대기 / diff·복구 설계 계속. 부모 경로·xattr의 실제 확인은 목표값과 구분 |
| H03 · #19 SEC-AC02/04/05/06; #16 자격증명 소비 | **정책 의미 회신 수신**. [R1][h-r12]: Token 최대/요청900초, 3600초는 기존 검증값. audience·갱신·CA 참조와 기존 AC 한계 [H03][h-reply] 수신 | 이권욱: CICD plan/gate/binding/JWT·정책 참조 정합화 및 시험, 실제 SA/접근·클러스터/비상 principal·사본/회수 한계, 미포함 SEC 행. 비밀값 비공개 유지 | Token 의미 회신 대기 해소 / 코드·최소 Matrix 준비 가능. 실제 발급·소비·보안 시험·AC 인수 미완료 |
| H04 · #14 IF06B/ICR 및 CR130 OID-02 | **귀속 수준 회신 수신**. [H04][h-reply]: gateway 구간 귀속, 특정 rule 귀속은 미요구. Source/401 증적122·gateway151 재사용. OID-02 preloaded·control01 drain 금지·OID-03 PENDING 유지 | 이권욱: 기존 monitor SYN 기준과 대체 기준의 적용 범위 연결, canary 만료/Console·관측 계정·원복안. OID 두 digest의 공급 원본/경로/Due 미정. AC 변경이면 Decision/CR | 해당 관측·정책 변경·판정만 대기 / 기존 raw 분석·최소 관측안 계속. 새 Runtime 성공 아님 |
| H05 · #13 HBR AC04~06; #16 Delivery | **회신·이력 정정 수신**. [R2][h-r12]: 소비자 확인 후 만료 전 정리 가능. [10/1 legacy Secret 삭제][legacy-deleted] 및 [10/10 재확인][reply-review]으로 해당 저장소 정리 대기 해소. TLS/IF09/10 과거 관측 유지 | 조직 Secret 확인 경로 U02·Harbor 실제 관리 접근 U03은 [보충 요청][open-inputs]. 이권욱: 현 소비자·edge01 Secret, Robot/CA/trust·scan/DB 시각·freshness, .50/.102·IPv6/INPUT 처분. 보관자/유효성 추정 금지 | archived Secret 중복 삭제 제외 / 해당 Push/Deploy·운영 인수는 현장 입력 필요. 전체 AC06 완료 아님 |
| H06 · #13 인수한 복구/자동복구 | **미기록 제약·미확인 회신 수신**. [H06][h-reply]: A2 이전 snapshot은 현재 backup 아님, 수동 변경 기록·원 승인 policy/전체 작성자 미확인. PR32~40·Linux270/270·증적191 재사용 | 이권욱: fresh UUID/격리·10개 ID·unit/tool/Compose/Engine/StopSignal·실측 예산, installer/H6·늦은 stop·세대 변경 복구, 게스트 private 원문 보존. 이미 모른다고 답한 자료 재요청 없음 | 복구점이 필요한 위험 회차만 대기 / 구현·정적/모의·실행 패키지 준비 가능 |
| H07 · #24 제3자 핵심 재현; Ansible#61 두 번째 운영자 | **미실행·참여 미정 회신 수신**. [H07][h-reply]의 독립 리뷰 목록은 실제 재현 증거 아님 | 이권욱: 구체 대상·시간·정상 접근을 포함한 회차 제시 후 적격 참여자 확인. 미정 참여를 선지정하지 않음 | 해당 제3자/운영 인수만 대기 / 코드·문서·자체 준비 계속 |

SEC 행별 대조는 [#19의 현행 AC 기록][sec]에서 시작한다. AC02의 기존 확정 실패·위험수용, AC04 특정 정책 귀속/부팅 연속 보호, AC05 encryption·rollback·격리 backup 성공과 예방 rotation NOT MET/RISK ACCEPTED, AC06 exec/정의/Ready와 실제 APP HTTP 잔여를 분리한다. 폐기된 집계·CR126~128을 복원하지 않고, 빠진 **행과 기대 결과만** 보완한다. [검토 정정][reply-review]처럼 증적157의 IF-03 목적지 SYN/DROP 및 IF-13A 일반 Pod/hostNetwork 지정 표본 관측을 미실행으로 되돌리지 않는다. 표본의 한계와 최종 AC 인수는 별도다. Token 회수도 현 구현 미수행과 SA 단위 무효화 가능성을 구별한다.

## 이재환 관련 입력 — 기존 회신과 10/10 정정 반영

아래 사실의 제공자는 이재환이며 기본 회신은 [한 댓글][j-reply], J03/H05의 후속은 [10/10 정정][j-correction]에 있다. 세부 완료 기준은 [J01~J08](SUPREME33_KR.md)을 따른다.

| ID · 기존 AC/잔여 | 현재 확인·근거 | 남은 최소 입력 · 다음 담당 | 막히는 작업 / 계속할 작업 |
|---|---|---|---|
| J01 · #15/#16 APP 공급 원본 | **보관 인수 회신 완료**. ZIP 109,786,915B·SHA256·125/125·목록 외0·Source affbc69/tool8eac4c 확인 및 이재환 보관 책임 인수. 변경/누락 없음이라는 회신 | 보관 인수를 다시 요청하지 않음. 이권욱: 사용 시점 scan/TLS/Robot/계획 유효성. C01 접근통제는 별도 | 공급 원본 준비 가능 / 현재 실행 적격성은 별도 확인 |
| J02 · #20 Final Regression; #15 업무 metrics | **고정 입력 회신 수신**. [증적68][e2e] criteria SHA256 `8aad7cc2…`, P01~P05/N01~N07·DB22행·기대 metrics. N+1 Rule, occurred_at, engine fail-open, SIM 정리 참조 수신 | 이권욱: affbc69와 기존 기준의 차이, 새 RUN fixture·KST/UTC·실패 HTTP/DB/metrics·정리/복구 결속. naive/TZ는 회신의 미확인 주장으로 코드 대조. 모순 발견 시만 담당자 추가 확인 | 최신 Final Regression 판정은 새 회차 후 / 기존 기준을 재작성·재승인하지 않고 계획 작성 가능 |
| J03 · #21 DR Exit/9월3일 dump 이전 약속 | **원본 사실·전달 후보 수신 / 미전달**. 5,206B·SHA256 `80962dcd41c8afe3920c7194e8b5e2a4531ee901b4027aad1d47209ed4a46f3d` 유지. [후속][j-correction]: 10/11(일)19:00 이후 가능, db01 콘솔/server08+sudo·base64 전달 제안 | 이재환: 붙여넣기 실현성 또는 기존 허용 전달 경로 U01 회신. 이권욱: 정확한 시작·비중첩·수신 위치/해시·postgres 소유·0700/0600·시각 확인. 30분은 담당자 예상 | DR 실제 인수/Close 대기 / 시간 후보를 확정 창으로 쓰지 않음. 수신 확인 전 PC 삭제 금지 |
| J04 · #17 Grafana 관리 접근 배타성 | **사실·한계 회신 수신**. 과거 임시 SA PF와 삭제/DENIED, control01 admin.conf→Pod exec 관리자 API 사용 확인. Secret 생성자/보관자·회전/회수 이력은 미확인 | 이권욱: H03 실제 보유자 입력과 앱/클러스터/비상 경로 대조. 원 생성자/감사 자료 존재 여부 확인; 회신의 Secret 회전은 제안이며 아직 채택·실행하지 않음 | 배타성/감사 인수 대기 / 접근 원장·잔여 통제안 작성 가능 |
| J05 · #17 Probe 외부 실패/복구·IF06B; #14 ICR-AC18 관측 연계 | **부분 수신**. Discord 08:57/08:58·원복08:58:24. MON 잔여는 관리 배타성, edge HTTPS/API LB TCP Probe 실패/복구, IF06B. H04의 gateway 구간 귀속 선택은 수신. Reboot는 MON AC가 아님 | 이권욱: H04 선택과 기존 판정의 대응, canary 만료/Console·gateway/monitor01 계정의 구체안. 원 담당자는 새로 발견한 기존 정보만 보완 | 해당 관측/ICR reboot 회차 대기 / 전후 up23/23 등 관측안 준비. 과거10/6 GO로 새 창을 대신하지 않음 |
| J06 · #11 W4 한계; FUP04~07 과거 원본 | **한계 사실 수신·처분 필요**. W4 20:26:49~20:27:52 NOT_MEASURED, 이재환이 아는 별도 원본 없음. Edge9파일·1,217기록으로 전체5xx0 판정 불가 | 이권욱: 영향·처분 작성. FUP별 원 생산자: 04 과거 로그, 05 당시 승인 참조, 06/07 개별 회신 시각/WBS 원본의 존재 여부만 확인. J 회신은 FUP 전체 원본 유실 확인이 아님 | 해당 최종 판단 대기 / 현재 시험으로 과거 공백을 메우지 않고 다른 작업 계속 |
| J07 · #22 HA Exit/변경 영향 | **기준·원본 참조 수신**. 증적92의 10/2 worker02 1회 A=0·Bmax0.510s, 0.5s tick. 9/27 NOT VERIFIED | 이권욱: 10/2 당시와 10/7 PR65 이후 manifest/digest·분산의 영향 평가, 최소 재시험 또는 제한 처분의 근거. 과거 AC8/8을 유지하되 현행 전체 HA로 확대하지 않음 | HA 최종 인수 대기 / 과거 원본 비교·현행 계획 준비 |
| J08 · #24 핵심 재현; Ansible#61 운영 인수 | **미실행·미지정 회신 수신**. 이재환의 직접 제3자 재현 없음, 두 번째 Runner 운영자 미지정, 추가 참여 미정 | 이권욱: 필요한 회차/대상 제시. 적격 참여자: 정상 계정 접근·실제 수행/정리 원본. #61 상시 queue/알림 운영은 직접 작업 S04 | 해당 운영 인수/최종 완료 대기 / 독립 준비 계속. 독립 코드 리뷰를 재현 실적으로 치환하지 않음 |

J02의 고정 파일 전체 SHA256은 `8aad7cc215137b97168230926d0e9655eba4dd3386944bf6efc06bfc83aae8d8`이다. 과거 24 PASS는 당시 결과이고 새 후보/현재 환경의 Final Regression 결과가 아니다. 업무 포트 metrics 404·전용 수집 유지의 후보 기대값과 이전 이미지 복귀 시 노출 복원을 함께 확인한다.

## 공통 원본 보관 — 지정과 실제 인수 구분

파일 목록·SHA256·원 보관/전송 시각의 정본은 [증적195의 보관 지정/영수증][custody]을 재사용한다. 아래는 이번 수신 상태만 덧붙인 것이며 새 독립 증적 편입 완료 선언이 아니다.

| 원본 · 크기 | 지정 보관자 | 확인된 상태와 잔여 |
|---|---|---|
| `k8s-tool-backup-20261009T091654.tar.gz` · 162,981B | 이하영 | 세션 바이트/내부38건 대조 + [H01 실제 수령·보관 인수][h-custody] 완료. C01 접근통제와 실제 서버 backup/restore는 별도 |
| `app-supply-37859961937.zip` · 109,786,915B | 이재환 | 세션 대조 + J01 실제 읽기/보관 책임 회신 완료. C01은 별도 |
| `app-tbs-37890963668-metadata.tar.gz` · 8,213B | 이권욱 | 도구를 통한 로컬/공유 바이트 대조. 지정 보관 책임·실제 접근 제한은 원 결정/후속 확인과 연결 |
| `ansible-ci76-11602757338.zip` · 512,208B | 이권욱 | 위와 같음 |
| `ansible-ci76-host-evidence.tar.gz` · 6,334B | 이권욱 | 위와 같음 |
| `app-raw-37890963668.tar.gz` · 326,294,507B | 이권욱 | 로컬/공유 외부 해시·크기 대조. 내부69 payload는 증적195의 기존 검증 범위 재사용 |

**C01 — 유효 접근통제 확인 필요.** 22:52 KST 읽기 조회에서 파일시스템 ACL의 Everyone·BUILTIN Users 상속 FullControl을 확인했다. SMB 서버 측 공유 ACL·허용 주체/그룹 구성은 **미조회**다. 현재 세션의 읽기 성공이나 해시 일치로 승인 사용자만 접근한다고 입증할 수 없고, 파일시스템 ACL만으로 외부 공개를 단정할 수도 없다. 사용자 진술과 독립 권한 확인을 구별한다.

- 필요한 입력: 실제 공유 서버 관리자(현재 문서상 미확정)의 해당 공유 ACL·허용 계정/그룹 범위 및 보관자의 접근 확인. 이권욱이 승인 경로의 읽기 확인을 연결한다. 관리자 신원을 임의로 지정하지 않는다.
- 소비: 원본 보관의 접근통제 판정. 이 확인 없이 새 민감 원본을 추가 전송하거나 권한 통제를 완료로 올리지 않는다. 기존 원본·ACL을 임의 변경하지 않고 기존 사본의 오프라인 분석은 계속한다.
- 보존: 증적195의 자원 회수기간 종료(현재 10/26 계획) 결정을 유지한다. 정확 종료 시각·삭제 실행을 임의 확정하지 않는다. GitHub 다운로드 artifact 만료와 별개이며 자동 삭제/재압축/덮어쓰기는 하지 않는다.

## 원 담당자의 답변으로 대체할 수 없는 이권욱 직접 작업

| ID · 기존 책임 | 다음에 만들 결과 · 완료조건 | 의존/대기 범위 |
|---|---|---|
| S01 · #16/#15/#20 Delivery·Final Regression | 승인 workflow SHA, UUID, SA/audience/TTL/CA/정책, target namespace/deployment/container/UID·복귀 image, 유효 구간·중단/복구를 고정한 계획. Push 후 새 receipt와 digest를 Deploy에 결속. 정상/Negative/rollback/최종 형상 회귀 결과를 구분 | H03/H05·J01/J02를 필요한 단계에서 소비. [증적198][delivery]의 `rollback_approved=false`와 관측 시각을 보존. 이전 image 복귀 시 metrics 노출이 돌아오는 보안 영향도 종료 상태에 기록 |
| S02 · #13 복구/자동복구 | installer·H6·늦은 stop/세대 변경 복구의 구현·검증·필요한 독립 리뷰, fresh 호스트 입력·원 policy 복원·게스트 private486 보존 확인 후 정확한 Runtime 결과 | H06의 미기록 제한만 추가 수신. 이미 수신한247파일을 전체486 보존으로 확대하지 않음. 운영 Registry 정상성/비중첩이 충족되면 S01의 공통 완료 Gate로 만들지 않음 |
| S03 · #10/#14/#19/#17/#22 | 파일별 복원안과 AC4/T14/T15 대응, SEC의 미입증 최소 행, IF06B 판단·관측/원복안, ICR-AC18 reboot 지속성, HA 형상 영향 평가. 각 회차 성공/중단/복구·원본·AC 대응 | H02~H04·J04/J05/J07. 원 담당자에게 새 전수 시험을 요구하지 않음. AC 변경/새 위험수용은 단순 실행 결과와 별도 판정 |
| S04 · Ansible#9/#61 | worker02 apply/reapply/rollback·엔진 전환 입력/실측, 상시 queue·알림 운영 기록, 두 번째 운영자의 실제 인수 | 기존 이권욱 업무로 추적. 의존하는 해당 실행만 대기하며 전체 Phase 1 공통 Gate로 확대하지 않음 |
| S05 · #11/#21/#24/#30 및 Gate | dump 실제 수신 확인, 과거 공백의 영향/유효 처분, 제3자 핵심 재현·원본 보관 인수·최종 형상과 하위 AC 판정 연결 | J03/J06·H07/J08·C01 중 해당 부분. 없는 과거 원본은 생성하지 않고 미충족/한계를 보존. 최종 Sign-off는 실제 완료조건 충족 범위로 판단 |

현재는 문서·입력 대조 단계다. 위 직접 작업의 새 구현·Runtime·최종 인수는 이 표 작성만으로 완료되지 않는다. 입력이 확보된 묶음부터 진행하되 공유 호스트/클러스터/Registry 변경은 비중첩으로 실행한다([EXECUTION](EXECUTION.md)).

## 후속 회신을 받았을 때

현재 담당자 보충 요청은 [U01~U03][open-inputs]으로 좁힌다. 기존 R1/R2 정책 의미와 legacy 저장소 삭제는 다시 묻지 않는다. [#30 이관 결정](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6082618226)을 기준으로 이권욱이 통합 판정하며, 후속 회신의 별도 HBR Lead 확인을 새 필수 GO로 채택하지 않는다. 이재환의 Harbor 삭제 수행 의사는 실제 접근·정확한 회차를 확인할 실행 분담이며 인수 권한의 반환이 아니다.

해당 H/J/C/S 행에 `자료/판정의 정확한 버전·확인자·KST 시각·원문 링크·해소된 빈 값·남은 값`만 갱신한다. 알려진 사실이 없다는 답변도 유효한 인계로 기록하고, 그 사실을 전체 검증 성공으로 바꾸지 않는다. 새로운 보안 설정·회전·허용 범위는 회신자의 제안을 자동 실행하지 않고 기존 AC/유효 결정과 대조한다. 이 표에 Phase 2 구현이나 미채택 DB 알림을 필수 잔여로 추가하지 않는다.

[h-review]: https://github.com/321Team/fds-project-baseline/pull/160#pullrequestreview-5470895792
[j-reply]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6082572533
[custody]: https://github.com/321Team/fds-project-evidence/pull/195
[delivery]: https://github.com/321Team/fds-project-evidence/pull/198
[sec]: https://github.com/321Team/fds-project-baseline/issues/19
[e2e]: https://github.com/321Team/fds-project-evidence/pull/68

[h-custody]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6083078172
[h-reply]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6083293377
[h-r12]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6084886811
[j-correction]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6084948949
[legacy-deleted]: https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5924842213
[reply-review]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6086529018
[open-inputs]: OPEN_INPUTS_20261010.md
