from datetime import datetime

from pydantic import UUID4, BaseModel, EmailStr


class UserBase(BaseModel):
    id: UUID4
    username: str
    email: EmailStr
    created_at: datetime

class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOutputSchema(UserBase):
    class Config:
        from_attributes = True
