from fastapi import FastAPI
from .database import Base, engine
from .routers import posts,comments

from fastapi.middleware.cors import CORSMiddleware
from . import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Community Board API",
    description="비회원 커뮤니티 게시판 API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message":"Community Board API is running"}

app.include_router(posts.router)
app.include_router(comments.router)








# from fastapi import FastAPI

# app = FastAPI()

# posts = [
#     {
#         "id":1,
#         "author_name":"tom",
#         "title":"첫번째 게시글",
#         "content":"FastAPI로 커뮤니티 게시판 만들기"
#     },
#     {
#         "id":2,
#         "author_name":"jane",
#         "title":"두번째 게시글",
#         "content":"게시글 목록 조회 테스트"
#     }
# ]

# @app.get("/")
# def root():
#     return {"message": "Hello FastAPI"}

# @app.get("/posts")
# def get_posts():
#     return posts