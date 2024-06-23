#!/usr/bin/python3
"""
script that prints the first State object from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # construct the Database URL
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1],
                                                    argv[2], argv[3])

    # create sqlalchemy engine 
    engine = create_engine(db_url)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # get the first state
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # close session
    session.close()

