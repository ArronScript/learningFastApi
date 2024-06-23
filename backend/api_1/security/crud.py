import utils

from fastapi import HTTPException, status

from typing import Tuple, Type

from sqlalchemy import select, Result
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from backend.core.models import User

from .shemas import UserCreate


class DatabaseUser:

    @staticmethod
    async def validate_auth_jwt(
            username: str = Form(),
            password: str = Form(),
    ):
        unauthed_exc = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid username or password",
        )
        if not (user := DatabaseUser.get_user(username)):
            raise unauthed_exc

        if not auth_utils.validate_password(
                password=password,
                hashed_password=user.password,
        ):
            raise unauthed_exc

        if not user.active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="user inactive",
            )

        return user

    @staticmethod
    async def add_user(session: AsyncSession, user_in: UserCreate) -> User | None:
        user_in.password = utils.hash_password(user_in.password)
        print({**user_in.model_dump()})
        user = User(**user_in.model_dump())
        print(user.__dict__)
        session.add(user)
        await session.commit()
        return user

    @staticmethod
    async def get_user(session: AsyncSession, login: str, password: str):
        result = await session.execute(select(User).where(User.username == login))
        user = result.scalars().first()
        if user:
            if utils.hash_password(password) == password:
                return {'user': user.__dict__}
        else:
            raise HTTPException(status_code=401, detail='Unauthorized')

        # result: Result = await session.execute(statement)
        #
        # print(result.first()[0].__dict__)
