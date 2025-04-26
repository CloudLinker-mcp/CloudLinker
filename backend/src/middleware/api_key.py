"""API key middleware for authentication.

This module provides middleware for validating API keys from request headers.
"""

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from ..settings import settings

class APIKeyMiddleware(BaseHTTPMiddleware):
    """Middleware for validating API keys.
    
    This middleware checks for the presence of an X-API-Key header in the request
    and validates it against the list of valid API keys in the settings.
    """
    
    async def dispatch(self, request: Request, call_next):
        """Process the request and validate the API key.
        
        Args:
            request: The incoming request
            call_next: The next middleware or route handler
            
        Returns:
            Response: The response from the next middleware or route handler
            
        Raises:
            HTTPException: If the API key is missing or invalid
        """
        # Skip API key validation for health check endpoint
        if request.url.path == "/health":
            return await call_next(request)
        
        # Get the API key from the request header
        api_key = request.headers.get("X-API-Key")
        
        # Check if the API key is present
        if not api_key:
            raise HTTPException(
                status_code=401,
                detail="API key is missing"
            )
        
        # Get the list of valid API keys from settings
        valid_api_keys = [key.strip() for key in settings.api_keys.split(",")]
        
        # Check if the API key is valid
        if api_key not in valid_api_keys:
            raise HTTPException(
                status_code=401,
                detail="Invalid API key"
            )
        
        # Continue to the next middleware or route handler
        return await call_next(request) 