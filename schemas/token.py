from pydantic import BaseModel
import datetime

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class TokenCreate(TokenSchema):
    token_id:str
    status:bool
    created_date:datetime.datetime