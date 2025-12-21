"""
TAITS AuditTrail (S2 Skeleton)

責任：
- 記錄 Data Layer 全流程事件
- 供 Compliance / Debug / 回放使用
"""

class AuditTrail:
    def record(self, event_type: str, payload: dict):
        """
        event_type: policy_decision / fetch / normalize / validate / cache / fallback
        """
        pass
