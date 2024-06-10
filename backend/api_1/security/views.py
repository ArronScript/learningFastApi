from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext

from backend.api_1.security import User, UserCreate
from backend.api_1.security import create_jwt_token
from backend.core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession


from .crud import add_user


from backend.core.models import db_helper
security_router = APIRouter(prefix='/demo-auth', tags=['Demo Auth'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@security_router.post("/register")
async def register_user(username: str,
                        password: str,
                        email: str | None = None,
                        full_name: str | None = None,
                        disabled: bool | None = None,
                        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
                        ):
    user_in = UserCreate(username=username, password=password, hash_password='None',
                         email=email, full_name=full_name,disabled=disabled)

    user_in.hash_password = str(pwd_context.hash(password))
    await add_user(session, user_in)
    # Сохраните пользователя в базе данных

    return {"user": user_in.hash_password}


async def get_user(username):
    return User(username= "Nika",password= '123qwe123qwe', email='nika@mail.ru', )


@security_router.post("/token")
async def authenticate_user(username: str, password: str):
    user = get_user(username)  # Получите пользователя из базы данных
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    is_password_correct = pwd_context.verify(password, user.hash_password)

    if not is_password_correct:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    jwt_token = create_jwt_token({"sub": user.username})
    return {"access_token": jwt_token, "token_type": "bearer"}
