from fastapi import FastAPI, HTTPException  # FastAPI 앱 생성 도구, HTTP 에러 반환 도구
from pydantic import BaseModel  # 요청/응답 데이터 형식 정의 도구
from rag_chain import ask  # 우리가 만든 RAG 체인의 ask 함수 가져오기

# FastAPI 앱 생성
# title, description은 /docs Swagger UI에 표시됨
app = FastAPI(
    title="쇼핑몰 고객상담 챗봇 API",
    description="LangChain RAG + Gemini 기반 고객상담 API",
    version="1.0.0"
)

# 요청 데이터 형식 정의 (Pydantic 모델)
# POST /ask 로 들어오는 JSON 구조를 정의
class QuestionRequest(BaseModel):
    question: str  # 고객이 보내는 질문 문자열

# 응답 데이터 형식 정의 (Pydantic 모델)
# POST /ask 가 반환하는 JSON 구조를 정의
class AnswerResponse(BaseModel):
    question: str  # 받은 질문을 그대로 반환 (확인용)
    answer: str    # RAG 체인이 생성한 답변

# GET /health 엔드포인트
# 서버가 정상 작동 중인지 확인할 때 사용
# 배포 환경에서 서버 상태 모니터링에 활용
@app.get("/health")
def health_check():
    return {"status": "ok"}  # 정상이면 ok 반환

# POST /ask 엔드포인트
# 고객 질문을 받아 RAG 체인으로 답변 생성 후 반환
@app.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    # 질문이 공백만 있거나 비어있으면 400 에러 반환
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="질문을 입력해주세요.")

    # rag_chain.py의 ask 함수 호출해서 답변 생성
    answer = ask(request.question)

    # 질문과 답변을 묶어서 반환
    return AnswerResponse(
        question=request.question,
        answer=answer
    )