# CloudLinker Backend

A FastAPI + PostgreSQL platform that lets LLMs translate natural-language questions into SQL.

## Features

- FastAPI with async SQLAlchemy + asyncpg
- PostgreSQL database with Alembic migrations
- Pydantic data validation
- Pytest with async support
- GitLab CI integration
- Natural language to SQL translation
- API key authentication
- Docker support

## Quick Start

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd CloudLinker/backend
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file:
   ```bash
   cp .env.template .env
   # Edit .env with your database credentials and API keys
   ```

4. Run database migrations:
   ```bash
   alembic upgrade head
   ```

5. Start the development server:
   ```bash
   uvicorn src.main:app --reload
   ```

6. Visit the API documentation:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Running with Docker

1. Build and start the services:
   ```bash
   docker compose up -d
   ```

2. Run database migrations:
   ```bash
   docker compose exec api alembic upgrade head
   ```

3. Check the logs:
   ```bash
   docker compose logs -f api db
   ```

4. Stop the services:
   ```bash
   docker compose down
   ```

## Development

### Running Tests

```bash
PYTHONPATH=. pytest
```

### Creating Database Migrations

```bash
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

### Project Structure

```
src/
├── __init__.py
├── main.py              # FastAPI application entry point
├── settings.py          # Environment configuration
├── db.py               # Database connection and session management
├── models/             # SQLAlchemy models
├── schemas/            # Pydantic schemas
├── services/           # Business logic layer
├── middleware/         # Middleware components
└── routers/            # API endpoints

tests/                  # Test suite
alembic/               # Database migrations
docs/                  # Documentation
```

## API Endpoints

- `GET /health` - Health check
- `GET /test-db` - Database connection test
- `POST /customers` - Create customer
- `GET /customers` - List customers
- `POST /query` - Translate and execute natural language query

### Authentication

All endpoints except `/health` require an API key to be provided in the `X-API-Key` header.

## Contributing

1. Create a feature branch
2. Make your changes
3. Run tests
4. Submit a merge request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 