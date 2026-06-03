from sqlalchemy import Column, Integer, String, Float, ForeignKey

from app.database import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)

    date = Column(String)

    title = Column(String)

    type = Column(String)

    zone = Column(String)

    distance = Column(Float)

    duration = Column(String)

    pace = Column(String)

    heart_rate = Column(String)

    details = Column(String)

    strava_link = Column(String)

    resource_link = Column(String)

    plan_id = Column(Integer, ForeignKey("plans.id"))
