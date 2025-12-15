# TAITS完整總架構 × 總流程 × 全資訊體系（MASTER VERSION）.md
（TAITS 歷史整合封存檔｜Reference Only｜禁止成為第二權威｜保留完整脈絡）

> 文件定位：歷史整合檔（Reference Only）
> 目的：保留你過去所有討論與整合痕跡，作為「知識資產」與「回溯參考」。
> 警告：本檔不得作為 TAITS 的「最高權威」來源，避免雙重真實來源（Double Source of Truth）。

---

## 0. 最高重要宣告（必讀，避免 TAITS 被你自己毀掉）

TAITS 的最高權威文件優先序如下（由高到低）：

1) TAITS_MASTER_ARCHITECTURE.md（憲章，Architecture Laws）
2) TAITS_Full_System_Architecture.md（十層分層藍圖）
3) TAITS_Architecture_and_Flow.md（資料流/決策流/事件流）
4) TAITS_Risk_and_Compliance.md（最高否決權）
5) TAITS_DataSources_Universe.md（資料來源全集）
6) TAITS_Strategy_Universe_Complete.md（策略宇宙：策略≠下單）
7) TAITS_Document_Index.md（導覽索引）

> 本檔（MASTER VERSION）僅為「歷史整合參考」，不可覆蓋上述文件內容。

---

## 1. 本檔存在的合理性（為什麼要保留）

你要求 TAITS 必須：
- 可長期演進、可擴充
- 不縮水、不刪掉討論成果
- 新對話能 100% 讀懂

但同時你也指出關鍵風險：
- GPT 對話不能分享
- 若不寫進檔案，新對話會「不知道」

因此本檔的設計是：
- 保留「歷史脈絡」與「你曾經要求的全部面向」
- 但用「權威順序」鎖死，避免任何人誤把本檔當第一權威

---

## 2. TAITS 的全資訊體系（你原本要求的「什麼會影響市場」都必須納入）

> 本章節只列「資訊版圖」與「可放的位置」，不取代各權威文件細節。

### 2.1 市場結構（Market Structure）
- 大盤指數、類股廣度、領漲梯隊、成交額結構
- 族群輪動、題材擴散、主流/次主流切換
- 市場深度與流動性（Liquidity/Depth）

對應權威：Architecture_and_Flow / DataSources / Regime

### 2.2 資金與籌碼（Flow/Positioning）
- 外資、投信、自營、主力行為
- 融資融券（Observe-only）
- 大戶持股變化、籌碼集中度（若可得）

對應權威：Strategy_Universe（CHIP/CREDIT）/ Risk

### 2.3 衍生品觀察（Derivatives Observation）
- 期貨：指數期貨/個股期貨（Observe-only）
- 選擇權：OI 壓力帶、Gamma/Vol 風險、結算釘住（Observe-only）
- 期現價差（Basis）、領先轉折、外資避險行為

對應權威：DataSources（TAIFEX）/ Strategy_Universe（DERIV）/ Risk

### 2.4 基本面（Fundamental）
- 財報、法說、重大訊息（MOPS）
- 產業供需、公司訂單、產品週期（可用多源交叉）

對應權威：DataSources（MOPS）/ Strategy_Universe（FUND/EVENT）

### 2.5 消息與情緒（News/Sentiment）
- 官方公告、主流媒體、社群/論壇（需可靠度）
- 題材敘事的形成、過熱、假消息風險

對應權威：DataSources（新聞/社群分級）/ Risk（事件旗標）

### 2.6 宏觀（Macro）
- 利率、匯率、通膨、景氣循環
- 國際市場連動（美股/美元/原物料等）

對應權威：DataSources（政府/宏觀）/ Regime

### 2.7 風控與極端情境（Risk/Extreme）
- 斷線、延遲、跳價、黑天鵝、交易制度變動
- KillSwitch / Observe-only / 降級策略

對應權威：Risk_and_Compliance（最高否決）

---

## 3. TAITS 的總流程（歷史整合版摘要，不取代 Flow 檔）

總流程（不可省）：
1) 取得市場資料 → 2) 標準化 → 3) 產生快照 Snapshot
4) 產生 FeatureVector（含 GMMA/CBL/威科夫/鮑迪克）
5) 判定 Regime（R1–R10）
6) 跑策略訊號（策略≠下單）
7) 融合與權重建議
8) Governance Gate（允許/降級/人工/禁止）
9) Risk Gate（PASS/SOFT/HARD/KILL）
10) 依你決定：只建議 / 半自動 / 全自動
11) 全程事件流與審計回放

權威對照：TAITS_Architecture_and_Flow.md

---

## 4. 本檔的使用方式（防呆）

你可以用本檔做三件事：
1) 回溯歷史脈絡（為什麼 TAITS 會長這樣）
2) 作為補充清單（檢查是否還有市場影響因子未寫入權威檔）
3) 作為未來擴充待辦池（Backlog）

你不可以用本檔做一件事：
- ❌ 把本檔內容當成「可直接覆蓋權威文件」的依據

---

## 5. 本檔封板宣告

本檔為「保留完整討論成果」用途存在。  
TAITS 的權威以其他文件為準，本檔不作為第一順位引用。
