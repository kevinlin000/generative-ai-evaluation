#!/usr/bin/env python3
"""
Ground truth comparison script.

Usage (after filling actual_returns_template.csv):
    python3 scripts/compute_ground_truth.py

Inputs:
    ground_truth/ai_predictions.csv       — AI forecasts (annual %)
    ground_truth/actual_returns_template.csv — actual 6-month returns (fill Actual_Return_6M column)

Output:
    ground_truth/comparison.csv           — verdict per (Scenario, Model)
"""

import csv
import os

ROOT = os.path.join(os.path.dirname(__file__), '..')
PREDICTIONS_CSV = os.path.join(ROOT, 'ground_truth', 'ai_predictions.csv')
ACTUALS_CSV     = os.path.join(ROOT, 'ground_truth', 'actual_returns_template.csv')
OUTPUT_CSV      = os.path.join(ROOT, 'ground_truth', 'comparison.csv')

VERDICT_THRESHOLD_PP = 5   # percentage points


def annual_to_6m(annual_pct: float) -> float:
    """Convert annual return % to 6-month return % (compound)."""
    r = annual_pct / 100
    return ((1 + r) ** 0.5 - 1) * 100


def verdict(expected_6m: float, actual_6m: float) -> str:
    diff = actual_6m - expected_6m   # positive = AI was too pessimistic
    if abs(diff) < VERDICT_THRESHOLD_PP:
        return 'Accurate'
    elif diff > 0:
        return 'Over-pessimistic'   # actual > expected
    else:
        return 'Over-optimistic'    # actual < expected


def load_predictions(path: str) -> dict:
    """Returns {(scenario, model): {optimistic, base, pessimistic, drawdown}}"""
    result = {}
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            key = (row['Scenario'], row['Model'])
            result[key] = {
                'optimistic':  float(row['Optimistic']),
                'base':        float(row['Base']),
                'pessimistic': float(row['Pessimistic']),
                'drawdown':    float(row['Max_Drawdown_Estimate']),
                'holding_1':   row['Holding_1'], 'pct_1': float(row['Pct_1']),
                'holding_2':   row['Holding_2'], 'pct_2': float(row['Pct_2']),
                'holding_3':   row['Holding_3'], 'pct_3': float(row['Pct_3']),
            }
    return result


def load_actuals(path: str) -> dict:
    """Returns {(scenario, model): [(pct, actual_return_6m), ...]}"""
    result = {}
    with open(path, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            sc, model = row['Scenario'], row['Model']
            raw = row.get('Actual_Return_6M', '').strip()
            if not raw:
                continue   # skip unfilled rows
            try:
                ret = float(raw)
            except ValueError:
                print(f"  [WARN] Cannot parse Actual_Return_6M='{raw}' for {sc}/{model}/{row['Ticker']}")
                continue
            key = (sc, model)
            result.setdefault(key, []).append((float(row['Pct']), ret))
    return result


def weighted_return(holdings: list) -> float:
    """holdings = [(pct, actual_return_6m), ...]
    Returns weighted average actual 6M return (%).
    Weights are proportional to Pct (need not sum to 100).
    """
    total_pct = sum(p for p, _ in holdings)
    if total_pct == 0:
        raise ValueError("Total percentage is 0")
    return sum(p * r for p, r in holdings) / total_pct


def main():
    # ── Load data ─────────────────────────────────────────────────────────────
    predictions = load_predictions(PREDICTIONS_CSV)

    if not os.path.exists(ACTUALS_CSV):
        print(f"ERROR: {ACTUALS_CSV} not found.")
        return

    actuals = load_actuals(ACTUALS_CSV)

    missing = [k for k in predictions if k not in actuals]
    if missing:
        print(f"[WARN] No actuals found for {len(missing)} combos (unfilled rows):")
        for sc, m in sorted(missing):
            print(f"       {sc} / {m}")

    # ── Compute & write ───────────────────────────────────────────────────────
    rows = []
    for (sc, model), pred in sorted(predictions.items()):
        if (sc, model) not in actuals:
            continue

        actual_6m = weighted_return(actuals[(sc, model)])

        # AI benchmark: pessimistic annual → 6M compound
        pess_6m    = annual_to_6m(pred['pessimistic'])
        base_6m    = annual_to_6m(pred['base'])
        opt_6m     = annual_to_6m(pred['optimistic'])
        drawdown   = pred['drawdown']

        diff_vs_pess = actual_6m - pess_6m   # + means reality beat pessimism
        verdict_str  = verdict(pess_6m, actual_6m)

        # Was actual worse than the max drawdown estimate?
        exceeded_drawdown = actual_6m < drawdown

        rows.append({
            'Scenario':         sc,
            'Model':            model,
            'Actual_6M_Return': round(actual_6m, 2),
            'AI_Pessimistic_Annual': pred['pessimistic'],
            'AI_Pessimistic_6M':    round(pess_6m, 2),
            'AI_Base_6M':           round(base_6m, 2),
            'AI_Optimistic_6M':     round(opt_6m, 2),
            'Diff_vs_Pessimistic':  round(diff_vs_pess, 2),
            'Verdict':          verdict_str,
            'Max_Drawdown_Est': drawdown,
            'Exceeded_Drawdown':exceeded_drawdown,
        })

    if not rows:
        print("No complete data to compute. Fill Actual_Return_6M in the template CSV first.")
        return

    fieldnames = [
        'Scenario', 'Model',
        'Actual_6M_Return',
        'AI_Pessimistic_Annual', 'AI_Pessimistic_6M',
        'AI_Base_6M', 'AI_Optimistic_6M',
        'Diff_vs_Pessimistic',
        'Verdict',
        'Max_Drawdown_Est', 'Exceeded_Drawdown',
    ]

    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✓ comparison.csv written ({len(rows)} rows)")
    print()

    # ── Console summary ───────────────────────────────────────────────────────
    print(f"{'Scenario':<10} {'Model':<10} {'Actual6M':>8} {'Pess6M':>8} {'Diff':>8}  {'Verdict'}")
    print("-" * 65)
    for r in rows:
        exceeded_flag = " ⚠️ drawdown exceeded" if r['Exceeded_Drawdown'] else ""
        print(
            f"{r['Scenario']:<10} {r['Model']:<10} "
            f"{r['Actual_6M_Return']:>8.2f}% "
            f"{r['AI_Pessimistic_6M']:>8.2f}% "
            f"{r['Diff_vs_Pessimistic']:>+8.2f}pp  "
            f"{r['Verdict']}{exceeded_flag}"
        )

    # Verdict summary
    from collections import Counter
    counts = Counter(r['Verdict'] for r in rows)
    print()
    print("=== Verdict Summary ===")
    for v, c in sorted(counts.items()):
        print(f"  {v}: {c} / {len(rows)}")

    exceeded = sum(1 for r in rows if r['Exceeded_Drawdown'])
    print(f"  Exceeded max drawdown estimate: {exceeded} / {len(rows)}")


if __name__ == '__main__':
    main()
