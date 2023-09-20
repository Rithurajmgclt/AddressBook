
from fastapi import APIRouter
router = APIRouter()

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud  
from database import get_db  
from schema import AddressBase,AddressUpdate,AddressPost,AddressOut
from  models import Address
from fastapi import HTTPException
from fastapi.logger import logger 
from typing import List
from fastapi import Query

@router.post("/", response_model=None)
def create_address(
    address: AddressPost,
    db: Session = Depends(get_db)
   

):  
    try:
        address_dict ={
                'name':address.name,
                'email':address.email.email,
                'home':address.home,
                'street':address.street,
                'latitude':address.latitude,
                'longitude':address.longitude,
                

        }
        created_address = crud.create_address(db, address_dict)
        return created_address
    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=500, detail=error_message)
    
@router.put("/{address_id}", response_model=None)
def update_address(
    address_id: int,
    updated_address: AddressUpdate,
    db: Session = Depends(get_db)
):
    try:
        address = crud.get_address(db, address_id)
        if not address:
            raise HTTPException(status_code=404, detail="Address not found")
        updated_address_dict = updated_address.dict(exclude_unset=True)
        address = crud.update_address(db, address, updated_address_dict)
        return address
    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=500, detail=error_message)
@router.delete("/{address_id}", response_model=AddressOut)
def delete_address(
    address_id: int,
    db: Session = Depends(get_db)
):
    address = crud.get_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    crud.delete_address(db, address)
    return address
@router.get("/", response_model=List[AddressOut])
def get_address(db: Session = Depends(get_db)):
    addresses = crud.get_all_addresses(db)
    if not addresses:
        raise HTTPException(status_code=404, detail="Addresses not found")
    return addresses

@router.get("/address/from/cordinates", response_model=List[AddressOut])
def get_address_on_lat_and_long(
    min_latitude: float = Query(..., description="Latitude of the target min_location"),
    max_latitude: float = Query(..., description="Latitude of the target max_location"),
    min_longitude: float = Query(..., description="Longitude of the target min_location"),
    max_longitude: float = Query(..., description="Longitude of the target max_location"),
    db: Session = Depends(get_db)):
    
    addresses = crud.get_all_addresses_from_lat_long(db,min_latitude,max_latitude,min_longitude,max_longitude)


    if not addresses:
        raise HTTPException(status_code=404, detail="Addresses not found")
    return addresses
@router.get("/{address_id}", response_model=AddressOut)
def get_address(
    address_id: int,
    db: Session = Depends(get_db)

):
    address = crud.get_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

