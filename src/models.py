import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()





  

class Films(Base):
    __tablename__ = 'films'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)

class Locations(Base):
   __tablename__ = "locations"
   film_id = Column(Integer, ForeignKey(films.id))
   planet_id = Column(Integer, ForeignKey(planets.id))


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    shown_in_films = relationship(Films, secondary=film_characters, backref="characters")
    homeworld = relationship(Planets)
    homeworld_id = Column(String(250), ForeignKey("planet.id"))
    height = Column(Integer, nullable=False)

 
class Film_characters(Base):
    __tablename__="film_characters"
    film_id = Column(Integer, ForeignKey(people.id))
    character_id = Column(Integer, ForeignKey(people.id)) 


class Planets(Base):
    __tablename__= "planets"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    seen_in_films = relationship(Films, secondary=locations, backref="plantets")

class Vehicles_in_films(Base):
    __tablename__= "vehicles_in_films"
    film_id = Column(Integer, ForeignKey(vehcles.id))
    vehicle_id = column(Integer, ForeignKey(films.id))      

class Vehicles(Base):
    __tablename__="vehicles"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    seen_in_films = relationship(Films, secondary=vehicles_in_films, backref="vehicles")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


##   post_code = Column(String(250), nullable=False)
  ##  person_id = Column(Integer, ForeignKey('person.id'))
   ## person = relationship(Person) 