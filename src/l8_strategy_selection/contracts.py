# -*- coding: utf-8 -*-
from typing import TypedDict, List

class StrategyDecisionContract(TypedDict):
    strategy_id: str
    reason: str
    flags: List[str]
