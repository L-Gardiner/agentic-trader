from typing import Any, Dict

from domains.strategies.base.base_strategy import BaseStrategy


class TimeSeriesStrategy(BaseStrategy):
    """ML-based time series prediction strategy."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.model_uri = config["model_uri"]
        self.prediction_window = config.get("prediction_window", 5)
        self.confidence_threshold = config.get("confidence_threshold", 0.7)
        # Load model from registry
        self.model = None  # To be loaded from MLflow

    def generate_signals(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate trading signals based on ML predictions."""
        if not self.model:
            raise RuntimeError("Model not loaded")

        features = self._prepare_features(market_data)
        prediction = self.model.predict(features)
        confidence = self._calculate_confidence(prediction)

        if confidence < self.confidence_threshold:
            return {"signal": "hold", "confidence": confidence}

        return {
            "signal": "buy" if prediction > 0 else "sell",
            "confidence": confidence,
            "predicted_return": float(prediction),
        }

    def calculate_position_size(
        self, signal: Dict[str, Any], account_info: Dict[str, Any]
    ) -> float:
        """Calculate position size based on prediction confidence."""
        raise NotImplementedError()

    def _prepare_features(self, market_data: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare features for model prediction."""
        raise NotImplementedError()

    def _calculate_confidence(self, prediction: float) -> float:
        """Calculate confidence score for the prediction."""
        raise NotImplementedError()
