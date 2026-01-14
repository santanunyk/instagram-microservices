from bson import ObjectId

async def get_user_feed(username: str, db):
    # 1. Get the list of users that "username" follows
    user = await db.user_profiles.find_one({"username": username})

    if not user:
        return []

    following = user.get("following", [])

    if not following:
        return []  # no posts if follows no one

    # 2. Get posts from followed users
    cursor = db.posts.find({"username": {"$in": following}})

    feed = []
    async for post in cursor:
        feed.append({
            "id": str(post["_id"]),
            "username": post["username"],
            "caption": post["caption"],
            "media_url": f"/media/{post['media_filename']}",
            "created_at": post["created_at"]
        })

    # 3. Sort by newest first
    feed.sort(key=lambda x: x["created_at"], reverse=True)

    return feed

