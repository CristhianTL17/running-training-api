from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.utils.auth import hash_password

router = APIRouter()


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post("/register")
def create_user(name: str, email: str, password: str, db: Session = Depends(get_db)):
    new_user = User(name=name, email=email, password=hash_password(password))

    db.add(new_user)
    db.commit()

    return {"message": "User created"}


@router.put("/users/{id}")
def update_user(
    id: int, name: str, email: str, password: str, db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == id).first()

    user.name = name
    user.email = email
    user.password = password

    db.commit()

    return {"message": "User updated"}


## Eliminar Usuario
@router.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}
