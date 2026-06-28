from dotenv import load_dotenv  # .env 파일에서 환경변수 로드
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI  # Gemini 임베딩 모델, Gemini LLM
from langchain_chroma import Chroma  # 저장된 ChromaDB 불러오기
from langchain_core.prompts import PromptTemplate  # 프롬프트 템플릿 정의
from langchain_core.runnables import RunnablePassthrough  # 입력값을 그대로 다음 단계로 전달
from langchain_core.output_parsers import StrOutputParser  # LLM 출력을 문자열로 변환

load_dotenv()  # .env 파일에서 GEMINI_API_KEY 읽기

CHROMA_DIR = "chroma_db"  # ingest.py에서 저장한 벡터DB 경로

def get_rag_chain():
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    # ingest.py와 동일한 임베딩 모델 사용 (다르면 검색 불가)

    db = Chroma(
        persist_directory=CHROMA_DIR,   # 저장된 ChromaDB 폴더 경로
        embedding_function=embeddings   # 검색 시 사용할 임베딩 모델
    )

    retriever = db.as_retriever(search_kwargs={"k": 3})
    # 질문과 가장 유사한 청크 3개를 검색하는 retriever 생성

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",  # 무료 Gemini 모델
        temperature=0              # 0: 일관된 답변, 1에 가까울수록 창의적
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],  # 템플릿에서 사용할 변수
        template="""
당신은 쇼핑몰 고객상담 챗봇입니다.
아래 참고 문서를 바탕으로 고객 질문에 친절하게 답변해주세요.
문서에 없는 내용은 "해당 내용은 고객센터로 문의 부탁드립니다."라고 답하세요.

참고 문서:
{context}

고객 질문: {question}

답변:"""
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    # 검색된 여러 청크들을 하나의 텍스트로 합치는 함수

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        # retriever로 유사 청크 검색 → format_docs로 텍스트 합치기 → question은 그대로 전달
        | prompt   # context와 question을 프롬프트 템플릿에 삽입
        | llm      # 완성된 프롬프트를 Gemini LLM에 전달해서 답변 생성
        | StrOutputParser()  # LLM 출력을 순수 문자열로 변환
    )

    return chain


def ask(question: str) -> str:
    chain = get_rag_chain()  # RAG 체인 생성
    result = chain.invoke(question)  # 질문을 체인에 전달해서 답변 생성
    return result  # 생성된 답변 문자열 반환