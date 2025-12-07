# 📘 **C-29：Logging & Monitoring（紀錄、監控、告警總設計）**

這一章是 TAITS_S1 的「黑盒子透明化系統」。
目標是：**任何錯誤、任何決策、任何下單、任何異常 → 你事後都找得到「發生什麼事、為什麼、在哪裡」。**

---

## 🧩 C-29.1 角色 & 目標

Logging / Monitoring 在 TAITS_S1 中負責：

1. **系統紀錄（System Logging）**

   * Orchestrator 執行狀態
   * DataSource 成功/失敗
   * Indicator / Strategy / Agent 執行關鍵點
2. **交易紀錄（Trading Logs）**

   * 每一筆委託 / 成交 / 取消 / 風控介入
3. **風險與錯誤（Risk & Errors）**

   * 連線錯誤、API 失敗
   * 策略輸出異常（NaN、inf、錯誤 signal）
   * 回測與實盤結果異常（極端虧損、滑價異常）
4. **監控與告警（Monitoring / Alerts）**

   * 日內最大虧損超標
   * 富邦 API 無回應
   * 資料源連續失敗
   * Agent / Orchestrator crash

---

## 🧩 C-29.2 目錄結構（Logging & Monitoring 層）

```bash
/config/
    config.yaml
    profiles/
        dev.yaml
        backtest.yaml
        sandbox.yaml
        live.yaml

/logs/
    system/
        system_2025-12-05.log
    trading/
        trading_2025-12-05.log
    backtest/
        backtest_2025-12-05.log
    alerts/
        alerts_2025-12-05.log

/monitoring/
    __init__.py
    logger.py           # 封裝 logging.getLogger
    trade_logger.py     # 專門記錄交易事件
    metrics.py          # 統計指標、即時指標（虧損、風險）
    alert_manager.py    # 發送告警（目前可以先 print / 之後再接 Telegram / Email）
```

---

## 🧩 C-29.3 logging 設計原則

1. **所有模組不直接 new Logger**
   一律透過 `monitoring.logger.get_logger(name)` 取得統一設定後的 logger。

2. **分類 Log 檔**：

   * `/logs/system/`：系統執行狀態、錯誤
   * `/logs/trading/`：策略信號、送單、成交、風控
   * `/logs/backtest/`：回測整體紀錄、績效摘要
   * `/logs/alerts/`：告警事件（觸發止損、API fail 等）

3. **等級使用**：

   * `DEBUG`：開發用，細節資訊（指標結果、DataFrame shape）
   * `INFO`：正常流程關鍵資訊（啟動、完成、每日結算）
   * `WARNING`：可恢復問題（某個 DataSource 失敗但 fallback 成功）
   * `ERROR`：功能受影響（策略無法執行、API 連線失敗）
   * `CRITICAL`：需要人工處理（Live 模式停擺、風險爆表）

4. **可由 config 控制**：

   * `logging.level`：DEBUG / INFO / WARNING…
   * 是否存 JSON（方便未來接 ELK / Loki / ClickHouse）
   * 是否 rotate（按日分檔）

---

## 🧩 C-29.4 `monitoring/logger.py`（統一 Logger 入口）

📁 `monitoring/logger.py`

```python
import logging
import os
from datetime import datetime
from config.settings import ConfigLoader


def _ensure_log_dirs():
    base = "logs"
    subdirs = ["system", "trading", "backtest", "alerts"]
    os.makedirs(base, exist_ok=True)
    for s in subdirs:
        os.makedirs(os.path.join(base, s), exist_ok=True)


def _build_file_handler(log_type: str, level: int):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join("logs", log_type, f"{log_type}_{today}.log")
    fh = logging.FileHandler(filename, encoding="utf-8")
    fh.setLevel(level)
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    fh.setFormatter(formatter)
    return fh


_cfg_cache = None
def _get_cfg():
    global _cfg_cache
    if _cfg_cache is None:
        _cfg_cache = ConfigLoader().load()
    return _cfg_cache


def get_logger(name: str, log_type: str = "system") -> logging.Logger:
    """
    log_type: system / trading / backtest / alerts
    """
    _ensure_log_dirs()
    cfg = _get_cfg()

    logger = logging.getLogger(name)
    if logger.handlers:
        # 已初始化
        return logger

    level_str = cfg.logging.level.upper()
    level = getattr(logging, level_str, logging.INFO)
    logger.setLevel(level)

    # console handler
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch_fmt = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%H:%M:%S",
    )
    ch.setFormatter(ch_fmt)
    logger.addHandler(ch)

    # file handler
    fh = _build_file_handler(log_type, level)
    logger.addHandler(fh)

    logger.propagate = False
    return logger
```

---

## 🧩 C-29.5 `trade_logger.py`（專門記錄交易事件）

📁 `monitoring/trade_logger.py`

```python
from dataclasses import dataclass, asdict
from datetime import datetime
from monitoring.logger import get_logger

_trade_log = get_logger("trading", log_type="trading")


@dataclass
class TradeEvent:
    timestamp: str
    mode: str           # backtest / sandbox / live
    symbol: str
    action: str         # BUY / SELL / SHORT / COVER
    qty: int
    price: float
    reason: str         # 來自哪個策略 / Agent
    order_id: str = ""
    extra: dict = None


def log_trade_event(event: TradeEvent):
    data = asdict(event)
    _trade_log.info(f"TRADE_EVENT | {data}")


def log_order_rejected(order_id: str, reason: str, symbol: str, qty: int):
    _trade_log.warning(
        f"ORDER_REJECTED | order_id={order_id} | symbol={symbol} | qty={qty} | reason={reason}"
    )


def log_risk_block(symbol: str, reason: str):
    _trade_log.warning(f"RISK_BLOCK | symbol={symbol} | reason={reason}")
```

