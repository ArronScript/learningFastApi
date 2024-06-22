from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext

from backend.api_1.security import UserCreate
from backend.core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

from .crud import DatabaseUser

from backend.core.models import db_helper

from backend.core.models import User

security_router = APIRouter(prefix='/demo-auth', tags=['Demo Auth'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@security_router.post("/register")
async def register_user(username: str,
                        password: str,
                        email: str | None = None,
                        full_name: str | None = None,
                        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
                        ):
    user_in = UserCreate(username=username, password=password,
                         email=email, full_name=full_name)
    print(user_in.__dict__)
    await DatabaseUser.add_user(session, user_in)
    return {"user": user_in.password}


@security_router.post("/token")
async def authenticate_user(username: str, password: str,
                            session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    user = await DatabaseUser.get_user(session=session, login=username, password=password)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {'username' : username,
            'password': password}
    # if not is_password_correct:
    #     raise HTTPException(status_code=400, detail="Incorrect username or password")
    #
    # jwt_token = create_jwt_token({"sub": user.password})
    # return {"access_token": jwt_token, "token_type": "bearer"}
