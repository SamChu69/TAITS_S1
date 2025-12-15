# 📘 **TAITS_02A_官方資料源與OpenAPI清單.md**

（最完整落地版｜只寫「官方」與「可程式化介面」：TWSE / TPEx / TAIFEX / MOPS / 政府開放資料）

---

## 0. 文件定位（02A 的角色）

本文件只做一件事：

> **把 TAITS 需要的「官方資料源」與「官方可程式化介面（OpenAPI / API / 可下載結構化資料）」完整列出**，讓任何人不用通靈就能接。

* 本文件不談策略、不談指標公式、不談下單。
* 若官方 API/端點更新：**以各 OpenAPI 的 swagger.json 為準**（禁止硬編造端點清單）。

---

## 1. 官方資料源總覽（四大核心＋一個官方開放平台）

| 類別      | 官方單位           | 主要用途（TAITS）          | 介面型態              |
| ------- | -------------- | -------------------- | ----------------- |
| 證券（上市）  | TWSE 台灣證券交易所   | 個股/指數/市場報表/法人/融資融券等  | OpenAPI + 官網報表    |
| 證券（上櫃等） | TPEx 櫃買中心      | 上櫃/興櫃/創櫃/債券等發行與交易資訊  | OpenAPI + 官網報表    |
| 期貨/選擇權  | TAIFEX 台灣期貨交易所 | 期貨/選擇權行情、OI 等（僅觀察）   | OpenAPI + 官網資料    |
| 公開揭露    | MOPS 公開資訊觀測站   | 財報/重大訊息/法說/股東會等      | 官網查詢（無統一 OpenAPI） |
| 政府開放資料  | data.gov.tw    | 部分市場/指數/櫃買等資料的官方彙整入口 | Dataset API/下載    |

---

## 2. TWSE（台灣證券交易所）官方 OpenAPI

### 2.1 官方入口

