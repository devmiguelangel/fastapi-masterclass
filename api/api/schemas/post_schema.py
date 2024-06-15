from pydantic import UUID4, BaseModel

from api.schemas.user_schema import UserOutputSchema


class PostBase(BaseModel):
    title: str
    content: str
    is_published: bool = True

class PostCreateSchema(PostBase):
    pass

class PostEditSchema(PostBase):
    pass

class PostOutputSchema(PostBase):
    id: UUID4
    user: UserOutputSchema

    class Config:
        from_attributes = True
