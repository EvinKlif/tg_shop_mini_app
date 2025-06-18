from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from App.Models.product import Product


async def get_all_products(db: AsyncSession):
    result = await db.execute(select(Product))
    return result.scalars().all()


async def get_product_by_id(db: AsyncSession, product_id: int):
    result = await db.execute(select(Product).where(Product.id == product_id))
    return result.scalars().first()


async def get_product_by_name(db: AsyncSession, name: str):
    result = await db.execute(
        select(Product).where(Product.name == name)
    )
    return result.scalars().first()


async def create_product(db: AsyncSession, product_data: dict):
    db_product = Product(**product_data)
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product
