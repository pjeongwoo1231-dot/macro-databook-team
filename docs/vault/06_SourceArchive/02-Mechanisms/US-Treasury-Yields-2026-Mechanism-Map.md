---
title: "US Treasury Yields 2026 Mechanism Map"
type: "mechanism-map"
period: "2020-2026"
primary_text_read: true
reading_scope: "직접 검토한 2020~2026년 Fed·연방준비은행·Treasury·SEC·CFTC·IAWG·OFR·BIS·IMF·CBO·NBER·OECD 원문 38건을 바탕으로 전파경로를 종합."
status: "verified-primary-source"
tags:
  - US-Treasury
  - term-premium
  - fiscal-financial-nexus
  - repo
  - NBFI
---

# 미국 국채금리 2026 메커니즘 지도

## 중심 명제

> 2026년 미국 국채금리의 핵심 위험은 단순한 ‘기준금리 상승’이 아니라, **장기 위험프리미엄의 재가격 → 국채 발행·차환 부담 → repo 기반 NBFI 중개 → 시장유동성·금융여건 → 실물 및 국제금융 전파**가 같은 방향으로 강화되는 피드백이다.

## 기본 분해: 관측수익률과 분석수익률을 구분하기

| 층위 | 무엇을 뜻하는가 | 관측·추정의 구분 | 대표 원문 |
|---|---|---|---|
| 관측 수익률 | 2년·10년·30년 constant-maturity Treasury 수익률 | H.15의 시장호가 기반 보간치 | [[US-Treasury-Yields-2026-Core-Source-Summary]] |
| 기대 단기금리 | 향후 정책금리·실물·물가에 대한 시장 기대 | 관측수익률에서 직접 분리 불가 | [[Monetary-Policy-Transmission-and-International-Spillovers]] |
| 인플레이션 보상 | 명목–실질 금리 차이에 포함된 기대·위험·유동성 | TIPS 차이만으로 순수 기대인플레이션 확정 불가 | [[US-Treasury-Yields-2026-Core-Source-Summary]] |
| term premium | 장기채 보유에 요구되는 위험보상 | ACM 등 기간구조모형의 추정치 | [[US-Treasury-Yields-2026-Core-Source-Summary]] |

## 전파경로 A: 공급충격·정책 불확실성에서 장기 위험프리미엄으로

```text
에너지·관세·지정학·공급망 충격
    ↓
단기 인플레이션 보상 및 정책경로 불확실성
    ↓
장기 실질 위험·far-forward risk premium 재평가
    ↓
10년·30년 국채수익률 상승 / 수익률곡선 가팔라짐
    ↓
모기지·회사채·주식 할인율 및 기업 투자비용 상승
```

연준의 2026년 7월 통화정책보고서는 중동 분쟁 이후 단기 인플레이션 보상이 올랐다가 되돌아온 반면 장기 인플레이션 보상은 비교적 안정적이었다고 설명한다. Covitz·Engstrom은 far-forward 금리 상승을 장기 인플레이션 위험보다 실질 위험프리미엄 상승과 연관지었다. 이는 **장기금리 상승이 반드시 장기 기대인플레이션 탈고정과 동의어는 아님**을 뜻한다.[1] [2]

### 측정 보강: term premium과 term funding premium을 혼동하지 않기

FRBSF의 CR 모형은 2026년 8월 13일 10년 zero-coupon Treasury 수익률을 평균 기대 overnight rate와 term premium으로 분해해 각각 3.41%와 1.31%를 제시한다.[11] 반면 Dallas Fed 연구는 duration 위험을 swap으로 분리한 뒤에도 기간자금 제공 자체에 대한 보상, 즉 `term funding premium`이 남을 수 있다고 제안한다.[12] 두 결과는 서로 다른 질문·모형·데이터를 사용한다. 따라서 **하나의 term-premium 숫자를 재정위험·유동성위험·duration위험의 확정적 분해로 취급해서는 안 되며**, 시장 스트레스의 실시간 진단에는 수익률·asset-swap spread·repo·depth·price impact를 함께 본다.

## 전파경로 B: 적자·발행·만기구성에서 term premium으로

