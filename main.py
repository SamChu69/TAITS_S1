"""
TAITS - Taiwan Alpha Intelligence Trading System
main.py

System Entry Point (S1 Skeleton)

Design Principles:
- main.py is ONLY responsible for bootstrapping the system
- No strategy logic
- No data fetching
- No broker / execution calls
- All control is delegated to Orchestrator
"""

from enum import Enum
import logging
import sys
from datetime import datetime

# =============================================================================
# System Mode Definition
# =============================================================================

class SystemMode(Enum):
    RESEARCH = "research"
    BACKTEST = "backtest"
    PAPER = "paper"
    LIVE = "live"


# =============================================================================
# Basic Logger Setup (S1 Minimal)
# =============================================================================

def setup_logger() -> logging.Logger:
    logger = logging.getLogger("TAITS")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger


# =============================================================================
# Mode Resolver
# =============================================================================

def resolve_mode(argv) -> SystemMode:
    """
    Resolve system mode from CLI arguments.
    Default: RESEARCH
    """
    if len(argv) < 2:
        return SystemMode.RESEARCH

    raw = argv[1].lower()

    for mode in SystemMode:
        if raw == mode.value:
            return mode

    raise ValueError(
        f"Unknown system mode: {raw}. "
        f"Allowed modes: {[m.value for m in SystemMode]}"
    )


# =============================================================================
# Main Bootstrap
# =============================================================================

def main():
    logger = setup_logger()

    try:
        mode = resolve_mode(sys.argv)
    except Exception as e:
        logger.error(f"Failed to resolve system mode: {e}")
        sys.exit(1)

    logger.info("==================================================")
    logger.info("TAITS - Taiwan Alpha Intelligence Trading System")
    logger.info("System Bootstrap Starting")
    logger.info(f"System Mode : {mode.value.upper()}")
    logger.info(f"Start Time  : {datetime.now().isoformat()}")
    logger.info("==================================================")

    # Import orchestrator lazily to avoid side effects at import time
    try:
        from engine.orchestrator import Orchestrator
    except ImportError as e:
        logger.error("Failed to import Orchestrator.")
        logger.error("Make sure engine/orchestrator.py exists.")
        logger.error(str(e))
        sys.exit(1)

    # Initialize orchestrator
    orchestrator = Orchestrator(
        mode=mode,
        logger=logger,
    )

    # Run system
    try:
        orchestrator.run()
    except KeyboardInterrupt:
        logger.warning("System interrupted by user.")
    except Exception as e:
        logger.exception("Unhandled exception during system run.")
        logger.exception(str(e))
    finally:
        logger.info("==================================================")
        logger.info("TAITS System Shutdown")
        logger.info("==================================================")


# =============================================================================
# CLI Entry
# =============================================================================

if __name__ == "__main__":
    main()
