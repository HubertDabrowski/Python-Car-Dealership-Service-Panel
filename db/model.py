from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Model(Base):
    __tablename__ = "model"
    id_model = Column('id_model', Integer, primary_key = True)
    model = Column('model', String, nullable = False)

    def __init__(self, id_model, model):
        super().__init__()
        self.id_model = id_model
        self.model = model