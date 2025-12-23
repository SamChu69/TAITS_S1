# -*- coding: utf-8 -*-
from typing import TypedDict, List

class ExecutionResultContract(TypedDict):
    execution_mode: str
    plan_type: str
    status: str
    reason: str
    flags: List[str]
