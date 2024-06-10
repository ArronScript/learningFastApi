from fastapi import HTTPException, status, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from . import crud
from backend.core.models import db_helper
from .shemas import Product


async def get_product_by_id(prod_id: Annotated[int, Path],
                      session: AsyncSession = Depends(db_helper.scoped_session_dependency)) -> Product:
    prod = await crud.get_product(session=session, prod_id=prod_id)
    if prod is not None:
        return prod
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product_id {prod_id} is not found!"
    )
