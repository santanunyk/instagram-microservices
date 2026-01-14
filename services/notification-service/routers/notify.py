from fastapi import APIRouter, Request
from datetime import datetime
from bson import ObjectId

router = APIRouter()

# ------------------------------
# Create a notification
# ------------------------------
@router.post("/")
async def create_notification(request: Request):
    data = await request.json()
    db = request.app.mongodb

    notification = {
        "to_user": data["to_user"],      # who receives notification
        "from_user": data["from_user"],  # who triggered it
        "type": data["type"],            # 'like', 'comment', 'follow'
        "post_id": data.get("post_id"),  # optional
        "created_at": datetime.utcnow()
    }

    await db.notifications.insert_one(notification)
    return {"message": "notification created"}

# ------------------------------
# Get user's notifications
# ------------------------------
@router.get("/{username}")
async def get_notifications(username: str, request: Request):
    db = request.app.mongodb

    cursor = db.notifications.find({"to_user": username})
    notifications = []

    async for n in cursor:
        notifications.append({
            "id": str(n["_id"]),
            "type": n["type"],
            "from_user": n["from_user"],
            "post_id": n.get("post_id"),
            "created_at": n["created_at"]
        })

    notifications.sort(key=lambda x: x["created_at"], reverse=True)
    return notifications

