from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Plan(Base):
    __tablename__ = "plans"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    athlete_id = Column(Integer, ForeignKey("users.id"))
