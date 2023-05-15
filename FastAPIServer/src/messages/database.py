from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
session_maker = sessionmaker(engine, expire_on_commit=False)


def get_session() -> Generator[Session, None, None]:
    with session_maker() as session:
        yield session