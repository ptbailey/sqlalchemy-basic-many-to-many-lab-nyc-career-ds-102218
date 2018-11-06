from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
#https://www.pythoncentral.io/sqlalchemy-association-tables/

Base = declarative_base()

# Write your classes below
class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key = True)
    character = Column(String)
    actors = relationship('Actor', secondary='actor_roles')

class Actor(Base):
    __tablename__ = 'actor'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    roles = relationship('Role', secondary='actor_roles')

class ActorRole(Base):
    __tablename__ = 'actor_roles'
    actor_id = Column(Integer, ForeignKey('actor.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'), primary_key=True)




engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
