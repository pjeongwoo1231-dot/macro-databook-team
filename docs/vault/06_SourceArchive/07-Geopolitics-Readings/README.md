# 지정학 판독 납품물 — 원본 보관

마누스 납품물 **원본 그대로**와, 그에 대한 **독립 검증 로그**를 같이 둔다.
검증은 납품물의 `validation_bNN.json`(자기보고)이 아니라
`_System/Analysis/manus_batch_verify.py`가 **입력 zip 원문에서 직접 대조**한 결과다.

> ⚠ **이 폴더에 있다는 것이 수납을 뜻하지 않는다.** 반려분도 기록으로 남긴다.
> 수납 여부는 아래 표와 [[지정학 판독 검증 대기열]] §1이 정한다.

| 배치 | 파일 | 상태 |
|---|---|---|
| b02 | `readings_b02.jsonl` · `processed_b02.csv` | ✅ **수납** |
| b02 | `authors_b02.csv` | 🔴 **0행 — 재작업 요청 중** |
| b04 | `authors_b04.csv` | ✅ **수납** |
| b04 | `readings_b04.jsonl` · `processed_b04.csv` | 🔴 **반려 — 인용은 진짜지만 claim 35/35가 템플릿.** 인용하지 말 것 |

- 검증 로그: `verify_bNN_independent.txt`
- 재작업 요청서: `Documents/마누스_배치/batch02_재작업요청_authors.md` · `batch04_반려_readings_재작업.md`
