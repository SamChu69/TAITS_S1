# -*- coding: utf-8 -*-
from typing import TypedDict, List

class RiskGateContract(TypedDict):
    eligible: bool
    reason: str
    risk_flags: List[str]
