from typing import List, Optional

from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from api.repositories.post_repository import PostRepository
from api.schemas.post_schema import PostCreateSchema, PostEditSchema, PostOutputSchema


class PostService:
    def __init__(self, db: Session):
        self.repository = PostRepository(db)
        self.__user_id = None

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.repository.user_id = value
        self.__user_id = value

    def get_all(self) -> List[Optional[PostOutputSchema]]:
        return self.repository.get_all()

    def get_by_id(self, id: UUID4) -> Optional[PostOutputSchema]:
        post = self.repository.get_by_id(id)

        if not post:
            raise HTTPException(status_code=404, detail='Post not found')

        if post.user_id != self.user_id:
            raise HTTPException(status_code=403, detail='You are not allowed to view this post')

        return PostOutputSchema(**post.__dict__)

    def create(self, data: PostCreateSchema) -> PostOutputSchema:
        return self.repository.create(data)

    def update(self, id: UUID4, data: PostEditSchema) -> PostOutputSchema:
        post = self.repository.get_by_id(id)

        if not post:
            raise HTTPException(status_code=404, detail='Post not found')

        if post.user_id != self.user_id:
            raise HTTPException(status_code=403, detail='You are not allowed to update this post')

        return self.repository.update(post, data)

    def delete(self, id: UUID4) -> bool:
        post = self.repository.get_by_id(id)

        if not post:
            raise HTTPException(status_code=404, detail='Post not found')

        if post.user_id != self.user_id:
            raise HTTPException(status_code=403, detail='You are not allowed to delete this post')

        return self.repository.delete(post)
