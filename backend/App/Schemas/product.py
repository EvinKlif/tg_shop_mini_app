from pydantic import BaseModel
from typing import Optional


class ProductBase(BaseModel):
    name: str
    price: int
    photo_url: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True