from fastapi import FastAPI
from .settings import settings
from .db import test_connection
from .routers import customers  # Import your new customers router

app = FastAPI()

# Include the customers router
app.include_router(customers.router, prefix="/customers", tags=["customers"])

@app.get("/health")
async def health():
    return {"ok": True}

@app.get("/test-db")
async def test_db():
    try:
        result = await test_connection()
        return {"db_status": "ok", "result": result}
    except Exception as e:
        return {"db_status": "error", "detail": str(e)}