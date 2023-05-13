from fastapi import FastAPI, Depends

from src.auth.auth import auth_backend
from src.auth.routers import fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.events.routers import events

#
# from src.auth.auth import auth_backend
# from src.auth.models import User
# from src.auth.routers import fastapi_users
# from src.auth.schemas import UserRead, UserCreate
# from src.manager.routers import manager
# from src.reports.routers import reports

app = FastAPI(title="eventtown app")

# current_user = fastapi_users.current_user()
#
# app.include_router(manager)
app.include_router(events)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
