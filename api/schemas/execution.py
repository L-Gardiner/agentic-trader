from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class OrderType(str, Enum):
    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"
    STOP_LIMIT = "stop_limit"


class OrderSide(str, Enum):
    BUY = "buy"
    SELL = "sell"


class OrderRequest(BaseModel):
    platform: str
    symbol: str
    order_type: OrderType
    side: OrderSide
    quantity: float
    price: Optional[float] = None
    stop_price: Optional[float] = None
    time_in_force: Optional[str] = "GTC"


class OrderResponse(BaseModel):
    order_id: str
    platform: str
    symbol: str
    status: str
    filled_quantity: float = 0
    filled_price: Optional[float] = None
    timestamp: datetime = Field(default_factory=datetime.now)
