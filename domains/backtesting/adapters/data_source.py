from abc import ABC, abstractmethod
from typing import Dict, Any, List
from datetime import datetime

class MarketDataSource(ABC):
    """Abstract base class for market data sources."""
    
    @abstractmethod
    async def fetch_historical_data(
        self,
        symbol: str,
        start_date: datetime,
        end_date: datetime,
        timeframe: str
    ) -> List[Dict[str, Any]]:
        """Fetch historical market data for a given symbol and timeframe."""
        pass

    @abstractmethod
    async def get_available_symbols(self) -> List[str]:
        """Get list of available trading symbols."""
        pass

    @abstractmethod
    async def get_available_timeframes(self) -> List[str]:
        """Get list of available timeframes."""
        pass
