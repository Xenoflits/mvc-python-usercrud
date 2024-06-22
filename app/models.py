from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

#modellen
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    accesslevel = Column(Integer)

#database initializeren
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all('engine')
Session = sessionmaker(bind=engine)
session = Session()

#operaties
def create_user(name,email,password):
    new_user = User(name=name, email=email, password=password, accesslevel=1)
    session.add(new_user)
    session.commit()

def get_users():
    return session.query(User).all()

def update_user(user_id, name, email, password):
    user = session.query(User).filter(User.id == user_id).first()
    user.name = name
    user.email = email
    user.password = password
    session.commit()

def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    session.delete(user)
    session.commit
