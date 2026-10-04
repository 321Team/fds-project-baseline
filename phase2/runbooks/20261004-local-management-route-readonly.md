# Runner 관리 경로 local read-only 수집
2026-10-04 / CODEX_ASSISTED. #34 B1·#37·#40 기존 입력 요청을 위한 실행 보조.
작성 시점의 STATIC/MOCK과 후속 현장 관측을 구분한다. 2026-10-04 Runner/vpn-gw 로컬 수집 및 원본 SHA 대조 완료. 상세는 [DNS 계약 §11~14](../reviews/20261004-private-management-bidirectional-dns-contract.md)를 따른다. 동일 상태의 재수집은 불필요하며 route 변경·Freeze/Decision 승인 또는 네트워크 인수는 아니다.

## 실행 경계
- 대상: cicd-runner01의 기존 server01_cicd-runner 계정, vpn-gw01의 기존 담당자 승인 계정.
- 각 서버에서 로컬 실행한다. 자동 SSH나 다른 호스트 접속은 없다. sudo·새 권한 불필요.
- Bash, Python3, iproute, timeout, mktemp, sha256sum 필요.
- 주소 guard: runner=10.250.10.20 / vpn-gw=10.1.93.51이 실제 로컬 IPv4에 없으면 결과 디렉터리 생성 전 STOP. hostname만으로 대상 판정하지 않는다.
- 주소가 변경됐다면 guard를 임의 해제하지 말고 변경 근거를 확인한다.
- 수집은 로컬 주소·rule·전체 IPv4 route table·resolver 설정·ip_forward·route lookup만. ip route get은 이 수집에서 실제 통신 시험으로 취급하지 않는다.
- cloud10.20.110.10은 기존 Relay 설계 목적지에 대한 로컬 route lookup일 뿐 실제 자원 존재·도달성 검증이 아니다.
- Secret/TSIG/VPN key/config/authfile/env 전체를 수집하지 않는다. resolver와 route에 내부 metadata가 포함되므로 private 자료로 다룬다.

## 순서
1. 이 PR의 검증한 동일 commit에서 [수집기](collect-local-management-route.sh)를 내려받아 기존 WinSCP 등 승인된 전달 경로로 각 사용자 홈에 저장한다. 다운받은 파일과 PR 코멘트의 SHA256을 대조한다.
2. 우선 Runner에서 실행하고 결과를 검토한다. vpn-gw는 기존 담당자의 접근 권한으로만 실행한다.

Runner:
```bash
if bash "$HOME/collect-local-management-route.sh" runner; then
  printf 'LOCAL_ROUTE_CAPTURE_RC=0\n'
else
  p2_route_rc=$?
  printf 'LOCAL_ROUTE_CAPTURE_RC=%s\n' "$p2_route_rc"
fi
```

vpn-gw01:
```bash
if bash "$HOME/collect-local-management-route.sh" vpn-gw; then
  printf 'LOCAL_ROUTE_CAPTURE_RC=0\n'
else
  p2_route_rc=$?
  printf 'LOCAL_ROUTE_CAPTURE_RC=%s\n' "$p2_route_rc"
fi
```

부모 shell 옵션을 바꾸거나 터미널을 종료하지 않는다. wrapper의 마지막 printf 상태가 아니라 출력된 LOCAL_ROUTE_CAPTURE_RC를 판정에 사용한다.
3. RESULT_DIR 아래 local-route.txt와 SHA256SUMS를 private 경로로 전달한다. 파일에는 source script hash·UTC/KST·계정·host·각 명령/RC가 기록된다.
4. 후속 콘솔에서 .58과10.250.10.1은 mgmt-gw01의 ens160/ens224로 확인했다. mgmt-gw는 vpn-gw01(.51)과 별도다. 본 수집기의 runner/vpn-gw 주소 guard를 변경해 mgmt-gw에 실행하지 않는다. 해당 장비의 기존 주소·규칙 관측은 DNS 계약 §13~14에 연결돼 있다.

## 판정·중단·복구
- RC0 / CAPTURED_REVIEW_REQUIRED: 고정 로컬 조회가 모두 RC0. L3 연결·방화벽 허용·VPN SA·DNS 응답 성공은 아님.
- RC1 / PARTIAL_REVIEW_REQUIRED: 하나 이상의 조회 실패/timeout. 성공 출력과 실패 명령/RC를 보존; 경로가 없다는 사실도 입력이다.
- RC2: 역할/필수도구/주소 guard 또는 결과 기록 선행 실패. 대상·도구부터 확인하고 권한을 확대하지 않는다.
- 각 명령 timeout10초. 0700 새 디렉터리·0600 결과이며 기존 파일을 덮어쓰지 않는다.
- remote 변경이 없으므로 rollback 없음. 실패 파일은 원인 확인 전 삭제/성공으로 재작성하지 않는다.
- source가 예상과 다르거나 unexpected default route면 그대로 STOP/검토. route add/selector 확대/SNAT/방화벽 해제/재시작 금지.
- 자료 수신 후 source/next-hop/return 양측 대응을 검토한다. 실제 forwarding/source보존 시험은 별도 범위로 구분한다.

## 작성 당시 준비 검증 (후속 현장 수신과 구분)
- bash -n PASS; 잘못된 role 입력 RC2.
- fake ip command를 사용한 MOCK5/5: Runner 정상, vpn-gw 정상, 주소 mismatch, route lookup 실패, 주소 JSON 오류.
- 정상/부분 수집은 결과 권한0700/0600 및 SHA256SUMS 확인. 실패 guard는 결과 디렉터리0.
- 실제 target host 접근·네트워크 probe·sudo 없음. 로컬 모의 출력은 Runtime 증적으로 편입하지 않는다.

[DNS 계약](../reviews/20261004-private-management-bidirectional-dns-contract.md) §10의 기존 DNS09-29 원본2개와 함께 소비한다.
