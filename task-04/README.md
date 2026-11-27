Task 4: Container lifecycle — Run, Stop, Restart and Remove

run container in detached mode
docker run -d --name super30-nginx nginx:latest

verify the running container
docker ps

stop container
docker stop super30-nginx

again start container 
docker start super30-ngnix

to remove container first stop it 
docker stop super30-nginx

remove container 
docker rm super30-nginx

verify 
docker ps -a

