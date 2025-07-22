from fastapi import APIRouter, HTTPException

from api.schemas.agents import AgentRequest, AgentResponse

router = APIRouter()


@router.post("/execute", response_model=AgentResponse)
async def execute_agent(request: AgentRequest):
    """Execute an agent's trading strategy."""
    raise HTTPException(status_code=501, detail="Not implemented")


@router.get("/status/{agent_id}")
async def get_agent_status(agent_id: str):
    """Get the current status of a running agent."""
    raise HTTPException(status_code=501, detail="Not implemented")
