from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud,schemas
from .. database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)

@router.get("",response_model=List[schemas.PostResponse])
def read_posts(db:Session=Depends(get_db)):
    return crud.get_posts(db)

@router.get("/{post_id}",response_model=schemas.PostResponse)
def read_post(post_id: int, db:Session=Depends(get_db)):
    post = crud.get_post(db,post_id)

    if post is None:
        raise HTTPException(status_code=404, detail="게시글 찾을 수 없음")
    
    return post

@router.post("",response_model=schemas.PostResponse,status_code=201)
def create_post(post_data: schemas.PostCreate, db: Session= Depends(get_db)):
    return crud.create_post(db,post_data)