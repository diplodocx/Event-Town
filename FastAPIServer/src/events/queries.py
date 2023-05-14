import sqlalchemy as db
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from .models import event


async def create_event(data, session: AsyncSession):
    try:
        stmt = db.insert(event).values(**data.dict())
        await session.execute(stmt)
        await session.commit()
        return JSONResponse(content={"detail": "done"}, status_code=201)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Event with this title already exists")


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


async def update_event(event_id, data, session: AsyncSession):
    stmt = db.select(event).where(event.c.id == event_id)
    res = await session.execute(stmt)
    element = res.fetchone()
    if not element:
        return await create_event(data, session)
    else:
        stmt = db.update(event).where(event.c.id == event_id).values(**data.dict())
        await session.execute(stmt)
        return JSONResponse(content={"detail": "done"}, status_code=200)
