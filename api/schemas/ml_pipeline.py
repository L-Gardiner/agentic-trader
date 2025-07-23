from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class ModelTrainRequest(BaseModel):
    model_name: str
    model_version: str
    dataset_path: str
    parameters: Dict[str, Any]
    features: List[str]
    target: str
    validation_split: float = 0.2
    test_split: Optional[float] = 0.1


class ModelPredictRequest(BaseModel):
    model_uri: str
    features: Dict[str, List[float]]


class ModelMetrics(BaseModel):
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    training_time: float
    timestamp: datetime = Field(default_factory=datetime.now)


class ModelResponse(BaseModel):
    model_uri: str
    metrics: ModelMetrics
    parameters: Dict[str, Any]
    feature_importance: Optional[Dict[str, float]]
