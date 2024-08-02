from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Priority

engine = create_engine('sqlite:///../tasktrack.db')
Session = sessionmaker(bind=engine)
session = Session()

priorities = ['Low', 'Medium', 'High']
for name in priorities:
    priority = Priority(name=name)
    session.add(priority)

session.commit()
session.close()

