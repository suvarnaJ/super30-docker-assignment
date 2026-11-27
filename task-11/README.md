Task 11: Dockerfile using WORKDIR, COPY, RUN, EXPOSE and CMD


docker build -t super30-task11 .

docker run -d --name task11-container -p 8011:8000 super30-task11

open http://localhost:8011/
