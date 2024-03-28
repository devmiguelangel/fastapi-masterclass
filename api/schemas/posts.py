from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreateSchema(PostBase):
    pass


class PostResponseSchema(PostBase):
    published: bool

    class Config:
        from_attributes = True
