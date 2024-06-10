from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from backend.core.models import Product
from .shemas import ProductCreate, ProductUpdate, ProductUpdatePartial


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


async def update_product(session: AsyncSession, product: Product,
                         product_update: ProductUpdate | ProductUpdatePartial, partial: bool = False) -> Product | None:
    for key, value in product_update.model_dump(exclude_unset=partial).items():
        setattr(product, key, value)
    await session.commit()
    return product


async def delete_product(session: AsyncSession, product: Product, ) -> None:
    await session.delete(product)
    await session.commit()
