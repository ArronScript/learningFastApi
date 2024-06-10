from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from backend.core.models import db_helper
from .shemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial
from .dependencies import get_product_by_id

product_router = APIRouter(tags=["Products"], prefix="/product")


@product_router.get("/", response_model=list[Product])
async def get_products(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_products(session=session)


@product_router.get("/{prod_id}/", response_model=Product)
async def get_products(product=Depends(get_product_by_id, )):
    return product


@product_router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(product_in: ProductCreate,
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.create_product(session=session, product_in=product_in)


@product_router.put("/{prod_id}/")
async def get_products(product_update: ProductUpdate, product=Depends(get_product_by_id),
                       session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update
    )


@product_router.patch("/{prod_id}/")
async def get_products_partial(product_update: ProductUpdatePartial, product: Product = Depends(get_product_by_id),
                               session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True
    )


@product_router.delete("/{prod_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product: Product = Depends(get_product_by_id),
                         session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    await crud.delete_product(product=product, session=session)
