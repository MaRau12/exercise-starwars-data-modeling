import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

favorites = Table("favorites", Base.metadata,
    Column('User', String, ForeignKey('user.id'), primary_key=True),
    Column('Films', String, ForeignKey('films.id'), primary_key=True),
    Column('People', String, ForeignKey('people.id'), primary_key=True),
    Column('Planets', String, ForeignKey('planets.id'), primary_key=True),
    Column('Vehicles', String, ForeignKey('vehicles.id'), primary_key=True)
)

class User(Base):
   __tablename__ = 'user'
   id = Column(Integer, primary_key=True) 
   name = Column(String(50), nullable=False)
   last_name = Column(String(50), nullable=False)
   email = Column(String(50), nullable=False)
   password = Column(String(50), nullable=False)
   is_active = Column(Boolean(), unique=False, nullable=False)
   fav_films = relationship("Films", secondary=favorites, backref="User")
   fav_characters = relationship("People", secondary=favorites, backref="User")
   fav_planets = relationship("Planets", secondary=favorites, backref="User")
   fav_vehicles = relationship("Vehicles", secondary=favorites, backref="User")
class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    
class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)

class Planets(Base):
    __tablename__= "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
      

class Vehicles(Base):
    __tablename__="vehicles"  
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
   



  ##  def to_dict(self):
      ##  return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
