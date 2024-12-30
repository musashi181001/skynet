from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.user import UserCreate
from schemas.user import RequestUser
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
    try:
        return user_service.create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/login")
def login(request: RequestUser, db: Session = Depends(get_db)):
    user_service = UserService(db)
    try:
        return user_service.authenticate_user(request.user_email, request.user_password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    