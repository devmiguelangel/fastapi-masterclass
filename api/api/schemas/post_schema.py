from typing import Optional

from pydantic import UUID4, BaseModel

from api.schemas.user_schema import UserOutputSchema


class PostBase(BaseModel):
    title: str
    content: str
    is_published: bool = True

class PostParamsSchema(BaseModel):
    limit: int = 10
    skip: int = 0
    search: Optional[str] = ''

class PostCreateSchema(PostBase):
    pass

class PostEditSchema(PostBase):
    pass

class PostOutputSchema(PostBase):
    id: UUID4
    votes: Optional[int] = 0
    user: UserOutputSchema

    class Config:
        from_attributes = True
