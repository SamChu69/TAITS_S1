# TAITS_S1｜L9 詳細投資報告模板（你可見）
版本：v1.0（251231）

> 定位：L9 = 詳細投資報告（你要看的主報告），含數據/圖形/價位建議/可追蹤版本。
> 注意：本模板不構成下單；下單/授權在 L10。

---

## A. 報告標頭（必填）
- report_id：
- symbol_id：
- report_version：
- time_range：
- regime_label（來自 L6）：
- gate_decision（來自 L7）：
- data_snapshot_id（來自 L3）：

## B. 一頁摘要（你快速判讀）
- 核心結論（3–5 點）：
- 主要風險（3–5 點）：
- 不確定性與需觀察的觸發條件：

## C. 數據與圖形（必含）
> 圖形由工程生成並引用；本報告負責解釋。
- 價格與趨勢圖：  
- 技術指標圖（例：均線/RSI/MACD）：  
- 籌碼/法人/融資融券彙總圖表：  
- 基本面關鍵指標表：

## D. 事件與消息（證據引用）
- 重要事件時間線（引用 EvidencePack）：
- 證據列表（evidence_id / source / timestamp / 摘要）：

## E. 進出場建議（Proposal，非下單）
- 進場區間（建議）：
- 出場區間（建議）：
- 停損/停利參考：
- 失效條件（何時這份報告不再適用）：

## F. 追蹤與更新策略（必含）
- 下一次更新條件（例如：regime 切換、重大事件、價格破位）：
- 與前版差異摘要（若 report_version > 1）：

---

# L9 Report Metadata（Machine-Readable Schema｜最小集合）
```json
{
  "report_id": "",
  "symbol_id": "",
  "report_version": 1,
  "time_range": {"start": "", "end": ""},
  "snapshot_id": "",
  "regime": {"label": "", "confidence": null},
  "gate": {"decision": "PASS|BLOCK|DOWNGRADE", "rule_refs": []},
  "evidence_refs": [],
  "proposal": {
    "entry_zone": null,
    "exit_zone": null,
    "stop_loss": null,
    "take_profit": null,
    "invalidations": []
  },
  "update_policy": {
    "next_update_triggers": [],
    "diff_from_prev": null
  }
}
```
