# 4. Ansible 운영 진입점 전환 준비 증분

CODEX_ASSISTED. 책임: [infra-ansible#9](https://github.com/321Team/infra-ansible/issues/9), 이권욱.
기존 Ansible-Engine-Transition-Preparation/Explicit-Engine-Selection 및 PR74 DNS 실행안을 재사용한다.
이번에 역할·운영 호출 경로를 실제 전환하지 않았다.

## 확인된 출발점

[운영 진입점 증적](https://github.com/321Team/infra-ansible/issues/9#issuecomment-6042409863):
ansible01/server01_ansible, /home/server01_ansible/p1-ans-01 HEAD e1c4458cf95dacca76870d7b9b012f8615f6974a,
기본 /usr/bin/ansible core2.16.19, cfg/wrapper5개 hash 일치, 엔진 선택 helper 없음.
후보의 CLI/MON 성공은 별도 checkout 결과다. 옛 checkout에 opt-in 변수만 주면 후보가 선택된다고 가정하지 않는다.
이 값들은 당시 실측이며 실제 전환 직전에는 drift를 다시 확인한다.

## 단계별 처리와 고정할 입력

| 순서 | 준비/실행 위치 | 완료조건·STOP |
|---|---|---|
| 1 | 이권욱: 최종 리뷰 source의 별도 checkout 경로와 2.21.3 venv/bin 실제 절대 경로 고정 | source/clean/hash/4 CLI version/config/inventory/vars/key 참조 일치. 미확정 경로는 임의 생성하지 않음 |
| 2 | ansible01에서 PR74 verify-worker02 한 회차 | worker02 .107/svc_ansible 단독 guard, changed0/failed0/unreachable0 및 DNS assertion. 120초 timeout; 오류 시 중단 |
| 3 | 위 DNS 원본과 기존 CLI/MON/SSH 비교 결과 연결 | 각 scope·source·엔진 구분. unit/구문 PASS를 role apply/rollback으로 확대 금지 |
| 4 | 기존 #9 계획의 canary role·대상·복구 범위를 Lead가 고정 | apply→실제 재적용→fresh SSH→role rollback을 검증할 새 창. worker02 verify를 canary apply 승인으로 사용하지 않음 |
| 5 | 수동·예약·Runner 진입점별 단계적 전환 | 호출별 source/config/engine realpath 기록. 누락 manager·동적 호출은 잔여로 유지 |
| 6 | 전환 후 역할·호출 경로별 증적과 복구 성공 대조 | 모두 확인된 범위만 전환 완료. 시스템 RPM/전역 PATH를 일괄 변경하지 않음 |

PR74 worker02 실행은 [고정 실행안](https://github.com/321Team/infra-ansible/blob/d8d99efaf2537c74fb8f412fef65b351af08f67a/docs/runbooks/Issue9-Worker02-DNS-Verify.md)을 소비한다.
FDS_ANSIBLE_ENGINE_DIR/FDS_ANSIBLE_ENGINE_VERSION=2.21.3, ANSIBLE_CONFIG, ANSIBLE_PRIVATE_KEY_FILE,
CR_EVIDENCE_DIR는 그 실행안의 실제 검토 경로로 고정한다. 전체 verify나 직접 playbook --limit로 대체하지 않는다.
기존 core2.16.19 및 운영 checkout은 해당 한 회차 동안 그대로 유지한다.

## 원복을 두 종류로 구분

- 엔진/호출 경로: 변경했던 진입점만 기존의 확인된 source·config·절대 엔진 경로로 복귀하고 버전 재확인.
- 대상 설정: 엔진 복귀는 DNS/SSH/MON/NTP 설정 복원이 아니다. 실제 변경한 role의 검토된 rollback과 백업을 사용.
- 실패/접속 손실/예상 변경이면 확대 중단, 원 로그·rc·hash·대상 상태 보존. 키 복원이나 보안 완화는 자동 조치하지 않음.

이번 완료는 경로·순서·검증·원복안의 증분 정리다. 운영 checkout 갱신, venv 설치, worker 접근,
DNS verify/apply, 엔진 전환은 모두 NOT_RUN. PR74와 evidence154의 리뷰 대기를 유지한다.
