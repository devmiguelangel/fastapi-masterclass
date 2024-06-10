from typing import List, Optional

from sqlalchemy.orm import Session

from api.repositories.post_repository import PostRepository
from api.schemas.post_schema import PostCreateSchema, PostOutputSchema


class PostService:
    def __init__(self, db: Session):
        self.repository = PostRepository(db)

    def get_all(self) -> List[Optional[PostOutputSchema]]:
        return self.repository.get_all()

    def create(self, data: PostCreateSchema) -> PostOutputSchema:
        return self.repository.create(data)
