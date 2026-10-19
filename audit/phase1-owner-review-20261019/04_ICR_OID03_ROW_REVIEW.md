# ICR·OID03 — 참조등록과 원 AC18/19 행별 판단 입력
대상: **이권욱(ICR Lead),이하영/이권욱(OID03 기존 기술 책임)**. baseline main `acc513cf5c9f3e07e58d818a18e4b8fcf1e0cf70`의 [원 ICR Description](https://github.com/321Team/fds-project-baseline/blob/acc513cf5c9f3e07e58d818a18e4b8fcf1e0cf70/tickets/v3.1.21/descriptions/ICR-D-NET-01-01.md)과 정본979facb9의 원 AC 유지. **Owner 최종 회신·전체 인수 미작성**.

## OID03 — 자료 참조등록 완료,전체 계약 채택 별도
10/19 **12:33:46 중앙 참조등록** 완료. [07:09 공유 보존](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6255792476)의 exact13RPM(primary9+worker02 provider4,129,242,114B)·공개키3·검증기록4: 원본20개+README/CATALOG2개 manifest22행(SHA0107c96f…a74376)과 source index를 현재 기술 참조로 등록했다. 미보유·미보존으로 되돌리지 않는다.
[worker02 native](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6248973398)의 containerd.io2.4.1-2.el10 단1종 parser/signature/설치 없는 transaction rc0 재사용. --test/--noscripts/--notriggers/--noplugins와 당시 설치 provider4종 가정 유지. provider 동시 재설치·새 key import 승인 아님.
남은 것은 **전체 OID03 공급·갱신·실제 복구 계약의 선택/인수**다. 신규 OS 전이 의존물 closure·실제 reinstall/서비스·데이터 복구 미입증,config/unit hash는 backup 아님. source/path/NEVRA/SHA 참조를 고정하고 실제 변경 회차에서만 차이별 입력·보호 backup·영향·유한 복귀 조건을 연결한다. 개별 수령/현재 ACL·서버 전달물 처분은 이번 미확인이다. 새 날짜·영구 egress·무기한 위험수용·전 노드 재설치를 조건으로 만들지 않는다.

## 원 AC18/19 — 자료 공백 해소와 최종 판정을 분리
AC18=**Reboot 후 정책 유지·재시험**,AC19=**Rollback 재현**. 기존 APP20행 대응·유효 처분 재사용.

| 행 | 현재 입력 / 남은 정확 판단 |
|---|---|
| 18-KCP/KW·EARLY | 기존 부팅 steady-state·CP3/Worker3 각각의 한정 수용 유지. EARLY NOT_MET/직접 미측정 보존. 같은 재부팅·정상시험·위험수용 재승인 제외 |
| 18-IF16-W/EDGE/HARBOR | [6257007655](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6257007655)의 Worker3·edge·Harbor 부팅 후 source/route·저장 구성 자료공백 해소. AC18에 소비할 한정 범위 판단 |
| 18-IF16-DB | [09:44 콘솔6257268951](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6257268951)의 ens192 활성UUID·저장/kernel/.30 route-get source55 일치. 콘솔 완료표시를 shell rc0으로 만들지 않음. 자료 재조회 불필요 |
| 18-NODEPORT | [현재 spread/HTTP6258431234](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-6258431234)로 Worker별 endpoint·NodePort3/진입점 HTTP200 전제 해소. AC18 양성 회귀 소비 범위 판단. D02 사람 수행·실거래/전체 E2E 대체 아님 |
| 18-IF06B-GW | 09:41/43 같은boot 구성·사용자12:30:58 신원 결속 재사용. 새 PR247의12:38:49~54 Worker03 공개CA 결속 후 source108 지정·목적지.30:443 관리 Harbor GET은 **curl28/HTTP000·연결0/timeout**. 실제 socket IP 빈 값·연결/TLS 미성립: ssl_verify_result0≠TLS PASS. GW 통과/특정 DROP 위치·정상 flow 미입증. 기존207 성공은 유지하고 이 결과·postboot flow 잔여 처분 판단 |
| 19-CP1/W01/CP02/K8S4/TOOLS | CP1 canary·W01 한정복구·CP02 회복 관측(최초OFF FAIL 보존),K8S4·도구 실제호출 미검증의 [기존6205182638](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6205182638) 재사용. 복구PASS 합산·새4대시험/도구호출 요구 없음 |
| 19-IF06B-GW/TEMP·IF16-ROUTE | 기존 정확 gateway 정책복구·207 임시물 회수 완료,새 route 변경이 없던 범위 N/A 재사용. 전체 서비스/정책 복구로 확대하지 않음 |
| 19-EDGE-PROFILE | 비활성UUID6b9f0643-4a4e-324d-a969-9e5393d7e0bf autoconnect=no 확인. 실제 no→yes 복귀 미시험은 별도 잔여. 현재no 유지·주소/역할 확인 후 실제 재사용 때 복귀 절차 검토라는 **한정 처분 후보**를 Owner가 판단. 잘못된 주소 재활성화 시험·자동 위험수용 없음 |
| 19-OTHER-OWNERS | APP/DB/Harbor 기존 인수·OID03 참조등록을 자기 범위로 소비. 전체 RPM/데이터 복구 시험을 ICR의 새 AC로 추가하지 않음 |

새 실제 증적: [PR247](https://github.com/321Team/fds-project-evidence/pull/247), 정확 HEAD `46cc46da43ad1206821f3fa8a4d0807ee2913625`. ICR 수집회차17파일(원본 사본14개+생성 기록3개)은 worker03 공개CA/단회GET 결과이며 normal flow 성공 증적이 아니다. 원본 사본14개는 당시 APP binding11개·FINAL_BINDING1개·사용자 콘솔2개, 생성 기록3개는 COPY_MAP·README·SHA256SUMS다. 상세 보존 경로는 해당 PR README·COPY_MAP을 따른다. 추가 GW 접속·GET 재시도·정책 변경을 배정하지 않는다.

## Owner 회신 빈양식 — 현재 미작성
- 검토자 / KST 시각 / 판단 입력·버전: ______
- OID03 참조등록을 넘는 전체 계약 채택 범위·미선택/미충족·근거: ______
- AC18 행별 판정·기존 근거 소비 범위 / GW postboot flow 정확 처분: ______
- AC19 기존 처분 유지 / Edge profile 실제 복귀 미시험 한정 처분 여부·조건: ______
- 원 AC 최종 인수·한계 / 추가 조치가 필요한 정확 원 요구: ______

원 AC·기존 승인·책임·기한·Status/종결을 DOC가 대신 바꾸지 않는다.

