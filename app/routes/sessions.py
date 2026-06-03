from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.session import Session as TrainingSession

from app.schemas.session import SessionCreate

router = APIRouter()


@router.post("/sessions")
def create_session(session: SessionCreate, db: Session = Depends(get_db)):
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
def get_sessions(db: Session = Depends(get_db)):
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
):
    session = db.query(TrainingSession).filter(TrainingSession.id == id).first()

    if not session:
        return {"error": "Session not found"}

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
def delete_session(id: int, db: Session = Depends(get_db)):
    session = db.query(TrainingSession).filter(TrainingSession.id == id).first()

    db.delete(session)

    db.commit()

    return {"message": "Session deleted"}


@router.get("/plans/{id}/sessions")
def get_plan_sessions(id: int, db: Session = Depends(get_db)):
    sessions = db.query(TrainingSession).filter(TrainingSession.plan_id == id).all()

    return sessions
