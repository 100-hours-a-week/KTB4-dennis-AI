from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud,schemas
from .. database import get_db



router = APIRouter(
    prefix="/posts/{post_id}/comments",
    tags=["comments"]
)

@router.get("",response_model=List[schemas.CommentResponse])
def read_comments(post_id: int, db:Session=Depends(get_db)):
    post = crud.get_post(db, post_id)

    if post is None:
        raise HTTPException(status_code=404, detail="게시글 찾을 수 없음")
    
    return crud.get_comments_by_post(db,post_id)

@router.post("",response_model=schemas.CommentResponse,status_code=201)
def create_comment(
    post_id: int,
    comment_data: schemas.CommentCreate,
    db:Session=Depends(get_db)
):
    post = crud.get_post(db,post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="게시글 찾을 수 없음")
    
    return crud.create_comment(db,post_id,comment_data)
    