# v3.1.21 Architecture authority view

D21 transport decision FINAL. Complete Architecture Freeze HOLD.

 이번 버전의 권위와 변경

현재 계획/담당/상태는 아래 78개 Record와 Ticket Pack이 기준이다. 승인된 기술 요구는 이전 v3.1.20에서 상속하며, 최신 정식 Decision/CR과 본 절의 명시적 정정이 충돌 항목에 우선한다. 과거 완료·날짜·후보 표기는 역사이며 현재 상태로 재사용하지 않는다.

- D21 FINAL: OCI Primary NO-GO(project suitability), AWS EC2+EIP self-managed Libreswan relay 선택. Region ap-northeast-2, VPC10.20/16, Relay10.20.110.10/subnet10.20.110/24, AZ2a/apne2-az1, t3.medium, encrypted gp3 40GiB, EIP1, public SSH DENY/SSM. 정확 AMI/route/security frozen input은 #36과 Architecture source snapshot 참조. 신규 sizing/NAT/source 모델 권장안은 미승인.
- P1 Close HOLD. #15 local endpoint 보장, #16 Delivery Runtime, #19 rollback 잔여를 보존한다. 10/6 심사 결과는 아직 없다.
- #119 Done: DB 장애는 API /readyz503·Endpoint 제외, engine 장애는 API Ready·HTTP201·skipped=true·DB 저장. ROSA에서 별도 검증.
- #125 Done: backup/rollback은 P1 필수, 예방 rotation은 NOT MET/RISK ACCEPTED. Receiver 없는 P2 이관 완료 금지. #126/#127/#128은 no-change 이력.
- #130 Done: OID02 결정은 #14가 추적하며 HBR 입력 제공은 유지. #16이 동일 Review Run 4/4·rollback을 생산하고 #13이 05B를 인수한다. HBR 종결 Gate를 제거하지 않는다.
- #110 Done: Wolfi/apko 공급망 Decision 승인. 구현 Source 병합과 Delivery Runtime을 구분한다.
- #74/#75/#109 등 완료 결정·변경은 최신 Record/원문으로 동기화하며 관련 Runtime·다른 Gate를 자동 Done으로 바꾸지 않는다.


Candidate specification source: https://github.com/321Team/fds-project-architecture/blob/c421733e702c8923e26f6788fd8ade5e8657badf/phase2/reviews/20261003-resource-fit-recommended-design.md

Diagram is the selected transport/acceptance boundary, not created resource evidence.
