"""
TAITS BaseConnector (S2 Skeleton)

責任：
- 定義所有 Connector 的最小介面
- 只負責「如何取數」，不處理 schema / validation
"""

class BaseConnector:
    source_name: str = "UNDEFINED"

    def fetch(self, params: dict):
        """
        取回 RawPayload + Meta
        """
        raise NotImplementedError("S2 skeleton: no fetch logic implemented")
