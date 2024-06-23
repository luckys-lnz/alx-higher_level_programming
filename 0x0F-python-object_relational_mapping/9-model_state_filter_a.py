#!/usr/bin/python3
"""
script that lists all State objects that contain the
letter a from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """list stats that has the letter a"""

    # connect to sqlachemy
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1],
            argv[2], argv[3])

    # create sqlalchemy engine
    engine = create_engine(db_url)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # script to search states that contains `a`
    for instance in session.query(State).filter(State.name.contains('a')).order_by(State.id):
        print(f"{instance.id}: {instance.name}")
