import sqlalchemy as db
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .models import event


async def create_event(data, session: AsyncSession):
    stmt = db.insert(event).values(**data.dict())
    await session.execute(stmt)
    await session.commit()
    return {"detail": "done"}


async def read_events(session: AsyncSession):
    stmt = db.select(event)
    res = await session.execute(stmt)
    return res.mappings().fetchall()


async def read_event(event_id, session: AsyncSession):
    stmt = db.select(event).where(event.c.id == event_id)
    res = await session.execute(stmt)
    element = res.mappings().fetchone()
    if not element:
        raise HTTPException(status_code=404, detail="Item not found")
    return element


async def delete_event(event_id, session: AsyncSession):
    stmt = db.select(event).where(event.c.id == event_id)
    res = await session.execute(stmt)
    element = res.fetchone()
    if not element:
        raise HTTPException(status_code=404, detail="Item not found")
    stmt = event.delete().where(event.c.id == event_id)
    await session.execute(stmt)
    await session.commit()
    return {"detail": "done"}
