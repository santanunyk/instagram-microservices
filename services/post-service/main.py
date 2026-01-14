from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers.posts import router as posts_router
import motor.motor_asyncio
import os

app = FastAPI(
    title="Post Service",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True
)

# MongoDB
MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb.insta.svc.cluster.local:27017/instagramdb")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.instagramdb

@app.on_event("startup")
async def startup_event():
    app.mongodb = db

# STATIC MEDIA FILES (images/videos)
MEDIA_PATH = os.getenv("MEDIA_PATH", "/app/storage/uploads")
app.mount("/media", StaticFiles(directory=MEDIA_PATH), name="media")

# Routers
app.include_router(posts_router, prefix="/posts", tags=["Posts"])

@app.get("/health")
def health():
    return {"status": "post-service ok"}

