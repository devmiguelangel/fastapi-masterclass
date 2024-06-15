from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from api.models.database import get_db
from api.schemas.auth_schema import TokenSchema
from api.services.auth_service import AuthService

router = APIRouter(
    prefix='/auth',
    tags=['authentication'],
)

@router.post('/login', status_code=status.HTTP_200_OK)
def login(credentials: Annotated[OAuth2PasswordRequestForm, Depends()], session: Session = Depends(get_db)) -> TokenSchema:
    _service = AuthService(session)
    return _service.get_access_token(credentials)
