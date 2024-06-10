from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.models.database import get_db
from api.schemas.post_schema import PostCreateSchema, PostOutputSchema
from api.services.post_service import PostService

router = APIRouter(
    prefix='/posts',
    tags=['posts'],
)

@router.get('/', response_model=List[PostOutputSchema])
def get_posts(session: Session = Depends(get_db)) -> List[PostOutputSchema]:
    _service = PostService(session)
    return _service.get_all()

@router.post('/')
def create_post(data: PostCreateSchema, session: Session = Depends(get_db)) -> PostOutputSchema:
    _service = PostService(session)
    return _service.create(data)
