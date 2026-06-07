from sqlalchemy.orm import Session

from app.models.enrollment import Enrollment


def get_enrollment(
    db: Session,
    user_id: int,
    course_id: int
):
    return (
        db.query(Enrollment)
        .filter(
            Enrollment.user_id == user_id,
            Enrollment.course_id == course_id
        )
        .first()
    )


def count_enrollments(
    db: Session,
    course_id: int
):
    return (
        db.query(Enrollment)
        .filter(
            Enrollment.course_id == course_id
        )
        .count()
    )


def create_enrollment(
    db: Session,
    user_id: int,
    course_id: int
):
    enrollment = Enrollment(
        user_id=user_id,
        course_id=course_id
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment


def delete_enrollment(
    db: Session,
    enrollment
):
    db.delete(enrollment)
    db.commit()