#!/usr/bin/python3
"""
This script lists all State objects from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Construct the database URL
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3])

    # Create an SQLAlchemy engine
    engine = create_engine(db_url)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print State objects sorted by id
    for instance in session.query(State).order_by(State.id):
        print('{}: {}'.format(instance.id, instance.name))

