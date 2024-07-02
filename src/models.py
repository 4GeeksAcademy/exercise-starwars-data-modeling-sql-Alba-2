import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

Favorite = Table(
    'favorite',
    Base.metadata,
    Column('planetas_id', Integer, ForeignKey('usuario.id')),
    Column('personajes_id', Integer, ForeignKey('usuario.id'))
)
class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(Integer, nullable=False)
    subscription_date = Column(Integer, nullable=False)


class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate  = Column(String(250), nullable=False)
 

    
class Personajes(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250),  nullable=False)
    eyes_color = Column(String(250), nullable=False)
    
   
   
class Planeta_Favorito(Base):
    __tablename__ = 'planetas_favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey("planetas.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("usuario.id"), primary_key=True)
    user=relationship(Usuario)
    planet=relationship(Planetas)

class Personaje_Favorito(Base):
    __tablename__ = 'personajes_favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey("personajes.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("usuario.id"), primary_key=True)
    user=relationship(Usuario)
    planet=relationship(Planetas)
 


def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
