import sqlalchemy as db
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

metadata = db.MetaData()

event = db.Table(
    "event",
    metadata,
    db.Column("id", db.Integer, autoincrement=True, primary_key=True),
    db.Column("title", db.String(200), unique=True, nullable=False),
    db.Column("description", db.String(2048), nullable=False),
    db.Column("date", db.TIMESTAMP, nullable=False)
)