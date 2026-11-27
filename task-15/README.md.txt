Task 15: Docker volume — Persistent data storage

create volume
docker volume create super30-data

verify volume data
docker volume ls

docker run --name volume-container-1 -v super30-data:/data alpine sh -c "echo 'Docker Volume Persistent Data - Super30' > /data/message.txt && cat /data/message.txt"

remove first container
docker rm volume-container-1

verify volume
docker volume ls

docker run --name volume-container-2 -v super30-data:/data alpine cat /data/message.txt

docker rm volume-container-2