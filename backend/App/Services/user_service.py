from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from App.Repositories.user_repository import create_user, get_user_by_telegram_id, get_all_user


async def list_user(db: AsyncSession):
    return await get_all_user(db)


async def register_user(db: AsyncSession, telegram_id: int, username: str | None, full_name: str | None):
    try:
        existing_user = await get_user_by_telegram_id(db, telegram_id)
        if existing_user:
            return {"user": existing_user, "created": False}

        new_user = await create_user(db, telegram_id, username, full_name)
        return {"user": new_user, "created": True}

    except SQLAlchemyError as e:
        pass