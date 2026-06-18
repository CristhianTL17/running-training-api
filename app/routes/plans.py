from fastapi import APIRouter, Depends, HTTPException
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


@router.put("/plans/{id}")
def update_plan(
    id: int,
    plan: PlanCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    existing_plan = db.query(Plan).filter(Plan.id == id).first()

    if not existing_plan:
        raise HTTPException(
            status_code=404,
            detail="Plan not found",
        )

    existing_plan.title = plan.title
    existing_plan.athlete_id = plan.athlete_id

    db.commit()

    return {"message": "Plan updated"}


@router.delete("/plans/{id}")
def delete_plan(
    id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    plan = db.query(Plan).filter(Plan.id == id).first()

    if not plan:
        raise HTTPException(
            status_code=404,
            detail="Plan not found",
        )

    db.delete(plan)

    db.commit()

    return {"message": "Plan deleted"}
