from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from ..schemas.customer import CustomerCreate, CustomerRead
from ..services.customer_service import CustomerService
from ..db import get_db

router = APIRouter()

@router.post("", response_model=CustomerRead, status_code=201)
async def create_customer(
    customer: CustomerCreate,
    db: AsyncSession = Depends(get_db)
) -> CustomerRead:
    """Create a new customer.
    
    Args:
        customer: Customer data to create
        db: Database session
        
    Returns:
        CustomerRead: Created customer data
    """
    service = CustomerService(db)
    return await service.create_customer(customer)

@router.get("", response_model=List[CustomerRead])
async def get_customers(
    db: AsyncSession = Depends(get_db)
) -> List[CustomerRead]:
    """Get all customers.
    
    Args:
        db: Database session
        
    Returns:
        List[CustomerRead]: List of all customers
    """
    service = CustomerService(db)
    return await service.get_customers()