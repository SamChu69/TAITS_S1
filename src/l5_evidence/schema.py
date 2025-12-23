# -*- coding: utf-8 -*-
from typing import TypedDict

class EvidenceInput(TypedDict):
    snapshot_id: str
    analysis_ref: str
    hash_ref: str

class EvidenceOutput(TypedDict):
    snapshot_id: str
    analysis_ref: str
    hash_ref: str
