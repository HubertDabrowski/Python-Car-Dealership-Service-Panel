from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

class Car(Base):
    __tablename__ = "car"
    id = Column('id', Integer, primary_key = True)
    color = Column('color', Integer)
    brand = Column('brand', Integer)
    model = Column('model', Integer)
    price = Column('price', Integer)
    engine_type = Column('engine_type', Integer)

    def __init__(self, id_car, color, brand, model, price, engine_type):
        super().__init__()
        self.id = id_car
        self.color = color
        self.brand = brand
        self.model = model
        self.price = price
        self.engine_type = engine_type