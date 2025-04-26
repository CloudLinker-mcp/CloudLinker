from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from ..models.customer import Customer
from ..schemas.customer import CustomerCreate

class CustomerService:
    """Service layer for customer operations.
    
    This class handles all database operations for customers,
    providing a clean interface for the router layer.
    """
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_customer(self, customer: CustomerCreate) -> Customer:
        """Create a new customer.
        
        Args:
            customer: Customer data to create
            
        Returns:
            Customer: Created customer instance
            
        Raises:
            HTTPException: If email already exists
        """
        db_customer = Customer(
            name=customer.name,
            email=customer.email,
        )
        
        try:
            self.session.add(db_customer)
            await self.session.commit()
            await self.session.refresh(db_customer)
            return db_customer
        except IntegrityError:
            await self.session.rollback()
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )
    
    async def get_customers(self) -> list[Customer]:
        """Get all customers.
        
        Returns:
            list[Customer]: List of all customers
        """
        result = await self.session.execute(select(Customer))
        return result.scalars().all() 