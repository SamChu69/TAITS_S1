"""
TAITS - Taiwan Alpha Intelligence Trading System
engine/risk_engine.py

Risk Engine (S1 Skeleton - Hard Gate)

Purpose:
- Provide a hard gate for compliance & risk veto
- Standardize risk decision output
- S1: keep minimal checks, default-block LIVE to prevent accidents
"""

from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional


class RiskDecisionStatus(Enum):
    ALLOW = "allow"
    BLOCK = "block"
    WARN = "warn"


@dataclass
class RiskDecision:
    status: RiskDecisionStatus
    reasons: List[str] = field(default_factory=list)
    details: Optional[Dict[str, Any]] = None
    checked_at: datetime = field(default_factory=datetime.utcnow)

    def is_allowed(self) -> bool:
        return self.status == RiskDecisionStatus.ALLOW


class RiskEngine:
    """
    RiskEngine is the final veto gate before any execution.

    In S1:
    - LIVE mode is blocked by default.
    - Other modes return ALLOW (with minimal checks placeholder).
    """

    def __init__(self, logger=None):
        self.logger = logger

    def evaluate(
        self,
        mode,
        fusion_decision: Optional[Dict[str, Any]] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> RiskDecision:
        """
        Evaluate whether the system is allowed to proceed.

        Args:
            mode: SystemMode from main.py (enum with .value)
            fusion_decision: Future placeholder for Fusion output
            context: Future placeholder for risk inputs (positions, cash, market state)

        Returns:
            RiskDecision
        """
        # ------------------------------------------------------------------
        # S1 Safety Guard: Live is blocked by default
        # ------------------------------------------------------------------
        if getattr(mode, "value", str(mode)) == "live":
            return self._block(
                reasons=[
                    "LIVE mode is disabled in S1 (safety guard).",
                    "RiskEngine hard-gate prevents any accidental execution.",
                ],
                details={"mode": "live"},
            )

        # ------------------------------------------------------------------
        # Minimal placeholder checks (extend in later phases)
        # ------------------------------------------------------------------
        reasons: List[str] = []

        # Example placeholder: fusion_decision existence in non-research modes
        if getattr(mode, "value", str(mode)) in ("paper", "backtest"):
            if fusion_decision is None:
                reasons.append("Fusion decision is missing (placeholder check).")

        if reasons:
            # In S1, missing fusion_decision triggers WARN instead of BLOCK
            return self._warn(
                reasons=reasons,
                details={"mode": getattr(mode, "value", str(mode))},
            )

        return self._allow(details={"mode": getattr(mode, "value", str(mode))})

    # ---
