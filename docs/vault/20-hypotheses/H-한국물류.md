---
type: hypothesis
status: open
created: 2026-08-24
updated: 2026-08-24
tags: [type/hypothesis, domain/intel]
---

# H-한국물류

> **한국 물동량이 **수출 통계보다 먼저** 대한해협 통항에 나타난다**

관세청 수출입 통계는 월 단위로 늦다. 대한해협 일별 통항이 그 선행 대리가 될 수 있다는 가설.
⚠ **아직 검정하지 않았다.** 통항과 수출액의 시차상관을 재기 전까지는 **대리지표 후보**일 뿐이다.
볼트 규칙: "X가 Y를 예고한다"는 **역방향 검정 F를 같이 적어야** 쓸 수 있다.

## 연결된 지표 (2개)

| 지표 | 소스 | 방향 규칙 |
|---|---|---|
| 대한해협 통항 | `portwatch` | ↑ contra / ↓ supports |
| 한국 원유 수입 (HS 2709) | `comtrade` | ↑ contra / ↓ supports |

## 자동 검증표

지표 노트가 수집될 때마다 `direction`이 갱신된다. **수집이 곧 검증이다.**

```dataview
TABLE label AS "지표", value AS "값", unit AS "단위", period AS "기간",
      direction AS "판정", retrieved AS "수집"
FROM "10-indicators"
WHERE contains(string(hypothesis), "H-한국물류")
SORT direction ASC, label ASC
```

### 지지 / 반박 집계

```dataview
TABLE length(rows) AS "건수"
FROM "10-indicators"
WHERE contains(string(hypothesis), "H-한국물류")
GROUP BY direction
```

### 판정 대기 (직전 값 없음)

```dataview
LIST label
FROM "10-indicators"
WHERE contains(string(hypothesis), "H-한국물류") AND direction = "unset"
```

## 읽는 규칙

- **`direction`은 방향 판정이지 크기 판정이 아니다.** 지지 3 : 반박 1이어도
  반박 쪽 한 건이 결정적일 수 있다 — **건수로 결론 내지 않는다**
- 초크포인트 통항은 **자기 표본 대비 변화**로만 읽는다.
  집계 방식 때문에 초크포인트 간 절대 수준 비교는 무의미하다
- 이 가설을 시황에 쓰려면 [[시황 분석 진입점]] §1에 규칙을 등록해야 한다.
  **등록하지 않은 것은 호출되지 않는다**

## 관련

[[시황 분석 진입점]] · [[지정학적 리스크]] · [[촉매 캘린더]]
