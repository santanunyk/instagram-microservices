from fastapi import APIRouter, Request
from utils.service_client import forward_request
import os

router = APIRouter()
COMMENT_URL = os.getenv("COMMENT_URL")

@router.post("/{post_id}")
async def add_comment(post_id: str, req: Request):
    body = await req.json()
    return await forward_request("POST", f"{COMMENT_URL}/{post_id}", data=body)

