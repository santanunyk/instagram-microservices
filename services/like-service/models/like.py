from pydantic import BaseModel

class LikeCreate(BaseModel):
    username: str

