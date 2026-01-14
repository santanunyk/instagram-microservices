from fastapi import APIRouter, UploadFile, File, Form, Request, HTTPException
from models.post import PostOut
from bson import ObjectId
from datetime import datetime
import os
import shutil

router = APIRouter()

# ---------------------------------------------------------
# Get post by ID
# ---------------------------------------------------------
@router.get("/{post_id}", response_model=PostOut)
async def get_post(post_id: str, request: Request):
    db = request.app.mongodb
    post = await db.posts.find_one({"_id": ObjectId(post_id)})

    if not post:
        raise HTTPException(404, "Post not found")

    media_url = f"/media/{post['media_filename']}"

    return PostOut(
        id=str(post["_id"]),
        username=post["username"],
        caption=post["caption"],
        media_url=media_url,
        created_at=post["created_at"]
    )

# ---------------------------------------------------------
# Get posts by username
# ---------------------------------------------------------
@router.get("/user/{username}")
async def get_user_posts(username: str, request: Request):
    db = request.app.mongodb
    cursor = db.posts.find({"username": username})
    posts = []

    async for post in cursor:
        posts.append({
            "id": str(post["_id"]),
            "username": post["username"],
            "caption": post["caption"],
            "media_url": f"/media/{post['media_filename']}",
            "created_at": post["created_at"]
        })

    return posts

# ---------------------------------------------------------
# Explore → Get ALL posts, newest first
# ---------------------------------------------------------
@router.get("/explore")
async def explore_posts(request: Request):
    db = request.app.mongodb

    cursor = db.posts.find({})
    posts = []

    async for post in cursor:
        posts.append({
            "id": str(post["_id"]),
            "username": post["username"],
            "caption": post.get("caption", ""),
            "media_url": f"/media/{post['media_filename']}",
            "created_at": post["created_at"]
        })

    # newest first
    posts.sort(key=lambda x: x["created_at"], reverse=True)

    return posts

