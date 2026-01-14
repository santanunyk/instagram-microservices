from fastapi import APIRouter, Request
from utils.service_client import forward_request
import os

router = APIRouter()
POST_URL = os.getenv("POST_URL")

@router.post("/")
async def create_post(req: Request):
    body = await req.json()
    return await forward_request("POST", f"{POST_URL}/", data=body)

@router.get("/{post_id}")
async def get_post(post_id: str):
    return await forward_request("GET", f"{POST_URL}/{post_id}")

