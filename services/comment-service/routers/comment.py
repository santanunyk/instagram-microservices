from fastapi import APIRouter, Request, HTTPException
from bson import ObjectId
from models.comment import CommentCreate, CommentOut
from datetime import datetime

router = APIRouter()

# ---------------------------------------------
# Create a comment on a post
# ---------------------------------------------
@router.post("/{post_id}", response_model=CommentOut)
async def add_comment(post_id: str, request: Request, comment: CommentCreate):
    db = request.app.mongodb

    new_comment = {
        "post_id": post_id,
        "username": comment.username,
        "text": comment.text,
        "created_at": datetime.utcnow()
    }

    result = await db.comments.insert_one(new_comment)
    comment_id = str(result.inserted_id)

    return CommentOut(
        id=comment_id,
        post_id=post_id,
        username=comment.username,
        text=comment.text,
        created_at=new_comment["created_at"]
    )

# ---------------------------------------------
# Get comments for a post
# ---------------------------------------------
@router.get("/{post_id}")
async def get_comments(post_id: str, request: Request):
    db = request.app.mongodb

    cursor = db.comments.find({"post_id": post_id})
    comments = []

    async for c in cursor:
        comments.append({
            "id": str(c["_id"]),
            "post_id": c["post_id"],
            "username": c["username"],
            "text": c["text"],
            "created_at": c["created_at"]
        })

    return comments

