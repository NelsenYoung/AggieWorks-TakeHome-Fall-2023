from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from sqlalchemy.orm import Session

from package1.subpackage1 import models, schemas

def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()

def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()

def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(id=location.id,
                                  address=location.address, 
                                  availability=location.availability, 
                                  price=location.price)
    
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location