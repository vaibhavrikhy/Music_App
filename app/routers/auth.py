from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import jwt
from app.models.user import User
from app.core.config import settings

router = APIRouter()
SECRET_KEY = settings.JWT_SECRET
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: int):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/signup")
async def signup(email: str, password: str):
    if len(password.encode("utf-8")) > 72:
        raise HTTPException(
            status_code=400,
            detail="Password must be 72 characters or fewer"
        )

    existing = await User.find_one(User.email == email)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        email=email,
        hashed_password=User.hash_password(password),
    )
    await user.insert()

    token = create_access_token({"sub": email}, settings.JWT_EXPIRES_MIN)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/signup")
async def signup(email: str, password: str):
    existing = await User.find_one(User.email == email)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(email=email, hashed_password=User.hash_password(password))
    await user.insert()
    token = create_access_token({"sub": email},  settings.JWT_EXPIRES_MIN)
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.find_one(User.email == form_data.username)
    if not user or not user.verify_password(form_data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email}, settings.JWT_EXPIRES_MIN)
    return {"access_token": token, "token_type": "bearer"}
