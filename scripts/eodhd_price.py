#!/usr/bin/env python3
"""
EODHD price/momentum helper for the Serenity bottleneck-hunter skill.

Purpose: give the skill PRICE CONTEXT for a candidate ticker so it can judge
"Mode A" entry timing (theme igniting / early uptrend — NOT 'wait for a dip').
This skill's EODHD plan only covers PRICE data (eod/real-time/search/symbol-list);
fundamentals/screener/calendar are NOT available -> get valuation/growth via web research.

Usage:
    EODHD_API_KEY=xxxx python eodhd_price.py AXTI.US [SIVE.ST IQE.LSE ...]

Outputs one JSON object per ticker with: last close, 6-mo range position,
% off 6-mo high, returns (1m/3m), SMA50 relation, and a coarse "stage" label.
"""
import json, os, sys, urllib.request, datetime

KEY = os.environ.get("EODHD_API_KEY", "").strip()
if not KEY:
    print("ERROR: set EODHD_API_KEY env var (do not hardcode the key).", file=sys.stderr)
    sys.exit(1)

END = datetime.date.today().isoformat()
FROM = (datetime.date.today() - datetime.timedelta(days=400)).isoformat()

def fetch(sym):
    url = f"https://eodhd.com/api/eod/{sym}?api_token={KEY}&from={FROM}&to={END}&period=d&fmt=json"
    for _ in range(3):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                return json.load(r)
        except Exception as e:
            err = str(e)
    return {"error": err}

def analyze(sym):
    d = fetch(sym)
    if isinstance(d, dict) or not d:
        return {"ticker": sym, "error": str(d)[:120]}
    closes = [x["close"] for x in d]
    last = closes[-1]
    w6 = d[-126:] if len(d) >= 126 else d              # ~6 trading months
    lo6 = min(x["low"] for x in w6); hi6 = max(x["high"] for x in w6)
    rng_pos = round((last - lo6) / (hi6 - lo6) * 100) if hi6 > lo6 else 50
    off_high = round((last / hi6 - 1) * 100, 1)
    sma50 = sum(closes[-50:]) / min(50, len(closes))
    r1m = round((last / closes[-21] - 1) * 100, 1) if len(closes) > 21 else None
    r3m = round((last / closes[-63] - 1) * 100, 1) if len(closes) > 63 else None
    up = last > sma50
    # stage heuristic — now weights 1-MONTH momentum + range position, not just 3-month.
    # Dogfood lesson: 长电 +99%/1m & 5N+ +44%/1m were wrongly tagged "early" when only 3m was used.
    hot_1m = (r1m is not None and r1m > 40)            # +40%+ in a month = already hot
    at_top = (rng_pos >= 95 and (r3m or 0) > 30)       # pinned at 6mo high after a real run
    if (r3m is not None and r3m > 120) or hot_1m or at_top:
        stage = "extended/parabolic (already ran hot -> late for Mode A; DON'T chase, wait for pullback)"
    elif up and r3m is not None and 5 < r3m <= 120 and not hot_1m:
        stage = "early-uptrend (reasonable Mode-A entry: theme igniting, not yet overextended)"
    elif not up and r3m is not None and r3m < -10:
        stage = "downtrend/basing (only Mode B 'buy the dip' if catalyst is non-material)"
    else:
        stage = "range/neutral"
    return {"ticker": sym, "last": round(last, 2), "range_pos_6mo_pct": rng_pos,
            "pct_off_6mo_high": off_high, "ret_1m_pct": r1m, "ret_3m_pct": r3m,
            "above_sma50": up, "stage": stage}

if __name__ == "__main__":
    syms = sys.argv[1:] or []
    if not syms:
        print("usage: EODHD_API_KEY=xxx python eodhd_price.py TICKER.EXCH [...]", file=sys.stderr); sys.exit(1)
    for s in syms:
        print(json.dumps(analyze(s), ensure_ascii=False))
