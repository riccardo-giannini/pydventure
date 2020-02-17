# Very important lesson: never name a python module with a dash: 
# it generates invalid syntax (it is treated as a minus operator, I guess)
# Renaming my module from
# from sqlite-test import Person, Base, Address
# to
from sqlite_test import Person, Base, Address
# ^^^ I am importing the tables I defined in sqlite_test
from sqlalchemy import create_engine

# vvv this is how i instantiate the connection with DB
# where the DB is
engine = create_engine('sqlite:///dev/tests/sqlalchemy_example.db')

# bind it to ORM
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
# make a session (for DB transactions)
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

# ^^^ end of connection with DB

# these are displayed as objects instantiated at some memory cell, signed by a registry code
print(session.query(Person).all())

# to see the content of a row in a table, instead, use:
for x in session.query(Person).all():
    # this prints the actual name
    print(x.name)

# or:
# this actually works like a single query, so not good :D
print(session.query(Person).first())

# TODO: how to add a where condition?
# It's probably FILTER
print(session.query(Person).filter(Person.name == 'Mario').first().name)

# this one shows you the que you're actually making
print(session.query(Person).filter(Person.name == 'Mario'))