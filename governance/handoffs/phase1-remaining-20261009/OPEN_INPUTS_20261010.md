# Phase 1 인계 보충 회신 — 확인할 입력과 실행 잔여

작성: 이권욱 / CODEX_ASSISTED · 2026-10-10 KST

## 이번 문서의 목적과 기준

[PR160][pr160]은 reviewed HEAD `151a60536e6c18a9f6f3b0a1d20bf61db950b763`, merge `068411bd3bef2747587933a2b0b137810affb903`로 병합됐다. 이 후속은 뒤늦게 수신한 사실을 현황표에 반영하고, 아직 필요한 답변의 담당·범위·완료조건을 명시한다. 자료가 없다는 답변을 미회신과 구분하며 이미 수신한 H/J 전체를 다시 요청하지 않는다.

사용자 요청은 기존 인계 PR 병합과 미확인 부분을 설명받기 위한 새 PR 발행이다. 실행 코드·배포 입력은 바꾸지 않는다. 문서 병합·회신 완료를 Runtime·AC 인수·티켓 Close 또는 정본 발행으로 표시하지 않는다. [#30 이관 결정][delegation]의 Phase 1 잔여 범위와 코드/증적 독립 리뷰를 유지하며 Phase 2 사전작업은 포함하지 않는다.

## 확정 또는 정정된 부분 — 다시 질문하지 않음

| 기존 ID | 확인한 사실과 출처 | 여전히 별도인 것 |
|---|---|---|
| H01 | [보관 인수 회신][custody]: K8S archive 162,981B·SHA256 확인 및 책임 인수. 내부38건은 기존 검증 재사용 | C01 유효 접근통제, 실서버 backup/restore |
| H02 | [H 회신][h-reply]: 17파일 목표 label `system_u:object_r:usr_t:s0`, root:root·0750·기본 ACL, 추가 ACL/capability 없음. 부모 /opt·/opt/fds0755 및 패키지 root/code0750이라는 목표 수신 | 원 관측값과 목표값을 혼동하지 않음. 선택 xattr 관측만으로 모든 xattr/부모 ACL 부재를 단정하지 않음. 복귀 context·호출 배제는 이권욱 회차 준비 |
| H03·R1 | [정책 의미 확정][h-r12]: 최대 수명과 요청 수명900초. 3600초는 별도 허용이 아니라 정합화할 기존 검증값 | CICD `c9eff5fb…`의 plan/gate/binding/JWT·정책 참조 수정과 시험, 실제 발급/소비 |
| H03 SEC 행 | [증적157 일반 Pod 보강][sec-pod]·[hostNetwork 보강][sec-host]은 기존 IF-03/IF-13A 지정 표본을 보완 | L3/L4 표본·counter 상관의 한계와 전체 AC 인수를 분리. 과거 미검증 문구로 수집 완료 표본을 되돌리지 않음 |
| H04 | [H 회신][h-reply]의 요구 수준은 gateway 구간 귀속, 특정 rule 귀속은 미요구 | 기존 monitor SYN 기준과의 대체 범위·canary/Console·계정·실제 관측. 단순 TIMEOUT을 차단 PASS로 판정하지 않음 |
| H05·R2 | [정책 회신][h-r12]: 추가 유지 사유 기록 없음, 현 소비자 확인 후 10/27 전에 정리 가능 | Harbor 계정·edge01 Secret 실제 정리와 AC06 인수 |
| H05 legacy | [10/1 삭제 기록][legacy-deleted]과 [10/10 정정][j-correction]. GWONUK의 [재대조][review]에서도 archived=true, Actions secret/Environment/Variables/Dependabot secret 각0 | 해당 저장소만 직접 재확인. 조직 단위는403, 전체 비밀값·타 저장소 전수를 이번에 확인한 것은 아님. 과거 로그/CI에 따른 옛 Robot 사용 연계이지 비밀값 바이트 대조가 아님 |
| J03 | [후속 회신][j-correction]: 10/11(일)19:00 이후 가능. db01 콘솔 server08+sudo와 base64 전달 제안 | U01과 정확한 비중첩 창, 실제 수신. 30분은 담당자의 예상. 일정 확정/전달/Restore 성공 아님 |

## 담당자 보충 요청 — 답변은 U01~U03만

### U01 — db01 콘솔 전달 방법의 실현성

- 연결/응답자: J03·DR #21, 이재환(@supreme33-kr).
- 빈 값: 제안한 PC→db01 콘솔 붙여넣기가 실제 가능한지에 대한 확인 여부. db01 콘솔·server08+sudo를 사용한다는 회신은 이미 수신했다.
- 요청: `확인한 환경·시점·허용/가능 여부` 또는 `아직 확인하지 않음`을 답한다. 불가한 경우 이미 허용된 다른 전달 경로를 알고 있으면 참조만 연결한다. 아직 사용할 경로가 없으면 필요한 조건을 남긴다.
- 제출 범위: 공개 검토본에는 가능 여부와 방법의 식별만 남긴다. dump 원문/base64·접근 비밀값은 올리지 않는다. 이번 요청으로 clipboard·HGFS·방화벽·접근권한을 새로 변경하지 않는다. 과거 Harbor clone의 붙여넣기 제약을 db01의 현재 사실로 자동 적용하지도 않는다.
- **인계 답변 완료조건:** 확인된 전달 방법과 근거, 또는 명시된 미확인/불가 및 필요한 조건이 기록됨. `모름`은 유효한 답변이지만 실행 준비 완료는 아니다.
- **실제 실행 전 조건:** 이권욱이 경로 실현성·정확한 시작 시각·db01 비중첩·수신 준비를 확인한다. 담당자의 가능 시간은 10/11 19:00 이후라는 후보이며 확정 작업창이 아니다.
- **전달 완료조건:** 기존 원본 `fdsdb_backup_20260903.dump` 5,206B, SHA256 `80962dcd41c8afe3920c7194e8b5e2a4531ee901b4027aad1d47209ed4a46f3d`와 수신본 일치, `/var/lib/pgsql/fds-evidence/`·postgres:postgres·디렉터리0700/파일0600·시각 readback 및 이권욱 수신 확인. 수신 확인 전 PC 원본 보존, 이후 삭제도 별도 처리한다. 해시/권한 실패 시 인수 완료로 올리지 않고 원본을 보존한다.
- 대기 범위: 해당 dump 전달·DR 원본 인수. 다른 개발·기존 Restore 증적 대조는 계속한다.

### U02 — 조직 Secret의 기존 확인 경로와 한계

- 연결/응답자: H05·R2·HBR AC06. 이하영(@hayeounglee)·이재환(@supreme33-kr)은 알고 있는 기존 관리자/정상 확인 경로를 연결한다. 실제 API/UI 확인자는 그 권한을 가진 사람이며, 이 문서에서 임의 지정하지 않는다.
- 빈 값: 조직 단위 Actions Secret의 관련 제공 범위·소비 참조. 10/1 원 기록과 10/10 두 조회 모두 권한 부족으로 미확인이다. 저장소/조직 역할과 현재 사용 중인 토큰의 유효 권한을 구별한다.
- 요청: 기존 권한으로 확인 가능한 담당자·경로가 있는지, 현재 확인 가능/불가와 이유를 답한다. 이미 확인했다면 옛 Robot/HARBOR 및 관련 저장소에 제공되는 조직 Secret의 메타데이터·visibility/선택 저장소·참조 대조 범위와 시점만 제시한다. 이름에 HARBOR가 없다는 이유만으로 모든 credential 소비자 부재를 판정하지 않는다.
- 제출 범위: 값·Token·개인키는 제출하지 않는다. 새 admin:org 권한 부여·토큰 scope 확대·조직 전체 credential 회전/삭제·Phase 2 감사는 요청하지 않는다.
- **인계 답변 완료조건:** 실제 확인 주체/범위·시각·관련 항목 존재 여부 또는 조회 불가의 한계/접근 경로가 명시됨. HTTP403을 `0건`으로 기록하지 않음.
- **정리 판단 전 조건:** 이권욱이 확인된 범위와 남은 한계를 소비자/원복 영향에 연결한다. 미확인 상태가 기술적으로 해소되지 않았다면 인계 답변 완료와 별개로 남기고, 예외·위험수용은 자동 생성하지 않는다.
- 대기 범위: 조직 범위를 포함한 credential 정리의 영향 판단. Token 코드 정합화·installer 개발의 공통 대기가 아니다.

### U03 — Harbor 삭제 수행자의 실제 관리 접근

- 연결/응답자: H05·R2, 이재환(@supreme33-kr). [회신][j-correction]의 Harbor `robot$fds-ci` 삭제 수행 의사는 수신했다.
- 빈 값: 현재 승인된 Harbor 관리 접근을 실제 사용할 수 있는지와 가능 작업 범위. 계정 생성 이력·GitHub 저장소 admin 권한으로 Harbor 권한을 추정하지 않는다.
- 요청: 사용 가능한 기존 관리 경로의 식별·확인 시점·가능 범위, 또는 접근 미확인/불가와 필요한 연결 주체를 알려준다. 실제 비밀번호/Token을 전달하거나 지금 로그인·삭제를 새로 실행했다는 결과를 요구하지 않는다.
- **인계 답변 완료조건:** 수행 의사와 별도로 접근 가능 사실 또는 미확인 조건이 식별됨. 실제 실행 직전 접근 확인은 별도다.
- **실행 전 조건:** 이권욱이 pull/push 로그의 보존 범위·실제 Secret/설정 참조·소비자·원본 보존·오판 시 대응·비중첩을 확인해 회차를 구체화한다. 로그0건은 휴면 소비자 부재의 단독 증거가 아니며, push 이력만으로 pull을 판단하지 않는다.
- 대기 범위: Harbor 계정의 실제 변경만. archived 저장소의 중복 삭제를 요청하지 않는다. edge01 Secret 처리는 이권욱이 준비하며, 중지된 k3s를 이 문서만으로 다시 켜지 않는다.

## 책임과 승인 조건의 정합성

후속 회신의 `HBR Lead 확인`을 새 필수 GO로 채택하지 않는다. [#30][delegation]에 따라 이번 Phase 1 잔여의 실행·검증·결과 수용·종결 판단은 이권욱에게 이관됐다. 원 담당자의 사실 제공·기술 지원·기존 정책상 독립 코드/증적 리뷰를 유지한다.

이재환이 Harbor 삭제를 수행하겠다는 회신은 실제 접근과 회차를 확인할 **작업 분담**이다. 인수 권한을 반환하거나 Issue Assignee를 변경한 것이 아니다. U03의 답변이나 이 PR의 승인을 실제 삭제 명령으로 취급하지 않는다. 담당자에게 이미 합의한 이관 자체의 재승인을 요청하지 않는다.

## 담당자 재질문과 구분할 이권욱 직접 잔여

| 묶음 | 아직 남은 것 | 진행 가능한 준비 |
|---|---|---|
| C01 원본 접근통제 | 실제 공유 관리자·SMB 권한/허용 계정·그룹과 보관자 접근 확인. NTFS 넓은 ACL만으로 외부 공개를 단정하지 않음 | 기존 사본 분석·관리자 확인 경로 준비. 새 민감 원본 추가 전송과 접근통제 완료 판정은 별도 |
| H02 K8S | 복귀 metadata 선택·실제 호출자 배제·현장 backup/restore, AC4·T14/T15 및 처분7건 | 수신 목표값과 원본 diff·복귀 설계. 17파일 성공을 #10 전체 완료로 확대하지 않음 |
| H03 Delivery·SEC | 900초 코드/시험 정합화, 실제 SA/CA/정책 참조·비상 principal/사본, 남은 AC 행 | 기존 표본 재사용·코드/최소 Matrix 준비. 현재 회수 미수행과 SA 단위 무효화 가능성 구분 |
| H04·J05·J07 | 귀속 기준과 기존 AC 대응, canary·Console·관측 접근, OID-02 공급/OID-03 경로, ICR reboot·현행 HA 영향 평가 | 기존 증적/형상 비교·회차 설계. 실제 AC 변경은 Decision/CR로 분리 |
| H05 운영 | 실제 Robot 소비/보관·권한/유효성, worker 10/16·push10/18 만료 전 대응 필요성, trust 참조·fresh scan/DB 시각, .50/.102·IPv6 INPUT | 읽기 확인안·회전/정리 영향과 실패 대응 준비. 만료 시각은 10/8 UI 기반 회신이므로 실행 전 최신값 확인 |
| H06 복구 | fresh UUID/격리·Python/SELinux·대상 ID/Compose/Engine/StopSignal·예산·원 정책/복구점·private 원문 보존 | 기존 PR32~40을 재사용한 installer·H6/늦은 stop·세대 변경 실패 처리 개발·모의검증 |
| H07·J08 운영 인수 | 실제 제3자 재현·Runner 두 번째 운영자 참여 미정 | 이권욱이 대상·시간·정상 접근이 있는 회차를 먼저 제시한 뒤 참여 확인. 문서 리뷰를 재현 실적으로 집계하지 않음 |
| J04·J06·S04 등 | Grafana 관리 사본/회수 한계, 과거 공백·FUP 처분, Ansible 기존 운영 잔여 | [수신 현황표](INTAKE_STATUS.md)의 각 제한/완료조건 유지. 이미 모른다고 답한 자료 전수 재요청 없음 |

위 표는 새 팀 정책·새 전수 시험 목록이 아니다. 이미 인수한 잔여의 확인 주체를 분리한 것이며 원본 부재를 새 시험으로 소급 보충하지 않는다. 이 PR만으로 일정·AC·위험수용·Runtime 값을 확정하지 않는다.

## 회신과 검토 완료 기준

이하영은 H 사실 반영·R1 정책값·U02 연결·이관 경계, 이재환은 J03/H05 정정·U01/U03·본인이 아는 U02 연결을 검토한다. 문서 정확성 리뷰와 실제 답변 상태를 따로 기록한다. 같은 원본·정책 회신을 다시 제출하지 않는다.

```text
검토 HEAD / 입력 ID(U01~U03):
답변 상태: 확인됨 / 미확인 / 현재 불가 / 해당 없음
확인한 사실·범위·시각 / 근거 링크 또는 기존 비공개 참조:
남은 조건 / 실제 확인 가능한 담당 또는 미정:
즉시 답하기 어렵다면 회신 가능 시점 또는 그 시점을 정할 조건:
```

`확인됨`은 해당 질문 범위만 충족한다. `미확인/불가`도 책임·제약의 인계 답변으로 기록하지만 소비 작업을 자동 허용하지 않는다. 회신은 이 PR 댓글로 받고 [INTAKE_STATUS](INTAKE_STATUS.md)에 정확한 링크·버전·해소/미해소를 반영한다. 모든 답변의 동시 완료나 새 Lead GO를 전체 개발의 선행조건으로 추가하지 않는다.

기존 검토는 [PR160 후속 검토][review]에 있으며, 이번 문서 자체의 리뷰·CI는 새 PR의 정확 HEAD로 확인한다. 실제 전달·삭제·발급·설치·AC 인수는 아직 이 문서로 실행하지 않았다.

[pr160]: https://github.com/321Team/fds-project-baseline/pull/160
[delegation]: https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6082618226
[custody]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6083078172
[h-reply]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6083293377
[h-r12]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6084886811
[j-correction]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6084948949
[legacy-deleted]: https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5924842213
[review]: https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6086529018
[sec-pod]: https://github.com/321Team/fds-project-evidence/blob/6014e9a961af497e78be9c383d270291013db5cf/evidence/P1-SEC-01/network-gaps-20261008/README.md
[sec-host]: https://github.com/321Team/fds-project-evidence/blob/6014e9a961af497e78be9c383d270291013db5cf/evidence/P1-SEC-01/hostnetwork-20261008/README.md
