# -*- coding: utf-8 -*-
from .schema import RiskDecision

def assess_risk(evidence: dict, regime: dict) -> RiskDecision:
    regime_type = regime.get("regime_type", "")
    evidence_flags = evidence.get("hash_ref", "")
    
    eligible = True
    reason = "pass"
    risk_flags = []
    
    if regime_type == "":
        eligible = False
        reason = "regime_undefined"
        risk_flags.append("REGIME_MISSING")
    
    if evidence_flags == "":
        eligible = False
        reason = "evidence_incomplete"
        risk_flags.append("EVIDENCE_INCOMPLETE")
    
    return RiskDecision(
        eligible=eligible,
        reason=reason,
        risk_flags=risk_flags
    )
