# Python
from uuid import UUID
from typing import Optional
from datetime import date
# Pydantic
from pydantic import BaseModel, EmailStr, Field


class User(BaseModel):
    birth_date: Optional[date] = Field(default=None)
    email: EmailStr = Field(...)
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    user_id: UUID = Field(...)


class UserLogin(User):
    password: str = Field(..., min_length=8)
