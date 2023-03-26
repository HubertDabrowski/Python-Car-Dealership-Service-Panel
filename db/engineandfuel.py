from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class EngineAndFuel(Base):
    __tablename__ = "engineandfuel"
    id_engine = Column('id_engine', Integer, primary_key=True)
    designation = Column('designation', Float, nullable=False)
    fuel = Column('fuel', String, nullable=False)

    def __init__(self, id_engine, designation, fuel):
        super().__init__()
        self.id_engine = id_engine
        self.designation = designation
        self.fuel = fuel
