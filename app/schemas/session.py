from pydantic import BaseModel


class SessionCreate(BaseModel):

    date: str

    title: str

    type: str

    zone: str

    distance: float

    duration: str

    pace: str

    heart_rate: str

    details: str

    strava_link: str

    resource_link: str

    plan_id: int


class SessionUpdate(BaseModel):

    title: str

    type: str

    zone: str

    distance: float

    duration: str

    pace: str

    heart_rate: str

    details: str
