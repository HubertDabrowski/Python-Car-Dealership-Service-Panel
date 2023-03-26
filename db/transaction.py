from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transaction"
    id_transaction = Column('id_transaction', Integer, primary_key = True)
    client_id = Column('client_id', Integer)
    car = Column('car', Integer)
    transaction_date = Column('transaction_date', DateTime)

    def __init__(self, id_transaction, client_id, car, transaction_date):
        super().__init__()
        self.id_transaction = id_transaction
        self.client_id = client_id
        self.car = car
        self.transaction_date = transaction_date