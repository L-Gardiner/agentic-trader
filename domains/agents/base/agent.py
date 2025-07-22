from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional


class AgentState(Enum):
    IDLE = "idle"
    ANALYZING = "analyzing"
    EXECUTING = "executing"
    COOLING_DOWN = "cooling_down"
    ERROR = "error"


class BaseAgent:
    """Base class for all trading agents."""

    def __init__(self, agent_id: str, config: Dict[str, Any]):
        self.agent_id = agent_id
        self.config = config
        self.state = AgentState.IDLE
        self.last_action_time: Optional[datetime] = None

    async def analyze_market(self) -> Dict[str, Any]:
        """Analyze current market conditions."""
        raise NotImplementedError()

    async def make_decision(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
        """Make trading decisions based on market analysis."""
        raise NotImplementedError()

    async def execute_decision(self, decision: Dict[str, Any]) -> bool:
        """Execute a trading decision."""
        raise NotImplementedError()

    async def run_loop(self):
        """Main agent loop."""
        try:
            self.state = AgentState.ANALYZING
            market_data = await self.analyze_market()

            self.state = AgentState.EXECUTING
            decision = await self.make_decision(market_data)
            success = await self.execute_decision(decision)

            self.state = AgentState.COOLING_DOWN
            self.last_action_time = datetime.now()
            return success
        except Exception as e:
            self.state = AgentState.ERROR
            raise e
