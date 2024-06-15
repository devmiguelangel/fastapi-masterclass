from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import EmailStr
from sqlalchemy.orm import Session

from api.config.settings import Settings
from api.models.database import get_db
from api.schemas.auth_schema import TokenDataSchema
from api.services.user_service import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

settings = Settings()

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str, credentials_exception: HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload is None:
            raise credentials_exception

        email: EmailStr = payload.get('sub')

        if email is None:
            raise credentials_exception

        return TokenDataSchema(email=email)
    except JWTError as e:
        raise credentials_exception from e


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )

    token = decode_access_token(token, credentials_exception)

    user_service = UserService(db)
    user = user_service.get_by_email(token.email)

    if user is None:
        raise credentials_exception

    return user
