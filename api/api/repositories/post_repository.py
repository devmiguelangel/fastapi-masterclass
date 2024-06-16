from typing import List, Optional, Type

from pydantic import UUID4
from sqlalchemy.orm import Session, joinedload

from api.models.posts import Post
from api.schemas.post_schema import PostCreateSchema, PostEditSchema, PostOutputSchema, PostParamsSchema


class PostRepository:
    def __init__(self, db: Session):
        self.db = db
        self.__user_id = None

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    def get_all(self, query_params: PostParamsSchema) -> List[Optional[PostOutputSchema]]:
        posts = self.db.query(Post).options(joinedload(Post.user)) \
                    .filter(Post.user_id == self.user_id, Post.title.icontains(query_params['search'])) \
                    .limit(query_params['limit']) \
                    .offset(query_params['skip']) \
                    .all()
        return [PostOutputSchema(**post.__dict__) for post in posts]

    def get_by_id(self, id: UUID4) -> Type[Optional[Post]]:
        return self.db.query(Post).options(joinedload(Post.user)).filter(Post.id == id).first()

    def create(self, data: PostCreateSchema) -> PostOutputSchema:
        post = Post(user_id=self.user_id, **data.model_dump())
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
        self.db.delete(post)
        self.db.commit()
        return True
