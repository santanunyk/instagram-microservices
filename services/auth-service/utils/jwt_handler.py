import jwt
from datetime import datetime, timedelta
import os

SECRET = os.getenv("JWT_SECRET", "supersecretkey")

def create_token(user_id: str, email: str):
    payload = {
        "user_id": user_id,
        "email": email,
        "exp": datetime.utcnow() + timedelta(days=2),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

