# Project Architecture: CloudLinker

## Introduction
CloudLinker is a FastAPI-based application designed to manage customers and their data. This document outlines the architecture to help contributors understand the project structure.

## Folder Structure
src/
├── routers/    # Contains FastAPI routers (e.g., customers.py)
├── models/     # Pydantic models for validation
├── services/   # Business logic for reusability
├── utils/      # Helper functions or utilities
├── settings.py # Configuration management
├── db.py       # Database connection and ORM setup
└── main.py     # Entry point of the application


---

## Key Files

### `src/main.py`
- The entry point of the FastAPI application.
- Initializes and includes routers like `/customers` for modular organization.
- Handles general application setup.

### `src/routers/customers.py`
- Defines API routes for managing customer data.
- Handles operations such as creating and retrieving customers (`POST` and `GET`).

### `src/models/customer.py`
- Contains `CustomerCreate` and `CustomerRead` Pydantic models for input validation and structured API responses.

### `src/db.py`
- Manages the database connection and ORM (future integration planned with SQLAlchemy or similar).

### `src/settings.py`
- Centralized configuration file to handle environment variables and global settings.

---

## Application Flow

1. **Request Flow**:
   - User makes an API request via `/customers` endpoints (e.g., creating or fetching customers).
   - The request is processed by routers, validated using Pydantic models, and served from storage.

2. **Validation**:
   - Pydantic models ensure incoming data is valid, reducing the risk of errors.

3. **Database Interaction**:
   - Currently, an in-memory list stores data. Future integration will allow persistent storage using SQLAlchemy.

4. **Health Monitoring**:
   - `/health` endpoint provides server status.
   - `/test-db` verifies database connectivity.

---

## Future Plans
1. **Database Integration**:
   - Replace in-memory storage with PostgreSQL using SQLAlchemy.

2. **Additional Endpoints**:
   - Expand API functionality for advanced operations (e.g., updating and deleting customers).

3. **Improved Documentation**:
   - Add examples and diagrams for better understanding.

---

## Collaboration
All contributors are encouraged to review this guide before making changes. Updates to architecture should be documented here to maintain consistency.

---
