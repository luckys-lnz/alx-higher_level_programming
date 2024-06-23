#!/usr/bin/python3
"""
script that creates the State “California” with
the City “San Francisco” from the database `hbtn_0e_100_usa`
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    db_url = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                            .format(argv[1], argv[2], argv[3]))

    # create DB using metadata
    Base.metadata.create_all(db_url)

    # session DBAPI
    Session = sessionmaker(bind=db_url)
    session = Session()

    # create a state
    new_state = State(name='California')

    # create city
    new_city = City(name='San Francisco', state=new_state)

    # use session to generate new state
    session.add(new_state)

    # commit session
    session.commit()

    #close session connection
    session.close()
