Task 2: Install Python inside Ubuntu and execute a program

create ubuntu container
docker run -it --name ubuntu-python ubuntu:latest bash

update ubuntu package
apt-get update

Install python and verify version 
apt-get install -y python3
python3 --version

Inside ubuntu container craete program and execute 
echo 'print("Hello from Python inside Docker!")' > hello.py
python3 hello.py

exit

verify the installation inside container and not in local system
docker ps -a

Note: This installation is inside the container. It does not install Python on your Windows machine.