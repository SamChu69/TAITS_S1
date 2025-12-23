# -*- coding: utf-8 -*-
import ast
from .schema import RegimeContext

def classify_regime(evidence: dict) -> RegimeContext:
    analysis_ref = evidence.get("analysis_ref", "")
    
    # 從 analysis_ref 字串中解析出 close
    current_close = None
    try:
        if isinstance(analysis_ref, str):
            # 嘗試解析字串化的 dict
            parsed = ast.literal_eval(analysis_ref)
            if isinstance(parsed, dict):
                current_close = parsed.get("close")
    except:
        pass
    
    # 暫時使用固定值作為昨日 close（最小實現）
    # 實際應該從歷史資料或快照中取得
    prev_close = 500.0
    
    # 如果無法取得當前 close，使用預設值
    if current_close is None:
        current_close = prev_close
    
    # 判斷 regime
    # 先檢查波動幅度
    if prev_close > 0:
        change_ratio = abs(current_close - prev_close) / prev_close
        if change_ratio < 0.005:
            regime_type = "SIDEWAYS"
        elif current_close > prev_close:
            regime_type = "UP"
        else:
            regime_type = "DOWN"
    else:
        # prev_close 為 0 或負數時的處理
        if current_close > prev_close:
            regime_type = "UP"
        elif current_close < prev_close:
            regime_type = "DOWN"
        else:
            regime_type = "SIDEWAYS"
    
    return RegimeContext(
        regime_type=regime_type,
        description="price_based"
    )
