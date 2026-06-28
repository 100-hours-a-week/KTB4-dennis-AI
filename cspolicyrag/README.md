# 🛍️ 쇼핑몰 고객상담 챗봇 API

LangChain RAG 파이프라인을 FastAPI로 래핑한 쇼핑몰 고객상담 REST API입니다.  
배송, 환불/교환, 회원/포인트 관련 FAQ 문서를 기반으로 Gemini LLM이 답변을 생성합니다.

---

## 🗂️ 프로젝트 구조

```
cs_policy_chat/
├── data/
│   ├── shipping.txt       # 배송 관련 FAQ
│   ├── refund.txt         # 환불/교환 관련 FAQ
│   └── membership.txt     # 회원/포인트 관련 FAQ
├── ingest.py              # 문서 → ChromaDB 임베딩 저장 (최초 1회 실행)
├── rag_chain.py           # LangChain RAG 파이프라인
├── main.py                # FastAPI 서버
├── requirements.txt
└── chroma_db/             # 벡터DB 저장 폴더 (자동 생성)
```

---

## ⚙️ 기술 스택

- **LLM**: Google Gemini 2.5 Flash Lite
- **Embedding**: Google Gemini Embedding 001
- **Vector DB**: ChromaDB
- **RAG Framework**: LangChain
- **API Server**: FastAPI

---

## 🚀 실행 방법

### 1. 가상환경 생성 및 활성화

```bash
python -m venv .venv
source .venv/bin/activate  
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 환경변수 설정

`.env` 파일을 루트에 생성 후 Gemini API 키를 입력합니다.

```
GEMINI_API_KEY=여기에_API_키_입력
```

### 4. 문서 임베딩 (최초 1회만 실행)

```bash
python ingest.py
```

### 5. API 서버 실행

```bash
uvicorn main:app --reload
```

### 6. API 테스트

브라우저에서 Swagger UI 접속

```
http://localhost:8000/docs
```

---

## 📡 API 엔드포인트

| Method | URL | 설명 |
|--------|-----|------|
| GET | `/health` | 서버 상태 확인 |
| POST | `/ask` | 고객 질문 답변 |

### 요청 예시

```json
{
  "question": "배송은 얼마나 걸리나요?"
}
```

### 응답 예시

```json
{
  "question": "배송은 얼마나 걸리나요?",
  "answer": "일반 배송은 2~3일, 빠른 배송은 당일 또는 익일 도착합니다."
}
```

---

# 📝 프로젝트 회고

이번 프로젝트는 코드의 완성도보다 RAG와 LangChain의 핵심 개념을 이해하는 것에 초점을 맞췄습니다. 단순히 코드를 작성하는 것에 그치지 않고, 각 컴포넌트가 왜 필요한지, 어떤 역할을 하는지 이해하며 진행했습니다.

가장 크게 경험한 것은 RAG 파이프라인의 전체 사이클입니다. 미리 준비한 FAQ 문서를 청킹하고 임베딩하여 벡터DB에 저장한 뒤, 질문이 들어왔을 때 유사도 검색으로 관련 내용을 추출하고 LLM이 답변을 생성하는 흐름을 직접 구현하고 체감할 수 있었습니다.

```
문서 준비 (FAQ txt)
    ↓
텍스트 청킹
    ↓
임베딩 변환 → 벡터DB 저장 (ChromaDB)
    ↓
질문 입력
    ↓
유사도 검색 → 관련 청크 추출
    ↓
프롬프트 조합 (컨텍스트 + 질문)
    ↓
LLM 답변 생성 (Gemini)
```

아쉬운 점은 LangChain이 빠르게 업데이트되면서 deprecated된 방식과 최신 방식을 구분하는 데 시간이 걸렸고, FAQ 문서가 적어 청크 수가 6개에 그쳤다는 점입니다. 또한 Langsmith 로 chain 실행을 trace 하고 dataset기반으로 평가하는 것은 진행하지 못했습니다. 추후 코드 구조 개선과 기능 확장을 위한 리팩토링을 진행할 예정입니다.