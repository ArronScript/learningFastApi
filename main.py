from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.config import settings
from core.models import Base, db_helper
from api_1 import router_api_1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan, )
app.include_router(router=router_api_1, prefix=settings.prefix_api_v1)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
