from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.comment import router as comment_router
import motor.motor_asyncio
import os

app = FastAPI(
    title="Comment Service",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True
)

# MongoDB
MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017/instagramdb")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.instagramdb

@app.on_event("startup")
async def startup_db():
    app.mongodb = db

# Routers
app.include_router(comment_router, prefix="/comments", tags=["Comments"])

@app.get("/health")
def health():
    return {"status": "comment-service ok"}

