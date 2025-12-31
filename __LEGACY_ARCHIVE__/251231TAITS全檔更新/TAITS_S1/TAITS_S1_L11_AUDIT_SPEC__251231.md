# TAITS_S1｜L11 工程稽核回放規格（最小工件集）
版本：v1.0（251231）

> 定位：L11 = 工程稽核/回放（全層留痕），不是交易層。
> 目的：讓你能看懂（Human）＋工程能回放（Machine）。

---

## 1. 必須留痕的事件（Event Types）
- ingest_complete（L1）
- normalize_complete（L2）
- snapshot_created（L3）
- analysis_complete（L4）
- evidence_pack_created（L5）
- regime_decided（L6）
- gate_decided（L7）
- proposals_created（L8）
- report_published（L9）
- decision_made（L10）
- audit_bundle_sealed（L11）

## 2. audit_manifest（Machine-Readable）必備欄位
- run_id / symbol_id / time_range
- layer_artifacts：每層工件清單（artifact_id, path, sha256, created_at）
- model_routing：若使用 AI，必記錄（provider, model_id, parameters, prompt_hash）
- inputs_digest：本次輸入摘要（可重播必要資訊）
- outputs_digest：輸出摘要（含 L9/L10 的版本鏈）

### Schema（最小集合）
```json
{
  "run_id": "",
  "symbol_id": "",
  "time_range": {"start": "", "end": ""},
  "layer_artifacts": [
    {"layer": "L1", "artifact_id": "", "sha256": "", "path": "", "created_at": ""}
  ],
  "model_routing": [
    {"layer": "L9", "provider": "", "model_id": "", "params": {}, "prompt_hash": ""}
  ],
  "inputs_digest": {},
  "outputs_digest": {}
}
```

## 3. audit_summary（Human-Readable）最低要求
- 本次 run 的目的與範圍
- 各層是否完成（完成/失敗原因）
- L9 報告版本與關鍵變更
- L10 裁決模式與授權封套摘要
- 任何 gate 阻擋與理由
- 建議需要檢修的層（工程視角），與你需確認的事項（人類視角）

## 4. replay_bundle（可回放最小集合）
- L3 snapshot + L5 evidence pack + L9 metadata + L10 decision_record + audit_manifest
- 以及生成圖形所需的最小資料與程式版本指紋（如適用）

（完）
