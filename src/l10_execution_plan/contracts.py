# -*- coding: utf-8 -*-
from typing import TypedDict, List

class ExecutionPlanContract(TypedDict):
    plan_type: str
    intent_type: str
    desired_exposure: str
    reason: str
    flags: List[str]
