# from abc import ABC, abstractmethod, ABCMeta
#
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from backend.core.models.user import User
# from backend.core.models.product import Product
#
#
# class AbstractRepository(ABC):
#     @abstractmethod
#     async def add_one(self, session: AsyncSession, model_type: str):
#         raise NotImplementedError
#
#     @abstractmethod
#     async def find_all(self, session: AsyncSession, model_type: str):
#         raise NotImplementedError
#
#
# class SQLAlchemyRepository(AbstractRepository):
#     model = None
#     @abstractmethod
#     async def add_one(self, session: AsyncSession, model_type: str):
#         match model_type:
#             case 'Product':
#                 product = Product(**product_in.model_dump())
#
#         session.add(self.model)
#         await session.commit()
#         return product
#
#     @abstractmethod
#     async def find_all(self, session: AsyncSession, model_type: str):
#         raise NotImplementedError
#
#
