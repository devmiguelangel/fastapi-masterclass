import pytest
from fastapi import status
from fastapi.testclient import TestClient

from api.models.database import get_db
from api.schemas.auth_schema import TokenSchema
from api.schemas.user_schema import UserOutputSchema
from main import app

from .utils import TestingSessionLocal


@pytest.fixture(scope='session')
def session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope='session')
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


def test_auth_login(client):
    data = {'username': 'test01@email.com', 'password': 'test01'}
    res = client.post('/api/v1/auth/login', data=data)

    token = TokenSchema(**res.json())

    assert res.status_code == status.HTTP_200_OK
    assert token.access_token is not None
    assert token.token_type == 'bearer'
