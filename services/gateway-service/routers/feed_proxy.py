from fastapi import APIRouter
from utils.service_client import forward_request
import os

router = APIRouter()
FEED_URL = os.getenv("FEED_URL")

@router.get("/")
async def get_feed():
    return await forward_request("GET", f"{FEED_URL}/")

