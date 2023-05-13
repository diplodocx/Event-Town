from datetime import datetime

from pydantic import BaseModel


class EventGet(BaseModel):
    pass


class EventPost(BaseModel):
    title: str
    description: str
    date: datetime
