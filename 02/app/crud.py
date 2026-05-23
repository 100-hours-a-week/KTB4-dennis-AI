from sqlalchemy.orm import Session
from . import models,schemas

def get_posts(db: Session):
    return db.query(models.Post).order_by(models.Post.id.desc()).all()

def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

def create_post(db: Session,post_data: schemas.PostCreate):
    new_post = models.Post(
        author_name=post_data.author_name,
        title=post_data.title,
        content= post_data.content
    )

    db.add(new_post)

    db.commit()

    db.refresh(new_post)

    return new_post


def get_comments_by_post(db: Session, post_id: int):
    return(
        db.query(models.Comment)
        .filter(models.Comment.post_id == post_id)
        .order_by(models.Comment.id.asc())
        .all()
    )

def create_comment(db: Session, post_id: int, comment_data: schemas.CommentCreate):
    new_comment = models.Comment(
        post_id=post_id,
        author_name=comment_data.author_name,
        content=comment_data.content
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment