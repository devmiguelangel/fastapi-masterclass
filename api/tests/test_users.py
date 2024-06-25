import pytest
from fastapi import status
from jose import jwt

from api.config.settings import Settings
from api.schemas.auth_schema import TokenSchema

settings = Settings()

def test_root(client):
    res = client.get('/')
    assert res.status_code == status.HTTP_200_OK
    assert res.json() == {'Hello': 'World'}


def test_auth_login(client, test_user):
    data = {'username': test_user['email'], 'password': test_user['password']}
    res = client.post('/api/v1/auth/login', data=data)

    token = TokenSchema(**res.json())
    payload = jwt.decode(token.access_token, settings.secret_key, algorithms=[settings.algorithm])

    assert payload.get('sub') == test_user['email']

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
