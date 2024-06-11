from typing import List, Optional

from fastapi import HTTPException
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
        post = self.repository.get_by_id(id)

        if not post:
            raise HTTPException(status_code=404, detail='Post not found')

        return PostOutputSchema(**post.__dict__)

    def create(self, data: PostCreateSchema) -> PostOutputSchema:
        return self.repository.create(data)

    def delete(self, id: UUID4) -> bool:
        post = self.repository.get_by_id(id)

        if not post:
            raise HTTPException(status_code=404, detail='Post not found')

        return self.repository.delete(post)
