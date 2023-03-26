import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

Base = declarative_base()


class Session:
    def __init__(self):
        super().__init__()
        self.url = 'mysql+pymysql://root:hubert@localhost:3303/project_car_dealer'
        self.engine = create_engine('mysql+pymysql://root:hubert@localhost:3303/project_car_dealer')
        self.session = sessionmaker(self.engine)

    def connect(self):
        Base.metadata.create_all(bind=self.engine)

    def save(self, instance): #(siebie, obiekt)
        self.connect()
        session = self.session()
        session.add(instance)
        session.commit()
        session.close()

    def remove(self, instance, _id): #(siebie, klasa, szukane_id)
        self.connect()
        session = self.session()
        record = session.query(instance).filter_by(id=_id).delete()
        #session.delete(record)
        session.commit()
        session.close()

    def select(self, instance, _id):
        self.connect()
        session = self.session()
        record = session.query(instance).filter_by(id=_id).one()
        result = self.take_attributes(record)
        session.commit()
        session.close()
        return record

    def take_all(self, instance):
        result = []
        self.connect()
        session = self.session()
        records = session.query(instance).all()
        for record in records:
            result += [self.take_attributes(record)]
        session.commit()
        session.close()
        return records

    def take_highest_id(self, instance):
        result = []
        self.connect()
        session = self.session()
        records = session.query(instance).all()
        id=0
        for record in records:
            if record.id >0:
                id = record.id
        session.commit()
        session.close()
        return id

    def take_attributes(self, obj):
        result = []
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and x != 'registry']:
            fields[field] = obj.__getattribute__(field)

        return fields

    def modify(self, column, _id, old_value, new_value):
        engine = db.create_engine("mysql+pymysql://root:hubert@localhost:3303/project_car_dealer", echo=False)
        connection = engine.connect()
        metadata = db.MetaData()

        cars = db.Table('car', metadata, autoload_with=engine)

        if column == "color":
            car_data = cars.update().where(cars.c.id == _id).values(color=new_value)
        elif column == "brand":
            car_data = cars.update().where(cars.c.id == _id).values(brand=new_value)
        elif column == "engineandfuel":
            car_data = cars.update().where(cars.c.id == _id).values(engine_type=new_value)
        elif column == "model":
            car_data = cars.update().where(cars.c.id == _id).values(model=new_value)
        elif column == "price":
            car_data = cars.update().where(cars.c.id == _id).values(price=new_value)
        else:
            print("error")

        connection.execute(car_data)

    def join_car(self, _car, _brand, _model, _engine, _color): #, _model, _engineandfuel, _color):
        self.connect()
        session = self.session()

        records = session.query(_car, _brand, _model, _engine, _color).filter(_car.brand == _brand.id_brand).filter(_car.model==_model.id_model).filter(_car.engine_type==_engine.id_engine).filter(_car.color==_color.id_color).order_by(_car.id).all()  #.filter(_car.brand==_brand.id_brand).all() #_car.color==_color.id_color  and _car.engine_type==_engineandfuel.id_engine and _car.model==_model.id_model and _car.brand==_brand.id_brand)

        return records

    def join_client(self, _client): #, _model, _engineandfuel, _color):
        self.connect()
        session = self.session()

        records = session.query(_client).all()
        return records

    def take(self, _car, _id): #, _model, _engineandfuel, _color):
        self.connect()
        session = self.session()
        records = session.query(_car).filter_by(id=_id).one()
        taken_brand = records.brand
        return taken_brand

    def take_old_value(self, _car, _id,column): #, _model, _engineandfuel, _color):
        self.connect()
        session = self.session()
        records = session.query(_car).filter_by(id=_id).one()

        if column=='color':
            old_value = records.color
        elif column=='brand':
            old_value = records.brand
        elif column=='model':
            old_value = records.model
        elif column=='engineandfuel':
            old_value = records.engine_type
        elif column=='price':
            old_value = int(records.price)

        return old_value