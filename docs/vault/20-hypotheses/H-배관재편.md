---
type: hypothesis
status: open
created: 2026-08-24
updated: 2026-08-24
tags: [type/hypothesis, domain/intel]
---

# H-배관재편

> **중동 해상운송 의존이 줄고 **미주·파이프라인 경로로 재편**되는 중이다**

원유·가스 물류가 호르무즈 같은 해상 초크포인트에서 벗어나
미국 수출·육상 파이프라인 쪽으로 옮겨가고 있다는 가설.

**참이면 보이는 것**: 호르무즈 통항·탱커 용량 감소, 미국 원유·가스 수출 증가,
중국의 중동산 수입 감소.
**거짓이면**: 호르무즈가 정상 수준으로 복귀하고 미국 수출이 정체한다.

## 연결된 지표 (5개)

| 지표 | 소스 | 방향 규칙 |
|---|---|---|
| 호르무즈 통항 | `portwatch` | ↑ contra / ↓ supports |
| 호르무즈 탱커 용량 | `portwatch` | ↑ contra / ↓ supports |
| 미국 원유 수출 | `eia_v2` | ↑ supports / ↓ contra |
| 미국 천연가스 수출 | `eia_v2` | ↑ supports / ↓ contra |
| 중국 원유 수입 (HS 2709) | `comtrade` | ↑ contra / ↓ supports |

## 자동 검증표

지표 노트가 수집될 때마다 `direction`이 갱신된다. **수집이 곧 검증이다.**

```dataview
TABLE label AS "지표", value AS "값", unit AS "단위", period AS "기간",
      direction AS "판정", retrieved AS "수집"
FROM "10-indicators"
WHERE contains(string(hypothesis), "H-배관재편")
SORT direction ASC, label ASC
```

### 지지 / 반박 집계

```dataview
TABLE length(rows) AS "건수"
FROM "10-indicators"
WHERE contains(string(hypothesis), "H-배관재편")
GROUP BY direction
```

### 판정 대기 (직전 값 없음)

```dataview
LIST label
FROM "10-indicators"
WHERE contains(string(hypothesis), "H-배관재편") AND direction = "unset"
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
