from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Color(Base):
    __tablename__ = "color"
    id_color = Column('id_color', Integer, primary_key = True)
    color = Column('color', String, nullable = False)

    def __init__(self, id_color, color):
        super().__init__()
        self.id_color = id_color
        self.color = color