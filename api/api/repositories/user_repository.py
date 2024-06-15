from typing import List, Optional, Type

from fastapi.security import OAuth2PasswordRequestForm
from pydantic import UUID4, EmailStr
from sqlalchemy.orm import Session

from api.models.users import User
from api.schemas.user_schema import UserCreateSchema, UserOutputSchema
from api.utils import password


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Optional[UserOutputSchema]]:
        users = self.db.query(User).all()
        return [UserOutputSchema(**user.__dict__) for user in users]

    def get_by_id(self, id: UUID4) -> Type[Optional[User]]:
        return self.db.query(User).filter(User.id == id).first()

    def get_by_email(self, email: EmailStr) -> Type[Optional[User]]:
        return self.db.query(User).filter(User.email == email).first()

    def get_by_credentials(self, credentials: OAuth2PasswordRequestForm) -> Optional[User]:
        user = self.db.query(User).filter(User.email == credentials.username).first()

        if not user:
            return None

        if not password.verify(credentials.password, user.password):
            return None

        return user

    def create(self, data: UserCreateSchema) -> UserOutputSchema:
        hashed_password = password.hash(data.password)
        data.password = hashed_password

        user = User(**data.model_dump())
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return UserOutputSchema(**user.__dict__)
