from fastapi import APIRouter
from utils.service_client import forward_request
import os

router = APIRouter()
NOTIFICATION_URL = os.getenv("NOTIFICATION_URL")

@router.get("/")
async def get_notifications():
    return await forward_request("GET", f"{NOTIFICATION_URL}/")

