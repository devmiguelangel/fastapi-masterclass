from typing import List, Optional

from pydantic import UUID4
from sqlalchemy.orm import Session

from api.repositories.post_repository import PostRepository
from api.schemas.post_schema import PostCreateSchema, PostOutputSchema


class PostService:
    def __init__(self, db: Session):
        self.repository = PostRepository(db)

    def get_all(self) -> List[Optional[PostOutputSchema]]:
        return self.repository.get_all()

    def get_by_id(self, id: UUID4) -> Optional[PostOutputSchema]:
        return self.repository.get_by_id(id)

    def create(self, data: PostCreateSchema) -> PostOutputSchema:
        return self.repository.create(data)