```text
적자·공공부채·순시장성차입 확대
    ↓
민간 투자자의 국채 흡수 필요 증가
    ↓
국채 수급·duration 배분·발행 만기구성 재평가
    ↓
term premium 및 수익률곡선 변화
    ↓
이자비용·재정전망·시장신뢰에 대한 피드백
```

CBO는 높은 적자·부채와 장기금리의 조건부 기준선을 제시하고, TBAC는 실제 차입수요·coupon/bill 발행구성·SOMA 변화·수요지표를 점검한다.[3] [4] NBER WP 35098은 경매발표 충격 분석에서 debt-volume shock이 term premium을 높이고 금융여건을 긴축시킨다는 결과를 제시하며, maturity-extension shock은 장기금리와 다른 방식으로 위험프리미엄·재정 불확실성을 바꿀 수 있다고 보고한다.[5]

**해석 경계:** 적자·부채가 크다고 해서 같은 비율로 즉시 금리가 상승하는 기계적 규칙은 없다. 성장률, 인플레이션, 국내외 안전자산 수요, 만기구성, 정책 신뢰, 시장 중개능력이 함께 작용한다.

## 전파경로 C: 국채시장 중개·repo·NBFI의 증폭

```text
국채 발행·금리변동·수급충격
    ↓
repo 조달조건·선물마진·swap spread·VaR 변화
    ↓
헤지펀드 relative-value / basis trade 포지션 조정
    ↓
현물 국채 매도 및 dealer balance-sheet 수요 증가
    ↓
시장 유동성 저하 ↔ 금리 변동성·term premium 확대
```

BIS·IMF·연준은 금융중개가 은행 단독 구조에서 NBFI와 prime brokerage·repo·파생상품을 포함한 구조로 이동했다는 점을 공통으로 강조한다.[6] [7] [8] 헤지펀드의 basis trade와 swap-spread 거래는 평상시 가격발견과 유동성에 기여할 수 있지만, repo haircut·margin·VaR 제약이 동시 발생하면 디레버리징이 국채 현물·선물·repo시장에 함께 전파될 수 있다.[8]

| 증폭기 | 평상시 기능 | 스트레스 시 취약성 | 직접 근거 |
|---|---|---|---|
| basis trade | 현물–선물 가격 괴리 축소 | repo 조달·마진 악화 시 빠른 청산 | Fed FEDS Note, 2026 |
| swap-spread trade | 현물·swap 시장 간 상대가치 중개 | 금리·유동성 충격에 포지션 unwind | Fed FEDS Note, 2026 |
| dealer 중개 | 시장조성·repo·위험 흡수 | VaR·balance-sheet 제약이 위험 흡수 능력을 축소 | Fed FSR, 2026 |
| MMF·펀드·보험 | 국채 수요·duration 관리 | 환매·margin call·유동성 불일치가 매도를 유발 | BIS AER, 2026; IMF GFSR, 2026 |

### 역사·측정 보강: 2020년과 2025년을 구분하기

2020년 3월에는 현금 수요와 레버리지 해소가 dealer 중개능력과 충돌하면서 Treasury market dysfunction이 나타났다. 연준·OFR 연구는 large hedge funds의 Treasury 매도와 basis trade unwind가 그 스트레스의 한 증폭기였을 수 있다고 보지만, 모든 매도를 basis trade 하나로 환원하지 않는다.[13] [14] [15] 2025년 4월 관세 충격에서는 장기수익률·bid-ask spread·depth·price impact가 급격히 악화했으나, repo 자금조달이 상대적으로 질서 있게 유지돼 2020년 같은 광범위한 dysfunction으로 진행하지 않았다는 뉴욕연은의 평가가 있다.[16] [17]

이 차이는 2026년의 관찰 규칙을 만든다. **국채수익률 상승 자체와 시장기능 악화를 구별**해야 하며, 둘 사이의 연결고리는 변동성, repo rollover 비용, margin·haircut, dealer balance-sheet 여력, 고객 매도흐름이다. Basis trade의 규모도 CFTC short futures·Form PF net repo·TRACE cash-futures 거래가 서로 다른 상·하한과 시차를 지니므로 단일 숫자로 단정할 수 없다.[14]

### 제도 전환: 중앙청산은 해결책이면서 이행 리스크이기도 하다

