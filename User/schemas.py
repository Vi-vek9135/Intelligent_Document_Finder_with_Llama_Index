from pydantic import BaseModel
import datetime




# User Creation Model
class UserCreate(BaseModel):
    username: str
    email: str
    password: str



# Request Details Model
class requestdetails(BaseModel):
    email:str
    password:str



# Token Schema Model   
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str


# Change Password Model
class changepassword(BaseModel):
    email:str
    old_password:str
    new_password:str



# Token Creation Model
class TokenCreate(BaseModel):
    user_id:str
    access_token:str
    refresh_token:str
    status:bool
    created_date:datetime.datetime
