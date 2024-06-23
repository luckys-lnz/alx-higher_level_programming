#!/usr/bin/python3
"""
This script prints the State object with the name
passed as an argument from the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """prints state object with name passed as argument"""

    # construct the database url
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    # sqlalchemy engine
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    state_name_to_search = argv[4]
    state = session.query(State).filter_by(name=state_name_to_search).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()

