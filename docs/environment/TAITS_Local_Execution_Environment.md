# TAITS 本地執行環境基線（Local Execution Environment）

## 1. 使用者本機硬體規格

- CPU：Intel Core i7-8750H (6C / 12T, 2.20GHz)
- RAM：32 GB
- GPU：4 GB（僅顯示用途，非主要運算）
- Storage：SSD 約 1 TB
- OS：Windows 11 專業版（25H2）

## 2. 本機定位

本機定位為：

- 策略研發主機
- 多策略並行決策系統
- 日頻～分鐘級交易決策
- 零股 / 中低頻投資為主

## 3. 架構設計約束

TAITS 在本機環境下：

- 不設計高頻 Tick 級模型
- 不進行大型深度學習訓練
- 所有策略需可在 CPU + 32GB RAM 下穩定運行

## 4. 擴充策略原則

- 未來如需 NLP / 情緒模型，優先採用 API 或輕量模型
- GPU 升級僅在策略確定帶來邊際優勢後才評估
