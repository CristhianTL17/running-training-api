from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.plan import Plan

from app.routes.auth import get_current_user

from app.schemas.plan import PlanCreate

router = APIRouter()


@router.post("/plans")
def create_plan(
    plan: PlanCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    new_plan = Plan(
        title=plan.title,
        athlete_id=plan.athlete_id,
    )

    db.add(new_plan)

    db.commit()

    return {"message": "Plan created"}


@router.get("/plans")
def get_plans(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    plans = db.query(Plan).all()

    return plans
