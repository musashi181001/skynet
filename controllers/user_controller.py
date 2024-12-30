from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.user import UserCreate

from database.database import SessionLocal
from services.user_service import UserService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get_user_by_email(user.user_email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    try:
        return user_service.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))