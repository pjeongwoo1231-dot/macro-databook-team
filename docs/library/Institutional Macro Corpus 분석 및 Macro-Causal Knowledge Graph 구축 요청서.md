# Institutional Macro Corpus 분석 및 Macro-Causal Knowledge Graph 구축 요청서

## 1. 역할과 최종 목표

당신은 중앙은행 연구, 국제금융, 거시경제, 금융시장, 원자재 및 정책기관 자료를 전문적으로 분석하는 연구자다. 첨부된 `Institutional-Macro-Corpus-B3-Hybrid.zip`을 기반으로 2020년 이후 공개된 Fed, ECB, BOJ, BIS, IMF, World Bank, OECD 자료를 체계적으로 분석하라.

최종 목표는 문서별 요약을 만드는 것이 아니라, 다음과 같은 **Macro-Causal Knowledge Graph**를 구축하는 것이다.

> Global Dollar → Global Liquidity → Bank Balance Sheet → Credit → Asset Prices → Financial Conditions → Real Economy

그리고 다음의 실물·국제·원자재 경로를 위의 금융 경로와 연결하라.

> China / Trade / Supply Chain / Energy / Metals / Commodity Prices → Inflation / FX / Capital Flows / Monetary Policy / Financial Stability

분석 결과는 Obsidian에서 바로 사용할 수 있는 Markdown 문서와 상호 연결된 메커니즘 노드로 작성하라.

## 2. 첨부파일과 먼저 읽을 파일

먼저 압축을 풀고 아래 파일을 순서대로 읽어라.

1. `README.md`
2. `_Obsidian/Institutional-Macro-Corpus-Index.md`
3. `_Obsidian/Full-Text-Priority-Rules.md`
4. `manifest/documents.jsonl`
5. `manifest/documents.csv`
6. `manifest/quality_check.json`
7. `raw/` 폴더의 실제 공개 원문 PDF

`documents.jsonl`과 `documents.csv`는 전체 문서 목록과 공식 링크를 확인하는 인덱스로 사용하라. 실제 원문 분석은 manifest의 `local_path`가 비어 있지 않고 `full_text_status`가 `public_downloaded`인 문서부터 수행하라.

## 3. 중요한 수집 범위 원칙

이 코퍼스는 모든 자료를 동일한 깊이로 읽는 구조가 아니다. 전체 문서의 metadata와 공식 URL은 보존하되, 다음 주제의 문서를 원문 분석 우선 대상으로 삼아라.

| 우선순위 | 핵심 영역 | 주요 검색어 |
|---:|---|---|
| 1 | 금융안정·은행·유동성 | bank, liquidity, repo, reserves, collateral, dealer, leverage, credit, NBFI |
| 2 | 통화정책·인플레이션 | monetary policy, inflation, wages, expectations, term premium, yield curve, QT |
| 3 | 달러·FX·글로벌 유동성 | dollar, exchange rate, FX, capital flows, international finance, EM, spillovers |
| 4 | 원자재·에너지·금속 | commodity, oil, gas, LNG, energy, metals, copper, inventory, futures |
| 5 | 중국·무역·공급망 | China, trade, tariff, exports, imports, supply chain, industrial policy |
| 6 | 거시 체제·지정학 | fiscal, debt, housing, productivity, AI investment, sanctions, geopolitical risk |

Working Paper, FEDS Note, Research Bulletin, staff note 및 discussion paper는 동료심사 논문과 구분하라. 기관 연구자의 견해와 기관의 공식 정책 결정을 동일하게 취급하지 말라.

## 4. 분석 순서

처음부터 전체 문서를 한 번에 분석하지 말고 다음 단계로 진행하라.

### 1단계: 파일럿 분석

먼저 20~30편을 골라 분석 형식을 검증하라. 파일럿은 다음 영역이 균형 있게 포함되도록 구성하라.

- Fed IFDP 또는 FEDS: 달러·FX·자본이동·글로벌 금융조건
- BIS Working Paper 또는 Quarterly Review: 글로벌 유동성·은행 대차대조표·신용·자산가격
- ECB Economic Bulletin 또는 Research Bulletin: 통화정책·인플레이션·금융시장
- BOJ Working Paper 또는 Review: 금리·임금·인플레이션 기대·FX·금융안정
- World Bank: 중국·무역·원자재·공급망·신흥국
- 가능하면 IMF 또는 OECD: 글로벌 전망·금융안정·에너지전환·산업정책

### 2단계: 파일럿 형식 검수

파일럿 결과가 단순 요약인지, 실제 인과 메커니즘을 추출했는지 검수하라. 제목과 초록만으로 추론하지 말고 원문에서 연구 설계와 결과를 확인하라. 원문을 읽지 못한 문서는 반드시 `metadata_only` 또는 `official_link_only`로 표시하라.

### 3단계: 배치 확장

