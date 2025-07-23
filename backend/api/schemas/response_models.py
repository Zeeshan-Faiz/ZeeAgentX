from pydantic import BaseModel, Field
from backend.api.schemas.chat_models import ModelName

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None)
    model: ModelName = Field(default=ModelName.GPT_4_1)

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName