from pydantic import BaseModel


class PlanCreate(BaseModel):
    title: str
    athlete_id: int
