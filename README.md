
# Super30 Docker Assignment

## Project Overview

This repository contains 23 Docker exercises.

The assignment covers:

- Docker Images
- Docker Containers
- Ubuntu
- Python
- Dockerfiles
- FastAPI
- Port Mapping
- Environment Variables
- Docker Volumes
- Docker Networking
- PostgreSQL
- Docker Compose
- Health Checks
- CRUD Operations

## Technology Stack

- Docker Desktop
- Python 3.12
- FastAPI
- PostgreSQL 16
- SQLAlchemy
- NGINX
- HTML, CSS, JavaScript
- Docker Compose
- Windows PowerShell
- VS Code

## Assignment Structure

Tasks 01-05: Docker Fundamentals

Tasks 06-12: Dockerfiles and FastAPI

Tasks 13-16: Environment Variables,
Volumes and Networking

Tasks 17-19: PostgreSQL and Docker Compose

Tasks 20-22: Three-Tier Application and CRUD

Task 23: Student Management System

## Final Project Architecture

Frontend (NGINX)
       |
       v
FastAPI Backend
       |
       v
PostgreSQL Database

All services run as separate Docker containers.

Docker Compose manages the services.

A named Docker volume provides persistent database storage.

## How to Run Final Project

1. Install Docker Desktop.

2. Clone repository:

   git clone https://github.com/YOUR_USERNAME/super30-docker-assignment.git

3. Navigate to final project:

   cd super30-docker-assignment/task-23

4. Create .env using .env.example
   and configure local database credentials.

5. Start application:

   docker compose up --build

6. Open frontend:

   http://localhost:8083

7. Open Swagger:

   http://localhost:8023/docs

8. Check health:

   http://localhost:8023/health

## Docker Commands

docker images

docker ps

docker ps -a

docker build

docker run

docker stop

docker start

docker rm

docker volume ls

docker network ls

docker compose up --build

docker compose down

## Final Project Features

- Add Students
- View Students
- Update Students
- Delete Students
- Search Students
- PostgreSQL Database
- Persistent Docker Volume
- Custom Docker Network
- Health Check
- Environment Configuration

## Author

Super30 Docker Assignment

## YouTube Demonstration

Video Link: Add your YouTube video URL here.
