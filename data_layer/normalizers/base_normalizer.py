"""
TAITS BaseNormalizer (S2 Skeleton)

責任：
- 將 RawPayload 轉為 TAITS Schema
- 不得補假資料
"""

class BaseNormalizer:
    def normalize(self, raw_payload, meta: dict):
        """
        回傳 NormalizedFrame（符合 TAITS_DataBundle_and_Schema.md）
        """
        raise NotImplementedError("S2 skeleton: no normalization implemented")
