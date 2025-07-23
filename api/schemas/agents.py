from datetime import datetime
from typing import Dict, Any, Optional, List
from enum import Enum
from pydantic import BaseModel, Field

class AgentType(str, Enum):
    FOREX = "forex"
    CRYPTO = "crypto"
    STOCK = "stock"
    COMMODITY = "commodity"
    PORTFOLIO = "portfolio"

class AgentState(str, Enum):
    IDLE = "idle"
    ANALYZING = "analyzing"
    EXECUTING = "executing"
    COOLING_DOWN = "cooling_down"
    ERROR = "error"

class AgentRequest(BaseModel):
    agent_type: AgentType
    symbols: List[str]
    parameters: Dict[str, Any]
    risk_limit: float
    max_position_size: float
    time_horizon: str

class AgentResponse(BaseModel):
    agent_id: str
    agent_type: AgentType
    state: AgentState
    current_positions: Dict[str, float]
    last_action: Optional[Dict[str, Any]]
    performance_metrics: Dict[str, float]
    timestamp: datetime = Field(default_factory=datetime.now)
