Task 1 - Pull the latest Ubuntu Docker image and run it interactively. Execute at least five Linux commands inside the container.


Pull Ubuntu image 
docker pull ubuntu:latest

Verify image
docker images

Run Ubuntu interactively
docker run -it --name ubuntu-task01 ubuntu:latest bash

Execute few linux commands inside ubuntu 

whoami
ls -l
pwd 
date
df -h

Exit the container 
exit

verify container status back in powershell 
docker ps -a

Task 1 completed : Ubuntu is downloaded, the container runs interactively, and i have demonstrated at least five Linux commands.