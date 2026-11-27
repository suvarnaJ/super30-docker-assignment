Task 18: Connect FastAPI with PostgreSQL using separate containers

Build fastapi image
docker build -t super30-task18-api .

create network
docker network create task18-network

run postgresql
docker run -d --name db --network task18-network -e POSTGRES_DB=studentdb -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin123 postgres:16

docker logs db

run fast api container
docker run -d --name super30-api-18 --network task18-network -p 8018:8000 --env-file .env super30-task18-api

verify both containers
docker ps

http://localhost:8018/db-test?utm_source=chatgpt.com