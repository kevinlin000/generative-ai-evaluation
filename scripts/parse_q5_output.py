#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluate AI JSON output compliance for Q5b responses.
Usage: python scripts/parse_q5_output.py q5_outputs/*.json
"""
import json
import sys
from pathlib import Path

REQUIRED_KEYS = [
    "timestamp",
    "overall_risk_score",
    "asset_allocation",
    "expected_annual_return",
    "max_drawdown_estimate",
    "rebalance_trigger",
]


def evaluate(file_path, expected_amount=800000):
    text = Path(file_path).read_text()
    score = 0
    issues = []

    # 檢查 1：可不可以直接 parse
    try:
        data = json.loads(text)
        score += 3
    except json.JSONDecodeError as e:
        issues.append(f"JSON parse failed: {e}")
        # 試著去除 markdown 標記再 parse
        cleaned = text.replace("```json", "").replace("```", "").strip()
        try:
            data = json.loads(cleaned)
            issues.append("Note: markdown stripped before parse (-1 點)")
            score += 1
        except Exception:
            return {"score": 0, "issues": issues, "data": None}

    # 檢查 2：必要欄位是否齊全
    missing = [k for k in REQUIRED_KEYS if k not in data]
    if not missing:
        score += 2
    else:
        issues.append(f"Missing keys: {missing}")

    # 檢查 3：金額加總
    if "asset_allocation" in data and isinstance(data["asset_allocation"], list):
        total = sum(item.get("amount_twd", 0) for item in data["asset_allocation"])
        if total == expected_amount:
            score += 2
        else:
            issues.append(f"amount_twd sum = {total}, expected {expected_amount}")

    # 檢查 4：百分比加總
    if "asset_allocation" in data and isinstance(data["asset_allocation"], list):
        pct = sum(item.get("percentage", 0) for item in data["asset_allocation"])
        if abs(pct - 100) < 0.01:
            score += 2
        else:
            issues.append(f"percentage sum = {pct}, expected 100")

    # 檢查 5：型別正確性
    if "overall_risk_score" in data and isinstance(data["overall_risk_score"], int):
        score += 1

    return {"score": score, "max": 10, "issues": issues, "data": data}


if __name__ == "__main__":
    for path in sys.argv[1:]:
        result = evaluate(path)
        print(f"\n{path}: {result['score']}/{result['max']}")
        for issue in result["issues"]:
            print(f"  - {issue}")
