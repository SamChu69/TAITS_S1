# -*- coding: utf-8 -*-
from typing import TypedDict, List

class StrategyInput(TypedDict):
    analysis: dict
    risk_decision: dict

class StrategyDecision(TypedDict):
    strategy_id: str
    reason: str
    flags: List[str]
