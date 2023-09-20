from sqlalchemy.orm import Session
from models import Address

# Create a new address
def create_address(db: Session, address_data: dict):

   
    address = Address(**address_data)
    db.add(address)
    db.commit()
    db.refresh(address)
    return address

# Retrieve a single address by ID
def get_address(db: Session, address_id: int):
    return db.query(Address).filter(Address.id == address_id).first()

# Retrieve a list of all addresses
def get_all_addresses(db: Session):
    return db.query(Address).all()

# Update an existing address
def update_address(db: Session, address: Address, updated_data: dict):
   

    for key, value in updated_data.items():
        if key == 'email':
            value = value['email']
            
        setattr(address, key, value)
    address.__dict__  
    db.commit()
    db.refresh(address)
    return address

# Delete an address
def delete_address(db: Session, address: Address):
    db.delete(address)
    db.commit()
#input lat and long
def get_all_addresses_from_lat_long(db: Session,min_latitude,max_latitude,min_longitude,max_longitude):
    return db.query(Address).filter(Address.latitude.between(min_latitude, max_latitude)).filter(Address.longitude.between(min_longitude, max_longitude)).all()


