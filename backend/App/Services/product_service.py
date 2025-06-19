from sqlalchemy.ext.asyncio import AsyncSession

from App.Repositories.product_repository import get_all_products, get_product_by_id, create_product, \
    get_product_by_name, delete_product


async def list_products(db: AsyncSession):
    return await get_all_products(db)


async def get_product_details(db: AsyncSession, product_id: int):
    product = await get_product_by_id(db, product_id)
    if not product:
        raise ValueError("Product not found")
    return product


async def add_product(db: AsyncSession, product_data: dict):
    name = product_data.get("name")
    if not name:
        raise ValueError("Name is required")

    existing = await get_product_by_name(db, name)
    if existing:
        raise ValueError("Product with this name already exists")
    return await create_product(db, product_data)


async def service_delete_product(db: AsyncSession, product_id: int):
    deleted_product = await delete_product(db, product_id)
    if not deleted_product:
        return None
    return {"message": "Product deleted successfully", "product_id": product_id}
