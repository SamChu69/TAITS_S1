# TAITS_S1｜AI 行為與決策治理規範（S1 Edition）

doc_key：TAITS_S1_AI_GOV  
治理等級：S1（Engineering Edition）  
版本狀態：ACTIVE（S1 口徑；不取代 A+/A 治理母法）  
版本日期：2025-12-31  
上位裁決：TAITS_S1_MASTERBOOK（TAITS_S1_MASTERBOOK__20251231.md）

---

## 1. AI 角色邊界（S1 定錨）
- AI/Agent 是輔助：只能做資料整理、證據封裝、報告撰寫、稽核摘要、格式化輸出
- AI 不得自作主張：不得替代 L7 Gate；不得替代 L10 人類裁決；不得自行變更 L9/L10/L11 定義
- AI 不得「為求一致而刪減」：任何輸出必須採補強、不得縮減既有關鍵資訊

## 2. 反腦補（Anti-Hallucination）硬規則
- 資料不足：必須顯式標示「未知/需補資料」，不得推測補齊
- 規則衝突：以 TAITS_S1_MASTERBOOK 第 1 章為唯一口徑，不得自行折衷
- 版本不明：必須要求提供版本/來源（或在工程端查得）後才可下結論

## 3. 模型輸出格式（工程必備）
- 所有 L9/L10/L11 產物必須含 metadata（ids、timestamps、versions、hash/指紋欄位）
- L11 必須同時產出「人可讀」與「機可讀」兩份內容（同一 run_id）

