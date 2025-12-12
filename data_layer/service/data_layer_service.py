"""
TAITS DataLayerService (S2 Skeleton)

Data Layer 對 Orchestrator 的唯一入口。
"""

class DataLayerService:
    def get_bundle(self, universe: list, datasets: list, asof_ts, context: dict):
        """
        高階流程：
        - policy -> connector -> normalizer -> validator -> cache -> audit -> bundle
        """
        raise NotImplementedError("S2 skeleton: service not wired yet")
