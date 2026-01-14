from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    username: str
    caption: Optional[str] = ""

class PostOut(BaseModel):
    id: str
    username: str
    caption: str
    media_url: str
    created_at: datetime

