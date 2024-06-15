from typing import List, Optional

from fastapi import HTTPException, status
from pydantic import UUID4, EmailStr
from sqlalchemy.orm import Session

from api.repositories.user_repository import UserRepository
from api.schemas.user_schema import UserCreateSchema, UserOutputSchema


class UserService:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def get_all(self) -> List[Optional[UserOutputSchema]]:
        return self.repository.get_all()

    def get_by_id(self, id: UUID4) -> Optional[UserOutputSchema]:
        user = self.repository.get_by_id(id)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found')

        return UserOutputSchema(**user.__dict__)

    def get_by_email(self, email: EmailStr) -> Optional[UserOutputSchema]:
        user = self.repository.get_by_email(email)

        if not user:
            return None

        return UserOutputSchema(**user.__dict__)

    def create(self, data: UserCreateSchema) -> UserOutputSchema:
        try:
            return self.repository.create(data)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
