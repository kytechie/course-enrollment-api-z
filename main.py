from fastapi import FastAPI

from app.database.database import (
    Base,
    engine
)

from app.models.user import User
from app.models.course import Course
from app.models.enrollment import Enrollment

from app.routers.auth import router as auth_router
from app.routers.users import router as user_router
from app.routers.courses import router as course_router
from app.routers.enrollment import router as enrollment_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Course Enrollment API"
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(course_router)
app.include_router(enrollment_router)


@app.get("/")
def home():
    return {
        "message": "Course Enrollment API"
    }