Task 13: Pass environment variables to a Docker container

docker build -t super30-task13 .

docker run -d --name task13-container -p 8013:8000 -e APP_NAME="Super30 Student API" -e APP_ENV="Docker" super30-task13

-e passes env variable 
app_name contains application name
app_env contains application environment

verify environment variable
docker exec task13-container printenv
or 
docker exec task13-container printenv APP_NAME