from pydantic import BaseModel, Field, validator
from typing import Optional


class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"johndoe",
                "email":"johndoe@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }



class Settings(BaseModel):
    authjwt_secret_key:str='59171a93c39c4068f5cbbc6bffa6ec19b6487cd64b4651a6a10ab3a26202bf72'



class LoginModel(BaseModel):
    username: str
    password: str

