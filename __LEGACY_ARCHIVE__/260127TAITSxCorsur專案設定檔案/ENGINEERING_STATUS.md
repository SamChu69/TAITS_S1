# TAITS｜工程計畫與進度追蹤（ENGINEERING_STATUS）

## 文件頭（Document Header）
- doc_key：ENGINEERING_STATUS
- 文件性質：工程支援／進度追蹤（不具治理裁決力；不得改寫任何治理文件之語義）
- 治理裁決序位（引用，不得改寫）：DOCUMENT_INDEX → MASTER_ARCH → AI_GOV
- Canonical Flow（L1–L11）唯一正文來源（引用，不得改寫）：MASTER_CANON
- 工程流程定錨唯一來源（引用，不得改寫）：PROCESS_ANCHOR（Unified Process Anchor）
- 語言：繁體中文（英文專有名詞需附中文說明）

---

## 0. 本文件用途（小白可用版）
本文件只做三件事，確保你每次開新對話都能銜接：
1) **固定交接格式**：新對話一貼就能接續工程進度（不靠記憶）
2) **固定工單拆解法**：Phase（大段）→ WP（工作包）→ Ticket（最小步）
3) **固定驗收與回退**：每張 Ticket 都有「驗收指令」與「回退指令」

> 規則：你不需要理解專有名詞；你只要照本文件的格式「複製貼上」與「填空」。

---

## 1. 新對話交接段（每次開新對話必貼）
> 你每次開新對話，只要把下面區塊整段貼出去，並填入括號內容即可。

【基線日期｜Asia/Taipei】：（YYYY-MM-DD）  
【工程定錨】：PROCESS_ANCHOR（Unified Process Anchor）  
【當前 Phase】：（Phase 0/1/2/3/4/5）  
【當前 WP】：（例：P1-WP-L1、P1-WP-L2、P3-WP-GATE）  
【當前 Ticket】：（例：P1-L1-001）  
【本次目標一句話】：（例：建立 L1 資料源介面骨架＋最小驗收）  
【Cursor 專案狀態】：（已開啟/未開啟）  
【工作分支 branch】：（例：work-001）  
【最近一次 commit】：（可留空）  
【本次限制（固定）】：
- 不修改治理正文語義
- 不改裁決序位
- L1–L11 只引用 MASTER_CANON，不另起定義
【我要你輸出（固定四段）】：
A. 我在 Cursor 下一步怎麼做（步驟）  
B. 我該貼給 Cursor AI 的一句話提示（最短可貼用）  
C. 完成後如何驗收（指令＋成功標準）  
D. 若失敗如何回退（保命指令）  
【我目前看到的結果/錯誤】：（成功就寫成功；失敗就貼 Terminal 紅字整段）

---

## 2. 專案固定資產（22 檔 doc_key 清單）
> 本段只列清單，不做語義解釋；避免與治理正文重複。

- AI_GOV
- DOCUMENT_INDEX
- MASTER_ARCH
- MASTER_CANON
- FULL_ARCH
- ARCH_FLOW
- RISK_COMPLIANCE
- GOVERNANCE_GATE_SPEC
- EXECUTION_CONTROL
- UI_SPEC
- DEPLOY_OPS
- LOCAL_ENV
- VERSION_AUDIT
- DATA_SOURCES
- TWSE_RULES
- STRATEGY_UNIVERSE
- STRATEGY_FEATURE_INDEX
- GOVERNANCE_STATE__FREEZE_v1.0
- BEGINNER_GUIDE
- README
- TAITS_PROJECT_PROMPT
- PROCESS_ANCHOR（Unified Process Anchor）

---

## 3. 工程分層：Phase／WP／Ticket（不新增治理，只定工程粒度）
### 3.1 Phase（固定：0–5）
- Phase 0：治理基線與版本鎖定
- Phase 1：L1–L3（資料進來／清洗／基礎特徵）
- Phase 2：L4–L6（訊號／模型／Regime）
- Phase 3：L7–L8（組合／風控與合規 Gate）
- Phase 4：L9–L10（報告／人類裁決）
- Phase 5：L11（稽核／回放／營運）

> 注意：Phase 不新增、不改名；細化一律用 WP/Ticket。

### 3.2 WP（工作包）命名規則
- 格式：`P{Phase}-WP-{主題}`
- 範例：
  - `P1-WP-L1`：L1 工作包
  - `P1-WP-L2`：L2 工作包
  - `P3-WP-GATE`：Gate（風控/合規）工作包
  - `P5-WP-AUDIT`：稽核/回放工作包

### 3.3 Ticket（最小可驗收步）命名規則
- 格式：`P{Phase}-{子域}-{序號3碼}`
- 範例：
  - `P1-L1-001`、`P1-L1-002`
  - `P3-GATE-001`
- Ticket 粒度原則：**一次只做一張 Ticket**（可驗收、可回退、可 review）

---

## 4. 工單模板（每張 Ticket 都照這個填）
> 你不會寫沒關係；你只要把 Ticket 交給我，我會回你 A/B/C/D。

### Ticket 卡（模板）
- Ticket：（例：P1-L1-001）
- Phase / WP：（例：Phase 1 / P1-WP-L1）
- 目標（1 句）：（例：建立資料源介面骨架）
- 產出（列檔名/路徑）：（例：src/ingest/...）
- 不可碰（固定）：
  - 不修改治理正文語義
  - 不改裁決序位
  - 不另起 L1–L11 定義
- 驗收（我提供，你執行）：（指令＋成功標準）
- 回退（固定保命）：（指令）

---

## 5. 目前進度（你只需要更新這一段）
### 5.1 狀態總覽
- 當前 Phase：（Phase X）
- 當前 WP：（P?-WP-???）
- 當前 Ticket：（P?-???-???）
- 目前狀態：
  - 已完成：
    - [ ] （填）
  - 進行中：
    - [ ] （填）
  - 下一步（最多 3 條）：
    - [ ] （填）
- 阻塞/風險（有就寫，沒有留空）：
  - （填）

### 5.2 變更紀錄（最小留痕）
> 每完成一張 Ticket，新增一筆即可（不用寫長篇）
- YYYY-MM-DD：完成（Ticket 編號）｜摘要：……｜驗收：PASS/FAIL｜commit：（hash 可留空）

---

## 6. Cursor 小白固定操作（你只要照抄）
### 6.1 開始前：建立工作分支（保護 main）
```bash
git checkout -b work-XXX
```

### 6.2 做完一張 Ticket：檢查狀態
```bash
git status
```

### 6.3 做完一張 Ticket：存一個「存檔點」（commit）
```bash
git add -A
git commit -m "work-XXX: P?-???-??? <一句話>"
```

### 6.4 失敗回退（保命）
> 情況 A：你還沒 commit，只想丟掉目前改動
```bash
git reset --hard
```

> 情況 B：你已 commit，但想回到上一個 commit
```bash
git reset --hard HEAD~1
```

> 情況 C：你想放棄整個分支（回到 main）
```bash
git checkout main
git branch -D work-XXX
```

---

## 7. 你的「對 GPT 請求格式」（每次只貼這個）
【基線日期】：YYYY-MM-DD（Asia/Taipei）  
【Phase / WP / Ticket】：Phase X / P?-WP-??? / P?-???-???  
【本次目標一句話】：……  
【我要你輸出】：A/B/C/D（Cursor 下一步／一句話提示／驗收／回退）  
【我目前看到的結果/錯誤】：（成功寫成功；失敗貼紅字整段）
