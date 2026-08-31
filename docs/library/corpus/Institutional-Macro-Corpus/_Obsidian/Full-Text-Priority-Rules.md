---
title: Full Text Priority Rules
tags: [institutional-research, full-text, macroeconomics, corpus]
---

# Full Text Priority Rules

> 전체 문서는 metadata·공식 URL로 보존한다. 공개 원문은 거시·금융·원자재 지식 그래프의 메커니즘 노드를 확장하는 자료부터 우선 보관한다.

## Priority A — 반드시 원문 보관

| Domain | Core keywords / signals | Typical source series |
|---|---|---|
| 금융안정·은행·유동성 | bank, banking, liquidity, repo, reserves, collateral, dealer, leverage, private credit, NBFI, money market fund | Fed FEDS / Notes, BIS QR / WP, IMF GFSR, BOJ Review |
| 통화정책·인플레이션 | monetary policy, inflation, wage, expectations, term premium, yield curve, QT, balance sheet | Fed FEDS, ECB Economic Bulletin, BOJ WP, BIS QR, IMF WEO |
| 달러·FX·글로벌 유동성 | dollar, FX, exchange rate, capital flows, international finance, EM, spillovers, foreign currency debt | Fed IFDP, BIS WP / QR, IMF GFSR / WP, BOJ |
| 원자재·에너지·금속 | commodity, oil, gas, LNG, energy, metals, copper, critical minerals, inventory, futures, supply | Fed Notes / IFDP, BIS, IMF, World Bank, OECD |
| 중국·무역·공급망 | China, tariff, trade, exports, imports, supply chain, industrial policy, geoeconomics | Fed IFDP / Notes, World Bank, OECD, IMF |
| 거시 체제 전환 | fiscal, debt, housing, productivity, AI investment, financial conditions, geopolitical risk, sanctions | Fed, ECB, BIS, IMF, OECD |

## Priority B — 메타데이터 우선, 필요 시 원문 보관

노동시장·불평등·가계금융·산업별 미시연구·교육·보건·개별 국가 개발정책 등은 제목·초록·공식 URL을 유지한다. 다만 위 Priority A 메커니즘과 직접 이어지는 경우에는 원문을 승격한다.

## Technical Filters

```text
Primary title / abstract keyword match
AND public PDF / HTML availability
AND publication date >= 2020-01-01
AND official source URL
AND no duplicate DOI / official URL / normalized title
```

## Storage and File Naming

```text
raw/{Institution}/{Series}/{Year}/{document_id}__{short-title}.pdf
```

각 원문 옆에는 동일 basename의 `.md` source note를 두고, 공식 URL·PDF URL·SHA256·수집시각·기관 고지·주제 태그·관련 Mechanism Node를 기록한다.

## Exclusions

- 로그인·유료·접근제한 문서의 우회 수집
- robots.txt 또는 명시적 이용조건에 반하는 대량 수집
- title keyword만 맞고 초록·내용이 핵심 메커니즘과 무관한 문서
- 동일한 보고서의 언어별 중복본, 동일 PDF의 단순 mirror

## Review Rule

원문 수집 결과는 `public_downloaded`, `official_link_only`, `metadata_only`, `restricted`, `failed`로 구분한다. 실패·제한 문서는 숨기지 않고 manifest에 남긴다.
