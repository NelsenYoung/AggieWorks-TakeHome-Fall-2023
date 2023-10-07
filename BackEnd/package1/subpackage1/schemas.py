from pathlib import Path
from typing import Optional
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from pydantic import BaseModel

class LocationBase(BaseModel):
    id: int
    address: str
    availability: bool
    price: float

class LocationCreate(LocationBase):
    pass

class Location(LocationBase):

    class Config:
        orm_mode = True

class LocationUpdate(BaseModel):
    address: Optional[str] = None
    availability: Optional[bool] = True
    price: Optional[float] = None