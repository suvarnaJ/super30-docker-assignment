Task 23 - Build a Student Management System using Docker

docker compose up --build

one command startup 

Docker Compose will:
1. Build the frontend image.
2. Build the FastAPI backend image.
3. Download PostgreSQL.
4. Create the custom network.
5. Create the persistent database volume.
6. Start PostgreSQL.
7. Wait for PostgreSQL to become healthy.
8. Start FastAPI.
9. Wait for FastAPI to become healthy.
10. Start the frontend.

check services
docker compose ps

check only logs
docker compose logs

check only backend logs
docker compose logs backend

check only db 
docker compose logs db

open application -> http://localhost:8083/

to stop the application 
docker compose down

start again
docker compose up -d

open the frontend again , record still exist.

verify the volume 
docker volume ls

should see a volume with a name similar to:
task-23_student_data


This proves database persistence.

Important: Never use docker compose down -v during your persistence demonstration. That command deletes the named volume too.


