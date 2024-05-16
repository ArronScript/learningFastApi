from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper
from .shemas import Product, ProductCreate

product_router = APIRouter(tags=["Products"])


@product_router.get("/")
async def get_products(
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_products(session=session)
