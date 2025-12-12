"""
TAITS - Taiwan Alpha Intelligence Trading System
engine/data_validator.py

Data Validator (S1 Skeleton)

Purpose:
- Validate data availability and basic integrity
- Enforce data governance rules at runtime
- Provide standardized validation results
"""

from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional


class ValidationStatus(Enum):
    PASS = "pass"
    WARN = "warn"
    FAIL = "fail"


@dataclass
class ValidationResult:
    status: ValidationStatus
    message: str
    details: Optional[Dict[str, Any]] = None
    checked_at: datetime = datetime.utcnow()


class DataValidator:
    """
    DataValidator performs basic checks to determine
    whether input data is usable for downstream modules.
    """

    def __init__(self, logger=None):
        self.logger = logger

    # ---------------------------------------------------------------------
    # Public API
    # ---------------------------------------------------------------------

    def validate_dataset(
        self,
        dataset_name: str,
        data: Any,
        required_fields: Optional[List[str]] = None,
    ) -> ValidationResult:
        """
        Validate a dataset with minimal rules.

        Args:
            dataset_name: Human-readable dataset identifier
            data: Any data object (DataFrame, dict, list, etc.)
            required_fields: Required field names (if applicable)

        Returns:
            ValidationResult
        """
        if data is None:
            return self._fail(
                dataset_name,
                "Data is None",
            )

        if hasattr(data, "__len__") and len(data) == 0:
            return self._fail(
                dataset_name,
                "Data is empty",
            )

        if required_fields:
            missing = self._check_required_fields(data, required_fields)
            if missing:
                return self._fail(
                    dataset_name,
                    "Missing required fields",
                    details={"missing_fields": missing},
                )

        return self._pass(
            dataset_name,
            "Basic validation passed",
        )

    # ---------------------------------------------------------------------
    # Internal helpers
    # ---------------------------------------------------------------------

    def _check_required_fields(
        self,
        data: Any,
        required_fields: List[str],
    ) -> List[str]:
        """
        Check required fields for dict-like or DataFrame-like objects.
        """
        missing: List[str] = []

        if isinstance(data, dict):
            for f in required_fields:
                if f not in data:
                    missing.append(f)
            return missing

        # DataFrame-like check
        if hasattr(data, "columns"):
            for f in required_fields:
                if f not in data.columns:
                    missing.append(f)
            return missing

        # Unsupported type: cannot verify fields
        return []

    def _pass(self, name: str, message: str) -> ValidationResult:
        if self.logger:
            self.logger.info(f"[DataValidator][PASS] {name}: {message}")
        return ValidationResult(
            status=ValidationStatus.PASS,
            message=message,
        )

    def _fail(
        self,
        name: str,
        message: str,
        details: Optional[Dict[str, Any]] = None,
    ) -> ValidationResult:
        if self.logger:
            self.logger.error(f"[DataValidator][FAIL] {name}: {message}")
        return ValidationResult(
            status=ValidationStatus.FAIL,
            message=message,
            details=details,
        )

    def _warn(
        self,
        name: str,
        message: str,
        details: Optional[Dict[str, Any]] = None,
    ) -> ValidationResult:
        if self.logger:
            self.logger.warning(f"[DataValidator][WARN] {name}: {message}")
        return ValidationResult(
            status=ValidationStatus.WARN,
            message=message,
            details=details,
        )
