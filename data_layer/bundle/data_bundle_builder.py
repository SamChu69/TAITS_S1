"""
TAITS DataBundleBuilder (S2 Skeleton)

責任：
- 組裝 DataBundle
- 不得產生策略、訊號、下單意圖
"""

class DataBundleBuilder:
    def build(self, datasets: dict, validation: dict, audit: list, meta: dict):
        """
        回傳 DataBundle（dict / object）
        """
        raise NotImplementedError("S2 skeleton: no bundle logic implemented")
