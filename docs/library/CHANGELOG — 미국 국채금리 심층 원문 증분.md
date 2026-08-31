# CHANGELOG — 미국 국채금리 심층 원문 증분

- **증분 ID:** `us-treasury-yields-2026-08-15`
- **기준일:** 2026-08-15 GMT+9
- **대상 주제:** 미국 국채금리, term premium, 재정·발행, repo·basis trade, NBFI, 시장기능
- **병합 원칙:** 기존 Obsidian 볼트의 파일을 삭제하거나 일괄 교체하지 않습니다. 이 ZIP의 파일만 기존 볼트 루트에 **증분으로 추가**하고, 아래의 기존 노트 변경은 병합 전 사본을 보관한 뒤 문맥을 확인해 반영합니다.

## 요약

이번 증분은 2025~2026년의 Fed·뉴욕연은·미 재무부·CBO·BIS·IMF·NBER·FSB 공식 원문 **16건**을 재검토해 작성했습니다. 이 중 BIS *Annual Economic Report 2026, Chapter II*와 IMF *Global Financial Stability Report, April 2026*은 기존 2024~2026 세트에 이미 포함돼 있어, 기존 33건과의 **순증은 14건**, 2024~2026년 verified-primary-source 집계는 **47건**입니다.

## 추가 파일

| 경로 | 종류 | 내용 |
|---|---|---|
| `obsidian-package/01-Events/US-Treasury-Yield-Issues-2026.md` | 사건 노트 | 2008~09, 2020, 2022~23, 2024~26의 역사적 연결과 입문용 읽기 경로 |
| `obsidian-package/02-Mechanisms/US-Treasury-Yields-2026-Mechanism-Map.md` | 메커니즘 지도 | 공급충격·term premium·발행·repo·NBFI·실물·국제금융 전파 |
| `obsidian-package/03-Sources/US-Treasury-Yields-2026-Core-Source-Summary.md` | 핵심 출처 요약 | 직접 열람한 16건의 원문, 2026-08-13 수익률 곡선, 해석·한계 |
| `obsidian-package/04-Reading-Process/US-Treasury-Yields-File-Verification.md` | 검증표 | PDF·HTML 15개 원문 파일 형식·페이지·텍스트 추출 검사 |
| `obsidian-package/05-Primary-PDFs/US-Treasury-Yields-2026/` | 원문 보관 | 보존 성공한 공식 PDF·HTML 15개 |

## 기존 파일의 증분 변경

| 경로 | 변경 | 목적 | 병합 방법 |
|---|---|---|---|
| `obsidian-package/00-Start/Macro-Financial-Crisis-MOC.md` | `updated` 날짜와 ‘미국 국채금리 심층 원문 세트’ 섹션 추가 | 메인 읽기 경로 연결 | 기존 노트의 해당 섹션에 추가 문단만 병합 |
| `obsidian-package/02-Mechanisms/2019-2021-Comparative-Mechanism-Map.md` | 10개 미해결 개별 문헌 링크를 검증된 `2019-2021-Core-Source-Summary` 앵커 링크로 정정 | 내부 링크 무결성 | 표의 supporting sources 링크만 정정 |
| `obsidian-package/02-Mechanisms/2024-2026-Comparative-Mechanism-Map.md` | ‘미국 국채금리 심층 연결’ 섹션 추가 | 2024~26 국채·NBFI·재정 축을 새 세트와 연결 | 새 소절만 추가 |
| `obsidian-package/03-Sources/2024-2026-Core-Source-Summary.md` | 직접검토 집계 33→47, 심층 원문 세트 설명 추가 | 중복 제외 원칙과 순증 14건을 명시 | 집계 문장·새 소절만 업데이트 |
| `obsidian-package/04-Reading-Process/Source-Selection-and-Reading-Log.md` | 미국 국채금리 16건의 검증 표와 중복 집계 설명 추가 | 출처·직접열람·보존 한계 기록 | 문서 끝에 섹션을 추가 |
| `obsidian-package/03-Sources/BIS-2009-79th-Annual-Report.md` 등 기존 8개 노트 | `reading_scope` YAML 메타데이터 추가 | strict primary 검증의 기존 메타데이터 누락 해소 | frontmatter에 행 하나만 추가 |

## 검증 결과

| 검사 | 결과 |
|---|---|
| 새 원문 PDF·HTML 파일 검사 | PDF 8건 페이지·텍스트 추출 성공, HTML 7건 구조 확인 |
| CBO 원문 | 공식 완전 HTML 직접 열람. 서버 403으로 로컬 자동 보존만 제한 |
| Obsidian 내부 wiki-link | 미해결 대상 0건 |
| `primary_text_read` 메타데이터 | `reading_scope` 누락 0건 |
| 원문 검증 상태 | 16건 모두 `verified-primary-source`; 제목·URL만 확인한 후보는 포함하지 않음 |

## 제외 및 한계

CBO 보고서는 원문 전문을 직접 열람했으나 자동 다운로드가 HTTP 403으로 제한되어 로컬 원문 폴더에는 넣지 못했습니다. 이는 원문을 읽지 않았다는 뜻이 아니며, `US-Treasury-Yields-2026-Core-Source-Summary.md`와 공식 URL에 검증 범위·제약을 명시했습니다. Working Paper와 FEDS Note의 결과는 저자 연구이며 기관의 확정 정책입장 또는 동료심사 완료의 인과결론으로 읽지 않습니다.

## 무결성

증분 ZIP 내부에는 `SHA256SUMS`를 동봉하며, 외부에는 동일 ZIP의 SHA-256 해시 파일을 제공합니다. 병합 전 `SHA256SUMS`와 외부 `.SHA256`을 검증하고, `unzip -tq` 검사에 성공한 뒤 적용하십시오.
