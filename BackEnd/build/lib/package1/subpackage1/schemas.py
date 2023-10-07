from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from pydantic import BaseModel

class LocationBase(BaseModel):
    address: str
    availibility: bool
    price: float

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):
    id: int

    class Config:
        orm_mode = True