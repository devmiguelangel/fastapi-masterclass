from fastapi import status
import pytest

from api.schemas.auth_schema import TokenSchema
from api.schemas.user_schema import UserOutputSchema


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


@pytest.mark.parametrize(('email', 'password', 'status_code'), [
    ('wrongEmail@email.com', 'password123', status.HTTP_404_NOT_FOUND),
    ('someUser@email.com', 'wrongPassword123', status.HTTP_404_NOT_FOUND),
    ('wrongEmail@email.com', 'wrongPassword123', status.HTTP_404_NOT_FOUND),
    (None, 'password123', status.HTTP_422_UNPROCESSABLE_ENTITY),
    ('someUser@email.com', None, status.HTTP_422_UNPROCESSABLE_ENTITY),
])
def test_auth_login_invalid(client, email, password, status_code):
    data = {'username': email, 'password': password}
    res = client.post('/api/v1/auth/login', data=data)

    assert res.status_code == status_code
