from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class StrategyType(str, Enum):
    MOVING_AVERAGE = "moving_average"
    RSI = "rsi"
    MACD = "macd"
    BOLLINGER = "bollinger"
    ML_PREDICTION = "ml_prediction"
    SENTIMENT = "sentiment"
    REINFORCEMENT = "reinforcement"
    ENSEMBLE = "ensemble"


class SignalType(str, Enum):
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"


class StrategyRequest(BaseModel):
    strategy_type: StrategyType
    symbols: List[str]
    parameters: Dict[str, Any]
    timeframe: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class Signal(BaseModel):
    symbol: str
    signal_type: SignalType
    confidence: float
    price: float
    timestamp: datetime
    metadata: Optional[Dict[str, Any]] = None


class StrategyResponse(BaseModel):
    strategy_id: str
    strategy_type: StrategyType
    signals: List[Signal]
    performance_metrics: Dict[str, float]
    analysis_timestamp: datetime = Field(default_factory=datetime.now)
