from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from App.Models import Order
from App.Repositories.order_repository import create_order, get_order_by_id, get_orders_by_user
from App.Repositories.user_repository import get_user_by_telegram_id
from App.Schemas.order import OrderCreate


async def place_orders(db: AsyncSession, orders: List[OrderCreate]):
    results = []
    for order in orders:
        data = order.model_dump()
        telegram_id = data.get("user_id")
        if not telegram_id:
            raise ValueError("user_id is required")

        user = await get_user_by_telegram_id(db, telegram_id)
        db_order = Order(user_id=user.id, product_id=data["product_id"], quantity=data["quantity"])
        db.add(db_order)
        results.append(db_order)

    await db.commit()
    for order in results:
        await db.refresh(order)

    return results


async def get_order_details(db: AsyncSession, order_id: int):
    order = await get_order_by_id(db, order_id)
    if not order:
        raise ValueError("Order not found")
    return order


async def list_user_orders(db: AsyncSession, user_id: int):
    return await get_orders_by_user(db, user_id)