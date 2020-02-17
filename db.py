from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# autoincreasing_id = Column(Integer, primary_key=True)
# We're using a lambda function without arguments so that we can 
# create the table with an id column that is always the same!
# We need lambda functions, it wouldn't work otherwise
# That's because if we directly instatiate the variable, the program does not know
# for which table instantiate the Column. The function "freezes" the Column instantiation
# and thaws it for when the function is called upon. Very useful!
# TL;DR: when in difficulty using variables for following DRY principles, use 
# functions and anonymous (/lambda) functions!
autoincreasing_id = lambda: Column(Integer, primary_key=True)


class Room(Base):
    __tablename__='rooms'
    id = autoincreasing_id()
    # id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class OnScene(Base):
    __tablename__ = 'on_scene'
    id = autoincreasing_id()
    # id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    rooms = relationship(Room)

class Action(Base):
    __tablename__ = 'actions'
    # id = Column(Integer, primary_key=True)
    id = autoincreasing_id()

engine = create_engine('sqlite:///test.db')

Base.metadata.create_all(engine)

Base.metadata.bind = engine
