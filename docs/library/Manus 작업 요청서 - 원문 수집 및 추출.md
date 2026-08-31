# 작업 요청서 — 기관 자료 원문 수집 및 구조화 추출

**작업 성격**: 수집(acquisition)과 기계적 추출(extraction) **전담**. 해석·요약·평가는 이 작업의 범위가 아니다.

---

## 0. 이 요청의 배경 — 왜 이렇게 요구하는가

이 산출물은 **다른 분석 시스템의 입력**으로 쓰인다. 그 시스템은 원문을 직접 대조해 수치를 검증하고 신뢰도를 판정한다.

이전 배치에서 다음 문제가 실측됐고, 이 요청서는 그것을 막기 위한 것이다.

| 이전 배치의 문제 | 실측 결과 |
|---|---|
| 마크다운 노트에 위키링크를 넣음 | 끊긴 링크 **3,079회**. 그중 **893회**는 템플릿 섹션 제목(`Shock classification` 등)이 링크로 걸린 것 |
| 요약·해석을 함께 제공 | 검증 안 된 해석은 **재검증 비용이 원문 정독보다 크다**. 실제 대조에서 9건 중 2건이 하향 판정됨 |
| README가 수집 상태를 실제보다 넓게 서술 | "BIS·BOJ 수집" 서술 vs 실제 원문 확보 **0건**. 5,330건을 전수 파싱해야 294건임이 확인됨 |
| 본문만 제공하고 표를 누락 | 어떤 논문에서 **본문과 표의 수치가 전부 불일치**하는 것이 발견됨. 표가 없으면 잡을 수 없다 |

**요약: 완성돼 보이는 산출물보다, 검증 가능한 원자료가 훨씬 가치 있다.**

---

## 1. 산출물 구조

```
staging/
├── manifest.jsonl            # 1행 = 1문서
├── raw/{id}.pdf              # 원문 PDF 원본
├── text/{id}.txt             # 전문 텍스트
├── tables/{id}_T01.txt       # 표 단위 개별 파일
│   {id}_T02.txt
└── COLLECTION-REPORT.md      # 수집 결과 보고 (§7)
```

- `{id}`는 파일명 안전 문자만 사용 (영숫자·언더스코어·하이픈). 공백·특수문자·한글 금지.
- 마크다운 분석 노트는 **만들지 않는다.** 위 4종이 전부다.

---

## 2. manifest.jsonl 스키마

문서 1건당 JSON 1행. 값이 없으면 빈 문자열 `""` 또는 `null`. **추정해서 채우지 않는다.**

```json
{
  "id": "BIS_WP_1123",
  "title": "원문 제목 그대로",
  "authors": "성명; 성명; 성명",
  "institution": "BIS",
  "series": "BIS Working Papers",
  "number": "1123",
  "year": "2024",
  "pub_date": "2024-03-15",
  "revision": "",
  "doc_type": "working_paper",
  "publication_status": "staff view",
  "peer_reviewed": false,
  "doi": "",
  "official_url": "https://www.bis.org/publ/work1123.htm",
  "pdf_url": "https://www.bis.org/publ/work1123.pdf",
  "text_status": "full",
  "pages": 48,
  "text_chars": 118432,
  "table_count": 7,
  "abstract_verbatim": "초록 원문 그대로. 번역·요약·교정 금지",
  "limitations_verbatim": "저자가 한계·향후과제를 쓴 문단 원문. 없으면 빈 문자열",
  "sha256": "파일 해시",
  "retrieved_at": "2026-08-14",
  "notes": "수집 중 특이사항"
}
```

### 필드 규칙

| 필드 | 규칙 |
|---|---|
| `doc_type` | `working_paper` / `journal_article` / `official_publication` / `bulletin` / `staff_note` / `speech` / `report` 중 하나 |
| `publication_status` | 기관 공식 견해인지 저자 개인 견해인지. PDF의 disclaimer 문구를 근거로 판정. 불명확하면 `""` |
| `peer_reviewed` | 워킹페이퍼·스태프노트는 `false`. 확실하지 않으면 `null` |
| **`text_status`** | **`full`**(전문 텍스트 레이어 정상) / **`ocr`**(스캔본을 OCR) / **`partial`**(일부만 추출) / **`none`**(원문 미확보) |
| `revision` | 개정본이면 `r1`·`r2` 등. PDF 파일명이나 표지에서 확인되는 경우만 |
| `abstract_verbatim` | **원문 그대로 복사.** 번역·요약·오탈자 교정 금지 |
| `limitations_verbatim` | "Limitations", "한계", "Caveats", "Future research" 절의 원문 |

**`text_status`는 이 매니페스트에서 가장 중요한 필드다.** 원문을 못 구했으면 반드시 `none`으로 적는다.

---

## 3. 수집 대상

### A. 최우선 — 기존 코퍼스의 미확보 원문

