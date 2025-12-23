# -*- coding: utf-8 -*-
from typing import TypedDict

class SnapshotRecord(TypedDict):
    snapshot_id: str
    instrument_id: str
    data_payload: dict
    created_at: str
    source: str
    quality_flags: list
