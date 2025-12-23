# -*- coding: utf-8 -*-
from src.l1_data_source.mock_source import get_mock_price
from src.l2_normalization.normalizer import normalize_price
from src.l3_snapshot.snapshotter import create_snapshot
from src.l4_analysis.analyzer import analyze
from src.l5_evidence.builder import build_evidence
from src.l6_regime_v2.classifier import classify_regime
from src.l7_risk.assessor import assess_risk
from src.l8_strategy_selection.selector import select_strategy
from src.l9_position_intent.compiler import compile_intent
from src.l10_execution_plan.planner import plan_execution
from src.l11_execution.executor import execute

raw_data = get_mock_price()
normalized = normalize_price(raw_data, "MOCK")
snapshot = create_snapshot(normalized, "MOCK")
analysis = analyze(snapshot)
evidence = build_evidence(analysis)
regime = classify_regime(evidence)
risk_decision = assess_risk(evidence, regime)
strategy_decision = select_strategy(analysis, risk_decision)
position_intent = compile_intent(strategy_decision)
execution_plan = plan_execution(position_intent)
execution_result = execute(execution_plan)
print(execution_result)
