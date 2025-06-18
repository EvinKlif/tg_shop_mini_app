from pydantic import BaseModel
from typing import Optional
from typing import Generic, TypeVar

class UserBase(BaseModel):
    telegram_id: int
    username: Optional[str] = None
    full_name: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True

T = TypeVar("T")

class RegisterResponseSchema(BaseModel, Generic[T]):
    user: T
    created: bool

    class Config:
        from_attributes = True