# #49 증적·산출물 접수 대장

기준: 2026-10-20 23시대 KST. [하영 회신](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6291485599), [재환 회신](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6291988326)을 통합했다.
생산·공유·수신/재해시·내용 검토·증적 편입·AC 인수를 각각 구분한다. 원본 전체 재제출이나 동일 시험 반복은 요구하지 않는다.

| 대상·생산 책임 | 현재 확인 범위 | 편입·인수 상태 / 다음 완료조건 |
|---|---|---|
| D-11d 원본 / 권욱·재환, 편입 하영 | 권욱 공유·재해시·내용 검토, 교차 독립 검토 연결 완료 | [ev249](https://github.com/321Team/fds-project-evidence/pull/249) MERGED `04464931ae70fc4d78fb2601d6cc2c384487b317`. 18파일 편입이며 전체 ROSA AC 완료와 구분 |
| Stage-B VPN / 재환 | 10/15 기존 수용·원본 편입 재사용 | [ev239](https://github.com/321Team/fds-project-evidence/pull/239) 기존 병합. 현재 창 A/B/C 전체 PASS로 확대하지 않음 |
| 창 A / 재환·하영 | T1/T3 PASS, T3-R 성공 보고, T6 INCONCLUSIVE. DB W4·P9/P8·양쪽 V9 원복/정리 보고. 원본3개 비공개 반출·권욱3/3 수신/검토 | 증적 PR 아직 미제출, **재환 담당**. 기존 수신 원본과 중앙 한계 판정을 편입해 Close 전에 연결. 새 시험/중복 반출 요구 없음 |
| G4 후속 / 하영·재환→권욱 | #7 B/A·N3, C7 일부 미실행. [#39 입력](https://github.com/321Team/fds-project-baseline/issues/39#issuecomment-6288503072) | 기존 원 AC의 잔여와 처분 근거 필요. T6를 PASS로 변경하거나 보류만으로 G4 완료 처리하지 않음 |
| PG-03 / 하영 | 6-1 관측 수용, 6-2 NOT_RUN, PG-03 HOLD 및 기존 GO 이탈 이력 보존 | [rosa51](https://github.com/321Team/infra-rosa/pull/51) MERGED `70e5dc8cc52e44919c2390feb71d1631111a6e1b`. 수집기 코드 수정이며 새 실행/AC PASS 아님 |
| Harbor C1C3 / 하영 | 읽기 원본 수신·재해시136/136·33개 rc0의 기존 검토 재사용. 카드v0·예측 묶음27파일 해시 확인 | [최소 보완3건](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6292974828). 아직 Robot/Secret 발급·전환·cold-pull·D22 FINAL 미완료 |
| IaC live/source 정합 / 하영·권욱 | [tf33](https://github.com/321Team/infra-terraform/pull/33) MERGED `ef74f689df6ebf53e495f6c2b6fd9a715baca05a` | 소스 편입·독립 검토, CI0=NOT_RUN. 이 병합으로 실제 IAM 변경을 다시 수행하지 않음 |
| #46 소비 구현 / 권욱 | [cicd98](https://github.com/321Team/infra-cicd/pull/98) `f7930de90f20e5e42c36d38be7b68e3b563cd22e`, [cicd99](https://github.com/321Team/infra-cicd/pull/99) `4827ff3c1d0ec2dca5fa894b96c7c2cbb0f4c2fd` 병합. [PR100](https://github.com/321Team/infra-cicd/pull/100) 9객체 Draft 검토 | 실제 issuer/producer/finish 의미·authority 및 site 채택 미설정, 기본 STOP. CI/MOCK을 실제 공급/배포·실패차단 Runtime PASS로 표시하지 않음 |
| 앱·공급 / 재환 | 기존 두 앱 digest는 기존 원본 기준, [MSA40](https://github.com/321Team/fds-msa/pull/40) 병합 재사용. end-page [MSA41](https://github.com/321Team/fds-msa/pull/41) Draft | 실제 세 번째 digest·clean render 미수신. 0 digest/placeholder를 승인값으로 만들지 않음. D07 Major Known Issue 보존 |
| ROSA Route·삭제 / 하영 | Route [PR50](https://github.com/321Team/infra-rosa/pull/50) R1~R4 잔여, 삭제v6 namespace2건 지적 | 수정 Route·삭제v7 연결 후 변경분만 재검토. 현재 구현/실행 완료로 기재하지 않음 |
| DB A2/I4 / 재환→하영 | A2 NOT_RUN, DB Secret 절차 결정·위험 수용은 기존 범위. I4 값은 비공개1:1 | 창 C 전 실제 인계·소비/회수 연결. Secret 생성/DB 변경 GO와 구분 |

증적 private 원본은 고정 공유 `02차 프로젝트`에서 검토하고, 최종 승인 산출물만 `02 프로젝트 결과물`로 넘긴다.
원본 Plan/state/credential은 공개 GitHub에 올리지 않는다. 이 대장은 #54 제출 후보이며 Deliverable Freeze·정본 발행·인수 완료가 아니다.
