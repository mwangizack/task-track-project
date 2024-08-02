from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Priority(Base):
    __tablename__ = 'priorities'
    
    id = Column(Integer, primary_key=True)
    priority = Column(String, nullable=False, unique=True)
    tasks = relationship('Task', back_populates='priority')

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    to_do = Column(String, nullable=False)
    priority_id = Column(Integer, ForeignKey('priorities.id'))
    priority = relationship('Priority', back_populates='tasks')

