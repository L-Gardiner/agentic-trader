from typing import Dict, Any, List, Optional
from datetime import datetime
from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    """Base class for all trading strategies."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.position: Dict[str, float] = {}
        self.last_update: Optional[datetime] = None

    @abstractmethod
    def generate_signals(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate trading signals from market data."""
        pass

    @abstractmethod
    def calculate_position_size(self, signal: Dict[str, Any], 
                              account_info: Dict[str, Any]) -> float:
        """Calculate position size based on signal and account information."""
        pass

    def validate_signal(self, signal: Dict[str, Any]) -> bool:
        """Validate a trading signal against risk management rules."""
        raise NotImplementedError()

    def get_parameters(self) -> Dict[str, Any]:
        """Get strategy parameters."""
        return self.config

    def update_parameters(self, new_params: Dict[str, Any]):
        """Update strategy parameters."""
        self.config.update(new_params)
        self.last_update = datetime.now()
