Task 21: Implement FastAPI health check

Build image
docker build -t super30-task21 .

run container
docker run -d --name task21-container -p 8021:8000 super30-task21

verify 
docker ps

inspect docker health
docker inspect --format='{{.State.Health.Status}}' task21-container