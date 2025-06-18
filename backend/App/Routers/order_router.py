from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from App.Schemas.order import OrderCreate, Order
from App.Services.order_service import get_order_details, list_user_orders, place_orders
from App.DataBase.session import get_session


router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=List[OrderCreate], status_code=status.HTTP_201_CREATED)
async def create_order(orders: List[OrderCreate], db: AsyncSession = Depends(get_session)):
    return await place_orders(db, orders)


@router.get("/{order_id}", response_model=Order)
async def read_order(order_id: int, db: AsyncSession = Depends(get_session)):
    return await get_order_details(db, order_id)


@router.get("/user/{user_id}", response_model=list[Order])
async def read_user_orders(user_id: int, db: AsyncSession = Depends(get_session)):
    return await list_user_orders(db, user_id)