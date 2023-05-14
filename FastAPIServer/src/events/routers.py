from typing import List, Optional
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
async def get_events(per_page: int = 20, page: int = 1, session: AsyncSession = Depends(get_async_session)):
    return await queries.read_events(per_page, page, session)


@events.get("/event/{event_id}", response_model=EventGet)
async def retrieve_event(event_id: int, session: AsyncSession = Depends(get_async_session)):
    return await queries.read_event(event_id, session)


@events.delete("/events/{event_id}")
async def delete_event(event_id: int, session: AsyncSession = Depends(get_async_session)):
    return await queries.delete_event(event_id, session)


@events.put("/events/{event_id}")
async def put_event(event_id: int, event: EventPost, session: AsyncSession = Depends(get_async_session)):
    return await queries.update_event(event_id, event, session)
