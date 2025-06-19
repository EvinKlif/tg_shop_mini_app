from fastapi import APIRouter, Depends, status, Form, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from App.Core.utils import save_photo
from App.Schemas.product import ProductCreate, Product as ProductSchema
from App.Services.product_service import list_products, add_product, service_delete_product
from App.DataBase.session import get_session

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[ProductSchema])
async def get_products(db: AsyncSession = Depends(get_session)):
    return await list_products(db)


@router.post("/", response_model=ProductSchema, status_code=status.HTTP_201_CREATED)
async def create_product(name: str = Form(...), price: int = Form(...), photo: UploadFile = File(...), db: AsyncSession = Depends(get_session)):
    photo_url = await save_photo(photo)
    product_data = {
        "name": name,
        "price": price,
        "photo_url": photo_url
    }
    return await add_product(db, product_data)


@router.delete("/{product_id}", status_code=status.HTTP_200_OK)
async def delete_product_endpoint(product_id: int, db: AsyncSession = Depends(get_session)):
    return await service_delete_product(db, product_id)