from pydantic import BaseModel
from datetime import datetime




class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str

    class Config:
        orm_mode = True




class CommentBase(BaseModel):
    text : str
    timestamp : datetime
    user_id : int
    post_id : int

class CommentDisplay(BaseModel):
    id: int
    user: User
    post_id: int
    timestamp: datetime
    text: str
    
    class Config:
        orm_mode = True



class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int




class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: list[CommentDisplay]

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    id : int
    username : str
    email : str


    class Config:
        orm_mode = True
