from fastapi import APIRouter, HTTPException

from api.schemas.strategies import StrategyRequest, StrategyResponse

router = APIRouter()


@router.post("/evaluate", response_model=StrategyResponse)
async def evaluate_strategy(request: StrategyRequest):
    """Evaluate a trading strategy with given parameters."""
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/list")
async def list_strategies():
    """List all available trading strategies."""
    raise HTTPException(status_code=501, detail="Not implemented")
