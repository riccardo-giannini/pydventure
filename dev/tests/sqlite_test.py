# this is just an sqlite3 test, so that i can try to connect to an existing
# DB and try to do some sandboxing and build something that instantiates a DB and do
# stuff.

# on a second thought, it's probably more efficient if i just wrap around an ORM
# (object relationship manager) so that I don't have to deal with a lot of complicated
# instantiation stuff
# I think I will use sqlalchemy

# Trying this one:
# https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Person(Base):
    __tablename__= 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

# How the path works:
# sqlite:// -> base. I guess it indicates that we are using sqlite.
# https://docs.sqlalchemy.org/en/13/core/engines.html <-- Here are different kind of db engine you can use.
engine = create_engine('sqlite:///dev/tests/sqlalchemy_example.db')

Base.metadata.create_all(engine)

Base.metadata.bind = engine

from sqlalchemy.orm import sessionmaker

DBSession = sessionmaker(bind=engine)
session = DBSession()

new_person = Person(name = 'new person')
session.add(new_person)
session.commit()

new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()

mario = Person(name = 'Mario')
session.add(mario)
#session.commit()
session.rollback()

# not really sure right now on how to use commit() e rollback(), but it doesn't matter at this point

# Idea: administrate DB with alchemy. Create tables, create the first objects inside the rooms.

# How to print data from DB?