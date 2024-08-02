import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Task, Priority

engine = create_engine('sqlite:///tasktrack.db')
Session = sessionmaker(bind=engine)

def add_task(to_do, priority_name):
    session = Session()
    priority = session.query(Priority).filter_by(level=priority_name).first()
    if not priority:
        raise ValueError('Invalid priority name. Use High, Medium or Low.')
    task = Task(to_do=to_do, priority=priority)
    session.add(task)
    session.commit()
    session.close()

def view_tasks():
    session = Session()
    tasks = session.query(Task).all()
    for task in tasks:
        print(f'{task.id}: {task.to_do} ({task.priority.level} Priority)')
    session.close()

def edit_task(task_id, to_do=None, priority_name=None):
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if not task:
        raise ValueError('Task not found')
    if to_do:
        task.to_do = to_do
    if priority_name:
        priority = session.query(Priority).filter_by(level=priority_name).first()
        if not priority:
            raise ValueError('Invalid priority name')
        task.priority = priority
    session.commit()
    session.close()

def delete_task():
    session = Session()
    task = session.query(Task).filter_by(id=task_id).first()
    if not task:
        raise ValueError('Task not found')
    session.delete(task)
    session.commit()
    session.close()


