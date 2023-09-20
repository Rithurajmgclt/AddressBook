
from pydantic import BaseModel, Field,EmailStr,validator
from typing import Optional
import crud
from fastapi import Depends
from sqlalchemy.orm import Session
from models import Address

from sqlalchemy.orm import sessionmaker
from database import engine
Session = sessionmaker(bind=engine)
session=Session()


class EmailModel(BaseModel):
    email: EmailStr
    @validator("email")
    def validate_email_unique(cls, email: str,values):
        current_email = values.get('current_email')
        # Check if the email is unique in the database
        if session.query(Address).filter(Address.email == email).filter(Address.email != current_email).first():

            raise ValueError("Email address already exists")
        return email
class AddressBase(BaseModel):
    id: int
    name: str
    email: EmailModel
    home: str
    street: str
    latitude: str
    longitude: str
class AddressPost(BaseModel):
   
    name: str
    email: EmailModel
    home: str
    street: str
    latitude: float
    longitude: float

class AddressUpdate(BaseModel):
    name: Optional[str] = Field(default=None)
    email: EmailModel = Field(default=None)
    home: Optional[str] = Field(default=None)
    street: Optional[str] = Field(default=None)
    latitude: Optional[str] = Field(default=None)
    longitude: Optional[str] = Field(default=None)
class Coordinates(BaseModel):
    min_latitude: float
    min_longitude: float
    max_latitude: float
    max_longitude: float

class AddressOut(BaseModel):
    id: int
    name: str
    email: str
    home: str
    street: str
    latitude: float
    longitude: float
