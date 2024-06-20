import base64

from typing import Tuple, Type

from sqlalchemy import select, Result
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from backend.core.models import User

from .shemas import UserCreate


class PasswordCoding:
    @staticmethod
    def encode_password(password: str) -> str:
        return base64.b64encode(password.encode()).decode()

    @staticmethod
    def decode_password(encoded_password: str) -> str:
        return base64.b64decode(encoded_password.encode()).decode()


class DatabaseUser:
    @staticmethod
    async def add_user(session: AsyncSession, user_in: UserCreate) -> User | None:
        user_in.password = PasswordCoding.encode_password(user_in.password)
        print({**user_in.model_dump()})
        user = User(**user_in.model_dump())
        print(user.__dict__)
        session.add(user)
        await session.commit()
        return user

# -> Type[User] | None
    @staticmethod
    async def get_user(session: AsyncSession, login: str, password: str):
        statement = select(User).order_by(User.username)
        result: Result = await session.execute(statement)

        print(result.all())




