from sqlalchemy.orm import Session

from app.models.course import Course


def get_all_courses(db: Session):
    return db.query(Course).all()


def get_course_by_id(
    db: Session,
    course_id: int
):
    return (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )


def get_course_by_code(
    db: Session,
    code: str
):
    return (
        db.query(Course)
        .filter(Course.code == code)
        .first()
    )


def create_course(
    db: Session,
    course_data
):
    course = Course(
        title=course_data.title,
        code=course_data.code,
        capacity=course_data.capacity
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return course


def get_course(
    db: Session,
    course_id: int
):
    return (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )