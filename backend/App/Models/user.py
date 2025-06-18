from sqlalchemy import Column, String, BigInteger

from App.DataBase.session import Base


class UserDB(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    telegram_id = Column(BigInteger, unique=True)
    username = Column(String(64))
    full_name = Column(String(128))