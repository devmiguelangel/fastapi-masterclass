from typing import List, Optional, Type

from pydantic import UUID4
from sqlalchemy.orm import Session

from api.models.posts import Post
from api.schemas.post_schema import PostCreateSchema, PostEditSchema, PostOutputSchema


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

    def update(self, post: Type[Post], data: PostEditSchema) -> PostOutputSchema:
        for key, value in data.model_dump(exclude_none=True).items():
            setattr(post, key, value)

        self.db.commit()
        self.db.refresh(post)
        return PostOutputSchema(**post.__dict__)

    def delete(self, post: Type[Post]) -> bool:
        post.delete(synchronize_session=False)
        self.db.commit()
        return True
