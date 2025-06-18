from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from App.Models.order import Order


async def create_order(db: AsyncSession, user_id: int, product_id: int, quantity: int):
    db_order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order


async def get_order_by_id(db: AsyncSession, order_id: int):
    result = await db.execute(select(Order).where(Order.id == order_id))
    return result.scalars().first()


async def get_orders_by_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(Order).where(Order.user_id == user_id))
    return result.scalars().all()