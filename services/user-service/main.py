from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.users import router as users_router
import motor.motor_asyncio
import os

app = FastAPI(
    title="User Service",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# MongoDB connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017/instagramdb")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client.instagramdb

@app.on_event("startup")
async def startup_event():
    app.mongodb = db

# Routers
app.include_router(users_router, prefix="/users", tags=["Users"])

@app.get("/health")
def health():
    return {"status": "user-service ok"}