중앙청산 확대는 netting을 늘리고, 상대방·운영 위험과 정보 공백을 줄이며, dealer balance sheet의 효율을 높일 수 있다.[18] [19] OFR의 2025년 자료 기반 반사실 계산은 중앙청산 rule 적용 시 평균 일일 Treasury repo의 중앙청산 비중이 45%에서 77%가 될 수 있고, U.S. G-SIB dealer subsidiaries의 non-netted repo·reverse repo 포지션이 $207bn 감소할 수 있음을 제시한다.[19] 다만 이는 시장참가자의 행태변화를 반영하지 않은 반사실이다. SEC가 예고한 cash 청산 2026년 12월 31일, repo 청산 2027년 6월 30일의 이행 과정은 margin, 국경간 거래, 계열사, fails, clearing outage를 포함한 새로운 운영위험도 남긴다.[20]

## 전파경로 D: 은행·재정·실물 및 국제금융으로

```text
국채 수익률 재가격
    ├─ 은행 증권 포트폴리오 평가손익·자본·대출 여력
    ├─ 재정 이자비용·차환·정책여력
    ├─ 모기지·회사채·사모신용 차입비용
    └─ 달러·캐리트레이드·신흥국 자본흐름
          ↓
금융여건 긴축 → 투자·주택·소비·성장 하방 위험
```

2022~2023년 긴축 국면에서 보인 은행의 duration·평가손실 문제는 2026년에는 주권부채·NBFI 연결을 포함하는 더 넓은 fiscal–financial nexus로 확장됐다.[6] IMF는 높은 공공부채와 단기발행 의존, 은행–주권 연결, NBFI 레버리지의 상호작용을 금융안정의 증폭기라고 진단한다.[7]

국경간 측면에서 최종 보유자 측정에는 한계가 있다. Cayman 소재 헤지펀드의 국채보유가 TIC 통계에서 과소계상될 수 있다는 연준 연구는 외국인 보유자별 표면 통계를 수요의 완전한 설명으로 사용해서는 안 됨을 보여준다.[9] FSB는 이런 데이터·국경간 연결을 감독과 위기대응의 핵심 공백으로 본다.[10]

## 역사적 연결

| 시기 | 핵심 사건 | 2026년 국채금리 논의에 남긴 교훈 |
|---|---|---|
| 2008~09 | 글로벌 금융위기와 비전통적 통화정책 | 안전자산 수요와 시장 기능은 별개로 움직일 수 있음 |
| 2020-03 | dash for cash | 국채도 펀드 환매·basis trade unwind·dealer 제약 속 유동성 스트레스를 겪을 수 있음 |
| 2022~23 | 인플레이션·급격한 긴축·은행 스트레스 | 금리 상승은 은행 증권평가손실·대출·부동산·재정 이자비용으로 전파 |
| 2024 | IAWG·SEC의 중앙청산·데이터·중개 회복력 작업 | 발행·유동성·거래 투명성·repo 데이터가 함께 관리 대상임을 명확화 |
| 2025-04 | 관세 충격과 장기금리·현물 유동성의 단기 악화 | repo 안정 여부가 cash-market strain을 market dysfunction으로 번지지 않게 하는 핵심 완충장치임을 확인 |
| 2024~26 | 재정·발행·NBFI·지정학·공급충격 | term premium과 시장 중개능력이 장기금리의 독립 축으로 부각 |

## 정책 상충

| 정책 목표 | 필요한 조치 | 발생 가능한 상충 |
|---|---|---|
| 물가안정 | 기대 탈고정 방지, 정책 신뢰 유지 | 시장유동성 지원이 완화 신호로 해석될 위험 |
| 시장기능 | repo·국채시장 유동성 backstop의 운영 준비 | 반복 개입이 레버리지·도덕적 해이를 키울 위험 |
| 재정 지속가능성 | 신뢰할 수 있는 중기 경로, 발행·만기구성 관리 | 단기 자금조달 비용과 차환위험의 교환관계 |
| NBFI 회복력 | repo·leverage·상대방·공시·데이터 강화 | 과도한 규제가 정상시 유동성·헤지 기능을 위축할 위험 |
| 중앙청산 이행 | netting·가시성·상대방·운영위험 관리 | margin·cross-border·계열사·clearing outage 전환위험 |

