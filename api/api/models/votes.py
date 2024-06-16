from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, text
from sqlalchemy.dialects.postgresql import UUID

from .database import Base


class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    post_id = Column(UUID, ForeignKey('posts.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(UUID, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('NOW()'))
