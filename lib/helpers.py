from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Task, Priority

engine = create_engine('sqlite:///todo_app.db')
Session = sessionmaker(bind=engine)

def add_task(to_do, priority_name):
    session = Session()
    priority = session.query(Priority).filter_by(name=priority_name).first()
    if not priority:
        raise ValueError('Invalid priority name. Use High, Medium or Low.')
    task = Task(to_do=title, priority=priority)
    session.add(task)
    session.commit()
    session.close()

