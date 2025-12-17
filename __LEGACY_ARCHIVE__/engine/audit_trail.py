"""
TAITS - Taiwan Alpha Intelligence Trading System
engine/audit_trail.py

Audit Trail (S1 Skeleton)

Purpose:
- Provide a unified audit event structure
- Allow every decision step to be reconstructable
- S1 uses in-memory storage only
"""

from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List


class AuditEventType(Enum):
    DATA = "data"
    INDICATOR = "indicator"
    STRATEGY = "strategy"
    AGENT = "agent"
    REGIME = "regime"
    FUSION = "fusion"
    RISK = "risk"
    EXECUTION = "execution"
    SYSTEM = "system"


@dataclass
class AuditEvent:
    event_type: AuditEventType
    name: str
    payload: Dict[str, Any]
    timestamp: datetime = field(default_factory=datetime.utcnow)


class AuditTrail:
    """
    Central audit trail recorder.
    In S1, events are kept in memory only.
    """

    def __init__(self):
        self._events: List[AuditEvent] = []

    def append(
        self,
        event_type: AuditEventType,
        name: str,
        payload: Dict[str, Any],
    ):
        event = AuditEvent(
            event_type=event_type,
            name=name,
            payload=payload,
        )
        self._events.append(event)

    def list_events(self) -> List[AuditEvent]:
        return list(self._events)

    def clear(self):
        self._events.clear()

    def summary(self) -> Dict[str, int]:
        """
        Return simple statistics of recorded events.
        """
        stats: Dict[str, int] = {}
        for e in self._events:
            key = e.event_type.value
            stats[key] = stats.get(key, 0) + 1
        return stats
