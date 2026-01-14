from fastapi import APIRouter, Request
from utils.service_client import forward_request
import os

router = APIRouter()
USER_URL = os.getenv("USER_URL")

@router.get("/{username}")
async def get_profile(username: str):
    return await forward_request("GET", f"{USER_URL}/{username}")

@router.post("/follow/{username}")
async def follow(username: str, req: Request):
    body = await req.json()
    return await forward_request("POST", f"{USER_URL}/follow/{username}", data=body)

