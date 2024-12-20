from datetime import datetime

from sqlalchemy import Column, Integer, String, update, delete, Date, Boolean
from sqlalchemy.future import select

from aiobot.database import Base, db


class User(Base):
    user_id = Column(String(50), unique=True, primary_key=True)
    username = Column(String(30))
    is_admin = Column(Boolean, default=False)
    role = Column(String(30), default="user")

    def __repr__(self):
        return f'<{self.__class__.__name__}: user_id={self.user_id}, username={self.username}>'

    @classmethod
    async def create(cls, user_id, username):
        user = cls(user_id=user_id, username=username)
        db.add(user)
        await cls.commit()
        return user

    @classmethod
    async def get(cls, user_id):
        query = select(cls).where(cls.user_id == user_id)
        users = await db.execute(query)
        user, = users.first() or None,
        return user

    @classmethod
    async def get_all(cls):
        query = select(cls)
        users = await db.execute(query)
        return users

    @classmethod
    async def update(cls, user_id, **kwargs):
        query = (
            update(cls)
            .where(cls.user_id == user_id)
            .values(**kwargs)
            .execution_options(synchronize_session="fetch")
        )
        await db.execute(query)
        await cls.commit()

    @classmethod
    async def delete(cls, user_id):
        query = delete(cls).where(cls.user_id == user_id)
        await db.execute(query)
        await cls.commit()
        return True