from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database settings
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
