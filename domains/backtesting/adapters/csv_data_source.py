from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

from .data_source import MarketDataSource


class CSVDataSource(MarketDataSource):
    """CSV file-based market data source."""

    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self._available_symbols = None
        self._available_timeframes = None

    async def fetch_historical_data(
        self, symbol: str, start_date: datetime, end_date: datetime, timeframe: str
    ) -> List[Dict[str, Any]]:
        """Fetch historical market data from CSV files."""
        file_path = self.data_dir / f"{symbol}_{timeframe}.csv"
        if not file_path.exists():
            raise FileNotFoundError(
                f"No data file found for {symbol} with timeframe {timeframe}"
            )

        # Read CSV file
        df = pd.read_csv(file_path)
        df["timestamp"] = pd.to_datetime(df["timestamp"])

        # Filter by date range
        mask = (df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)
        filtered_df = df.loc[mask]

        # Convert to list of dictionaries
        return filtered_df.to_dict("records")

    async def get_available_symbols(self) -> List[str]:
        """Get list of available trading symbols from CSV files."""
        if self._available_symbols is None:
            self._available_symbols = list(
                {f.stem.split("_")[0] for f in self.data_dir.glob("*.csv")}
            )
        return self._available_symbols

    async def get_available_timeframes(self) -> List[str]:
        """Get list of available timeframes from CSV files."""
        if self._available_timeframes is None:
            self._available_timeframes = list(
                {f.stem.split("_")[1] for f in self.data_dir.glob("*.csv")}
            )
        return self._available_timeframes
