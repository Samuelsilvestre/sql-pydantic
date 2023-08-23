from sqlalchemy import Column, String, Integer
from src.config.base import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key = True)
    user_name = Column(String(50))
    email = Column(String(50))