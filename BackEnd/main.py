from pathlib import Path
print('Running' if __name__ == '__main__' else 'Importing', Path(__file__).resolve())

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from package1 import crud
from package1.subpackage1 import schemas
from package1.subpackage1 import models

from package1.subpackage1.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "PUT"],
    allow_headers=["GET", "POST", "PATCH", "PUT"],
    max_age=3600,
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/locations/", response_model=schemas.Location)
def create_location(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    return crud.create_location(db=db, location=location)


@app.get("/locations/", response_model=list[schemas.Location])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations

@app.patch("/locations/{location_id}", response_model=schemas.Location)
def update_location(location_id: int, location: schemas.LocationUpdate, db: Session = Depends(get_db)):
        db_location = crud.get_location(db, location_id=location_id)    
        location_data = location.model_dump(exclude_unset=True)
        for key, value in location_data.items():
            setattr(db_location, key, value)
        db.add(db_location)
        db.commit()
        db.refresh(db_location)
        return db_location
