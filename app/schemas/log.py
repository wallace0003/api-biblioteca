from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime


class LogBase(BaseModel):
    event: str
    data: Optional[Dict[str, Any]] = None


class LogCreate(LogBase):
    pass


class LogResponse(LogBase):
    id: str = Field(alias="_id")
    created_at: datetime

    class Config:
        from_attributes = True
        populate_by_name = True


class LogFilter(BaseModel):
    event: Optional[str] = None
