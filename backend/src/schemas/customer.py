from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional

class CustomerBase(BaseModel):
    """Base Pydantic model for customer data.
    
    Attributes:
        name: Customer's full name
        email: Unique email address
    """
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr

class CustomerCreate(CustomerBase):
    """Schema for creating a new customer."""
    pass

class CustomerRead(CustomerBase):
    """Schema for reading customer data.
    
    Attributes:
        id: Primary key
        created_at: Timestamp of record creation
        updated_at: Timestamp of last update
    """
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True) 