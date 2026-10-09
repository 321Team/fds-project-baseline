# 이하영 인계 요청 — K8S·SEC·Harbor

인계·업무 검토: 이하영(@hayeounglee) / 수신·잔여 통합 수행: 이권욱(@GWONUK)

공통 원칙·회신 양식은 [README](README.md), 소비 작업과 우회 진행은 [EXECUTION](EXECUTION.md)을 따른다. 아래는 기존 담당자가 알고 있거나 보유한 입력의 인계 요청이다. 새로운 서버 수집·정책 변경·시험을 이하영에게 일괄 재수행하도록 요청하지 않는다. 기존 자료가 이미 있으면 해당 근거를 재사용하고 빈 부분만 회신한다.

## 우선순위

1. Delivery를 막는 H05의 Registry 인증·정책 입력과 H03의 해당 SA/Token 경계.
2. H01~H02의 K8S 변경/복원 입력과 H04의 경로 판정 범위.
3. H06~H07의 미기록 현장 제약·인수 역할. 이 순서는 다른 행의 제공을 지연시키라는 뜻이 아니다.

## H01 — K8S 원본·기존 보관본

- 연결: [baseline#10](https://github.com/321Team/fds-project-baseline/issues/10), [evidence#174](https://github.com/321Team/fds-project-evidence/pull/174), [#182](https://github.com/321Team/fds-project-evidence/pull/182), [#195](https://github.com/321Team/fds-project-evidence/pull/195).
- 재사용: 45파일 대조, 변경17/유지28/control02 제외, 17개 원본 PC 사본과 파일·부모 metadata/SELinux/ACL. 기존 비공개 archive와 Manifest를 새로 만들지 않는다.
- 제공할 미확인 부분: 실제 보관 위치·접근 주체, 원본/Manifest와 승인 대상 파일 목록의 연결, 새 버전/누락 여부, #195의 지정 인수자 수령 여부. 이미 이권욱 보관본이 같은 바이트로 확인되면 재전송 없이 그 기록으로 답한다.
- 완료: 이권욱이 해당 archive 접근·목록·크기·해시와 수집 범위를 대조하고 보관 책임/기간을 기록. 개인정보·민감 원문을 Git에 넣지 않는다.
- 소비: K8S 현장 backup/교체/restore 준비. PC 사본을 실서버 backup·복원 성공으로 사용하지 않는다.
- 미제공 시: K8S 쓰기만 대기. 기존 Manifest 분석, 원본 보존, 비의존 작업 진행.

## H02 — 기대 형상·라벨·복귀값·호출 배제

- 연결: [K8S PR78](https://github.com/321Team/infra-kubernetes/pull/78), baseline#10의 형상/복구 잔여.
- 제공: 대상17개별 승인 소스/설치 경로·소유자/모드·기대 SELinux label·ACL/xattr 처리와 근거, 교체 실패 시 되돌릴 원본/metadata, 현재 호출자·timer/job/동시 작성자에 대해 알고 있는 사실. 후보와 승인값을 구분한다.
- 관측된 worker01의 `user_home_t` 및 다른 파일의 `usr_t`는 관측값이다. 기대값으로 자동 채택하거나 재라벨 명령을 이번 문서에 추가하지 않는다.
- 현장 fresh backup·실제 restore·동시 호출 배제 검증의 준비/수행은 이권욱이 담당한다. 원 담당자는 이미 확보한 사실과 미확정 영역을 넘긴다.
- 완료: 실제 적용할 대상/기대값/복귀값의 근거와 미확정점이 행별로 식별되고, 이권욱이 해당 회차 입력·중단/복구안을 확정할 수 있음. 미확정값을 임의 기본값으로 채우지 않는다.
- 미제공 시: 교체/relabel 중단. 파일 diff·복구 설계·다른 영역 준비 진행. 폐기된 CR128을 대표1대 축소 승인으로 쓰지 않는다.

## H03 — SEC 잔여 Matrix·실제 자격증명 소비 경계

- 연결: [baseline#19](https://github.com/321Team/fds-project-baseline/issues/19), [#14](https://github.com/321Team/fds-project-baseline/issues/14), [#16](https://github.com/321Team/fds-project-baseline/issues/16), [CR125](https://github.com/321Team/fds-project-baseline/issues/125).
- 재사용: AC01/03 기존 인수, IF12B/방식B #144, IF03/IF13A/IF05C #157, Edge #169, 격리 restore #152, Probe #173/#177. 기존 수신분의 재제출은 불필요하다.
- 제공: 미입증 AC02/04/05/06의 정확한 행·Source/Destination/포트·보호 주체·적용 manifest/실측 근거·제한, 기존 유효한 위험수용. 성공 관측과 특정 정책의 차단 귀속을 분리한다.
- Delivery 관련 우선 입력: 현재 SA/Role/TokenRequest의 승인 범위·발급/만료/갱신/회수 경로·CA 참조·허용 대상. Secret/Token 값은 제출하지 않는다. 기존 can-i Matrix 인수와 실제 자격증명 소비의 잔여를 구분한다.
- 완료: 필요한 최소 시험 행과 기존 성공/미측정/위험수용 경계가 연결됨. 이권욱이 새 실행 결과를 기존 AC에 대응할 수 있음.
- 미제공 시: 해당 보안 변경·자격증명 소비만 대기. 기존 증적/소스 비교·음성 시험안 작성 진행. 새 rotation·전수 장애주입을 필수로 추가하지 않는다.

## H04 — ICR/IF06B·OID-02의 판정 입력

- 연결: [MON 잔여 정정](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6072071555), [baseline#14](https://github.com/321Team/fds-project-baseline/issues/14), [CR130](https://github.com/321Team/fds-project-baseline/issues/130).
- 재사용: Source/401 증적122, gateway 원본151. 기존 성공을 전부 미실행으로 되돌리지 않는다.
- 제공: 8443 귀속에 적용할 현행 AC/유효 결정, gateway 구간과 특정 rule 중 요구 수준의 근거, 과거 monitor SYN 도착 기준과 gateway 선차단의 충돌, 원 정책/복구/임시 canary 한계. OID-02의 해당 P1 결정·수신 주체와 이미 이관된 범위를 연결한다.
- 역할: 이하영은 알고 있는 승인 기준·정책 사실을 전달하고, 이권욱이 기존 AC 안에서 필요한 회차/판정을 정리한다. 동일 실행의 새 Lead GO를 별도로 요구하지 않는다. 실제 AC 변경은 Decision/CR로 구분한다.
- 완료: J05의 관측 지점·접근 정보와 결합해 최소 관측안·복구안을 만들 수 있음.
- 미제공 시: attribution 의존 시험/정책 변경만 대기. 기존 raw 분석 지속. 과거 handle606은 현재 값으로 쓰지 않으며 없는 counter를 전후 비교할 수 있다고 가정하지 않는다.

## H05 — P1 Harbor Robot·TLS·scan·임시 예외

- 연결: [baseline#13 AC04~06](https://github.com/321Team/fds-project-baseline/issues/13), [evidence#34](https://github.com/321Team/fds-project-evidence/issues/34), [#165](https://github.com/321Team/fds-project-evidence/pull/165).
- 제공: 운영 Registry/프로젝트, Robot의 승인 권한·유효기간/30일 회전 근거·현재 보관 주체·공개 fingerprint/비공개 credential 참조, 옛 계정의 실제 삭제/재발급 또는 유효 처분 증거. 계정 이름만으로 권한과 회수 완료를 추정하지 않는다.
- 제공: TLS chain/SAN/신뢰 bundle의 현행 참조, scan raw report 식별·대상 digest·시각·최신성 기준, 임시 .50/.102 및 IPv6/INPUT 운영 경계의 유효 결정과 잔여.
- 완료: 이권욱이 사용 시점 검증을 수행할 정상 접근 경로와 승인 입력을 확보. 계정 생성·교체·삭제가 필요한 경우 정확한 행위·영향·복구 범위를 별도로 기록한다.
- 소비: P1 Delivery 및 HBR AC04~06. P2 Robot/ROSA allowlist/principal을 새 조건으로 들이지 않는다.
- 미제공 시: credential을 소비하는 Push/Deploy와 해당 HBR 운영 변경만 대기. 비의존 installer/격리 모의검증·문서 작업 진행.

## H06 — Harbor·공유 환경의 미기록 제약

- 연결: [Harbor PR40](https://github.com/321Team/infra-harbor-trivy/pull/40), [수동 복구 증적191](https://github.com/321Team/fds-project-evidence/pull/191).
- 제공: 알고 있는 Console/복구점의 접근 주체, 원 policy/unit/Compose/Engine 승인 자료와 미기록 수동 변경, 다른 회차·작성자와의 충돌 가능성. 이미 이권욱이 확보한 자료는 링크만 재사용한다.
- 이권욱 수행: fresh UUID/격리·Python/SELinux·unit/tool/Compose/Engine·대상 ID·실측 예산 확인, installer와 H6/늦은 stop·세대 변경 복구 경로 준비. 이를 이하영의 신규 구축 업무로 돌리지 않는다.
- 완료: 알려진 제한·원복 기준의 누락 여부가 확인되고, 새 현장 수집이 필요한 부분이 분리됨. 이미 인수된 복구의 구현 GO를 다시 요청하지 않는다.
- 미제공 시: 미확인 복구점을 필요로 하는 위험 회차만 대기. 원 A3 실패·claim·비공개 원문 보존 유지.

## H07 — 독립 검토·재현 참여의 인계

- 연결: [DOC#24](https://github.com/321Team/fds-project-baseline/issues/24), [Runner#61](https://github.com/321Team/infra-ansible/issues/61).
- 제공: 담당 범위에서 검토 가능한 코드/증적, 제3자 핵심 재현 또는 Runner 두 번째 운영자 인수 참여 가능 여부·적격 대체자 제안. 이미 완료된 유효한 제3자 근거가 있으면 먼저 연결한다.
- 현재 미정인 역할을 지정 완료/실습 완료로 쓰지 않는다. 이하영과 이재환 모두가 모든 시험을 수행할 필요는 없다.
- 완료: 필요한 참여 주체와 실제 완료 증거가 연결되거나, 미완료 참여와 영향받는 인수 조건이 식별됨.
- 미제공 시: 코드 작성/모의검증·입력 준비는 계속한다. 해당 독립 리뷰 또는 실제 제3자 인수가 필요한 병합/완료 판정만 대기한다.
