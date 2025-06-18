from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from App.DataBase.session import get_session
from App.Schemas.user import UserCreate, RegisterResponseSchema, User
from App.Services.user_service import register_user, list_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=RegisterResponseSchema[User], status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_session)):
    return await register_user(db, **user.model_dump())


@router.get("/", response_model=list[User])
async def get_products(db: AsyncSession = Depends(get_session)):
    return await list_user(db)
