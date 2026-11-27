
from fastapi import FastAPI

app = FastAPI(
    title="Super30 Docker API",
    description="My first FastAPI application inside Docker",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Super30 Docker Assignment",
        "status": "success"
    }

@app.get("/students")
def get_students():
    return {
        "students": [
            {"id": 1, "name": "Suvarna"},
            {"id": 2, "name": "Rahul"},
            {"id": 3, "name": "Priya"}
        ]
    }

@app.get("/about")
def about():
    return {
        "application": "Student Management API",
        "technology": "FastAPI + Docker"
    }
