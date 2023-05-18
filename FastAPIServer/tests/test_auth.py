from .conftest import client


def test_register():
    response = client.post("/auth/register", json={
        "email": "test@test.com",
        "password": "test",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "is_recipient": True
    })
    assert response.status_code == 201


def test_login():
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
    assert response.status_code == 200
