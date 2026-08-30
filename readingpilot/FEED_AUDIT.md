# 읽을거리 피드 감사 — 2026-08-30

132건을 실제로 판독해 보고 피드를 정리했다. **전부 실호출·본문 확인 근거다.**

## 제거 2

| 소스 | 사유 |
|---|---|
| **Bruegel** | 피드 전체 10건이 컨퍼런스 일정("Lunch", "Coffee break")이고 발간물이 한 건도 오지 않는다. `/rss/publications.xml` · `/feed` · `/rss` · `/rss/all.xml` 전부 404이고 홈에 `<link rel=alternate>` 피드도 없다 — **대체 경로 자체가 없다.** → `ecb_pub` 으로 대체 |
| **arXiv q-fin.TR** | 12건 전량이 마이크로구조·RL 마켓메이킹·LOB 생성. 4축 어디에도 안 걸린다. 피드는 살아 있으나 읽을 이유가 없어 URL을 주석으로 남겨 두었다 |

## Reuters — 왜 유지하되 `headline_only` 인가

파고들어 보니 3단계였다.

1. 링크가 `news.google.com/rss/articles/CBMi…` 리다이렉트인데 **protobuf 인코딩**이라
   base64 안에 URL이 없다. 그냥 열면 빈 페이지가 온다.
2. Google 내부 `batchexecute` 로 실제 URL 복원은 **성공**했다
   → `reuters.com/business/energy/oil-track-weekly-loss-even-iran-tensions-simmer-2026-08-28/`
3. **그런데 reuters.com 자체가 봇 차단이라 본문을 못 읽는다.**

즉 비공개 엔드포인트에 의존하는 취약한 디코더를 붙여도 얻는 게 없다.
limit 20→8 로 줄이고 `headline_only: true` 를 달아 **판독기가 fetch를 시도하지 않게** 했다.

## 신규 3

| 소스 | 검증 |
|---|---|
| `ecb_pub` | 실호출 15건, 워킹페이퍼 제목 정상 — Bruegel 대체 |
| `gcaptain` | **Reuters가 못 주던 호르무즈·탱커 beat를 본문까지 준다.** 판독 확인: 파나마운하 혼잡 기사에서 대기 14척·예약 없으면 최대 8일·초대형탱커 1척이 새치기에 $4.6M 지불까지 나온다 |
| `hellenic_shipping` | 실호출 20건 — BDI·건화물·탱커 운임 |

## 한도 축소 5

| 소스 | 변경 | 근거 |
|---|---|---|
| `nber` | 20→10 | 매일 신간 20편 중 우리 축에 걸리는 건 0~2편 |
| `liberty_street` | 25→12 | 게시가 주 1~2회인데 25건은 두 달치를 매일 되긁던 것 |
| `everycrsreport` | →8 | 12건 중 9건이 축 밖(사회보장 과세·우편투표·증류주 규제) |
| `oregon_group` | →8 | 아래 |
| `baker_institute` | →5 | 10건 중 8건이 2025년 자료. 죽은 피드는 아니고 발행이 드물다 |

## `tier` 도입

`primary` / `secondary` / `promotional` / `headline-only` 를 소스마다 달았다.
판독 프롬프트가 이걸 읽고 취급을 달리한다.

**`oregon_group` 을 `promotional` 로 내린 이유**: "구리 슈퍼 스퀴즈" 기사의 본론이
Generation Mining 프로젝트 소개였다. 인용된 골드만 적자 전망(2026년 64만 톤)은
**원출처를 찾기 전에는 쓰지 않는다.** 핵심광물 커버리지를 대체할 피드가 없어 유지하되
출처가 아니라 **포인터로만** 쓴다.

## write_reading() 변경 — 착시를 코드에서 막았다

판독 불가 피드는 섹션마다 ⚠ 배너가 붙고, 프론트매터에 `readable: N / headline_only: M` 이 찍힌다.

> 표시하지 않으면 "수집됐다"는 착시만 남는다. 실제로 2026-08-30 Reuters 20건이
> 전부 판독 불가였는데 목록상으로는 정상으로 보였다.
> 같은 날 논문 하베스터에서도 **랜딩페이지 6건을 본문으로 세고 있었다** — 같은 종류의 오류다.
> **집계가 거짓말을 못 하게 만드는 것**이 이 변경의 목적이다.

## 결과

소스 12→11개, 하루 132→114건. 검증: `python -m databook intel --only reading --dry-run` → 성공 11 / 실패 0.
