# Mini Backend - Week 3 Assignment

## Overview

This project demonstrates how to replace an in-memory data store with PostgreSQL running inside Docker while keeping the application architecture unchanged.

The goal of this assignment is to prove the benefit of layered architecture by changing only the repository implementation without modifying routes or services.

---

## Tech Stack

* Python 3.12
* FastAPI
* PostgreSQL 17
* Docker
* Docker Compose
* psycopg3
* python-dotenv

---

## Project Structure

```text
mini-backend/
│
├── app/
│   ├── models/
│   │   └── item.py
│   │
│   ├── repositories/
│   │   ├── memory_repository.py
│   │   └── postgres_repository.py
│   │
│   ├── routes/
│   │   └── item_routes.py
│   │
│   └── services/
│       └── item_service.py
│
├── postgres-init/
│   └── init.sql
│
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Architecture

```text
Client
   ↓
Routes
   ↓
Services
   ↓
Repository
   ↓
PostgreSQL
```

Only the repository implementation changed.

### Before

```text
Routes → Services → MemoryRepository
```

### After

```text
Routes → Services → PostgresRepository
```

Routes and services remained unchanged.

This demonstrates proper separation of concerns and layered architecture.

---

## Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/flyrank_db

POSTGRES_DB=flyrank_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

Example file:

`.env.example`

```env
DATABASE_URL=

POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd mini-backend
```

---

### Start Entire Stack

```bash
docker compose up --build
```

Run in background:

```bash
docker compose up -d --build
```

---

## API Documentation

Swagger UI:

```text
http://localhost:8000/docs
```

---

# API Endpoints

## Create Item

```http
POST /items
```

Request:

```json
{
  "name": "Laptop"
}
```

Response:

```json
{
  "id": 1,
  "name": "Laptop"
}
```

---

## Get All Items

```http
GET /items
```

Response:

```json
[
  {
    "id": 1,
    "name": "Laptop"
  }
]
```

---

# Database Verification

Connect to PostgreSQL:

```bash
docker exec -it mini-backend-db-1 psql -U postgres -d flyrank_db
```

List tables:

```sql
\dt
```

Check data:

```sql
SELECT * FROM items;
```

Example:

```text
 id |  name  |         created_at
----+--------+----------------------------
 1  | Laptop | 2026-07-18 16:56:49
```

---

# Persistence Verification

### Step 1

Create an item:

```bash
curl -X POST http://localhost:8000/items \
-H "Content-Type: application/json" \
-d '{"name":"Laptop"}'
```

### Step 2

Verify:

```bash
curl http://localhost:8000/items
```

Output:

```json
[
  {
    "id":1,
    "name":"Laptop"
  }
]
```

---

### Step 3

Stop containers:

```bash
docker compose down
```

---

### Step 4

Restart containers:

```bash
docker compose up -d
```

---

### Step 5

Verify data again:

```bash
curl http://localhost:8000/items
```

Output:

```json
[
  {
    "id":1,
    "name":"Laptop"
  }
]
```

The item still exists after restarting both the application and database containers, proving that PostgreSQL data persists through Docker volumes.

---

# Docker Volume

The PostgreSQL container uses a persistent Docker volume:

```yaml
volumes:
  postgres_data:
```

This prevents data loss when containers are restarted.

---

# Assignment Requirements Checklist

* [x] PostgreSQL running in Docker
* [x] Docker volume for persistent storage
* [x] Connection string stored in `.env`
* [x] `.env.example` committed
* [x] Database initialized using SQL script
* [x] Postgres repository implemented
* [x] Routes unchanged
* [x] Services unchanged
* [x] Entire stack starts using `docker compose up`
* [x] Persistence verified after restart

---

# Future Improvements

* Add Redis integration
* Add indexes and benchmark queries with `EXPLAIN ANALYZE`
* Add authentication
* Add database migrations using Alembic
* Add unit and integration tests
