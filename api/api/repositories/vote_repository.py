from typing import Optional, Type

from pydantic import UUID4
from sqlalchemy.orm import Session

from api.models.votes import Vote


class VoteRepository:
    def __init__(self, db: Session):
        self.db = db
        self.__user_id = None

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    def get_vote(self, post_id: UUID4) -> Type[Optional[Vote]]:
        return self.db.query(Vote).filter(Vote.post_id == post_id, Vote.user_id == self.user_id).first()

    def create(self, post_id: UUID4) -> Type[Vote]:
        vote = Vote(post_id=post_id, user_id=self.user_id)
        self.db.add(vote)
        self.db.commit()
        self.db.refresh(vote)

        return vote

    def delete(self, vote: Type[Vote]) -> bool:
        self.db.delete(vote)
        self.db.commit()
        return True
