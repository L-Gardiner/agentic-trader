from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from api.routes import (
    agents,
    backtesting,
    execution,
    ml_pipeline,
    sentiment,
    strategies,
)

app = FastAPI(
    title="Agentic Trader API",
    description="Trading bot platform with ML/AI capabilities",
    version="0.1.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    backtesting.router, prefix="/api/v1/backtesting", tags=["backtesting"]
)
app.include_router(execution.router, prefix="/api/v1/execution", tags=["execution"])
app.include_router(ml_pipeline.router, prefix="/api/v1/ml", tags=["ml_pipeline"])
app.include_router(sentiment.router, prefix="/api/v1/sentiment", tags=["sentiment"])
app.include_router(agents.router, prefix="/api/v1/agents", tags=["agents"])
app.include_router(strategies.router, prefix="/api/v1/strategies", tags=["strategies"])


@app.get("/health")
async def health_check():
    return {"status": "healthy"}
