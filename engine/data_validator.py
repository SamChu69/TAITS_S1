# engine/data_validator.py
# ============================================================
# TAITS – 資料檢查模組（Data Validator）
# 負責在進入指標 / 策略 / Agents 之前，先檢查原始 K 線資料是否合格
# ============================================================

from typing import Tuple
import pandas as pd


class DataValidator:
    """
    TAITS S1 資料檢查器

    主要功能：
    1. 確認 DataFrame 不為空
    2. 檢查必要欄位是否存在（open, high, low, close, volume）
    3. 檢查是否有明顯異常值（NaN / 無窮大 等）
    4. 預留未來可加入更多檢查（例如：日期排序、跳價檢查、停牌處理）

    回傳：
        (ok: bool, message: str)
    """

    def __init__(self) -> None:
        self.required_columns = ["open", "high", "low", "close", "volume"]

    # --------------------------------------------------------
    # 對外主入口
    # --------------------------------------------------------
    def validate(self, df: pd.DataFrame) -> Tuple[bool, str]:
        """
        檢查整體資料是否合格。
        """
        if df is None:
            return False, "DataFrame 為 None"

        if not isinstance(df, pd.DataFrame):
            return False, "輸入不是 pandas DataFrame"

        if df.empty:
            return False, "DataFrame 為空"

        # 檢查必要欄位
        missing = [c for c in self.required_columns if c not in df.columns]
        if missing:
            return False, f"缺少必要欄位：{missing}"

        # 檢查 NaN / Inf
        if df[self.required_columns].isna().any().any():
            return False, "K 線欄位中存在 NaN"

        if not df.index.is_monotonic_increasing:
            # 不算致命錯誤，只是提醒
            df.sort_index(inplace=True)

        return True, "OK"
