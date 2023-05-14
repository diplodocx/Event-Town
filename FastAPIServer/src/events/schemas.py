from datetime import datetime

from pydantic import BaseModel


class EventGet(BaseModel):
    id: int
    title: str
    description: str
    date: datetime


class EventPost(BaseModel):
    title: str
    description: str
    date: datetime
