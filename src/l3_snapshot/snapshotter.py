# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
from .schema import SnapshotRecord

def create_snapshot(normalized_data: dict, source: str) -> dict:
    snapshot_id = str(uuid.uuid4())
    created_at = datetime.utcnow().isoformat() + "Z"
    
    return SnapshotRecord(
        snapshot_id=snapshot_id,
        instrument_id=normalized_data.get("instrument_id", ""),
        data_payload=normalized_data,
        created_at=created_at,
        source=source,
        quality_flags=normalized_data.get("quality_flags", [])
    )
