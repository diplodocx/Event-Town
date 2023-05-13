from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from .schemas import EventGet, EventPost
from . import queries

manager = APIRouter(
    prefix="/events",
    tags=['events']
)

@manager.post("/event")
async def post_event(event: EventPost, session: AsyncSession = Depends(get_async_session)):
    return queries.create_event()

@manager.get("/event", response_model=List[EventGet])
async def get_events(session: AsyncSession = Depends(get_async_session)):
    return
