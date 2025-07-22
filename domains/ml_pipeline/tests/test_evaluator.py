import pytest
import numpy as np
from ..evaluation.evaluator import ModelEvaluator

def test_model_evaluator_metrics():
    """Test model evaluation metrics calculation."""
    evaluator = ModelEvaluator(metrics_config={})
    
    # Test data
    y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y_pred = np.array([1.1, 2.1, 3.1, 4.1, 5.1])
    
    metrics = evaluator.evaluate_predictions(y_true, y_pred)
    
    assert "mse" in metrics
    assert "rmse" in metrics
    assert "mae" in metrics
    assert "r2" in metrics
    
    # Basic sanity checks
    assert metrics["mse"] > 0
    assert metrics["rmse"] > 0
    assert metrics["mae"] > 0
    assert metrics["r2"] <= 1.0

def test_model_evaluator_weighted_metrics():
    """Test weighted metrics calculation."""
    evaluator = ModelEvaluator(metrics_config={})
    
    y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y_pred = np.array([1.1, 2.1, 3.1, 4.1, 5.1])
    weights = np.array([1.0, 0.5, 1.0, 0.5, 1.0])
    
    weighted_metrics = evaluator.evaluate_predictions(
        y_true, y_pred, sample_weights=weights
    )
    unweighted_metrics = evaluator.evaluate_predictions(
        y_true, y_pred
    )
    
    # Metrics should be different with weights
    assert weighted_metrics["mse"] != unweighted_metrics["mse"]
