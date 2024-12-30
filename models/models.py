from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    user_email = Column(String, unique=True, index=True)
    user_phone = Column(String, unique=True, index=True)
    user_password = Column(String)