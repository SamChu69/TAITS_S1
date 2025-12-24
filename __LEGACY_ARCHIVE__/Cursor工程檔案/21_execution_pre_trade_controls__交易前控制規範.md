<!--
ENGINEERING_META (TAITS × Cursor)
- 本段為工程轉譯用 Meta 資訊，不屬於系統規格或交易邏輯
- 本檔為「交易前控制」之工程轉譯文件
- 不承接 Conditional，不進行治理語義歸位
- engineering_role: execution_pre_trade_controls
-->

# 21_execution_pre_trade_controls__交易前控制規範.md

doc_key：EXECUTION_PRE_TRADE_CONTROLS  
文件性質：Engineering Translation（非 Canonical）  
治理狀態：GOVERNANCE_STATE = Freeze v1.0  
變更原則：Only-Add  
版本狀態：ENGINEERING_ACTIVE  
上位約束：DOCUMENT_INDEX / MASTER_ARCH / MASTER_CANON  

Canonical 來源錨定（SOURCE_TAG）：
- TAITS_交易執行與控制規範（EXECUTION_CONTROL）
- TAITS_治理閘門與裁決規範（GOVERNANCE_GATE_SPEC）
- TAITS_版本控管、稽核與可追溯治理規範（VERSION_AUDIT）

---

## 一、工程檔定位（不可替代）

本工程檔定義 **「交易執行之前」必須完成之控制條件與工程檢核規範**。

本檔唯一責任是：

> **將 Canonical 中「交易前必須滿足的治理與控制條件」，  
> 轉譯為工程系統可檢核、可阻斷、不可繞過的前置控制結構。**

本檔 **不**：

- 定義任何交易策略
- 定義任何交易邏輯或參數
- 補完或解釋 Canonical 條文
- 承接任何 Conditional 歸位聲明

---

## 二、交易前控制的工程邊界定位

### 2.1 工程層定義

在工程語義中，「交易前（Pre-Trade）」指的是：

> **任何尚未進入 Execution Intent 狀態之前的治理與控制檢核階段**

只要未滿足本檔定義之條件：

> **工程層必須阻止 Execution Intent 的生成**

---

## 三、交易前必備控制條件（Pre-Trade Mandatory Controls）

以下條件屬 **硬性前置條件**，不可延遲、不可降級、不可替代。

### 3.1 Governance Gate 完整通過

工程轉譯要求：

- Governance Gate 狀態 = PASS
- 必須可追溯其 Gate 類型與裁決結果
- 不得以快取、預設或推測狀態替代

---

### 3.2 Risk / Compliance 放行已完成

工程轉譯要求：

- Risk / Compliance 狀態 = PASS
- 其結果必須可被引用與驗證
- 工程層不推論風險邏輯，只驗證結果存在性

---

### 3.3 Human Decision 已明確完成

工程轉譯要求：

- 必須存在可回放的人類裁決結果（APPROVE）
- 裁決來源必須為合法 UI 決策入口
- 禁止：
  - 隱含批准
  - 系統自動補齊
  - 事後補登

---

## 四、交易前阻斷條件（Pre-Trade Block Conditions）

任一條件成立時，工程層必須直接阻斷：

- 任一必要 Gate 狀態缺失
- 裁決資訊不可回放
- 控制狀態與版本資訊不一致
- 系統處於 Freeze / Block 狀態

阻斷行為屬：

> **工程層 Hard Stop，不進入任何模擬或執行流程**

---

## 五、交易前狀態不可轉移原則

工程層必須確保：

- 未完成交易前控制檢核  
  → 不得生成 Execution Intent
- 不得：
  - 跳過
  - 補跑
  - 回填檢核結果

---

## 六、工程檔終止聲明

本工程檔至此完成以下任務：

- 定義交易前控制之工程邊界
- 明確阻止任何未完成治理條件的執行行為
- 保持 Canonical 治理語義之完整與不可變性

---

> **本檔輸出完成。  
> 依工程規範，於此停止，不處理任何其他工程檔。**
