import pytest
from fastapi import status
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from alembic import command
from alembic.config import Config
from api.config.settings import Settings
from api.models.database import get_db
from api.schemas.user_schema import UserOutputSchema
from api.utils.oauth2 import create_access_token
from main import app

settings = Settings()

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.db_test_user}:{settings.db_test_password}@{settings.db_test_host}:{settings.db_test_port}/{settings.db_test_name}'

def migrate_in_memory(migrations_path, alembic_ini_path='alembic.ini', connection=None, revision='head'):
    config = Config(alembic_ini_path)
    config.set_main_option('script_location', migrations_path)
    config.set_main_option('sqlalchemy.url', SQLALCHEMY_DATABASE_URL)
    if connection is not None:
        config.attributes['connection'] = connection

    command.downgrade(config, 'base')
    command.upgrade(config, revision)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

with engine.begin() as connection:
    migrate_in_memory('alembic', 'alembic.ini', connection)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def override_get_db():
    db: Session = TestingSessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


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


@pytest.fixture(scope='session')
def test_user(client):
    data = {'email': 'john@email.com', 'username': 'john', 'password': 'password123'}
    res = client.post('/api/v1/users', json=data)

    user = UserOutputSchema(**res.json())
    assert res.status_code == status.HTTP_201_CREATED
    assert user.email == 'john@email.com'
    assert user.username == 'john'

    return data


@pytest.fixture(scope='session')
def token(test_user):
    return create_access_token(data={'sub': test_user['email']})


@pytest.fixture(scope='session')
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        'Authorization': f'Bearer {token}',
    }

    return client
