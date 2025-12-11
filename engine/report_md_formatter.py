# engine/report_md_formatter.py
# ============================================================
# TAITS – Markdown Report Formatter（Markdown 報告輸出器）
# 負責輸出可閱讀性極高、格式美觀的 Markdown 交易報告
# ============================================================

from pathlib import Path
from typing import Dict, Any, List
from datetime import datetime

import json
import pandas as pd
import numpy as np


class MarkdownReportFormatter:
    """
    產生 Markdown 版本的 TAITS 報告。
    --------------------------------------------------------
    輸出內容包含：
      1. 標的資訊
      2. 市場狀態（Regime）
      3. 策略層輸出
      4. Agents 層輸出
      5. 價格摘要（最後 5 根 K 線）
      6. JSON-safe Result（Debug 用）
    """

    def __init__(self):
        pass

    # --------------------------------------------------------
    # 對外 API：儲存 Markdown 檔案
    # --------------------------------------------------------
    def save_markdown(self, result: Dict[str, Any], output_dir: str) -> str:

        md_text = self.to_markdown(result)

        ticker = result.get("ticker", "UNKNOWN")
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{ticker}_{ts}_TAITS_S1_Report.md"

        output_path = Path(output_dir) / filename
        output_path.write_text(md_text, encoding="utf-8")

        print(f"[MarkdownReportFormatter] Markdown 報告已輸出：{output_path}")

        return str(output_path)

    # --------------------------------------------------------
    # Markdown Builder
    # --------------------------------------------------------
    def to_markdown(self, result: Dict[str, Any]) -> str:

        ticker = result.get("ticker", "N/A")
        regime = result.get("regime", "N/A")
        strategies = result.get("strategies", [])
        agents = result.get("agents", [])
        final_signal = result.get("final_signal", {})
        price_df: pd.DataFrame = result.get("price_data", pd.DataFrame())

        lines: List[str] = []
        append = lines.append

        # Header
        append(f"# TAITS S1 報告 — {ticker}")
        append("")
        append("---")
        append("")

        # =====================================================
        # 1. 總覽（Overview）
        # =====================================================
        append("## 1. 總覽（Overview）")
        append("")
        append(f"- **標的（Ticker）**：{ticker}")
        append(f"- **市場狀態（Regime）**：{regime}")
        append("")
        append("### 最終結論（Final Decision）")
        append(f"- **最終建議（Final Bias）**：{final_signal.get('final_bias', 'N/A')}")
        append(f"- **信心（Confidence）**：{final_signal.get('confidence', 0.0)}")
        append(f"- **理由（Reason）**：{final_signal.get('reason', 'N/A')}")
        append("")
        append("---")
        append("")

        # =====================================================
        # 2. 策略層（Strategies）
        # =====================================================
        append("## 2. 策略層（Strategy Layer）")
        append("")
        append("| 策略名稱 | 訊號 | 信心 | 說明 |")
        append("|---------|------|------|------|")

        for s in strategies:
            name = s.get("name", "N/A")
            signal = s.get("signal", "N/A")
            conf = s.get("confidence", 0.0)
            reason = str(s.get("reason", "")).replace("|", "｜")
            append(f"| {name} | {signal} | {conf} | {reason} |")

        append("")
        append("---")
        append("")

        # =====================================================
        # 3. Agents 層（Multi-Agent Layer）
        # =====================================================
        append("## 3. Agents 層（智慧代理層）")
        append("")
        append("| Agent | Bias | 信心 | 說明 |")
        append("|--------|------|------|------|")

        for a in agents:
            name = a.get("name", "N/A")
            bias = a.get("bias", "N/A")
            conf = a.get("confidence", 0.0)
            comment = str(a.get("comment", "")).replace("|", "｜")
            append(f"| {name} | {bias} | {conf} | {comment} |")

        append("")
        append("---")
        append("")

        # =====================================================
        # 4. 價格摘要（最後 5 根 K 線）
        # =====================================================
        append("## 4. 價格摘要（最後 5 根 K 線）")
        append("")

        if isinstance(price_df, pd.DataFrame) and not price_df.empty:
            clean_df = price_df.reset_index().tail(5)
            append(clean_df.to_markdown(index=False))
        else:
            append("（無價格資訊）")

        append("")
        append("---")
        append("")

        # =====================================================
        # 5. JSON 結構摘要（Debug 用）
        # =====================================================
        append("## 5. JSON 結構摘要（Debug 用）")
        append("")
        append("```json")
        safe_json = self._json_safe(result)
        append(json.dumps(safe_json, ensure_ascii=False, indent=2))
        append("```")
        append("")
        append("---")
        append("")
        append("（報告結束）")

        return "\n".join(lines)

    # --------------------------------------------------------
    # JSON-SAFE 轉換器（完全避免報錯）
    # --------------------------------------------------------
    def _json_safe(self, obj: Any):
        """
        將任何 TAITS result 安全轉成 JSON 可序列化格式。
        支援：
          - pandas.DataFrame → list(dict)
          - pandas.Timestamp → str
          - numpy scalar → Python 原生型別
          - list / tuple / set
          - dict key 統一轉 str
          - 其他 → str(obj)
        """

        # DataFrame
        if isinstance(obj, pd.DataFrame):
            return obj.reset_index().to_dict(orient="records")

        # Timestamp
        if isinstance(obj, (pd.Timestamp, np.datetime64)):
            return str(obj)

        # numpy scalar
        if isinstance(obj, (np.integer, np.floating)):
            return obj.item()

        # list
        if isinstance(obj, list):
            return [self._json_safe(i) for i in obj]

        # tuple/set → list
        if isinstance(obj, (tuple, set)):
            return [self._json_safe(i) for i in obj]

        # dict
        if isinstance(obj, dict):
            new_dict = {}
            for k, v in obj.items():
                new_dict[str(k)] = self._json_safe(v)
            return new_dict

        # 如果直接可轉 JSON，則直接返回
        try:
            json.dumps(obj)
            return obj
        except Exception:
            return str(obj)
