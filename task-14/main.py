import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "application": os.getenv("APP_NAME"),
        "environment": os.getenv("APP_ENV"),
        "version": os.getenv("APP_VERSION")
    }