from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class NoteCreate(BaseModel):
    userName: str
    title: str
    description: str

class NoteResponse(BaseModel):
    id: int
    userName: str
    title: str
    description: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True