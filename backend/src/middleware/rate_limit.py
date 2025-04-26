"""Rate limiting middleware.

This module provides middleware for rate limiting API requests using a token bucket algorithm.
"""

import asyncio
import time
from typing import Dict, Tuple

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from ..utils.logger import get_logger

logger = get_logger(__name__)

# Rate limit configuration
REQUESTS_PER_MINUTE = 30
TOKEN_BUCKET_CAPACITY = REQUESTS_PER_MINUTE
TOKEN_REFILL_RATE = REQUESTS_PER_MINUTE / 60  # tokens per second

class TokenBucket:
    """Token bucket for rate limiting.
    
    This class implements a token bucket algorithm for rate limiting.
    """
    
    def __init__(self, capacity: int, refill_rate: float):
        """Initialize the token bucket.
        
        Args:
            capacity: Maximum number of tokens the bucket can hold
            refill_rate: Number of tokens to add per second
        """
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity
        self.last_update = time.time()
        self.lock = asyncio.Lock()
    
    async def consume(self) -> bool:
        """Consume a token from the bucket.
        
        Returns:
            bool: True if a token was consumed, False otherwise
        """
        async with self.lock:
            now = time.time()
            # Calculate time passed since last update
            time_passed = now - self.last_update
            # Add new tokens based on time passed
            new_tokens = time_passed * self.refill_rate
            self.tokens = min(self.capacity, self.tokens + new_tokens)
            self.last_update = now
            
            # Check if there are enough tokens
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False

class RateLimitMiddleware(BaseHTTPMiddleware):
    """Middleware for rate limiting API requests.
    
    This middleware limits the number of requests a client can make per minute
    using a token bucket algorithm.
    """
    
    def __init__(self, app, requests_per_minute: int = REQUESTS_PER_MINUTE):
        """Initialize the rate limit middleware.
        
        Args:
            app: The ASGI application
            requests_per_minute: Maximum number of requests per minute
        """
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.token_buckets: Dict[str, TokenBucket] = {}
        self.bucket_lock = asyncio.Lock()
    
    async def get_bucket(self, api_key: str) -> TokenBucket:
        """Get or create a token bucket for an API key.
        
        Args:
            api_key: The API key to get a bucket for
            
        Returns:
            TokenBucket: The token bucket for the API key
        """
        async with self.bucket_lock:
            if api_key not in self.token_buckets:
                self.token_buckets[api_key] = TokenBucket(
                    TOKEN_BUCKET_CAPACITY,
                    TOKEN_REFILL_RATE
                )
            return self.token_buckets[api_key]
    
    async def dispatch(self, request: Request, call_next):
        """Process the request and apply rate limiting.
        
        Args:
            request: The incoming request
            call_next: The next middleware or route handler
            
        Returns:
            Response: The response from the next middleware or route handler
            
        Raises:
            HTTPException: If the rate limit is exceeded
        """
        # Skip rate limiting for health check endpoint
        if request.url.path == "/health":
            return await call_next(request)
        
        # Get the API key from the request header
        api_key = request.headers.get("X-API-Key")
        
        # If no API key, skip rate limiting (will be caught by API key middleware)
        if not api_key:
            return await call_next(request)
        
        # Get the token bucket for the API key
        bucket = await self.get_bucket(api_key)
        
        # Try to consume a token
        if await bucket.consume():
            # Token consumed, proceed with the request
            return await call_next(request)
        else:
            # Rate limit exceeded
            logger.warning("rate_limit.exceeded", api_key_hash=hash(api_key))
            return JSONResponse(
                status_code=429,
                content={
                    "detail": "Rate limit exceeded. Please try again later.",
                    "retry_after": 60
                }
            ) 