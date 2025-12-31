# TAITS_S1｜本地執行與運算環境規範（S1 Edition）

doc_key：TAITS_S1_LOCAL_ENV  
治理等級：S1（Engineering Edition）  
版本狀態：ACTIVE（S1 口徑；不取代 A+/A 治理母法）  
版本日期：2025-12-31  
上位裁決：TAITS_S1_MASTERBOOK（TAITS_S1_MASTERBOOK__20251231.md）

---

## 1. 你的本地基線（鎖定）
- 裝置：ASUS FX504GE
- 作業系統：Windows 11
- CPU：Intel Core i7-8750H（6C/12T）
- 記憶體（RAM）：32GB
- GPU：NVIDIA GeForce GTX 1050 Ti
- GPU VRAM：4GB
- 儲存：256GB SSD + 750GB HDD


## 2. 本地推理定位（以 4GB VRAM 為前提）
- 優先本地化：L11 / L1 / L2 / L5（摘要、抽取、結構化、人讀稽核）
- 不建議本地硬扛：L4/L6/L9 主力（推理一致性與長文品質）
- 模型級別：3B（優先）→ 7B（量化；控制上下文）
- 工程建議：本地模型做「稽核/抽取」；雲端模型做「報告/裁決整理」

## 3. 必須落盤的環境資訊（L11）
- OS 版本、Python/Runtime 版本
- 模型名稱、量化方式、模型檔 hash
- 推理參數（context、temperature、max_tokens）

