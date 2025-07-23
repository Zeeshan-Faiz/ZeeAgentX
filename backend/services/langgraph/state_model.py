from typing import Optional
from pydantic import BaseModel

# Define state model for LangGraph
class AgentState(BaseModel):
    query: str
    response: Optional[str] = None
    route: Optional[str] = None  # Expected: "rag", "agent", or "clarify"
    context: Optional[dict] = None