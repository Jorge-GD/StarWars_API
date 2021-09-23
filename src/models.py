import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    firstname = Column(String(10), nullable=False)
    lastname = Column(String(10), nullable=False)
    email = Column(String(10), nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    favorite_set = relationship("Favorite", back_populates="parent", uselist=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    planetid = Column(String)
    peopleid = Column(String)
    spaceshipid = Column(String)
    userid = Column(String, ForeignKey("User.id"))
    user_set = relationship("User")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    rotation_period = Column(String, nullable=False)
    orbital_period = Column(String, nullable=False)
    diameter = Column  (String, nullable=False)
    climate = Column (String, nullable=False)
    gravity = Column (String, nullable=False)
    terrain = Column (String, nullable=False)
    surface_water = Column (String, nullable=False)
    population = Column (String, nullable=False)
    residents = Column (String, nullable=False)
    url = Column (String, nullable=False)
    favorites_id = Column(Integer, ForeignKey("favorite.id"))
    favorite = relationship(Favorite)
    
class Starship (Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model  = Column(String, nullable=False)
    manufacturer  = Column(String, nullable=False)
    cost_in_credits  = Column(String, nullable=False)
    length  = Column(String, nullable=False)
    max_atmosphering_speed  = Column(String, nullable=False)
    crew   = Column(String, nullable=False)
    passengers  = Column(String, nullable=False)
    cargo_capacity  = Column(String, nullable=False)
    consumables = Column(String, nullable=False)
    hyperdrive_rating  = Column(String, nullable=False)
    MGLT  = Column(String, nullable=False)
    starship_class  = Column(String, nullable=False)
    pilots  = Column(String, nullable=False)
    url  = Column(String, nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    favorite = relationship(Favorite)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    height  = Column(String, nullable=False)
    mass  = Column(String, nullable=False)
    hair_color  = Column(String, nullable=False)
    skin_color  = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year  = Column(String, nullable=False)
    gender  = Column(String, nullable=False)
    homeworld  = Column(String, nullable=False)
    species  = Column(String, nullable=False)
    vehicles  = Column(String, nullable=False)
    starships = Column(String, nullable=False)
    url  = Column(String, nullable=False)
    favorite_id = Column(Integer, ForeignKey("favorite.id"))
    favorite = relationship(Favorite)


def to_dict(self):
    return {}


render_er(Base, 'diagram.png')