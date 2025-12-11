# engine/report_formatter.py
# ============================================================
# TAITS – Report Formatter（TXT / JSON 報告輸出器）
# 負責將 Orchestrator 的 result 轉成文字報告與 JSON 檔案
# ============================================================

from pathlib import Path
from typing import Dict, Any
from datetime import datetime
import json

import pandas as pd
import numpy as np


class ReportFormatter:
    """
    TAITS S1 報告輸出工具
    --------------------------------------------------------
    主要職責：
      1. 將整體 result 轉成「人類可讀」的 TXT 報告
      2. 將 result 轉成 JSON 檔（經過 JSON-safe 處理）
      3. 自動建立 output 目錄，並依 ticker + 時間命名檔案
    """

    def __init__(self) -> None:
        pass

    # --------------------------------------------------------
    # 對外主入口：同時輸出 TXT + JSON
    # --------------------------------------------------------
    def save_files(self, result: Dict[str, Any], output_dir: str) -> Dict[str, str]:
        """
        儲存 TXT + JSON 報告檔案。

        :param result: Orchestrator.run() 回傳的 dict
        :param output_dir: 輸出資料夾路徑
        :return: {"txt": <path>, "json": <path>}
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        ticker = result.get("ticker", "UNKNOWN")
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")

        txt_name = f"{ticker}_{ts}_TAITS_S1_Report.txt"
        json_name = f"{ticker}_{ts}_TAITS_S1_Report.json"

        txt_path = output_path / txt_name
        json_path = output_path / json_name

        # 產生文字報告
        txt_content = self.to_text(result)
        txt_path.write_text(txt_content, encoding="utf-8")

        # 產生 JSON 報告（經過 JSON-safe 轉換）
        json_dict = self.to_json_dict(result)
        json_path.write_text(
            json.dumps(json_dict, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        print(f"[ReportFormatter] TXT 報告已輸出：{txt_path}")
        print(f"[ReportFormatter] JSON 報告已輸出：{json_path}")

        return {
            "txt": str(txt_path),
            "json": str(json_path),
        }

    # --------------------------------------------------------
    # 文字報告（TXT）格式
    # --------------------------------------------------------
    def to_text(self, result: Dict[str, Any]) -> str:
        """
        將 result 轉成人類可讀的純文字報告。
        """

        ticker = result.get("ticker", "N/A")
        regime = result.get("regime", "N/A")
        strategies = result.get("strategies", [])
        agents = result.get("agents", [])
        final_signal = result.get("final_signal", {})
        price_df: pd.DataFrame = result.get("price_data", pd.DataFrame())

        lines = []
        append = lines.append

        append("===================================================")
        append(f" TAITS S1 報告 - {ticker}")
        append("===================================================\n")

        # 1. 總覽
        append("[1] 總覽 (Overview)")
        append(f"- 標的 (Ticker)：{ticker}")
        append(f"- 市場狀態 (Regime)：{regime}")
        append("")
        append("最終決策 (Final Decision)：")
        append(f"- Bias      ：{final_signal.get('final_bias', 'N/A')}")
        append(f"- Confidence：{final_signal.get('confidence', 0.0)}")
        append(f"- Reason    ：{final_signal.get('reason', 'N/A')}")
        append("\n---------------------------------------------------\n")

        # 2. 策略層
        append("[2] 策略層 (Strategies)")
        if not strategies:
            append("  (無策略輸出)")
        else:
            for s in strategies:
                name = s.get("name", "N/A")
                signal = s.get("signal", "N/A")
                conf = s.get("confidence", 0.0)
                reason = s.get("reason", "")
                append(f"· {name}: {signal}  (conf={conf})")
                append(f"  ↳ {reason}")
        append("\n---------------------------------------------------\n")

        # 3. Agents 層
        append("[3] Agents 層 (多智能體)")
        if not agents:
            append("  (無 Agents 輸出)")
        else:
            for a in agents:
                name = a.get("name", "N/A")
                bias = a.get("bias", "N/A")
                conf = a.get("confidence", 0.0)
                comment = a.get("comment", "")
                append(f"· {name}: {bias}  (conf={conf})")
                append(f"  ↳ {comment}")
        append("\n---------------------------------------------------\n")

        # 4. 價格摘要
        append("[4] 價格摘要 (最後 5 根 K 線)")
        if isinstance(price_df, pd.DataFrame) and not price_df.empty:
            last5 = price_df.reset_index().tail(5)
            # 簡易表格輸出
            cols = list(last5.columns)
            append("  " + " | ".join(str(c) for c in cols))
            for _, row in last5.iterrows():
                append("  " + " | ".join(str(row[c]) for c in cols))
        else:
            append("  (無價格資料)")
        append("\n---------------------------------------------------\n")

        append("[5] 結語")
        append("本報告由 TAITS S1 自動產生，僅供研究與教育用途，")
        append("不構成任何投資建議。")

        return "\n".join(lines)

    # --------------------------------------------------------
    # JSON 輸出（先轉成 JSON-safe dict）
    # --------------------------------------------------------
    def to_json_dict(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        將 result 轉成「可被 json.dumps() 序列化」的 dict。
        """

        return self._json_safe(result)

    # --------------------------------------------------------
    # JSON-SAFE 轉換工具（與 MD 版邏輯一致）
    # --------------------------------------------------------
    def _json_safe(self, obj: Any):
        """
        將任意物件轉成 JSON-safe 格式。
        支援：
          - pandas.DataFrame
          - pandas.Timestamp / numpy datetime
          - numpy scalar
          - list / tuple / set
          - dict（key 轉 str）
        其他無法處理者 → str(obj)
        """

        # DataFrame
        if isinstance(obj, pd.DataFrame):
            return obj.reset_index().to_dict(orient="records")

        # pandas Timestamp / numpy datetime
        if isinstance(obj, (pd.Timestamp, np.datetime64)):
            return str(obj)

        # numpy scalar
        if isinstance(obj, (np.integer, np.floating)):
            return obj.item()

        # list
        if isinstance(obj, list):
            return [self._json_safe(i) for i in obj]

        # tuple / set → list
        if isinstance(obj, (tuple, set)):
            return [self._json_safe(i) for i in obj]

        # dict
        if isinstance(obj, dict):
            new_dict = {}
            for k, v in obj.items():
                new_dict[str(k)] = self._json_safe(v)
            return new_dict

        # 其他型別直接嘗試 json.dumps
        try:
            json.dumps(obj)
            return obj
        except Exception:
            return str(obj)
