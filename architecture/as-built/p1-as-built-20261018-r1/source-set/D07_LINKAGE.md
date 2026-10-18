# D-07 기존 공식 대장 연결 후보 재사용

2026-10-16 KST · CODEX_ASSISTED · 새 대장 행 작성/공식 등록 없음

[기존 원본 대장 행](../../../defect-d07-reply-linkage-20261016/D07_LEDGER_ROW.md)과 [이 묶음의 보존 사본](references/D07/D07_LEDGER_ROW.md)은 bytes가 같다.

- 전체 `D07_LEDGER_ROW.md` SHA256: `749468df858a8ec511d49f53a2596cf563e39a4bc5cc339ab3bf642ac6dd5957`.
- Lead 8열 행 자체 SHA256: `3f5de9224aea8d7a92108eb4f1d8b4f72ab55296db15fd9318a579dd1847d515` — 기존 결속의 행 단위 hash이며 전체 파일 hash와 다르다.
- Lead 회신 본문 SHA256: `2a3b47629ec36f92258b314545902eeb9ec400c75e1617818a1787689bdfc107`.
- [기존 FINAL_BINDING](references/D07/FINAL_BINDING.json) 파일 SHA256: `b8cf79e39f9649aecd6208a74a6218c358a2cfeb7e0b52194830a2939ee6fa31`.
- 출처: [Lead 회신6211817978](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-6211817978), 2026-10-16 17:52:26 KST. 이번 외부 재조회는 없음.

확정된 ID D-07·Owner 이재환(APP Lead)·APP 최종 인수 직전 첫 재검토는 재질문하거나 새 값으로 바꾸지 않는다. Major·P1 코드 무수정·잔여위험, 실제 음수 저장/후속 미탐 NOT_RUN, 운영 db01 제약 NOT_VERIFIED, I01 분리와 기존 Critical0·Regression/Defect 승인도 유지한다. 첫 재검토는 수정 완료기한·P2 이관·위험수용 만료일이 아니다.

남은 결정은 기존 #20 대장의 [8열 대장 댓글](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-5980751335)과 [관리값 보완](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-5981501458)에 이 후보를 어떻게 채택/연결할지, 그리고 수신 기록을 어디에 둘지다. 과거 본문에 이미 반영됐다고 가정하지 않는다. 현재 외부 상태를 새로 확인하거나 대장·이슈를 수정하지 않았다.

[기존 인계](references/D07/FINAL_HANDOFF.md)의 APP39 OPEN 표기는 그 문서의 17:56 스냅샷 이력이다. 현재 선택한 설명 후보는 APP39 merge93800f09·main CI 영수증을 이미 소비한다. 이는 D-07 행의 재작성·제품 위험 해소나 전체 APP/Phase1 인수를 뜻하지 않는다.
