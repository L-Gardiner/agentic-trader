import pytest
from datetime import datetime
from ..analysis.analyzer import SentimentAnalyzer

def test_sentiment_analyzer_initialization():
    """Test SentimentAnalyzer initialization."""
    config = {
        "model_name": "finbert",
        "threshold": 0.5
    }
    analyzer = SentimentAnalyzer(config)
    assert analyzer.threshold == 0.5

@pytest.mark.asyncio
async def test_analyze_text():
    """Test text sentiment analysis."""
    analyzer = SentimentAnalyzer({"model_name": "finbert"})
    text = "The company reported strong earnings growth."
    
    result = await analyzer.analyze_text(text)
    assert "sentiment" in result
    assert "score" in result
    assert "confidence" in result
    assert result["sentiment"] in ["positive", "negative", "neutral"]
    assert 0 <= result["confidence"] <= 1

@pytest.mark.asyncio
async def test_aggregate_sentiment():
    """Test sentiment aggregation over multiple texts."""
    analyzer = SentimentAnalyzer({"model_name": "finbert"})
    texts = [
        "Strong market performance",
        "Concerning economic indicators",
        "Stable growth reported"
    ]
    
    aggregated = await analyzer.aggregate_sentiment(texts)
    assert "overall_sentiment" in aggregated
    assert "confidence" in aggregated
    assert "breakdown" in aggregated
