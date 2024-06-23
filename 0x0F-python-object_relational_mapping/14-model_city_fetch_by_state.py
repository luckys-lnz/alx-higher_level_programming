#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    
    # create a database URL connection
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    # create DB engine
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    # Call the session DBAPI
    Session = sessionmaker(bind=engine)
    session = Session()

# Query the database and print the results
    for state, city in session.query(State, City)\
                             .filter(State.id == City.state_id)\
                             .order_by(City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
