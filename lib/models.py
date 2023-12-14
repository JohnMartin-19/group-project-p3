from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///many_to_many.db')

Base = declarative_base()
user = Table(
    'users',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    
    extend_existing=True,
)

