from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.session import Session as TrainingSession

from app.schemas.session import SessionCreate

from app.routes.auth import get_current_user

router = APIRouter()


@router.post("/sessions")
def create_session(
    session: SessionCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    new_session = TrainingSession(
        date=session.date,
        title=session.title,
        type=session.type,
        zone=session.zone,
        distance=session.distance,
        duration=session.duration,
        pace=session.pace,
        heart_rate=session.heart_rate,
        details=session.details,
        strava_link=session.strava_link,
        resource_link=session.resource_link,
        plan_id=session.plan_id,
    )

    db.add(new_session)

    db.commit()

    return {"message": "Session created"}


@router.get("/sessions")
def get_sessions(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    sessions = db.query(TrainingSession).all()

    return sessions


@router.put("/sessions/{id}")
def update_session(
    id: int,
    title: str,
    type: str,
    zone: str,
    distance: float,
    duration: str,
    pace: str,
    heart_rate: str,
    details: str,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    session = db.query(TrainingSession).filter(TrainingSession.id == id).first()

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Session not found",
        )

    session.title = title
    session.type = type
    session.zone = zone
    session.distance = distance
    session.duration = duration
    session.pace = pace
    session.heart_rate = heart_rate
    session.details = details

    db.commit()

    return {"message": "Session updated"}


@router.delete("/sessions/{id}")
def delete_session(
    id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    session = db.query(TrainingSession).filter(TrainingSession.id == id).first()

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Session not found",
        )

    db.delete(session)

    db.commit()

    return {"message": "Session deleted"}


@router.get("/plans/{id}/sessions")
def get_plan_sessions(
    id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    sessions = db.query(TrainingSession).filter(TrainingSession.plan_id == id).all()

    return sessions
