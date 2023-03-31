from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, DateTime

from utils.db_api.base import Base
from datetime import datetime


class Users(Base):
    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(20))
    first_name = Column(String(50))
    date = Column(DateTime, default=datetime.utcnow)


class Projects(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(50))
    demo = Column(String(50))
    github = Column(String(100))
    date = Column(DateTime, default=datetime.utcnow)