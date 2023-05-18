from datetime import datetime

from .test_auth import get_jwt
from .conftest import client, async_session_maker
import sqlalchemy as db
from events.models import event

test_range = 100


async def test_post_event():
    jwt = get_jwt().json()["access_token"]
    for i in range(test_range):
        response = client.post("/events/event", headers={
            'Authorization': f'Bearer {jwt}'
        }, json={
            "title": f"test{i}",
            "description": "--",
            "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        })
        assert response.status_code == 201
    async with async_session_maker() as session:
        stmt = db.select(event)
        result = await session.execute(stmt)
        assert len(result.fetchall()) == test_range


async def test_get_events():
    jwt = get_jwt().json()["access_token"]
    response = client.get("/events/event", headers={
        'Authorization': f'Bearer {jwt}'
    }, params={
        'per_page': 20,
        'page': 1
    })
    assert response.status_code == 200
    assert response.json()[0]["title"] == "test0"
    assert len(response.json()) <= 20


async def test_get_event():
    jwt = get_jwt().json()["access_token"]
    response = client.get("/events/event/1", headers={
        'Authorization': f'Bearer {jwt}'
    })
    assert response.status_code == 200
    assert response.json()["title"] == "test0"