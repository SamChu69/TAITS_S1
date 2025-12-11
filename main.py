# main.py
# ============================================================
# TAITS – Taiwan Alpha Intelligent Trading System
# 主程式入口（世界級正式版）
# ============================================================

import os
import sys
import traceback
from pathlib import Path
import yaml

from engine.orchestrator import Orchestrator


# ------------------------------------------------------------
# 1. 啟動前：環境診斷（避免 cache 舊版本污染）
# ------------------------------------------------------------
def diagnose_environment():
    print("\n================ TAITS S1 環境自動診斷 ================")

    # [1] 顯示目前執行 main.py 的路徑
    print("[1] 目前已載入的模組（含路徑）")
    print(">>> __main__           ->", sys.modules["__main__"])
    print(">>> __file__           ->", __file__)

    # [2] 測試 MarkdownReportFormatter 是否能載入
    print("\n[2] MarkdownReportFormatter 實際載入檢查：")
    try:
        from engine.report_md_formatter import MarkdownReportFormatter
        print(">>> OK:", MarkdownReportFormatter)
    except Exception as e:
        print(">>> ERROR:", e)

    # [3] 搜尋 report_md_formatter.py 所在位置
    print("\n[3] 搜尋所有 'report_md_formatter.py'：")
    root_dir = Path(__file__).resolve().parent
    matches = list(root_dir.rglob("report_md_formatter.py"))
    if matches:
        for p in matches:
            print(">>> found:", p)
    else:
        print(">>> 未找到任何 report_md_formatter.py")

    # [4] 標記 .__pycache__（避免載入舊版本）
    print("\n[4] 檢查 __pycache__ 位置：")
    for p in root_dir.rglob("__pycache__"):
        print(">>> cache found:", p)

    print("建議：手動刪除所有 __pycache__，避免載入舊版本程式碼。")

    print("\n========================================================\n")


# ------------------------------------------------------------
# 2. 載入設定檔（config.yaml）
# ------------------------------------------------------------
def load_config():
    config_path = Path(__file__).resolve().parent / "config.yaml"
    if not config_path.exists():
        raise FileNotFoundError("找不到 config.yaml")

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return config


# ------------------------------------------------------------
# 3. 主執行流程
# ------------------------------------------------------------
def main():
    try:
        diagnose_environment()

        # Load config.yaml
        config = load_config()

        ticker = str(config.get("ticker", "2330"))
        start = str(config.get("start_date", "2024-01-01"))
        end = str(config.get("end_date", "2024-12-31"))

        print("========== TAITS S1 系統啟動 ==========")
        print(f"[Main] 執行標的：{ticker} / 區間：{start} -> {end}")

        orch = Orchestrator()
        result = orch.run(ticker, start, end)

        print("\n========== TAITS S1 系統結束 ==========\n")
        return result

    except Exception:
        print("\n[TAITS ERROR] 系統發生例外錯誤：")
        traceback.print_exc()
        return None


# ------------------------------------------------------------
# 4. 程式進入點
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
