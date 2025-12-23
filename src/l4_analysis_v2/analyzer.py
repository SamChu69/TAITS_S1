# -*- coding: utf-8 -*-
from .schema import AnalysisInput, AnalysisOutput

def analyze(snapshot: dict) -> AnalysisOutput:
    data_payload = snapshot.get("data_payload", {})
    return AnalysisOutput(
        snapshot_id=snapshot.get("snapshot_id", ""),
        close=data_payload.get("close", 0.0),
        symbol=data_payload.get("symbol", ""),
        market=data_payload.get("market", "")
    )
