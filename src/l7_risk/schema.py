# -*- coding: utf-8 -*-
from typing import TypedDict, List

class RiskInput(TypedDict):
    evidence: dict
    regime: dict

class RiskDecision(TypedDict):
    eligible: bool
    reason: str
    risk_flags: List[str]
