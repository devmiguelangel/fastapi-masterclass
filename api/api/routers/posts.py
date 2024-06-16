from typing import Annotated, List, Optional

from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session

from api.models.database import get_db
from api.schemas.post_schema import PostCreateSchema, PostEditSchema, PostOutputSchema, PostParamsSchema
from api.schemas.user_schema import UserOutputSchema
from api.services.post_service import PostService
from api.utils.oauth2 import get_current_user

router = APIRouter(
    prefix='/posts',
    tags=['posts'],
)

@router.get('/', status_code=200, response_model=List[PostOutputSchema])
def get_posts(
    session: Session = Depends(get_db),
    current_user: Annotated[UserOutputSchema, Depends(get_current_user)] = None,
    limit: Optional[int] = 10,
    skip: Optional[int] = 0,
    search: Optional[str] = '',
) -> List[PostOutputSchema]:
    query_params: PostParamsSchema = {
        'limit': limit,
        'skip': skip,
        'search': search,
    }

    _service = PostService(session)
    _service.user_id = current_user.id
    return _service.get_all(query_params)

@router.get('/{id}', status_code=200, response_model=PostOutputSchema)
def get_post(
    id: UUID4,
    session: Session = Depends(get_db),
    current_user: Annotated[UserOutputSchema, Depends(get_current_user)] = None
):
    _service = PostService(session)
    _service.user_id = current_user.id
    return _service.get_by_id(id)

@router.post('/', status_code=201, response_model=PostOutputSchema)
def create_post(
    data: PostCreateSchema,
    session: Session = Depends(get_db),
    current_user: Annotated[UserOutputSchema, Depends(get_current_user)] = None
) -> PostOutputSchema:
    _service = PostService(session)
    _service.user_id = current_user.id
    return _service.create(data)

@router.put('/{id}', status_code=200, response_model=PostOutputSchema)
def update_post(
    id: UUID4,
    data: PostEditSchema,
    session: Session = Depends(get_db),
    current_user: Annotated[UserOutputSchema, Depends(get_current_user)] = None
):
    _service = PostService(session)
    _service.user_id = current_user.id
    return _service.update(id, data)

@router.delete('/{id}', status_code=204)
def delete_post(
    id: UUID4,
    session: Session = Depends(get_db),
    current_user: Annotated[UserOutputSchema, Depends(get_current_user)] = None
):
    _service = PostService(session)
    _service.user_id = current_user.id
    return _service.delete(id)
