from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.models import User, TokenTable
from schemas.user import UserCreate
from utils.jwt_utils import create_access_token,create_refresh_token,verify_password,get_hashed_password


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.user_email == email).first()

    def create_user(self, user: UserCreate):
        db_user = self.get_user_by_email(user.user_email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        encrypted_password =get_hashed_password(user.user_password)
        new_user = User(
            user_name=user.user_name,
            user_email=user.user_email,
            user_phone=user.user_phone,
            user_password=encrypted_password
        )
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
    def authenticate_user(self, email: str, password: str):
        user = self.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=400, detail="Invalid email")
        hashed_password = user.user_password
        if not verify_password(password, hashed_password):
            raise HTTPException(status_code=400, detail="Invalid password")
        
        access=create_access_token(user.user_id)
        refresh = create_refresh_token(user.user_id)

        token = TokenTable(
            token_id=user.user_id,  
            access_token=access,  
            refresh_token=refresh, 
            status=True
        )
        self.db.add(token)
        self.db.commit()
        self.db.refresh(token)
        return {
            "access_token": access,
            "refresh_token": refresh,
        }
