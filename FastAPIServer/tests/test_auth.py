import sqlalchemy as db
from auth.models import user
from .conftest import client, async_session_maker


async def test_register():
    response = client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "test",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "is_recipient": True
    })
    assert response.status_code == 201
    async with async_session_maker() as session:
        stmt = db.select(user.c.email)
        result = await session.execute(stmt)
        assert result.fetchone() == ('test@test.com',)
        stmt = db.update(user).where(user.c.id == 1).values(is_superuser=True)
        await session.execute(stmt)
        await session.commit()


def get_jwt():
    response = client.post("/auth/login", headers={
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }, data={
        'grant_type': "",
        'username': 'test@test.com',
        'password': 'test',
        'scope': "",
        'client_id': "",
        'client_secret': ""
    })
    return response


def test_login():
    response = get_jwt()
    assert response.status_code == 200
