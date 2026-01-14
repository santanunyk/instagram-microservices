from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logic.feed_builder import get_user_feed
import motor.motor_asyncio
import os

app = FastAPI(
    title="Feed Service",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# MongoDB
MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017/instagramdb")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.instagramdb

@app.on_event("startup")
async def startup_db():
    app.mongodb = db

@app.get("/feed/{username}")
async def feed(username: str):
    return await get_user_feed(username, db)

@app.get("/health")
def health():
    return {"status": "feed-service ok"}

