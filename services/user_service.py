from sqlalchemy.orm import Session
from models.models import User
from schemas.user import UserCreate

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.user_email == email).first()

    def create_user(self, user: UserCreate):
        new_user = User(
            user_name=user.user_name,
            user_email=user.user_email,
            user_phone=user.user_phone,
            user_password=user.user_password
        )
        # encrypted_password =get_hashed_password(user.user_password)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
