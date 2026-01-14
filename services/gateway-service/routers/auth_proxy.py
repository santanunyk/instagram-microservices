from fastapi import APIRouter, Request
import requests

router = APIRouter()

AUTH_SERVICE = "http://auth:8001/auth"   # 🔥 Base path includes /auth


# ------------------------------
# LOGIN
# ------------------------------
@router.post("/login")
async def login_user(request: Request):
    data = await request.json()
    resp = requests.post(f"{AUTH_SERVICE}/login", json=data)
    return resp.json()


# ------------------------------
# REGISTER
# ------------------------------
@router.post("/register")
async def register_user(request: Request):
    data = await request.json()
    resp = requests.post(f"{AUTH_SERVICE}/register", json=data)
    return resp.json()


# ------------------------------
# HEALTH CHECK
# ------------------------------
@router.get("/health")
async def health():
    resp = requests.get(f"{AUTH_SERVICE}/health")
    return resp.json()

