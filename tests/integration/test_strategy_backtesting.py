from datetime import datetime, timedelta

from domains.backtesting.core.engine import BacktestEngine
from domains.strategies.rule_based.moving_average import MovingAverageStrategy


async def test_strategy_backtest_integration(mock_market_data):
    """Test integration between strategy and backtest engine."""
    # Setup
    strategy = MovingAverageStrategy({"short_window": 2, "long_window": 5})

    engine = BacktestEngine({"initial_capital": 10000, "commission": 0.001})

    # Run backtest
    results = await engine.run(
        strategy=strategy,
        market_data=mock_market_data,
        start_time=datetime.now() - timedelta(days=30),
        end_time=datetime.now(),
    )

    # Verify results structure
    assert "trades" in results
    assert "metrics" in results
    assert "equity_curve" in results

    # Verify basic metrics
    metrics = results["metrics"]
    assert "total_return" in metrics
    assert "sharpe_ratio" in metrics
    assert "max_drawdown" in metrics
