from typing import List, Optional

from sqlalchemy.orm import Session

from api.models.posts import Post
from api.schemas.post_schema import PostOutputSchema


class PostRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Optional[PostOutputSchema]]:
        posts = self.db.query(Post).all()
        return [PostOutputSchema(**post.__dict__) for post in posts]
