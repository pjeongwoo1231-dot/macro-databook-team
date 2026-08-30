---
title: "Copper Atomic Claims, Mechanisms and Debates"
type: MOC
tags: [type/MOC, domain/commodity, flag/unverified]
status: unverified
reliability: secondary
verified: "❌ 원문 미대조 — Manus AI 생성"
import_origin: "카카오톡 수신 Copper Atomic Claims, Mechanisms and Debates.md (2026-08-13)"
related: ["[[Library MOC]]"]
---

> ⚠ **원문 미대조 · AI 생성 문서.** 401–500 배치의 **중간 계층**(claim register)이다. 제텔이 아니라 **제텔 후보 목록**으로 취급한다.
> 볼트의 [[Dr. Copper는 급락기에만 경기를 말한다]](원문 대조 완료)와 **충돌 여부를 먼저 확인**할 것.

> ⚠ **끊긴 링크 28건 — 2026-08-19 실측.** 이 문서가 인용하는 `Copper Macro-Causal Research Library 401-500`과
> 그 안의 개별 노트(`421 Bernanke Gertler Gilchrist`, `484 Fama & French`, `DEBATE_001` 등)는
> **볼트에 존재하지 않는다.** 임포트되지 않았거나 애초에 만들어진 적이 없다.
> 이 링크들은 **출처가 아니라 만들어야 할 목록**이다. **판정에 인용하지 않는다.**
> 구리 판정은 원문 대조가 끝난 [[Dr. Copper는 급락기에만 경기를 말한다]]와 [[구리 가격]] 노드를 쓴다.

# Copper Atomic Claims, Mechanisms and Debates

> 이 파일은 [[Copper Macro-Causal Research Library 401–500]]의 논문 노트를 메커니즘 중심 지식 그래프로 전환하기 위한 중간 계층이다. 각 claim은 하나의 경제 관계만 담고, 논문·증거·경계조건·관찰변수·반증조건을 분리한다.

## Claim Register

| ID | Atomic claim | Tags | Confidence | Supporting literature | Boundary conditions |
|---|---|---|---|---|---|
| CLAIM-CU-001 | China credit impulse ↑ → fixed investment ↑ | [CHINA] [CREDIT] [DEMAND] [GROWTH] | HIGH | Kiyotaki–Moore; BGG; Chen et al.; Chen–Ren–Zha | credit allocation, property policy, debt service burden |
| CLAIM-CU-002 | Fixed investment ↑ → construction·infrastructure·grid activity ↑ | [CHINA] [DEMAND] [COMMODITY] | HIGH | Song et al.; Dong et al.; Ma et al. | investment composition, local-government funding, project completion |
| CLAIM-CU-003 | Construction·grid·manufacturing activity ↑ → copper end-use demand ↑ | [CHINA] [DEMAND] [COMMODITY] | HIGH | Dong et al.; Ma et al.; Fama–French (metals) | material intensity, substitution, scrap availability |
| CLAIM-CU-004 | Copper demand ↑ relative to refined supply → exchange inventory ↓ | [DEMAND] [INVENTORY] [COMMODITY] | HIGH | storage literature; physical market studies | off-exchange stocks, warrant movement, import arbitrage |
| CLAIM-CU-005 | Inventory ↓ → convenience yield ↑ | [INVENTORY] [FUTURES] [COMMODITY] | HIGH | Working; Fama–French; Deaton–Laroque; Casassus–Collin-Dufresne | storage access, financing cost, grade/location differences |
| CLAIM-CU-006 | Convenience yield ↑ → backwardation / spot premium ↑ | [INVENTORY] [FUTURES] [COMMODITY] | HIGH | Working; Fama–French; Litzenberger–Rabinowitz; Casassus–Collin-Dufresne | interest rates, warehouse fees, delivery constraints |
| CLAIM-CU-007 | Ore grade ↓ → energy·water·material intensity ↑ | [SUPPLY] [TECHNOLOGY] [COMMODITY] | HIGH | Northey et al.; Calvo et al.; Mudd | technology, mine mix, energy source, recycling |
| CLAIM-CU-008 | Volatility ↑ → mining investment threshold ↑ | [SUPPLY] [FINANCE] [EXPECTATIONS] | HIGH | Pindyck; Dixit–Pindyck; Slade | project reversibility, hedging, financing access |
| CLAIM-CU-009 | Mining capex lag ↑ → supply response delay ↑ | [SUPPLY] [COMMODITY] | HIGH | Pindyck; Radetzki; mining economics | permitting, geology, financing, political risk |
| CLAIM-CU-010 | USD / real rates ↑ → commodity financial demand ↓ | [FX] [FINANCE] [COMMODITY] | MEDIUM | Chen–Rogoff–Rossi; Frankel; futures literature | physical tightness, global growth, risk aversion |
| CLAIM-CU-011 | China slowdown → copper price ↓ | [CHINA] [DEMAND] [COMMODITY] | MEDIUM | China demand literature; macro fundamentals studies | can be offset by supply shock, inventories, USD, other demand sources |
| CLAIM-CU-012 | Mine/refining disruption ↑ → copper price ↑ despite China slowdown | [SUPPLY] [INVENTORY] [COMMODITY] | MEDIUM–HIGH | supply response, storage theory | size/duration of shock, buffer stocks, substitution |
| CLAIM-CU-013 | TC/RC ↓ → concentrate market tightness or smelter margin compression | [SUPPLY] [PROCESSING] [COMMODITY] | MEDIUM | mining and refining market structure | new smelter capacity, treatment terms, quality mix |
| CLAIM-CU-014 | Copper price ↑ → PPI ↑ | [INFLATION] [COMMODITY] | MEDIUM | macro commodity literature | copper weight, shock origin, pass-through speed |
| CLAIM-CU-015 | Copper price ↑ → broad CPI / monetary tightening | [INFLATION] [MONETARY] [COMMODITY] | LOW–MEDIUM | commodity-macro literature | price basket weight, second-round effects, central-bank reaction function |

