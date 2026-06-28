import os  # 파일 경로 조합에 사용
from dotenv import load_dotenv  # .env 파일에서 환경변수 로드
from langchain_community.document_loaders import TextLoader  # txt 파일을 LangChain Document 객체로 로드
from langchain_text_splitters import RecursiveCharacterTextSplitter  # 텍스트를 작은 청크 단위로 분할
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Gemini 임베딩 모델 (텍스트 → 벡터 변환)
from langchain_chroma import Chroma  # ChromaDB 연동 (벡터 저장 및 검색)

load_dotenv()  # .env 파일에서 GEMINI_API_KEY 읽기

CHROMA_DIR = "chroma_db"  # 벡터DB가 저장될 폴더 이름
DATA_DIR = "data"          # FAQ txt 파일들이 있는 폴더 이름

def ingest():
    files = ["shipping.txt", "refund.txt", "membership.txt"]  # 임베딩할 FAQ 파일 목록
    documents = []  # 로드된 문서들을 담을 리스트

    for file in files:
        path = os.path.join(DATA_DIR, file)  # data/shipping.txt 형태로 경로 조합

        loader = TextLoader(path, encoding="utf-8")  # txt 파일을 Document 객체로 로드
        docs = loader.load()  # 실제 파일 읽기

        for doc in docs:
            doc.metadata["source"] = file  # 각 문서에 출처 파일명 태그 추가 (나중에 Agent 확장 시 카테고리 필터링에 활용)

        documents.extend(docs)  # 전체 문서 리스트에 추가
        print(f"{file} 로딩 완료!")  # 파일 로딩 진행상황 출력

    splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    # chunk_size=300: 300자 단위로 텍스트 분할
    # chunk_overlap=50: 앞뒤 청크가 50자씩 겹치게 해서 문맥 유지

    chunks = splitter.split_documents(documents)  # 문서들을 청크로 분할
    print(f"총 {len(chunks)}개 청크로 분할 완료!")  # 청크 분할 진행상황 출력

    print("Gemini 임베딩 중... 잠시 기다려주세요!")  # 임베딩 시작 알림
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    # Gemini 임베딩 모델로 텍스트를 벡터(숫자 배열)로 변환
    # 벡터로 변환해야 유사도 기반 검색이 가능함

    print("ChromaDB에 저장 중...")  # 저장 시작 알림
    db = Chroma.from_documents(
        documents=chunks,       # 분할된 청크들
        embedding=embeddings,   # 임베딩 모델
        persist_directory=CHROMA_DIR  # chroma_db/ 폴더에 영구 저장
    )

    print(f"완료! 총 {len(chunks)}개 청크가 저장되었습니다.")

if __name__ == "__main__":
    ingest()  # 이 파일을 직접 실행할 때만 ingest() 호출 (다른 파일에서 import 시 실행 안됨)