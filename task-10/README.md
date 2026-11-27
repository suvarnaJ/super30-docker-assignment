Task 10: Run the same FastAPI image on host port 5000

to stop and remove previous container
docker stop super30-api-container

docker rm super30-api-container

to run same image on different host port
docker run -d --name super30-api-5000 -p 5000:8000 super30-api

The application itself has not changed. Only the host port mapping has changed.
http://localhost:5000/
http://localhost:5000/docs
http://localhost:5000/students