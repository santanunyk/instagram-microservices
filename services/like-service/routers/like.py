from fastapi import APIRouter, Request, HTTPException
from bson import ObjectId
from models.like import LikeCreate

router = APIRouter()

# -------------------------------------------
# Like a post
# -------------------------------------------
@router.post("/{post_id}")
async def like_post(post_id: str, request: Request, like: LikeCreate):
    db = request.app.mongodb

    # Check if already liked
    existing = await db.likes.find_one({
        "post_id": post_id,
        "username": like.username
    })

    if existing:
        return {"message": "Already liked"}

    new_like = {
        "post_id": post_id,
        "username": like.username
    }

    await db.likes.insert_one(new_like)

    return {"message": f"{like.username} liked post {post_id}"}

# -------------------------------------------
# Unlike a post
# -------------------------------------------
@router.delete("/{post_id}")
async def unlike_post(post_id: str, request: Request, username: str):
    db = request.app.mongodb

    result = await db.likes.delete_one({
        "post_id": post_id,
        "username": username
    })

    if result.deleted_count == 0:
        raise HTTPException(404, "Like not found")

    return {"message": f"{username} unliked post {post_id}"}

# -------------------------------------------
# Count likes for a post
# -------------------------------------------
@router.get("/{post_id}/count")
async def like_count(post_id: str, request: Request):
    db = request.app.mongodb

    count = await db.likes.count_documents({"post_id": post_id})

    return {"post_id": post_id, "likes": count}

# -------------------------------------------
# Check if user liked a post
# -------------------------------------------
@router.get("/{post_id}/user/{username}")
async def user_liked(post_id: str, username: str, request: Request):
    db = request.app.mongodb

    like = await db.likes.find_one({
        "post_id": post_id,
        "username": username
    })

    return {"liked": like is not None}

