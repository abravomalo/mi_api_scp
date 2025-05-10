from sqlalchemy import Column, Integer, Float, String, TIMESTAMP
from database import Base

class BdPrototipe(Base):
    __tablename__ = "bd_prototipe"

    id = Column(Integer, primary_key=True, index=True)
    num_house = Column(Float)
    fec_start = Column(TIMESTAMP)
    location_start = Column(String)
    location_end = Column(String)
    first_application = Column(String)
    second_application = Column(String)
    third_application = Column(String)
    fec_end = Column(TIMESTAMP)
