
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Dependencies installed automatically",
        "framework": "FastAPI",
        "server": "Uvicorn"
    }
