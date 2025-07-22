from fastapi import APIRouter, HTTPException

from api.schemas.ml_pipeline import ModelPredictRequest, ModelTrainRequest

router = APIRouter()


@router.post("/train")
async def train_model(request: ModelTrainRequest):
    """Train a new ML model with provided data."""
    raise HTTPException(status_code=501, detail="Not implemented")


@router.post("/predict")
async def get_prediction(request: ModelPredictRequest):
    """Get predictions from a trained model."""
    raise HTTPException(status_code=501, detail="Not implemented")
