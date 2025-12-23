# -*- coding: utf-8 -*-
from .contracts import ExecutionResultContract

def execute(plan: dict) -> ExecutionResultContract:
    plan_type = plan.get("plan_type", "")
    
    return ExecutionResultContract(
        execution_mode="DRY_RUN",
        plan_type=plan_type,
        status="SIMULATED",
        reason="dry_run_execution",
        flags=[]
    )