---

# Mechanism Nodes

## [[China Credit → Fixed Investment → Copper Demand]]

```text
China Credit / TSF / Local-government finance
        ↓ HIGH
Fixed Investment
     ↙                 ↘
Housing                Infrastructure / Grid
     ↓ HIGH                 ↓ HIGH
Construction           Power equipment
         ↘             ↙
           Copper end-use demand
```

| Field | Content |
|---|---|
| Supporting papers | [[422 Kiyotaki & Moore]], [[421 Bernanke Gertler Gilchrist]], [[406 China Credit Expansion]], [[428 Financial Accelerator in China]], [[438 Dong et al.]], [[439 Ma et al.]] |
| Contradicting / limiting evidence | credit may fund debt rollover·SOEs·financial assets rather than copper-intensive investment; property policy can interrupt transmission |
| Observable variables | TSF/credit impulse, medium-long-term loans, FAI, property starts, grid investment, PMI, copper imports |
| Market confirmation | imports↑, bonded stock drawdown, SHFE inventory↓, Yangshan premium↑ |
| Failure condition | credit↑ but FAI·property·grid·imports do not rise, while inventory↑ and premium↓ |
| Confidence | HIGH for credit-to-investment conditional on allocation; MEDIUM for credit-to-copper price |

## [[Copper Supply Response]]

```text
Ore grade / geology / permitting / ESG / financing
        ↓
Mine cost and project economics
        ↓
Capex decision under uncertainty
        ↓
Mine / concentrate supply after long lead time
        ↓
Refined availability and market balance
```

| Field | Content |
|---|---|
| Supporting papers | [[452 Tilton & Lagos]], [[458 Northey]], [[463 Calvo]], [[471 Pindyck]], [[479 Radetzki]] |
| Contradicting / limiting evidence | technology, discoveries, higher recovery, recycling, substitution, new project commissioning can relax the constraint |
| Observable variables | ore grade, capex guidance, mine disruption, project approval, concentrate production, energy cost, scrap supply |
| Market confirmation | TC/RC↓, concentrate tightness, refined output constraint, warehouse draw |
| Failure condition | cost/grade pressure rises but production, inventories, and curve show no physical tightness |
| Confidence | HIGH for lead-time and investment frictions; MEDIUM for price effect |

