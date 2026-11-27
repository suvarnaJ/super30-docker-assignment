
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Docker Environment Variable Demo",
        "application": os.getenv("APP_NAME", "Default Application"),
        "environment": os.getenv("APP_ENV", "development")
    }
