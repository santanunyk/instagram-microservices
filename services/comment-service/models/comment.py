from pydantic import BaseModel
from datetime import datetime

class CommentCreate(BaseModel):
    username: str
    text: str

class CommentOut(BaseModel):
    id: str
    post_id: str
    username: str
    text: str
    created_at: datetime

