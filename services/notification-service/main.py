from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.notify import router as notify_router
import motor.motor_asyncio
import os

app = FastAPI(
    title="Notification Service",
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

app.include_router(notify_router, prefix="/notifications", tags=["Notifications"])

@app.get("/health")
def health():
    return {"status": "notification-service ok"}

