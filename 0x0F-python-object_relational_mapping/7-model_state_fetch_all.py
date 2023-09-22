#!/usr/bin/python3
"""Lists all State objects from db hbtn_0e_6_usa"""
from model_state import Base, State
import sys
import sqalchemy

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    # Session to interact w db
    Session = sessionmaker(bind=engine)
    session = Session()

    #query to retrieve all State objects = sqalchemy(not sql like over tasks)
    state_obj = session.query(State).order_by(State.id).all()

    for obj in state_obj:
        print("{}: {}".format(obj.id, obj.name))
