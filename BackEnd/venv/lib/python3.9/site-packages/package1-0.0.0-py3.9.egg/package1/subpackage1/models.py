from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from sqlalchemy import Boolean, Column, Integer, String, Float

from .database import Base


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, unique=True, index=True)
    availability = Column(Boolean, deafult=True)
    price = Column(Float)


