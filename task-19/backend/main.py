
import os
import time
import psycopg

from fastapi import FastAPI
from psycopg.rows import dict_row

app = FastAPI(title="Super30 FastAPI PostgreSQL")

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
            print("PostgreSQL connected successfully")
            return
        except Exception:
            if attempt == 19:
                raise
            time.sleep(3)

@app.get("/")
def home():
    return {"message": "FastAPI and PostgreSQL are connected"}

@app.get("/db-test")
def db_test():
    with get_connection() as conn:
        result = conn.execute(
            "SELECT current_database() AS database"
        ).fetchone()
    return {"database": result["database"], "status": "connected"}

@app.get("/students")
def get_students():
    with get_connection() as conn:
        students = conn.execute(
            "SELECT * FROM students ORDER BY id"
        ).fetchall()
    return students
