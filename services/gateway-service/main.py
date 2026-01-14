from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import (
    auth_proxy,
    user_proxy,
    post_proxy,
    comment_proxy,
    like_proxy,
    feed_proxy,
    notification_proxy
)

app = FastAPI(
    title="Instagram API Gateway",
    version="1.0.0",
    description="Routes all traffic to microservices."
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_proxy.router, prefix="/auth", tags=["Auth"])
app.include_router(user_proxy.router, prefix="/users", tags=["Users"])
app.include_router(post_proxy.router, prefix="/posts", tags=["Posts"])
app.include_router(comment_proxy.router, prefix="/comments", tags=["Comments"])
app.include_router(like_proxy.router, prefix="/likes", tags=["Likes"])
app.include_router(feed_proxy.router, prefix="/feed", tags=["Feed"])
app.include_router(notification_proxy.router, prefix="/notifications", tags=["Notifications"])

@app.get("/health")
def health():
    return {"status": "ok", "gateway": "running"}

