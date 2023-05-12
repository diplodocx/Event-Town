from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from fastapi_users.authentication import JWTStrategy
from config import AUTH_SECRET

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")
SECRET = AUTH_SECRET


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)