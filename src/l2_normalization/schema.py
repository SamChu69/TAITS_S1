# -*- coding: utf-8 -*-
from typing import TypedDict

class NormalizedPrice(TypedDict):
    instrument_id: str
    symbol: str
    market: str
    close: float
    currency: str
    source: str
    normalized_at: str
    quality_flags: list
