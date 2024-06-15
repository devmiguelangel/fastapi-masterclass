from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.repositories.user_repository import UserRepository
from api.utils.oauth2 import create_access_token


class AuthService:
    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def get_access_token(self, credentials: OAuth2PasswordRequestForm) -> dict:
        user = self.user_repository.get_by_credentials(credentials)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')

        access_token = create_access_token(data={'sub': user.email})

        return {'access_token': access_token, 'token_type': 'bearer'}
