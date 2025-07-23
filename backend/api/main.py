from fastapi import FastAPI
from backend.api.routes import chat, documents 

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to ZeeAgentX API. Visit http://127.0.0.1:8000/docs for Swagger UI."}

# Include routers
app.include_router(chat.router)
app.include_router(documents.router)
