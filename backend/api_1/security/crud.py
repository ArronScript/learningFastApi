from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from backend.core.models import User


from .shemas import UserCreate



async def add_user(session: AsyncSession, user_in: UserCreate) -> User | None:
    print({**user_in.model_dump()})

    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user