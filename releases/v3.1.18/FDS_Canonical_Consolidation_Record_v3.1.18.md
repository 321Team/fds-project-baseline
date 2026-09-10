# FDS v3.1.18 누적 변경 통합 기록

> CANDIDATE / 2026-09-10. 현재 RELEASED v3.1.17. 문서 검토이며 실서버 실행·새 승인·merge·Release 발행은 수행하지 않았다.

## 고정 기준

- main / RELEASED v3.1.17: `2d93395a0e19ea67e5be199d7183a7edbaa6cf4c`.
- PR #3 후보: `15bdbac9b646f30c18d17b34fcf403fd12ef675c`.
- PR #68 속성 정책 후보: `573c18877a5b710a04ee50dae59fedf4e3552aea`.
- evidence main: `493c09e728b643d620debe29738f1b47b3cafa8a`.
- 티켓 본문/댓글 수집 기준: 2026-09-10, 각 Issue의 updated_at 및 원문은 `tickets/v3.1.18/source-snapshot.json`에 고정. 같은 날 후속 실행은 별도 변화로 취급한다.

## 반영 대장

| 분류 | 근거 | 반영 | 한계 |
| --- | --- | --- | --- |
| 완료 CR | [infra-ansible PR #1](https://github.com/321Team/infra-ansible/pull/1) | DNS CR Done·승인/merge SHA·AC 11/11·CI NOT RUN | 당시 실행·리뷰에 근거, 이번 Runtime 재시험 아님 |
| 완료 코드·운영 | [PR #4](https://github.com/321Team/infra-ansible/pull/4), [운영 #10](https://github.com/321Team/infra-ansible/issues/10) | SSH 검증식 코드 승인과 운영 6대/SFTP 후속 종결 | 원 P1-ANS Done/일자 유지, 엔진 전환 별도 |
| 완료 코드 | [infra-ansible PR #3](https://github.com/321Team/infra-ansible/pull/3) | Gate 0 도구 병합 | 6대 실제 Gate PASS로 전용 금지 |
| 종결 결정 | [Decision #4](https://github.com/321Team/fds-project-baseline/issues/4), [#5](https://github.com/321Team/fds-project-baseline/issues/5), [#6](https://github.com/321Team/fds-project-baseline/issues/6) | 현행 유지·기능 확대 유예 | 신규 사람 독립 승인/실행 PASS 생성 없음 |
| 현재 실행 | [K8S #10](https://github.com/321Team/fds-project-baseline/issues/10), [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14), [K8S PR #2](https://github.com/321Team/infra-kubernetes/pull/2) | CP1 Ready·단일 etcd·사전 진단 완료, 부분 가입 및 canary 대기 | 110개 조회 PASS는 적용/인수 PASS가 아님 |
| 진행 상태 | [#13 Harbor](https://github.com/321Team/fds-project-baseline/issues/13), [#16 CICD](https://github.com/321Team/fds-project-baseline/issues/16), [#19 Security](https://github.com/321Team/fds-project-baseline/issues/19) | In Progress·현행 책임·Runtime HOLD | 새 Scope 제안은 승인 대기로 구분 |
| 임시 실증 | [#11 DB](https://github.com/321Team/fds-project-baseline/issues/11), [#15 APP](https://github.com/321Team/fds-project-baseline/issues/15), [#17 MON](https://github.com/321Team/fds-project-baseline/issues/17) | k3s/fds 사전 실증과 정본 Runtime 차이 명시 | 저장소 merge는 직접 조회, 실행 성과는 원 보고 범위 |
| 인수·원본 | [evidence #4](https://github.com/321Team/fds-project-evidence/issues/4) | FUP 현재 상태·Stage A 조건부 인수 및 현재 Permanent 편입 | 인수 조건·과거 참조 미확인 유지 |
| 모니터링 교정 | Baseline §11, D33, #17/#25 | #17의 14 AC+2 보조통제, #25의 P1 고도화 복원 | 새 임계값·저장소·노출/권한 도입 없음 |
| 가용일·집계 | PR #3 Team Calendar, 현재 64 Issues | 55개 일정관리 + 종결 이력 9개; 이하영 09-08 가용일 반영 | Start/End 및 Gate 목표일 이동 없음 |
| 동기화 통제 | PR #68·사용자 실행 증적 | Task Type 34·카탈로그 생성 이력, 후속 적용 대기 | 오래된 plan 적용 금지, 최종 동기화 PASS 아님 |

## 교정 근거와 미결정 사항

1. DB의 9/10 진행 댓글은 PR #2 미병합으로 적었으나 실제 GitHub는 9/9 merged=true다. 최신 정본은 병합 사실과 PARTIAL_VERIFIED를 함께 기록한다. 최신 댓글이 항상 모든 필드의 권위 원본은 아니다.
2. Stage A는 단순 인수 미확인이 아니라 조건부 인수다. Permanent Supplement의 독립 편입 완료를 실제 인수 조건 종결로 확대하지 않는다.
3. P1-K8S/ICR의 과거 Calico 설치 전 firewalld OFF 문구는 현행 노드별 보호 전환 리뷰와 충돌한다. 목표 상태는 유지하고 전환 절차의 교정을 후보 리뷰 항목으로 표시했다. 이 변경으로 canary/join 실행 승인 또는 고정 Source 허용을 부여하지 않는다.
4. P1-MON-02의 고도화 범위를 기존 D33으로 복원했지만 가용일은 1일이다. 실제 범위·일정 실행 가능성은 Lead 판단이 필요하며 자동 재기준선화하지 않는다.
5. #59/#61 원본 속성 미확인 2건, Milestone HOLD 20건, #46 End/G5 충돌, DB 시간대/Timestamp 계약 및 OID/NTP 승인 입력은 명시적 잔여다. 문서 정리로 해소했다고 표시하지 않는다.
6. 승인·발행 시점의 최신 Runtime 변화는 별도 cutoff delta로 확인한다. 수집 이후 Issue 기록을 덮어쓰지 않는다.

## 검토·발행 순서

이 통합 후보는 기존 PR #3·#68 변경을 포함해 검토 가능한 전체 묶음으로 제출한다. 기존 두 PR을 이번 작업에서 merge하거나 닫지 않는다. 독립 Reviewer가 통합 후보의 정확한 HEAD와 무결성을 검토한 뒤 이권욱이 명시적으로 병합을 승인해야 한다. CURRENT/RELEASED/Tag는 승인된 finalization 단계에서 확정한다. 발행 후 실제 GitHub Release Asset의 XLSX·ZIP·SHA256SUMS 일치를 확인한다.

발행 전에는 실제 Issue Description·속성 적용을 하지 않는다. 발행 이후 먼저 새 정본의 Description과 최신 운영 이력을 합친 차이를 검토하고 그 결과를 기준으로 metadata map/plan을 새로 만든다. 이번의 `canonical-records.json`은 Description 후보의 원본이며 native apply 계획이 아니다.
