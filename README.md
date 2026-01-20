# FastAPI Practice Monorepo

A FastAPI monorepo containing multiple backend practice projects focused on real-world API design, clean architecture, and interview-ready backend patterns.

This repository is intended for learning, experimentation, and best-practice backend implementation using FastAPI, SQLAlchemy, and PostgreSQL.

## 📦 About This Repository

This repo contains multiple FastAPI practice projects.
Each API:

- Lives in its own folder
- Is independently runnable
- Has its own database
- Follows clean backend architecture principles

## 🏗 Architecture Principles

- Route Layer – HTTP request/response handling
- Service Layer – Business logic & validation
- CRUD Layer – Database interaction only
- Models – SQLAlchemy ORM models
- No business logic in CRUD
- Strict separation of concerns

## 🧱 Tech Stack

- Backend Framework: FastAPI
- Language: Python
- Database: PostgreSQL
- ORM: SQLAlchemy
- Containerization: Docker & Docker Compose
- API Documentation: OpenAPI / Swagger UI

## 🚀 Running an API (Common Example)

Navigate to any API folder (example shown below):

```bash
cd example-api
```

Build and run the API using Docker:

```bash
docker compose up -d --build example_api
```

Running in detached mode (-d) helps prevent the database from being erased when updating code.

## 🌐 Access the API

Base URL:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

## 🔍 List All Docker Containers

```bash
docker ps -a
```

## 🛑 Stop Running Containers

```bash
docker compose down
```

## 🗑 Remove a Specific Container

```bash
docker rm <container_id>
```

## 🧹 Clean Docker (Remove All Containers)

**⚠ Warning:**  
This removes all containers.

```bash
docker rm $(docker ps -aq)
```

## 🧽 Clean Docker Completely (Images + Volumes)

**⚠ WARNING:**  
This will delete all containers, images, and volumes (databases will be erased).

```bash
docker system prune -a --volumes
```

Use this only when you want a fully fresh environment.

## 🎯 Purpose of This Monorepo

- Practice FastAPI backend development
- Learn clean, service-layer-driven architecture
- Understand ORM relationships and validations
- Prepare for backend interviews
- Build portfolio-ready backend projects

## 📝 Notes

- Each API is designed like a real backend assignment
- APIs are independent and Docker-based
- This monorepo is meant for learning and consistency, not shortcuts
