import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api.models.database import get_db
from api.schemas.user_schema import UserOutputSchema
from main import app

from .utils import TestingSessionLocal


@pytest.fixture()
def session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)


def test_root(client):
    res = client.get('/')
    assert res.status_code == status.HTTP_200_OK
    assert res.json() == {'Hello': 'World'}


def test_create_user(client):
    data = {'email': 'test01@email.com', 'username': 'test01', 'password': 'test01'}
    res = client.post('/api/v1/users', json=data)

    user = UserOutputSchema(**res.json())
    assert res.status_code == status.HTTP_201_CREATED
    assert user.email == 'test01@email.com'
    assert user.username == 'test01'
