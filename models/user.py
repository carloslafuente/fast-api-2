# Python
from typing import Optional
from uuid import UUID
from datetime import date
# Pydantic
from pydantic import BaseModel
from pydantic import Field, EmailStr


class BaseUser(BaseModel):
    id: UUID = Field(...)
    email: EmailStr = Field(...)


class PasswordMixin(BaseModel):
    password: str = Field(..., min_length=8)


class UserLogin(BaseUser, PasswordMixin):
    pass


class User(BaseUser):
    username: str = Field(
        ...,
        min_length=1,
        max_length=80
    )
    names: str = Field(
        ...,
        min_length=1,
        max_length=80
    )
    lastname: str = Field(
        ...,
        min_length=1,
        max_length=80
    )
    birth_date: Optional[date] = Field(default=None)


class UserSignup(User, PasswordMixin):
    pass
