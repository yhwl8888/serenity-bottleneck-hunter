# Serenity Bottleneck Hunter — a Claude Skill

> Given an investment **theme**, this skill reverse-maps the supply chain to surface **overlooked upstream "bottleneck" stocks** — distilled from the *publicly shared* methodology of X/Twitter trader **Serenity (@aleabitoreddit)**.
>
> 给定一个投资主题,复用 X 博主 **Serenity** 公开分享的"供应链瓶颈逆向映射"方法,独立挖出被市场忽视的**上游瓶颈股**(而非抄他已喊过的票)。

## ⚠️ Disclaimer / 免责声明
- **Not financial advice — educational / research use only.** / **非投资建议,仅供研究教育。**
- This project distills a **methodology** from Serenity's public posts. It does **not** redistribute his content and is **not affiliated with, sponsored by, or endorsed by** him. / 本项目只提炼其**公开方法论**,不转载其原始内容,与本人**无任何关联或背书**。
- Any "validation" inside is **logic-consistency + forward tracking**, NOT an audited performance record. Markets are risky; do your own research. / 文中"验证"为逻辑自洽 + 向前跟踪,**非经审计的业绩**。投资有风险,务必独立判断。

## What it does / 做什么
Theme → reverse supply-chain map → apply **9 "bottleneck archetypes"** → output a short list of overlooked upstream candidates with: thesis, archetype, valuation, entry-timing (Mode-A "buy early momentum, not the dip"), target/timeframe, and risks. The edge is being **early to the theme**, not chasing crowded names.

主题 → 逆向拆解供应链 → 套用 **9 大瓶颈原型** → 产出被忽视的上游候选 + 论点/估值/入场时机/目标价/风险。核心是**早于机构发现主题**,不追拥挤标的。

## Use / 用法
- **As a Claude skill**: drop this folder into your skills directory (or install the `.skill` bundle), then ask Claude e.g. *"用 Serenity 的方法分析 AI 数据中心电力 这个主题,给候选标的"*.
- Or just point Claude at `SKILL.md`.

## Structure / 结构
```
SKILL.md                         # 主流程:主题→挖股 7 步 + 两套择时 + 输出模板
reference/
  methodology.md                 # 方法论(理念/筛选清单/两套择时/回避清单/风险)
  supply-chain-and-archetypes.md # 元框架 + 产业链速查表 + 9 大瓶颈原型库
  example_commercial_space.md    # 完整 worked example(商业航天)
scripts/price.py                 # 价格/动量助手(EODHD 优先 → yfinance 兜底,绝不用 WebSearch 猜)
tracking/                        # 向前(样本外)验证:候选表 + 打分脚本
```

## Data / 数据
- **Price & timing**: `scripts/price.py` 自动按 **EODHD(`EODHD_API_KEY`)→ yfinance** 顺序回退。EODHD 全球覆盖最广(海外股推荐);yfinance 无需 key,美股 OK 但非美股常有 gap。**WebSearch 一律不用于抓价格——猜测视为流程错误**。
- **Fundamentals & bottleneck judgment**: web research per candidate — the skill's real edge is qualitative (is it a true single-source chokepoint?), which no data feed provides.

## Validation honesty / 验证说明
The only credible test is **forward / out-of-sample**: see `tracking/forward_picks.csv` (dated, rules-locked picks) + `tracking/score_tracker.py` (re-pulls prices later and scores them). Any in-sample "backtest" suffers look-ahead & survivorship bias and is **not** a performance claim.

## License / 协议
MIT (see `LICENSE`). Methodology credit: **Serenity (@aleabitoreddit)** — this is an independent, fan-made distillation of publicly shared ideas.
