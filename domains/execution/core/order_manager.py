from enum import Enum
from typing import Any, Dict, Optional


class OrderStatus(Enum):
    PENDING = "pending"
    FILLED = "filled"
    CANCELLED = "cancelled"
    REJECTED = "rejected"


class OrderManager:
    """Core order management system."""

    def __init__(self):
        self.active_orders: Dict[str, Dict[str, Any]] = {}
        self.positions: Dict[str, float] = {}

    async def place_order(self, platform: str, order_params: Dict[str, Any]) -> str:
        """Place an order through the specified platform adapter."""
        raise NotImplementedError()

    async def cancel_order(self, order_id: str) -> bool:
        """Cancel an active order."""
        raise NotImplementedError()

    async def get_order_status(self, order_id: str) -> Optional[OrderStatus]:
        """Get the current status of an order."""
        raise NotImplementedError()
