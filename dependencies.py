from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from sqlalchemy.orm import Session

from app.core.security import (
    SECRET_KEY,
    ALGORITHM
)

from app.database.database import get_db

from app.repositories.user_repository import (
    get_user_by_id
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = int(payload.get("sub"))

        user = get_user_by_id(
            db,
            user_id
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


def get_admin_user(
    current_user=Depends(
        get_current_user
    )
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admins only"
        )

    return current_user


def get_student_user(
    current_user=Depends(
        get_current_user
    )
):
    if current_user.role != "student":
        raise HTTPException(
            status_code=403,
            detail="Students only"
        )

    return current_user