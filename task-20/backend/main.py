
import os
import time
import psycopg

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg.rows import dict_row

app = FastAPI(title="Super30 Three Tier Application")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)

@app.on_event("startup")
def startup():
    for attempt in range(20):
        try:
            with get_connection() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS students (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        email VARCHAR(150) UNIQUE NOT NULL
                    )
                """)
            return
        except Exception:
            if attempt == 19:
                raise
            time.sleep(3)

@app.get("/")
def home():
    return {"message": "Super30 Three Tier Application"}

@app.get("/students")
def get_students():
    with get_connection() as conn:
        return conn.execute(
            "SELECT * FROM students ORDER BY id"
        ).fetchall()

@app.post("/students")
def add_student(student: dict):
    with get_connection() as conn:
        return conn.execute(
            "INSERT INTO students (name, email) VALUES (%s, %s) RETURNING *",
            (student["name"], student["email"])
        ).fetchone()
