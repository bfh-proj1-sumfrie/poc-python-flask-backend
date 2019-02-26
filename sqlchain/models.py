from sqlalchemy import Column, Integer, String
from sqlchain.database import Base


class User(Base):
    __tablename__ = 'user_details'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(String(10))
    status = Column(Integer)
    password = Column(String(20))

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User(id=%d, username='%s', password='%s')>" % (self.id, self.username, self.password)

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'status': self.status,
            'gender': self.gender,
        }
