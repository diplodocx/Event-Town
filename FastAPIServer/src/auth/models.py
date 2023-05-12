import sqlalchemy as db

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

