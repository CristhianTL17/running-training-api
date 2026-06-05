from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.session import Session as TrainingSession

from app.schemas.session import SessionCreate, SessionUpdate

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
    session_data: SessionUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user),
):
    session = db.query(TrainingSession).filter(TrainingSession.id == id).first()

    if not session:
        raise HTTPException(
            status_code=404,
            detail="Session not found",
        )

    session.title = session_data.title
    session.type = session_data.type
    session.zone = session_data.zone
    session.distance = session_data.distance
    session.duration = session_data.duration
    session.pace = session_data.pace
    session.heart_rate = session_data.heart_rate
    session.details = session_data.details

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
