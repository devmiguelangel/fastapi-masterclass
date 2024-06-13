from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from api.models.database import get_db
from api.schemas.user_schema import UserCreateSchema, UserOutputSchema
from api.services.user_service import UserService

router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@router.get('/{id}', response_model=UserOutputSchema)
def get_user_by_id(id: UUID4, session: Session = Depends(get_db)) -> UserOutputSchema:
    _service = UserService(session)
    return _service.get_by_id(id)

@router.post('/', status_code=201, response_model=UserOutputSchema)
def create_user(data: UserCreateSchema, session: Session = Depends(get_db)) -> UserOutputSchema:
    _service = UserService(session)
    return _service.create(data)
