# -*- coding: utf-8 -*-
from .schema import ExecutionPlan

def plan_execution(position_intent: dict) -> ExecutionPlan:
    intent_type = position_intent.get("intent_type", "")
    desired_exposure = position_intent.get("desired_exposure", "")
    
    if intent_type == "OBSERVE" or intent_type == "EMPTY_INTENT":
        return ExecutionPlan(
            plan_type="NO_OP_EXECUTION_PLAN",
            intent_type=intent_type,
            desired_exposure=desired_exposure,
            reason="observe_only",
            flags=[]
        )
    
    return ExecutionPlan(
        plan_type="PREPARE",
        intent_type=intent_type,
        desired_exposure=desired_exposure,
        reason="prepared",
        flags=[]
    )
