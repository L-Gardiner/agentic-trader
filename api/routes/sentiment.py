from fastapi import APIRouter, HTTPException
from api.schemas.sentiment import SentimentRequest, SentimentResponse

router = APIRouter()

@router.post("/analyze", response_model=SentimentResponse)
async def analyze_sentiment(request: SentimentRequest):
    """Analyze sentiment from news and social media sources."""
    raise HTTPException(status_code=501, detail="Not implemented")
