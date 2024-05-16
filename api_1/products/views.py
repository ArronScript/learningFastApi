from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from core.models import db_helper
from .shemas import Product, ProductCreate

product_router = APIRouter(tags=["Products"])


@product_router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_products(session=session)


@product_router.get("/{prod_id}/", response_model=Product)
async def get_products(prod_id: int, session: AsyncSession = Depends(db_helper.session_dependency)):
    prod = await crud.get_product(session=session, prod_id=prod_id)
    if prod is not None:
        return prod
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product_id {prod_id} is not found!"
    )


@product_router.post("/", response_model=Product)
async def create_product(product_in: ProductCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_product(session=session, product_in=product_in)