`Institutional-Macro-Corpus-B3-Hybrid.zip`의 `manifest/documents.jsonl`에 **공식 URL이 이미 보존돼 있으나 PDF가 없는 문서들**이다. 그 URL을 입력으로 사용하라.

| 순위 | 기관 / 시리즈 | 미확보 건수 | 비고 |
|---:|---|---:|---|
| **1** | **BIS / BIS Working Papers** | **536** | 최우선. 글로벌 유동성·은행 대차대조표·신용 축 |
| 2 | BIS / BIS Quarterly Review | 24 | |
| 3 | ECB / Working Papers · Research Bulletin · Economic Bulletin | 83 | |
| 4 | BOJ / BOJ Working Papers · BOJ Review | 168 | |
| 5 | Fed / IFDP | 175 | 국제금융. FEDS와 별개 시리즈 |
| 6 | Fed / FEDS Notes | 487 | |
| 7 | World Bank / Policy Research Working Paper | 2,629 | 아래 주제 필터 적용 |

**World Bank는 전수 수집하지 말 것.** 다음 키워드가 제목·초록에 있는 것만: `China`, `trade`, `supply chain`, `commodity`, `metal`, `copper`, `energy`, `industrial policy`, `capital flow`, `exchange rate`, `debt`, `financial stability`.

> 현재 코퍼스의 원문 확보 실태(참고): 총 5,330건 중 `public_downloaded` **294건(5.5%)**, 전부 Fed FEDS.
> BIS·ECB·BOJ·World Bank는 **0건**이다. IMF·OECD는 코퍼스에 아예 없다.

### B. 개별 지정 논문 — 유료라 확보 실패한 것

기관 구독 접근이 가능하면 확보한다. **불가능하면 우회하지 말고 `text_status: "none"`으로 기록**하고 사유를 `notes`에 적는다.

| 논문 | 출처 | 상태 |
|---|---|---|
| Swan, T.W. (1956), *Economic Growth and Capital Accumulation* | Economic Record 32(2), 334-361. DOI 10.1111/j.1475-4932.1956.tb00434.x | Wiley 유료. Unpaywall OA 없음 |
| Romer, P. (1986), *Increasing Returns and Long-Run Growth* | JPE 94(5), 1002-1037. DOI 10.1086/261420 | JPE 유료. OA 없음 |
| King, Plosser & Rebelo (1988), *Production, Growth and Business Cycles: I* | JME 21(2-3), 195-232. DOI 10.1016/0304-3932(88)90030-X | Elsevier 유료 |
| Barro, R. (1990), *Government Spending in a Simple Model of Endogenous Growth* | **JPE 98(5, Pt.2), S103-S125** — DOI 10.1086/261726 | NBER WP #2588 판본은 확보됨. **JPE 최종판**이 필요 |

### C. IMF·OECD

현재 코퍼스에 **0건**이다. 다음 시리즈의 2020년 이후 공개 원문을 metadata부터 수집한다.

- IMF: Working Papers, Global Financial Stability Report, World Economic Outlook
- OECD: Economic Outlook, Economics Department Working Papers

접근제한 문서는 우회하지 않는다.

---

## 4. 텍스트 추출 규격

1. **전문 추출.** 참고문헌·부록 포함. 잘라내지 않는다.
2. **레이어 있는 PDF**는 `pymupdf`(fitz) 등으로 직접 추출 → `text_status: "full"`
3. **스캔본**은 OCR 수행 → `text_status: "ocr"`. OCR 품질이 낮으면 `notes`에 명시
4. 추출 실패·부분 실패 시 있는 만큼 저장하고 `partial`
5. **원문 문자를 교정하지 않는다.** 수식이 깨져도, 오탈자가 있어도 그대로 둔다. 그 자체가 검증 대상이다
6. 인코딩은 **UTF-8**. 이전 배치에서 `Reserve's` → `Reserveâs` 같은 mojibake가 다수 발생했다

---

## 5. 표(Table) 추출 규격 — 가장 중요

**표는 별도 파일로 분리한다.** 이 요구가 이 작업에서 가장 가치가 높다.

`tables/{id}_T01.txt` 형식:

```
CAPTION: Table 7. Granger Causality Test Results
PAGE: 37
---
Null Hypothesis | F-statistic | p-value
RealFactor does not Granger-cause govt12m | 7.6236 | 0.0060
govt12m does not Granger-cause RealFactor | 0.0005 | 0.9996
ffer does not Granger-cause govt12m | 5.4596 | 0.0197
ffer does not Granger-cause govt36m | 0.8960 | 0.3700
---
NOTE: *** p<0.01, ** p<0.05, * p<0.1
```

