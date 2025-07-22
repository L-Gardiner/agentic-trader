from typing import Any, Dict

import numpy as np

from domains.strategies.base.base_strategy import BaseStrategy


class MovingAverageStrategy(BaseStrategy):
    """Moving Average Crossover trading strategy."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.short_window = config.get("short_window", 20)
        self.long_window = config.get("long_window", 50)

    def generate_signals(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate trading signals based on MA crossover."""
        prices = market_data.get("close_prices", [])
        if len(prices) < self.long_window:
            return {"signal": "hold", "confidence": 0.0}

        # Calculate moving averages
        short_ma = np.mean(prices[-self.short_window :])
        long_ma = np.mean(prices[-self.long_window :])

        # Generate signals
        if short_ma > long_ma:
            return {"signal": "buy", "confidence": 0.7}
        elif short_ma < long_ma:
            return {"signal": "sell", "confidence": 0.7}
        return {"signal": "hold", "confidence": 0.5}

    def calculate_position_size(
        self, signal: Dict[str, Any], account_info: Dict[str, Any]
    ) -> float:
        """Calculate position size based on signal confidence."""
        raise NotImplementedError()
