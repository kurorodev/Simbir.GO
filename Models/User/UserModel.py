from sqlalchemy import Column, Integer, String, Boolean, Double
from DataBase.DataBase import Base
from sqlalchemy.orm import relationship
from flask_jwt_extended import create_access_token
from datetime import timedelta
from passlib.hash import bcrypt

class AccountModel(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(String(100))
    """transports = relationship('AccountModel', backref='rent_table', lazy=True)"""
    """rent = relationship('AccountModel', backref='transport_table', lazy=True)"""

    def __init__(self,**kwargs):
        self.name = kwargs.get('name')
        self.password = kwargs.get('password')

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id,
            expires_delta=expire_delta
        )
        return token

    @classmethod
    def authenticate(cls, name, password):
        user = cls.query.filter(cls.name == name).one()
        #if not bcrypt.verify(password, user.password):
            #raise Exception('No user with this password')
        return user

class RentModel(Base):
    __tablename__ = 'rent_table'
    id = Column(Integer, primary_key=True)
    lat = Column(Double)
    long = Column(Double)
    radius = Column(Double)
    type = Column(String())


class TransportModel(Base):
    __tablename__ = 'transport_table'
    id = Column(Integer, primary_key=True)
    canBeRented = Column(Boolean)
    transportType = Column(String())
    model = Column(String())
    color = Column(String())
    identifier = Column(String())
    description = Column(String())
    latitude = Column(Double)
    longitude = Column(Double)
    minutePrice = Column(Double)
    dayPrice = Column(Double)


