Task 19: Docker Compose — Run FastAPI and PostgreSQL together

create docker compose file and execute command in powershel
docker compose up --build

run in detached mode 
docker compose up --build -d 

verify services 
docker compose ps

check logs
docker compose logs

check only backend logs
docker compose logs backend

check only db logs
docker compose logs db 

http://localhost:8019/docs?utm_source=chatgpt.com#/default/db_test_db_test_get

stop services 
docker compose down

