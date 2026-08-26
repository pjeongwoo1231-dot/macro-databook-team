"""의존성 없는 최소 xlsx 리더.

xlsx는 XML을 담은 zip이다. openpyxl/pandas를 요구하지 않으려고 필요한 만큼만 직접 읽는다.
이 도구는 공개 배포본이라 `pip install` 목록을 늘리지 않는 편이 낫다.

지원: 단일 시트의 셀 값 읽기(숫자·문자·공유문자열·날짜 시리얼).
미지원: 수식 재계산, 스타일, 병합셀 해석.
"""
from __future__ import annotations

import io
import re
import zipfile
from datetime import date, timedelta
from typing import Any

# 엑셀 날짜 시리얼의 기준일(1900 시스템). 1900년 윤년 버그 때문에 -2일 보정.
EXCEL_EPOCH = date(1899, 12, 30)


def _col_to_idx(ref: str) -> int:
    """'BC12' → 열 인덱스(0-based)."""
    n = 0
    for ch in ref:
        if not ch.isalpha():
            break
        n = n * 26 + (ord(ch.upper()) - 64)
    return n - 1


def _row_of(ref: str) -> int:
    m = re.search(r"\d+", ref)
    return int(m.group()) if m else 0


def serial_to_date(v: float) -> date | None:
    try:
        return EXCEL_EPOCH + timedelta(days=float(v))
    except Exception:
        return None


def read_sheet(data: bytes, sheet_index: int = 0) -> list[list[Any]]:
    """xlsx 바이트 → 행 리스트. 각 셀은 float | str | None."""
    zf = zipfile.ZipFile(io.BytesIO(data))

    shared: list[str] = []
    if "xl/sharedStrings.xml" in zf.namelist():
        xml = zf.read("xl/sharedStrings.xml").decode("utf-8", "replace")
        for si in re.findall(r"<si>(.*?)</si>", xml, re.S):
            shared.append("".join(re.findall(r"<t[^>]*>(.*?)</t>", si, re.S)))

    sheets = sorted(n for n in zf.namelist()
                    if n.startswith("xl/worksheets/sheet") and n.endswith(".xml"))
    if not sheets:
        return []
    xml = zf.read(sheets[min(sheet_index, len(sheets) - 1)]).decode("utf-8", "replace")

    rows: dict[int, dict[int, Any]] = {}
    for rm in re.finditer(r"<row[^>]*r=\"(\d+)\"[^>]*>(.*?)</row>", xml, re.S):
        rn = int(rm.group(1))
        cells: dict[int, Any] = {}
        for cm in re.finditer(r"<c([^>]*)>(.*?)</c>", rm.group(2), re.S):
            attrs, body = cm.group(1), cm.group(2)
            ref = re.search(r'r="([A-Z]+\d+)"', attrs)
            if not ref:
                continue
            ci = _col_to_idx(ref.group(1))
            typ = re.search(r't="(\w+)"', attrs)
            t = typ.group(1) if typ else "n"
            if t == "inlineStr":
                val: Any = "".join(re.findall(r"<t[^>]*>(.*?)</t>", body, re.S))
            else:
                vm = re.search(r"<v>(.*?)</v>", body, re.S)
                if not vm:
                    continue
                raw = vm.group(1)
                if t == "s":
                    idx = int(raw)
                    val = shared[idx] if 0 <= idx < len(shared) else ""
                elif t in ("str", "e"):
                    val = raw
                else:
                    try:
                        val = float(raw)
                    except ValueError:
                        val = raw
            cells[ci] = val
        if cells:
            rows[rn] = cells

    if not rows:
        return []
    out: list[list[Any]] = []
    width = max(max(c) for c in rows.values()) + 1
    for rn in sorted(rows):
        cells = rows[rn]
        out.append([cells.get(i) for i in range(width)])
    return out
