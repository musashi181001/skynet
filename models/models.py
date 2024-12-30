from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database.database import Base
import datetime

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    user_email = Column(String, unique=True, index=True)
    user_phone = Column(String, unique=True, index=True)
    user_password = Column(String)

class TokenTable(Base):
    __tablename__ = "token"
    token_id = Column(Integer)
    access_token = Column(String(450), primary_key=True)
    refresh_token = Column(String(450),nullable=False)
    status = Column(Boolean)
    created_date = Column(DateTime, default=datetime.datetime.now)