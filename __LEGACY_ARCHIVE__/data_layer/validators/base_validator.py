"""
TAITS BaseValidator (S2 Skeleton)

責任：
- 根據 TAITS_Data_Validation_Rules.md
- 回傳 ValidationReport（OK/WARN/BLOCK）
"""

class BaseValidator:
    def validate(self, normalized_frame):
        """
        回傳 ValidationReport dict
        """
        raise NotImplementedError("S2 skeleton: no validation implemented")
