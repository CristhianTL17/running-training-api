from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.plan import Plan

router = APIRouter()


@router.post("/plans")
def create_plan(title: str, athlete_id: int, db: Session = Depends(get_db)):
    new_plan = Plan(title=title, athlete_id=athlete_id)

    db.add(new_plan)

    db.commit()

    return {"message": "Plan created"}


@router.get("/plans")
def get_plans(db: Session = Depends(get_db)):
    plans = db.query(Plan).all()

    return plans
