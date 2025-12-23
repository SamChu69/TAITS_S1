# -*- coding: utf-8 -*-
from .schema import EvidenceOutput

def build_evidence(analysis_result: dict) -> EvidenceOutput:
    return EvidenceOutput(
        snapshot_id=analysis_result.get("snapshot_id", ""),
        analysis_ref=str(analysis_result),
        hash_ref=""
    )
