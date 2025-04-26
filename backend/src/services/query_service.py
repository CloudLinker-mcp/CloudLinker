"""Service for handling natural language to SQL queries.

This module provides a service that translates natural language questions into SQL
and executes them against the database.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi import HTTPException

from ..translator import translate
from ..utils.sql_sanitizer import is_safe_select
from ..utils.logger import get_logger

logger = get_logger(__name__)

class QueryService:
    """Service for handling natural language to SQL queries.
    
    This class provides methods for translating natural language questions into SQL
    and executing them against the database.
    """
    
    def __init__(self, session: AsyncSession):
        """Initialize the query service.
        
        Args:
            session: The database session to use for executing queries
        """
        self.session = session
    
    async def process_query(self, question: str, api_key: str) -> dict:
        """Process a natural language query.
        
        Args:
            question: The natural language question to process
            api_key: The API key used for the request (for logging)
            
        Returns:
            dict: A dictionary containing the SQL query and its result
            
        Raises:
            HTTPException: If the query is not a SELECT statement or is unsafe
        """
        # Translate the question to SQL
        sql = await translate(question)
        
        # If the SQL is a TODO, return it without executing
        if sql == "-- TODO":
            logger.info("query.translation.not_found", question=question, api_key_hash=hash(api_key))
            return {"sql": sql, "result": []}
        
        # If the SQL is BLOCKED, return it without executing
        if sql == "-- BLOCKED":
            logger.warning("query.translation.blocked", question=question, api_key_hash=hash(api_key))
            return {"sql": sql, "result": []}
        
        # Check if the SQL is safe
        if not is_safe_select(sql):
            logger.warning("query.sanitizer.unsafe", sql=sql, api_key_hash=hash(api_key))
            raise HTTPException(
                status_code=400,
                detail="Unsafe SQL query detected"
            )
        
        # Execute the query
        try:
            logger.info("query.execution.start", sql=sql, api_key_hash=hash(api_key))
            result = await self.session.execute(text(sql))
            rows = [dict(row) for row in result]
            logger.info("query.execution.success", row_count=len(rows), api_key_hash=hash(api_key))
            return {"sql": sql, "result": rows}
        except Exception as e:
            logger.error("query.execution.error", error=str(e), api_key_hash=hash(api_key))
            raise HTTPException(
                status_code=500,
                detail=f"Error executing query: {str(e)}"
            ) 