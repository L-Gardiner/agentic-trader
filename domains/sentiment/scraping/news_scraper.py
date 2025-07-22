from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, List


class NewsScraper(ABC):
    """Base class for news data scrapers."""

    @abstractmethod
    async def fetch_news(
        self, symbols: List[str], start_time: datetime, end_time: datetime
    ) -> List[Dict[str, Any]]:
        """Fetch news articles for given symbols within timeframe."""
        pass

    @abstractmethod
    async def get_sources(self) -> List[str]:
        """Get list of available news sources."""
        pass
