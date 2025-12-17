# 📘 TAITS_Architecture_Slimming_Audit.md
## TAITS 架構瘦身檢查（Slimming Audit）

---

## 0. 文件定位

本文件為 TAITS 的「結構化瘦身檢查」。目標不是刪內容，而是：
- 降低重複文件
- 降低概念重覆描述
- 增加索引與責任邊界清晰度
- 降低未來維護成本與誤用風險

原則：
- 任何涉及 Regime / Risk / 否決權 的文件：不得瘦身成模糊摘要
- 可瘦身的，通常是「重複敘述」而不是「功能」

---

## 1. 瘦身總原則（必遵守）

### P1｜優先「索引化」而非「刪除」
若兩份文件談同一主題：
- 保留一份為主規格（SPEC）
- 另一份改為索引（INDEX）或引用（REF），避免重寫

### P2｜層級不同，不合併
例如：
- Architecture（架構）與 Operations（日常流程）不得合併
- Risk Gate（否決）與 Evidence（證據）不得混寫

### P3｜一個概念只能有一個「權威定義」
例如：
- Time Advantage 的核心定義只能在一處出現（其他文件引用）
- MR-0~MR-3 的定義只能在一處出現（其他文件只引用）

---

## 2. 文件分類與建議定位（建議）

- [ARCH] 架構骨幹（不可動）
- [GOV] 治理規範（少動）
- [OPS] 操作流程（可調）
- [REF] 清單/宇宙/資料庫（可擴充）
- [SPEC] 規格主文（權威定義）

---

## 3. 重複/相近主題掃描與處置建議（核心）

### 3.1 Dual-Track / Time Advantage / Playbook
可能重疊點：
- 都會提到：Explore/Exploit、Trade/Wait/No Trade、避免早下注

建議：
- 保留「權威定義」：TAITS_Dual_Track_Decision_Architecture.md（SPEC）
- 保留「時間護城河」：TAITS_Time_Advantage_Framework.md（SPEC）
- 保留「單頁入口」：TAITS_Single_Page_Playbook.md（OPS/入口頁）
- 其他提到雙軌/時間優勢者：改為引用，不再重寫定義

瘦身方式：
- 在所有文件中，用「引用段」取代重複段落（不刪功能）

---

### 3.2 Wyckoff Framework vs Wyckoff Rule Matrix
可能重疊點：
- 都談威科夫行為與定位

建議：
- TAITS_Wyckoff_Market_Structure_Framework.md：保留為主規格（SPEC）
- TAITS_Wyckoff_Explore_Exploit_Rule_Matrix.md：保留為操作對照（OPS/矩陣）
- 不合併（層級不同）：一份講定位，一份講可執行規則

瘦身方式：
- Framework 文件不再列完整對照表，只引用 Matrix

---

### 3.3 Manipulation Risk Framework vs Checklist
可能重疊點：
- 風險等級定義與行為例子

建議：
- TAITS_Market_Manipulation_Risk_Framework.md：主規格（SPEC，權威定義 MR 等級）
- TAITS_Market_Manipulation_Risk_Checklist.md：檢查清單（OPS）
- 不合併（權威定義 vs 可勾選操作）

瘦身方式：
- Checklist 中不重寫 MR 定義，只引用 Framework 的 MR 定義段落（保留勾選規則）

---

### 3.4 Strategy Universe Mapping vs Dual-Track Strategy Governance vs Multi-Lane
可能重疊點：
- 都談「策略如何被管起來」

建議：
- TAITS_Strategy_Universe_Mapping_to_Dual_Track.md：策略宇宙角色定位（GOV）
- TAITS_Dual_Track_Strategy_Governance.md：策略治理規則（GOV）
- TAITS_Multi-Lane_Decision_Architecture.md：決策風格線架構（ARCH/GOV 交界）
- 不建議合併：因為「策略治理」與「決策風格線」是不同抽象層

瘦身方式：
- 在 Multi-Lane 文件中避免重述策略分群細節，改成指向治理文件

---

### 3.5 Risk Blind Spot Coverage Map vs Daily/Weekly Procedure
可能重疊點：
- 都談「避免被割」

建議：
- TAITS_Risk_Blind_Spot_Coverage_Map.md：風險全景地圖（GOV/索引）
- TAITS_Daily_Weekly_Risk_Check_Procedure.md：日常流程（OPS）
- 不合併：地圖是設計視角，流程是操作視角

瘦身方式：
- 流程文件只引用地圖的風險分類（R1~R8），不重寫原因與論述

---

## 4. 不可瘦身清單（Hard-Keep）

以下屬於「系統安全與一致性」核心，禁止刪減為摘要：

- TAITS_Risk_and_Compliance.md（最高否決權）
- TAITS_Market_Manipulation_Risk_Framework.md（MR 定義）
- TAITS_Dual_Track_Decision_Architecture.md（決策結構）
- TAITS_Single_Page_Playbook.md（唯一入口頁）
- 資料源宇宙與 Validator 規格（資料一致性基礎）

---

## 5. 建議新增的「索引型文件」以降低重複

為防止文件越來越多、內容重寫，建議新增或強化：

1) TAITS_Architecture_Layer_Map.md（已提供）
2) TAITS_Decision_Core_Inputs_Index.md（建議）
   - 列出 Decision Core 唯一允許的輸入項目（Regime、MR、Evidence、策略群組等）
   - 任何新模組若要進 Decision Core，必須先進索引清單

---

## 6. 一次性瘦身動作清單（建議執行順序）

1) 先定義每份文件的標籤：[ARCH]/[GOV]/[OPS]/[REF]/[SPEC]
2) 找出重複段落（例如雙軌/時間優勢常見敘述）
3) 把重複段落改成「引用」並回指權威定義文件
4) 保留操作文件（Checklist/Procedure）作為唯一可勾選入口
5) 最後更新 TAITS_Document_Index.md，確保新手與新 AI 一鍵進入正確入口

---

## 7. 結論（瘦身的真正目的）

> TAITS 的強，不在於文件多；
> 而在於每份文件各就其位、彼此引用、層級清楚、否決權明確。
> 瘦身是降低重複與維護成本，不是刪掉安全性。
