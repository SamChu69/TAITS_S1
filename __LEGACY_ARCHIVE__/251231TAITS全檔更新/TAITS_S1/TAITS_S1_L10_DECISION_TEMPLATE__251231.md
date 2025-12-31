# TAITS_S1｜L10 人類裁決模板（交易授權層）
版本：v1.0（251231）

> 定位：L10 = 你裁決與交易授權層（唯一決策中心）。
> 任何「下單/執行」只能在你授權後由執行層執行；本模板只是裁決記錄。

---

## A. 裁決標頭（必填）
- decision_id：
- report_id（對應 L9）：
- timestamp：
- 你的模式裁決（必選其一）：
  - NO_ACTION / BACKTEST / SIMULATION / PAPER / LIVE_SEMI / LIVE_AUTO

## B. 授權封套（Authorization Envelope）
- 有效期（start/end）：
- 最大單筆風險：
- 最大總曝險：
- 可交易標的範圍：
- 允許策略/禁止策略（若適用）：
- 觸發撤銷條件（必填）：

## C. 你給系統的指示（可選）
- 你要觀察的關鍵指標：
- 你要的更新頻率（L9）：
- 你要的告警條件（例如：跌破/突破）：

---

# L10 decision_record（Machine-Readable Schema｜最小集合）
```json
{
  "decision_id": "",
  "report_id": "",
  "timestamp": "",
  "mode": "NO_ACTION|BACKTEST|SIMULATION|PAPER|LIVE_SEMI|LIVE_AUTO",
  "authorization_envelope": {
    "valid_from": "",
    "valid_to": "",
    "max_single_trade_risk": null,
    "max_total_exposure": null,
    "universe": [],
    "strategy_allowlist": [],
    "strategy_blocklist": [],
    "revoke_conditions": []
  },
  "notes": null
}
```