파일럿 형식이 확정되면 50~100편 단위로 확장하라. 각 배치가 끝날 때마다 중복 문서, 유사한 주장, 상반된 증거, 미확인 수치를 별도로 정리하라.

### 4단계: 지식 그래프 통합

최종적으로 기관·문서별 노트를 다음 메커니즘 노드에 연결하라.

`[[Global Dollar]]`  
`[[Global Liquidity]]`  
`[[Bank Balance Sheet]]`  
`[[Credit Cycle]]`  
`[[Financial Conditions]]`  
`[[Capital Flows]]`  
`[[FX Pass-through]]`  
`[[Inflation Expectations]]`  
`[[Commodity Prices]]`  
`[[China Demand]]`  
`[[Copper Regime]]`  
`[[Energy Transition]]`  
`[[Supply Chain]]`  
`[[Financial Stability]]`  
`[[Monetary Policy Reaction]]`

## 5. 문서별 분석 템플릿

각 문서마다 아래 항목을 빠짐없이 작성하라.

### 기본 서지정보

- 기관:
- 시리즈:
- 문서 유형:
- 발행일:
- 저자:
- 공식 문서 URL:
- 공식 PDF URL:
- 원문 접근 상태:
- 동료심사 여부:
- 관련 데이터·부록 URL:

### 1. 연구 질문

저자가 설명하려는 경제적·금융적 현상을 한두 문장으로 정리하라.

### 2. 문헌상 공백

기존 연구가 설명하지 못했거나 이 문서가 새롭게 추가하는 부분을 적어라. 단순히 “중요한 주제다”라고 쓰지 말라.

### 3. 핵심 주장

저자의 핵심 주장을 한 문장으로 먼저 제시하고, 그 주장이 성립하는 조건을 설명하라.

### 4. 핵심 메커니즘

다음 형식으로 작성하라.

> 충격 또는 정책 변화 → 중간 전달경로 → 금융시장·실물 변수 → 최종 결과

예시는 다음과 같다.

> Fed 긴축 → 달러 강세·글로벌 유동성 축소 → EM 자본유출·은행 외화부채 부담 → 신용축소·성장 둔화

### 5. 충격 또는 정책 분류

공급충격, 수요충격, 금융충격, 통화정책충격, 재정충격, 환율충격, 지정학충격, 기후충격, 기술충격 중 해당되는 것을 분류하라.

### 6. 데이터와 변수

표본 기간, 국가·지역, 빈도, 주요 종속변수, 핵심 설명변수, 통제변수, 시장가격, 금융조건지수를 구체적으로 기록하라.

### 7. 식별전략과 방법론

VAR, local projection, event study, panel regression, factor model, structural model, high-frequency identification, instrumental variable, difference-in-differences 등 어떤 방법을 사용했는지 설명하라. 충격의 외생성 가정도 반드시 적어라.

### 8. 주요 결과

계수의 방향과 크기, 시차, 비선형성, 국가별 차이, 위기·정상기 차이를 가능한 경우 정확히 적어라. 원문에 수치가 없으면 수치를 만들어내지 말고 “정성적 결과”라고 표시하라.

### 9. 레짐 의존성

정상기, 긴축기, 완화기, 금융위기, 공급충격기, 저재고 국면, 고부채 국면에서 결과가 어떻게 달라지는지 분석하라.

### 10. 정책 함의

중앙은행, 금융감독, 재정당국, 국제기구, 외환당국이 각각 무엇을 관찰하거나 고려해야 하는지 설명하라. 정책 권고와 저자의 실증결과를 구분하라.

### 11. 자산가격 함의

금리, 국채, 회사채 스프레드, 주식, 은행주, FX, 원자재, 금, 선물곡선, 변동성, 신흥국 자산에 미치는 영향을 정리하라.

### 12. 반증조건

다음 중 무엇이 관찰되면 저자의 주장이 약해지는지 적어라.

- 예상한 충격보다 반대 방향의 반응
- 핵심 중간 전달변수의 부재
- 다른 식별전략에서 결과가 사라짐
- 표본기간·국가를 바꾸면 결과가 사라짐
- 정책 레짐을 통제하면 효과가 사라짐
- 상반된 연구가 더 강한 데이터와 식별을 제시함

### 13. 상반된 증거와 논쟁

이 문서의 결론과 다른 연구, 다른 식별전략, 다른 국가 사례가 있으면 나란히 비교하라. 합의가 없는 경우 억지로 결론을 내리지 말라.

### 14. 연결 문헌

기존 1~500번 논문 라이브러리와 이번 기관 코퍼스의 관련 문서를 Obsidian 링크로 연결하라.

### 15. Atomic Claim

검증 가능한 단일 주장 하나를 다음 형식으로 작성하라.

> [조건]에서 [충격]은 [메커니즘]을 통해 [결과]를 유발한다.

그 아래에 출처, 증거 수준, 적용 범위와 한계를 적어라.

### 16. 한 문장 요약

연구 질문·메커니즘·결과를 한 문장으로 압축하라.

