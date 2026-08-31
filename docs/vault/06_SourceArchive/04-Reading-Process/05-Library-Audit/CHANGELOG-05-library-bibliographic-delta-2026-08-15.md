# 05_Library 서지·원문 URL 증분 정정 — 2026-08-15

이 증분은 사용자가 제공한 `05_Library1.zip`의 399개 원본 노트를 기준으로 만들었다. **기존 볼트 전체를 덮어쓰지 말고**, 이 ZIP에 포함된 경로의 Markdown만 적용한다.

| 구분 | 결과 |
|---|---:|
| 기준 노트 | 399 |
| 기존 URL/DOI 결측 | 250 |
| 이번에 보수적으로 확정해 URL 또는 DOI를 추가한 결측 노트 | 171 |
| 추정 방지를 위해 미해결로 남긴 결측 노트 | 79 |
| 요청서 지정 11건과 관련해 수정된 고유 노트 | 12 |
| 실제 변경 Markdown 파일 | 183 |

## 적용 원칙

원문 제목·저자·연도와 URL 또는 DOI가 일치한 경우에만 `bibliographic_status: "official-record-verified"`와 `출처·서지 검증 (2026-08-15)`을 추가했다. 이는 **서지 레코드 대조**를 뜻하며, 기존 자동 생성 본문을 원문 전체 검토본으로 승격하지 않는다. 따라서 기존 `status: unverified`, `verified: ❌ 원문 미대조` 및 본문의 주장·수치 표시는 의도적으로 유지했다.

## 요청서 지정 정정

L3·L156의 제목에 `Revisited`를 복원했고, L44·L20·L48·L15·L192·L195·L199·L215·L218의 오연결 URL을 발행처 URL·DOI로 교체했다. L30도 기존 노트에 별도 `wrong_source_url` 플래그가 있어 제목·저자·연도·DOI를 발행처 페이지로 추가 대조했다. 근거는 `04-Reading-Process/05-Library-Audit/requested-11-bibliographic-corrections-2026-08-15.json`에 있다.

## 미해결 항목

`UNRESOLVED-URL-DOI-LOG.md`의 79건에는 그럴듯한 URL이나 DOI를 넣지 않았다. 후속 원문 확인 전까지 `source_url_missing: true` 상태를 유지한다.
