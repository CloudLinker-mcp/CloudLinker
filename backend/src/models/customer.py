from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base class for SQLAlchemy models."""
    pass

class Customer(Base):
    """SQLAlchemy model for the customers table.
    
    Attributes:
        id: Primary key
        name: Customer's full name
        email: Unique email address
        created_at: Timestamp of record creation
        updated_at: Timestamp of last update
    """
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)