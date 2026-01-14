from fastapi import FastAPI
from routers.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
import motor.motor_asyncio
import os

app = FastAPI(
    title="Auth Service",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB
MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017/instagramdb")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.instagramdb

@app.on_event("startup")
async def init_db():
    app.mongodb = db

# Routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])

@app.get("/health")
def health():
    return {"status": "auth-service ok"}

