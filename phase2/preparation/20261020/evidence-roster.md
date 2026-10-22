# #49 증적·산출물 접수 대장

기준: 2026-10-22 00시대 KST 재조회. 기존 10/20 접수 기록을 재사용하며 코드·결정 delta만 갱신한다. [하영 회신](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6291485599), [재환 회신](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-6291988326)을 통합했다.
생산·공유·수신/재해시·내용 검토·증적 편입·AC 인수를 각각 구분한다. 원본 전체 재제출이나 동일 시험 반복은 요구하지 않는다.

| 대상·생산 책임 | 현재 확인 범위 | 편입·인수 상태 / 다음 완료조건 |
|---|---|---|
| D-11d 원본 / 권욱·재환, 편입 하영 | 권욱 공유·재해시·내용 검토, 교차 독립 검토 연결 완료 | [ev249](https://github.com/321Team/fds-project-evidence/pull/249) MERGED `04464931ae70fc4d78fb2601d6cc2c384487b317`. 18파일 편입이며 전체 ROSA AC 완료와 구분 |
| Stage-B VPN / 재환 | 10/15 기존 수용·원본 편입 재사용 | [ev239](https://github.com/321Team/fds-project-evidence/pull/239) 기존 병합. 현재 창 A/B/C 전체 PASS로 확대하지 않음 |
| 창 A / 재환·하영 | T1/T3 PASS, T3-R 성공 보고, T6 INCONCLUSIVE. DB W4·P9/P8·양쪽 V9 원복/정리 보고. 원본3개 비공개 반출·권욱3/3 수신/검토 | 증적 PR 아직 미제출, **재환 담당**. 기존 수신 원본과 중앙 한계 판정을 편입해 Close 전에 연결. 새 시험/중복 반출 요구 없음 |
| G4 후속 / 하영·재환→권욱 | #7 B/A·N3, C7 일부 미실행. [#39 입력](https://github.com/321Team/fds-project-baseline/issues/39#issuecomment-6288503072) | 기존 원 AC의 잔여와 처분 근거 필요. T6를 PASS로 변경하거나 보류만으로 G4 완료 처리하지 않음 |
| PG-03 / 하영 | 6-1 관측 수용, 6-2 NOT_RUN, PG-03 HOLD 및 기존 GO 이탈 이력 보존 | [rosa51](https://github.com/321Team/infra-rosa/pull/51) MERGED `70e5dc8cc52e44919c2390feb71d1631111a6e1b`. 수집기 코드 수정이며 새 실행/AC PASS 아님 |
| Harbor C1C3 / 하영 | 기존 읽기 원본·수신 검증 재사용. [v1 검토](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6314870347)에서 manifest9/9·script2개가 기존 중앙 수정 후보와 동일함을 확인해 기존 B1~B3 정적 수정 연결 | 실제 netns/예측 지문 대조·호스트 적용·정상 Robot/Secret·앱 SA 연결/readback·cold-pull·실패/회수 원본은 별도. [앱 SA (가) 결정](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6315085580)은 실행0, D22 FINAL=PENDING_RUNTIME 유지 |
| IaC live/source 정합 / 하영·권욱 | [tf33](https://github.com/321Team/infra-terraform/pull/33) MERGED `ef74f689df6ebf53e495f6c2b6fd9a715baca05a` | 소스 편입·독립 검토, CI0=NOT_RUN. 이 병합으로 실제 IAM 변경을 다시 수행하지 않음 |
| #46 소비 구현 / 권욱 | [PR100~109](https://github.com/321Team/infra-cicd/pull/109) MERGED. PR109 `54d108bd5f6ef6228cf92c8100c182f9c59995ae`는 P2 job/driver 편입. [PR110](https://github.com/321Team/infra-cicd/pull/110) `aebc03bbaa849f0b9660f66d29e480e0ce092e65` 하영 범위 APPROVED·재환 범위 대기, CI708=704 PASS/4 SKIP. [PR111](https://github.com/321Team/infra-cicd/pull/111) `96b483b5ff8c7d77eb80bc6b6ee03cc134af54a8`은 수신/전송·job 부모 helper Draft, CI763=759 PASS/4 SKIP | 09시대 코드/CI delta이며 독립 리뷰·MERGE 대기. [운영 구성 연결표](p46-operating-configuration.md)의 `SITE=None`·실제 SSH/rendezvous·issuer/source/control/producer/finish·운영 자격 경로는 미채택. 코드·MOCK/CI를 Runtime·AC 인수로 표시하지 않음 |
| 앱·공급 / 재환 | 기존 두 current digest/TBS·Push 공급 원본 재사용. 현재 main 소비 계약은 2앱/6객체, [MSA41](https://github.com/321Team/fds-msa/pull/41) end-page 후보 Draft, [MSA42](https://github.com/321Team/fds-msa/pull/42) Harbor 후보 Draft | D22 FINAL 이후 실제 Registry/full image URI·clean render/contract/source를 결속. 실제 세 번째 image는 미수신이며 9/3 코드 지원만으로 채택·전체 AC 면제하지 않음. 기존 공급 원본 재빌드/재Push·중복 제출 요구 없음 |
| ROSA Route·삭제 / 하영 | Route [PR50](https://github.com/321Team/infra-rosa/pull/50) R1~R4 잔여, 삭제v6 namespace2건 지적 | 수정 Route·삭제v7 연결 후 변경분만 재검토. 현재 구현/실행 완료로 기재하지 않음 |
| DB A2/I4 / 재환→하영 | A2 NOT_RUN. DB Secret 절차 v2는 [기존 B1~B3 검토](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6287016696) 대비 같은 원본·생성 HOLD. I4 값은 기존 비공개1:1 | [창 C v1.1](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-6315050301)의 전체245분·소비 중지/C-STOP·원복/정리 포함은 미승인 제안. Secret 보완·B 실제 인계·#46 종료 scope를 연결하고 기존 security 수명을 유지. 새 실행 GO 아님 |

증적 private 원본은 고정 공유 `02차 프로젝트`에서 검토하고, 최종 승인 산출물만 `02 프로젝트 결과물`로 넘긴다.
원본 Plan/state/credential은 공개 GitHub에 올리지 않는다. 이 대장은 #54 제출 후보이며 Deliverable Freeze·정본 발행·인수 완료가 아니다.
