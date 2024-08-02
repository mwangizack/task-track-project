from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Priority

engine = create_engine('sqlite:///tasktrack.db', connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()

priorities = ['Low', 'Medium', 'High']
for name in priorities:
    priority = Priority(level=name)
    session.add(priority)

session.commit()
session.close()

