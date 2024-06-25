from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from alembic import command
from alembic.config import Config
from api.config.settings import Settings

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
