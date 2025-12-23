# -*- coding: utf-8 -*-
from typing import TypedDict, List

class AnalysisInput(TypedDict):
    snapshot_id: str
    instrument_id: str
    data_payload: dict
    created_at: str
    source: str
    quality_flags: list

class AnalysisOutput(TypedDict):
    snapshot_id: str
    close: float
    symbol: str
    market: str
