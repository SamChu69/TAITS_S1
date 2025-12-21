"""
TAITS CacheManager (S2 Skeleton)

責任：
- 負責落盤與 hash
- 核心目標：可重現（Reproducibility）
"""

class CacheManager:
    def store(self, normalized_frame, meta: dict):
        """
        回傳 cache_path + content_hash
        """
        raise NotImplementedError("S2 skeleton: no cache logic implemented")
