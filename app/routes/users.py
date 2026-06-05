from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.utils.auth import hash_password

from app.routes.auth import get_current_user

from app.schemas.user import UserCreate, UserUpdate

router = APIRouter()


@router.get("/users")
def get_users(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    users = db.query(User).all()

    return users


@router.post("/register")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
    )

    db.add(new_user)
    db.commit()

    return {"message": "User created"}


@router.put("/users/{id}")
def update_user(
    id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    user = db.query(User).filter(User.id == id).first()

    # Manejo de errores
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    user.name = user_data.name
    user.email = user_data.email
    user.password = hash_password(user_data.password)

    db.commit()

    return {"message": "User updated"}


## Eliminar Usuario
@router.delete("/users/{id}")
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}
