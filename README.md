# TAITS – Taiwan Alpha Intelligence Trading System  
台灣阿爾法智能交易系統

---

## 專案定位（Project Positioning）

**TAITS** 是一套為 **台灣市場（TWSE / TPEX）** 設計的  
**系統級量化交易母體（Trading System Canon）**。

本專案的核心不是單一策略、不是回測工具、也不是教學範例，  
而是一套具備以下特性的長期演進系統：

- 架構先行（Architecture-first）
- 治理高於策略（Governance > Strategy）
- 風控與合規可否決一切（Risk / Compliance First）
- 可審計、可回放、可中斷再續
- AI 僅為輔助角色，非唯一真理

---

## 專案狀態（Current Status）

- 本 Repo 為 **Canon-first 重建版本**
- 所有歷史內容已隔離（非刪除）
- 目前僅存放「已確認、可作為權威依據」的文件
- **尚未進入程式實作階段（Phase 5 未啟動）**

---

## 最高權威文件（Canonical Authority）

本專案所有設計、流程、策略、AI 行為，  
**一律以以下文件為最高依據**：

### Governance（治理）
- `docs/governance/TAITS_AI_最終完整規則全集__251217.md`
- `docs/governance/TAITS_AI_自動審查Checklist__251217.md`

### Architecture / Flow（架構與流程）
- `docs/architecture/TAITS_最新總架構__251217.md`
- `docs/architecture/TAITS_最新總流程__251217.md`

### Strategy Governance（策略治理）
- `docs/strategies/TAITS_最新策略總覽與治理__251217.md`

### Cross-layer Specification（跨層細節）
- `docs/TAITS_最新細節規格彙編__251217.md`

📌 **任何與上述文件衝突的內容，均視為無效。**

---

## Repo 使用原則（重要）

- 本 Repo 不是雜物倉庫
- 不接受未經治理審查的新增檔案
- 不接受未經確認的策略或流程
- 所有新內容必須符合：
  - Only-Add 原則
  - 可審計 / 可回放
  - 不破壞既有 Canon

---

## 舊資料處理方式（Legacy）

- 所有舊檔案已集中於 `__LEGACY_ARCHIVE__/`
- 該資料夾已被 Cursor / AI 忽略
- 舊內容僅作歷史保留，不參與當前設計

---

## 備註

- 本專案以 **股票（STOCK）× 零股（odd-lot）** 為當前唯一啟用範圍
- 券商 API 以 **富邦 TradeAPI** 為主要設計對象
- 其他產品與交易方式僅作制度預留，尚未啟用

---

> **TAITS 的目的不是「跑得快」，  
而是「每一步都能被完整解釋」。**
