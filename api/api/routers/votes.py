from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from api.models.database import get_db
from api.schemas.user_schema import UserOutputSchema
from api.schemas.vote_schema import VoteSchema
from api.services.vote_service import VoteService
from api.utils.oauth2 import get_current_user

router = APIRouter(
    prefix='/votes',
    tags=['votes'],
)

@router.post('/')
def vote(
    response: Response,
    data: VoteSchema,
    session: Session = Depends(get_db),
    current_user: Annotated[UserOutputSchema, Depends(get_current_user)] = None,
):
    _service = VoteService(session)
    _service.user_id = current_user.id
    result = _service.vote(data)

    if result:
        response.status_code = status.HTTP_201_CREATED
        return {'vote': 'Created'}

    response.status_code = status.HTTP_204_NO_CONTENT
    return {'vote': 'Deleted'}

