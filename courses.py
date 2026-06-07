from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import (
    get_db
)

from app.schemas.course import (
    CourseCreate,
    CourseResponse
)

from app.services.course_service import (
    fetch_courses,
    fetch_course,
    add_course
)

router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.get(
    "/",
    response_model=list[CourseResponse]
)
def get_courses(
    db: Session = Depends(get_db)
):
    return fetch_courses(db)


@router.get(
    "/{course_id}",
    response_model=CourseResponse
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = fetch_course(
        db,
        course_id
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@router.post(
    "/",
    response_model=CourseResponse
)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    try:
        return add_course(
            db,
            course
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )