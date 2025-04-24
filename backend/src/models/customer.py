from pydantic import BaseModel

# Model for creating a new customer
class CustomerCreate(BaseModel):
    name: str
    email: str
    phone: str

# Model for reading customer information
class CustomerRead(BaseModel):
    id: int
    name: str
    email: str
    phone: str

    class Config:
        from_attributes = True