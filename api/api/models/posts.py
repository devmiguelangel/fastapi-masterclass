from uuid import uuid4

from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, String, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from api.models.votes import Vote

from .database import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid4)
    user_id = Column(UUID, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    is_published = Column(Boolean, default=True, nullable=False, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('NOW()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('NOW()'), onupdate=text('NOW()'))

    user = relationship('User')
    votes = relationship('Vote')

    @hybrid_property
    def votes_count(self):
        return len(self.votes)

    @votes_count.expression
    @classmethod
    def votes_count(cls):
        return (
            func.count(Vote.post_id)
        )
