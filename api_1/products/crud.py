from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Product
from .shemas import ProductCreate


async def get_products(session: AsyncSession) -> list[Product]:
    statement = select(Product).order_by(Product.id)
    result: Result = await session.execute(statement)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, prod_id: int) -> Product | None:
    return await session.get(Product, prod_id)


async def create_product(session: AsyncSession, product_in: ProductCreate) -> Product | None:
    product = Product(**product_in.model_dump())
    session.add(product)
    await session.commit()
    return product
