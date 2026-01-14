from fastapi import APIRouter
from utils.service_client import forward_request
import os

router = APIRouter()
LIKE_URL = os.getenv("LIKE_URL")

@router.post("/{post_id}")
async def like_post(post_id: str):
    return await forward_request("POST", f"{LIKE_URL}/{post_id}")

