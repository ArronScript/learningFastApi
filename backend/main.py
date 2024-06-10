from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from backend.core.config import settings
from backend.api_1 import router_api_1


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield


app = FastAPI(lifespan=lifespan, )
app.include_router(router=router_api_1, prefix=settings.prefix_api_v1)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
