from sqlalchemy import Column, Integer, String

from App.DataBase.session import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)
    photo_url = Column(String(255))