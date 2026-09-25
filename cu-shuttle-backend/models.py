# models.py

from pydantic import BaseModel


class LocationData(BaseModel):
    user_id: str
    route: str
    latitude: float
    longitude: float
    accuracy: float | None = None
    speed: float | None = None
    heading: float | None = None
    timestamp: int