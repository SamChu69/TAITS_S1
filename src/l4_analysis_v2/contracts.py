# -*- coding: utf-8 -*-
from typing import TypedDict

class AnalysisResult(TypedDict):
    snapshot_id: str
    instrument_id: str
    close: float
    symbol: str
    market: str
