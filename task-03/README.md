Task 3: Create Ubuntu container with a custom name

run container
docker run -it --name super30-linux ubuntu:latest bash

Execute below commands inside container
echo "Welcome to Super30 Docker Assignment"
whoami
pwd
exit

Verify the container name
docker ps -a

start the container again 
docker start super30-linux

Verify container
docker ps

Note: The container was created only once. docker start starts that existing container again.