from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from App.Models import UserDB


async def get_all_user(db: AsyncSession):
    result = await db.execute(select(UserDB))
    return result.scalars().all()


async def get_user_by_telegram_id(db: AsyncSession, telegram_id: int) -> UserDB | None:
    result = await db.execute(select(UserDB).where(UserDB.telegram_id == telegram_id))
    return result.scalars().first()


async def create_user(db: AsyncSession, telegram_id: int, username: str, full_name: str):
    db_user = UserDB(telegram_id=telegram_id, username=username, full_name=full_name)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user