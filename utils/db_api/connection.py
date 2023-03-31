from typing import Sequence
from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession

from utils.db_api.base import Base
from utils.db_api.models import Users, Projects


class Database:
    async def load(self) -> AsyncSession:
        engine = create_async_engine(
            "sqlite+aiosqlite:///database.db",
            future=True
        )

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        async_sessionmaker = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession
        )

        self.async_session = async_sessionmaker

    # ---Users---

    async def reg_user(self, user_id: str, username: str, first_name: str):
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession
            await session.merge(
                Users(
                    user_id=user_id,
                    username=username,
                    first_name=first_name
                )
            )
            await session.commit()

    async def get_user(self, user_id) -> Users:
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.get(Users, user_id)
            return response

    # ---Projects---

    async def reg_project(self, title: str, description: str, demo: str, github: str):
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession
            await session.merge(
                Projects(
                    title=title,
                    description=description,
                    demo=demo,
                    github=github
                )
            )
            await session.commit()

    async def get_all_projects(self) -> Sequence[Projects]:
        """Some docs"""
        async with self.async_session() as session:
            session: AsyncSession

            response = await session.execute(select(Projects))
            return response.scalars().all()
