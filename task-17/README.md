Task 17: Create PostgreSQL Docker container

pull postgresql image
docker pull postgres:16

create postgress container
docker run -d --name super30-postgres -e POSTGRES_DB=studentdb -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin123 -p 5433:5432 postgres:16

verify container 
docker ps

check logs
docker logs super30-postgres

connect to postgress
docker exec -it super30-postgres psql -U admin -d studentdb

Execute commands
SELECT version();
SELECT current_database();
SELECT current_user

exit postgress 
\q

stop container
docker stop super30-postgres