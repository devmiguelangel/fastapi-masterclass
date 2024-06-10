from pydantic import UUID4, BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    is_published: bool = True

class PostCreateSchema(PostBase):
    pass

class PostOutputSchema(PostBase):
    id: UUID4

    class Config:
        from_attributes = True