## 연결 노트

- [[US-Treasury-Yields-2026-Core-Source-Summary]]
- [[US-Treasury-Yields-2026-Expansion-Primary-Source-Catalog]]
- [[US-Treasury-Yields-Expansion-File-Verification]]
- [[2024-2026-Comparative-Mechanism-Map]]
- [[2024-2026-Core-Source-Summary]]
- [[Credit-Leverage-Risk-Pricing-Loop]]
- [[Monetary-Policy-Transmission-and-International-Spillovers]]

## References

[1]: https://www.federalreserve.gov/monetarypolicy/2026-07-mpr-part1.htm "Federal Reserve Board, Monetary Policy Report – July 2026"  
[2]: https://www.federalreserve.gov/econres/notes/feds-notes/why-have-far-forward-nominal-treasury-rates-increased-so-much-in-the-past-few-years-20260212.html "Covitz and Engstrom, 2026"  
[3]: https://www.cbo.gov/publication/62105 "CBO, The Budget and Economic Outlook: 2026 to 2036"  
[4]: https://home.treasury.gov/system/files/221/CombinedChargesforArchivesQ32026.pdf "U.S. Treasury, TBAC FY2026 Q3 Report"  
[5]: https://www.nber.org/papers/w35098 "Bi, Phillot and Zubairy, NBER Working Paper 35098"  
[6]: https://www.bis.org/publ/arpdf/ar2026e2.htm "BIS Annual Economic Report 2026, Chapter II"  
[7]: https://www.imf.org/en/publications/gfsr/issues/2026/04/14/global-financial-stability-report-april-2026 "IMF Global Financial Stability Report, April 2026"  
[8]: https://www.federalreserve.gov/econres/notes/feds-notes/decomposing-hedge-funds-u-s-treasury-exposures-20260622.html "Monin, 2026"  
[9]: https://www.federalreserve.gov/econres/notes/feds-notes/the-cross-border-trail-of-the-treasury-basis-trade-20251015.html "Barth et al., 2025"  
[10]: https://www.fsb.org/2025/07/leverage-in-nonbank-financial-intermediation-final-report/ "FSB, 2025"  
[11]: https://www.frbsf.org/research-and-insights/data-and-indicators/treasury-yield-premiums/ "FRBSF, Treasury Yield Premiums"  
[12]: https://www.dallasfed.org/research/economics/2026/0625 "Dallas Fed, Term funding premium: Time is money even absent interest rate risk"  
[13]: https://www.federalreserve.gov/econres/notes/feds-notes/sizing-hedge-funds-treasury-market-activities-and-holdings-20211006.html "Federal Reserve Board, Sizing hedge funds’ Treasury market activities and holdings"  
[14]: https://www.federalreserve.gov/econres/notes/feds-notes/quantifying-treasury-cash-futures-basis-trades-20240308.html "Federal Reserve Board, Quantifying Treasury Cash-Futures Basis Trades"  
[15]: https://www.financialresearch.gov/briefs/2020/07/16/basis-trades-and-treasury-market-illiquidity/ "OFR Brief 20-01, Basis Trades and Treasury Market Illiquidity"  
[16]: https://www.newyorkfed.org/newsevents/speeches/2025/per250509 "FRBNY, Recent Developments in Treasury Market Liquidity and Funding Conditions"  
[17]: https://libertystreeteconomics.newyorkfed.org/2026/04/treasury-market-liquidity-since-april-2025/ "FRBNY, Treasury Market Liquidity Since April 2025"  
[18]: https://home.treasury.gov/system/files/136/2024-IAWG-report.pdf "IAWG, Enhancing the Resilience of the U.S. Treasury Market: 2024 Staff Progress Report"  
[19]: https://www.financialresearch.gov/the-ofr-blog/2026/01/29/central-clearing-impact-repo-market/ "OFR, How Will Central Clearing Impact the Repo Market?"  
[20]: https://www.sec.gov/newsroom/speeches-statements/uyeda-statement-update-secs-work-toward-treasury-clearing-implementation-080726-update-secs-work-toward-treasury-clearing-implementation-august-2026 "SEC, Update on the SEC’s Work Toward Treasury Clearing Implementation [August 2026]"  
