# -*- coding: utf-8 -*-
from .schema import StrategyDecision

def select_strategy(analysis: dict, risk_decision: dict) -> StrategyDecision:
    eligible = risk_decision.get("eligible", False)
    
    if not eligible:
        return StrategyDecision(
            strategy_id="NO_STRATEGY",
            reason="risk_not_eligible",
            flags=risk_decision.get("risk_flags", [])
        )
    
    return StrategyDecision(
        strategy_id="OBSERVE",
        reason="eligible",
        flags=[]
    )
