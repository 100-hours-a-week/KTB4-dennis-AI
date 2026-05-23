from datetime import datetime 
from pydantic import BaseModel, Field, ConfigDict

class PostCreate(BaseModel):
    author_name: str = Field(...,min_length=1, max_length=50)
    title: str = Field(...,min_length=1,max_length=200)
    content:str = Field(...,min_length=1)


class PostResponse(BaseModel):
    id:int
    author_name:str
    title:str
    content:str
    created_at:datetime

    model_config = ConfigDict(from_attributes=True)

class CommentCreate(BaseModel):
    author_name: str = Field(...,min_length=1,max_length=50)
    content: str = Field(...,min_length=1)

class CommentResponse(BaseModel):
    id:int
    post_id:int
    author_name: str
    content: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


