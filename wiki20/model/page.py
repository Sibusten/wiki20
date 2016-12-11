from sqlalchemy import Column
from sqlalchemy.types import Integer, Text

from wiki20.model import DeclarativeBase


class Page(DeclarativeBase):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True)
    pagename = Column(Text, unique=True)
    data = Column(Text)
