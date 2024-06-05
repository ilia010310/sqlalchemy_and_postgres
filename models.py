import datetime
from typing import Annotated

from sqlalchemy import ForeignKey, MetaData, DateTime
from sqlalchemy.orm import mapped_column, Mapped

from database import Base

int_pk = Annotated[int, mapped_column(primary_key=True)]
metadata_obj = MetaData()

class Genre(Base):
    __tablename__ = 'genres'

    id: Mapped[int_pk]
    genre_name: Mapped[str]


class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[int_pk]
    author_name: Mapped[str]


class Book(Base):
    __tablename__ = 'books'

    book_id: Mapped[int_pk]
    name: Mapped[str]
    author_id: Mapped[int] = mapped_column(
        ForeignKey('authors.id', ondelete='CASCADE')
    )
    price: Mapped[int]
    quantity: Mapped[int]
    genre_id: Mapped[int] = mapped_column(
        ForeignKey('genres.id', ondelete='CASCADE')
    )


class City(Base):
    __tablename__ = 'cities'

    id: Mapped[int_pk]
    delivery_time: Mapped[int]


class Client(Base):
    __tablename__ = 'clients'

    id: Mapped[int_pk]
    client_name: Mapped[str]
    client_email: Mapped[str]
    city_id: Mapped[int] = mapped_column(
        ForeignKey('cities.id', ondelete='CASCADE')
    )


class Buy(Base):
    __tablename__ = 'buy'

    buy_id: Mapped[int_pk]
    buy_description: Mapped[str]
    client_id: Mapped[int] = mapped_column(
        ForeignKey('clients.id', ondelete='CASCADE')
    )


class BuyBook(Base):
    __tablename__ = 'buy_books'

    buy_book_id: Mapped[int_pk]
    buy_id: Mapped[int] = mapped_column(
        ForeignKey('buy.buy_id', ondelete='CASCADE')
    )
    book_id: Mapped[int] = mapped_column(
        ForeignKey('books.book_id', ondelete='CASCADE')
    )
    amount: Mapped[int]


class Step(Base):
    __tablename__ = 'steps'

    step_id: Mapped[int_pk]
    name_step: Mapped[str]


class BuyStep(Base):
    __tablename__ = 'buy_steps'

    buy_step_id: Mapped[int_pk]
    buy_id: Mapped[int] = mapped_column(
        ForeignKey('buy.buy_id', ondelete='CASCADE')
    )
    step_id: Mapped[int] = mapped_column(
        ForeignKey('steps.step_id', ondelete='CASCADE')
    )
    date_step_beg: Mapped[datetime] = mapped_column(DateTime)
    date_step_end: Mapped[datetime] = mapped_column(DateTime)