* **TWSE OpenAPI（Swagger UI）**：[https://openapi.twse.com.tw/](https://openapi.twse.com.tw/) ([openapi.twse.com.tw][1])
* **OAS/Swagger 規格檔**：[https://openapi.twse.com.tw/v1/swagger.json](https://openapi.twse.com.tw/v1/swagger.json) ([openapi.twse.com.tw][1])
* **Base URL（基底網址）**：`https://openapi.twse.com.tw/v1` ([openapi.twse.com.tw][1])

### 2.2 嚴格規則（禁止偷懶）

* **端點清單不得手寫在 TAITS 文件中當作權威**。
* 端點、參數、欄位、回傳格式 **全部以 swagger.json 為唯一權威**。([openapi.twse.com.tw][1])

### 2.3 TAITS 取得方式（落地標準）

* **做法 A（推薦）**：程式啟動時讀取 swagger.json → 自動生成「端點索引」→ 由索引抓資料。([openapi.twse.com.tw][1])
* **做法 B（允許）**：人工在 Swagger UI 內查端點後寫入「設定檔」；但設定檔必須保留：

  * `source = TWSE_OPENAPI`
  * `swagger_version/hash`
  * `endpoint`
  * `params`
  * `schema_version`

---

## 3. TPEx（櫃買中心）官方 OpenAPI

### 3.1 官方入口

* **TPEx OpenAPI（入口頁）**：[https://www.tpex.org.tw/openapi/](https://www.tpex.org.tw/openapi/) ([tpex.org.tw][2])
* **OAS/Swagger 規格檔**：[https://www.tpex.org.tw/openapi/swagger.json](https://www.tpex.org.tw/openapi/swagger.json) ([tpex.org.tw][2])
* **Servers/Base URL（官方列示）**：`https://www.tpex.org.tw/openapi/v1` ([tpex.org.tw][2])

### 3.2 官方覆蓋範圍（TPEx 入口頁明示）

* 上櫃、興櫃、創櫃及債券等發行及交易資訊皆屬 API 覆蓋範圍。([tpex.org.tw][2])

### 3.3 政府開放資料對應（佐證 swagger.json 位置）

* data.gov.tw 的多個資料集亦明示 TPEx OpenAPI 與 swagger.json 位置。([政府資料開放平臺][3])

### 3.4 TAITS 取得方式（落地標準）

同 TWSE：**以 swagger.json 作為唯一權威**，禁止手寫端點清單當作「最終正確」。([tpex.org.tw][4])

---

## 4. TAIFEX（台灣期貨交易所）官方 OpenAPI

### 4.1 官方入口

* **TAIFEX OpenAPI（Swagger UI）**：[https://openapi.taifex.com.tw/](https://openapi.taifex.com.tw/) ([openapi.taifex.com.tw][5])
* **OAS/Swagger 規格檔**：[https://openapi.taifex.com.tw/swagger.json](https://openapi.taifex.com.tw/swagger.json) ([openapi.taifex.com.tw][5])
* **Servers/Base URL（官方列示）**：`https://openapi.taifex.com.tw/v1` ([openapi.taifex.com.tw][5])

### 4.2 嚴格角色定義（TAITS 不可越界）

* TAIFEX OpenAPI 資料在 TAITS 中屬於：

  * **跨市場資訊（Cross-Market）**
  * **市場狀態（Regime）**
  * **風險/壓力（Risk/Pressure）**
* **嚴格禁止**把 TAIFEX 資料定位成「期貨下單策略輸入」的唯一依據；它只能作為 **觀察與調權/風險** 的輸入（決策權仍在你）。

### 4.3 重要釐清（官方 OpenAPI vs 其他資料索取）

* TAIFEX 的 OpenAPI 是正式可程式化介面（如上）。([openapi.taifex.com.tw][5])
* 同時，TAIFEX 也在 Q&A 中說明某些「資料庫/歷史資料」可能需要另行申請（不代表 OpenAPI 不存在，而是**不同資料範圍的供應方式不同**）。([taifex.com.tw][6])

### 4.4 TAITS 取得方式（落地標準）

* 一律以 `swagger.json` 自動生成端點索引與 schema（欄位/型別），不得通靈列端點。([openapi.taifex.com.tw][7])

---

## 5. MOPS（公開資訊觀測站）官方資料入口

### 5.1 官方入口（資訊揭露主站）

* **MOPS（TWSE 維運）**：[https://mopsov.twse.com.tw/mops/web/index](https://mopsov.twse.com.tw/mops/web/index) ([mopsov.twse.com.tw][8])

### 5.2 嚴格事實（很重要）

* MOPS **沒有像 TWSE/TPEx/TAIFEX 一樣統一的 OpenAPI（swagger.json）平台入口**（至少在官方公開入口中未提供）。([mopsov.twse.com.tw][8])
* 因此在 TAITS 中，MOPS 的資料取得屬於「官方網站查詢介面」範疇：

  * 可做合規的自動化擷取（需遵守網站條款/頻率/robots 等）
  * 或以其他「合法授權的資料供應」做替代/備援

> 📌 02D（資料治理與備援）會把「MOPS 擷取」的合規邊界、頻率限制、快取策略、失效降級規則完整寫清楚。

---

## 6. 政府開放資料（data.gov.tw）官方入口（補強與佐證）

### 6.1 官方入口

* [https://data.gov.tw](https://data.gov.tw)

### 6.2 在 TAITS 的定位

* 作為部分資料集的「官方彙整入口」與「備援來源」。
* 多個資料集頁面會提供 OAS/Swagger 說明連結（例如 TPEx OpenAPI）。([政府資料開放平臺][3])

---

## 7. TAITS 落地必備的「來源登錄表」欄位（硬規格）

TAITS 對任何官方來源（TWSE/TPEx/TAIFEX/MOPS/data.gov）都必須以同一份登錄表管理（這是為了杜絕「少一樣」）：

**SourceRegistry（資料來源登錄表）必要欄位：**

* `source_id`：唯一代碼（例如 `TWSE_OPENAPI`, `TPEX_OPENAPI`, `TAIFEX_OPENAPI`, `MOPS_WEB`, `DATAGOV_DATASET`）
* `official_name_zh`：官方名稱（中文）
* `official_name_en`：官方名稱（英文，如有）
* `home_url`：入口網址
* `api_base_url`：Base URL（如有）
* `swagger_url`：swagger.json（如有）
* `auth_required`：是否需金鑰/登入（unknown 也要寫）
* `rate_limit_policy`：頻率限制（unknown 也要寫）
* `data_domains`：覆蓋資料域（價量/指數/衍生品/公告…）
* `license_terms_url`：使用條款網址（若官方提供）
* `last_verified_at`：最後驗證時間（日期）
* `notes`：備註（例如「部分歷史資料需申請」）

---

## 8. 本卷鎖定聲明（02A 完整性保證）

* 本卷已完整列出 TAITS 的**官方資料源與官方可程式化介面入口**：
  **TWSE OpenAPI、TPEx OpenAPI、TAIFEX OpenAPI、MOPS 官方入口、data.gov.tw**。([openapi.twse.com.tw][1])
* 本卷刻意**不手寫端點清單**，因為那會造成你最痛恨的「AI 少一樣 / 寫錯一樣」。
* 唯一權威：各 OpenAPI 的 `swagger.json`。([openapi.taifex.com.tw][7])

---

## 9. 下一卷（02B）

下一卷我會輸出：

# 📘 **TAITS_02B_新聞資料源與事件擷取規格.md**

（完整列出：台灣/國際新聞來源類型、RSS/API、事件抽取欄位標準、合規邊界、備援策略）

---

你只要回：**02B**

[1]: https://openapi.twse.com.tw/?utm_source=chatgpt.com "臺灣證券交易所OpenAPI"
[2]: https://www.tpex.org.tw/openapi/?utm_source=chatgpt.com "證券櫃檯買賣中心OpenAPI 1.0.0 OAS3"
[3]: https://data.gov.tw/en/datasets/17247?utm_source=chatgpt.com "Information on the rise and fall limits not traded on the OTC ..."
[4]: https://www.tpex.org.tw/openapi/swagger.json "www.tpex.org.tw"
[5]: https://openapi.taifex.com.tw/?utm_source=chatgpt.com "Swagger UI - 臺灣期貨交易所"
[6]: https://www.taifex.com.tw/cht/9/tradersQAIS?utm_source=chatgpt.com "交易人最常詢問之問題及解答-資訊面"
[7]: https://openapi.taifex.com.tw/swagger.json "openapi.taifex.com.tw"
[8]: https://mopsov.twse.com.tw/mops/web/index?utm_source=chatgpt.com "MOPS - 資訊觀測站- 臺灣證券交易所"

# 📘 **TAITS_02B_新聞資料源與事件擷取規格.md**

（最完整落地版｜全產業覆蓋 × 免費優先 × 新聞來源全集 × 擷取方式 × 合規邊界 × 事件抽取欄位 × 去重可信度 × 與 Regime/策略的正確關係）

---

## 0. 文件定位（02B 的任務）

本文件只定義 **TAITS 的新聞資料**如何落地，包含：

1. **新聞來源宇宙（N1–N12）完整定義**（全產業覆蓋，不鎖定少數領域）
2. **免費優先（Free-First）** 的取得策略（RSS/公開API/公開頁面）
3. **取得模式（M1–M4）**：RSS / 公開API / 授權供應商 / 合規網站擷取
4. **事件擷取（Event Extraction）** 的完整欄位規格（不可省略）
5. **去重、可信度、多來源聚合、時間線與版本化**
6. **新聞在 TAITS 的正確角色**（只做 L5 事件與題材，不越權變下單指令）

---

## 1. 核心原則（你要求的兩點，硬鎖）

### 1.1 全產業覆蓋（Industry Coverage = ALL）

* TAITS 的新聞來源 **不得只鎖定 AI/DRAM/PCB/機器人等少數產業**
* 必須支援 **台股全產業**（電子、傳產、金融、航運、鋼鐵、化工、生技、觀光、營建、能源、軍工、資服、通路、原物料…等）
* 任何「產業垂直媒體（N8）」只要存在且可合規取得，皆可納入，且 **不限定清單**（採登錄與擴展機制）

### 1.2 免費優先（Free-First）

* 預設採用 **免費/公開** 可取得方式：

  * RSS / 公開Feed
  * 公開API（不付費）
  * 官方公告
  * 合規範圍的公開頁面擷取（不存全文鏡像）
* 付費供應商（N12）只作為：

  * **可選加強**（你決定）
  * **備援**（免費來源不足時）
  * **回溯補洞**（歷史事件完整性需求時）

---

## 2. 新聞在 TAITS 的正確定位（不可越權）

* 新聞屬於 **L5 事件與題材層（Event & Theme Layer｜事件與題材）**
* 新聞只能影響輸出物：

  * `EventThemePack`（事件題材包）
  * `ThemeHeatScore`（題材熱度）
  * `NarrativeShiftSignal`（敘事轉折）
  * `EventRiskFlag`（事件風險旗標）
* 新聞 **不得直接輸出**：買/賣、進出場、倉位

> 結論：新聞是「前哨與解釋」，不是「策略指令」。

---

## 3. 新聞來源宇宙（Source Universe｜N1–N12 全集）

> 注意：以下定義是「類型宇宙」，不是固定名單。
> 固定名單會導致你說的「鎖死範圍」與「少一樣」。

---

### **N1｜官方/監管/政府公告（最高可信、免費）**

**範圍**

* TWSE/TPEx/TAIFEX 公告與新聞
* 監管/政府政策公告（金融、產業、出口管制、法規）

**用途**

* 制度性事件、處置、交易規則變動
* 市場結構性風險（停券、處置、重大風險提示）

**取得方式**

* 官方網站公告（合規擷取）
* 官方 OpenAPI（若提供）

---

### **N2｜公司官方資訊（免費或半免費）**

**範圍**

* 公司新聞稿（Press Release｜新聞稿）
* IR/投資人關係公告、簡報、法說相關

**用途**

* 個股事件源（接單、擴產、事故、訴訟、產品）
* 題材起點（新產品、新技術、新客戶）

**取得方式**

* 公司官網公開頁面、PDF（保存 hash）
* MOPS 公開資訊（02A 另規格）

---

### **N3｜台灣主流財經媒體（免費優先）**

**範圍（類型）**

* 即時財經新聞站、傳統媒體財經版、商業/財經專題

**用途**

* 事件盤早期感知
* 題材擴散（小眾→主流）
* 產業鏈影響範圍（上游/中游/下游）

**取得方式（免費優先）**

* RSS（若提供）優先
* 公開API（若提供）其次
* 合規網站擷取最後（只存元資料/摘要/短片段）

---

### **N4｜國際主流財經媒體（外溢影響）**

**範圍**

* 國際通訊社、國際財經媒體、國際產業媒體

**用途**

* 半導體/出口限制/利率/能源/地緣政治 → 台股外溢
* 國際供需訊號（例如記憶體、伺服器、材料）

**取得方式（免費優先）**

* RSS/公開快訊（若有）
* 需授權者 → 僅保留元資料或連結（由你決定是否啟用 N12）

---

### **N5｜券商/投顧研究摘要（可選、免費優先）**

**範圍**

* 券商晨報、策略週報、產業研究摘要

**用途**

* 題材脈絡與法人敘事框架（觀點，不等於事實）
* 用於解釋與輔助聚類

**取得方式**

* 免費公開版本：可用（只存元資料/摘要）
* 付費完整版：不預設啟用（由你決定）

---

### **N6｜財報會議/法說逐字稿與摘要（免費優先）**

**範圍**

* 法說逐字稿、Q&A、管理層指引（guidance｜展望）

**用途**

* 語氣轉折、供需與庫存訊號（全產業都適用）

**取得方式**

* 公開逐字稿：合規擷取、保存連結與摘要
* 第三方整理：只存元資料（除非授權）

---

### **N7｜重大突發事件快訊（免費＋多源交叉）**

**範圍**

* 災害、事故、地緣政治、制裁、供應鏈中斷、金融風險

**用途**

* 觸發 `EventRiskFlag`
* 影響 `RiskMode`（Normal/RiskOff/Crisis）

**取得方式**

* 主流媒體快訊 + 官方/多源交叉驗證

---

### **N8｜產業垂直媒體（全產業覆蓋、不得鎖定）**

**這段是你要求重寫的重點：不鎖範圍、全產業都要。**

#### 8.1 定義（不是清單）

「產業垂直媒體」指的是：
**針對某產業/供應鏈/專業領域提供更早、更細的消息來源**，例如（僅舉例，不構成限制）：

* 半導體、記憶體、PCB、材料、設備
* 航運、鋼鐵、化工、塑化
* 金融、保險、消費、通路
* 生技、醫材、醫療服務
* 能源、綠能、電力
* 建築營建、觀光餐旅
* 軍工、資安、資服
* 任何台股存在的產業，都屬於覆蓋範圍

#### 8.2 N8「鎖定範圍」的正確做法（不是鎖死，而是可擴展登錄）

TAITS 採用 **「產業分類×來源登錄×自動發現」** 三段式：

* **(A) 產業分類（Industry Taxonomy）**
  以 TAITS 的產業分類表為主（可對應 TWSE/TPEx 產業分類），確保「全產業」可枚舉。

* **(B) 來源登錄（VerticalSourceRegistry）**
  N8 不用固定清單鎖死，但必須「可控」：
  每新增一個垂直媒體來源，必須在 registry 登錄，並標記其產業覆蓋、語言、擷取方式與合規策略。

* **(C) 自動發現（Source Discovery｜來源發現）**（免費優先）
  允許透過以下方式發現新 N8 來源，但新增進系統前仍需登錄：

  * 公開 RSS 目錄/站內 RSS 索引
  * 公開頁面的 RSS 探測（link rel="alternate"）
  * 以「產業關鍵字＋RSS」方式建立候選清單（只產生候選，是否納入由你決定）
  * Google News RSS（若使用）僅作為 **候選來源與趨勢線索**，不作為權威真相來源

#### 8.3 N8 取得方式（免費優先）

* RSS 優先（M1）
* 公開 API（若有）（M2）
* 合規擷取（M4）最後手段（只存元資料/摘要/短片段，不鏡像全文）

#### 8.4 N8 用途（全產業一致）

* 題材萌芽偵測（seed/early）
* 供應鏈擴散（材料→設備→代工→組裝→通路）
* 小型股爆發前線索（你最在意的部分）

---

### **N9｜社群轉載型新聞（只看擴散，不看真相）**

**用途**

* 擴散速度、擁擠度、熱點偵測
* 僅影響 `ThemeHeatScore` 的「擴散分量」

**限制**

* 必須標記 `credibility = low` 或 `unverified`
* 不得直接變成策略理由

---

### **N10｜市場處置/交易異常相關新聞（制度事件）**

**用途**

* 直接影響可交易性與風險
* 對接治理層（L1）做限制建議（仍由治理層決定）

**來源**

* 官方公告（N1）優先，媒體為輔

---

### **N11｜宏觀事件日曆與數據發布（免費優先）**

**用途**

* 公布前後的風險模式調整
* 預警（不是事後解釋）

**來源**

* 官方機構網站或公開日曆資料（免費優先）
* 若需更完整回溯，可選擇 N12（你決定）

---

### **N12｜付費資料供應商（可選，不預設）**

**定位**

* 不預設啟用
* 只作為：

  * 回溯補洞
  * 長期穩定
  * 全文與結構化事件的加強

---

## 4. 新聞取得方式（Ingestion Modes｜M1–M4）完整規格

### **M1：RSS（免費優先，首選）**

必備功能：

* RSS URL 清單管理（可多 feed）
* 拉取頻率、重試、快取
* 解析欄位：title/link/pubDate/source

### **M2：公開 API（免費優先，次選）**

必備功能：

* API Key（若需）管理
* Rate limit 遵守
* Schema 驗證
* 回應 hash 保存

### **M3：授權供應商 API（可選）**

* 不預設啟用
* 僅在你開啟 N12 時使用
* 權限與可保存內容必須寫死在策略（02D 會細寫）

### **M4：網站擷取（最後手段）**

硬限制：

* 尊重條款與頻率
* 不鏡像全文
* 只存：元資料 + 結構化摘要 + 短片段證據鏈

---

## 5. 保存策略（版權與完整性兼顧）

### **S1：元資料（永遠保存）**

* source、title、url、published_at、fetched_at、language、author（若有）

### **S2：結構化摘要（預設保存）**

* summary_zh、key_points、entities、event_candidates

### **S3：證據片段（受限保存）**

* snippet_text（短）、snippet_hash、citation_url

> 原則：TAITS 追求「可追溯證據」，不是「存全文新聞庫」。

---

## 6. 事件擷取（Event Extraction）完整欄位規格（不可省略）

TAITS 對每則新聞都要抽取成 `NewsEventRecord`（新聞事件紀錄）。

### 6.1 `NewsEventRecord` 欄位

**A. 基本識別**

* `event_id`（hash）
* `news_id`（hash）
* `source_id`
* `source_type`（N1–N12）
* `url`
* `title`
* `title_zh`（非中文必填）
* `published_at`（含時區）
* `fetched_at`（含時區）
* `language`

**B. 事件分類（Event Taxonomy）**

* `event_domain`：macro / policy / industry / company / market_structure / risk
* `event_type`（可多項）：earnings / guidance / order / capex / mna / lawsuit / accident / policy_change / rate_decision / supply_chain / export_control / geopolitics / rumor
* `event_severity`：low / medium / high / critical
* `event_status`：unverified / confirmed / retracted

**C. 影響範圍**

* `impact_scope`：market / sector / company / supply_chain
* `affected_sectors`（可空）
* `affected_tickers`（可空）

**D. 題材與敘事**

* `theme_primary`（例如：AI、DRAM、PCB、航運、鋼鐵、生技…）
* `theme_secondary`（可多項）
* `theme_stage`：seed / early / mainstream / late
* `narrative_direction`：positive / negative / neutral / mixed
* `narrative_shift`：upshift / downshift / none

**E. 情緒與強度**

* `sentiment_score`（-1~+1）
* `urgency_score`（0~1）
* `novelty_score`（0~1）
* `spread_score`（0~1，來自多源/社群/搜尋；02C 會定義）

**F. 可信度**

* `credibility_level`：A/B/C/D

  * A：官方/原始文件
  * B：主流媒體多源一致
  * C：單一來源或引用鏈不完整
  * D：社群/匿名/未證實
* `credibility_reasons`（條列）
* `source_count`（交叉來源數）

**G. 證據鏈**

* `evidence_snippets`（短片段＋hash＋url）
* `related_urls`（官方/公告/其他媒體）

**H. 版本與追溯**

* `schema_version`
* `content_hash`
* `ingestion_mode`（M1~M4）
* `license_flag`（unknown/allowed/restricted）

---

## 7. 去重（Deduplication）三層硬規格

* **Dedupe-1：URL 去重**
* **Dedupe-2：標題＋來源＋時間窗**
* **Dedupe-3：事件語意聚合（event_cluster）**
  不同媒體報同一事件 → 聚合後提高 `source_count` 與可信度

---

## 8. 題材聚類（Theme Clustering）硬規格（全產業）

`ThemeCluster` 必備欄位：

* `cluster_id`
* `theme_name_primary`
* `theme_aliases`
* `industry_tags`（可多項，對應全產業分類）
* `time_window`
* `event_count`
* `source_count`
* `heat_score`
* `credibility_weighted_heat`
* `top_entities`
* `narrative_direction`
* `stage`

---

## 9. 新聞如何影響 Regime / 策略（只允許正確通道）

### 9.1 允許

* L4 Regime：事件盤/風險模式的輔助
* L8 權重：題材熱度/敘事轉折調權
* L1 治理：重大事件觸發風險鎖建議

### 9.2 禁止

* 新聞單獨觸發買賣
* `unverified` 事件提高倉位
* N9（社群轉載）成為策略主理由

---

## 10. 來源登錄表（NewsSourceRegistry｜必備，防少一樣）

每個新聞來源必須登錄，不得「口頭存在」。

必備欄位：

* `source_id`
* `source_name_zh`
* `source_name_en`（若有）
* `source_type`（N1–N12）
* `industry_coverage`：**ALL** 或 指定產業集合（N8 預設 ALL）
* `home_url`
* `rss_urls`（可多）
* `api_base_url`（若有）
* `auth_required`
* `license_terms_url`
* `ingestion_mode_allowed`（M1/M2/M3/M4）
* `rate_limit_policy`
* `content_storage_policy`（S1/S2/S3/全文是否允許）
* `language_default`
* `timezone_default`
* `last_verified_at`
* `notes`

---

## 11. 失效與降級（Degrade Rules）

* `NewsAvailabilityState`：OK / PARTIAL / FAIL
* PARTIAL：仍輸出事件包，但降低信心度、標記缺口
* FAIL：輸出空事件包；Regime 不得判為事件盤；治理不得因新聞觸發風險鎖

---

## 12. 本卷鎖定聲明（02B 最終版）

* N8 已改為：**全產業覆蓋 + 登錄擴展 + 自動發現（不鎖死）**
* 新聞來源採：**免費優先（Free-First）**，付費 N12 不預設啟用
* 事件擷取欄位、去重、題材聚類、可信度、合規保存策略：**完整不省略**
* 未來新增來源：只需登錄 `NewsSourceRegistry`，不改結構、不刪內容

---

## 13. 下一卷（02C）

下一卷我會輸出：

# 📘 **TAITS_02C_社群/情緒資料源與量化規格.md**

（全社群覆蓋、免費優先、合規邊界、文本清洗、情緒/擁擠度/擴散特徵、與新聞事件融合規格）

---

# 📘 **TAITS_02C_社群/情緒資料源與量化規格.md**

（最完整落地版｜全社群覆蓋 × 免費優先 × 合規邊界 × 文本清洗 × 情緒/擁擠度/擴散特徵 × 與新聞事件融合）

---

## 0. 文件定位（02C 的任務）

本文件定義 TAITS 的 **社群/情緒（Community & Sentiment）資料**如何落地，包含：

1. **社群資料源宇宙（S1–S12）全覆蓋**（不鎖平台、不鎖題材、不鎖產業）
2. **免費優先（Free-First）** 的取得策略（公開頁面/RSS/公開API/合法匯入）
3. **合規邊界（Compliance Boundary）**：可抓什麼、不得做什麼、如何保存
4. **文本清洗與標準化（Normalization）**：繁中、口語、表情、代號、錯字
5. **量化特徵（Feature Spec）**：情緒、擁擠度、擴散速度、主題強度、敘事轉折
6. **與 02B 新聞事件融合規格**：去重、交叉驗證、可信度加權
7. **降級與容錯（Degrade Rules）**：來源失效不通靈、不崩盤

❌ 不定義策略買賣規則（在 05）
❌ 不定義指標公式（在 03）
✅ 只把「社群/情緒資料」變成 TAITS 可用的結構化輸入（L5/L6/L8/L1）

---

## 1. 社群在 TAITS 的正確定位（不可越權）

社群/情緒資料在 TAITS 中是：

* **L5 事件與題材層**：題材萌芽、敘事轉折、擴散速度
* **L6 指標與特徵層**：情緒/擁擠度/擴散特徵
* **L8 融合與權重層**：只作為「權重調整」與「風險擁擠」
* **L1 治理層**：只作為「風險旗標」與「過熱警示」（不可直接否決交易，需治理規則）

嚴格禁止：

* 社群單一訊號直接觸發買賣
* 社群內容直接作為「事實」
* 未驗證謠言直接提升倉位

> 結論：社群是「熱度/擴散/擁擠」的偵測器，不是事實供應器。

---

## 2. 社群資料源宇宙（S1–S12 全覆蓋）

TAITS 社群來源分為十二類（宇宙定義，不綁固定名單）：

---

### **S1｜股市論壇（長文深度討論）**

**例（僅例，不鎖）**：PTT Stock 等
**用途**：

* 題材萌芽、主流論點、風向轉折
* 個股討論熱度、疑慮與風險敘事

**取得方式（免費優先）**：公開頁面/合規擷取、公開 API（若存在）

---

### **S2｜社群平台貼文（擴散快）**

**例**：X（Twitter）、Facebook 公開貼文
**用途**：

* 擴散速度、熱點偵測
* KOL 影響力擴散（但不等於正確）

**取得方式**：公開 API（若有且符合條款）/公開頁面（合規擷取）/合法匯入

---

### **S3｜短影音/影音平台（敘事放大器）**

**例**：YouTube（標題/描述/留言）
**用途**：

* 題材從小眾走向大眾的放大訊號
* 「散戶敘事」集中化（擁擠度）

**取得方式**：公開 API（若有）/公開頁面（合規擷取）

---

### **S4｜即時聊天/社群群組（高噪音高速度）**

**例**：Telegram 公開群、Discord 公開頻道
**用途**：

* 超早期題材萌芽（但謠言多）
* 擴散速度與風險訊號

**取得方式**：僅限公開頻道/合法匯入（禁止非法侵入私域）

---

### **S5｜問答/討論平台（口語與新手群體）**

**例**：Dcard 投資相關
**用途**：

* 散戶情緒轉折與恐慌/貪婪偵測
* 題材「入門化」階段偵測（mainstream 前兆）

---

### **S6｜新聞留言區/討論串（情緒樣本）**

**用途**：

* 與 02B 新聞事件連動：新聞出現後的情緒反應曲線
* 正負面極化程度（polarization）

---

### **S7｜搜尋熱度與趨勢（非社群但屬情緒代理）**

**例**：Google Trends
**用途**：

* 關注度變化（interest shift）
* 題材熱度曲線補強

---

### **S8｜APP/看盤平台公開熱門榜（擁擠度代理）**

**用途**：

* 熱門排行、點閱排行、討論排行
* 散戶擁擠程度（crowding）

**限制**：若無公開介面，僅能由你合法匯入或放棄（不得用灰色手段）

---

### **S9｜KOL/自媒體文章（敘事節點）**

**用途**：

* 影響力加權的敘事轉折
* 題材「被定義」的時刻

**限制**：KOL 觀點不等於事實，可信度需分級

---

### **S10｜企業雇主/員工評論與招募（產業熱度側訊號）**

**用途**：

* 產業景氣側面訊號（擴產/招工/裁員）
* 供應鏈緊張程度

**限制**：此類資料噪音高、延遲高，只能作輔助特徵

---

### **S11｜公開投資社群資料集（研究用）**

**用途**：

* 回測用歷史情緒樣本（若可取得）
* 模型校正與評估

---

### **S12｜使用者自有匯入（你提供的內容）**

**用途**：

* 你自行蒐集的群組訊息、截圖摘要、筆記
* 由你決定是否匯入 TAITS（最高控制權）

---

## 3. 免費優先（Free-First）取得策略（硬規格）

TAITS 的社群資料擷取必須遵循：

1. **公開可取得優先**（公開頁面、RSS、公開API）
2. **不強制付費**（付費 API/供應商不預設啟用）
3. **不做灰色地帶**（不碰私域、不繞過權限、不破解）
4. **可被你手動匯入**（S12 必須存在，補足平台限制）

---

## 4. 合規邊界（Compliance Boundary｜硬規則）

### 4.1 可做

* 抓取公開頁面可見內容（遵守條款與頻率）
* 使用官方公開 API（遵守授權與 rate limit）
* 保存元資料與結構化摘要
* 保存短片段作證據鏈（不鏡像全文）

### 4.2 不可做

* 抓取私密群組/私訊
* 規避登入/付費牆
* 大量鏡像內容建立「替代平台」
* 以自動化大量抓取造成平台負載或違反條款

---

## 5. 社群資料標準化（Normalization）完整規格

### 5.1 原始資料轉為 `CommunityPostRecord`

必備欄位：

* `post_id`（唯一 hash）
* `source_id`（來源）
* `source_type`（S1–S12）
* `url`（若有）
* `author_id`（可匿名化）
* `author_role`（一般/疑似KOL/媒體/官方/未知）
* `created_at`（含時區）
* `fetched_at`（含時區）
* `language`（zh-TW/zh/…）
* `raw_text`（原文）
* `clean_text`（清洗後）
* `symbols`（解析出的股票代碼列表）
* `topics_raw`（原平台標籤，若有）
* `engagement`（互動：like/comment/share/view，若有）
* `media_refs`（圖片/影片連結，若有）
* `license_flag`（unknown/allowed/restricted）
* `schema_version`

### 5.2 清洗規則（必做）

* 去除 URL 追蹤參數、重複空白、無意義符號
* 轉換全形半形、常見錯字修正（可規則庫）
* 表情符號/梗詞保留為 token（避免情緒訊號被刪）
* 股票代碼解析（台股常見：2330、台積電、TSMC 等）
* 繁中優先：非中文需做中譯欄位（只中譯摘要，不強制全文）

---

## 6. 情緒/擁擠度/擴散特徵（Feature Spec）最完整清單

TAITS 對社群資料輸出的核心特徵集合定義為 `SentimentCrowdingFeatures`：

### 6.1 情緒特徵（Sentiment Features）

* `sentiment_score`：-1 ~ +1（整體情緒）
* `emotion_fear_score`：恐慌（0~1）
* `emotion_greed_score`：貪婪（0~1）
* `emotion_anger_score`：憤怒（0~1）
* `emotion_hope_score`：期待（0~1）
* `emotion_uncertainty_score`：不確定（0~1）
* `polarity_shift`：情緒轉折（上升/下降/無）

### 6.2 擁擠度特徵（Crowding Features）

* `mention_count`：提及次數（時間窗）
* `unique_author_count`：獨立作者數
* `engagement_rate`：互動率（互動/曝光）
* `retail_crowding_index`：散戶擁擠指數（合成）
* `topic_concentration`：題材集中度（越集中越擁擠）
* `bull_bear_ratio_text`：文字多空比（看多/看空比例）

### 6.3 擴散速度（Spread / Virality Features）

* `spread_velocity`：擴散速度（單位時間新增量）
* `spread_acceleration`：擴散加速度
* `cross_platform_spread`：跨平台擴散（是否從 S1 → S2 → S3）
* `time_to_mainstream`：從 seed 到 mainstream 的時間
* `influencer_amplification`：KOL 放大程度

### 6.4 敘事與主題（Narrative & Topic Features）

* `theme_primary`：主題材
* `theme_secondary_list`
* `narrative_direction`：正/負/中/混合
* `narrative_shift_signal`：敘事轉折
* `claim_density`：陳述密度（「據說/聽說」等不確定詞比例）
* `rumor_probability`：謠言概率（僅作風險提示）

### 6.5 個股/產業映射特徵（Mapping Features）

* `ticker_heat_map`：個股熱度表
* `sector_heat_map`：產業熱度表（全產業）
* `supply_chain_link_map`：供應鏈關聯擴散（若有映射庫）

---

## 7. 與 02B 新聞事件的融合規格（必做）

TAITS 必須把社群與新聞做「互證」而不是互相污染。

### 7.1 交叉驗證（Cross-Validation）

對同一題材/事件：

* 新聞先出現、社群後爆量 → 可信度提升（但也可能是追高擁擠）
* 社群先爆量、新聞後跟上 → **題材萌芽成功**（seed→early）
* 社群爆量但無新聞/無公告 → 標記 `unverified_theme`（風險提示，不否決）

### 7.2 可信度加權（Credibility Weighting）

* 社群來源預設可信度低於官方/主流新聞
* 但「多平台一致」可提升權重（cross_platform_spread）

### 7.3 融合輸出（必備物件）

* `SocialNewsFusionPack`

  * `verified_event_links`（已互證的事件關聯）
  * `unverified_theme_alerts`（未互證題材警示）
  * `crowding_risk_flags`（擁擠風險旗標）
  * `narrative_shift_confirmations`（敘事轉折確認）

---

## 8. 降級與容錯（Degrade Rules｜不通靈）

### 8.1 狀態定義

* `SocialAvailabilityState`：OK / PARTIAL / FAIL

### 8.2 降級規則

* OK：正常輸出所有特徵
* PARTIAL：只輸出可得平台特徵，`confidence` 下修
* FAIL：輸出空 `SentimentCrowdingFeatures`，並在 `DecisionPacket` 顯示缺失（不得猜測）

---

## 9. 必備登錄表（SocialSourceRegistry｜防少一樣）

每個社群來源必須登錄：

必備欄位：

* `source_id`
* `source_name_zh`
* `source_name_en`（若有）
* `source_type`（S1–S12）
* `industry_coverage`：ALL（預設全產業）
* `home_url`
* `api_base_url`（若有）
* `rss_urls`（若有）
* `auth_required`
* `license_terms_url`
* `ingestion_mode_allowed`（M1/M2/M4/匯入）
* `rate_limit_policy`
* `content_storage_policy`（S1/S2/S3）
* `language_default`
* `timezone_default`
* `last_verified_at`
* `notes`

---

## 10. 本卷鎖定聲明（02C 完整性保證）

* 已定義社群來源宇宙 S1–S12（全覆蓋）
* 已定義免費優先與合規邊界（禁止灰色）
* 已定義完整資料結構、清洗、特徵集合
* 已定義與新聞融合與交叉驗證
* 已定義降級與登錄表（防少一樣）

---

## 11. 下一卷（02D）

下一卷我會輸出：

# 📘 **TAITS_02D_資料治理與備援/降級策略.md**

（含：資料品質評分、來源優先序、快取策略、版本化、缺失補洞、故障切換、全系統降級路徑、治理層否決觸發條件）

---

# 📘 **TAITS_02D_資料治理與備援/降級策略.md**

（最完整落地版｜資料品質評分 × 來源優先序 × 快取/版本化 × 缺失補洞 × 故障切換 × 全系統降級路徑 × 治理否決觸發）

---

## 0. 文件定位（02D 的任務）

本文件是 TAITS 的 **資料治理中樞規格**，目的在於解決你最痛恨的問題：

> 「AI 寫一樣少一樣」與「資料斷了就通靈」

因此 02D 明確定義：

1. **資料品質（Data Quality）如何量化評分**
2. **資料來源優先序（Primary/Fallback）如何制定**
3. **快取、版本化、可重現（Reproducibility）如何做到**
4. **資料缺失（Missing）如何補洞與什麼情況不得補**
5. **來源故障（Failover）如何切換，且不影響系統一致性**
6. **全系統降級（Degrade）路徑：少了哪一塊該怎麼運行、哪裡必須停止**
7. **治理否決（Governance Veto）與風險鎖（Risk Lock）觸發條件**

❌ 本文件不談策略邏輯（在 05）
❌ 本文件不談指標公式（在 03）
✅ 本文件是「資料可信」的最高保證

---

## 1. 核心原則（硬鎖）

1. **不通靈**：資料缺失不得靠猜
2. **可追溯**：每一筆資料都要知道來自哪裡、何時取得、版本是什麼
3. **可重現**：同版本資料 + 同版本程式 = 同結果
4. **可降級**：資料少了仍可運行，但必須「標示缺口」與「降低信心」
5. **可停止**：遇到關鍵資料失效，必須能「凍結」決策，避免誤判
6. **免費優先**：能用公開/免費來源就不依賴付費，但仍要可擴展到授權供應商

---

## 2. TAITS 資料治理總體架構（文字流程圖）

```
Data Ingestion（抓取）
  ↓
Schema Validation（格式/欄位驗證）
  ↓
Normalization（標準化欄位與型別）
  ↓
Quality Checks（品質檢查）
  ↓
Anomaly Detection（異常偵測）
  ↓
Versioning & Lineage（版本化與血緣）
  ↓
Cache & Storage（快取與存放）
  ↓
Serving Layer（供上游特徵/Regime/策略使用）
  ↓
Degrade / Failover（降級/切換）
  ↓
Governance Signals（提供治理否決依據）
```

---

## 3. 資料分級（Data Tiering）與必要性（不可省）

TAITS 將資料分為 **T0–T4** 五級，決定「可否缺失」「缺失是否停止」。

### T0｜系統生命線（缺失即停止）

* 基礎行情（至少包含：指數與個股 OHLCV 之核心欄位）
* 日期/時間軸（交易日曆、時區）
* 資料品質狀態（DataQualityState）

缺失處理：

* **直接停止推進 L4/L7/L8/L10**，並回報 `FAIL`

---

### T1｜核心決策資料（缺失強降級）

* 法人買賣超/籌碼（官方）
* 融資融券（官方）
* 市場廣度（漲跌家數等）
* 主要公告（MOPS / 官方處置）

缺失處理：

* 可運行，但 `confidence` 下修
* 治理層（L1）可能限制策略集合

---

### T2｜跨市場資料（缺失中度降級）

* TAIFEX 期貨/選擇權（僅觀察）
* 匯率/宏觀（公開）

缺失處理：

* Regime 仍可算，但 `CrossMarketConfidence` 下修
* 相關策略權重下降或禁用（由 L1 決定）

---

### T3｜新聞資料（缺失可降級）

* 新聞（RSS/公開API/公開頁面）
* 事件日曆

缺失處理：

* 不可把市場判成事件盤
* 題材熱度與敘事轉折輸出為空

---

### T4｜社群情緒資料（缺失可降級）

* 社群/情緒/搜尋熱度

缺失處理：

* 擁擠度特徵輸出為空
* 不可做情緒調權與擁擠風險提示

---

## 4. 資料來源優先序（Primary → Fallback）規則（硬規格）

每一個資料域（Data Domain）都必須有：

* **Primary Source（主來源）**
* **Fallback Source（備援來源）**（至少 1 個）
* **Degrade Policy（降級策略）**
* **Stop Policy（停止策略）**

### 4.1 Data Domain 清單（02 對齊）

* D1 個股價量
* D2 指數與市場廣度
* D4 融資融券
* D5 法人籌碼
* D6 期貨（TAIFEX）
* D7 選擇權（TAIFEX）
* D8 官方公告（MOPS 等）
* D9 新聞
* D10 社群/情緒
* D13 宏觀

---

### 4.2 來源選擇的總原則

1. **官方 > 非官方**
2. **結構化 API > 網站頁面**
3. **可回溯 > 只能即時**
4. **免費優先 > 付費可選**
5. **多來源交叉 > 單一來源**

---

## 5. 標準化與 Schema 驗證（防止欄位亂飄）

### 5.1 Schema Registry（欄位規格登錄）

每個資料域必須有 schema 定義，包含：

* 欄位名稱（中文/英文）
* 型別（int/float/string/datetime）
* 是否必填
* 合法範圍（min/max）
* 單位（元/張/%）
* 時間粒度（日/分/秒）

### 5.2 驗證規則（必做）

* 欄位缺失：標記 Missing，不得默默補上
* 型別錯誤：拒收或轉型（需記錄）
* 日期錯位：拒收
* 重複資料：去重並保留血緣

---

## 6. 資料品質評分（Data Quality Score, DQS）完整規格

每個資料集（每來源×每日期/時間窗）都要輸出 DQS。

### 6.1 DQS 組成（0–100）

* `Completeness`（完整性）0–30
* `Timeliness`（即時性）0–20
* `Consistency`（一致性）0–20
* `Validity`（合法性/範圍）0–20
* `Uniqueness`（唯一性/去重）0–10

### 6.2 分數等級

* **A（90–100）**：可用於全系統
* **B（75–89）**：可用但需降低信心
* **C（60–74）**：僅限研究/顯示，不可驅動策略
* **F（<60）**：FAIL，必須停止或強降級

### 6.3 必備輸出物

* `DataQualityState`：OK/WARN/FAIL
* `DQS_Report`：各分項分數與原因
* `MissingDataReport`
* `AnomalyReport`

---

## 7. 異常偵測（Anomaly Detection）完整規格

### 7.1 基本異常（必做）

* 價格負值/成交量負值
* 異常跳變（單日漲跌 > 合理閾值）
* 成交量突變（倍數超過閾值）
* 交易日缺失/重複
* 時間戳不在交易時段（盤中資料才適用）

### 7.2 進階異常（建議）

* 與次來源比對差異（cross-source discrepancy）
* 指數與成分股一致性檢查（粗略）
* 期現價差離群

### 7.3 異常處理（不可通靈）

* 輕微：標記 WARN + 降低信心
* 嚴重：FAIL + 停止推進
* 永遠保留原始資料與異常記錄（可追溯）

---

## 8. 快取與存放（Cache & Storage）完整規格

### 8.1 Cache 層（短期）

* 目的：避免頻繁抓取造成來源壓力
* 規則：

  * 按來源與端點快取
  * 設定 TTL（依資料頻率）
  * 支援 ETag/Last-Modified（若來源提供）

### 8.2 Storage 層（長期）

* 目的：回測、重現、審計
* 必存：

  * 原始回應（raw）
  * 標準化後資料（normalized）
  * schema version
  * content hash
  * ingest metadata（來源、時間、模式）

---

## 9. 版本化與血緣（Versioning & Lineage）硬規格

每批資料必須產生 `DataLineageRecord`：

必備欄位：

* `dataset_id`
* `source_id`
* `endpoint_or_path`
* `ingestion_mode`（API/RSS/WEB/IMPORT）
* `fetched_at`
* `data_time_range`
* `schema_version`
* `content_hash`
* `transform_version`（清洗/轉換版本）
* `quality_score`
* `quality_state`
* `parent_datasets`（若由多源合併）

> 任何上層輸出（特徵/Regime/策略候選）都要能追溯到 lineage。

---

## 10. 缺失補洞（Missing Data Imputation）完整規格

### 10.1 允許補洞的資料類型

* 只允許「非關鍵衍生特徵」補洞
  例如：情緒熱度缺一小段，可用時間平滑（需標記）
* 不允許補洞的資料：

  * 原始行情 OHLCV（T0）
  * 官方公告（T1）
  * 期貨/選擇權核心欄位（T2）

### 10.2 補洞必備規則

* 必須標記 `imputed = true`
* 必須保留補洞方法與參數
* 補洞後的資料不得提升策略信心，只能「減少空洞」

---

## 11. 故障切換（Failover）完整規格

### 11.1 切換觸發條件

* 連續 N 次抓取失敗
* DQS < 60
* schema 驗證失敗
* 來源回應延遲過長（超時）

### 11.2 切換行為

* 切到 fallback source
* 同步更新 `DataLineageRecord`
* 記錄 `FailoverEvent`

### 11.3 禁止事項

* 不得在切換時偷偷改欄位定義
* 不得把不同定義的資料硬拼在一起（必須經標準化後合併）

---

## 12. 全系統降級（Degrade）路徑（最重要）

TAITS 必須輸出 `SystemAvailabilityState`：

* `FULL`：全功能
* `DEGRADED`：降級可運行
* `FROZEN`：凍結（停止決策）
* `SAFE_MODE`：安全模式（只顯示，不建議）

### 12.1 典型降級矩陣

| 缺失    | 系統狀態     | 允許輸出        | 禁止輸出        |
| ----- | -------- | ----------- | ----------- |
| T0 缺失 | FROZEN   | 僅缺失報告       | Regime/策略候選 |
| T1 缺失 | DEGRADED | Regime（降信心） | 部分策略族群      |
| T2 缺失 | DEGRADED | Regime（無跨市） | 跨市調權策略      |
| T3 缺失 | DEGRADED | 非事件盤判定      | 題材/敘事輸出     |
| T4 缺失 | DEGRADED | 基本策略候選      | 情緒調權/擁擠提示   |

---

## 13. 治理否決與風險鎖（Governance Veto / Risk Lock）觸發條件

### 13.1 必須否決（VETO）條件（硬規格）

* `DataQualityState = FAIL`（T0）
* 時間戳錯位（交易日/時段錯）
* 來源回應與 schema 不一致且無法轉換
* 原始行情存在重大異常且未能交叉驗證

### 13.2 風險鎖（RiskLock）條件（可配置）

* T1/T2 缺失導致 Regime 信心過低
* 新聞/社群出現 `critical` 但未驗證（避免被假消息攻擊）
* 市場極端波動觸發（由 04/11 定義）

### 13.3 風險鎖輸出

* `RiskLock = ON/OFF`
* `LockReason`
* `LockScope`（全市場/特定產業/特定標的）
* `RequiredHumanAck`（是否需要你確認）

---

## 14. 落地必備輸出物（02D 交付清單）

TAITS 在資料層必須能輸出：

* `DataQualityState`
* `DQS_Report`
* `MissingDataReport`
* `AnomalyReport`
* `DataLineageRecord`
* `FailoverEventLog`
* `SystemAvailabilityState`
* `DegradeDecisionLog`
* `GovernanceSignalPack`（提供 L1 使用）

---

## 15. 本卷鎖定聲明（02D 最終版）

* 已完整定義資料治理全鏈路：抓取→驗證→標準化→品質評分→版本化→快取→降級→治理否決
* 已明確定義「何時可降級」「何時必須停止」
* 不通靈、可追溯、可重現、可落地
* 免費優先，但允許你未來自行開啟付費備援（不破壞架構）
