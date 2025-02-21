from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime

Base = declarative_base()

class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    birth = Column(DateTime)
    created = Column(DateTime, default=datetime.utcnow)


users = [
    UserModel(firstname='Bob', birth=datetime(1993, 3, 14)),
    UserModel(firstname='Jane', birth=datetime(2005, 2, 5)),

]

session_maker = sessionmaker(bind=create_engine('sqlite:///models.db'))

def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

create_users()