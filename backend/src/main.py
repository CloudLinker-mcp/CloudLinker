from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .settings import settings
from .db import test_connection
from .routers import customers, query  # Import the query router
from .middleware.api_key import APIKeyMiddleware  # Import the API key middleware
from .middleware.rate_limit import RateLimitMiddleware  # Import the rate limit middleware

app = FastAPI(
    title="CloudLinker API",
    description="A FastAPI platform that lets LLMs translate natural-language questions into SQL",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add rate limiting middleware (before API key middleware)
app.add_middleware(RateLimitMiddleware)

# Add API key middleware
app.add_middleware(APIKeyMiddleware)

# Include the routers
app.include_router(customers.router, prefix="/customers", tags=["customers"])
app.include_router(query.router, prefix="/query", tags=["query"])

@app.get("/health", tags=["health"])
async def health() -> dict[str, bool]:
    """Check if the API is running.
    
    Returns:
        dict: {"ok": true} if the API is healthy
    """
    return {"ok": True}

@app.get("/test-db", tags=["health"])
async def test_db() -> dict[str, str]:
    """Test database connection.
    
    Returns:
        dict: Database connection status
        
    Raises:
        HTTPException: If database connection fails
    """
    try:
        result = await test_connection()
        return {"db_status": "ok", "result": str(result)}   
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(e)}"
        )