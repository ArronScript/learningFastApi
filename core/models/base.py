from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.orm import Mapped


class Base(DeclarativeBase):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)