> 🔹 用法：由 `OrderManager` / `RiskManager` / `Orchestrator` 在關鍵事件時呼叫。

---

## 🧩 C-29.6 `metrics.py`（風險與績效即時統計）

📁 `monitoring/metrics.py`

```python
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class RiskMetrics:
    day_pnl: float = 0.0
    max_drawdown: float = 0.0
    exposure: float = 0.0
    num_trades: int = 0
    winning_trades: int = 0
    losing_trades: int = 0

    def record_trade(self, pnl: float):
        self.day_pnl += pnl
        self.num_trades += 1
        if pnl > 0:
            self.winning_trades += 1
        elif pnl < 0:
            self.losing_trades += 1
        # max_drawdown 之後可加 equity 曲線計算

    @property
    def win_rate(self) -> float:
        if self.num_trades == 0:
            return 0.0
        return self.winning_trades / self.num_trades


class MetricsStore:
    """
    簡單 in-memory 指標儲存，可未來換成 Prometheus / InfluxDB。
    """
    def __init__(self):
        self.risk = RiskMetrics()
        self.custom: Dict[str, float] = {}

    def set_metric(self, name: str, value: float):
        self.custom[name] = value

    def get_metric(self, name: str, default=None):
        return self.custom.get(name, default)


metrics = MetricsStore()
```

---

## 🧩 C-29.7 `alert_manager.py`（告警系統雛形）

📁 `monitoring/alert_manager.py`

```python
from monitoring.logger import get_logger
from monitoring.metrics import metrics
from config.settings import ConfigLoader

_alert_log = get_logger("alerts", log_type="alerts")


class AlertManager:
    """
    未來可以接：
      - Telegram Bot
      - Email
      - Discord / LINE Notify
    目前先用 log + print
    """
    def __init__(self):
        self.cfg = ConfigLoader().load()

    def alert(self, message: str, level: str = "WARNING"):
        text = f"[ALERT][{level}] {message}"
        _alert_log.warning(text)
        print(text)

    def check_daily_loss(self):
        max_loss = self.cfg.trading.max_loss_day
        if metrics.risk.day_pnl <= max_loss:
            self.alert(
                f"日內虧損 {metrics.risk.day_pnl} 已超過上限 {max_loss}，建議停止交易。",
                level="CRITICAL",
            )

    def notify_api_down(self, api_name: str):
        self.alert(f"{api_name} 連線失敗，已啟用 fallback 或建議人工檢查。", level="ERROR")
```

---

## 🧩 C-29.8 Orchestrator / Engine 如何串 Logging？

### 在 Orchestrator 裡：

```python
# engine/orchestrator.py
from monitoring.logger import get_logger
from monitoring.alert_manager import AlertManager
from monitoring.metrics import metrics

class Orchestrator:
    def __init__(self):
        self.logger = get_logger("orchestrator", log_type="system")
        self.alerts = AlertManager()

    def run(self):
        self.logger.info("Orchestrator started")

        try:
            # load data
            self.logger.info("Loading data...")
            # ...
            # run strategies / agents
            self.logger.info("Running strategies & agents...")
            # ...
            # risk checks
            self.alerts.check_daily_loss()
        except Exception as e:
            self.logger.exception(f"Orchestrator crashed: {e}")
            self.alerts.alert("Orchestrator 發生嚴重錯誤，系統已停止。", level="CRITICAL")
```

### 在 OrderManager 裡：

```python
# trading/order_manager.py
from monitoring.trade_logger import log_trade_event, TradeEvent
from config.settings import ConfigLoader
from datetime import datetime

class OrderManager:
    def __init__(self):
        self.cfg = ConfigLoader().load()

    def send_order(self, symbol: str, action: str, qty: int, price: float, reason: str):
        # TODO: 接富邦 / sandbox 實作
        event = TradeEvent(
            timestamp=datetime.now().isoformat(),
            mode=self.cfg.trading.mode,
            symbol=symbol,
            action=action,
            qty=qty,
            price=price,
            reason=reason,
        )
        log_trade_event(event)
```

---

## 🧩 C-29.9 Logging 與 Config 的關係

在 `config/config.yaml` 中你已經有：

```yaml
logging:
  level: "INFO"
  save_json: true
  rotate: true
```

未來你可以加：

```yaml
logging:
  level: "DEBUG"
  save_json: true
  rotate: true
  show_backtest_detail: false
  show_live_only: true
```

然後在 `logger.py` / `backtester.py` 裡，用設定來控制要不要輸出大量細節。

---

## 🧩 C-29.10 未來升級方向（預留）

1. **接 Prometheus / Grafana**

   * 把 `metrics` 改成對外暴露 HTTP `/metrics`。
2. **接 ELK / Loki / ClickHouse**

   * `save_json = true` 時，log 格式改為 JSON，方便集中查詢。
3. **Live Trading 告警自動化**

   * 當 `mode=live` 並且 `AlertManager` 發出 `CRITICAL` 時，自動：

     * 把 `trading.enabled = false`
     * 或直接不再送新單，只允許平倉。

---

## ✅ C-29 完成狀態（10/10）

你現在擁有的東西：

* 一套 **完整 logging 架構**（system / trading / backtest / alerts）
* 一個 **統一 Logger 入口**（不會混亂亂 new logger）
* 交易專用 `TradeEvent` 結構，可查每筆交易的：

  * 時間 / 模式 / 價格 / 數量 / 策略來源
* `Metrics` + `AlertManager`：

  * 可以監控日內虧損
  * 未來可接 Telegram / Email / LINE
* 與 `Orchestrator` / `OrderManager` 已經完成最小整合示範

---
