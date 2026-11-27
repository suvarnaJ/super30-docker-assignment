Task 6: Create a simple Python application and Dockerfile

create application folder
cd C:\Users\suvarna\Documents\super30-docker-assignment
cd task-06

create app.py file
create Dockerfile

build the image 
docker build -t super30-task06 .

run the container
docker run --name python-task06 super30-task06

verify
docker ps -a
docker images