## [[Inventory → Convenience Yield → Futures Curve]]

```text
Market balance
        ↓
Inventory / days of cover
        ↓ HIGH
Convenience yield
        ↓ HIGH
Cash-to-3M spread / contango / backwardation
        ↓ MEDIUM
Spot-price volatility and price support
```

| Field | Content |
|---|---|
| Supporting papers | [[481 Working]], [[482 Working]], [[484 Fama & French]], [[485 Deaton & Laroque]], [[489 Casassus & Collin-Dufresne]], [[500 Storage Synthesis]] |
| Contradicting / limiting evidence | exchange inventory may not equal total stocks; financing, warehousing, warrant rules and positioning affect the curve |
| Observable variables | LME/SHFE/COMEX inventory, cancelled warrants, cash-3M spread, implied convenience yield, regional premiums |
| Market confirmation | inventories↓ + premium↑ + backwardation↑ are stronger together than any one signal alone |
| Failure condition | inventories↓ but curve remains contango with weak premium and ample off-exchange supply |
| Confidence | HIGH for physical carry; MEDIUM for directional spot-price forecast |

## [[USD / Real Rates → Copper Financial Demand]]

```text
USD / real rates / global liquidity
        ↓
carry, risk premium, investment flow
        ↓
Copper futures and cross-commodity co-movement
        ↓
Spot-futures interaction
```

| Field | Content |
|---|---|
| Supporting papers | [[446 Chen Rogoff Rossi]], [[442 Pindyck Rotemberg]], [[449 Bastianin]], [[496 Bastianin]], [[497 West Wong]] |
| Contradicting / limiting evidence | severe physical tightness can overwhelm financial headwinds; FX may reflect the same commodity shock rather than cause it |
| Observable variables | DXY, US real yields, CFTC/LME positioning, ETF flows, copper curve, cross-commodity beta |
| Market confirmation | USD↑ / real yields↑ with inventory stable or rising and weak PMIs |
| Failure condition | USD↑ but inventories collapse and backwardation·physical premiums increase sharply |
| Confidence | MEDIUM |

---

# Debate Files

## [[DEBATE_001 — China slowdown: Is copper necessarily bearish?]]

| Side | Evidence |
|---|---|
| Bearish channel | China credit↓ → property·construction↓ → copper demand↓ → inventory↑ → copper price↓ |
| Bullish counter-channel | mine/refining disruption; low stocks; grid/AI/data-center demand; US/India infrastructure; USD↓; TC/RC↓ |
| Diagnosis | Does Tier 1 physical data confirm demand weakness? Are premiums·inventories·curve consistent? Is the shock China-only or global? |
| Conditional conclusion | China slowdown is a **demand headwind**, not a standalone trading rule. |

## [[DEBATE_002 — Does a lower TC/RC mean copper bullish?]]

| Side | Evidence |
|---|---|
| Bullish interpretation | concentrate tightness / smelter margin pressure can signal upstream scarcity |
| Alternative interpretation | smelter capacity additions, contract negotiation, concentrate quality, policy distortions can move TC/RC without immediate refined tightness |
| Data test | combine TC/RC with concentrate output, smelter utilization, refined production, imports, inventories, cash-3M spread |
| Conditional conclusion | TC/RC is a processing signal; it is not a standalone copper-price signal. |

## [[DEBATE_003 — Are futures curves physical or financial?]]

| Side | Evidence |
|---|---|
| Physical-storage view | inventory, storage costs, convenience yield determine carry and backwardation |
| Financial view | funding costs, positioning, risk premiums, benchmark flows affect term structure |
| Data test | stocks·premiums·warrants·spread plus rates·positioning·ETF flow |
| Conditional conclusion | futures curves are joint physical-financial equilibria. |
