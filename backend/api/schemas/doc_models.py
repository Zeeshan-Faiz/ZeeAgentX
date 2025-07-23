from backend.api.schemas.chat_models import ModelName
from datetime import datetime
from pydantic import BaseModel

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime

class DeleteFileRequest(BaseModel):
    file_id: int