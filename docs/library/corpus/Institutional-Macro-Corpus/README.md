---
title: Institutional Macro Corpus — B-3 Hybrid Collection
author: Manus AI
tags: [institutional-research, macroeconomics, central-banks, corpus]
---

# Institutional Macro Corpus — B-3 Hybrid Collection

이 코퍼스는 **2020년 이후 공개된 기관 연구·정책·금융시장 자료**를 대상으로 한다. 모든 수집 레코드는 공식 문서 URL, 발행일, 제목, 이용 가능 여부를 유지하며, 핵심 거시·금융·원자재 메커니즘과 직접 연결되는 공개 원문만 로컬에 저장한다.

> 이 라이브러리는 “논문을 많이 가진 폴더”가 아니라, `Dollar → Global Liquidity → Bank Balance Sheet → Credit → Asset Prices → Real Economy` 및 `Commodity / China / Trade / Energy Transition` 메커니즘을 추적하기 위한 연구 인프라다.

## What Is Included

| Layer | Content | Status |
|---|---|---|
| Unified manifest | `manifest/documents.csv`, `documents.jsonl` | 현재 수집분 제공 |
| Source registry | `manifest/sources.json`, `source_status.csv` | 공식 아카이브·수집상태 기록 |
| Obsidian layer | 기관·시리즈·주제·수집 로그·원문 우선순위 규칙 | 제공 |
| Downloaded full text | `raw/` 아래 B-3 핵심 주제 공개 PDF | 부분 수집; manifest의 `public_downloaded` 확인 |
| Official link layer | `official_url`, `pdf_url` | 원문 미수집 레코드도 최대한 보존 |

## B-3 Decision Rule

**전수 metadata + 핵심 주제 공개 원문 보관**을 사용한다. 우선 보관 대상은 금융안정·은행·유동성·통화정책·인플레이션·달러·FX·글로벌 유동성·원자재·에너지·금속·중국·무역·공급망·산업정책·지정학 리스크다. 이 주제 외의 문서는 metadata와 공식 링크를 남겨 지식 그래프의 탐색성을 유지한다.

## Important Usage Notes

| Field | Use |
|---|---|
| `publication_status` | working paper / staff view / institutional publication을 구분 |
| `full_text_status` | `public_downloaded`, `official_link_only`, `metadata_only`, `restricted`, `failed` 상태 확인 |
| `official_url` | 인용·확인에 우선 사용하는 원 출처 |
| `pdf_url` | 공개 원문이 존재할 때의 공식 다운로드 링크 |
| `content_sha256` | 로컬 보관 원문의 무결성 확인 |
| `topics` | Obsidian 태그·질의·메커니즘 노드 연결의 출발점 |

## Source-Specific Caveats

연준, BOJ, BIS는 연도별·개별 공식 페이지의 구조가 비교적 안정적이어서 metadata와 PDF 링크를 직접 수집했다. ECB는 Economic Bulletin의 과거 호와 공식 RSS로 확인 가능한 최신 Research Bulletin·Working Paper를 우선 반영했다. IMF eLibrary와 OECD의 동적 publication catalog는 metadata backfill과 공개 원문 접근을 분리해야 하며, 이용제한·login 상태는 `full_text_status`에 유지한다. World Bank Documents & Reports는 공식 API를 통해 B-3 우선 주제의 문서 metadata를 확장했다.

## Obsidian Start Point

1. `_Obsidian/Institutional-Macro-Corpus-Index.md`를 시작 노트로 연다.
2. `_Obsidian/Full-Text-Priority-Rules.md`에서 원문 보관 규칙을 확인한다.
3. `manifest/documents.csv`를 Dataview 또는 CSV Importer로 불러온다.
4. 논문 노트를 만들 때는 `official_url`, 발행 상태, 반증 조건, 연결할 Mechanism Node를 함께 기록한다.

## Compliance

공개된 공식 자료만 대상으로 하며, 접근제한·유료·로그인 보호 문서는 우회하지 않는다. working paper와 staff note의 견해는 각 기관의 공식 정책 견해가 아닐 수 있으므로, manifest의 고지와 원문 disclaimer를 유지한다.
