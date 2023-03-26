from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Brand(Base):
    __tablename__ = "brand"
    id_brand = Column('id_brand', Integer, primary_key = True)
    brand = Column('brand', String, nullable = False)

    def __init__(self, id_brand, brand):
        super().__init__()
        self.id_brand = id_brand
        self.brand = brand