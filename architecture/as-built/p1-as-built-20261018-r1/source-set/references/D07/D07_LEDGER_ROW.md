# D-07 대장 행 — Lead 회신 원문

출처: https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-6211817978 · 2026-10-16 17:52:26 KST · supreme33-kr / 이재환. 아래 행은 원문 보존이며 중앙 대장 채택·외부 반영 결과가 아니다. 의미와 검증 한계는 [최종 인계](FINAL_HANDOFF.md)를 함께 읽는다.

| ID | 내용 | 근거 | 영향 버전/범위 | Severity | 판단 근거 | Owner | Disposition |
|---|---|---|---|---|---|---|---|
| D-07 | 음수 금액 검증 부재 — API `amount: float`·DB `Numeric`·migration에 양수 제약 없음. 음수 transfer 이력이 R07 합계를 낮춰 탐지 회피 가능 | [6206804605](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-6206804605), [fds-msa#38 §2.3](https://github.com/321Team/fds-msa/pull/38) | 두 앱 현 source(`affbc69`=`c9c42cc1` 앱 코드), R07(합계)·R01(건수) | Major | 탐지 회피에 쓰일 수 있는 입력 검증 누락. 거래 저장·가용성 영향 없음. 신규 입력 규약(`amount > 0`) 밖의 입력이 원인 | 이재환 | 규약 문서 반영(#38), P1 코드 무수정, 잔여 위험. 실제 음수 저장·후속 미탐 재현 NOT_RUN. 운영 db01 제약 NOT VERIFIED. 첫 재검토: APP 최종 인수 판정 직전 |
