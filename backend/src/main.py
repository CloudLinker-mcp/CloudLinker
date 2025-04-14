from fastapi import FastAPI
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.settings import settings
app = FastAPI()

from src.db import test_connection
@app.get("/test-db")
async def test_db():
    try:
        result = await test_connection()
        return {"db_status": "ok", "result": result}
    except Exception as e:
        return {"db_status": "error", "detail": str(e)}

@app.get("/health")
async def health():
    return {"ok": True}