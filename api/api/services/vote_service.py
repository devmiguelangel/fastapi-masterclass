from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.repositories.post_repository import PostRepository
from api.repositories.vote_repository import VoteRepository
from api.schemas.vote_schema import VoteSchema


class VoteService:
    def __init__(self, db: Session):
        self.repository = VoteRepository(db)
        self.post_repository = PostRepository(db)
        self.__user_id = None

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.repository.user_id = value
        self.__user_id = value

    def vote(self, data: VoteSchema) -> bool:
        post = self.post_repository.get_by_id(data.post_id)

        if not post:
            raise HTTPException(status_code=404, detail='Post not found')

        vote = self.repository.get_vote(data.post_id)

        if data.dir == 1:
            if vote:
                raise HTTPException(status_code=400, detail='User already voted')
            self.repository.create(data.post_id)

            return True
        else:
            if not vote:
                raise HTTPException(status_code=400, detail='User did not vote')

            self.repository.delete(vote)

            return False
