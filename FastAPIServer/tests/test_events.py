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


def test_get_events():
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


def test_get_event():
    jwt = get_jwt().json()["access_token"]
    response = client.get("/events/event/1", headers={
        'Authorization': f'Bearer {jwt}'
    })
    assert response.status_code == 200
    assert response.json()["title"] == "test0"


async def test_update_event():
    jwt = get_jwt().json()["access_token"]
    response = client.put("/events/event/1", headers={
        'Authorization': f'Bearer {jwt}'
    }, json={
        "title": "test0",
        "description": "!!",
        "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    })
    assert response.status_code == 200
    async with async_session_maker() as session:
        stmt = db.select(event.c.description)
        result = await session.execute(stmt)
        assert result.fetchall()[0][0] == "!!"
    jwt = get_jwt().json()["access_token"]
    response = client.put(f"/events/event/{test_range + 1}", headers={
        'Authorization': f'Bearer {jwt}'
    }, json={
        "title": "test_new",
        "description": "--",
        "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    })
    assert response.status_code == 201


async def test_delete_event():
    jwt = get_jwt().json()["access_token"]
    response = client.delete(f"/events/event/{test_range + 1}", headers={
        'Authorization': f'Bearer {jwt}'
    })
    assert response.status_code == 200
    async with async_session_maker() as session:
        stmt = db.select(event).where(id == test_range)
        result = await session.execute(stmt)
        assert result.fetchall() == []