- **캡션·페이지 번호를 반드시 포함**한다
- **모든 셀 값을 원문 그대로.** 반올림·단위 변환·재계산 금지
- 유의성 표기(`***`)와 표 하단 주석도 함께
- 표 구조가 복잡해 파싱이 어려우면 **그 페이지의 텍스트를 그대로** 넣고 `NOTE: 자동 파싱 실패, 원문 텍스트 그대로 첨부`라고 적는다

**왜 이렇게까지 요구하는가**: 검증 과정에서 어떤 논문의 본문 서술과 표의 수치가 전부 어긋난 사례가 나왔다. 본문은 "Level 자기충격 93.2%"라 썼는데 표는 97.70%였다. 표가 없으면 이런 오류를 잡을 수 없고, 잘못된 수치가 그대로 인용된다.

---

## 6. 금지 사항

각 항목에 이유를 붙인다. 이유를 알면 판단이 필요한 경계 상황에서도 방향이 맞는다.

| 금지 | 이유 |
|---|---|
| **요약·해석·인과 서술 작성** | 검증 안 된 해석은 재검증 비용이 원문 정독보다 크다. 실제로 하향 판정된 사례가 있다 |
| **대괄호 두 개 위키링크 사용** | 대상 시스템의 노드 이름을 알 수 없어 반드시 깨진다. 이전 배치에서 3,079회 발생 |
| **템플릿 섹션 제목을 링크로 감싸기** | `Shock classification`·`Transmission mechanism` 같은 문서 구조어가 링크가 되면 무의미한 허브 노드가 생긴다. 이전 배치 893회 |
| **초록·결론 번역 또는 다듬기** | 원문 대조가 불가능해진다 |
| **수치 반올림·단위 변환·재계산** | 원문의 오류인지 가공 중 발생한 오류인지 구분할 수 없게 된다 |
| **원문 미확보 문서의 내용 추정** | 가장 심각한 오염이다. 못 구했으면 `text_status: "none"`이 정답이다 |
| **frontmatter tags 부여** | 대상 시스템은 닫힌 태그 집합을 쓴다. 임의 태그는 제거 작업을 유발한다 |
| **접근제한·유료·로그인 문서 우회** | 준수 사항 |
| **확보율을 실제보다 높게 서술** | 이전 배치의 가장 큰 문제였다 |

---

## 7. COLLECTION-REPORT.md — 보고 형식

작업 종료 시 다음을 그대로 채운다. **실제 수치만 적는다.**

```markdown
# 수집 결과 보고

## 총계
- 시도한 문서 수:
- PDF 확보 성공:
- 그중 text_status = full:
- 그중 text_status = ocr:
- 그중 text_status = partial:
- PDF 확보 실패 (text_status = none):
- 표 추출 완료 문서 수 / 총 표 개수:

## 기관·시리즈별 확보율
| 기관 | 시리즈 | 시도 | 확보 | 확보율 |

## 확보 실패 사유별 분류
| 사유 | 건수 | 예시 URL |
(유료 / 로그인 필요 / 404 / 타임아웃 / robots 차단 / PDF 아님 / 기타)

## 알려진 문제
- 인코딩 손상이 확인된 문서:
- OCR 품질이 낮은 문서:
- 표 파싱에 실패한 문서:
- 중복으로 판단되는 문서 쌍:
- 개정본(revision)이 여러 개 발견된 문서:

## 하지 못한 것
(범위 안이었으나 완료하지 못한 항목을 숨기지 말고 전부 적는다)
```

---

## 8. 완료 조건 체크리스트

- [ ] `manifest.jsonl`의 모든 행이 스키마를 만족하고, `text_status`가 실제 상태와 일치한다
- [ ] `raw/`의 PDF 개수 = manifest에서 `text_status != "none"`인 행 수 **(이전 배치에서 1건 불일치가 있었다)**
- [ ] `text/`의 파일 개수가 위와 같다
- [ ] 표가 있는 문서는 `tables/`에 최소 1개 파일이 있고, `table_count`와 일치한다
- [ ] `abstract_verbatim`이 원문과 문자 단위로 같다 (번역·요약본이 아니다)
- [ ] 마크다운 분석 노트를 **만들지 않았다**
- [ ] 대괄호 두 개 링크가 산출물 어디에도 **없다**
- [ ] `COLLECTION-REPORT.md`의 수치가 실제 파일 개수와 일치한다
- [ ] 확보하지 못한 문서를 확보한 것처럼 쓰지 않았다

---

## 9. 우선순위 요약 — 시간이 부족하면 이 순서로

1. **BIS Working Papers 536편** — 원문 PDF + 텍스트 + 표
2. **§3-B의 개별 논문 4편** — 유료 접근이 되는 경우에만
3. ECB 83편 · BOJ 168편
4. Fed IFDP 175편
5. World Bank (주제 필터 적용)
6. IMF·OECD metadata 수집

**1번만 완수해도 충분히 가치가 있다.** 전체를 얕게 하는 것보다 1번을 규격대로 완결하는 쪽이 낫다.
