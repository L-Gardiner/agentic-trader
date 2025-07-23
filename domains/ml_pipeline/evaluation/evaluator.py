from datetime import datetime
from typing import Any, Dict, List

import mlflow
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


class ModelEvaluator:
    """Evaluates ML models for trading strategies."""

    def __init__(self, metrics_config: Dict[str, Any]):
        self.metrics_config = metrics_config

    def evaluate_predictions(
        self, y_true: np.ndarray, y_pred: np.ndarray, sample_weights: np.ndarray = None
    ) -> Dict[str, float]:
        """Calculate model performance metrics."""
        metrics = {
            "mse": mean_squared_error(y_true, y_pred, sample_weight=sample_weights),
            "rmse": np.sqrt(
                mean_squared_error(y_true, y_pred, sample_weight=sample_weights)
            ),
            "mae": mean_absolute_error(y_true, y_pred, sample_weight=sample_weights),
            "r2": r2_score(y_true, y_pred, sample_weight=sample_weights),
        }
        return metrics

    def evaluate_trading_performance(
        self,
        predictions: np.ndarray,
        actual_returns: np.ndarray,
        timestamps: List[datetime],
    ) -> Dict[str, float]:
        """Evaluate model performance in trading context."""
        raise NotImplementedError()

    def log_metrics(self, run_id: str, metrics: Dict[str, float]):
        """Log metrics to MLflow."""
        with mlflow.start_run(run_id=run_id):
            mlflow.log_metrics(metrics)
