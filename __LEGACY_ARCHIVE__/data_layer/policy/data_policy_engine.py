"""
TAITS DataPolicyEngine (S2 Skeleton)

責任：
- 依據文件：
  - TAITS_DataSource_Priority_and_Fallback.md
- 決定資料來源使用順序（primary + fallback）
- 不負責實際取數
- 必須可被 Audit 記錄

S2 限制：
- 僅 RESEARCH
- 不得靜默切換來源
"""

class DataPolicyEngine:
    def __init__(self):
        pass

    def decide_source_plan(self, dataset: str, symbol: str, freq: str, context: dict):
        """
        回傳 Source Plan（概念結構）：
        {
            "primary_source": "...",
            "fallback_sources": [...],
            "reason": None
        }
        """
        raise NotImplementedError("S2 skeleton: no policy logic implemented")
