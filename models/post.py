from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))