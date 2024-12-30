from pydantic import BaseModel

class UserBase(BaseModel):
    user_name: str
    user_email: str
    user_phone: str

class UserCreate(UserBase):
    user_password: str

class UserRead(UserBase):
    user_id: int

    class Config:
        from_attributes = True

class RequestUser(BaseModel):
    user_email: str
    user_password: str