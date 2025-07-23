from fastapi import APIRouter, HTTPException
from api.schemas.backtesting import BacktestRequest, BacktestResponse

router = APIRouter()

@router.post("/run", response_model=BacktestResponse)
async def run_backtest(request: BacktestRequest):
    """Run a backtest simulation for a given strategy."""
    raise HTTPException(status_code=501, detail="Not implemented")
