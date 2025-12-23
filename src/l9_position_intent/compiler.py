# -*- coding: utf-8 -*-
from .schema import PositionIntent

def compile_intent(strategy_decision: dict) -> PositionIntent:
    strategy_id = strategy_decision.get("strategy_id", "")
    
    if strategy_id == "NO_STRATEGY":
        return PositionIntent(
            intent_type="EMPTY_INTENT",
            desired_exposure="NONE"
        )
    
    return PositionIntent(
        intent_type="OBSERVE",
        desired_exposure="NEUTRAL"
    )
