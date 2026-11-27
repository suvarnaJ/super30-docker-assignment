
from fastapi import FastAPI

app = FastAPI(title="Super30 Health Check API")

@app.get("/")
def home():
    return {"message": "Application is running"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "Super30 FastAPI",
        "version": "1.0"
    }
