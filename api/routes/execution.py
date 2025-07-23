from fastapi import APIRouter, HTTPException
from api.schemas.execution import OrderRequest, OrderResponse

router = APIRouter()

@router.post("/order", response_model=OrderResponse)
async def place_order(request: OrderRequest):
    """Place a trading order through the selected platform adapter."""
    raise HTTPException(status_code=501, detail="Not implemented")
