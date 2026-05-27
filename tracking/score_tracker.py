#!/usr/bin/env python3
"""
Forward-test scorer for the Serenity bottleneck-hunter skill.

Reads forward_picks.csv (dated, rules-locked picks the skill produced), re-pulls
CURRENT prices from EODHD, computes return-since-entry, and writes a scored
markdown report. This is the ONLY methodologically clean validation (out-of-sample,
no look-ahead/survivorship) — contrast with the in-sample photonics "backtest".

Usage:
    EODHD_API_KEY=xxxx python score_tracker.py
        -> reads forward_picks.csv (same dir), writes score_report.md (same dir)

Console is often GBK on Windows -> we print ASCII-only summary and write the
full (Chinese) table to score_report.md in UTF-8.
"""
import csv, os, sys, json, urllib.request, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "forward_picks.csv")
OUT = os.path.join(HERE, "score_report.md")
KEY = os.environ.get("EODHD_API_KEY", "").strip()
if not KEY:
    print("ERROR: set EODHD_API_KEY env var (do not hardcode the key).", file=sys.stderr)
    sys.exit(1)

def latest_close(sym):
    url = f"https://eodhd.com/api/eod/{sym}?api_token={KEY}&order=d&fmt=json"
    for _ in range(3):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                d = json.load(r)
                if isinstance(d, list) and d:
                    return d[0]["close"], d[0]["date"]
        except Exception:
            pass
    return None, None

today = datetime.date.today()
rows = list(csv.DictReader(open(CSV, encoding="utf-8")))
scored = []
for r in rows:
    cur, cur_date = latest_close(r["eodhd_symbol"])
    try:
        entry = float(r["entry_price"])
    except Exception:
        entry = None
    ret = round((cur / entry - 1) * 100, 1) if (cur and entry) else None
    try:
        d0 = datetime.date.fromisoformat(r["record_date"])
        days = (today - d0).days
    except Exception:
        days = None
    r.update({"current": cur, "current_date": cur_date, "ret_pct": ret, "days_held": days})
    scored.append(r)

# --- write full UTF-8 markdown report ---
with open(OUT, "w", encoding="utf-8") as f:
    f.write(f"# 向前跟踪打分 (更新于 {today.isoformat()})\n\n")
    f.write("> 样本外验证:从记录日入场价到今日的真实涨跌(EODHD)。非投资建议。\n\n")
    f.write("| 记录日 | 主题 | 标的 | 档位 | 判定 | 入场价 | 现价 | 入场以来% | 持有天 | stage(入场时) |\n")
    f.write("|---|---|---|---|---|---|---|---|---|---|\n")
    for r in scored:
        f.write("| {record_date} | {theme} | {name} | {tier} | {skill_verdict} | "
                "{entry_price} {currency} | {current} | {ret_pct} | {days_held} | {entry_stage} |\n".format(**r))
    # discipline check: did "AVOID/别追" picks underperform "观察" picks?
    def grp(pred):
        xs = [r["ret_pct"] for r in scored if r["ret_pct"] is not None and pred(r["skill_verdict"])]
        return round(sum(xs) / len(xs), 1) if xs else None
    avoid = grp(lambda v: ("AVOID" in v) or ("别追" in v))
    watch = grp(lambda v: ("观察" in v) and ("别追" not in v))
    f.write(f"\n**纪律检验**:标注 AVOID/别追 的均值 = {avoid}% ;标注 观察 的均值 = {watch}% 。\n")
    f.write("(若 AVOID 组之后跌得更多/涨得更少,说明'别追'的择时纪律有效。)\n")

# --- ASCII summary to stdout ---
ok = [r for r in scored if r["ret_pct"] is not None]
print(f"scored {len(ok)}/{len(scored)} picks; report -> {OUT}")
for r in scored:
    print(f"  {r['eodhd_symbol']:14} ret={r['ret_pct']}%  days={r['days_held']}  [{ 'AVOID' if ('AVOID' in r['skill_verdict'] or '别追' in r['skill_verdict']) else 'WATCH'}]")
