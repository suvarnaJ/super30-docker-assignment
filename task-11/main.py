from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Task 11 Dockerfile is working"}