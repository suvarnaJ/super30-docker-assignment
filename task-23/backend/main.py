
import time

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    Query
)

from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from sqlalchemy import or_, text

from sqlalchemy.exc import IntegrityError

from database import Base, engine, get_db

from models import Student

from schemas import (
    StudentCreate,
    StudentUpdate,
    StudentResponse
)


app = FastAPI(
    title="Super30 Student Management System",
    description="Student Management API using FastAPI, PostgreSQL and Docker",
    version="1.0.0"
)


# CORS configuration

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8083"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Database startup

@app.on_event("startup")
def startup():

    for attempt in range(20):

        try:

            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))

            Base.metadata.create_all(bind=engine)

            print("PostgreSQL connected successfully")

            return

        except Exception as error:

            print(f"Database connection attempt {attempt + 1}: {error}")

            if attempt == 19:
                raise

            time.sleep(3)


# Home endpoint

@app.get("/")
def home():

    return {
        "application": "Student Management System",
        "status": "running",
        "technology": "FastAPI + PostgreSQL + Docker"
    }


# Health endpoint

@app.get("/health")
def health(db: Session = Depends(get_db)):

    try:

        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception:

        raise HTTPException(
            status_code=503,
            detail="Database unavailable"
        )


# CREATE student

@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=201
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = Student(
        **student.model_dump()
    )

    try:

        db.add(new_student)

        db.commit()

        db.refresh(new_student)

        return new_student

    except IntegrityError:

        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="Student email already exists"
        )


# READ and SEARCH students

@app.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students(
    search: str | None = Query(default=None),
    db: Session = Depends(get_db)
):

    query = db.query(Student)

    if search:

        query = query.filter(
            or_(
                Student.name.ilike(f"%{search}%"),
                Student.email.ilike(f"%{search}%"),
                Student.course.ilike(f"%{search}%")
            )
        )

    return query.order_by(Student.id).all()


# READ individual student

@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# UPDATE student

@app.put(
    "/students/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    updates = student_data.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():

        setattr(student, key, value)

    try:

        db.commit()

        db.refresh(student)

        return student

    except IntegrityError:

        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="Student email already exists"
        )


# DELETE student

@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)

    db.commit()

    return {
        "message": "Student deleted successfully",
        "student_id": student_id
    }
