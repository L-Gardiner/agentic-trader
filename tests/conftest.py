import pytest
from pathlib import Path
import sys

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

@pytest.fixture
def test_data_dir():
    """Fixture providing path to test data directory."""
    return Path(__file__).parent / "fixtures" / "data"

@pytest.fixture
def mock_market_data():
    """Fixture providing sample market data."""
    return {
        "symbol": "BTC-USD",
        "timeframe": "1h",
        "data": [
            {"timestamp": "2025-01-01T00:00:00Z", "open": 100.0, "high": 101.0, "low": 99.0, "close": 100.5, "volume": 1000},
            {"timestamp": "2025-01-01T01:00:00Z", "open": 100.5, "high": 102.0, "low": 100.0, "close": 101.5, "volume": 1100},
        ]
    }

@pytest.fixture
def mock_api_client():
    """Fixture providing mock FastAPI test client."""
    from fastapi.testclient import TestClient
    from api.main import app
    return TestClient(app)
