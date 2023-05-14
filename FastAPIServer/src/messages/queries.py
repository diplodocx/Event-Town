from sqlalchemy.orm import Session
import sqlalchemy as db

from src.auth.models import user


def read_users(session: Session):
    stmt = db.select(user.email).where(user.c.is_recipient == True)
    result = session.execute(stmt)
    data = result.fetchall()
    return data

