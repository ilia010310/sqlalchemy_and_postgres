

from database import engine, session, Base
from models import  Genre


def create_tables():
    """Удаление и создание таблиц"""
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def inset_data():
    """Добавление данных"""
    with session() as s:
        misic = Genre(genre_name='Музыка')
        movie = Genre(genre_name='Фильмы')
        s.add_all([misic, movie])
        s.commit()
