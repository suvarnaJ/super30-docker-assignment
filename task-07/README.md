Task 7: Build custom Docker image named super30-python-app

go to directory 

cd ..\task-07

craete app.py file 
create Dockerfile


FROM python:3.12-slim

WORKDIR /app

COPY app.py /app/app.py

CMD ["python", "app.py"]


build using required  image name
docker build -t super30-python-app .

run image
docker run --name super30-python-container super30-python-app

verify container
docker ps -a

