from sqlalchemy import Column, Integer, String
from database import Base

# Define the database table name for this model
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(String(500), nullable=True)
