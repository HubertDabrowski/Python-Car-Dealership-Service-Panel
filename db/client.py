from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Client(Base):
    __tablename__ = "client"
    id_client = Column('id_client', Integer, primary_key = True)
    client_name = Column('client_name', String, nullable = False)
    surname = Column('surname', String, nullable = False)
    address = Column('address', String, nullable = False)

    def __init__(self, id_client, client_name, surname, address):
        super().__init__()
        self.id_client = id_client
        self.client_name = client_name
        self.surname = surname
        self.address = address