# FastAPI - REST API Key
from fastapi import FastAPI
from pydantic import BaseModel
 
try:
    from app.rag_pipeline import create_rag_pipeline
except ModuleNotFoundError:
    from rag_pipeline import create_rag_pipeline
 
app = FastAPI()
 
qa_chain = None
 
class Query(BaseModel):
    query: str
 
@app.get("/")
def home():
    return {"message": "RAG API Running"}
 
@app.post("/ask")
def ask(q : Query):
    global qa_chain
    if qa_chain is None:
        qa_chain = create_rag_pipeline()
    result = qa_chain.invoke({"question": q.query})
    response = result['answer']
 
    sources = result.get('source_documents', [])
    return {"response": response, "sources": sources}
 
 