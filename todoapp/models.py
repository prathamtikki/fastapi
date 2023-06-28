from database import Base 
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey


class Users(Base):
    __tablename__='users'

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,primary_key=True)
    username=Column(String,unique=True)
    first_name=Column(String)
    last_name=Column(String)
    hashed_password=Column(Boolean,default=True)
    is_active=Column(String)
    role=Column(String)

class Todos(Base):
    __tablename__ = 'todos'
    id = Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    priority=Column(Integer)
    complete=Column(Boolean,default=False)
    owner_id=Column(Integer,ForeignKey("user.id"))
