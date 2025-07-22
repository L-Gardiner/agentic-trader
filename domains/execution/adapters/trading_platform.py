from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime

class TradingPlatform(ABC):
    """Abstract base class for trading platform adapters."""
    
    @abstractmethod
    async def place_order(self, order_params: Dict[str, Any]) -> str:
        """Place an order on the trading platform."""
        pass

    @abstractmethod
    async def cancel_order(self, order_id: str) -> bool:
        """Cancel an existing order."""
        pass

    @abstractmethod
    async def get_order_status(self, order_id: str) -> Dict[str, Any]:
        """Get the current status of an order."""
        pass

    @abstractmethod
    async def get_account_balance(self) -> Dict[str, float]:
        """Get current account balances."""
        pass

    @abstractmethod
    async def get_market_price(self, symbol: str) -> Optional[float]:
        """Get current market price for a symbol."""
        pass

    @abstractmethod
    async def get_trading_fees(self, symbol: str) -> Dict[str, float]:
        """Get trading fees for a symbol."""
        pass
