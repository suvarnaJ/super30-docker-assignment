Task 16: Connect two containers using a custom Docker network

docker network create super30-network

start python http server
docker run -d --name web-server --network super30-network python:3.12-slim python -m http.server 8000 --bind 0.0.0.0

start the client container
docker run --rm --network super30-network busybox wget -qO- http://web-server:8000

inspect network
docker network inspect super30-network

verify container
docker ps

cleanup
docker stop web-server
docker rm web-server
docker network rm super30-network