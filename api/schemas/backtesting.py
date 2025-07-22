from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class BacktestRequest(BaseModel):
    strategy_id: str
    start_date: datetime
    end_date: datetime
    initial_capital: float
    instruments: List[str]
    parameters: Optional[dict] = None


class Trade(BaseModel):
    timestamp: datetime
    instrument: str
    side: str
    price: float
    quantity: float
    pnl: float


class BacktestResponse(BaseModel):
    strategy_id: str
    total_return: float
    sharpe_ratio: float
    max_drawdown: float
    trades: List[Trade]
    metrics: dict
