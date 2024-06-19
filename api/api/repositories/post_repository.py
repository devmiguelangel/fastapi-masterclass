from typing import List, Optional, Type

from pydantic import UUID4
from sqlalchemy.orm import Session, aliased, joinedload

from api.models.posts import Post
from api.models.users import User
from api.models.votes import Vote
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

    def get_by_id_query(self, id: UUID4):
        return self.db.query(Post).filter(Post.id == id)

    def get_all(self, query_params: PostParamsSchema) -> List[Optional[PostOutputSchema]]:
        user_alias = aliased(User)

        posts = self.db.query(Post, Post.votes_count) \
                    .options(joinedload(Post.user.of_type(user_alias))) \
                    .join(Vote, Vote.post_id == Post.id, isouter=True) \
                    .filter(Post.user_id == self.user_id, Post.title.icontains(query_params['search'])) \
                    .group_by(Post.id, user_alias.id) \
                    .limit(query_params['limit']) \
                    .offset(query_params['skip']) \
                    .all()
        return [PostOutputSchema(**post.Post.__dict__, votes=post.votes_count) for post in posts]

    def get_by_id(self, id: UUID4) -> Type[Optional[Post]]:
        user_alias = aliased(User)

        query = self.db.query(Post, Post.votes_count) \
                    .options(joinedload(Post.user.of_type(user_alias))) \
                    .join(Vote, Vote.post_id == Post.id, isouter=True) \
                    .filter(Post.id == id) \
                    .group_by(Post.id, user_alias.id).first()

        return query

    def create(self, data: PostCreateSchema) -> PostOutputSchema:
        post = Post(user_id=self.user_id, **data.model_dump())
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)

        return PostOutputSchema(**post.__dict__, user=post.user.__dict__)

    def update(self, post: Type[Post], data: PostEditSchema) -> PostOutputSchema:
        for key, value in data.model_dump(exclude_none=True).items():
            setattr(post, key, value)

        self.db.commit()
        self.db.refresh(post)
        return PostOutputSchema(**post.__dict__, user=post.user.__dict__, votes=post.votes_count)

    def delete(self, post: Type[Post]) -> bool:
        self.db.delete(post)
        self.db.commit()
        return True
