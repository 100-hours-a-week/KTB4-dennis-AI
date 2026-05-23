# Community Board

FastAPI 벡엔드와 HTML/CSS/JavaScript 프론트엔드를 분리하여 만든 간단한 비회원 커뮤니티 게시판 입니다

사용자는 작성자 이름을 입력하여 게시글과 댓글을 작성할 수 있습니다.

## 주요 기능

- 게시글 목록 조회
- 게시글 상세 조회
- 게시글 작성
- 댓글 목록 조회
- 댓글 작성

## 기술 스택

- Backend: Python, FastAPI, SQLALchemy, SQLite
- Frontend: HTML, CSS, JavaScript
- Server : Uvicorn, Python http.server

## 프로젝트 구조

```text
app/
    main.py
    database.py
    models.py
    schemas.py
    crud.py
    routers/
        posts.py
        comments.py

frontend/
    index.html
    create.html
    detail.html
    css/
        style.css
    js/
        api.js
        index.js
        create.js
        detail.js
```

## 실행 방법

### 1. 가상환경 생성 및 활성화

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 백엔드 서버 실행

프로젝트 최상위 폴더에서 실행합니다.

```bash
uvicorn app.main:app -- reload --host 127.0.0.1 --port 8000
```

벡엔드 API 문서:

```text
http://127.0.0.1:8000/docs
```

### 4. 프론트엔드 서버 실행

새 터미널을 열고 프로젝트 최상위 폴더에서 실행합니다.

```bash
cd frontend
python -m http.server 5500 --bind 127.0.0.1
```

프론트엔드 화면:

```text
http://127.0.0.1:5500
```

## 테스트 방법

1. 백엔드 서버를 실행합니다.
2. 프론트엔드 서버를 실행합니다.
3. 브라우저에서 'http://127.0.0.1:5500' 에 접속합니다.
4. 글 작성 버튼을 눌러 게시글을 작성합니다.
5. 상세 페이지에서 댓글을 작성합니다.
6. 목록으로 돌아가 게시글이 표시되는지 확인합니다.

## 참고

- 백엔드는 8000번 포트에서 실행됩니다.
- 프론트엔드는 5500번 포트에서 실행됩니다.
- 프론트엔드와 백엔드가 다른 포트에서 실행되므로 FastAPI에 CORS 설정이 포함되어 있습니다.
- SQLite DB 파일은 로컬 실행 중 생성됩니다.
