from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from datetime import datetime
from typing import List

from database import SessionLocal
from models import BdPrototipe

app = FastAPI()

class RegistroRequest(BaseModel):
    num_house: float
    fec_start: datetime
    location_start: str
    location_end: str
    first_application: str
    second_application: str
    third_application: str
    fec_end: datetime

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/registro")
def guardar_registros(data: List[RegistroRequest], db: Session = Depends(get_db)):
    registros = [BdPrototipe(**item.dict()) for item in data]
    db.add_all(registros)
    db.commit()
    return {"status": "ok", "insertados": len(registros)}
