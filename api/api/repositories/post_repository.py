from typing import List, Optional, Type

from pydantic import UUID4
from sqlalchemy.orm import Session

from api.models.posts import Post
from api.schemas.post_schema import PostCreateSchema, PostOutputSchema


class PostRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Optional[PostOutputSchema]]:
        posts = self.db.query(Post).all()
        return [PostOutputSchema(**post.__dict__) for post in posts]

    def get_by_id(self, id: UUID4) -> Type[Optional[Post]]:
        return self.db.query(Post).filter(Post.id == id).first()

    def create(self, data: PostCreateSchema) -> PostOutputSchema:
        post = Post(**data.model_dump())
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)

        return PostOutputSchema(**post.__dict__)

    def delete(self, post: Type[Post]) -> bool:
        self.db.delete(post)
        self.db.commit()
        return True
