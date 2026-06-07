from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.database.database import (
    get_db
)

from app.schemas.enrollment import (
    EnrollmentCreate,
    EnrollmentResponse
)

from app.services.enrollment_service import (
    enroll_student,
    unenroll_student
)

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"]
)


@router.post(
    "/",
    response_model=EnrollmentResponse
)
def enroll(
    data: EnrollmentCreate,
    db: Session = Depends(get_db)
):
    try:
        return enroll_student(
            db,
            data.user_id,
            data.course_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.delete(
    "/{course_id}"
)
def unenroll(
    course_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    try:
        return unenroll_student(
            db,
            user_id,
            course_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )