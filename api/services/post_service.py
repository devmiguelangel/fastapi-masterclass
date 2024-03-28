from sqlalchemy.orm import Session

from models import posts as models
from models.database import engine, get_db
from models.posts import Post
from schemas.posts import PostCreateSchema

models.Base.metadata.create_all(bind=engine)

class PostService:
    def __init__(self) -> None:
        self.db: Session = get_db().__next__()

    async def get_all(self):
        return self.db.query(Post).all()

    async def get_one(self, id: int):
        return self.db.query(Post).filter(Post.id == id).first()

    async def create(self, post: PostCreateSchema):
        new_post = Post(**post.model_dump())
        self.db.add(new_post)
        self.db.commit()
        self.db.refresh(new_post)

        return new_post

    async def update(self, id: int, post: PostCreateSchema):
        post_query = self.db.query(Post).filter(Post.id == id).first()

        if post_query is None:
            return False

        post_query.title = post.title
        post_query.content = post.content
        post_query.published = post.published

        self.db.commit()

        return post

    async def delete(self, id: int):
        post = self.db.query(Post).filter(Post.id == id)

        if post.first() is None:
            return False

        post.delete(synchronize_session=False)
        self.db.commit()

        return True
