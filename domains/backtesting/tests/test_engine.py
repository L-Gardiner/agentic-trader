import pytest
from datetime import datetime, timedelta
from ..core.engine import BacktestEngine

def test_backtest_engine_initialization():
    """Test BacktestEngine initialization with config."""
    config = {
        "initial_capital": 10000,
        "commission": 0.001,
        "slippage": 0.0005
    }
    engine = BacktestEngine(config)
    assert engine.initial_capital == 10000
    assert engine.commission == 0.001
    assert engine.slippage == 0.0005

@pytest.mark.asyncio
async def test_calculate_metrics():
    """Test backtest metrics calculation."""
    engine = BacktestEngine({"initial_capital": 10000})
    trades = [
        {"entry_price": 100, "exit_price": 110, "size": 1, "pnl": 10},
        {"entry_price": 110, "exit_price": 105, "size": 1, "pnl": -5}
    ]
    
    metrics = await engine._calculate_metrics(trades)
    assert "total_return" in metrics
    assert "win_rate" in metrics
    assert "sharpe_ratio" in metrics
    assert "max_drawdown" in metrics
