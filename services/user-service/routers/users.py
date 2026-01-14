from fastapi import APIRouter, HTTPException, Request
from models.user_profile import UserProfile
from bson import ObjectId

router = APIRouter()

# ----------------------------
# Get Profile
# ----------------------------
@router.get("/{username}")
async def get_profile(username: str, request: Request):
    db = request.app.mongodb
    user = await db.user_profiles.find_one({"username": username})

    if not user:
        raise HTTPException(404, "User not found")

    user["id"] = str(user["_id"])
    del user["_id"]
    return user

# ----------------------------
# Create Profile
# Called after registration
# ----------------------------
@router.post("/create/{username}")
async def create_profile(username: str, request: Request):
    db = request.app.mongodb

    profile = {
        "username": username,
        "bio": "",
        "avatar": None,
        "followers": [],
        "following": []
    }

    exists = await db.user_profiles.find_one({"username": username})
    if exists:
        return {"message": "Profile already exists"}

    await db.user_profiles.insert_one(profile)
    return {"message": "Profile created"}

# ----------------------------
# Follow a user
# ----------------------------
@router.post("/follow/{username}")
async def follow_user(username: str, request: Request):
    body = await request.json()
    follower = body.get("follower")

    db = request.app.mongodb

    if follower == username:
        raise HTTPException(400, "You cannot follow yourself")

    user = await db.user_profiles.find_one({"username": username})
    me = await db.user_profiles.find_one({"username": follower})

    if not user or not me:
        raise HTTPException(404, "User not found")

    # Add follower
    await db.user_profiles.update_one(
        {"username": username},
        {"$addToSet": {"followers": follower}}
    )

    # Add my following
    await db.user_profiles.update_one(
        {"username": follower},
        {"$addToSet": {"following": username}}
    )

    return {"message": f"{follower} now follows {username}"}

