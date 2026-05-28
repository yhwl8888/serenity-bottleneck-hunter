#!/usr/bin/env python3
"""
Forward-test scorer for the Serenity bottleneck-hunter skill.

Reads forward_picks.csv (dated, rules-locked picks the skill produced), re-pulls
CURRENT prices via the unified price helper (`scripts/price.py`,EODHD优先→yfinance兜底),
computes return-since-entry, and writes a scored markdown report.

This is the ONLY methodologically clean validation (out-of-sample, no look-ahead /
survivorship) — contrast with the in-sample photonics "backtest".

Usage:
    python score_tracker.py                                    # 走 yfinance (美股OK)
    EODHD_API_KEY=xxxx python score_tracker.py                  # 走 EODHD(海外股推荐)

Console is often GBK on Windows -> we print ASCII-only summary and write the
full (Chinese) table to score_report.md in UTF-8.
"""
import csv, datetime, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
from price import fetch_history  # 共享数据源回退链

CSV_F = os.path.join(HERE, "forward_picks.csv")
OUT_F = os.path.join(HERE, "score_report.md")


def latest_close(sym):
    """Return (last_close, last_date, provider) or (None, None, None)。"""
    data, prov = fetch_history(sym, days=30)
    if data:
        return data[-1]["close"], data[-1]["date"], prov
    return None, None, None


def main():
    today = datetime.date.today()
    rows = list(csv.DictReader(open(CSV_F, encoding="utf-8")))
    scored = []
    for r in rows:
        cur, cur_date, prov = latest_close(r["eodhd_symbol"])
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
        r.update({"current": cur, "current_date": cur_date, "provider": prov,
                  "ret_pct": ret, "days_held": days})
        scored.append(r)

    # --- UTF-8 markdown report ---
    with open(OUT_F, "w", encoding="utf-8") as f:
        f.write(f"# 向前跟踪打分 (更新于 {today.isoformat()})\n\n")
        f.write("> 样本外验证:从记录日入场价到今日的真实涨跌(数据源:EODHD 优先→yfinance 兜底)。\n> 非投资建议。\n\n")
        f.write("| 记录日 | 主题 | 标的 | 档位 | 判定 | 入场价 | 现价 | 入场以来% | 持有天 | 数据源 | stage(入场时) |\n")
        f.write("|---|---|---|---|---|---|---|---|---|---|---|\n")
        for r in scored:
            f.write("| {record_date} | {theme} | {name} | {tier} | {skill_verdict} | "
                    "{entry_price} {currency} | {current} | {ret_pct} | {days_held} | "
                    "{provider} | {entry_stage} |\n".format(**r))

        def grp(pred):
            xs = [r["ret_pct"] for r in scored if r["ret_pct"] is not None and pred(r["skill_verdict"])]
            return round(sum(xs) / len(xs), 1) if xs else None
        avoid = grp(lambda v: ("AVOID" in v) or ("别追" in v))
        watch = grp(lambda v: ("观察" in v) and ("别追" not in v) and ("AVOID" not in v))
        f.write(f"\n**纪律检验**:标注 AVOID/别追 的均值 = {avoid}% ;标注 观察 的均值 = {watch}% 。\n")
        f.write("(若 AVOID 组之后跌得更多/涨得更少,说明'别追'的择时纪律有效。)\n")
        missing = [r for r in scored if r["current"] is None]
        if missing:
            f.write(f"\n**未拉到价格的标的**({len(missing)}):" +
                    ", ".join(r["eodhd_symbol"] for r in missing) +
                    " — 多为海外股,请设 `EODHD_API_KEY` 后重跑。\n")

    # --- ASCII summary ---
    ok = [r for r in scored if r["ret_pct"] is not None]
    print(f"scored {len(ok)}/{len(scored)} picks; report -> {OUT_F}")
    for r in scored:
        tag = "AVOID" if ("AVOID" in r["skill_verdict"] or "别追" in r["skill_verdict"]) else "WATCH"
        ret = r["ret_pct"] if r["ret_pct"] is not None else "NA"
        prov = r["provider"] or "no-data"
        print(f"  {r['eodhd_symbol']:14} ret={ret}%  days={r['days_held']}  [{tag}]  src={prov}")


if __name__ == "__main__":
    main()
