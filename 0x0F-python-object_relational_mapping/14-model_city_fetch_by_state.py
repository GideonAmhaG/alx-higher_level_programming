#!/usr/bin/python3
"""module for a script that that prints the first State object from the
database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City, State).join(State)
    for city, state in rows.all():
        print("{}: ({:d}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
