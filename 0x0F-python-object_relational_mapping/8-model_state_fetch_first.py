#!/usr/bin/python3
'''
prints the first State object from the database hbtn_0e_6_usa
'''
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    try:
        states = session.query(State).order_by(State.id).first()
        print('{}: {}'.format(states.id, states.name))
    except:
        print('Nothing')
