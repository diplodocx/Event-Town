import sqlalchemy as db
from sqlalchemy.ext.asyncio import AsyncSession
from .models import event


async def create_event(data, session: AsyncSession):
    stmt = db.insert(event).values(**data.dict())
    await session.execute(stmt)
    await session.commit()
    return {"detail": "done"}
