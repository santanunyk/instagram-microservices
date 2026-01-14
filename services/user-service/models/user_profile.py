from pydantic import BaseModel
from typing import List, Optional

class UserProfile(BaseModel):
    username: str
    bio: Optional[str] = ""
    avatar: Optional[str] = None  # path to profile image
    followers: List[str] = []
    following: List[str] = []

