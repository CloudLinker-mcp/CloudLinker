"""Router for handling natural language to SQL queries.

This module provides routes for translating natural language questions into SQL
and executing them against the database.
"""

from fastapi import APIRouter, Depends, Header
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_db
from ..services.query_service import QueryService

router = APIRouter()

class QueryRequest(BaseModel):
    """Request model for the query endpoint.
    
    Attributes:
        question: The natural language question to translate
    """
    question: str

class QueryResponse(BaseModel):
    """Response model for the query endpoint.
    
    Attributes:
        sql: The SQL query generated from the question
        result: The result of executing the SQL query
    """
    sql: str
    result: list

@router.post("", response_model=QueryResponse)
async def process_query(
    query: QueryRequest,
    x_api_key: str = Header(..., alias="X-API-Key"),
    db: AsyncSession = Depends(get_db)
) -> QueryResponse:
    """Process a natural language query.
    
    Args:
        query: The query request containing the natural language question
        x_api_key: The API key from request headers
        db: The database session
        
    Returns:
        QueryResponse: The response containing the SQL query and its result
    """
    service = QueryService(db)
    return await service.process_query(query.question, x_api_key) 