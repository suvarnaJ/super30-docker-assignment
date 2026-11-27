Task 5: Pull three Docker images and display locally available images

pull three images 
docker pull ubuntu:latest
docker pull nginx:latest
docker pull python:3.12-slim

display images 
docker image ls

inspect images and display history
docker inspect ubuntu:latest
docker history ubuntu:latest