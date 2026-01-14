from fastapi import APIRouter, HTTPException, status, Depends, Request
from models.user import UserCreate, UserLogin, UserOut
from utils.jwt_handler import create_token
from passlib.context import CryptContext
from bson import ObjectId

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(raw: str, hashed: str):
    return pwd_context.verify(raw, hashed)

@router.post("/register", response_model=UserOut)
async def register(user: UserCreate, request: Request):
    db = request.app.mongodb
    existing = await db.users.find_one({"email": user.email})
    if existing:
        raise HTTPException(400, "Email already registered")

    hashed_pw = hash_password(user.password)

    new_user = {
        "email": user.email,
        "username": user.username,
        "password": hashed_pw
    }

    result = await db.users.insert_one(new_user)
    user_id = str(result.inserted_id)

    token = create_token(user_id, user.email)

    return UserOut(id=user_id, email=user.email, username=user.username, token=token)

@router.post("/login", response_model=UserOut)
async def login(user: UserLogin, request: Request):
    db = request.app.mongodb
    record = await db.users.find_one({"email": user.email})

    if not record:
        raise HTTPException(400, "Invalid credentials")

    if not verify_password(user.password, record["password"]):
        raise HTTPException(400, "Invalid credentials")

    token = create_token(str(record["_id"]), user.email)

    return UserOut(
        id=str(record["_id"]),
        email=record["email"],
        username=record["username"],
        token=token
    )

