from fastapi import APIRouter
from typing import List
from src.models.customer import CustomerCreate, CustomerRead

router = APIRouter()

# Temporary in-memory storage for demo purposes
customers = []
next_id = 1

# Endpoint to create a customer
@router.post("/customers", response_model=CustomerRead)
def create_customer(customer: CustomerCreate):
    global next_id
    customer_data = {"id": next_id, **customer.dict()}
    customers.append(customer_data)
    next_id += 1
    return customer_data

# Endpoint to get a list of customers
@router.get("/customers", response_model=List[CustomerRead])
def get_customers():
    return customers