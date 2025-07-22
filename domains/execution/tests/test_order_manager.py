from decimal import Decimal

import pytest

from ..core.order_manager import OrderManager


def test_order_manager_initialization():
    """Test OrderManager initialization."""
    config = {"max_orders": 10, "default_timeout": 30}
    manager = OrderManager(config)
    assert manager.max_orders == 10
    assert manager.default_timeout == 30


@pytest.mark.asyncio
async def test_place_order():
    """Test order placement."""
    manager = OrderManager({"max_orders": 10})

    order = {
        "symbol": "BTC-USD",
        "side": "buy",
        "type": "limit",
        "price": Decimal("50000"),
        "quantity": Decimal("0.1"),
    }

    order_id = await manager.place_order(order)
    assert order_id is not None

    # Check order tracking
    active_orders = await manager.get_active_orders()
    assert order_id in active_orders


@pytest.mark.asyncio
async def test_order_validation():
    """Test order validation rules."""
    manager = OrderManager({"max_orders": 1})

    # Test max orders limit
    order1 = {"symbol": "BTC-USD", "side": "buy", "quantity": Decimal("0.1")}
    order2 = {"symbol": "ETH-USD", "side": "buy", "quantity": Decimal("1.0")}

    await manager.place_order(order1)
    with pytest.raises(ValueError):
        await manager.place_order(order2)  # Should exceed max orders
