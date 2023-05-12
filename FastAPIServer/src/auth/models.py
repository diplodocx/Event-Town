import sqlalchemy as db
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped

metadata = db.MetaData()

user = db.Table(
    "user",
    metadata,
    db.Column("id", db.Integer, autoincrement=True, primary_key=True),
    db.Column("email", db.String(200), unique=True, nullable=False),
    db.Column("hashed_password", db.String(length=1024), nullable=False),
    db.Column("is_active", db.Boolean, default=True, nullable=False),
    db.Column("is_superuser", db.Boolean, default=False, nullable=False),
    db.Column("is_verified", db.Boolean, default=False, nullable=False),
    db.Column("is_recipient", db.Boolean, default=False, nullable=False)
)

class Base(DeclarativeBase):
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(
        db.Integer, autoincrement=True, primary_key=True
    )
    email: Mapped[str] = mapped_column(
        db.String(200), unique=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        db.String(1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        db.Boolean, default=True, nullable=False
    )
    is_superuser: Mapped[bool] = mapped_column(
        db.Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        db.Boolean, default=False, nullable=False
    )
    is_recipient: Mapped[bool] = mapped_column(
        db.Boolean, default=False, nullable=False
    )