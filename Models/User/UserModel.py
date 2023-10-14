from sqlalchemy import Column, Integer, String, Boolean, Double
from DataBase.DataBase import Base

class AccountModel(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    password = Column(Integer)


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


