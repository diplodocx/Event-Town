from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session
from .schemas import EventGet, EventPost
from . import queries

events = APIRouter(
    prefix="/events",
    tags=['events']
)


@events.post("/event")
async def post_event(event: EventPost, session: AsyncSession = Depends(get_async_session)):
    return await queries.create_event(event, session)


@events.get("/event", response_model=List[EventGet])
async def get_events(session: AsyncSession = Depends(get_async_session)):
    return await queries.read_events(session)


@events.get("/event/{event_id}", response_model=EventGet)
async def retrieve_event(event_id: int, session: AsyncSession = Depends(get_async_session)):
    return await queries.read_event(event_id, session)