## 6. Macro-Causal Knowledge Graph 작성 규칙

문서별 노트를 만든 뒤 다음 유형의 메커니즘 노드를 별도 Markdown 파일로 작성하라.

### Global Dollar 노드

Fed 정책, 달러 유동성, 외화부채, 글로벌 자본이동, EM 금융조건, 원자재 가격의 연결을 정리하라.

### Bank Balance Sheet 노드

은행 자본, 유동성, 담보, 레포, 레버리지, 대출공급, 신용스프레드, 자산가격의 연결을 정리하라.

### Commodity Prices 노드

공급·수요·재고·저장·편의수익률·선물곡선·달러·금리·금융화·인플레이션을 연결하라.

### China Demand 노드

중국 신용·부동산·인프라·제조업·전력망·수입·구리·원자재 수요를 연결하라.

### Energy Transition 노드

에너지전환 투자, 전력망, 핵심광물, 중국 정제능력, 공급망 집중, 산업정책, 지정학적 리스크를 연결하라.

각 화살표에는 반드시 관련 문서 번호 또는 Obsidian 링크를 붙여라. 가능하면 다음과 같이 신뢰도를 표시하라.

- `High`: 여러 자료와 명확한 식별전략이 일치
- `Medium`: 반복되는 상관관계이나 식별에 한계
- `Low`: 이론적 연결 또는 제한적 사례
- `Contested`: 연구 간 결론이 충돌

## 7. 통합 결과물

최종 결과물은 다음 파일 구조로 작성하라.

```text
Institutional-Macro-Analysis/
├── 00_Master_Index.md
├── 01_Macro-Causal-Knowledge-Graph.md
├── 02_Global-Dollar-and-Liquidity.md
├── 03_Bank-Balance-Sheet-and-Credit.md
├── 04_FX-Capital-Flows-and-EM.md
├── 05_Inflation-and-Monetary-Policy.md
├── 06_Commodity-Energy-Metals.md
├── 07_China-Trade-and-Supply-Chain.md
├── 08_Energy-Transition-and-Industrial-Policy.md
├── 09_Contradictory-Evidence-and-Debates.md
├── 10_Regime-Dashboard.md
├── papers/
├── mechanism-nodes/
└── batch-reports/
```

## 8. 품질관리 규칙

다음 사항을 반드시 지켜라.

1. 원문을 읽지 않은 문서의 결과를 추정해서 작성하지 말라.
2. 제목·초록만으로 방법론·결과·정책 함의를 만들어내지 말라.
3. Working Paper, Staff Note, Research Bulletin, Economic Bulletin, 공식 정책보고서를 서로 다른 문서 유형으로 구분하라.
4. 문서의 견해와 기관의 공식 정책 결정을 구분하라.
5. 수치·계수·표 번호를 원문에서 확인하지 못하면 수치를 만들어내지 말라.
6. 모든 외부 사실에는 공식 URL을 달아라.
7. 중복 문서, 개정판, 번역판, 동일 PDF mirror를 구분하라.
8. 접근제한·유료·로그인 보호 문서는 우회하지 말라.
9. `public_downloaded`, `official_link_only`, `metadata_only`, `restricted`, `failed` 상태를 유지하라.
10. 결과물 마지막에는 읽은 문서 수, 원문 분석 문서 수, metadata-only 문서 수, 접근제한 문서 수, 미완료 문서 수를 보고하라.

## 9. 첫 작업에서 제출할 결과

먼저 다음 파일을 제출하라.

1. `Pilot-Analysis-Index.md` — 파일럿 20~30편 목록과 선정 이유.
2. `Pilot-Paper-Analyses.md` — 문서별 템플릿 분석.
3. `Pilot-Mechanism-Nodes.md` — 파일럿에서 발견한 인과 메커니즘.
4. `Pilot-Contradictions-and-Gaps.md` — 상반된 증거와 자료 공백.
5. `Pilot-Quality-Report.md` — 원문 접근 상태, 분석 가능 여부, 인용 검수.

파일럿 분석을 승인하기 전에는 5,330건 전체에 대한 장문 분석을 시작하지 말라. 파일럿 결과가 만족스럽지 않으면 형식을 수정한 뒤 다음 배치로 넘어가라.

## 10. 최종 완료 조건

최종 완료로 간주하려면 다음을 모두 충족해야 한다.

- 전체 metadata manifest를 보존했다.
- 실제 원문을 읽은 문서와 링크만 확인한 문서를 구분했다.
- 핵심 주제 문서에 문서별 분석 템플릿을 적용했다.
- 기관별 연구를 메커니즘 노드와 인과 그래프로 통합했다.
- 상반된 증거와 반증조건을 별도로 기록했다.
- 기존 원자재·구리·글로벌 매크로 라이브러리와 Obsidian 링크로 연결했다.
- 수집·분석 범위와 미완료 항목을 숨기지 않고 보고했다.
