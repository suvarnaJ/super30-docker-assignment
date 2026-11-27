Task 12: Automatically install dependencies using requirements.txt

build image
docker build -t super30-task12 .

run container
docker run -d --name task12-container -p 8012:8000 super30-task12

verify
http://localhost:8011/

Important concept: Docker layer caching
We copy requirements.txt and install packages before copying main.py.

Why?

If only main.py changes, Docker can reuse the dependency installation layer instead of installing all packages again.

This makes image builds faster.