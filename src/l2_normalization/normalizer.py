# -*- coding: utf-8 -*-
from datetime import datetime
from .schema import NormalizedPrice

def normalize_price(raw: dict, source: str) -> NormalizedPrice:
    symbol = raw.get("symbol", "")
    return NormalizedPrice(
        instrument_id=f"TWSE:{symbol}",
        symbol=symbol,
        market="TWSE",
        close=float(raw.get("close", 0)),
        currency="TWD",
        source=source,
        normalized_at=datetime.utcnow().isoformat() + "Z",
        quality_flags=[]
    )
