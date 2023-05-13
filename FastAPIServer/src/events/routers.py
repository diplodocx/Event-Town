from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

manager = APIRouter(
    prefix="/manager",
    tags=['manager']
)


@manager.get("/events", response_model=List[CategoryGet])
async def get_category(session: AsyncSession = Depends(get_async_session)):
    return
