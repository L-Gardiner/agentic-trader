from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class SentimentSource(str, Enum):
    NEWS = "news"
    TWITTER = "twitter"
    REDDIT = "reddit"
    RSS = "rss"


class SentimentLevel(int, Enum):
    VERY_NEGATIVE = -2
    NEGATIVE = -1
    NEUTRAL = 0
    POSITIVE = 1
    VERY_POSITIVE = 2


class SentimentRequest(BaseModel):
    symbols: List[str]
    sources: List[SentimentSource]
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class SourceSentiment(BaseModel):
    source: SentimentSource
    sentiment: SentimentLevel
    confidence: float
    text: str
    url: Optional[str]
    timestamp: datetime


class SentimentResponse(BaseModel):
    symbol: str
    aggregate_sentiment: float
    confidence: float
    sources: List[SourceSentiment]
    analysis_timestamp: datetime = Field(default_factory=datetime.now)
