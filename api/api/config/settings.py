from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Database settings
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str
    # Database test settings
    db_test_host: str
    db_test_port: int
    db_test_user: str
    db_test_password: str
    db_test_name: str
    # Authentication settings
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
